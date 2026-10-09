import os
import json
import re
import requests
from datetime import datetime, timezone

# 基础配置
GH_TOKEN = os.getenv("GH_PAT")
USERNAME = os.getenv("GITHUB_ACTOR", "stephenchou888")

HEADERS = {
    "Authorization": f"Bearer {GH_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "GitHub-Stars-Digest"
}

CACHE_FILE = "data/cache.json"
NOW = datetime.now(timezone.utc)

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
    # 若已经包含较多中文字符，则直接返回原文
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

    if any(k in text_corpus for k in ["ai", "llm", "agent", "gpt", "claude", "ollama", "dify", "chatgpt", "langchain", "prompt", "vision", "model"]):
        return "🤖 AI 与智能体生态"
    elif any(k in text_corpus for k in ["proxy", "v2ray", "xray", "clash", "sing-box", "hysteria", "vpn", "trojan", "passwall", "network", "tunnel"]):
        return "🌐 网络与代理技术"
    elif any(k in text_corpus for k in ["music", "video", "media", "player", "audio", "download", "bilibili", "youtube", "podcast"]):
        return "🎬 影音媒体与下载"
    elif any(k in text_corpus for k in ["office", "pdf", "markdown", "editor", "docs", "sheets", "photoshop", "desktop", "ui", "notes"]):
        return "📝 效率办公与创作"
    elif any(k in text_corpus for k in ["docker", "linux", "cli", "terminal", "tool", "devtools", "extension", "utility", "script"]):
        return "🛠️ 系统与开发者工具"
    else:
        return "📦 实用开源精选"

def check_health(repo):
    """判断维护健康状态"""
    if repo.get("archived", False):
        return "abandoned", "作者已正式归档 (Archived)"
    
    pushed_at_str = repo.get("pushed_at")
    if not pushed_at_str:
        return "abandoned", "无代码提交记录"
        
    pushed_at = datetime.fromisoformat(pushed_at_str.replace("Z", "+00:00"))
    days = (NOW - pushed_at).days
    
    if days > 365:
        return "abandoned", f"超过 {days} 天无代码提交"
    elif days > 90:
        return "stale", f"近 {days} 天未更新（低频维护）"
    return "active", f"{days} 天前有活跃更新"

def extract_and_summarize_highlights(release_notes):
    """提取核心条目并自动翻译为简洁中文"""
    if not release_notes or not release_notes.strip():
        return "该版本未提供详细更新说明。"

    # 优先截取 What's Changed / Features 区块
    pattern = r"(?i)#{1,4}\s*(features|what's changed|new|highlights|changelog)(.*?)(?=#{1,4}\s|\Z)"
    match = re.search(pattern, release_notes, re.DOTALL)
    target_text = match.group(2) if match else release_notes

    # 提取有价值的更新行（过滤噪音）
    valid_lines = []
    for line in target_text.splitlines():
        line = line.strip()
        if line.startswith(("- ", "* ")) and len(line) > 5:
            lower = line.lower()
            if not any(noise in lower for noise in ["chore:", "ci:", "bump", "typo", "merge pull request"]):
                # 剔除作者标签如 (@author)
                cleaned = re.sub(r'\(?@[\w-]+\)?', '', line).strip()
                valid_lines.append(cleaned)
        if len(valid_lines) >= 3:
            break

    if valid_lines:
        combined_en = "\n".join(valid_lines)
        zh_text = translate_to_zh(combined_en)
        return zh_text

    # 无列表结构时截取前 250 字翻译
    clean_text = re.sub(r'#+\s*', '', release_notes).strip()[:250]
    return translate_to_zh(clean_text)

