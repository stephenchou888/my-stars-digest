import os
import sys
import json
import re
import requests
from datetime import datetime, timezone

# 基础配置：优先使用 GitHub Actions 内置永不过期的 GITHUB_TOKEN，其次才是 GH_PAT
GH_TOKEN = (os.getenv("GITHUB_TOKEN") or os.getenv("GH_PAT") or "").strip()
# 固定使用指定用户名拉取 Star（避免受运行环境 GITHUB_ACTOR 影响）
USERNAME = "stephenchou888"
REPO_NAME = "my-stars-digest"
PAGES_URL = f"https://{USERNAME}.github.io/{REPO_NAME}/"
STAR_API = f"https://api.github.com/users/{USERNAME}/starred"

HEADERS = {
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "GitHub-Stars-Digest"
}
if GH_TOKEN:
    HEADERS["Authorization"] = f"Bearer {GH_TOKEN}"

CACHE_FILE = "data/cache.json"
DASHBOARD_DATA_FILE = "data/dashboard.json"
WEB_DASHBOARD_DATA_FILE = "web/public/data/dashboard.json"
NOW = datetime.now(timezone.utc)


def github_get(url, timeout=15):
    """带自动回退机制的 GitHub API 请求：若 Token 过期返回 401，自动剥离无效 Token 重试"""
    resp = requests.get(url, headers=HEADERS, timeout=timeout)
    if resp.status_code == 401 and "Authorization" in HEADERS:
        print("⚠️ 检测到当前 Token 无效或已过期 (HTTP 401)，已自动切换为免 Token 模式继续请求...")
        HEADERS.pop("Authorization", None)
        resp = requests.get(url, headers=HEADERS, timeout=timeout)
    return resp


def load_cache():
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def save_cache(cache):
    os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)


