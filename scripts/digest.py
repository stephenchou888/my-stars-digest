import os
import json
import re
import requests
from datetime import datetime, timezone

# 环境变量与配置
GH_TOKEN = os.getenv("GH_PAT")
USERNAME = os.getenv("GITHUB_ACTOR", "stephenchou888")
MODELS_ENDPOINT = "https://models.github.ai/inference/chat/completions"

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

def get_all_starred_repos(username):
    """分页拉取用户 Star 的所有项目元数据"""
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{username}/starred?per_page=100&page={page}"
        resp = requests.get(url, headers=HEADERS)
        if resp.status_code != 200:
            print(f"获取 Star 列表失败: {resp.status_code} {resp.text}")
            break
        data = resp.json()
        if not data or not isinstance(data, list):
            break
        repos.extend(data)
        page += 1
    return repos

def check_health(repo):
    """判断维护健康状态"""
    if repo.get("archived", False):
        return "abandoned", "项目已被作者正式归档 (Archived)"
    
    pushed_at_str = repo.get("pushed_at")
    if not pushed_at_str:
        return "abandoned", "无代码提交记录"
        
    pushed_at = datetime.fromisoformat(pushed_at_str.replace("Z", "+00:00"))
    days = (NOW - pushed_at).days
    
    if days > 365:
        return "abandoned", f"已连续 {days} 天无代码提交"
    elif days > 90:
        return "stale", f"近 {days} 天未更新（低频维护）"
    return "active", f"{days} 天前有活跃更新"

def extract_fallback_summary(release_notes):
    """当 AI 调用异常或无响应时的本地离线提取兜底"""
    if not release_notes or not release_notes.strip():
        return "该版本未提供详细更新说明。"
    
    # 策略 1: 提取以 - 或 * 开头的前 3 条核心更新项（自动过滤 CI、依赖和琐碎改动）
    items = []
    for line in release_notes.splitlines():
        line = line.strip()
        if line.startswith(("- ", "* ")) and len(line) > 5:
            lower = line.lower()
            if not any(noise in lower for noise in ["chore:", "ci:", "bump", "doc:", "typo", "merge pull request"]):
                items.append(line)
        if len(items) >= 3:
            break
            
    if items:
        return "\n".join(items)
    
    # 策略 2: 无列表格式时，过滤 Markdown 标题符号后截取前 200 字
    clean_text = re.sub(r'#+\s*', '', release_notes).strip()
    return clean_text[:200] + ("..." if len(clean_text) > 200 else "")

def summarize_with_github_models(repo_name, release_notes):
    """调用 GitHub Models 官方端点总结亮点，带自动容灾兜底"""
    if not release_notes or not release_notes.strip():
        return "该版本未提供详细更新说明。"

    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": (
                    "你是一个资深开源观察家。请根据提供的 GitHub Release Notes，"
                    "用中文提炼出该版本的 1-3 个核心亮点/破坏性变更。"
                    "要求语言精炼、直击痛点，按列表项输出，不要说客套废话。"
                )
            },
            {
                "role": "user",
                "content": f"项目: {repo_name}\n\n更新日志:\n{release_notes[:2500]}"
            }
        ],
        "temperature": 0.2,
        "max_tokens": 250
    }

    try:
        resp = requests.post(MODELS_ENDPOINT, headers=HEADERS, json=payload, timeout=20)
        if resp.status_code == 200:
            content = resp.json()["choices"][0]["message"]["content"].strip()
            if content:
                return content
        else:
            print(f"[{repo_name}] Models 接口响应异常 [{resp.status_code}]: {resp.text}")
    except Exception as e:
        print(f"[{repo_name}] 请求 Models 异常: {e}")

    # 模型调用失败时，自动切换至本地规则提取
    return extract_fallback_summary(release_notes)

def check_repo_updates(full_name, cache):
    """检查是否有新增的 Release 并进行亮点摘要"""
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
    
    # 只关注近 30 天内发布的 Release
    if (NOW - published_at).days > 30:
        return None

    # 若缓存中已记录该版本且有内容，直接复用缓存
    cached_tag = cache.get(full_name, {}).get("last_tag")
    cached_summary = cache.get(full_name, {}).get("summary", "")
    if cached_tag == tag_name and cached_summary and "超时或失败" not in cached_summary:
        return {
            "tag": tag_name,
            "url": data.get("html_url"),
            "published_at": published_at_str[:10],
            "summary": cached_summary
        }

    # 处理新版本或覆盖之前的失败摘要
    body = data.get("body", "")
    summary = summarize_with_github_models(full_name, body)

    # 写入缓存
    cache[full_name] = {