def check_repo_updates(repo, cache):
    full_name = repo["full_name"]
    url = f"https://api.github.com/repos/{full_name}/releases/latest"
    resp = requests.get(url, headers=HEADERS)
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
            "raw_body": data.get("body", "")
        }

    raw_desc = repo.get("description") or "暂无项目描述"
    desc_zh = translate_to_zh(raw_desc)
    raw_body = data.get("body", "")
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
    
    # 统计分类
    categories = {}
    for item in active_updates:
        cat = item["category"]
        categories.setdefault(cat, []).append(item)

    md = [
        f"# 📡 Starred 项目雷达看板",
        f"> **生成时间**：`{date_str}` ｜ **关注项目总数**：`{total_count}` ｜ **本期更新**：`{len(active_updates)}` ｜ **弃坑预警**：`{len(abandoned_repos)}`\n",
        "| 统计指标 | 数量 | 状态提示 |",
        "| :--- | :---: | :--- |",
        f"| 🌟 总关注库 | **{total_count}** | 监控运行中 |",
        f"| 🚀 近期有更新 | **{len(active_updates)}** | 涵盖 {len(categories)} 个分类 |",
        f"| 🛑 建议清理/弃坑 | **{len(abandoned_repos)}** | 建议取消 Star 保持关注列表整洁 |",
        "\n---",
        "## 🧭 领域分类速览导航\n"
    ]

    for cat, items in categories.items():
        md.append(f"- [{cat} ({len(items)})](#{cat.replace(' ', '-').replace('🤖', '').replace('🌐', '').replace('🎬', '').replace('📝', '').replace('🛠️', '').replace('📦', '').strip()})")

    md.append("\n---")

    # 分类展示
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
            
            # 折叠原生英文发布说明，保持页面干净整洁
            if item['raw_body'].strip():
                md.append("<details>")
                md.append("<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>\n")
                md.append("```markdown")
                md.append(item['raw_body'][:1500].strip())
                md.append("```")
                md.append("</details>\n")
            md.append("---")

    # 弃坑项目清单
    md.append("\n## 🛑 建议清理 / 放弃维护项目\n")
    md.append("<details>")
    md.append(f"<summary>⚠️ 点击展开已放弃维护或超过 1 年停更的仓库清单 ({len(abandoned_repos)} 个)</summary>\n")
    md.append("| 仓库名称 | Stars | 状态说明 | 操作建议 |")
    md.append("| :--- | :---: | :--- | :---: |")
    for item in abandoned_repos:
        md.append(f"| [{item['repo']}]({item['html_url']}) | {item['stars']:,} | {item['reason']} | [进入取消 Star]({item['html_url']}) |")
    md.append("</details>\n")

    return "\n".join(md)

def main():
    print(f"正在拉取 @{USERNAME} 的 Star 列表...")
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{USERNAME}/starred?per_page=100&page={page}"
        resp = requests.get(url, headers=HEADERS)
        if resp.status_code != 200:
            break
        data = resp.json()
        if not data or not isinstance(data, list):
            break
        repos.extend(data)
        page += 1

    total = len(repos)
    print(f"共获取到 {total} 个 Star 项目。")

    cache = load_cache()
    active_updates = []
    abandoned_repos = []

    for idx, repo in enumerate(repos, 1):
        full_name = repo["full_name"]
        status, reason = check_health(repo)

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
                cat = classify_repo(repo)
                active_updates.append({
                    "repo": full_name,
                    "html_url": repo["html_url"],
                    "stars": repo.get("stargazers_count", 0),
                    "language": repo.get("language") or "Other",
                    "category": cat,
                    "tag": update_info["tag"],
                    "release_url": update_info["url"],
                    "published_at": update_info["published_at"],
                    "desc_zh": update_info["desc_zh"],
                    "summary_zh": update_info["summary_zh"],
                    "raw_body": update_info["raw_body"]
                })

    save_cache(cache)

    md_content = generate_markdown(active_updates, abandoned_repos, total)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(md_content)

    os.makedirs("reports", exist_ok=True)
    report_filename = f"reports/{NOW.strftime('%Y-%m-%d')}.md"
    with open(report_filename, "w", encoding="utf-8") as f:
        f.write(md_content)

    print("周报更新完成！")

if __name__ == "__main__":
    main()