def translate_to_zh(text):
    """免 Key 的安全开放翻译引擎（仅传输公开技术文档，无任何个人数据）"""
    if not text or not text.strip():
        return ""
    zh_chars = len(re.findall(r'[\u4e00-\u9fa5]', text))
    if zh_chars > 8 or (len(text) > 0 and zh_chars / len(text) > 0.3):
        return text

    url = "https://translate.googleapis.com/translate_a/single"
    params = {
        "client": "gtx",
        "sl": "auto",
        "tl": "zh-CN",
        "dt": "t",
        "q": text[:2000]
    }
    try:
        resp = requests.get(url, params=params, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            translated = "".join([seg[0] for seg in data[0] if seg and seg[0]])
            return translated.strip()
    except Exception as e:
        print(f"翻译异常: {e}")
    return text


def classify_repo(repo_info):
    """基于仓库的 Topics 标签、名称与描述进行多维度自动聚类"""
    text_corpus = (
        repo_info.get("name", "") + " " +
        (repo_info.get("description") or "") + " " +
        " ".join(repo_info.get("topics", []))
    ).lower()

    if any(k in text_corpus for k in ["ai", "llm", "agent", "gpt", "claude", "ollama", "dify", "chatgpt", "langchain", "prompt", "vision", "model", "mcp", "deepseek", "openai"]):
        return "🤖 AI 与智能体生态"
    elif any(k in text_corpus for k in ["proxy", "v2ray", "xray", "clash", "sing-box", "hysteria", "vpn", "trojan", "passwall", "network", "tunnel", "gfw", "sub-store"]):
        return "🌐 网络与代理技术"
    elif any(k in text_corpus for k in ["music", "video", "media", "player", "audio", "download", "bilibili", "youtube", "podcast", "tv", "iptv", "spotify"]):
        return "🎬 影音媒体与下载"
    elif any(k in text_corpus for k in ["office", "pdf", "markdown", "editor", "docs", "sheets", "photoshop", "desktop", "ui", "notes", "notion", "obsidian", "epub", "book"]):
        return "📝 效率办公与创作"
    elif any(k in text_corpus for k in ["docker", "linux", "cli", "terminal", "tool", "devtools", "extension", "utility", "script", "macos", "windows", "shell", "git"]):
        return "🛠️ 系统与开发者工具"
    else:
        return "📦 实用开源精选"


def check_health(repo):
    """判断维护健康状态并返回 (status, reason, days_since_push)"""
    pushed_at_str = repo.get("pushed_at")
    days = 9999
    if pushed_at_str:
        try:
            pushed_at = datetime.fromisoformat(pushed_at_str.replace("Z", "+00:00"))
            days = max(0, (NOW - pushed_at).days)
        except Exception:
            days = 9999

    if repo.get("archived", False):
        return "abandoned", "作者已正式归档 (Archived)", days

    if not pushed_at_str:
        return "abandoned", "无代码提交记录", days

    if days > 365:
        return "abandoned", f"超过 {days} 天无代码提交", days
    elif days > 90:
        return "stale", f"近 {days} 天未更新（低频维护）", days
    return "active", f"{days} 天前有活跃更新", days


def extract_and_summarize_highlights(release_notes):
    """提取核心条目并自动翻译为简洁中文"""
    if not release_notes or not release_notes.strip():
        return "该版本未提供详细更新说明。"

    pattern = r"(?i)#{1,4}\s*(features|what's changed|new|highlights|changelog)(.*?)(?=#{1,4}\s|\Z)"
    match = re.search(pattern, release_notes, re.DOTALL)
    target_text = match.group(2) if match else release_notes

    valid_lines = []
    for line in target_text.splitlines():
        line = line.strip()
        if line.startswith(("- ", "* ")) and len(line) > 5:
            lower = line.lower()
            if not any(noise in lower for noise in ["chore:", "ci:", "bump", "typo", "merge pull request"]):
                cleaned = re.sub(r'\(?@[\w-]+\)?', '', line).strip()
                valid_lines.append(cleaned)
        if len(valid_lines) >= 3:
            break

    if valid_lines:
        combined_en = "\n".join(valid_lines)
        zh_text = translate_to_zh(combined_en)
        return zh_text

    clean_text = re.sub(r'#+\s*', '', release_notes).strip()[:250]
    return translate_to_zh(clean_text)


def check_repo_updates(repo, cache):
    full_name = repo["full_name"]
    url = f"https://api.github.com/repos/{full_name}/releases/latest"
    resp = github_get(url)
    if resp.status_code != 200:
        return None

    data = resp.json()
    tag_name = data.get("tag_name")
    published_at_str = data.get("published_at")
    if not tag_name or not published_at_str:
        return None

    published_at = datetime.fromisoformat(published_at_str.replace("Z", "+00:00"))
    if (NOW - published_at).days > 30:
        return None

    cached = cache.get(full_name, {})
    if cached.get("last_tag") == tag_name and cached.get("summary_zh"):
        return {
            "tag": tag_name,
            "url": data.get("html_url"),
            "published_at": published_at_str[:10],
            "desc_zh": cached.get("desc_zh", ""),
            "summary_zh": cached.get("summary_zh", ""),
            "raw_body": data.get("body") or ""
        }

    raw_desc = repo.get("description") or "暂无项目描述"
    desc_zh = translate_to_zh(raw_desc)
    raw_body = data.get("body") or ""
    summary_zh = extract_and_summarize_highlights(raw_body)

    cache[full_name] = {
        "last_tag": tag_name,
        "desc_zh": desc_zh,
        "summary_zh": summary_zh,
        "updated_at": NOW.isoformat()
    }

    return {
        "tag": tag_name,
        "url": data.get("html_url"),
        "published_at": published_at_str[:10],
        "desc_zh": desc_zh,
        "summary_zh": summary_zh,
        "raw_body": raw_body
    }


def generate_markdown(active_updates, abandoned_repos, total_count):
    date_str = NOW.strftime("%Y-%m-%d")

    categories = {}
    for item in active_updates:
        cat = item["category"]
        categories.setdefault(cat, []).append(item)

    md = [
        f"# 📡 Starred 项目雷达看板",
        f"> 🖥️ **交互式管理看板 (shadcn/ui)**：[👉 点击进入在线雷达看板 ({PAGES_URL})]({PAGES_URL})\n",
        f"> **生成时间**：`{date_str}` ｜ **关注项目总数**：`{total_count}` ｜ **本期更新**：`{len(active_updates)}` ｜ **弃坑预警**：`{len(abandoned_repos)}`\n",
        "| 统计指标 | 数量 | 状态提示 |",
        "| :--- | :---: | :--- |",
        f"| 🌟 总关注库 | **{total_count}** | [进入 shadcn 在线看板管理]({PAGES_URL}) |",
        f"| 🚀 近期有更新 | **{len(active_updates)}** | 涵盖 {len(categories)} 个分类 |",
        f"| 🛑 建议清理/弃坑 | **{len(abandoned_repos)}** | 建议取消 Star 保持关注列表整洁 |",
        "\n---",
        "## 🧭 领域分类速览导航\n"
    ]

    for cat, items in categories.items():
        anchor = cat.replace(' ', '-').replace('🤖', '').replace('🌐', '').replace('🎬', '').replace('📝', '').replace('🛠️', '').replace('📦', '').strip()
        md.append(f"- [{cat} ({len(items)})](#{anchor})")

    md.append("\n---")

    for cat, items in categories.items():
        anchor = cat.replace(' ', '-').replace('🤖', '').replace('🌐', '').replace('🎬', '').replace('📝', '').replace('🛠️', '').replace('📦', '').strip()
        md.append(f"\n## <span id=\"{anchor}\">{cat}</span>\n")
        for item in items:
            lang = item['language']
            stars = item['stars']
            tag = item['tag']

            md.append(f"### 📦 [{item['repo']}]({item['html_url']})")
            md.append(
                f"`⭐ Stars: {stars:,}` &nbsp;|&nbsp; "
                f"`💻 语言: {lang}` &nbsp;|&nbsp; "
                f"`🏷️ 最新版本: [{tag}]({item['release_url']}) ({item['published_at']})`\n"
            )
            md.append(f"> **简介**：{item['desc_zh']}\n")
            md.append(f"**💡 核心亮点更新 (中文)**：\n{item['summary_zh']}\n")

            if item['raw_body'].strip():
                md.append("<details>")
                md.append("<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>\n")
                md.append("```markdown")
                md.append(item['raw_body'][:1500].strip())
                md.append("```")
                md.append("</details>\n")
            md.append("---")

    md.append("\n## 🛑 建议清理 / 放弃维护项目\n")
    md.append("<details>")
    md.append(f"<summary>⚠️ 点击展开已放弃维护或超过 1 年停更的仓库清单 ({len(abandoned_repos)} 个)</summary>\n")
    md.append("| 仓库名称 | Stars | 状态说明 | 操作建议 |")
    md.append("| :--- | :---: | :--- | :---: |")
    for item in abandoned_repos:
        md.append(f"| [{item['repo']}]({item['html_url']}) | {item['stars']:,} | {item['reason']} | [进入取消 Star]({item['html_url']}) |")
    md.append("</details>\n")

    return "\n".join(md)


SHADCN_WEB_FILES = {
    "web/.gitignore": """node_modules/
dist/
.DS_Store
*.local
""",
    "web/package.json": """{
  "name": "stars-radar-shadcn",
  "private": true,
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "@radix-ui/react-dialog": "^1.1.2",
    "@radix-ui/react-slot": "^1.1.0",
    "@radix-ui/react-tabs": "^1.1.1",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "lucide-react": "^0.460.0",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "tailwind-merge": "^2.5.4"
  },
  "devDependencies": {
    "@types/react": "^18.3.12",
    "@types/react-dom": "^18.3.1",
    "@vitejs/plugin-react": "^4.3.3",
    "autoprefixer": "^10.4.20",
    "postcss": "^8.4.49",
    "tailwindcss": "^3.4.15",
    "typescript": "~5.6.2",
    "vite": "^5.4.11"
  }
}
""",
    "web/components.json": """{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "new-york",
  "rsc": false,
  "tsx": true,
  "tailwind": {
    "config": "tailwind.config.js",
    "css": "src/index.css",
    "baseColor": "zinc",
    "cssVariables": true,
    "prefix": ""
  },
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils",
    "ui": "@/components/ui"
  }
}
""",
    "web/tsconfig.json": """{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "isolatedModules": true,
    "moduleDetection": "force",
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": false,
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": ["src"]
}
""",
    "web/vite.config.ts": """import { fileURLToPath, URL } from "node:url"
import { defineConfig } from "vite"
import react from "@vitejs/plugin-react"

export default defineConfig({
  base: "./",
  plugins: [react()],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
})
""",
    "web/postcss.config.js": """export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
""",
    "web/tailwind.config.js": """/** @type {import('tailwindcss').Config} */
export default {
  darkMode: ["class"],
  content: ["./index.html", "./src/**/*.{ts,tsx,js,jsx}"],
  theme: {
    extend: {
      colors: {
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        primary: {
          DEFAULT: "hsl(var(--primary))",
          foreground: "hsl(var(--primary-foreground))",
        },
        secondary: {
          DEFAULT: "hsl(var(--secondary))",
          foreground: "hsl(var(--secondary-foreground))",
        },
        destructive: {
          DEFAULT: "hsl(var(--destructive))",
          foreground: "hsl(var(--destructive-foreground))",
        },
        muted: {
          DEFAULT: "hsl(var(--muted))",
          foreground: "hsl(var(--muted-foreground))",
        },
        accent: {
          DEFAULT: "hsl(var(--accent))",
          foreground: "hsl(var(--accent-foreground))",
        },
        popover: {
          DEFAULT: "hsl(var(--popover))",
          foreground: "hsl(var(--popover-foreground))",
        },
        card: {
          DEFAULT: "hsl(var(--card))",
          foreground: "hsl(var(--card-foreground))",
        },
      },
      borderRadius: {
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)",
      },
    },
  },
  plugins: [],
}
""",
    "web/index.html": """<!doctype html>
<html lang="zh-CN" class="dark">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>📡 Starred 项目雷达看板 · shadcn/ui</title>
  </head>
  <body class="min-h-screen bg-background text-foreground antialiased selection:bg-primary selection:text-primary-foreground">
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
""",
    "web/src/index.css": """@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 240 10% 3.9%;
    --card: 0 0% 100%;
    --card-foreground: 240 10% 3.9%;
    --popover: 0 0% 100%;
    --popover-foreground: 240 10% 3.9%;
    --primary: 240 5.9% 10%;
    --primary-foreground: 0 0% 98%;
    --secondary: 240 4.8% 95.9%;
    --secondary-foreground: 240 5.9% 10%;
    --muted: 240 4.8% 95.9%;
    --muted-foreground: 240 3.8% 46.1%;
    --accent: 240 4.8% 95.9%;
    --accent-foreground: 240 5.9% 10%;
    --destructive: 0 84.2% 60.2%;
    --destructive-foreground: 0 0% 98%;
    --border: 240 5.9% 90%;
    --input: 240 5.9% 90%;
    --ring: 240 5.9% 10%;
    --radius: 0.65rem;
  }

  .dark {
    --background: 240 10% 3.9%;
    --foreground: 0 0% 98%;
    --card: 240 10% 5.5%;
    --card-foreground: 0 0% 98%;
    --popover: 240 10% 5.5%;
    --popover-foreground: 0 0% 98%;
    --primary: 0 0% 98%;
    --primary-foreground: 240 5.9% 10%;
    --secondary: 240 3.7% 13.5%;
    --secondary-foreground: 0 0% 98%;
    --muted: 240 3.7% 13.5%;
    --muted-foreground: 240 5% 64.9%;
    --accent: 240 3.7% 15.9%;
    --accent-foreground: 0 0% 98%;
    --destructive: 0 62.8% 30.6%;
    --destructive-foreground: 0 0% 98%;
    --border: 240 3.7% 15.9%;
    --input: 240 3.7% 15.9%;
    --ring: 240 4.9% 83.9%;
  }
}

@layer base {
  * {
    @apply border-border;
  }
  body {
    @apply bg-background text-foreground;
    font-feature-settings: "rlig" 1, "calt" 1;
  }
}
""",
    "web/src/lib/utils.ts": """import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
""",
    "web/src/components/ui/button.tsx": """import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { cva, type VariantProps } from "class-variance-authority"
import { cn } from "@/lib/utils"

const buttonVariants = cva(
  "inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground shadow hover:bg-primary/90",
        destructive: "bg-destructive text-destructive-foreground shadow-sm hover:bg-destructive/90",
        outline: "border border-input bg-background shadow-sm hover:bg-accent hover:text-accent-foreground",
        secondary: "bg-secondary text-secondary-foreground shadow-sm hover:bg-secondary/80",
        ghost: "hover:bg-accent hover:text-accent-foreground",
        link: "text-primary underline-offset-4 hover:underline",
      },
      size: {
        default: "h-9 px-4 py-2",
        sm: "h-8 rounded-md px-3 text-xs",
        lg: "h-10 rounded-md px-8",
        icon: "h-9 w-9",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  asChild?: boolean
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : "button"
    return (
      <Comp
        className={cn(buttonVariants({ variant, size, className }))}
        ref={ref}
        {...props}
      />
    )
  }
)
Button.displayName = "Button"

export { Button, buttonVariants }
""",
    "web/src/components/ui/card.tsx": """import * as React from "react"
import { cn } from "@/lib/utils"

const Card = React.forwardRef<HTMLDivElement, React.HTMLAttributes<HTMLDivElement>>(
  ({ className, ...props }, ref) => (
    <div
      ref={ref}
      className={cn("rounded-xl border bg-card text-card-foreground shadow-sm", className)}
      {...props}
    />
  )
)
Card.displayName = "Card"

const CardHeader = React.forwardRef<HTMLDivElement, React.HTMLAttributes<HTMLDivElement>>(
  ({ className, ...props }, ref) => (
    <div ref={ref} className={cn("flex flex-col space-y-1.5 p-5", className)} {...props} />
  )
)
CardHeader.displayName = "CardHeader"

const CardTitle = React.forwardRef<HTMLParagraphElement, React.HTMLAttributes<HTMLHeadingElement>>(
  ({ className, ...props }, ref) => (
    <h3 ref={ref} className={cn("font-semibold leading-none tracking-tight", className)} {...props} />
  )
)
CardTitle.displayName = "CardTitle"

const CardDescription = React.forwardRef<HTMLParagraphElement, React.HTMLAttributes<HTMLParagraphElement>>(
  ({ className, ...props }, ref) => (
    <p ref={ref} className={cn("text-sm text-muted-foreground", className)} {...props} />
  )
)
CardDescription.displayName = "CardDescription"

const CardContent = React.forwardRef<HTMLDivElement, React.HTMLAttributes<HTMLDivElement>>(
  ({ className, ...props }, ref) => (
    <div ref={ref} className={cn("p-5 pt-0", className)} {...props} />
  )
)
CardContent.displayName = "CardContent"

const CardFooter = React.forwardRef<HTMLDivElement, React.HTMLAttributes<HTMLDivElement>>(
  ({ className, ...props }, ref) => (
    <div ref={ref} className={cn("flex items-center p-5 pt-0", className)} {...props} />
  )
)
CardFooter.displayName = "CardFooter"

export { Card, CardHeader, CardFooter, CardTitle, CardDescription, CardContent }
""",
    "web/src/components/ui/badge.tsx": """import * as React from "react"
import { cva, type VariantProps } from "class-variance-authority"
import { cn } from "@/lib/utils"

const badgeVariants = cva(
  "inline-flex items-center rounded-md border px-2.5 py-0.5 text-xs font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2",
  {
    variants: {
      variant: {
        default: "border-transparent bg-primary text-primary-foreground shadow hover:bg-primary/80",
        secondary: "border-transparent bg-secondary text-secondary-foreground hover:bg-secondary/80",
        destructive: "border-transparent bg-destructive text-destructive-foreground shadow hover:bg-destructive/80",
        outline: "text-foreground",
        success: "border-emerald-500/30 bg-emerald-500/15 text-emerald-600 dark:text-emerald-400",
        warning: "border-amber-500/30 bg-amber-500/15 text-amber-600 dark:text-amber-400",
        danger: "border-rose-500/30 bg-rose-500/15 text-rose-600 dark:text-rose-400",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  }
)

export interface BadgeProps
  extends React.HTMLAttributes<HTMLDivElement>,
    VariantProps<typeof badgeVariants> {}

function Badge({ className, variant, ...props }: BadgeProps) {
  return <div className={cn(badgeVariants({ variant }), className)} {...props} />
}

export { Badge, badgeVariants }
""",
    "web/src/components/ui/input.tsx": """import * as React from "react"
import { cn } from "@/lib/utils"

export interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {}

const Input = React.forwardRef<HTMLInputElement, InputProps>(
  ({ className, type, ...props }, ref) => {
    return (
      <input
        type={type}
        className={cn(
          "flex h-9 w-full rounded-md border border-input bg-transparent px-3 py-1 text-sm shadow-sm transition-colors file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-50",
          className
        )}
        ref={ref}
        {...props}
      />
    )
  }
)
Input.displayName = "Input"

export { Input }
""",
    "web/src/components/ui/tabs.tsx": """import * as React from "react"
import * as TabsPrimitive from "@radix-ui/react-tabs"
import { cn } from "@/lib/utils"

const Tabs = TabsPrimitive.Root

const TabsList = React.forwardRef<
  React.ElementRef<typeof TabsPrimitive.List>,
  React.ComponentPropsWithoutRef<typeof TabsPrimitive.List>
>(({ className, ...props }, ref) => (
  <TabsPrimitive.List
    ref={ref}
    className={cn(
      "inline-flex h-10 items-center justify-center rounded-lg bg-muted p-1 text-muted-foreground",
      className
    )}
    {...props}
  />
))
TabsList.displayName = TabsPrimitive.List.displayName

const TabsTrigger = React.forwardRef<
  React.ElementRef<typeof TabsPrimitive.Trigger>,
  React.ComponentPropsWithoutRef<typeof TabsPrimitive.Trigger>
>(({ className, ...props }, ref) => (
  <TabsPrimitive.Trigger
    ref={ref}
    className={cn(
      "inline-flex items-center justify-center whitespace-nowrap rounded-md px-3 py-1.5 text-sm font-medium ring-offset-background transition-all focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 data-[state=active]:bg-background data-[state=active]:text-foreground data-[state=active]:shadow",
      className
    )}
    {...props}
  />
))
TabsTrigger.displayName = TabsPrimitive.Trigger.displayName

const TabsContent = React.forwardRef<
  React.ElementRef<typeof TabsPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof TabsPrimitive.Content>
>(({ className, ...props }, ref) => (
  <TabsPrimitive.Content
    ref={ref}
    className={cn(
      "mt-3 ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2",
      className
    )}
    {...props}
  />
))
TabsContent.displayName = TabsPrimitive.Content.displayName

export { Tabs, TabsList, TabsTrigger, TabsContent }
""",
    "web/src/components/ui/table.tsx": """import * as React from "react"
import { cn } from "@/lib/utils"

const Table = React.forwardRef<HTMLTableElement, React.HTMLAttributes<HTMLTableElement>>(
  ({ className, ...props }, ref) => (
    <div className="relative w-full overflow-auto">
      <table ref={ref} className={cn("w-full caption-bottom text-sm", className)} {...props} />
    </div>
  )
)
Table.displayName = "Table"

const TableHeader = React.forwardRef<HTMLTableSectionElement, React.HTMLAttributes<HTMLTableSectionElement>>(
  ({ className, ...props }, ref) => (
    <thead ref={ref} className={cn("[&_tr]:border-b", className)} {...props} />
  )
)
TableHeader.displayName = "TableHeader"

const TableBody = React.forwardRef<HTMLTableSectionElement, React.HTMLAttributes<HTMLTableSectionElement>>(
  ({ className, ...props }, ref) => (
    <tbody ref={ref} className={cn("[&_tr:last-child]:border-0", className)} {...props} />
  )
)
TableBody.displayName = "TableBody"

const TableRow = React.forwardRef<HTMLTableRowElement, React.HTMLAttributes<HTMLTableRowElement>>(
  ({ className, ...props }, ref) => (
    <tr
      ref={ref}
      className={cn("border-b transition-colors hover:bg-muted/50 data-[state=selected]:bg-muted", className)}
      {...props}
    />
  )
)
TableRow.displayName = "TableRow"

const TableHead = React.forwardRef<HTMLTableCellElement, React.ThHTMLAttributes<HTMLTableCellElement>>(
  ({ className, ...props }, ref) => (
    <th
      ref={ref}
      className={cn(
        "h-10 px-3 text-left align-middle font-medium text-muted-foreground [&:has([role=checkbox])]:pr-0",
        className
      )}
      {...props}
    />
  )
)
TableHead.displayName = "TableHead"

const TableCell = React.forwardRef<HTMLTableCellElement, React.TdHTMLAttributes<HTMLTableCellElement>>(
  ({ className, ...props }, ref) => (
    <td ref={ref} className={cn("p-3 align-middle [&:has([role=checkbox])]:pr-0", className)} {...props} />
  )
)
TableCell.displayName = "TableCell"

export { Table, TableHeader, TableBody, TableHead, TableRow, TableCell }
""",
    "web/src/components/ui/dialog.tsx": """import * as React from "react"
import * as DialogPrimitive from "@radix-ui/react-dialog"
import { X } from "lucide-react"
import { cn } from "@/lib/utils"

const Dialog = DialogPrimitive.Root
const DialogTrigger = DialogPrimitive.Trigger
const DialogPortal = DialogPrimitive.Portal
const DialogClose = DialogPrimitive.Close

const DialogOverlay = React.forwardRef<
  React.ElementRef<typeof DialogPrimitive.Overlay>,
  React.ComponentPropsWithoutRef<typeof DialogPrimitive.Overlay>
>(({ className, ...props }, ref) => (
  <DialogPrimitive.Overlay
    ref={ref}
    className={cn(
      "fixed inset-0 z-50 bg-black/70 backdrop-blur-sm data-[state=open]:animate-in data-[state=closed]:animate-out",
      className
    )}
    {...props}
  />
))
DialogOverlay.displayName = DialogPrimitive.Overlay.displayName

const DialogContent = React.forwardRef<
  React.ElementRef<typeof DialogPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof DialogPrimitive.Content>
>(({ className, children, ...props }, ref) => (
  <DialogPortal>
    <DialogOverlay />
    <DialogPrimitive.Content
      ref={ref}
      className={cn(
        "fixed left-[50%] top-[50%] z-50 grid w-[95vw] max-w-2xl translate-x-[-50%] translate-y-[-50%] gap-4 border bg-background p-6 shadow-xl duration-200 rounded-xl max-h-[85vh] overflow-y-auto",
        className
      )}
      {...props}
    >
      {children}
      <DialogPrimitive.Close className="absolute right-4 top-4 rounded-sm opacity-70 ring-offset-background transition-opacity hover:opacity-100 focus:outline-none focus:ring-2 focus:ring-ring">
        <X className="h-4 w-4" />
        <span className="sr-only">Close</span>
      </DialogPrimitive.Close>
    </DialogPrimitive.Content>
  </DialogPortal>
))
DialogContent.displayName = DialogPrimitive.Content.displayName

const DialogHeader = ({ className, ...props }: React.HTMLAttributes<HTMLDivElement>) => (
  <div className={cn("flex flex-col space-y-1.5 text-left", className)} {...props} />
)
DialogHeader.displayName = "DialogHeader"

const DialogTitle = React.forwardRef<
  React.ElementRef<typeof DialogPrimitive.Title>,
  React.ComponentPropsWithoutRef<typeof DialogPrimitive.Title>
>(({ className, ...props }, ref) => (
  <DialogPrimitive.Title
    ref={ref}
    className={cn("text-lg font-semibold leading-none tracking-tight", className)}
    {...props}
  />
))
DialogTitle.displayName = DialogPrimitive.Title.displayName

const DialogDescription = React.forwardRef<
  React.ElementRef<typeof DialogPrimitive.Description>,
  React.ComponentPropsWithoutRef<typeof DialogPrimitive.Description>
>(({ className, ...props }, ref) => (
  <DialogPrimitive.Description
    ref={ref}
    className={cn("text-sm text-muted-foreground", className)}
    {...props}
  />
))
DialogDescription.displayName = DialogPrimitive.Description.displayName

export {
  Dialog,
  DialogPortal,
  DialogOverlay,
  DialogTrigger,
  DialogClose,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogDescription,
}
""",
    "web/src/main.tsx": """import React from "react"
import ReactDOM from "react-dom/client"
import App from "./App"
import "./index.css"

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
)
""",
    "web/src/App.tsx": """import React, { useEffect, useMemo, useState } from "react"
import {
  Activity,
  AlertTriangle,
  Archive,
  BookmarkCheck,
  Check,
  Copy,
  ExternalLink,
  FileText,
  Filter,
  GitFork,
  Github,
  KeyRound,
  LayoutGrid,
  List,
  Moon,
  RefreshCw,
  Rocket,
  Search,
  Sparkles,
  Star,
  Sun,
  Trash2,
} from "lucide-react"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Input } from "@/components/ui/input"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog"

interface ReleaseInfo {
  tag: string
  url: string
  published_at: string
  summary_zh: string
  raw_body: string
}

interface RepoItem {
  id: number
  repo: string
  name: string
  owner: string
  avatar_url: string
  html_url: string
  description: string
  desc_zh: string
  stars: number
  forks: number
  open_issues: number
  language: string
  topics: string[]
  category: string
  status: "active" | "stale" | "abandoned"
  reason: string
  days_since_push: number
  pushed_at: string
  created_at: string
  archived: boolean
  homepage: string
  release: ReleaseInfo | null
}

interface DashboardData {
  generated_at: string
  date: string
  username: string
  stats: {
    total: number
    active_releases: number
    active_health: number
    stale_health: number
    abandoned: number
    categories: Record<string, number>
    languages: Record<string, number>
  }
  repos: RepoItem[]
}

const STORAGE_TOKEN_KEY = "stars_radar_gh_token"
const STORAGE_KEEP_KEY = "stars_radar_keep_repos"
const STORAGE_UNSTARRED_KEY = "stars_radar_unstarred_repos"

export default function App() {
  const [data, setData] = useState<DashboardData | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [darkMode, setDarkMode] = useState(true)

  // Filters & view state
  const [activeTab, setActiveTab] = useState<string>("releases")
  const [search, setSearch] = useState("")
  const [selectedCategory, setSelectedCategory] = useState<string>("ALL")
  const [selectedLanguage, setSelectedLanguage] = useState<string>("ALL")
  const [selectedStatus, setSelectedStatus] = useState<string>("ALL")
  const [sortBy, setSortBy] = useState<string>("release")
  const [viewMode, setViewMode] = useState<"grid" | "table">("grid")

  // Management state
  const [selectedRepos, setSelectedRepos] = useState<Set<string>>(new Set())
  const [keepRepos, setKeepRepos] = useState<Set<string>>(() => {
    try {
      const saved = localStorage.getItem(STORAGE_KEEP_KEY)
      return saved ? new Set(JSON.parse(saved)) : new Set()
    } catch {
      return new Set()
    }
  })
  const [unstarredRepos, setUnstarredRepos] = useState<Set<string>>(() => {
    try {
      const saved = localStorage.getItem(STORAGE_UNSTARRED_KEY)
      return saved ? new Set(JSON.parse(saved)) : new Set()
    } catch {
      return new Set()
    }
  })
  const [ghToken, setGhToken] = useState<string>(() => localStorage.getItem(STORAGE_TOKEN_KEY) || "")
  const [tokenInput, setTokenInput] = useState<string>(() => localStorage.getItem(STORAGE_TOKEN_KEY) || "")
  const [tokenModalOpen, setTokenModalOpen] = useState(false)
  const [detailRepo, setDetailRepo] = useState<RepoItem | null>(null)
  const [unstarBusy, setUnstarBusy] = useState<string | null>(null)
  const [copiedCmd, setCopiedCmd] = useState(false)
  const [toastMsg, setToastMsg] = useState<string | null>(null)

  useEffect(() => {
    const root = document.documentElement
    if (darkMode) {
      root.classList.add("dark")
    } else {
      root.classList.remove("dark")
    }
  }, [darkMode])

  const showToast = (msg: string) => {
    setToastMsg(msg)
    setTimeout(() => setToastMsg(null), 3200)
  }

  const fetchData = async () => {
    setLoading(true)
    setError(null)
    try {
      const resp = await fetch(`./data/dashboard.json?t=${Date.now()}`)
      if (!resp.ok) throw new Error(`HTTP ${resp.status}`)
      const json: DashboardData = await resp.json()
      setData(json)
    } catch (e: any) {
      setError(e?.message || "加载看板数据失败")
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    fetchData()
  }, [])

  const saveToken = () => {
    const trimmed = tokenInput.trim()
    setGhToken(trimmed)
    if (trimmed) {
      localStorage.setItem(STORAGE_TOKEN_KEY, trimmed)
      showToast("✅ 已保存 GitHub Token（仅保存在您的浏览器本地）")
    } else {
      localStorage.removeItem(STORAGE_TOKEN_KEY)
      showToast("已清除本地 GitHub Token")
    }
    setTokenModalOpen(false)
  }

  const toggleKeepRepo = (fullName: string) => {
    const next = new Set(keepRepos)
    if (next.has(fullName)) {
      next.delete(fullName)
      showToast(`已从保留白名单移除 ${fullName}`)
    } else {
      next.add(fullName)
      showToast(`🛡️ 已将 ${fullName} 加入保留白名单`)
    }
    setKeepRepos(next)
    localStorage.setItem(STORAGE_KEEP_KEY, JSON.stringify(Array.from(next)))
  }

  const toggleSelectRepo = (fullName: string) => {
    const next = new Set(selectedRepos)
    if (next.has(fullName)) {
      next.delete(fullName)
    } else {
      next.add(fullName)
    }
    setSelectedRepos(next)
  }

  const handleUnstarSingle = async (fullName: string, htmlUrl: string) => {
    if (!ghToken) {
      window.open(htmlUrl, "_blank", "noopener,noreferrer")
      return
    }
    setUnstarBusy(fullName)
    try {
      const resp = await fetch(`https://api.github.com/user/starred/${fullName}`, {
        method: "DELETE",
        headers: {
          Authorization: `Bearer ${ghToken}`,
          Accept: "application/vnd.github.v3+json",
        },
      })
      if (resp.status === 204 || resp.status === 404) {
        const next = new Set(unstarredRepos)
        next.add(fullName)
        setUnstarredRepos(next)
        localStorage.setItem(STORAGE_UNSTARRED_KEY, JSON.stringify(Array.from(next)))
        const nextSel = new Set(selectedRepos)
        nextSel.delete(fullName)
        setSelectedRepos(nextSel)
        showToast(`✅ 已成功取消 Star: ${fullName}`)
      } else {
        showToast(`❌ 取消 Star 失败 (HTTP ${resp.status})，请检查 Token 是否勾选 public_repo 权限`)
      }
    } catch (e: any) {
      showToast(`❌ 网络异常: ${e?.message}`)
    } finally {
      setUnstarBusy(null)
    }
  }

  const handleBatchUnstar = async () => {
    if (selectedRepos.size === 0) return
    if (!ghToken) {
      setTokenModalOpen(true)
      return
    }
    const targets = Array.from(selectedRepos)
    setUnstarBusy("BATCH")
    let successCount = 0
    const nextUnstarred = new Set(unstarredRepos)

    for (const fullName of targets) {
      try {
        const resp = await fetch(`https://api.github.com/user/starred/${fullName}`, {
          method: "DELETE",
          headers: {
            Authorization: `Bearer ${ghToken}`,
            Accept: "application/vnd.github.v3+json",
          },
        })
        if (resp.status === 204 || resp.status === 404) {
          successCount++
          nextUnstarred.add(fullName)
        }
      } catch {
        // ignore individual failure
      }
    }
    setUnstarredRepos(nextUnstarred)
    localStorage.setItem(STORAGE_UNSTARRED_KEY, JSON.stringify(Array.from(nextUnstarred)))
    setSelectedRepos(new Set())
    setUnstarBusy(null)
    showToast(`🎉 批量处理完成：成功取消 ${successCount} / ${targets.length} 个仓库的 Star`)
  }

  const copyGhCliCommands = () => {
    const targets = Array.from(selectedRepos)
    if (targets.length === 0) return
    const cmd = targets.map((r) => `gh api -X DELETE /user/starred/${r}`).join("\\n")
    navigator.clipboard.writeText(cmd)
    setCopiedCmd(true)
    showToast(`📋 已复制 ${targets.length} 条 gh CLI 取消 Star 命令`)
    setTimeout(() => setCopiedCmd(false), 2000)
  }

  const visibleRepos = useMemo(() => {
    if (!data) return []
    return data.repos.filter((r) => !unstarredRepos.has(r.repo))
  }, [data, unstarredRepos])

  const categoriesList = useMemo(() => {
    const counts: Record<string, number> = {}
    for (const r of visibleRepos) {
      counts[r.category] = (counts[r.category] || 0) + 1
    }
    return Object.entries(counts).sort((a, b) => b[1] - a[1])
  }, [visibleRepos])

  const languagesList = useMemo(() => {
    const counts: Record<string, number> = {}
    for (const r of visibleRepos) {
      const lang = r.language || "Other"
      counts[lang] = (counts[lang] || 0) + 1
    }
    return Object.entries(counts).sort((a, b) => b[1] - a[1])
  }, [visibleRepos])

  const filteredRepos = useMemo(() => {
    let list = visibleRepos

    // Tab filter
    if (activeTab === "releases") {
      list = list.filter((r) => r.release !== null)
    } else if (activeTab === "cleanup") {
      list = list.filter((r) => r.status === "abandoned" || r.status === "stale")
    }

    // Status filter
    if (selectedStatus !== "ALL") {
      if (selectedStatus === "RELEASE") {
        list = list.filter((r) => r.release !== null)
      } else if (selectedStatus === "KEEP") {
        list = list.filter((r) => keepRepos.has(r.repo))
      } else {
        list = list.filter((r) => r.status === selectedStatus)
      }
    }

    // Category filter
    if (selectedCategory !== "ALL") {
      list = list.filter((r) => r.category === selectedCategory)
    }

    // Language filter
    if (selectedLanguage !== "ALL") {
      list = list.filter((r) => (r.language || "Other") === selectedLanguage)
    }

    // Search query
    if (search.trim()) {
      const q = search.toLowerCase().trim()
      list = list.filter(
        (r) =>
          r.repo.toLowerCase().includes(q) ||
          (r.desc_zh && r.desc_zh.toLowerCase().includes(q)) ||
          (r.description && r.description.toLowerCase().includes(q)) ||
          r.topics.some((t) => t.toLowerCase().includes(q)) ||
          (r.release?.summary_zh && r.release.summary_zh.toLowerCase().includes(q))
      )
    }

    // Sort
    const sorted = [...list]
    sorted.sort((a, b) => {
      if (sortBy === "release") {
        const da = a.release?.published_at || ""
        const db = b.release?.published_at || ""
        if (da !== db) return db.localeCompare(da)
        return b.stars - a.stars
      }
      if (sortBy === "stars") return b.stars - a.stars
      if (sortBy === "recent_push") return a.days_since_push - b.days_since_push
      if (sortBy === "oldest_push") return b.days_since_push - a.days_since_push
      if (sortBy === "name") return a.repo.localeCompare(b.repo)
      return 0
    })

    return sorted
  }, [
    visibleRepos,
    activeTab,
    selectedStatus,
    selectedCategory,
    selectedLanguage,
    search,
    sortBy,
    keepRepos,
  ])

  const statsSummary = useMemo(() => {
    const total = visibleRepos.length
    const releases = visibleRepos.filter((r) => r.release !== null).length
    const active = visibleRepos.filter((r) => r.status === "active").length
    const stale = visibleRepos.filter((r) => r.status === "stale").length
    const abandoned = visibleRepos.filter((r) => r.status === "abandoned").length
    return { total, releases, active, stale, abandoned }
  }, [visibleRepos])

  const renderStatusBadge = (repo: RepoItem) => {
    if (keepRepos.has(repo.repo)) {
      return <Badge variant="secondary">🛡️ 白名单保留</Badge>
    }
    if (repo.archived) {
      return <Badge variant="danger">🗄️ 已归档 (Archived)</Badge>
    }
    if (repo.status === "active") {
      return <Badge variant="success">💚 {repo.reason}</Badge>
    }
    if (repo.status === "stale") {
      return <Badge variant="warning">🟡 {repo.reason}</Badge>
    }
    return <Badge variant="danger">🛑 {repo.reason}</Badge>
  }

  if (loading) {
    return (
      <div className="flex min-h-screen flex-col items-center justify-center gap-3">
        <RefreshCw className="h-8 w-8 animate-spin text-primary" />
        <p className="text-sm text-muted-foreground">正在加载 Starred 项目雷达看板数据...</p>
      </div>
    )
  }

  if (error || !data) {
    return (
      <div className="flex min-h-screen flex-col items-center justify-center gap-4 p-6 text-center">
        <AlertTriangle className="h-10 w-10 text-destructive" />
        <h2 className="text-lg font-semibold">无法加载看板数据</h2>
        <p className="text-sm text-muted-foreground">{error}</p>
        <Button onClick={fetchData}>重试加载</Button>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-background pb-20">
      {/* Top Toast */}
      {toastMsg && (
        <div className="fixed bottom-6 right-6 z-50 flex items-center gap-2 rounded-lg border bg-card px-4 py-3 text-sm font-medium shadow-xl">
          <span>{toastMsg}</span>
        </div>
      )}

      {/* Header */}
      <header className="sticky top-0 z-30 border-b bg-background/85 backdrop-blur-md">
        <div className="mx-auto flex max-w-7xl flex-wrap items-center justify-between gap-4 px-4 py-3.5 sm:px-6">
          <div className="flex items-center gap-3">
            <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-primary text-primary-foreground shadow">
              <Sparkles className="h-5 w-5" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h1 className="text-lg font-bold tracking-tight sm:text-xl">
                  Starred 项目雷达看板
                </h1>
                <Badge variant="outline" className="hidden sm:inline-flex">
                  shadcn/ui
                </Badge>
              </div>
              <p className="text-xs text-muted-foreground">
                @{data.username} · 数据更新于 {data.generated_at}
              </p>
            </div>
          </div>

          <div className="flex items-center gap-2">
            <Button
              variant={ghToken ? "secondary" : "outline"}
              size="sm"
              onClick={() => setTokenModalOpen(true)}
            >
              <KeyRound className="h-4 w-4" />
              <span>{ghToken ? "已连接 Token (可直连取消Star)" : "连接 Token 管理"}</span>
            </Button>

            <Button
              variant="outline"
              size="sm"
              asChild
            >
              <a
                href={`https://github.com/${data.username}/my-stars-digest/actions`}
                target="_blank"
                rel="noopener noreferrer"
              >
                <RefreshCw className="h-3.5 w-3.5" />
                <span className="hidden md:inline">Actions 同步</span>
              </a>
            </Button>

            <Button
              variant="outline"
              size="icon"
              asChild
              title="前往 GitHub 仓库"
            >
              <a
                href={`https://github.com/${data.username}/my-stars-digest`}
                target="_blank"
                rel="noopener noreferrer"
              >
                <Github className="h-4 w-4" />
              </a>
            </Button>

            <Button
              variant="ghost"
              size="icon"
              onClick={() => setDarkMode(!darkMode)}
              title="切换深色/浅色主题"
            >
              {darkMode ? <Sun className="h-4 w-4" /> : <Moon className="h-4 w-4" />}
            </Button>
          </div>
        </div>
      </header>

      <main className="mx-auto max-w-7xl space-y-6 px-4 pt-6 sm:px-6">
        {/* KPI Stat Cards */}
        <div className="grid grid-cols-2 gap-3 sm:grid-cols-3 lg:grid-cols-5">
          <Card
            onClick={() => {
              setActiveTab("all")
              setSelectedStatus("ALL")
            }}
            className={`cursor-pointer transition-all hover:border-primary/50 ${
              activeTab === "all" && selectedStatus === "ALL" ? "ring-2 ring-primary" : ""
            }`}
          >
            <CardHeader className="p-4 pb-2">
              <CardDescription className="flex items-center justify-between text-xs">
                <span>🌟 总关注项目</span>
                <Star className="h-4 w-4 text-amber-400" />
              </CardDescription>
              <CardTitle className="text-2xl font-bold">{statsSummary.total}</CardTitle>
            </CardHeader>
            <CardContent className="p-4 pt-0 text-xs text-muted-foreground">
              涵盖 {categoriesList.length} 个技术领域
            </CardContent>
          </Card>

          <Card
            onClick={() => {
              setActiveTab("releases")
              setSelectedStatus("ALL")
              setSortBy("release")
            }}
            className={`cursor-pointer transition-all hover:border-primary/50 ${
              activeTab === "releases" ? "ring-2 ring-primary" : ""
            }`}
          >
            <CardHeader className="p-4 pb-2">
              <CardDescription className="flex items-center justify-between text-xs">
                <span>🚀 近30天新发版</span>
                <Rocket className="h-4 w-4 text-blue-400" />
              </CardDescription>
              <CardTitle className="text-2xl font-bold text-blue-500 dark:text-blue-400">
                {statsSummary.releases}
              </CardTitle>
            </CardHeader>
            <CardContent className="p-4 pt-0 text-xs text-muted-foreground">
              含自动提炼中文更新亮点
            </CardContent>
          </Card>

          <Card
            onClick={() => {
              setActiveTab("all")
              setSelectedStatus("active")
              setSortBy("recent_push")
            }}
            className={`cursor-pointer transition-all hover:border-primary/50 ${
              selectedStatus === "active" ? "ring-2 ring-primary" : ""
            }`}
          >
            <CardHeader className="p-4 pb-2">
              <CardDescription className="flex items-center justify-between text-xs">
                <span>💚 活跃维护 (&lt;90天)</span>
                <Activity className="h-4 w-4 text-emerald-400" />
              </CardDescription>
              <CardTitle className="text-2xl font-bold text-emerald-600 dark:text-emerald-400">
                {statsSummary.active}
              </CardTitle>
            </CardHeader>
            <CardContent className="p-4 pt-0 text-xs text-muted-foreground">
              近期有持续代码提交
            </CardContent>
          </Card>

          <Card
            onClick={() => {
              setActiveTab("cleanup")
              setSelectedStatus("stale")
              setSortBy("oldest_push")
            }}
            className={`cursor-pointer transition-all hover:border-primary/50 ${
              selectedStatus === "stale" ? "ring-2 ring-primary" : ""
            }`}
          >
            <CardHeader className="p-4 pb-2">
              <CardDescription className="flex items-center justify-between text-xs">
                <span>🟡 低频维护 (90-365天)</span>
                <AlertTriangle className="h-4 w-4 text-amber-400" />
              </CardDescription>
              <CardTitle className="text-2xl font-bold text-amber-600 dark:text-amber-400">
                {statsSummary.stale}
              </CardTitle>
            </CardHeader>
            <CardContent className="p-4 pt-0 text-xs text-muted-foreground">
              超 3 个月未提交代码
            </CardContent>
          </Card>

          <Card
            onClick={() => {
              setActiveTab("cleanup")
              setSelectedStatus("abandoned")
              setSortBy("oldest_push")
            }}
            className={`col-span-2 sm:col-span-1 cursor-pointer transition-all hover:border-destructive/60 ${
              activeTab === "cleanup" && selectedStatus === "abandoned"
                ? "ring-2 ring-destructive"
                : ""
            }`}
          >
            <CardHeader className="p-4 pb-2">
              <CardDescription className="flex items-center justify-between text-xs">
                <span>🛑 建议清理 (&gt;1年/归档)</span>
                <Archive className="h-4 w-4 text-rose-400" />
              </CardDescription>
              <CardTitle className="text-2xl font-bold text-rose-600 dark:text-rose-400">
                {statsSummary.abandoned}
              </CardTitle>
            </CardHeader>
            <CardContent className="p-4 pt-0 text-xs text-muted-foreground">
              点击进入批量清理工作台
            </CardContent>
          </Card>
        </div>

        {/* Category Pills */}
        <div className="flex flex-wrap items-center gap-2">
          <Button
            variant={selectedCategory === "ALL" ? "default" : "outline"}
            size="sm"
            onClick={() => setSelectedCategory("ALL")}
            className="h-8 rounded-full text-xs"
          >
            全部领域 ({visibleRepos.length})
          </Button>
          {categoriesList.map(([cat, count]) => (
            <Button
              key={cat}
              variant={selectedCategory === cat ? "default" : "outline"}
              size="sm"
              onClick={() => setSelectedCategory(selectedCategory === cat ? "ALL" : cat)}
              className="h-8 rounded-full text-xs"
            >
              {cat} ({count})
            </Button>
          ))}
        </div>

        {/* Tabs & Filter Controls */}
        <Tabs
          value={activeTab}
          onValueChange={(val) => {
            setActiveTab(val)
            if (val === "releases") {
              setSelectedStatus("ALL")
              setSortBy("release")
            } else if (val === "cleanup") {
              setSelectedStatus("abandoned")
              setSortBy("oldest_push")
            } else {
              setSelectedStatus("ALL")
              setSortBy("stars")
            }
          }}
        >
          <div className="flex flex-col gap-3 lg:flex-row lg:items-center lg:justify-between">
            <TabsList className="w-full sm:w-auto">
              <TabsTrigger value="releases" className="flex-1 sm:flex-initial">
                🚀 本期更新 ({statsSummary.releases})
              </TabsTrigger>
              <TabsTrigger value="all" className="flex-1 sm:flex-initial">
                📚 全部关注库 ({statsSummary.total})
              </TabsTrigger>
              <TabsTrigger value="cleanup" className="flex-1 sm:flex-initial">
                🛑 弃坑清理台 ({statsSummary.abandoned + statsSummary.stale})
              </TabsTrigger>
            </TabsList>

            {/* Search & Filters */}
            <div className="flex flex-wrap items-center gap-2">
              <div className="relative min-w-[220px] flex-1 sm:w-64">
                <Search className="absolute left-2.5 top-2.5 h-4 w-4 text-muted-foreground" />
                <Input
                  placeholder="搜索仓库名、中文简介、标签、更新内容..."
                  value={search}
                  onChange={(e) => setSearch(e.target.value)}
                  className="pl-8"
                />
              </div>

              <select
                value={selectedLanguage}
                onChange={(e) => setSelectedLanguage(e.target.value)}
                className="h-9 rounded-md border border-input bg-background px-3 text-xs shadow-sm focus:outline-none focus:ring-1 focus:ring-ring"
              >
                <option value="ALL">💻 全部语言</option>
                {languagesList.map(([lang, count]) => (
                  <option key={lang} value={lang}>
                    {lang} ({count})
                  </option>
                ))}
              </select>

              <select
                value={selectedStatus}
                onChange={(e) => setSelectedStatus(e.target.value)}
                className="h-9 rounded-md border border-input bg-background px-3 text-xs shadow-sm focus:outline-none focus:ring-1 focus:ring-ring"
              >
                <option value="ALL">⚡ 全部状态</option>
                <option value="active">💚 活跃维护 (&lt;90天)</option>
                <option value="stale">🟡 低频维护 (90-365天)</option>
                <option value="abandoned">🛑 停更/归档 (&gt;1年)</option>
                <option value="RELEASE">🚀 近期有新 Release</option>
                <option value="KEEP">🛡️ 白名单保留 ({keepRepos.size})</option>
              </select>

              <select
                value={sortBy}
                onChange={(e) => setSortBy(e.target.value)}
                className="h-9 rounded-md border border-input bg-background px-3 text-xs shadow-sm focus:outline-none focus:ring-1 focus:ring-ring"
              >
                <option value="release">📅 按最新发布排序</option>
                <option value="stars">⭐ 按 Star 数从高到低</option>
                <option value="recent_push">🔥 按最近代码提交排序</option>
                <option value="oldest_push">⏳ 按停更天数从高到低</option>
                <option value="name">🔤 按仓库名 A-Z</option>
              </select>

              <div className="flex items-center rounded-md border p-0.5">
                <Button
                  variant={viewMode === "grid" ? "secondary" : "ghost"}
                  size="icon"
                  className="h-7 w-7"
                  onClick={() => setViewMode("grid")}
                  title="卡片视图"
                >
                  <LayoutGrid className="h-3.5 w-3.5" />
                </Button>
                <Button
                  variant={viewMode === "table" ? "secondary" : "ghost"}
                  size="icon"
                  className="h-7 w-7"
                  onClick={() => setViewMode("table")}
                  title="表格管理视图"
                >
                  <List className="h-3.5 w-3.5" />
                </Button>
              </div>
            </div>
          </div>

          {/* Batch Management Bar */}
          {(activeTab === "cleanup" || selectedRepos.size > 0) && (
            <div className="mt-3 flex flex-wrap items-center justify-between gap-3 rounded-xl border bg-muted/40 p-3">
              <div className="flex flex-wrap items-center gap-2 text-xs">
                <Filter className="h-4 w-4 text-muted-foreground" />
                <span>
                  当前筛选共 <strong>{filteredRepos.length}</strong> 个项目，已勾选{" "}
                  <strong className="text-primary">{selectedRepos.size}</strong> 个
                </span>
                <Button
                  variant="outline"
                  size="sm"
                  className="h-7 text-xs"
                  onClick={() => {
                    const next = new Set(selectedRepos)
                    filteredRepos.forEach((r) => {
                      if (!keepRepos.has(r.repo)) next.add(r.repo)
                    })
                    setSelectedRepos(next)
                  }}
                >
                  全选当前列表 (排除白名单)
                </Button>
                {selectedRepos.size > 0 && (
                  <Button
                    variant="ghost"
                    size="sm"
                    className="h-7 text-xs"
                    onClick={() => setSelectedRepos(new Set())}
                  >
                    清空选择
                  </Button>
                )}
              </div>

              <div className="flex flex-wrap items-center gap-2">
                <Button
                  variant="outline"
                  size="sm"
                  className="h-8 text-xs"
                  disabled={selectedRepos.size === 0}
                  onClick={copyGhCliCommands}
                >
                  {copiedCmd ? <Check className="h-3.5 w-3.5" /> : <Copy className="h-3.5 w-3.5" />}
                  <span>复制 gh CLI 批量取关命令</span>
                </Button>

                <Button
                  variant="destructive"
                  size="sm"
                  className="h-8 text-xs"
                  disabled={selectedRepos.size === 0 || unstarBusy === "BATCH"}
                  onClick={handleBatchUnstar}
                >
                  <Trash2 className="h-3.5 w-3.5" />
                  <span>
                    {unstarBusy === "BATCH"
                      ? "正在批量取消 Star..."
                      : ghToken
                      ? `一键批量取消 Star (${selectedRepos.size})`
                      : `配置 Token 后批量取消 Star (${selectedRepos.size})`}
                  </span>
                </Button>
              </div>
            </div>
          )}

          {/* Content Area (Shared across tabs based on filteredRepos) */}
          <div className="mt-4">
            {filteredRepos.length === 0 ? (
              <Card className="p-12 text-center">
                <p className="text-sm text-muted-foreground">没有匹配的仓库，试试调整搜索词或筛选条件。</p>
              </Card>
            ) : viewMode === "grid" ? (
              <div className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
                {filteredRepos.map((item) => {
                  const isSelected = selectedRepos.has(item.repo)
                  const isKept = keepRepos.has(item.repo)
                  return (
                    <Card
                      key={item.repo}
                      className={`flex flex-col justify-between transition-all hover:shadow-md ${
                        isSelected ? "ring-2 ring-primary" : ""
                      }`}
                    >
                      <div>
                        <CardHeader className="pb-2.5">
                          <div className="flex items-start justify-between gap-2">
                            <div className="flex items-center gap-2.5 min-w-0">
                              <input
                                type="checkbox"
                                checked={isSelected}
                                onChange={() => toggleSelectRepo(item.repo)}
                                className="h-4 w-4 rounded border-input accent-primary cursor-pointer"
                                title="勾选以批量管理"
                              />
                              <img
                                src={item.avatar_url}
                                alt={item.owner}
                                className="h-6 w-6 rounded-full border"
                                loading="lazy"
                              />
                              <a
                                href={item.html_url}
                                target="_blank"
                                rel="noopener noreferrer"
                                className="truncate font-semibold hover:underline"
                                title={item.repo}
                              >
                                {item.repo}
                              </a>
                            </div>
                            <Button
                              variant="ghost"
                              size="icon"
                              className="h-7 w-7 shrink-0"
                              onClick={() => toggleKeepRepo(item.repo)}
                              title={isKept ? "从保留白名单移除" : "加入保留白名单（清理时忽略）"}
                            >
                              <BookmarkCheck
                                className={`h-4 w-4 ${
                                  isKept ? "text-emerald-500" : "text-muted-foreground"
                                }`}
                              />
                            </Button>
                          </div>

                          <div className="flex flex-wrap items-center gap-1.5 pt-1">
                            <Badge variant="secondary" className="text-[11px]">
                              {item.category}
                            </Badge>
                            {item.language && (
                              <Badge variant="outline" className="text-[11px]">
                                💻 {item.language}
                              </Badge>
                            )}
                            {renderStatusBadge(item)}
                          </div>
                        </CardHeader>

                        <CardContent className="space-y-3 pb-3">
                          <p className="line-clamp-2 text-xs leading-relaxed text-muted-foreground">
                            {item.desc_zh || item.description || "暂无项目描述"}
                          </p>

                          {item.release && (
                            <div className="rounded-lg border bg-muted/40 p-2.5 text-xs space-y-1.5">
                              <div className="flex items-center justify-between gap-2">
                                <a
                                  href={item.release.url}
                                  target="_blank"
                                  rel="noopener noreferrer"
                                  className="font-semibold text-blue-600 dark:text-blue-400 hover:underline flex items-center gap-1"
                                >
                                  <Rocket className="h-3.5 w-3.5" />
                                  <span>{item.release.tag}</span>
                                </a>
                                <span className="text-[11px] text-muted-foreground">
                                  {item.release.published_at}
                                </span>
                              </div>
                              <p className="line-clamp-3 whitespace-pre-line text-xs text-foreground/90">
                                {item.release.summary_zh}
                              </p>
                              {item.release.raw_body && (
                                <button
                                  onClick={() => setDetailRepo(item)}
                                  className="inline-flex items-center gap-1 text-[11px] font-medium text-primary hover:underline pt-0.5"
                                >
                                  <FileText className="h-3 w-3" />
                                  查看完整 Release Notes
                                </button>
                              )}
                            </div>
                          )}

                          {item.topics && item.topics.length > 0 && (
                            <div className="flex flex-wrap gap-1">
                              {item.topics.slice(0, 5).map((t) => (
                                <span
                                  key={t}
                                  onClick={() => setSearch(t)}
                                  className="cursor-pointer rounded bg-secondary/70 px-1.5 py-0.5 text-[10px] text-muted-foreground hover:text-foreground"
                                >
                                  #{t}
                                </span>
                              ))}
                            </div>
                          )}
                        </CardContent>
                      </div>

                      <CardFooter className="flex items-center justify-between border-t pt-3 text-xs text-muted-foreground">
                        <div className="flex items-center gap-3">
                          <span className="flex items-center gap-1 font-medium text-foreground">
                            <Star className="h-3.5 w-3.5 text-amber-400 fill-amber-400" />
                            {item.stars.toLocaleString()}
                          </span>
                          <span className="flex items-center gap-1">
                            <GitFork className="h-3.5 w-3.5" />
                            {item.forks.toLocaleString()}
                          </span>
                          <span title="最近代码推送日期">🕒 {item.pushed_at || "未知"}</span>
                        </div>

                        <div className="flex items-center gap-1.5">
                          <Button
                            variant={item.status === "abandoned" ? "destructive" : "outline"}
                            size="sm"
                            className="h-7 px-2.5 text-xs"
                            disabled={unstarBusy === item.repo}
                            onClick={() => handleUnstarSingle(item.repo, item.html_url)}
                          >
                            {unstarBusy === item.repo ? (
                              "处理中..."
                            ) : ghToken ? (
                              <>
                                <Trash2 className="h-3 w-3" />
                                <span>取消 Star</span>
                              </>
                            ) : (
                              <>
                                <ExternalLink className="h-3 w-3" />
                                <span>管理</span>
                              </>
                            )}
                          </Button>
                        </div>
                      </CardFooter>
                    </Card>
                  )
                })}
              </div>
            ) : (
              /* Table View */
              <Card>
                <Table>
                  <TableHeader>
                    <TableRow>
                      <TableHead className="w-10">
                        <input
                          type="checkbox"
                          checked={
                            filteredRepos.length > 0 &&
                            filteredRepos.every((r) => selectedRepos.has(r.repo))
                          }
                          onChange={(e) => {
                            if (e.target.checked) {
                              const next = new Set(selectedRepos)
                              filteredRepos.forEach((r) => next.add(r.repo))
                              setSelectedRepos(next)
                            } else {
                              setSelectedRepos(new Set())
                            }
                          }}
                          className="h-4 w-4 rounded border-input accent-primary cursor-pointer"
                        />
                      </TableHead>
                      <TableHead>仓库名称</TableHead>
                      <TableHead>分类 / 语言</TableHead>
                      <TableHead>Stars</TableHead>
                      <TableHead>健康状态 / 最后提交</TableHead>
                      <TableHead>近期版本</TableHead>
                      <TableHead className="text-right">操作</TableHead>
                    </TableRow>
                  </TableHeader>
                  <TableBody>
                    {filteredRepos.map((item) => {
                      const isSelected = selectedRepos.has(item.repo)
                      const isKept = keepRepos.has(item.repo)
                      return (
                        <TableRow key={item.repo}>
                          <TableCell>
                            <input
                              type="checkbox"
                              checked={isSelected}
                              onChange={() => toggleSelectRepo(item.repo)}
                              className="h-4 w-4 rounded border-input accent-primary cursor-pointer"
                            />
                          </TableCell>
                          <TableCell className="max-w-[260px]">
                            <div className="flex items-center gap-2">
                              <img
                                src={item.avatar_url}
                                alt={item.owner}
                                className="h-5 w-5 rounded-full"
                                loading="lazy"
                              />
                              <a
                                href={item.html_url}
                                target="_blank"
                                rel="noopener noreferrer"
                                className="font-medium hover:underline truncate"
                              >
                                {item.repo}
                              </a>
                            </div>
                            <p className="truncate text-xs text-muted-foreground mt-0.5">
                              {item.desc_zh || item.description}
                            </p>
                          </TableCell>
                          <TableCell>
                            <div className="flex flex-col gap-1">
                              <span className="text-xs">{item.category}</span>
                              <span className="text-[11px] text-muted-foreground">
                                {item.language || "Other"}
                              </span>
                            </div>
                          </TableCell>
                          <TableCell className="font-medium">
                            ⭐ {item.stars.toLocaleString()}
                          </TableCell>
                          <TableCell>
                            <div className="flex flex-col gap-1">
                              <div>{renderStatusBadge(item)}</div>
                              <span className="text-[11px] text-muted-foreground">
                                最后推送: {item.pushed_at}
                              </span>
                            </div>
                          </TableCell>
                          <TableCell>
                            {item.release ? (
                              <button
                                onClick={() => setDetailRepo(item)}
                                className="text-left text-xs text-blue-500 hover:underline"
                              >
                                <div className="font-semibold">{item.release.tag}</div>
                                <div className="text-[11px] text-muted-foreground">
                                  {item.release.published_at}
                                </div>
                              </button>
                            ) : (
                              <span className="text-xs text-muted-foreground">-</span>
                            )}
                          </TableCell>
                          <TableCell className="text-right">
                            <div className="flex items-center justify-end gap-1.5">
                              <Button
                                variant="ghost"
                                size="icon"
                                className="h-7 w-7"
                                onClick={() => toggleKeepRepo(item.repo)}
                                title={isKept ? "取消白名单保留" : "加入白名单保留"}
                              >
                                <BookmarkCheck
                                  className={`h-4 w-4 ${
                                    isKept ? "text-emerald-500" : "text-muted-foreground"
                                  }`}
                                />
                              </Button>
                              <Button
                                variant={item.status === "abandoned" ? "destructive" : "outline"}
                                size="sm"
                                className="h-7 px-2.5 text-xs"
                                onClick={() => handleUnstarSingle(item.repo, item.html_url)}
                              >
                                {ghToken ? "取消 Star" : "前往仓库"}
                              </Button>
                            </div>
                          </TableCell>
                        </TableRow>
                      )
                    })}
                  </TableBody>
                </Table>
              </Card>
            )}
          </div>
        </Tabs>
      </main>

      {/* Release Notes Modal */}
      <Dialog open={!!detailRepo} onOpenChange={(open) => !open && setDetailRepo(null)}>
        <DialogContent>
          {detailRepo && (
            <>
              <DialogHeader>
                <DialogTitle className="flex items-center gap-2">
                  <span>📦 {detailRepo.repo}</span>
                  {detailRepo.release && (
                    <Badge variant="secondary">{detailRepo.release.tag}</Badge>
                  )}
                </DialogTitle>
                <DialogDescription>
                  发布时间：{detailRepo.release?.published_at} · ⭐{" "}
                  {detailRepo.stars.toLocaleString()} Stars
                </DialogDescription>
              </DialogHeader>

              <div className="space-y-4 text-sm">
                <div className="rounded-lg border bg-muted/40 p-3.5 space-y-1.5">
                  <div className="font-semibold text-xs text-primary">
                    💡 核心亮点更新 (中文提炼)
                  </div>
                  <p className="whitespace-pre-line text-xs leading-relaxed">
                    {detailRepo.release?.summary_zh}
                  </p>
                </div>

                {detailRepo.release?.raw_body && (
                  <div className="space-y-1.5">
                    <div className="font-semibold text-xs text-muted-foreground">
                      🔍 官方原版 Release Notes
                    </div>
                    <pre className="max-h-72 overflow-auto rounded-lg border bg-muted/50 p-3 text-xs whitespace-pre-wrap font-mono">
                      {detailRepo.release.raw_body}
                    </pre>
                  </div>
                )}

                <div className="flex justify-end gap-2 pt-2">
                  {detailRepo.release?.url && (
                    <Button variant="outline" size="sm" asChild>
                      <a
                        href={detailRepo.release.url}
                        target="_blank"
                        rel="noopener noreferrer"
                      >
                        <ExternalLink className="h-3.5 w-3.5" />
                        查看 GitHub Release
                      </a>
                    </Button>
                  )}
                  <Button size="sm" asChild>
                    <a
                      href={detailRepo.html_url}
                      target="_blank"
                      rel="noopener noreferrer"
                    >
                      <Github className="h-3.5 w-3.5" />
                      访问项目主页
                    </a>
                  </Button>
                </div>
              </div>
            </>
          )}
        </DialogContent>
      </Dialog>

      {/* GitHub Token Modal */}
      <Dialog open={tokenModalOpen} onOpenChange={setTokenModalOpen}>
        <DialogContent>
          <DialogHeader>
            <DialogTitle className="flex items-center gap-2">
              <KeyRound className="h-5 w-5 text-primary" />
              <span>连接 GitHub Token（支持在看板直接取消 Star）</span>
            </DialogTitle>
            <DialogDescription>
              Token 仅保存在您当前浏览器的 <code>localStorage</code> 中，绝不会上传至任何服务器。
            </DialogDescription>
          </DialogHeader>

          <div className="space-y-4 text-sm">
            <div className="rounded-lg border bg-muted/40 p-3 text-xs space-y-1 text-muted-foreground">
              <p>1. 前往 GitHub Settings → Developer settings → Personal access tokens (Classic)</p>
              <p>
                2. 生成 Token 时勾选 <code>public_repo</code>（或 <code>user</code>）权限即可用于管理 Star。
              </p>
              <p>3. 配置后，点击看板中的「取消 Star」或「一键批量取消 Star」将直接调用 GitHub API 生效。</p>
            </div>

            <div className="space-y-2">
              <label className="text-xs font-medium">Personal Access Token (ghp_...)</label>
              <Input
                type="password"
                placeholder="粘贴您的 GitHub Token..."
                value={tokenInput}
                onChange={(e) => setTokenInput(e.target.value)}
              />
            </div>

            <div className="flex justify-end gap-2">
              {ghToken && (
                <Button
                  variant="outline"
                  size="sm"
                  onClick={() => {
                    setTokenInput("")
                    setGhToken("")
                    localStorage.removeItem(STORAGE_TOKEN_KEY)
                    setTokenModalOpen(false)
                    showToast("已清除本地 Token")
                  }}
                >
                  清除已存 Token
                </Button>
              )}
              <Button variant="outline" size="sm" onClick={() => setTokenModalOpen(false)}>
                取消
              </Button>
              <Button size="sm" onClick={saveToken}>
                保存配置
              </Button>
            </div>
          </div>
        </DialogContent>
      </Dialog>
    </div>
  )
}
""",
}


def ensure_shadcn_web_project():
    """确保仓库中存在完整的 shadcn/ui 看板前端工程文件"""
    for rel_path, content in SHADCN_WEB_FILES.items():
        os.makedirs(os.path.dirname(rel_path), exist_ok=True)
        with open(rel_path, "w", encoding="utf-8") as f:
            f.write(content)
    print("✅ shadcn/ui 看板工程文件已同步至 web/ 目录。")


def main():
    ensure_shadcn_web_project()

    print(f"正在拉取 @{USERNAME} 的 Star 列表...")
    repos = []
    page = 1
    while True:
        url = f"{STAR_API}?per_page=100&page={page}"
        resp = github_get(url)
        if resp.status_code != 200:
            print(f"❌ 请求失败 (HTTP {resp.status_code}): {resp.text[:300]}")
            if page == 1:
                sys.exit(1)
            break
        data = resp.json()
        if not data or not isinstance(data, list):
            break
        repos.extend(data)
        page += 1

    total = len(repos)
    print(f"共获取到 {total} 个 Star 项目。")
    if total == 0:
        print("❌ 未获取到任何 Star 项目，终止写入以防覆盖已有周报数据。")
        sys.exit(1)

    cache = load_cache()
    active_updates = []
    abandoned_repos = []
    dashboard_repos = []

    cat_counts = {}
    lang_counts = {}
    active_health_count = 0
    stale_health_count = 0

    for idx, repo in enumerate(repos, 1):
        full_name = repo["full_name"]
        status, reason, days_since_push = check_health(repo)
        cat = classify_repo(repo)
        lang = repo.get("language") or "Other"

        cat_counts[cat] = cat_counts.get(cat, 0) + 1
        lang_counts[lang] = lang_counts.get(lang, 0) + 1

        if status == "active":
            active_health_count += 1
        elif status == "stale":
            stale_health_count += 1

        release_obj = None

        if status == "abandoned":
            abandoned_repos.append({
                "repo": full_name,
                "html_url": repo["html_url"],
                "stars": repo.get("stargazers_count", 0),
                "reason": reason
            })
        elif status == "active":
            update_info = check_repo_updates(repo, cache)
            if update_info:
                active_updates.append({
                    "repo": full_name,
                    "html_url": repo["html_url"],
                    "stars": repo.get("stargazers_count", 0),
                    "language": lang,
                    "category": cat,
                    "tag": update_info["tag"],
                    "release_url": update_info["url"],
                    "published_at": update_info["published_at"],
                    "desc_zh": update_info["desc_zh"],
                    "summary_zh": update_info["summary_zh"],
                    "raw_body": update_info["raw_body"]
                })
                release_obj = {
                    "tag": update_info["tag"],
                    "url": update_info["url"],
                    "published_at": update_info["published_at"],
                    "summary_zh": update_info["summary_zh"],
                    "raw_body": update_info["raw_body"][:2500] if update_info["raw_body"] else ""
                }

        cached_entry = cache.get(full_name, {})
        raw_desc = repo.get("description") or ""
        desc_zh = cached_entry.get("desc_zh") or raw_desc or "暂无项目描述"

        dashboard_repos.append({
            "id": repo.get("id", idx),
            "repo": full_name,
            "name": repo.get("name", ""),
            "owner": (repo.get("owner") or {}).get("login", ""),
            "avatar_url": (repo.get("owner") or {}).get("avatar_url", ""),
            "html_url": repo.get("html_url", ""),
            "description": raw_desc,
            "desc_zh": desc_zh,
            "stars": repo.get("stargazers_count", 0),
            "forks": repo.get("forks_count", 0),
            "open_issues": repo.get("open_issues_count", 0),
            "language": lang,
            "topics": repo.get("topics") or [],
            "category": cat,
            "status": status,
            "reason": reason,
            "days_since_push": days_since_push,
            "pushed_at": (repo.get("pushed_at") or "")[:10],
            "created_at": (repo.get("created_at") or "")[:10],
            "archived": repo.get("archived", False),
            "homepage": repo.get("homepage") or "",
            "release": release_obj
        })

    save_cache(cache)

    dashboard_payload = {
        "generated_at": NOW.strftime("%Y-%m-%d %H:%M UTC"),
        "date": NOW.strftime("%Y-%m-%d"),
        "username": USERNAME,
        "stats": {
            "total": total,
            "active_releases": len(active_updates),
            "active_health": active_health_count,
            "stale_health": stale_health_count,
            "abandoned": len(abandoned_repos),
            "categories": cat_counts,
            "languages": lang_counts
        },
        "repos": dashboard_repos
    }

    for target_json in [DASHBOARD_DATA_FILE, WEB_DASHBOARD_DATA_FILE]:
        os.makedirs(os.path.dirname(target_json), exist_ok=True)
        with open(target_json, "w", encoding="utf-8") as f:
            json.dump(dashboard_payload, f, ensure_ascii=False, indent=2)

    md_content = generate_markdown(active_updates, abandoned_repos, total)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(md_content)

    os.makedirs("reports", exist_ok=True)
    report_filename = f"reports/{NOW.strftime('%Y-%m-%d')}.md"
    with open(report_filename, "w", encoding="utf-8") as f:
        f.write(md_content)

    print("周报与 shadcn/ui 看板数据更新完成！")


if __name__ == "__main__":
    main()
