# 📡 Starred 项目雷达看板
> 🖥️ **交互式管理看板 (shadcn/ui)**：[👉 点击进入在线雷达看板 (https://stephenchou888.github.io/my-stars-digest/)](https://stephenchou888.github.io/my-stars-digest/)

> **生成时间**：`2026-11-02` ｜ **关注项目总数**：`377` ｜ **本期更新**：`83` ｜ **弃坑预警**：`136`

| 统计指标 | 数量 | 状态提示 |
| :--- | :---: | :--- |
| 🌟 总关注库 | **377** | [进入 shadcn 在线看板管理](https://stephenchou888.github.io/my-stars-digest/) |
| 🚀 近期有更新 | **83** | 涵盖 6 个分类 |
| 🛑 建议清理/弃坑 | **136** | 建议取消 Star 保持关注列表整洁 |

---
## 🧭 领域分类速览导航

- [🤖 AI 与智能体生态 (43)](#-AI-与智能体生态)
- [📦 实用开源精选 (6)](#-实用开源精选)
- [🎬 影音媒体与下载 (12)](#-影音媒体与下载)
- [📝 效率办公与创作 (8)](#-效率办公与创作)
- [🌐 网络与代理技术 (12)](#-网络与代理技术)
- [🛠️ 系统与开发者工具 (2)](#-系统与开发者工具)

---

## <span id="-AI-与智能体生态">🤖 AI 与智能体生态</span>

### 📦 [openai/codex](https://github.com/openai/codex)
`⭐ Stars: 132,796` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [rust-v0.166.0](https://github.com/openai/codex/releases/tag/rust-v0.166.0) (2026-10-29)`

> **简介**：在您的终端中运行的轻量级编码代理

**💡 核心亮点更新 (中文)**：
- 添加了键盘驱动的转录选择，包括单词、行和页面动作、集成搜索和可配置的快捷方式。 （#57221、#57222、#57223、#57224）
- 在异步问题、选择、答案和文字回复中一致地呈现 Markdown。 （＃57259，＃57292）
- 将 GPT-6.1 Terra 添加到捆绑、Vertex AI 和 Amazon Bedrock 模型目录中。 (#57293)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## New Features

- Added keyboard-driven transcript selection with word, line, and page motions, integrated search, and configurable shortcuts. (#57221, #57222, #57223, #57224)
- Rendered Markdown consistently in async questions, choices, answers, and transcript replies. (#57259, #57292)
- Added GPT-6.1 Terra to the bundled, Vertex AI, and Amazon Bedrock model catalogs. (#57293)
- Added `codex queue --resume` to resume unloaded threads after queueing a message. (#57232)
- Added clearer safety-block explanations and selectable safer follow-up prompts in the TUI. (#57363, #57365)
- Added `codex doctor --network-only` for focused configuration, connectivity, and WebSocket diagnostics. (#57606)

## Bug Fixes

- Preserved acknowledged approval and permission settings when resuming or forking threads. (#57227)
- Preserved local image attachments when restoring killed composer text. (#57502)
- Fixed standalone release cleanup on macOS when installations are in use or paths contain non-ASCII characters. (#57503)
- Restored spawned descendant threads when unarchiving their parent. (#57635)
- Fixed app-server thread startup and shutdown races and released completed runtimes promptly. (#57787, #57788)
- Improved TUI reconnection recovery, including offline `/quit` and `/exit` handling. (#57820)
- Preserved reasoning-token accounting across resume and fork to avoid premature compaction. (#57839)

## Chores

- Switched Bazel to source-built V8 with target-matched Rust bindings and native
```
</details>

---
### 📦 [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)
`⭐ Stars: 14,874` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.3.1](https://github.com/akitaonrails/ai-memory/releases/tag/v3.3.1) (2026-11-01)`

> **简介**：用于代理编码 CLI 的长期记忆解决方案，并促进不同代理供应商之间的切换

**💡 核心亮点更新 (中文)**：
校验和 (SHA256)
````
cf5532fa6240c604915ab993530dc690afc774c914f7c88fe0b615638b4589e0 ai-内存-3.3.1-1.aarch64.rpm
42c6a8efd9c4f72124d2f5d0ce6b48c5a888cdc8b28d1f3bc974ff619de8568d ai内存-3.3.1-1.x86_64.rpm
10f7dbdbb925d786a1a55b1f8e285be5b4d7

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Checksums (SHA256)
```
cf5532fa6240c604915ab993530dc690afc774c914f7c88fe0b615638b4589e0  ai-memory-3.3.1-1.aarch64.rpm
42c6a8efd9c4f72124d2f5d0ce6b48c5a888cdc8b28d1f3bc974ff619de8568d  ai-memory-3.3.1-1.x86_64.rpm
10f7dbdbb925d786a1a55b1f8e285be5b4d796fa63beabc1f98bda62d8b177d2  ai-memory-claude-plugin.zip
6229aa42d512e7359cc2d2c7395ed744cdbe9d0328cbd2f21c395c951b34456d  ai-memory-hooks.tar.gz
5b8b9030c247b091ac2bacbf181f52f8fdba9d4ed47cdef23faab874d4c94d9f  ai-memory-install-hooks
6a3ba000bd675a45f42236b68ea7c9e5818562a68379cee407ae26650b77cd57  ai-memory-linux-aarch64.tar.gz
2045a115745a949d89cfc6a709da110a29b98fd6f2b63a928442ce949550fad4  ai-memory-linux-x86_64.tar.gz
0289d5b6ed3d371216bf086addc65e5f1beedff76cf6e640ad9fe4ddba70a18a  ai-memory-macos-aarch64.tar.gz
991d6b1053bfe742f1a4e2de46627522b8a5bb4d4b48f50dfad73b122464e1ae  ai-memory-macos-x86_64.tar.gz
99dcde5b7af450fe6212b23eccb43af3f608aadcd6999bf8c484efc7d08705db  ai-memory-windows-x86_64.zip
6a91c44ffa2e85d3b5a6ce26a4ccff0286b91d08d276d2bb4d47c346b036ee8b  ai-memory-wrapper.cmd
12a996a3d59aeaafbd46e03505c258631b9527a799f44921bc0d87db462147a4  ai-memory-wrapper.ps1
9c325aca5340bdc9bf3c1d0c38d5a9f13df07249c0e60345ee12de651e64c5bb  ai-memory-wrapper
6b105e4c8e6bcb3a2561a5316615a5c577b4074df24a1414ea45d306c1c7b89a  install.ps1
758c5d19348120619bbf8246b18975685daea2a2443017b47cd69ee64d6340bd  install.sh
```

## Install
```bash
# Linux/macOS, no root: checksum-verified release binary under ~/.local, then one-step set
```
</details>

---
### 📦 [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)
`⭐ Stars: 53,926` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.7.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.7.1) (2026-10-31)`

> **简介**：DeepTutor：终身个性化辅导。 https://deeptutor.info/。

**💡 核心亮点更新 (中文)**：
- **完整应用程序：** 停止 DeepTutor 并备份运行时主目录，然后运行 ​​`python -m pip install --upgrade "deeptutor[full]==1.7.1"`。保持相同的“DEEPTUTOR_HOME”，运行“python -m pip check”和“deeptutor module list”，然后重新启动。
- **旧版安装：** 从 1.6.15 或更早版本升级必须先卸载旧版 `deeptutor-cli` 软件包，然后再安装新软件包系列。按照[v1.7.0](ver1-7-0.md)中的迁移命令进行操作；运行时主目录数据与已安装的包保持分离。
- **源安装：**安装 `requirements/full.txt`，然后安装 `python -m pip install -e 。 --无部门`。核心轮和功能轮必须使用配套版本；在更改模块之前停止活动服务器和 CLI 轮流。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# DeepTutor v1.7.1 Release Notes

**Release Date:** 2026.11.01

Building on [v1.7.0](ver1-7-0.md), v1.7.1 introduces Open DeepTutor desktop previews, broader localization, and substantial improvements to chat, lessons, accounts, providers, and document handling. Existing runtime data stays in place; no manual migration is required.

## What's New

### Open DeepTutor desktop previews

Open DeepTutor bundles Python, Node.js, and the full learning workspace into a desktop app for Apple Silicon Macs, Intel Macs, and Windows x64. Preview builds are available from the Desktop Release workflow, with DMG downloads for macOS and Setup or portable ZIP options for Windows.

### More languages and account controls

Vietnamese, Japanese, Turkish, and Brazilian Portuguese join the interface and reply-language options, alongside expanded translations, regional date formatting, and right-to-left rendering. Account-scoped learning text controls adjust font size and line spacing. Users can change their passwords from Profile, while accounts still using an admin-assigned temporary password receive a change prompt.

### Chat that keeps your work and sources together

Unsent composer drafts survive navigation, and conversational creation drafts retain early work. Message-level Little Tutor threads can recover, move, or clear their source anchor without losing the surrounding conversation. Generated files gain consistent open and download controls, while editing or resending a message uses the cur
```
</details>

---
### 📦 [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)
`⭐ Stars: 107,774` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.6.1](https://github.com/Panniantong/Agent-Reach/releases/tag/v1.6.1) (2026-11-01)`

> **简介**：让您的人工智能代理有一双能够看到整个互联网的眼睛。阅读和搜索 Twitter、Reddit、YouTube、GitHub、Bilibili、小红书 — 一个 CLI，零 API 费用。

**💡 核心亮点更新 (中文)**：
- 全网搜索、Reddit、小红书、B站在 1.6.0 里会出现的几种"明明能查却报错"或"显示成功但内容是空的"，这版都修好了。
- 电脑上别的软件占用了浏览器端口时，可以换一个端口，不用关掉那个软件。
- 复制登录失败时会如实告诉你，不再假装成功。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
中文：

- 全网搜索、Reddit、小红书、B站在 1.6.0 里会出现的几种"明明能查却报错"或"显示成功但内容是空的"，这版都修好了。
- 电脑上别的软件占用了浏览器端口时，可以换一个端口，不用关掉那个软件。
- 复制登录失败时会如实告诉你，不再假装成功。
- Windows 上小红书带特殊符号的链接能正常打开了。

English:

- Several 1.6.0 cases where web search, Reddit, Xiaohongshu or Bilibili failed although the content was reachable, or reported success with empty content, are fixed.
- When another program on your computer uses the browser port, Agent Reach can use a different one; you don't have to close that program.
- A login copy that fails now says so instead of reporting success.
- On Windows, Xiaohongshu links with special characters open correctly.

中文（技术细节）：
- 全网搜索：请求统一带上 `agent-reach/<版本号>` 标识，避免被 Exa 的防护拦截（#877）。
- Reddit：站内工具临时失败（比如返回网页而不是数据）时，自动改用公开网页搜索和阅读（#880）。
- 小红书：适配 OpenCLI 2.0 的返回格式，阅读不再"成功但内容全空"；搜索和评论没有结果时也不再返回一条空数据（#861、#895）。
- B站：扫码后如果没存下有效登录，不再显示登录成功；提示改为运行 `agent-reach login bilibili`（#866、#883）。
- 专用浏览器端口可以改：`agent-reach configure browser-port <端口>`，9222 被别的软件占用时用（#848）。
- 复制登录：浏览器后台程序没开时不再记一次"复制了 0 条"；手动 `login <渠道> --import-existing` 一条都没复制到时会明确报错（#879）。
- Windows：链接里带 `&` 的小红书笔记能正常阅读和查看评论（#860）。

English (technical):
- Web search: every request identifies itself as `agent-reach/<version>`, so Exa's Cloudflare front no longer blocks it (#877).
- Reddit: when the site tool fails transiently (for example it returns HTML instead of data), search and read fall back to the public web (#880).
- Xiaohongshu: OpenCLI 2.0 results are mapped, so read no longer succeeds with empty fields; search and comme
```
</details>

---
### 📦 [Hsiung-Shao/exile-appraiser](https://github.com/Hsiung-Shao/exile-appraiser)
`⭐ Stars: 8` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.3.4](https://github.com/Hsiung-Shao/exile-appraiser/releases/tag/v0.3.4) (2026-10-30)`

> **简介**：ExileAppraiser / 流亡鑑價:Path of Exile 1/2 查價器,支援國際服與台服(繁中/英文客戶端)

**💡 核心亮点更新 (中文)**：
修正

・**PoE1 掛單物品浮窗**：催化劑品質、無形性、記憶絲縷不再顯示英文。（例：品質 (能力值詞綴)）
・**PoE2 掛單物品浮窗**：品質、催化劑品質、等級、堆疊數量、區域等級、試煉數量不再顯示英文。
  ⚠ 技能寶石的消耗、施放時間，以及藥劑、護符的效果說明仍是英文。

調整

・**支援遊戲版本**：關於頁的 PoE2 版本 0.5.5d → 0.5.5e。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 修正

・**PoE1 掛單物品浮窗**：催化劑品質、無形性、記憶絲縷不再顯示英文。（例：品質 (能力值詞綴)）
・**PoE2 掛單物品浮窗**：品質、催化劑品質、等級、堆疊數量、區域等級、試煉數量不再顯示英文。
  ⚠ 技能寶石的消耗、施放時間，以及藥劑、護符的效果說明仍是英文。

## 調整

・**支援遊戲版本**：關於頁的 PoE2 版本 0.5.5d → 0.5.5e。
```
</details>

---
### 📦 [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model)
`⭐ Stars: 56,281` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.8.0-macos-unofficial](https://github.com/Ebony-Vinyl/dsh-our-free-model/releases/tag/v2.8.0-macos-unofficial) (2026-11-01)`

> **简介**：在 dsh 里装上这个插件即可，无需登录、注册或填 API Key，就能使用包括 DeepSeek V4.1 Flash、Kimi K3 在内的前沿模型——完全免费，不限量。 All you do is install this plugin in dsh: no login, no sign-up, no API key — the frontier models are just there, DeepSeek V4.1 Flash and Kimi K3 among them. Completely free, with no usage cap.

**💡 核心亮点更新 (中文)**：
- 构建来源 / Source: v2.8.0 @ 999e9f784ea3ea7a11cae383b142697b1ff2c42f
- 构建记录 / CI run: https://github.com/Ebony-Vinyl/dsh-our-free-model/actions/runs/41273574493
- SHA256: abcf9304c6ac87199a5f0fc9dff46b944c002a1c83c30c6cdb7fd00aa59e906b

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 非官方社区构建 / Unofficial community build

这不是仓库作者发布的官方安装包。作者自 2.4.0 起将桌面安装包限制为 Windows-only，Mac 用户停留在 2.3.0。本 dmg 由本仓库的 GitHub Actions 从公开源码构建，可审计、可复现。

This is NOT an official release by the repository author. The author restricted desktop installers to Windows-only since 2.4.0, leaving Mac users on 2.3.0. This dmg is built by GitHub Actions from public, auditable source.

| 项 / Item | 值 / Value |
|---|---|
| 版本 / Version | 2.7.1 |
| 架构 / Arch | arm64 |

### 可信性 / Trust

1. 构建来自当前标签对应的公开源码，可逐行审计。
2. 本 dmg 正是你正在查看的这次 Actions 运行的产物，由 GitHub macOS runner 构建；任何人 fork 后重跑同一 workflow 即可复现。
3. 下载后请核对下方 SHA256。

### 「已损坏」/ "damaged" 怎么办？/ How to open

本包未经 Apple 签名与公证（社区构建没有 Apple Developer 账号），Gatekeeper 会拦截首次启动，并非文件损坏。任选其一：

The package is unsigned / not notarized (a community build has no Apple Developer account), so Gatekeeper blocks first launch. The file is NOT damaged. Pick any one:

1. 访达中右键（Control 点按）应用图标 → 「打开」→ 再次确认。In Finder, Control-click the app → Open → confirm again.
2. 终端清除隔离属性 / remove the quarantine attribute:



3. 仍提示损坏时用 sudo / if it still complains:



4. 系统设置 → 隐私与安全性 → 「仍要打开」。System Settings → Privacy & Security → Open Anyway.


---
- 构建来源 / Source: v2.8.0 @ 999e9f784ea3ea7a11cae383b142697b1ff2c42f
- 构建记录 / CI run: https://github.com/Ebony-Vinyl/dsh-our-free-model/actions/runs/41273574493
- SHA256: abcf9304c6ac87199a5f0fc9dff46b944c002a1c83c30c6cdb7fd00aa59e906b
```
</details>

---
### 📦 [hypit-ai/hypit](https://github.com/hypit-ai/hypit)
`⭐ Stars: 27,422` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.3.1](https://github.com/hypit-ai/hypit/releases/tag/v0.3.1) (2026-10-09)`

> **简介**：使用人工智能代理克隆任何病毒视频。不仅仅是一个脚本，而是整个工作流程：交换面孔、文字、幕后花絮，在一个命令中发送 100 个变体，并获得 1 亿次观看。

**💡 核心亮点更新 (中文)**：
- 视频域 SDK 是独立版本的 npm 包。默认视频功能仍随 Hypit 安装；通用主机 API 保留在 /hypit 下。
- Studio 解析计算的 CaptionTiming 引用，即使没有 Track 消耗它们，也会显示命名的 Instant，并保留紧凑的统一时间轴标题和投影行。窗口通过其消耗的跟踪项目保持可见。
- Studio 观察原子源文件替换，并随着加载的源闭包更改而更新监视。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Upgrade notice

Existing 0.3.0 project components may need SDK import and dependency updates. Read the [0.3.1 migration guide](https://github.com/hypit-ai/hypit/blob/v0.3.1/migrations/0.3.1.md) before updating a production. Preserve existing Sources, Runs and Results; update the project lockfile deliberately.

## Changes

- Video-domain SDKs are independently versioned npm packages. Default video capabilities still install with Hypit; generic host APIs remain under @hypit/hypit.
- Studio resolves computed CaptionTiming references, displays named Instants even when no Track consumes them, and retains the compact unified Timeline header and projection rows. Windows remain visible through their consuming Track Items.
- Studio observes atomic Source-file replacement and updates watches as the loaded Source closure changes.
- Pricing reports Producer failures completely and exits unsuccessfully when planning fails.
- Skill and documentation use the current SDK package names and installed Studio paths. The Skill updates separately through `npx skills add hypit-ai/hypit -g`.

For an existing global CLI installation, use `npm install -g @hypit/hypit@0.3.1` after publication completes. For a project-local installation, update the existing package.json and lockfile using the project package manager and migration guide.

This release does not publish the optional partner Provider packages or the four optional ecosystem components.
```
</details>

---
### 📦 [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app)
`⭐ Stars: 20,198` &nbsp;|&nbsp; `💻 语言: Vue` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.0.9](https://github.com/HBAI-Ltd/Toonflow-app/releases/tag/v2.0.9) (2026-10-31)`

> **简介**：短剧、漫剧制作工具 Toonflow：开源 AI 视频创作平台，集成剧本创作、智能分镜、角色与场景资产管理、图像生成和视频生成。融合无限画布、AI Agent 与可视化工作流，支持本地部署、自选模型、跨平台客户端、MCP 与插件扩展。Open-source AI short drama and motion comic creation tool with an infinite canvas, AI agents, storyboarding, image and video generation. Self-hosted and extensible, with a canvas-based approach similar to LibTV and TapNow.

**💡 核心亮点更新 (中文)**：
- 💻 **Windows**：双击下载的安装包，按提示完成安装。
- 🍎 **Mac**：打开下载的安装包，将 `toonflow.app` 拖入“应用程序”，再从“应用程序”打开。
- 📱 **Android**：在手机上打开 APK，按系统提示允许此来源安装应用。后续版本可直接覆盖安装。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 📦 下载指南

选择你的设备对应的安装包，点击即可下载：

| 你的设备 | 下载 |
| --- | --- |
| 💻 Windows（64 位） | [⬇️ 下载 Windows 安装包](https://github.com/HBAI-Ltd/Toonflow-app/releases/download/v2.0.9/toonflow-2.0.9-Setup.exe) |
| 🍎 Mac（M 系列芯片） | [⬇️ 下载 M 系列 Mac 安装包](https://github.com/HBAI-Ltd/Toonflow-app/releases/download/v2.0.9/macos-arm64-toonflow.dmg) |
| 🍎 Mac（Intel 芯片） | [⬇️ 下载 Intel Mac 安装包](https://github.com/HBAI-Ltd/Toonflow-app/releases/download/v2.0.9/stable-macos-x64-toonflow.dmg) |
| 📱 Android（ARM64，Android 8 及以上） | [⬇️ 下载 Android APK](https://github.com/HBAI-Ltd/Toonflow-app/releases/download/v2.0.9/toonflow-2.0.9-android-arm64.apk) |

> 💡 手动安装请选择上表中的链接。下方其他文件供软件自动更新使用。

## 🚀 安装说明

- 💻 **Windows**：双击下载的安装包，按提示完成安装。
- 🍎 **Mac**：打开下载的安装包，将 `toonflow.app` 拖入“应用程序”，再从“应用程序”打开。
- 📱 **Android**：在手机上打开 APK，按系统提示允许此来源安装应用。后续版本可直接覆盖安装。

M 系列 Mac 安装包已完成 Developer ID 签名与 Apple 公证。首次打开时，macOS 仍可能提示确认打开从互联网下载的应用。

---


**Full Changelog**: https://github.com/HBAI-Ltd/Toonflow-app/compare/v2.0.8...v2.0.9
```
</details>

---
### 📦 [morluto/rea](https://github.com/morluto/rea)
`⭐ Stars: 419,977` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [rea-agents-6.8.0](https://github.com/morluto/rea/releases/tag/rea-agents-6.8.0) (2026-10-25)`

> **简介**：Reverse engineer anything with agents, from app behavior down to native binaries.

**💡 核心亮点更新 (中文)**：
- Build local agent environments from network captures, browser scenarios, or a prompt, then serve derived reads and evidence-gated writes and compare them with fresh application captures.
- Inspect more shipped formats, including GPU code objects, BEAM, Python bytecode, Unity IL2CPP metadata, Godot PCK, PyInstaller, Node.js SEA, devicetree, and additional PE/ELF tables.
- Keep large investigations focused with retained summaries, selected fact queries, configurable recovery limits, and row-oriented CLI exports. Complete Evidence remains available.

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## [6.8.0](https://github.com/morluto/rea/compare/rea-agents-6.7.0...rea-agents-6.8.0) (2026-10-25)

### Highlights

- Build local agent environments from network captures, browser scenarios, or a prompt, then serve derived reads and evidence-gated writes and compare them with fresh application captures.
- Inspect more shipped formats, including GPU code objects, BEAM, Python bytecode, Unity IL2CPP metadata, Godot PCK, PyInstaller, Node.js SEA, devicetree, and additional PE/ELF tables.
- Keep large investigations focused with retained summaries, selected fact queries, configurable recovery limits, and row-oriented CLI exports. Complete Evidence remains available.

### ⚠ BREAKING CHANGES

- **Function analysis:** `analyze_function` now defaults to a retained summary. Set `detail: "complete"` for the previous inline dossier; the CLI retains its complete default and requires `--evidence_output` when selecting a summary. [#5660](https://github.com/morluto/rea/pull/5660). Thanks @CryptoJones, @gensokyo-dev, @RishTheFish21.
- **Accessibility:** Accept JSON numbers and booleans in node `value`, alongside strings and null. Update consumers that previously assumed text-only values. [cc90771](https://github.com/morluto/rea/commit/cc90771af14f045538651615147d8bf86b576549), [#6759](https://github.com/morluto/rea/pull/6759), [#6467](https://github.com/morluto/rea/issues/6467). Thanks @coygeek, @gensokyo-dev, @mvanhorn.
- **JSON Lines:** `--format jsonl` now emits object-collection rows fo
```
</details>

---
### 📦 [chatfire-AI/huobao-drama](https://github.com/chatfire-AI/huobao-drama)
`⭐ Stars: 16,912` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v4.0.10](https://github.com/chatfire-AI/huobao-drama/releases/tag/v4.0.10) (2026-11-01)`

> **简介**：🎬 火宝短剧 - 基于AI的一站式短剧生成平台 《一句话生成完整短剧，从剧本到成片全自动化》  Huobao Drama - An AI-Powered End-to-End Short Drama Generator "One Sentence to Complete Drama: Fully Automated from Script to Final Video"

**💡 核心亮点更新 (中文)**：
- 角色资产支持上传、试听、替换和移除音色样本。
- 分镜视频提示词支持在对白处使用 #角色名 引用音色，例如「0-3秒：，#林小雨轻声说：「早上好。」」。
- 首次分镜拆解、单条和批量视频提示词生成会依据角色绑定和可用音色生成引用。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
本次更新

- 角色资产支持上传、试听、替换和移除音色样本。
- 分镜视频提示词支持在对白处使用 #角色名 引用音色，例如「0-3秒：@林小雨抬头，#林小雨轻声说：「早上好。」」。
- 首次分镜拆解、单条和批量视频提示词生成会依据角色绑定和可用音色生成引用。
- 视频生成自动传入引用的音色，支持本地音频校验及格式转换。
- 修复 Windows 中文等非 ASCII 安装路径下的后端与媒体工具启动问题。

安装包覆盖 macOS Apple Silicon、macOS Intel 和 Windows x64。
Docker 镜像 huobao/huobao-drama:4.0.10 支持 linux/amd64 和 linux/arm64。
```
</details>

---
### 📦 [yetone/magpie](https://github.com/yetone/magpie)
`⭐ Stars: 27,973` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.1.2694](https://github.com/yetone/magpie/releases/tag/v0.1.2694) (2026-11-02)`

> **简介**：每个代理的模型。一处。来自菜单栏的 DeepSeek 上的 Codex、Kimi 上的 Claude Code。

**💡 核心亮点更新 (中文)**：
- codex：ChatGPT 后端拒绝的工具名称，作为它所采用的名称，并作为代理的名称返回
- **macOS（Apple Silicon）：** `magpie-darwin-arm64.dmg`
- **macOS（英特尔）：** `magpie-darwin-amd64.dmg`

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
### Changes

- codex: a tool name the ChatGPT backend refuses goes as one it takes, and comes back as the agent's

### Install

Download from [usemagpie.ai](https://usemagpie.ai), or `curl -fsSL https://usemagpie.ai/install.sh | sh`. An installed magpie updates itself.

- **macOS (Apple Silicon):** `magpie-darwin-arm64.dmg`
- **macOS (Intel):** `magpie-darwin-amd64.dmg`
- **Windows:** `magpie-windows-amd64.exe` (ARM: `magpie-windows-arm64.exe`)
- **Linux:** `magpie-linux-amd64` / `magpie-linux-arm64` (needs GTK 3 and WebKitGTK 4.1)
- **Terminal only:** `magpie-cli-<os>-<arch>`



---
The same release, and the feed magpie updates from: https://github.com/yetone/magpie-releases/releases/tag/v0.1.2694
```
</details>

---
### 📦 [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
`⭐ Stars: 259,607` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.22.5](https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.5) (2026-10-23)`

> **简介**：The agent that grows with you

**💡 核心亮点更新 (中文)**：
- Microsoft Store app: updates through the Store.
- Desktop app installed from the installer (.exe / .dmg): no change in this release; it updates with the next bundled release.
- CLI: `hermes update`, or re-run the installer one-liner.

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# Hermes Agent v0.22.5

**Release Date:** October 22, 2026

> Patch release. This tag rolls up the ~81 PRs merged since v0.22.4 into a stable release for the GitHub release (CLI and installers), the Microsoft Store app, Docker and Hermes Cloud. Full curated notes for this window ship with v0.23.0.

<!-- HERMES_BUILDS_TABLE -->

## About this release

Measured at commit `bf0203a794a`, the window since v0.22.4 contains **231 non-merge commits** across **804 changed files** (+35,212 / −17,885), **81 merged PRs** and **30 closed issues**.

Also in the window, undocumented here on purpose: Nous sign-in reworked (every sign-in is the plain device login, the free-tier guest hands over to your account, the result shows who signed in, connectors offer sign-in instead of opening a guest), `hermes update` holding back a stable release it refuses instead of offering it, Windows `hermes update` no longer stuck on the old launcher after a Python repin, usage-window plan support (plan gauges, limit cards and model-switch recovery for window-based plans), pluggable delegation backends (route subagents by model map or profile, switchable per session), plugin slash commands that can ask you to pick an option, `hermes import-agent`, OpenClaw migration, `hermes mcp serve` and the Singularity backend moving out of core into plugins (setup offers the importer when it finds another agent), Desktop drag-to-pin in the sidebar and one-click plugin installs with tier badges, the Electron 44 upgrade, Pi
```
</details>

---
### 📦 [Makememo/MemoAI](https://github.com/Makememo/MemoAI)
`⭐ Stars: 1,078` &nbsp;|&nbsp; `💻 语言: Other` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.8.9](https://github.com/Makememo/MemoAI/releases/tag/v1.8.9) (2026-10-26)`

> **简介**：MemoAI 视频翻译文本、字幕和注释变得简单。

**💡 核心亮点更新 (中文)**：
- 代理对话存档

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## New Features

- Agent conversation archiving

## Improvements

- Unified the player presentation for audio and video exports
- Migrated Agent conversation storage to the new location
- Upgraded Electron to 44.7.0 and removed legacy dependencies

## Fixes

- Fixed the missing scroll bar when saving TXT files (#435)
- Fixed a white screen on startup when the `HTTP_PROXY` environment variable is set
```
</details>

---
### 📦 [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)
`⭐ Stars: 11,527` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.12.446](https://github.com/genspark-ai/genoffice/releases/tag/v0.12.446) (2026-10-30)`

> **简介**：免费的开源 AI Office 套件：带有内置 AI 代理的文档、表格、幻灯片、PDF、Markdown 和 HTML 编辑器，以及“genoffice”CLI 和代理技能，以便 Claude Code、Codex 和 Cursor 可以在本地创建和编辑真正的 .docx/.xlsx/.pptx 文件。带上你自己的钥匙。 macOS、Windows 和 Linux。

**💡 核心亮点更新 (中文)**：
- **文档：**跟踪更改现在从头到尾跟随Word - 审阅窗格、显示标记过滤器和气球模式、每个作者的颜色、“跟踪更改选项”对话框、记录为移动对的移动以及可审阅的表格、编号、章节、脚注、标题和文本框修订；拒绝更改会恢复原始文本并运行格式（由 、 、 修复）报告；注释卡和注释切换与 Word 匹配，并且 AI 编辑记入设置用户名；非连续选择格式化、复制和删除每个范围（由 询问；字体菜单在大型文档上不再冻结（由 报告；浮动形状旋转并采用轮廓宽度 ；由 报告）；图片像 Word 一样移动、调整大小和重新选择；分页符保持不变编辑旁边的文本时放置；新表格采用 Word 的插入表格外观；从 100 个文档的 Word 比较中修复了数十个分页和字体规格。
- **工作表：**工作簿的拼写检查、假设数据表、组合图选择数据、数据透视图、x14 数据验证、持久表过滤器、允许编辑范围上的剩余显示值模式和密码；图片、合并和大小来自旧版 .xls 文件；具有绝对 OPC 目标或缺少 xfId 打开和重新计算的工作簿，由 , 报告；无头 PDF 导出打印每张已确定公式的工作表，并且 add_chart 接受公式范围，由 报告；保存到 SMB 共享可以容忍 fsync 被拒绝（由 报告；Ctrl+Y 重复上一个操作。
- **幻灯片：** JPG 页面导出；幻灯片编辑停止向 AI 重新发送内联媒体和完整幻灯片。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
GenOffice v0.12.446 stable desktop installers.

## What's New

- **Docs:** Track Changes now follows Word end to end — a Reviewing Pane, Show Markup filters and balloon modes, per-author colors, a Track Changes Options dialog, moves recorded as move pairs, and reviewable table, numbering, section, footnote, header and text-box revisions; rejecting a change restores the original text and run formatting (reported by @zidaliu32-hue, @speckofthecosmos, fix by @widechaos); comment cards and the Comments toggle match Word, and AI edits are credited to the Settings user name; non-contiguous selections format, copy and delete every range (asked by @wisnia2168); the font menu no longer freezes on large documents (reported by @elizeu5678); floating shapes rotate and take an outline width (@tokg-venv, asked by @Bembengs); pictures move, resize and reselect like Word (@ThallesCosta-dev); a page break stays put when the text beside it is edited (@ThallesCosta-dev); new tables take Word's Insert Table look; dozens of pagination and font-metric fixes from a 100-document Word comparison.
- **Sheets:** spelling check for workbooks, What-If data tables, combo-chart Select Data, PivotCharts, x14 data validation, persisted table filters, the remaining Show Values As modes and passwords on allow-edit ranges (@tokg-venv); pictures, merges and sizes come out of legacy .xls files (@tokg-venv); workbooks with absolute OPC targets or a missing xfId open and recalc (@tokg-venv, reported by @lepetitprin
```
</details>

---
### 📦 [ruvnet/RuView](https://github.com/ruvnet/RuView)
`⭐ Stars: 102,045` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [ruview-harness-v0.9.2](https://github.com/ruvnet/RuView/releases/tag/ruview-harness-v0.9.2) (2026-10-12)`

> **简介**：π RuView 将商用 WiFi 信号转化为实时空间智能、生命体征监测和存在检测 - 所有这些都无需视频像素。

**💡 核心亮点更新 (中文)**：
- 接受官方 C6 固件包文件名，同时保留校验和和板变体验证。
- 正确的 CSI 损失计算、观察到的捕获持续时间、主流选择和合成数据来源；拒绝格式错误的辅助数据包。
- 更正 ESPHome 单元和实体角色，报告不完整的串行捕获，并修复 LiDAR/mmWave 摘要和流完成。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
@ruvnet/ruview 0.9.2

Maintenance fixes from [PR #2248](https://github.com/ruvnet/RuView/pull/2248), which records the exact source heads for 38 integrated contributor PRs.

- Accept official C6 firmware bundle filenames while preserving checksum and board-variant validation.
- Correct CSI loss accounting, observed capture duration, dominant stream selection, and synthetic-data provenance; reject malformed auxiliary packets.
- Correct ESPHome units and entity roles, report incomplete serial captures, and fix LiDAR/mmWave summaries and stream completion.
- Validate CLI numeric arguments, preserve gaps in watch history, report corrupt manifests through doctor, and honor SDK strict errors.
- Replace inherited and explicit Windows hosts-file ACL grants with verified current-user-only access. Paths are passed as data to the bounded helper, including Unicode and shell-special characters.
- Preserve source recordings during transcoding, avoid capture-session filename collisions, and retain complete relayed UDP datagrams.
- Exercise the contributor harness on Linux and Windows and correct CI snapshot release metadata.

Install the exact package with `npm install @ruvnet/ruview@0.9.2`, or run its CLI using `npx @ruvnet/ruview@0.9.2 --help`.

Repository-only changes also improve Home Assistant client topic compatibility and the MTK bridge test lifecycle. These changes do not imply that a new Python wheel or hardware-qualified firmware was published with this npm package.

The release c
```
</details>

---
### 📦 [pascalorg/editor](https://github.com/pascalorg/editor)
`⭐ Stars: 25,270` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [@pascal-app/cli@1.0.6](https://github.com/pascalorg/editor/releases/tag/%40pascal-app/cli%401.0.6) (2026-10-23)`

> **简介**：Open-source 3D architectural editor with a local CLI, MCP tools, and practical workflows for humans and AI agents.

**💡 核心亮点更新 (中文)**：
The Pascal web editor runtime for `@pascal-app/cli@1.0.6`. The CLI downloads `pascal-web-runtime-1.0.6.tar.gz` the first time a command starts the editor and verifies it against the digest published inside the npm package. Offline installs can pass t

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
The Pascal web editor runtime for `@pascal-app/cli@1.0.6`. The CLI downloads `pascal-web-runtime-1.0.6.tar.gz` the first time a command starts the editor and verifies it against the digest published inside the npm package. Offline installs can pass the archive directly: `pascal editor --runtime pascal-web-runtime-1.0.6.tar.gz`.
```
</details>

---
### 📦 [librepods-org/librepods](https://github.com/librepods-org/librepods)
`⭐ Stars: 30,572` &nbsp;|&nbsp; `💻 语言: Kotlin` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.0.4](https://github.com/librepods-org/librepods/releases/tag/v1.0.4) (2026-10-16)`

> **简介**：AirPods 从苹果的生态系统中解放出来。

**💡 核心亮点更新 (中文)**：
- android：从foss切换到播放时改写横幅（[12e7f413](https://github.com/kavishdevar/librepods/commit/12e7f413deae2ff3630a32f00fd151bd19f143d0))
- android: 添加 ja 翻译 ([56570990](https://github.com/kavishdevar/librepods/commit/5657099096cc5e5ab4f53c19386af0b72e2b7c44))
- android: 会话 -> 会话意识 ([a383341d](https://github.com/kavishdevar/librepods/commit/a383341dd616177070f664400bfbec6ef582b1df))

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
<a href="https://play.google.com/store/apps/details?id=me.kavishdevar.librepods"><img width="170" alt="GetItOnGooglePlay_Badge_Web_color_English" src="https://github.com/user-attachments/assets/2948308f-af92-443f-94d9-ee381c3a6ccc"/></a>

## What's changed
- android: rephrase banner when switching from foss to play ([12e7f413](https://github.com/kavishdevar/librepods/commit/12e7f413deae2ff3630a32f00fd151bd19f143d0))
- android: add ja translation ([56570990](https://github.com/kavishdevar/librepods/commit/5657099096cc5e5ab4f53c19386af0b72e2b7c44))
- android: conversational -> conversation awareness ([a383341d](https://github.com/kavishdevar/librepods/commit/a383341dd616177070f664400bfbec6ef582b1df))
- android: update de translations ([45c61c41](https://github.com/kavishdevar/librepods/commit/45c61c4122114ba0cc3d63e6c0e4996a536d3e42))
- android: update zh-rCN translations ([2859b71a](https://github.com/kavishdevar/librepods/commit/2859b71a81acb0cf1429383303ac7bf75292ec44))
- android: add ko translations ([ff97656b](https://github.com/kavishdevar/librepods/commit/ff97656b89198619d1c132681b0cd62978354fc9))

**Full Changelog**: https://github.com/kavishdevar/librepods/compare/v1.0.3..v1.0.4

---
Some features on Play require an in-app purchase. The following features are free on Play:
    - Battery status
    - Ear detection
    - Changing Listening Mode
    - Press and Hold listening mode customization

But all builds released here will have all features availa
```
</details>

---
### 📦 [linshenkx/prompt-optimizer](https://github.com/linshenkx/prompt-optimizer)
`⭐ Stars: 40,318` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.14.0](https://github.com/linshenkx/prompt-optimizer/releases/tag/v2.14.0) (2026-11-02)`

> **简介**：人工智能提示优化器，用于编写更好的提示并获得更好的人工智能结果。

**💡 核心亮点更新 (中文)**：
- **发现本地模型服务：** 文本模型管理器识别受支持的可访问服务，并提供现有连接编辑器的快捷方式，以及特定于提供程序的设置指南。
- **更清晰的工作区控件：** 一致的图标、紧凑的源和模型选择器以及响应式工具栏使配置和输出操作更容易找到。
- **检查正在测试的提示：** 将鼠标悬停在桌面上阅读源预览，或直接打开其完整内容。源标签和模型选择与相应的工作区保持联系。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## English

### Summary

This release adds local-service discovery and guided model setup, unifies workspace controls and model selection, and reorganizes data management and cloud backups. It also adds prompt-source hover previews and fixes configuration fields that could not be cleared reliably, category-parent clearing, and delayed hover previews covering the full-prompt dialog.

### Highlights

- **Discover local model services:** the text model manager identifies supported reachable services and offers a shortcut to the existing connection editor, with provider-specific setup guidance.
- **Clearer workspace controls:** consistent icons, compact source and model selectors, and responsive toolbars make configuration and output actions easier to find.
- **Inspect the prompt being tested:** hover to read a source preview on desktop, or open its full content directly. Source labels and model selection stay tied to the corresponding workspace.
- **Organized data management:** review device storage, export or restore a local file, and manage cloud backups through distinct sections with clearer connection and loading states.

### Product Updates

#### Desktop

- Add controlled local-service probes through the desktop bridge and guided model connection setup.
- Preserve explicit field clears across desktop IPC when saving model configurations.
- Apply the shared workspace, source-preview and data-management improvements, including saved cloud-backup connection credentials and rea
```
</details>

---
### 📦 [RSSNext/Folo](https://github.com/RSSNext/Folo)
`⭐ Stars: 39,212` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [desktop/v1.17.0](https://github.com/RSSNext/Folo/releases/tag/desktop/v1.17.0) (2026-11-02)`

> **简介**：🧡 Folo 是人工智能 RSS 阅读器

**💡 核心亮点更新 (中文)**：
- 新的“自动播放视频”设置：将其关闭，YouTube 和 Bilibili 嵌入、悬停预览和媒体预览在播放前等待点击
- 离线或无法访问服务器时所做的更改将被保留，并在连接恢复后立即发送；只有服务器拒绝的更改才会被撤消，应用程序会告诉您原因
- 离线，没有存储条目的提要表示它处于离线状态，而不是永久加载，并在您重新上线后加载

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# What's new in v1.17.0

## Shiny new things

- New "Autoplay videos" setting in General: turn it off and YouTube and Bilibili embeds, hover previews and media previews wait for a click before playing

## Improvements

- Changes made offline or while the server is unreachable are kept and sent as soon as the connection is back; only changes the server refuses are undone, and the app tells you why
- Offline, a feed without stored entries says it is offline instead of loading forever, and loads once you are back online
- Find in page keeps every keystroke, no longer counts its own text, steps through matches in order, has its editing menu back and leaves no highlights behind after closing
- Links to footnotes and other sections inside an entry scroll to them
- RSSHub routes that need a paid plan, such as X (Twitter), show an upgrade button in the follow form instead of a fetch error
- The RSSHub page explains that Folo's built-in instance is used first and your own instance is the fallback, and checks an instance address before saving it
- Editing Actions on two devices no longer overwrites the other device's rules: you can load the latest rules, keep editing or save over them
- Clearer, translated errors for a wrong email or password, too many requested emails, refused sign-in links and provider sign-ins, feeds the follow form could not load, and an unreachable server instead of "Failed to fetch"
- Verified accounts are told that an email change is approved from the current ad
```
</details>

---
### 📦 [roboflow/supervision](https://github.com/roboflow/supervision)
`⭐ Stars: 51,457` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [0.31.3](https://github.com/roboflow/supervision/releases/tag/0.31.3) (2026-10-28)`

> **简介**：我们为您编写可重复使用的计算机视觉工具。 💜

**💡 核心亮点更新 (中文)**：
- **YOLO 导出** 将多部分蒙版合并到一个多边形中并跳过人群注释，并带有旧输出的标志。
- 背景叠加和比较注释器在灰度场景上绘制。
- 没有 OpenCV，调整大小、模糊、混合、绘图和连接的组件提供与 OpenCV 相同的像素。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# v0.31.3 — Grayscale annotators, OpenCV-exact fallbacks, and merged YOLO polygons

Grayscale scenes work with more annotators, the pure NumPy fallback matches OpenCV pixel for pixel, and YOLO export handles multi-part masks.

- **YOLO export** merges multi-part masks into one polygon and skips crowd annotations, with flags for the old output.
- Background overlay and comparison annotators draw on grayscale scenes.
- Without OpenCV, resize, blur, blending, drawing and connected components give the same pixels as OpenCV.
- Invalid input fails early: `ImageSink`, the video frame generator and depth arrays now raise clear errors.
- Short hex colors such as `"#f0f"` work in annotators.

Drop-in upgrade unless you export YOLO labels: the default output changes, see the Migration guide.

## ✨ Spotlights / highlights

### YOLO export merges multi-part masks and skips crowd annotations

`DetectionDataset.as_yolo` now omits detections whose `iscrowd` flag is set and writes a mask with several disconnected parts as one merged polygon line instead of one line per part. Both are on by default. The merge is done by the new `sv.merge_multi_segment`, which joins the parts through zero-width seams at their nearest vertices. (#2786)

```python
import supervision as sv

dataset = sv.DetectionDataset(...)
dataset.as_yolo(
    images_directory_path="images",
    annotations_directory_path="labels",
    data_yaml_path="data.yaml",
)  # 0.31.3: crowd skipped, one merged p
```
</details>

---
### 📦 [MetaCubeX/mihomo](https://github.com/MetaCubeX/mihomo)
`⭐ Stars: 35,438` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.19.33](https://github.com/MetaCubeX/mihomo/releases/tag/v1.19.33) (2026-10-21)`

> **简介**：A simple Python Pydantic model for Honkai: Star Rail parsed data from the Mihomo API.

**💡 核心亮点更新 (中文)**：
* 2df147b9 feat: support `dns-mode` for tun (#3288) by  Dust

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## What's Changed
* 2df147b9 feat: support `dns-mode` for tun (#3288) by @Chenx Dust

## BUG & Fix
* 349af191 fix: the embedded shadowsocks listener can't be closed (#3314) by @Token
* 80101933 fix: bound doh dials so ones the query gave up on cannot pile up (#3274) by @Cassian433
* 94b13aed fix: dialer-proxy cycle check takes quadratic time and memory (#3315) by @Token
* c4e81869 fix: CVE-2026-97031 for crypto/tls by @wwqgtxx
* df1b07af fix: a sub-millisecond URL test is reported as a failure (#3316) by @Token
* e4dd968d fix: keep fake-ip allocation state when cloning the pool on reload (#3283) by @Younes Beriane
* 1354e52e fix: unpassed loadbalance test by @wwqgtxx

## Maintenance
* 3f27ef39 chore: refactored and fixed issues for sudoku while also improving performance (#3333) by @saba-futai
* 9f053c49 chore: lazy init wireguard device and stack by @wwqgtxx
* bc76c139 chore: update mieru version (#3304) by @enfein

**Full Changelog**: https://github.com/MetaCubeX/mihomo/compare/v1.19.32...v1.19.33
```
</details>

---
### 📦 [microsoft/graphrag](https://github.com/microsoft/graphrag)
`⭐ Stars: 36,528` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.3.0](https://github.com/microsoft/graphrag/releases/tag/v3.3.0) (2026-10-08)`

> **简介**：基于模块化图的检索增强生成（RAG）系统

**💡 核心亮点更新 (中文)**：
* 通过 https://github.com/microsoft/graphrag/pull/2591 修复 sqlite 性能问题
* 发布 v3.3.0 https://github.com/microsoft/graphrag/pull/2592

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## What's Changed
* fix sqlite performance issue by @gaudyb in https://github.com/microsoft/graphrag/pull/2591
* Release v3.3.0 by @gaudyb in https://github.com/microsoft/graphrag/pull/2592


**Full Changelog**: https://github.com/microsoft/graphrag/compare/v3.2.0...v3.3.0
```
</details>

---
### 📦 [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev)
`⭐ Stars: 155,623` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.5.8](https://github.com/clash-verge-rev/clash-verge-rev/releases/tag/v2.5.8) (2026-10-09)`

> **简介**：A modern GUI client based on Tauri, designed to run in Windows, macOS and Linux for tailored proxy experience

**💡 核心亮点更新 (中文)**：
- 修复系统托盘代理组行不显示延迟、超时项与未测过项无法区分的问题
- 修复不同订阅源的同名节点测速和延迟显示指向错误节点的问题
- 修复端口设置混淆保存值与运行值、输入无效时缺少提示的问题

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## v2.5.8

<details>
<summary><strong> 🐞 修复问题 </strong></summary>

- 修复系统托盘代理组行不显示延迟、超时项与未测过项无法区分的问题
- 修复不同订阅源的同名节点测速和延迟显示指向错误节点的问题
- 修复端口设置混淆保存值与运行值、输入无效时缺少提示的问题
- 修复已有内核进程阻止启动时缺少多语言说明和处理建议的问题
- 修复从开始菜单再次打开应用后，窗口反复弹出并提示启动失败的问题
- 修复多个代理集合包含同名节点时，代理组中的节点变灰并显示 ambiguous、无法选择的问题
- 修复手动更新时重复下载后台已下载的安装包、启动时选「稍后」后每次启动都重新下载的问题
- 修复下载更新时镜像缓慢或卡住不会切换下载地址、点击「取消」无法中止下载的问题
- 修复关闭「自动检查更新」后，启动时仍弹出已下载更新的安装提示的问题
- 修复从 Dock 退出、注销或关机时，应用可能长时间卡住无法退出的问题
- 修复宽窗口下「订阅」页每行显示过多卡片，导致配置名称被截断的问题

**🖥️ Windows**

- 修复 Windows 升级后因文件权限异常无法启动、需要手动清理配置的问题
- 修复 Windows 服务启动类型被改为手动后，软件启动卡住约两分钟的问题，并提供一键修复
- 修复 Windows 长时间运行后，托盘菜单点击无响应的问题

**🍎 macOS**

- 修复 macOS 关闭 TUN 或退出后，系统 DNS 仍停留在 `114.114.114.114` 导致无法解析域名的问题

**🖥️/🍎 Windows/macOS**

- 修复 Windows/macOS 打开系统托盘菜单时，节点延迟与自动选择状态未刷新的问题

</details>

<details>
<summary><strong> ✨ 新增功能 </strong></summary>

- 新增系统托盘代理组中的「测试延迟」菜单项

</details>

<details>
<summary><strong> 🚀 优化改进 </strong></summary>

- 优化端口设置窗口的实现，精简重复代码
- 优化侧边栏流量图表的 CPU 占用

**🖥️ Windows**

- 优化 Windows 服务安全检查未通过时的提示：启动、安装或修复服务时说明原因与内核占用，并提供处理方法

</details>

## 下载地址

### Windows (不再支持Win7)
#### 正常版本(推荐)
- [64位(常用)](https://github.com/clash-verge-rev/clash-verge-rev/releases/download/v2.5.8/Clash.Verge_2.5.8_x64-setup.exe) | [ARM64(不常用)](https://github.com/clash-verge-rev/clash-verge-rev/releases/download/v2.5.8/Clash.Verge_2.5.8_arm64-setup.exe)

#### 内置Webview2版(体积较大，仅在企业版系统或无法安装webview2时使用)
- [64位](https://github.com/clash-verge-rev/clash-verge-rev/releases/download/v2.5.8/Clash.Verge_2.5.8_x64_fixe
```
</details>

---
### 📦 [unslothai/unsloth](https://github.com/unslothai/unsloth)
`⭐ Stars: 78,942` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.1.913-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.913-beta) (2026-10-30)`

> **简介**：用于运行和训练法学硕士和扩散模型的本地 UI。支持 GGUF、MLX、Qwen3.8、DeepSeek-V4.1、MiniMax-H3、Gemma 4、FLUX 等。

**💡 核心亮点更新 (中文)**：
- **自定义背景**来个性化您的聊天（+将作曲家移至底部 - 下周将提供更多自定义功能）
- **DeepSeek-V4.1-Flash-1017** 新的 Unsloth Dynamic v3.1 GGUF（预览版），在几乎所有基准测试中尺寸最准确 [博客](https://unsloth.ai/docs/models/deepseek-v4.1-flash)
- **Unsloth 的 14 种新语言**

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Make Unsloth your own with custom backgrounds and a improved UI/UX. This release also cuts app update times and speeds up Linux app and Qwen-Image gen when VRAM is limited.  Also new: DeepSeek-V4.1-Flash-1017 in Unsloth [Dynamic v3.1](https://unsloth.ai/docs/models/deepseek-v4.1-flash) GGUFs (preview), FLUX.2-klein-9B on low-RAM machines, smoother chats and batched MoE fine-tuning.

<img width="3520" height="958" src="https://github.com/user-attachments/assets/a4c01069-da2f-4cf3-afee-d19499cfefc3" />


## Highlights

- **Custom backgrounds** to personalize your chats (+ move composer to bottom - more customization coming next week)
- **DeepSeek-V4.1-Flash-1017** new Unsloth Dynamic v3.1 GGUFs (preview), the most accurate for their size on nearly all benchmarks [Blog](https://unsloth.ai/docs/models/deepseek-v4.1-flash)
- **14 new languages** for Unsloth
- **App updates** finish twice as fast
- **Linux** much less lag and improved performance
- **Qwen-Image** renders up to 2x faster under a 16 GB VRAM limit
- **Updated interface** with consistency and cleaner UI
- **MoE fine-tuning** runs compatible API jobs together

## Customization and interface

- Move the chat box to the bottom of new chats with **Composer at the bottom** in Settings > Chat.
- Hide the greeting entirely for a simpler new-chat screen.
- The Library gets shorter chat cards, clearer tooltips and consistent sort and filter icons.
- Copy images between input slots by dragging a filled slot
```
</details>

---
### 📦 [arc53/DocsGPT](https://github.com/arc53/DocsGPT)
`⭐ Stars: 18,353` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [1.1.0](https://github.com/arc53/DocsGPT/releases/tag/1.1.0) (2026-10-25)`

> **简介**：Private AI platform for agents, assistants and enterprise search. Built-in Agent Builder, Deep research, Document analysis, Multi-model support, and API connectivity for agents.

**💡 核心亮点更新 (中文)**：
* Keep the Responses prompt cache across turns and count replayed reasoning by  in https://github.com/arc53/DocsGPT/pull/3033
* docs: add Vercel OSS Program badge to README by  in https://github.com/arc53/DocsGPT/pull/3049
* Update the README translations by [bot] in https://github.com/arc53/DocsGPT/pull/3050

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## What's Changed
* Keep the Responses prompt cache across turns and count replayed reasoning by @dartpain in https://github.com/arc53/DocsGPT/pull/3033
* docs: add Vercel OSS Program badge to README by @dartpain in https://github.com/arc53/DocsGPT/pull/3049
* Update the README translations by @github-actions[bot] in https://github.com/arc53/DocsGPT/pull/3050
* docs: supporters row in README header by @dartpain in https://github.com/arc53/DocsGPT/pull/3052
* Update the README translations by @github-actions[bot] in https://github.com/arc53/DocsGPT/pull/3053
* docs: Neon dark logo on dark theme by @dartpain in https://github.com/arc53/DocsGPT/pull/3054
* Update the README translations by @github-actions[bot] in https://github.com/arc53/DocsGPT/pull/3057
* Richer Word artifacts, artifact downloads for API clients, and reference-only attachments by @dartpain in https://github.com/arc53/DocsGPT/pull/3060
* Report the prompt cache in /v1 usage by @dartpain in https://github.com/arc53/DocsGPT/pull/3064
* Keep a paused turn's attachments and state when it resumes by @dartpain in https://github.com/arc53/DocsGPT/pull/3063
* Triage: answer mentions, honour form claims, quieter PR re-reviews by @dartpain in https://github.com/arc53/DocsGPT/pull/3075
* Let scheduled and webhook agent runs use the code executor by @dartpain in https://github.com/arc53/DocsGPT/pull/3081
* (fix)drawio: preset connector flow by @ManishMadan2882 in https://github.com/arc53/DocsGPT/pull/3073
* chore(deps): bu
```
</details>

---
### 📦 [lobehub/lobehub](https://github.com/lobehub/lobehub)
`⭐ Stars: 83,693` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.3.0](https://github.com/lobehub/lobehub/releases/tag/v2.3.0) (2026-11-01)`

> **简介**：🤯 LobeHub 是您的首席代理运营商，通过招聘、调度和报告整个 AI 团队，将您的代理组织为 7×24 小时运营。

**💡 核心亮点更新 (中文)**：
- **默认情况下打开，带有关闭开关** - 推出标志消失了，每个机器人都会自行发言，除非其所有者将其关闭。该开关是通道设置“唤醒策略”选项卡顶部的新“主动参与”块，并在更改后立即保存。关闭后，“职责”、“频道”和“节奏”选项将被隐藏，只有观看关键字仍然会唤醒机器人。 (#22024)
- **当它可以提供帮助时介入** - 对于所有者编写职责的机器人来说，机器人不再等待落在其中的消息。当有人留下无人回答的悬而未决的问题或问题时，它也会介入，并且机器人可以解决它。在一个人进入模型后立即出现一行而不是被跳过，并且机器人仍然不会回复给其他人的回复。这不会添加额外的模型调用。 (#22038)
- **唤醒记录** — 机器人设置中的新唤醒记录选项卡列出了机器人判断的每条消息。它显示 30 天的摘要（唤醒、跳过、延迟、主动唤醒），以及每条消息的结果、模型分数和可读的原因，以及返回 Discord 上消息的链接。按结果过滤，仅主动唤醒或仅未标记，并将每个决策标记为 ✓ 正确或 ✗ 错误。 (#21934)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Release v2.3.0

From PR #22056: https://github.com/lobehub/lobehub/pull/22056

# 🚀 LobeHub Release (v2.3.0)

**Release Date:** November 1, 2026  
**Since v2.2.21:** 145 merged PRs · 7 contributors

> Bots stop waiting to be @-mentioned. With Proactive Bot on by default, every bot reads its channels, steps in when it can help, and shows its owner every call it made. Channels, pages, memory, dashboards, tasks and goals round out the release.

---

## 🤖 Proactive Bot

Until now a bot answered only when someone @-mentioned it. Bot wake was previewed behind a rollout flag in v2.2.21. In v2.3.0 it is on for every bot: the bot judges each message in the channels it watches and decides for itself whether to speak up, stay quiet or wait.

- **On by default, with an off switch** — The rollout flag is gone, and every bot speaks up on its own unless its owner turns it off. The switch is the new **Proactive participation** block at the top of the channel settings' Wake policy tab and saves as soon as it changes. With it off, the Duties, Channels and Pace options are hidden, and only watch keywords still wake the bot. (#22024)
- **Steps in when it can help** — For a bot whose owner wrote duties, the bot no longer waits for a message that falls inside them. It also steps in when someone leaves an open question or problem that nobody has answered and the bot can settle it. A line right after a person goes to the model instead of being skipped, and the bot still stays out of
```
</details>

---
### 📦 [labring/FastGPT](https://github.com/labring/FastGPT)
`⭐ Stars: 29,972` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v4.17.3](https://github.com/labring/FastGPT/releases/tag/v4.17.3) (2026-11-01)`

> **简介**：FastGPT 是一个建立在法学硕士基础上的知识平台，提供一整套开箱即用的功能，例如数据处理、RAG 检索和可视化 AI 工作流程编排，让您轻松开发和部署复杂的问答系统，无需进行大量设置或配置。

**💡 核心亮点更新 (中文)**：
* 文档：通过 https://github.com/labring/FastGPT/pull/7937 补充 4.17.2 的手动迁移脚本详细信息和索引优化
* feat(markdown): 支持受控的 HTML 渲染和丰富的组件 https://github.com/labring/FastGPT/pull/7940
* 修复：更新计费模式切换背景 https://github.com/labring/FastGPT/pull/7943

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 升级指南

### 配置变更

- 源码部署的 Node.js 版本须满足 `^22.23.4 || ^24.22.1 || ^26.12.1`，升级前请先确认运行环境符合该范围。
- `DEFAULT_TEAM_BASIC_PERMISSIONS_ENABLED` 仍默认 `false`；启用时，新团队默认全员组除应用、技能和知识库创建权限外，还会获得 API Key 创建权限，已有团队不自动补授。
- Agent 沙盒活跃实例总上限改为通过 `AGENT_SANDBOX_MAX` 配置，默认 100，应用会话与技能编辑共用额度；原 `AGENT_SANDBOX_MAX_EDIT_DEBUG` 不再使用。新增 `AGENT_SANDBOX_MAX_PER_TEAM` 设置单团队上限，默认不限制。商业版管理台中的配额配置优先于环境变量。
- OpenSandbox 新增 `AGENT_SANDBOX_CPU_OVERCOMMIT_FACTOR` 与 `AGENT_SANDBOX_MEMORY_OVERCOMMIT_FACTOR`，默认均为 1，取值须不小于 1。仅在 Kubernetes 运行态且 OpenSandbox Server 不低于 v0.2.1 时生效，降低资源预留但保持资源上限不变，仅影响新建或重建的沙盒。
- 商业版管理台新增「向量检索最大并发数」（`systemEnv.vectorRecallConcurrency`），允许配置 0–1000，默认 0 表示不限制。正数限制所有服务实例、所有向量库的共享召回并发；开源版不启用此限制，无对应环境变量。
- 新增 `AUXILIARY_GENERATION_SHOW_RUN_DETAIL`，默认 `false`，控制技能、Agent 和工作流辅助生成的运行详情入口是否展示。
- 应用市场默认地址（`MARKETPLACE_URL`）更新为 `https://v3.marketplace.fastgpt.cn`，显式配置的自定义地址继续使用原值。

### 镜像更新

- 更新 fastgpt-app（FastGPT 主服务）镜像 tag: v4.17.3
- 更新 fastgpt-pro（FastGPT 商业版）镜像 tag: v4.17.3
- 更新 fastgpt-plugin 镜像 tag: v1.2.0
- 更新 fastgpt-code-sandbox 镜像 tag(后续都独立发布，按需更新): v5.0.0
- 更新 AI Proxy 镜像 tag: v0.7.7

### 升级脚本

系统先完成启动必需任务及其前置依赖链，各 App 实例重载模型后启动业务。以下 3 个新增任务随后在后台自动执行，共享集群最多 3 个并发名额，失败不会阻断无依赖任务；可在管理页查看结果，修复失败数据后重试。

- **回填沙盒实例团队归属**（`20261009_backfill_agent_sandbox_team_id`）：根据来源应用或技能补齐历史实例的团队归属，用于团队配额统计；来源已删除的孤儿记录跳过并计数。
- **回填目录祖先路径**（`20261022_backfill_folder_ancestor_ids`）：重建应用、工具及知识库目录路径，清理非文件夹资源的残留字段。直接挂在其他类型目录树下的文件夹移到本团队根目录，并清理旧父级继承权限；更高层的跨树祖先路径在边界处截断。缺失父级、跨团队或成环等异常记录保留为失
```
</details>

---
### 📦 [yihong0618/bilingual_book_maker](https://github.com/yihong0618/bilingual_book_maker)
`⭐ Stars: 9,918` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.3.2](https://github.com/yihong0618/bilingual_book_maker/releases/tag/v1.3.2) (2026-10-30)`

> **简介**：使用人工智能翻译制作双语 epub 书籍

**💡 核心亮点更新 (中文)**：
* 壮举（文档）：通过 Cloudflare AI 网关将 Jev 集成为 epub 标签分类器，位于 https://github.com/yihong0618/bilingual_book_maker/pull/580
* 壮举：Datalab 作为 --to-epub 引擎，Markdown 和 EPUB 上的 Claude Message Batches (--batch-api)，双语 --to-epub 内容，阅读版本修复在 https://github.com/yihong0618/bilingual_book_maker/pull/581

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## What's Changed
* feat(docs): Integrate Jev through Cloudflare AI gateway as epub tag classifier by @pc418 in https://github.com/yihong0618/bilingual_book_maker/pull/580
* feat: Datalab as a --to-epub engine, Claude Message Batches (--batch-api) on Markdown and EPUB, bilingual --to-epub contents, reading-edition fixes by @pc418 in https://github.com/yihong0618/bilingual_book_maker/pull/581


**Full Changelog**: https://github.com/yihong0618/bilingual_book_maker/compare/v1.3.1...v1.3.2
```
</details>

---
### 📦 [1Panel-dev/1Panel](https://github.com/1Panel-dev/1Panel)
`⭐ Stars: 37,342` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.4.2](https://github.com/1Panel-dev/1Panel/releases/tag/v2.4.2) (2026-10-30)`

> **简介**：🔥 1Panel is a modern, open-source Linux server management panel and a lightweight AI management platform. 1Panel 是专门为 AI 服务器打造的管理面板。

**💡 核心亮点更新 (中文)**：
* System: Disabled MPTCP by default to mitigate a Linux kernel remote code execution vulnerability ([CVE-2026-98432](https://www.cve.org/CVERecord?id=CVE-2026-98432))
* 【系统】默认禁用 MPTCP，缓解 Linux 内核远程代码执行漏洞（[CVE-2026-98432](https://www.cve.org/CVERecord?id=CVE-2026-98432)）

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
[English](#en-v2.4.2) | [中文](#cn-v2.4.2)

<h3 id="en-v2.4.2">Bug Fixes</h3>

* System: Disabled MPTCP by default to mitigate a Linux kernel remote code execution vulnerability ([CVE-2026-98432](https://www.cve.org/CVERecord?id=CVE-2026-98432))

<h3 id="cn-v2.4.2">问题修复</h3>

* 【系统】默认禁用 MPTCP，缓解 Linux 内核远程代码执行漏洞（[CVE-2026-98432](https://www.cve.org/CVERecord?id=CVE-2026-98432)）
```
</details>

---
### 📦 [invoke-ai/InvokeAI](https://github.com/invoke-ai/InvokeAI)
`⭐ Stars: 28,956` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v6.14.3](https://github.com/invoke-ai/InvokeAI/releases/tag/v6.14.3) (2026-11-01)`

> **简介**：Invoke 是稳定扩散模型的领先创意引擎，使专业人士、艺术家和爱好者能够使用最新的人工智能驱动技术生成和创建视觉媒体。该解决方案提供了业界领先的WebUI，并作为多个商业产品的基础。

**💡 核心亮点更新 (中文)**：
InvokeAI v6.14.3 是一个补丁版本，它通过矢量图形层增强了 Canvas 并纠正了模型管理器中的下载错误。

新功能：可编辑矢量图层

@DustyShoe 为 Canvas 提供了增强功能，使您能够

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
InvokeAI v6.14.3 is a patch release that enhances the Canvas with a vector graphics layer and corrects a download bug in the Model Manager.

## New Feature: Editable vector layers

@DustyShoe contributed an enhancement to the Canvas that allows you to create a vector layer with editable shapes and splines. When you are satisfied with the vector shapes you can rasterize them and use them for img2img.

## Bug Fix: Keep restored downloads restartable

@primorLee fixed an issue that prevented partial downloads from being restarted after a server crash or termination.

## What's Changed
* fix(model-install): keep restored downloads restartable by @primorLee in https://github.com/invoke-ai/InvokeAI/pull/9521
* chore(prep): bump version by @lstein in https://github.com/invoke-ai/InvokeAI/pull/9640
* ci(docs): deploy invoke.ai from v6-bugfixes by @lstein in https://github.com/invoke-ai/InvokeAI/pull/9705
* chore(ui): back-port Weblate translations to v6 by @lstein in https://github.com/invoke-ai/InvokeAI/pull/9878
* feat(canvas): add editable vector layers and spline workflows by @DustyShoe in https://github.com/invoke-ai/InvokeAI/pull/9194

## New Contributors
* @primorLee made their first contribution in https://github.com/invoke-ai/InvokeAI/pull/9521

**Full Changelog**: https://github.com/invoke-ai/InvokeAI/compare/v6.14.2...v6.14.3
```
</details>

---
### 📦 [The-Vibe-Company/quivr](https://github.com/The-Vibe-Company/quivr)
`⭐ Stars: 39,625` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.0.2](https://github.com/The-Vibe-Company/quivr/releases/tag/v2.0.2) (2026-10-30)`

> **简介**：一个开源引擎，可将连续的内容流转化为搜索和监控。持久摄取、混合搜索、警报以及格式、模型和业务规则的插件。

**💡 核心亮点更新 (中文)**：
- **过滤的搜索不再随机失败。** Quivr 将每个矢量和混合搜索过滤到请求的范围。 Weaviate 的默认过滤策略可能会导致在链接数量多于预期的矢量图节点上进行此类搜索，然后搜索会返回错误。
- **安全性：** CVE-2026-63209，位于压缩库中。
- **内存较少。**

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Quivr 2.0.2

2.0.2 moves the search database to Weaviate 1.39.14. It changes no API, no configuration and no stored data. Upgrade any 2.0.x installation to it.

### What Weaviate 1.39.14 fixes for Quivr

- **Filtered searches no longer fail at random.** Quivr filters every vector and hybrid search to the scope of the request. Weaviate's default filtering strategy could crash such a search on a node of the vector graph with more links than expected, and the search then returned an error.
- **Security:** CVE-2026-63209, in the compression library.
- **Less memory.**
  - Quivr compresses its vectors. Compressed indexes now drop the uncompressed vector cache they no longer use, which can save gigabytes on a large index.
  - Weaviate also stops keeping memory it never frees when writing to its in-memory tables.
- **Safer restarts.** A crash right after a shutdown could leave a keyword-search file empty, and the database would then not start without a manual repair. Startup and shutdown are also faster.

Results do not change. The hybrid search changes in 1.39.14 only affect `offset` paging and `nearText` queries, and Quivr uses neither.

### Upgrade from 2.0.0 or 2.0.1

1. Back up the search database volume.
2. Deploy the 2.0.2 images and the new Weaviate pin from `deploy/infrastructure.json`, or the 2.0.2 compose bundle attached to this release for a single machine.
3. Keep the same Weaviate volume.

This is a patch upgrade within one Weaviate minor version: no re-indexing and
```
</details>

---
### 📦 [langgenius/dify](https://github.com/langgenius/dify)
`⭐ Stars: 160,197` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [1.18.0](https://github.com/langgenius/dify/releases/tag/1.18.0) (2026-10-23)`

> **简介**：Build Agentic workflows, RAG pipelines, with rich AI model and tool support on one collaborative workspace. Deploy on cloud, VPC, or self-hosted, so teams move from prototype to production without rebuilding the stack.

**💡 核心亮点更新 (中文)**：
- **Published triggers:** the draft-sync fix does not repair subscriptions already removed before upgrading. Rebind missing subscriptions and republish affected workflows as needed. (#44068)
- **Document extraction:** re-import/re-index affected content to apply extraction fixes to existing documents.
- **Built-in document metadata:** toggling built-in fields rewrites only enabled, non-archived documents whose indexing is complete. Other legacy rows can retain the old format and need a later rewrite when eligible; this release does not include a full backfill. (#44218)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Dify 1.18.0 brings **Agents that route workflows**, **portable app packages**, **deeper visibility into nested workflow runs**, and the opt-in **Agent Knowledge Base** experience. OpenAPI and the new difyctl expand how you build and manage apps from the command line.

> [!IMPORTANT]
> **Read the upgrade guide below before deploying.** Upgrade the API, workers, Agent Backend, and Agent runtime images together. Local Agent sandboxes require a non-empty authentication token, and Agent Backend uses a new run protocol. Source installations require Python 3.13. Install the new difyctl client and sign in again. Preserve your existing `PASSWORD_PEPPER` configuration.

### Release highlights

#### Agents that choose the next step

Let an Agent decide which workflow branch to take. Enable **Output Routes**, give each route a selection condition, and connect it to the next step—such as resolving a request directly or handing it to a specialist. The read-only `switch` output exposes the chosen route. (#42599)

![Agent Output Routes with Resolve directly and Escalate to team branches](https://github.com/user-attachments/assets/30480ac3-d53e-4522-b1c5-95eb1d9ac9f2)

*Output Routes configuration with two branches in the workflow editor.*

Plain Agent v2 nodes also stream text as it is generated. Structured results, routed results, and nodes using default-value error handling remain buffered. (#43986)

#### Portable apps in one package

Move an app with its supported resou
```
</details>

---
### 📦 [nextai-translator/nextai-translator](https://github.com/nextai-translator/nextai-translator)
`⭐ Stars: 25,022` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.6.54](https://github.com/nextai-translator/nextai-translator/releases/tag/v0.6.54) (2026-11-01)`

> **简介**：基于 ChatGPT API 的划词翻译浏览器插件和跨平台桌面端应用    -    Browser extension and cross-platform desktop application for translation based on ChatGPT API.

**💡 核心亮点更新 (中文)**：
- 修复了在设置中切换提供商后 API 模型下拉菜单打开不可见（零宽度）的问题；影响了每个提供商的模型选择器，为 Gemini 报告（#1945，#1947，谢谢
- Gemini：发送每个模型接受的思维配置（使用模型 API 的思维标志，带有每个系列的回退），修复多个模型上的 HTTP 400（#1947）

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
v0.6.54

- Fix the API Model dropdown opening invisibly (zero width) after switching provider in settings; affected every provider's model selector, reported for Gemini (#1945, #1947, thanks @Loongphy)
- Gemini: send the thinking config each model accepts (uses the models API's thinking flag, with per-family fallbacks), fixing HTTP 400s on several models (#1947)
```
</details>

---
### 📦 [langchain-ai/langchain](https://github.com/langchain-ai/langchain)
`⭐ Stars: 148,860` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [langchain-core==1.7.3](https://github.com/langchain-ai/langchain/releases/tag/langchain-core%3D%3D1.7.3) (2026-10-29)`

> **简介**：代理工程平台。

**💡 核心亮点更新 (中文)**：
自 langchain-core==1.7.2 以来的变化

版本（核心）：1.7.3（41564）

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Changes since langchain-core==1.7.2

release(core): 1.7.3 (#41564)
```
</details>

---
### 📦 [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)
`⭐ Stars: 187,864` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [autogpt-platform-beta-v0.10.0](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.10.0) (2026-10-27)`

> **简介**：AutoGPT 的愿景是为每个人提供易于使用和构建的人工智能。我们的使命是提供工具，以便您可以专注于重要的事情。

**💡 核心亮点更新 (中文)**：
- **#15990** - 记录每个 API 密钥最后一次使用的时间（由
- **#15862** - 告诉聊天平台机器人每条消息的来源（通过
- **#16023** - 角色和文本设计标记按当今的值 (DS1)（由

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 🔥 What's New?

### ⚠️ Breaking Changes

- **#15970** - Self-hosted Docker Compose generates its own service passwords per install and won't start without them: run `make init-env` (or the installer) before `docker compose up`. PostgreSQL, RabbitMQ, Redis, FalkorDB and ClamAV now listen on `127.0.0.1` only. Existing installs: see [Upgrading: service passwords are generated per install](https://github.com/Significant-Gravitas/AutoGPT/blob/master/docs/platform/getting-started.md#upgrading-service-passwords-are-generated-per-install) (by @ntindle)
- **#12206** - External API v1 is deprecated in favour of the new v2, and keeps working until 2027-01-31 (by @Pwuts)

### New Features

- **#15990** - Record when each API key was last used (by @ntindle)
- **#15862** - Tell chat-platform bots where each message came from (by @Bentlybro)
- **#16023** - Role and text design tokens at today's values (DS1) (by @Abhi1992002)
- **#16035** - Send product mail only to subscribers, trialists and accounts that lapsed in the last 7 days (by @Torantulino)
- **#16037** - Molecules read only role tokens, same look (DS2b) (by @Abhi1992002)
- **#16044** - Move contextual and renderers onto the design tokens (DS5c) (by @Abhi1992002)
- **#16045** - Atoms read only design tokens, same look (DS2a) (by @Abhi1992002)
- **#16078** - Move library, artifacts and (platform)/components onto design tokens (DS5e) (by @Abhi1992002)
- **#16081** - Data-slot on every element an atom renders (DS7-1)
```
</details>

---
### 📦 [rockbenben/ChatGPT-Shortcut](https://github.com/rockbenben/ChatGPT-Shortcut)
`⭐ Stars: 8,898` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v4.5.1](https://github.com/rockbenben/ChatGPT-Shortcut/releases/tag/v4.5.1) (2026-10-09)`

> **简介**：Stop writing prompts from scratch — a searchable prompt library for ChatGPT, Claude, Gemini and Cursor · Русский 한국어 العربية हिन्दी ไทย ｜ 别再从头写提示词：现成的拿来就用，好用的收进自己的库

**💡 核心亮点更新 (中文)**：
- Keep array and object identity stable so unrelated updates no longer re-render whole lists. Favoriting a prompt, searching, or clearing filters now re-renders only what actually changed instead of the entire grid.
- Tapping the favorite heart with no filter active no longer triggers two extra render passes on the homepage.
- The axios response interceptor's "always throw" contract is now enforced by the type system (`handleApiError` returns `never`). A stray early `return` — the shape that silently resolved `undefined` into every caller on timeouts and DNS failures — no longer compiles.

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Performance

- Keep array and object identity stable so unrelated updates no longer re-render whole lists. Favoriting a prompt, searching, or clearing filters now re-renders only what actually changed instead of the entire grid.
- Tapping the favorite heart with no filter active no longer triggers two extra render passes on the homepage.

## Fixes

- The axios response interceptor's "always throw" contract is now enforced by the type system (`handleApiError` returns `never`). A stray early `return` — the shape that silently resolved `undefined` into every caller on timeouts and DNS failures — no longer compiles.
- Copy-count failures no longer masquerade as zero counts. The function now follows the same cached-or-throw pattern used elsewhere, so callers can tell "backend down" from "nobody copied this".
- Community page selection fails fast on a corrupt traffic file instead of silently degrading to upvote ordering, which previously dropped every traffic-bearing community page from the static set while the build stayed green.

## Dependencies

Within existing semver ranges — `package.json` ranges are unchanged:

- react / react-dom 19.2.8 → 19.3.0
- antd 6.6.1 → 6.6.5
- @ant-design/icons 6.3.2 → 6.3.4
- @types/react 19.2.18 → 19.3.0

TypeScript stays on 6.0.3: `@docusaurus/tsconfig` still relies on `baseUrl`, and the deprecation is silenced only until Docusaurus moves to TS 7. Docusaurus remains pinned at 3.10.2 with no newer release.

## Translations
```
</details>

---
### 📦 [pionxzh/chatgpt-exporter](https://github.com/pionxzh/chatgpt-exporter)
`⭐ Stars: 2,852` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [userscript-v2.38.1](https://github.com/pionxzh/chatgpt-exporter/releases/tag/userscript-v2.38.1) (2026-10-30)`

> **简介**：导出并分享您的 ChatGPT 对话历史记录

**💡 核心亮点更新 (中文)**：
* 保留 ChatGPT 作为 url 标记写入的内联链接（[ba36a28](https://github.com/pionxzh/chatgpt-exporter/commit/ba36a289195288f97c81ff2f2af308fda11f319e)），关闭[#413](https://github.com/pionxzh/chatgpt-exporter/issues/413)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## [2.38.1](https://github.com/pionxzh/chatgpt-exporter/compare/userscript-v2.38.0...userscript-v2.38.1) (2026-10-30)


### Bug Fixes

* keep inline links that ChatGPT writes as url markers ([ba36a28](https://github.com/pionxzh/chatgpt-exporter/commit/ba36a289195288f97c81ff2f2af308fda11f319e)), closes [#413](https://github.com/pionxzh/chatgpt-exporter/issues/413)
```
</details>

---
### 📦 [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent)
`⭐ Stars: 47,744` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [2.2.2](https://github.com/zhayujie/CowAgent/releases/tag/2.2.2) (2026-10-30)`

> **简介**：开源个人人工智能助理和代理线束。计划任务，运行工具和技能，利用记忆和知识进行自我进化。多代理、多模式、多渠道。轻量级、可扩展、单行安装。

**💡 核心亮点更新 (中文)**：
- **独立页面**：每个页面都有自己的链接，访问者保留他们的聊天记录，并且名称、图标、主题颜色、欢迎消息和建议问题都是可定制的。
- **嵌入式聊天窗口**：单个代码片段将页面嵌入您的网站中，右下角有一个聊天按钮。您可以限制哪些站点可以嵌入它并在配置时预览结果。在 [CowAgent 网站](https://cowagent.ai/?chat=open) 上实时尝试。
- **数据隔离**：为访问者提供服务的代理只能使用为该页面启用的工具、技能和参考。它无法访问您的内存、对话或工作空间，无法运行命令，并且其网络请求仅限于公共地址。新页面从文件写入、文件发送和网络搜索关闭开始。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
🌐 [English](https://docs.cowagent.ai/releases/v2.2.2) | [中文](https://docs.cowagent.ai/zh/releases/v2.2.2)

## 💬 Guest Pages

Share an Agent as a standalone chat page, or embed it in your website as a chat window. Visitors open the link and start chatting without signing in, which suits product inquiries, knowledge base Q&A, customer support, and similar scenarios:

- **Standalone pages**: each page gets its own link, visitors keep their chat history, and the name, icon, theme color, welcome message, and suggested questions are all customizable.

<Frame>
  <img src="https://cdn.jsdelivr.net/gh/zhayujie/cowagent-assets@main/screenshots/en/guest-share-page-dark.png" alt="Guest page" width="800" />
</Frame>

- **Embedded chat window**: a single code snippet embeds the page in your website, with a chat button in the bottom-right corner. You can restrict which sites may embed it and preview the result while configuring. Try it live on the [CowAgent website](https://cowagent.ai/?chat=open).

<Frame>
  <img src="https://cdn.jsdelivr.net/gh/zhayujie/cowagent-assets@main/screenshots/en/guest-share-embed.png" alt="Embed in a page" width="800" />
</Frame>

- **Data isolation**: the Agent serving visitors can only use the tools, skills, and references enabled for that page. It cannot access your memory, conversations, or workspace, cannot run commands, and its network requests are limited to public addresses. New pages start with file writing, file sending, and web searc
```
</details>

---
### 📦 [lxhao61/integrated-examples](https://github.com/lxhao61/integrated-examples)
`⭐ Stars: 2,535` &nbsp;|&nbsp; `💻 语言: Shell` &nbsp;|&nbsp; `🏷️ 最新版本: [20261024](https://github.com/lxhao61/integrated-examples/releases/tag/20261024) (2026-10-24)`

> **简介**：以 Nginx 或 Caddy(v2 版) 配合 V2Ray(v4 版) 或 Xray、Caddy(v2 版) 加专用插件、Hysteria 等打造常用科学上网的优化配置及最优组合示例，且提供集成特定插件的 Caddy(v2 版) 文件，分享给大家食用及自己备份。

**💡 核心亮点更新 (中文)**：
以 Caddy 发行版 v2.11.7 源码加插件 forwardproxy、caddy-trojan、caddy-webdav、caddy-cloudflare-ip、caddy-trusted-cloudfront、caddy-dns/cloudflare、caddy-dns/duckdns、caddy-dns/tencentcloud、caddy-events-exec、caddy-l4、jsonc-adapter 基于稳定版 go1.27.3 定制编译而成，其额外应用及特点如下：
1、

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
以 Caddy 发行版 v2.11.7 源码加插件 forwardproxy、caddy-trojan、caddy-webdav、caddy-cloudflare-ip、caddy-trusted-cloudfront、caddy-dns/cloudflare、caddy-dns/duckdns、caddy-dns/tencentcloud、caddy-events-exec、caddy-l4、jsonc-adapter 基于稳定版 go1.27.3 定制编译而成，其额外应用及特点如下：
1、支持 NaiveProxy 应用（服务端）。采用 ZihaoFU245 大源码，支持 UoT。
2、支持 Trojan-Go 应用（服务端）。
3、支持 WebDAV 协议的网盘应用（服务端）。
4、支持启用可信任 Cloudflare IPs，可实现使用 Cloudflare CDN 后也能获取到客户端真实 IP。
5、支持启用可信任 Cloudfront IPs，可实现使用 Cloudfront CDN 后也能获取到客户端真实 IP。
6、支持由 Cloudflare 解析的域名以 DNS-01 验证方式申请及更新 TLS 证书、支持由 Cloudflare 解析的域名可 ECH 发布。
7、支持由 DuckDNS 解析的域名以 DNS-01 验证方式申请及更新 TLS 证书。
8、支持由 TencentCloud 解析的域名以 DNS-01 验证方式申请及更新 TLS 证书。
9、支持事件执行应用，可解决相关程序不支持‘证书热更新’问题。
10、支持 Caddy 的第 4 层（TCP/UDP）应用，可实现 SNI 分流共用 TCP/UDP 端口（含定向 UDP 转发）。SNI 分流共用 TCP 端口时支持 PROXY protocol 发送，即发送真实来源 IP 和端口给后端。
11、支持 Caddy 可使用 JSONC 格式配置文件（即可保留注释使用）。​

注意：如果版本小于 v2.10.2 升级，请参阅如下 v2.10.2 相关提示。
```
</details>

---
### 📦 [mack-a/v2ray-agent](https://github.com/mack-a/v2ray-agent)
`⭐ Stars: 22,266` &nbsp;|&nbsp; `💻 语言: Shell` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.5.35](https://github.com/mack-a/v2ray-agent/releases/tag/v3.5.35) (2026-11-01)`

> **简介**：Xray、Tuic、hysteria2、sing-box 八合一一键脚本

**💡 核心亮点更新 (中文)**：
fix(xhttp): 修正 REALITY 与 TLS 的 CDN 支持描述

fix(reality): 完善 Mihomo ML-KEM 配置及 pqv 导出规则

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
fix(xhttp): 修正 REALITY 与 TLS 的 CDN 支持描述

fix(reality): 完善 Mihomo ML-KEM 配置及 pqv 导出规则
```
</details>

---
### 📦 [electerm/electerm](https://github.com/electerm/electerm)
`⭐ Stars: 15,524` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v5.8.0](https://github.com/electerm/electerm/releases/tag/v5.8.0) (2026-10-30)`

> **简介**：📻免费开源终端/ssh/sftp/ftp/telnet/串口/RDP/VNC/Spice客户端(Linux, Mac, Windows, Android, HarmonyOS, iOS)

**💡 核心亮点更新 (中文)**：
- SSH 隧道：支持远程动态转发，远程服务器上的 SOCKS5 代理，其连接通过您自己的网络出去（#4658）
- 小部件：直接从 GitHub/AtomGit 存储库导入小部件（“owner/repo”、“owner/repo#branch”、monorepo 子文件夹、“git@” URL）以及现有文件夹导入
- 小部件：小部件现在可以提供 AI 配置（端点、模型、密钥）供您一键查看和应用，而不是要求您手动复制值 (#4591)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
### New features/UI/Updates

- SSH tunnel: support remote dynamic forwarding, a SOCKS5 proxy on the remote server whose connections go out through your own network (#4658)
- Widget: import a widget straight from a GitHub/AtomGit repository (`owner/repo`, `owner/repo#branch`, a monorepo subfolder, `git@` URL), alongside the existing folder import
- Widget: a widget can now offer an AI config (endpoint, model, key) for you to review and apply with one click, instead of asking you to copy values by hand (#4591)
- Support exporting the selected bookmarks to a JSON file from the bookmark multi-select dialog
- Much faster local file listing: one round trip per directory instead of two per entry, and worker replies are dispatched through a single listener (#4663)
- Linux: the deb package now declares its runtime dependencies, so installing on a minimal system pulls them in instead of the app failing to start (#4659) (#2709)
- Improve about page UI

### Bug fixes

- Fix `known_hosts` wildcard matching: rules like `*.example.com` never matched, and `@cert-authority` entries were treated as a host key mismatch
- Fix the terminal tab closing itself when the connection dropped: only a clean exit (status 0) closes the tab, a signalled or failed session keeps the tab and its output (#4629)
- Fix paste in full-screen apps (tmux/vim/less): a bare Ctrl+V now reaches the app in the alternate screen, only Ctrl+Shift+V is treated as paste (#4656)
- Fix AI parallel tool calls when
```
</details>

---
### 📦 [XTLS/Xray-core](https://github.com/XTLS/Xray-core)
`⭐ Stars: 42,549` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v26.10.31](https://github.com/XTLS/Xray-core/releases/tag/v26.10.31) (2026-10-31)`

> **简介**：X射线，穿透一切。也是最好的 v2ray 核心。魔法发生的地方。适合多种用途的开放平台。

**💡 核心亮点更新 (中文)**：
- **TRX(Tron)/USDT/USDC: `TNrDh5VSfwd4RPrwsohr6poyNTfFefNYan`**
- **TON：`UQApeV-u2gm43aC1uP76xAC1m6vCylstaN1gpfBmre_5IyTH`**
- **BTC：`1JpqcziZZuqv3QQJhZGNGBVdCBrGgkL6cT`**

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
紧急安全更新：[由于 Linux 内核刚被爆出监听 IPv4 MPTCP 极易被远程拿 root，且 Go 1.24+ 默认开了 MPTCP](https://github.com/XTLS/Xray-core/pull/7291#issuecomment-6540309985)，本版本默认关闭了 MPTCP 以显著减小攻击面（v26.10.29 让位，已被撤版），用户应尽快升级到该版本（该漏洞不止影响 Linux 服务端，安卓客户端的 Socks/HTTP 入站若开启了“允许来自局域网的连接”则也有点危险），并尽快更新 Linux 内核以从根源上修复漏洞

## Sponsors

[![Remnawave](https://github.com/user-attachments/assets/a22d34ae-01ee-441c-843a-85356748ed1e)](https://docs.rw)

[![Happ](https://github.com/user-attachments/assets/14055dab-e8bb-48bd-89e8-962709e4098e)](https://happ.su)

[![BlancVPN](https://github.com/user-attachments/assets/9145ea7d-5da3-446e-8143-710dba4292c3)](https://blanc.link/0SIDK7Z)

[**Sponsor Xray-core**](https://github.com/XTLS/Xray-core/issues/3668)

## Donation & NFTs

### [Collect a Project X NFT to support the development of Project X!](https://opensea.io/item/ethereum/0x5ee362866001613093361eb8569d59c4141b76d1/1)

[<img alt="Project X NFT" width="150px" src="https://raw2.seadn.io/ethereum/0x5ee362866001613093361eb8569d59c4141b76d1/7fa9ce900fb39b44226348db330e32/8b7fa9ce900fb39b44226348db330e32.svg" />](https://opensea.io/item/ethereum/0x5ee362866001613093361eb8569d59c4141b76d1/1)

- **TRX(Tron)/USDT/USDC: `TNrDh5VSfwd4RPrwsohr6poyNTfFefNYan`**
- **TON: `UQApeV-u2gm43aC1uP76xAC1m6vCylstaN1gpfBmre_5IyTH`**
- **BTC: `1JpqcziZZuqv3QQJhZGNGBVdCBrGgkL6cT`**
- **XMR: `4ABHQZ3yJZkBnLoqiKvb3f8eqUnX4iMPb6wdant5ZLGQELctcerceSGEfJnoCk6nnyRZm73wrwSgvZ2WmjYLng6R7sR67nq`**
- **SOL/USDT/USDC: `3x5NuXHzB5APG6vRi
```
</details>

---
### 📦 [klzgrad/naiveproxy](https://github.com/klzgrad/naiveproxy)
`⭐ Stars: 9,594` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [v154.0.8037.49-5](https://github.com/klzgrad/naiveproxy/releases/tag/v154.0.8037.49-5) (2026-10-22)`

> **简介**：Make a fortune quietly

**💡 核心亮点更新 (中文)**：
Block compromised eMudhra intermediates.

ALL USERS MUST UPGRADE as old versions are no longer safe from MitM attack using forged eMudhra certificates.

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Block compromised eMudhra intermediates.

ALL USERS MUST UPGRADE as old versions are no longer safe from MitM attack using forged eMudhra certificates.
```
</details>

---

## <span id="-实用开源精选">📦 实用开源精选</span>

### 📦 [JustAResearcher/gpu-unlock-ada](https://github.com/JustAResearcher/gpu-unlock-ada)
`⭐ Stars: 4,681` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.1.1](https://github.com/JustAResearcher/gpu-unlock-ada/releases/tag/v1.1.1) (2026-10-24)`

> **简介**：GPU tensor unlock source for RTX 4090 and experimental RTX 4070 Ti SUPER; firmware generated locally

**💡 核心亮点更新 (中文)**：
- [cutlass-fp8-stock-vs-unlocked.zip](https://github.com/JustAResearcher/gpu-unlock-ada/releases/download/v1.1.1/cutlass-fp8-stock-vs-unlocked.zip) — SHA-256 `b9468068a25cc208749eb0004fc86e15ac98c25c06517fc7c76d3a4f8ac6e861`
- [ada-fp8-profile-stock-unlocked-evidence.zip](https://github.com/JustAResearcher/gpu-unlock-ada/releases/download/v1.1.1/ada-fp8-profile-stock-unlocked-evidence.zip) — SHA-256 `5e9fa282298b996828e9554a47bc32c2da9ac65037fe50368e80f5bb95bac05c`
- [FP8 evidence checksums](https://github.com/JustAResearcher/gpu-unlock-ada/releases/download/v1.1.1/FP8-EVIDENCE-SHA256SUMS.txt)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
GPU Unlock 1.1.1 publishes a reproducible SM89 tensor issue-rate probe and matched stock/unlocked TF32 and unsigned INT4 results on one RTX 4070 Ti SUPER (`10de:2705`, NVIDIA `580.178.04`, 240 W cap). The Ada unlock transaction is unchanged from 1.1.0; the module and DKMS version metadata advance to 1.1.1.

| Register-resident mode | Stock | Unlocked |
| --- | ---: | ---: |
| FP16 inputs, FP32 accumulate (control) | 94.96 TF/s | 188.97 TF/s |
| TF32 inputs, FP32 accumulate | 47.49 TF/s | 94.51 TF/s |
| Unsigned INT4 inputs, INT32 accumulate | 754.81 TOP/s | 754.68 TOP/s |

The same cubin, card, driver, 240 W cap, and launch settings were used in both boots. Each mode checked 270,336 output cells with zero mismatches per state. **TF32 instruction issue rate gained 1.99×; unsigned INT4 did not improve.** These all-one, register-resident loops do not establish an application GEMM or inference speedup. INT8 and one previously tested FP8 GEMM were also unchanged.

Read the [canary report](https://github.com/JustAResearcher/gpu-unlock-ada/blob/v1.1.1/docs/ada-2705-report.md), [sanitized numeric output and hashes](https://github.com/JustAResearcher/gpu-unlock-ada/tree/v1.1.1/docs/evidence/ada2705), and [GPL benchmark source and reproduction steps](https://github.com/JustAResearcher/gpu-unlock-ada/blob/v1.1.1/diagnostics/bench/README.md). Installation and boot rollback are in the [Quick Start](https://github.com/JustAResearcher/gpu-unlock-ada/blob/v1.1.1/QUICKSTART.md).
```
</details>

---
### 📦 [NeverSinkDev/NeverSink-Filter-for-PoE2](https://github.com/NeverSinkDev/NeverSink-Filter-for-PoE2)
`⭐ Stars: 2,857` &nbsp;|&nbsp; `💻 语言: Other` &nbsp;|&nbsp; `🏷️ 最新版本: [0.10.4a](https://github.com/NeverSinkDev/NeverSink-Filter-for-PoE2/releases/tag/0.10.4a) (2026-10-15)`

> **简介**：这是游戏“流亡之路 2”的战利品过滤器。它添加了颜色、声音、地图图标、光束来突出显示非凡的装备并通知用户

**💡 核心亮点更新 (中文)**：
- 小的风格改进
- 建立更好的系统来防止层级列表重复
- 架构更改（其中大部分用户还不会注意到）

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
*All updates are also available through [FilterBlade](https://www.filterblade.xyz) and on the [PoE filter ladder](https://www.pathofexile.com/item-filter/ladder/follower). Major thanks to all patreon supporters to help us fund the continuous development. [Patreon](https://www.patreon.com/Neversink) supporters also receive a Patreon-exclusive [Filter-Auto-Updater](https://youtu.be/i8RJx0s0zsA).*

This update focuses on finetuning the filter for the upcoming leagues and preparing for some long-term goals.

# CHANGES:

- Minor style improvements
- Established better systems to prevent tierlist duplications
- Architecture changes (most of these should not be noticeable to the user yet)

------

Developed by NeverSink

[![Follow me on Twitter](https://img.shields.io/badge/twitter-grey.svg?style=for-the-badge&logo=twitter)](https://twitter.com/NeverSinkDev) [![FilterBlade Discord](https://img.shields.io/badge/discord-grey.svg?style=for-the-badge&logo=discord)](https://discord.gg/mye6xhF) [![Watch FB Dev on Twitch](https://img.shields.io/badge/twitch-grey.svg?style=for-the-badge&logo=twitch)](https://twitch.tv/neversink) [![Support development on Patreon](https://img.shields.io/badge/patreon-grey.svg?style=for-the-badge&logo=patreon)](https://www.patreon.com/Neversink)
```
</details>

---
### 📦 [kenzok8/compile-package](https://github.com/kenzok8/compile-package)
`⭐ Stars: 165` &nbsp;|&nbsp; `💻 语言: Shell` &nbsp;|&nbsp; `🏷️ 最新版本: [2026.11.01-20/23_arm_cortex-a9_vfpv3-d16](https://github.com/kenzok8/compile-package/releases/tag/2026.11.01-20/23_arm_cortex-a9_vfpv3-d16) (2026-11-01)`

> **简介**：small-package仓库，每日更新插件编译

**💡 核心亮点更新 (中文)**：
定时更新插件，推送发布 💤:

[下载链接] (https://dllkids.xyz/packages/arm_cortex-a9_vfpv3-d16/)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
定时更新插件，推送发布 💤:

[下载链接] (https://dllkids.xyz/packages/arm_cortex-a9_vfpv3-d16/)
```
</details>

---
### 📦 [jxxghp/MoviePilot](https://github.com/jxxghp/MoviePilot)
`⭐ Stars: 12,003` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.2.3](https://github.com/jxxghp/MoviePilot/releases/tag/v3.2.3) (2026-10-31)`

> **简介**：NAS媒体库自动化管理工具

**💡 核心亮点更新 (中文)**：
- 修复自定义剧集组的缺失季集计算，按所选剧集组重新识别；恢复订阅的严格媒体身份匹配，减少同名内容误匹配。
- 搜索与下载共享站点流控，保留频控错误原因，减少无效重试。
- 完善缺少元数据时的整理任务处理与结果结算，修复 Agent 定时任务的执行账号归属。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 本次更新内容

- 修复自定义剧集组的缺失季集计算，按所选剧集组重新识别；恢复订阅的严格媒体身份匹配，减少同名内容误匹配。
- 搜索与下载共享站点流控，保留频控错误原因，减少无效重试。
- 完善缺少元数据时的整理任务处理与结果结算，修复 Agent 定时任务的执行账号归属。
- 加强 API、文件管理及云盘操作的权限与目标校验。
- 完善 App 业务通知投递、海报展示和完整正文，修复重启或重新登录后通知误解绑的问题。
- 优化升级弹窗按钮文案与加载状态显示。
- 新增 iOS App 安装版本统计，遵循“分享使用统计”开关，支持查看 App 版本分布。
- iOS App 支持保存和切换多个服务，各服务分别保留登录状态；新增可选的本机钥匙串账号密码记忆。
- iOS App 优化服务列表与圆形左滑删除按钮，修复选站搜索返回时的导航中断，以及系统明暗切换后的顶部渐变异常。
- iOS App 改善启动加载与连接恢复，增加等待提示、“立即重试”和“更改地址”，并支持启动目录请求超时与有限重试。
- 修复数据库操作工具连接 PostgreSQL 时的驱动兼容性问题。
- 升级 pyasn1 至 [0.6.5](https://github.com/pyasn1/pyasn1/releases/tag/v0.6.5)，修复已知安全漏洞。

## 完整变更记录

- fix(download): 按所选剧集组重新计算缺失季集 (#7253) by @jxxghp ([a432906](https://github.com/jxxghp/MoviePilot/commit/a43290647503e8cd2039ec30059ed486bacc9b82))
- fix(database-operation): 用 psycopg 3 建同步引擎，修复缺 psycopg2 报错 (#7254) by @shyblacktea ([1000eae](https://github.com/jxxghp/MoviePilot/commit/1000eae146598c3ce80ce7750fecc6c4a76826b6))
- chore(release): publish v3.2.3 with frontend v3.2.3 (#7255) by @jxxghp ([142f41c](https://github.com/jxxghp/MoviePilot/commit/142f41cd3d6791e6b2fe5cc817b7d85b13b3164f))
- fix(site): skip search parameters when listing site categories by @MiCat-S ([4dfcac8](https://github.com/jxxghp/MoviePilot/commit/4dfcac8d041c042c4c83cc246dd7d0f083725dd5))
- fix: 按用户隔离 Web 智能助手临时附件 by @qingyukb ([aea8cf1](https://github.com/jxxghp/MoviePilot/commit/aea8cf11c48f012850a6444b8a0d03477feb20bd))
- fix(site): preserve text category IDs and replay resource configs by @jxxghp ([10e9ade](https
```
</details>

---
### 📦 [sandboxie-plus/Sandboxie](https://github.com/sandboxie-plus/Sandboxie)
`⭐ Stars: 19,848` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.18.8](https://github.com/sandboxie-plus/Sandboxie/releases/tag/v1.18.8) (2026-10-17)`

> **简介**：Sandboxie Plus 和 Classic

**💡 核心亮点更新 (中文)**：
![0 5 5](https://user-images.githubusercontent.com/3890945/105014988-575cb680-5a41-11eb-90d5-d942d28184b2.png)

发行说明

Sandboxie Plus 1.18.8 / Classic 5.73.8 为 Firefox 和其他沙盒浏览器带来了重要的兼容性改进

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
![0 5 5](https://user-images.githubusercontent.com/3890945/105014988-575cb680-5a41-11eb-90d5-d942d28184b2.png)

### Release Notes

Sandboxie Plus 1.18.8 / Classic 5.73.8 brings important compatibility improvements for Firefox and other sandboxed browsers, with a particular focus on fixing video playback issues.
Video playback now works correctly in sandboxed Firefox on websites such as Disney, Amazon Prime, Netflix, TVNZ and ESPN that rely on mediaCapabilities.decodingInfo() to check media support before starting playback. This resolves an issue that could leave videos unable to start on affected sites.
The release also improves AppContainer handling used by browsers and other applications to isolate their child processes. Fixes address missing sandbox permissions and overly restrictive substitute tokens that could prevent these processes from starting or accessing required system resources. Microsoft Edge can again use the corrected substitute token without enabling UnRestrictAppContainerToken by default.
A security fix addresses an out-of-bounds read in the GUI proxy’s MapWindowPoints handler that could expose service heap data to sandboxed callers. The Import Boxes workflow has also been corrected, allowing users to choose where imported sandboxes are created.
For existing sandboxes, the new fixboxdacls command in KmdUtil.exe adds missing AppContainer access permissions. Advanced configuration options provide additional control: KeepBroadGroupsInAppContainerToken=n
```
</details>

---
### 📦 [HMBSbige/NatTypeTester](https://github.com/HMBSbige/NatTypeTester)
`⭐ Stars: 4,903` &nbsp;|&nbsp; `💻 语言: C#` &nbsp;|&nbsp; `🏷️ 最新版本: [10.0.10](https://github.com/HMBSbige/NatTypeTester/releases/tag/10.0.10) (2026-10-08)`

> **简介**：测试当前网络的 NAT 类型（STUN）

**💡 核心亮点更新 (中文)**：
- 修复 Linux 在中文、日文等语言环境下可能选用错误默认字体，导致小写字母显示为小型大写等文字显示异常的问题（#332）

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 🐛 修复

- 修复 Linux 在中文、日文等语言环境下可能选用错误默认字体，导致小写字母显示为小型大写等文字显示异常的问题（#332）

**完整变更**：[10.0.9 → 10.0.10](https://github.com/HMBSbige/NatTypeTester/compare/10.0.9...10.0.10)
```
</details>

---

## <span id="-影音媒体与下载">🎬 影音媒体与下载</span>

### 📦 [KnifeLemon/Filee](https://github.com/KnifeLemon/Filee)
`⭐ Stars: 20,308` &nbsp;|&nbsp; `💻 语言: C#` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.2.0](https://github.com/KnifeLemon/Filee/releases/tag/v2.2.0) (2026-10-28)`

> **简介**：免费的开源文件转换器。通过拖放功能离线转换 263 格式 — 图像、PDF、Word、Excel、PowerPoint、HWP/HWPX、视频、音频、电子书和档案。无需上传，无需 Office。

**💡 核心亮点更新 (中文)**：
发生了什么变化

<!--更新
级别：推荐
zh: 图像编辑：在窗口中即时转换大小、格式和旋转。
en: 马赛克·模糊：分享照片前可以隐藏你的名字、面孔和电话号码
ko：组合图像：通过向上、向下或横向连接多个图像来创建一个图像，就像身份证的正面和背面一样。
zh: 您可以裁剪为 4:5 或直接输入的比例，并且在切割多张纸时所选比例将保持不变。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## What's Changed

<!-- update
level: recommended
ko: 이미지 편집: 크기·형식·회전을 그때그때 창에서 골라 변환해요
ko: 모자이크·흐림: 사진을 공유하기 전에 이름, 얼굴, 전화번호를 가릴 수 있어요
ko: 이미지 합치기: 신분증 앞뒷면처럼 여러 장을 위아래나 옆으로 이어 한 장으로 만들어요
ko: 4:5나 직접 입력한 비율로 자를 수 있고, 고른 비율은 여러 장을 자르는 동안 그대로 유지돼요
ko: 너비와 높이를 정확히 맞추거나, 짧은 변이 정한 길이가 될 때까지 키울 수 있어요
ko: 결과 크기 제한(MB)을 정하고, 이메일·디스코드·왓츠앱·인스타그램용 프리셋을 바로 추가할 수 있어요
ko: 홈에서 변환을 되돌리고 저장할 곳을 매번 고를 수 있으며, 창 크기와 위치를 기억해요
ko: 분할 압축 파일(.001), .dav·.m4s 동영상, .fon 글꼴, 가민 FIT, .ini·.sql 파일까지 모두 268가지 형식을 지원해요
ko: DWG·DXF를 흑백이나 회색조로 바꿀 수 있고, 독일어를 지원해요
ko: calibre 변환이 10분 만에 멈추던 문제, 변환 중 마우스가 끊기던 문제, OCR한 중국어 글자 사이에 공백이 생기던 문제를 고쳤어요
ko: AppData를 다른 드라이브로 옮기면 엔진이 설치되지 않던 문제, macOS 전체 화면 앱 위에 원형 툴바가 뜨지 않던 문제 등을 고쳤어요
en: Edit pictures: choose the size, format and rotation in a window each time
en: Pixelate / blur: hide names, faces and phone numbers in a picture before you share it
en: Merge images: pictures one under another or side by side, like both sides of an ID card
en: Crop at 4:5 or a ratio you type, kept for the whole batch
en: Resize to an exact width and height, or enlarge pictures to a minimum short edge
en: A size limit in MB, and ready-made presets for email, Discord, WhatsApp and Instagram
en: Undo a conversion on Home, choose where to save each time, and the window remembers its size and place
en: Split archives (.001), .dav and .m4s videos, .fon fonts, Garmin FIT, .ini and .sql files: 268 formats in all
en: DWG and DXF in black and white or grayscale, and Filee i
```
</details>

---
### 📦 [guohuiyuan/go-music-dl](https://github.com/guohuiyuan/go-music-dl)
`⭐ Stars: 5,793` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.1.3](https://github.com/guohuiyuan/go-music-dl/releases/tag/v1.1.3) (2026-10-19)`

> **简介**：一个基于 Go 语言的全网音乐搜索与下载工具。支持 CLI 命令行与 Web 服务双模式，内置网易云、QQ、酷狗、Bilibili、汽水音乐等 10+ 个主流平台，支持多源并发搜索与无损音质解析。music-dl交流群：755087923

**💡 核心亮点更新 (中文)**：
* 2c1cefe7064fba6e46034359791060debbc935e6 feat(macos): 添加原生菜单集成以及文件夹选择器功能
* efc8d7c61ddb9b5ea22d6a86a39fa53df7f77997 feat(tv-ui)：增强电视端UI支持，新增焦点管理与样式设置 - 更新搜索框模板，加入电视端可获取焦点元素。 - 新增用于电视端UI布局与组件的CSS样式。 - 实现JavaScript函数，用于在电视模式下管理焦点和导航。 - 添加电视端UI资源相关测试，保障正常集成。 - 优化安卓构建流程，为电视应用加入横幅配置。
* 08c57dafb87be52ceee1cf79bf1d51f307c13e3e feat(任务栏): 实现Windows任务栏缩略图工具栏支持

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Changelog
* 2c1cefe7064fba6e46034359791060debbc935e6 feat(macos): 添加原生菜单集成以及文件夹选择器功能
* efc8d7c61ddb9b5ea22d6a86a39fa53df7f77997 feat(tv-ui)：增强电视端UI支持，新增焦点管理与样式设置 - 更新搜索框模板，加入电视端可获取焦点元素。 - 新增用于电视端UI布局与组件的CSS样式。 - 实现JavaScript函数，用于在电视模式下管理焦点和导航。 - 添加电视端UI资源相关测试，保障正常集成。 - 优化安卓构建流程，为电视应用加入横幅配置。
* 08c57dafb87be52ceee1cf79bf1d51f307c13e3e feat(任务栏): 实现Windows任务栏缩略图工具栏支持
* e62df49aaf9d34656fdf164d6baba29b580df573 feat(任务栏): 更新图标渲染逻辑，支持圆角图标并优化像素清除
* 7c899479cca5ca42dbbb3db4a9408e5ee7e404a8 feat(压缩): 添加 Gzip 中间件以支持响应压缩 feat(设置): 更新默认每页条数至 50，并调整相关提示 test(压缩): 添加 Gzip 中间件的单元测试
* 933b3faf48dce4220bc7bf796650e7944fa0b7c2 feat(安卓): 通过JS桥增强播放能力支持
* 28ef81ae4ffae2062efe3ba498c7d75bda4b0121 feat(歌曲卡片): 优化歌曲卡片加载状态显示，调整样式以提升用户体验
* decdc582b87404d0d15d794b25de0f85ac3c4865 feat(测试): 添加 HTTP 失败和重试机制的单元测试，优化错误处理逻辑
* 25bec39ffbd4303b3fff6410f76dc293249126ac feat(设置): 添加汽水音乐客户端安装目录配置选项
* 9b3a161e9c1d8f0db550e5cad1f547637b30a380 feat(音频路由)：实现音频路由准备与恢复功能
* 5f950bdc28d0c4b5ffaff853d8a0f47714b08f02 feat: 持久化下载队列与整单下载，完善下载管理和 macOS 桌面交互 (#253)
* ec91fbf140c730893fa2fe9e33c2a5ac1b78bb25 fix(ios): 修复移动端白屏并强化安装包校验
* ddf2a4e550ca67086ff1f06edc5d15c7d4c8663d fix(music): ensure response body is closed properly in RegisterMusicRoutes
* 0679b6b7f7531a42b54df637fa10142f71e14755 fix: 完善播放清单持久化与管理，修复 macOS 退出快捷键 (#254)
* 0280dbfda2821bb1394c06cb33eb676cbd4fbe39 优化 README 文档，简化使用说明和功能描述，增强可读性
* 65251969083510df00249d5ef2819b2a612f31da 功能 (本地音乐)：优化本地音乐文件的元数据缓存与索引
* 29eb77fd1f72b0ef5d1dba3e4a96775866ce26f4 功能(gzip)
```
</details>

---
### 📦 [LibreSpark/LibreTV](https://github.com/LibreSpark/LibreTV)
`⭐ Stars: 23,272` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.21.1](https://github.com/LibreSpark/LibreTV/releases/tag/v2.21.1) (2026-10-26)`

> **简介**：一分钟搭建影视站，支持Docker等部署方式

**💡 核心亮点更新 (中文)**：
获取方式

Docker（多架构 linux/amd64 / linux/arm64）

```bash
docker pull docker.io/bestzwei/libretv:2.21.1
docker pull ghcr.io/librespark/libretv:2.21.1
```

两个 registry 的镜像内容一致（同一组 digest），`latest` 也指向本版本。

免 Docker（下方附件，Node 18+）

```bash
sha256sum -c SHA2

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 获取方式

### Docker（多架构 linux/amd64 / linux/arm64）

```bash
docker pull docker.io/bestzwei/libretv:2.21.1
docker pull ghcr.io/librespark/libretv:2.21.1
```

两个 registry 的镜像内容一致（同一组 digest），`latest` 也指向本版本。

### 免 Docker（下方附件，Node 18+）

```bash
sha256sum -c SHA256SUMS
tar -xzf libretv-2.21.1-standalone.tar.gz -C libretv
cd libretv && PASSWORD=your-password PORT=8080 node server.js
```

预构建包与 CPU 架构无关（x86_64 / arm64 / armv7），环境变量与 Docker 部署一致。

> 镜像由 docker-publish 工作流在同一 tag 上构建，刚发布时可能还要 5–10 分钟才可拉取。

## 变更

完整对比：https://github.com/LibreSpark/LibreTV/compare/v2.21.0...v2.21.1
```
</details>

---
### 📦 [dyang886/Game-Cheats-Manager](https://github.com/dyang886/Game-Cheats-Manager)
`⭐ Stars: 15,898` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.5.4](https://github.com/dyang886/Game-Cheats-Manager/releases/tag/v2.5.4) (2026-10-11)`

> **简介**：Easily download and manage single-player game cheats for your convenience

**💡 核心亮点更新 (中文)**：
- Added a `Use IPv4 only for network connections` option in Settings, on by default. This can probably fix requests failing on some networks where DNS lookups return bad addresses.
- 设置中新增 `网络连接仅使用 IPv4` 选项，默认开启。这应该能修复部分网络环境下因 DNS 解析异常导致所有网络请求失败的问题

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Patch Update

### English
- Added a `Use IPv4 only for network connections` option in Settings, on by default. This can probably fix requests failing on some networks where DNS lookups return bad addresses.

### 简体中文
- 设置中新增 `网络连接仅使用 IPv4` 选项，默认开启。这应该能修复部分网络环境下因 DNS 解析异常导致所有网络请求失败的问题
```
</details>

---
### 📦 [DIYgod/RSSHub](https://github.com/DIYgod/RSSHub)
`⭐ Stars: 46,769` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2026.11.02-8524.8176658](https://github.com/DIYgod/RSSHub/releases/tag/v2026.11.02-8524.8176658) (2026-11-02)`

> **简介**：🧡 一切都是RSSible

**💡 核心亮点更新 (中文)**：
- ghcr.io/diygod/rsshub:817665869f47f5adecdbb70fef8d2dd16649a2ae
- ghcr.io/diygod/rsshub:chromium-bundled-817665869f47f5adecdbb70fef8d2dd16649a2ae
- diygod/rsshub:817665869f47f5adecdbb70fef8d2dd16649a2ae

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Source commit: 817665869f47f5adecdbb70fef8d2dd16649a2ae

Published multi-platform images:
- ghcr.io/diygod/rsshub:817665869f47f5adecdbb70fef8d2dd16649a2ae
- ghcr.io/diygod/rsshub:chromium-bundled-817665869f47f5adecdbb70fef8d2dd16649a2ae
- diygod/rsshub:817665869f47f5adecdbb70fef8d2dd16649a2ae
- diygod/rsshub:chromium-bundled-817665869f47f5adecdbb70fef8d2dd16649a2ae

Use these commit-specific image tags to reproduce this release. Daily Docker tags may be updated by subsequent builds.
```
</details>

---
### 📦 [amir1376/ab-download-manager](https://github.com/amir1376/ab-download-manager)
`⭐ Stars: 18,912` &nbsp;|&nbsp; `💻 语言: Kotlin` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.11.2](https://github.com/amir1376/ab-download-manager/releases/tag/v1.11.2) (2026-10-31)`

> **简介**：下载管理器可加快您的下载速度

**💡 核心亮点更新 (中文)**：
* 在 https://github.com/amir1376/ab-download-manager/pull/1488 中做出了第一个贡献

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
### Added

- Add download location to the desktop download list table (disabled by default) (#1483)
- Add an option to disable the `Add`/`Download` button while download link information is loading (#1508)
- Add Start Queue, Stop Queue, and Stop All actions to the system tray
- Add QR code support for sharing and scanning download links (#1511)

### Fixed

- Prevent download progress windows from being brought to the front when retrying a failed download (#1482)
- Enforce API key authentication for specific routes (#1512)

### Improved

- Update translations

## New Contributors
* @monurpalan made their first contribution in https://github.com/amir1376/ab-download-manager/pull/1488
```
</details>

---
### 📦 [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp)
`⭐ Stars: 204,586` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [2026.10.26](https://github.com/yt-dlp/yt-dlp/releases/tag/2026.10.26) (2026-10-26)`

> **简介**：功能丰富的命令行音频/视频下载器

**💡 核心亮点更新 (中文)**：
- **最低*所需* Python 版本已提升至 3.11**
- Python 3.10 已于 2026 年 10 月终止生命周期，yt-dlp 现已删除对其的支持。 [阅读更多](https://github.com/yt-dlp/yt-dlp/issues/16916)
- **官方 Windows 发行版二进制文件现在需要 Windows 10 或更高版本。** [阅读更多](https://github.com/yt-dlp/yt-dlp/issues/16917)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
[![Installation](https://img.shields.io/badge/-Which%20file%20to%20download%3F-white.svg?style=for-the-badge)](https://github.com/yt-dlp/yt-dlp#installation "Installation instructions") [![Discord](https://img.shields.io/discord/807245652072857610?color=blue&labelColor=555555&label=&logo=discord&style=for-the-badge)](https://discord.gg/H5MNcFW63r "Discord") [![Donate](https://img.shields.io/badge/_-Donate-red.svg?logo=githubsponsors&labelColor=555555&style=for-the-badge)](https://github.com/yt-dlp/yt-dlp/blob/master/Maintainers.md#maintainers "Donate") [![Documentation](https://img.shields.io/badge/-Docs-brightgreen.svg?style=for-the-badge&logo=GitBook&labelColor=555555)](https://github.com/yt-dlp/yt-dlp/tree/2026.10.26#readme "Documentation") [![Nightly](https://img.shields.io/badge/Nightly%20builds-purple.svg?style=for-the-badge)](https://github.com/yt-dlp/yt-dlp-nightly-builds/releases/latest "Nightly builds") [![Master](https://img.shields.io/badge/Master%20builds-lightblue.svg?style=for-the-badge)](https://github.com/yt-dlp/yt-dlp-master-builds/releases/latest "Master builds")

#### A description of the various files is in the [README](https://github.com/yt-dlp/yt-dlp#release-files)

The zipimport Unix executable and release tarball contain code licensed under ISC and MIT. The PyInstaller-bundled executables are subject to these and other licenses, all of which are compiled in [THIRD_PARTY_LICENSES.txt](https://github.com/yt-dlp/yt-dlp/blob/f264a6cbd1f630894da0f368df00f8
```
</details>

---
### 📦 [obsproject/obs-studio](https://github.com/obsproject/obs-studio)
`⭐ Stars: 78,796` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [33.0.1](https://github.com/obsproject/obs-studio/releases/tag/33.0.1) (2026-10-29)`

> **简介**：OBS Studio - 用于直播和屏幕录制的免费开源软件

**💡 核心亮点更新 (中文)**：
* 修复了登录服务集成时启动崩溃的问题 [WizardCM] ([#554](https://github.com/obsproject/obs-browser/pull/554))
* 修复了登录 Twitch 集成 [WizardCM] 时发生的崩溃（[#14072](https://github.com/obsproject/obs-studio/pull/14072)）
* 修复了登录 YouTube 集成时出现的死锁 [WizardCM] ([#556](https://github.com/obsproject/obs-browser/pull/556))

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
33.0.1 Hotfix Changes
---------------------

* Fixed a crash on startup when logged into a service integration [WizardCM] ([#554](https://github.com/obsproject/obs-browser/pull/554))
* Fixed a crash when logging into the Twitch integration [WizardCM] ([#14072](https://github.com/obsproject/obs-studio/pull/14072))
* Fixed a deadlock when logging into the YouTube integration [WizardCM] ([#556](https://github.com/obsproject/obs-browser/pull/556))
* Fixed a race condition where browser panels could end up with incorrectly sized content [WizardCM] ([#558](https://github.com/obsproject/obs-browser/pull/558))
* Fixed a memory leak when using the image slideshow source [prgmitchell] ([#14078](https://github.com/obsproject/obs-studio/pull/14078))
* Fixed plugins failing to load on Flatpak [FiniteSingularity] ([#14103](https://github.com/obsproject/obs-studio/pull/14103))
* Fixed Plugin Manager not prompting for save after a change until the dialog is re-opened [Warchamp7] ([#14112](https://github.com/obsproject/obs-studio/pull/14112))

33.0 New Features
-----------------

* Updated CEF from 127/6533 to 150/7871 [WizardCM] ([#13900](https://github.com/obsproject/obs-studio/pull/13900))
  + This is a massive update to the underlying framework used for browser sources and docks from the July 2024 release to September 2026
  + All of this work is on the backend and should be invisible to users. Please be sure to report any new weirdness or problems you run into with browse
```
</details>

---
### 📦 [jerrykuku/luci-theme-argon](https://github.com/jerrykuku/luci-theme-argon)
`⭐ Stars: 5,577` &nbsp;|&nbsp; `💻 语言: CSS` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.1.2](https://github.com/jerrykuku/luci-theme-argon/releases/tag/v3.1.2) (2026-11-02)`

> **简介**：Argon 是一个干净整洁的 OpenWrt LuCI 主题，允许用户使用图像或视频自定义其登录界面。   它还支持明暗模式自动和手动切换。

**💡 核心亮点更新 (中文)**：
- 修复端口卡片换行和高度不一致，兼容 ImmortalWrt。
- 修复 OpenList2 按钮文字不可见和 OpenClash 状态日志溢出。
- 优化 Dockerman、Passwall 和系统备注框布局。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 修复

- 修复端口卡片换行和高度不一致，兼容 ImmortalWrt。
- 修复 OpenList2 按钮文字不可见和 OpenClash 状态日志溢出。
- 优化 Dockerman、Passwall 和系统备注框布局。

## Fixed

- Fix port card wrapping and alignment, including ImmortalWrt.
- Fix invisible OpenList2 button text and overflowing OpenClash status logs.
- Improve Dockerman, Passwall and system notes layouts.

v3.1.0 及以上可在线升级。安装说明：[中文](https://github.com/jerrykuku/luci-theme-argon/blob/v3.1.2/README_ZH.md#安装) · [English](https://github.com/jerrykuku/luci-theme-argon/blob/v3.1.2/README.md#install)
```
</details>

---
### 📦 [qier222/YesPlayMusic](https://github.com/qier222/YesPlayMusic)
`⭐ Stars: 33,513` &nbsp;|&nbsp; `💻 语言: Vue` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.4.11](https://github.com/qier222/YesPlayMusic/releases/tag/v0.4.11) (2026-10-10)`

> **简介**：高颜值的第三方网易云播放器，支持 Windows / macOS / Linux :electron: 

**💡 核心亮点更新 (中文)**：
- **Touch Bar 歌词**：在配备 Touch Bar 的 MacBook 上，播放时 Touch Bar 中间会实时显示当前歌词（原有的前进 / 后退、搜索和播放列表按钮已移除，以留出显示空间），感谢 [](https://github.com/KawakazeNotFound)（#2407）
- **主题颜色**：设置页新增「主题颜色」选项，除原始颜色外，还提供日落、海洋、森林三种渐变配色，感谢 [](https://github.com/wuzhi456)（#2461）
- **托盘图标颜色**：设置页新增「托盘图标颜色」选项，可选择自动、浅色或深色，让托盘图标在不同系统主题和任务栏背景下都清晰可见，感谢 [](https://github.com/657kbps)（#2414）

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 更新日志

### ✨ 新特性

- **Touch Bar 歌词**：在配备 Touch Bar 的 MacBook 上，播放时 Touch Bar 中间会实时显示当前歌词（原有的前进 / 后退、搜索和播放列表按钮已移除，以留出显示空间），感谢 [@KawakazeNotFound](https://github.com/KawakazeNotFound)（#2407）
- **主题颜色**：设置页新增「主题颜色」选项，除原始颜色外，还提供日落、海洋、森林三种渐变配色，感谢 [@wuzhi456](https://github.com/wuzhi456)（#2461）
- **托盘图标颜色**：设置页新增「托盘图标颜色」选项，可选择自动、浅色或深色，让托盘图标在不同系统主题和任务栏背景下都清晰可见，感谢 [@657kbps](https://github.com/657kbps)（#2414）
- **云盘歌曲内嵌歌词**：播放未与网易云曲库关联的云盘歌曲时，会显示上传音频文件中内嵌的歌词，感谢 [@Cinvin](https://github.com/Cinvin)（#2419）
- **每日推荐一键播放**：每日推荐页面新增「播放」按钮，可直接播放全部推荐歌曲，感谢 [@Utopia-V](https://github.com/Utopia-V)（#2482）

### 🐛 修复

- 修复听歌记录无法同步到网易云音乐的问题：网易云已不再统计旧接口上报的播放记录，现改为与官方客户端相同的上报方式，「最近播放」与「听歌排行」恢复正常更新；同时修复一首歌自然播放结束时被重复上报、以及未实际播放的歌曲也被上报的问题，感谢 [@LucasYanzy](https://github.com/LucasYanzy)（#2485）
- 修复歌曲缓存上限不生效、缓存会无限增长的问题，感谢 [@fatelove42](https://github.com/fatelove42)（#2430）
- 修复歌词页最后几行歌词无法滚动到页面中间的问题，感谢 [@LucasYanzy](https://github.com/LucasYanzy)（#2487）
- 修复在歌词页进入全屏后离开歌词页，窗口会卡在全屏状态、只能按 F11 退出的问题，感谢 [@xianshi3](https://github.com/xianshi3)（#2483）
- 修复歌词时间戳中的毫秒部分解析错误，导致部分歌词与歌曲不同步的问题，感谢 [@HomeArchbishop](https://github.com/HomeArchbishop)（#2441）
- 修复在播放栏上拖动进度条或音量条时，松开鼠标会误打开歌词页的问题，感谢 [@12471220](https://github.com/12471220)（#2444）
- 修复深色主题下托盘菜单图标对比度不足、看不清的问题，感谢 [@Utopia-V](https://github.com/Utopia-V)（#2481）
- Linux：修复 D-Bus 断开连接后 MPRIS 更新导致应用崩溃的问题，感谢 [@FSpark](https://github.com/FSpark) 和 [@GyrumAscend](https://github.com/GyrumAscend)（#2457、#2480）
- 网页版：修复部署到 Netlify 后直接访问子页面出现 404 的问题，感谢 [@LittleChest](htt
```
</details>

---
### 📦 [agalwood/Motrix](https://github.com/agalwood/Motrix)
`⭐ Stars: 57,686` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.2.0](https://github.com/agalwood/Motrix/releases/tag/v2.2.0) (2026-11-01)`

> **简介**：功能齐全的下载管理器。

**💡 核心亮点更新 (中文)**：
* 修复（bridge）：通过 https://github.com/agalwood/Motrix/pull/2468 隔离浏览器扩展安装
* 修复（bridge）：在 https://github.com/agalwood/Motrix/pull/2469 中的引擎调度之前清理浏览器 cookie
* 修复（最终确定）：支持 macos 上的 paragon ntfs 发布，网址为 https://github.com/agalwood/Motrix/pull/2464

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# Motrix 2.2.0

English | [简体中文](https://github.com/agalwood/Motrix/blob/v2.2.0/docs/release-notes/2.2.0.zh-CN.md)

Motrix 2.2.0 restores optional desktop download progress, enables browser-extension
media downloads on Server, and improves torrent metadata validation. It also fixes
browser-profile connections, cookie handoff, speed modes, and Paragon NTFS completion.

## Changes since 2.1.1

- Add an optional download-progress indicator for the macOS Dock and Windows
  taskbar. Enable it in Appearance; it is off by default. Progress survives
  lightweight-mode window release and is cleared when transfers finish or the
  option is disabled. The option is not enabled on Linux or Web.
- Apply the selected standard or low-speed profile when switching modes, including
  automatic switching. Empty low-speed fields inherit their corresponding
  standard values; adaptive limits continue to constrain Automatic mode.
- Clarify the Downloads **Connections** column: show HTTP connection counts
  during downloads and BT/magnet peers while downloading, fetching metadata, or
  seeding, including zero peers. Clear inactive counts and keep blank values
  last in either sort direction.
- Enable extension HLS/DASH downloads and separate audio/video merging on Server.
  FFmpeg detection is refreshed when the extension rescans capabilities, so
  installing or changing the executable does not require a Server restart.
  Media segments remain separate from the normal task list and are cancelled
  b
```
</details>

---
### 📦 [subhra74/xdm](https://github.com/subhra74/xdm)
`⭐ Stars: 8,253` &nbsp;|&nbsp; `💻 语言: Kotlin` &nbsp;|&nbsp; `🏷️ 最新版本: [v9.0.9](https://github.com/subhra74/xdm/releases/tag/v9.0.9) (2026-11-01)`

> **简介**：自 2013 年以来，快速、可靠的下载加速器和视频下载器

**💡 核心亮点更新 (中文)**：
下载

|安装人员|笔记|
|---|---|
| [xdm-app-9.0.9-arm64.dmg](https://github.com/subhra74/xdm/releases/download/v9.0.9/xdm-app-9.0.9-arm64.dmg) |适用于 Apple Silicon（M1 或更高版本）mac |
| [xdm-app-9.0.9-x64.dmg](https://github.com/subhra74/xdm

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Downloads

| Installer | Notes |
|---|---|
| [xdm-app-9.0.9-arm64.dmg](https://github.com/subhra74/xdm/releases/download/v9.0.9/xdm-app-9.0.9-arm64.dmg) | For Apple Silicon (M1 or later) mac |
| [xdm-app-9.0.9-x64.dmg](https://github.com/subhra74/xdm/releases/download/v9.0.9/xdm-app-9.0.9-x64.dmg) | For Intel mac |
| [xdm-9.0.9-arm64.msi](https://github.com/subhra74/xdm/releases/download/v9.0.9/xdm-9.0.9-arm64.msi) | For Windows ARM (Windows 10/11) |
| [xdm-9.0.9-x64.msi](https://github.com/subhra74/xdm/releases/download/v9.0.9/xdm-9.0.9-x64.msi) | For Windows x64 (Windows 10/11) |
| [xdmsetup-9.0.9.msi](https://github.com/subhra74/xdm/releases/download/v9.0.9/xdmsetup-9.0.9.msi) | Same as the x64 MSI; for XDM 8 (Microsoft Store) update notices |
| [xdm-app_9.0.9_amd64.deb](https://github.com/subhra74/xdm/releases/download/v9.0.9/xdm-app_9.0.9_amd64.deb) | For Debian / Ubuntu / Linux Mint x64 |
| [xdm-app_9.0.9_arm64.deb](https://github.com/subhra74/xdm/releases/download/v9.0.9/xdm-app_9.0.9_arm64.deb) | For Debian / Ubuntu / Linux Mint ARM |
| [xdm-app-9.0.9-1.aarch64.rpm](https://github.com/subhra74/xdm/releases/download/v9.0.9/xdm-app-9.0.9-1.aarch64.rpm) | For Fedora / RHEL / openSUSE ARM |
| [xdm-app-9.0.9-1.x86_64.rpm](https://github.com/subhra74/xdm/releases/download/v9.0.9/xdm-app-9.0.9-1.x86_64.rpm) | For Fedora / RHEL / openSUSE x64 |
| [xdm-app-9.0.9-1-aarch64.pkg.tar.zst](https://github.com/subhra74/xdm/releases/download/v9.0.9/xdm-app-9.0.9-1-aarch64.pkg.tar.z
```
</details>

---

## <span id="-效率办公与创作">📝 效率办公与创作</span>

### 📦 [robbietilton/Compositor](https://github.com/robbietilton/Compositor)
`⭐ Stars: 18,356` &nbsp;|&nbsp; `💻 语言: Swift` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.5.12](https://github.com/robbietilton/Compositor/releases/tag/v1.5.12) (2026-10-27)`

> **简介**：适用于 Mac 的 Photoshop 替代品

**💡 核心亮点更新 (中文)**：
- 新的边缘光滤镜：在拍摄对象后面添加最多三种颜色的光，每种都有自己的角度、强度、宽度和光圈
- 发光让光线渗入主体周围的空气中并包裹其边缘，因此它位于光线中，而不是看起来被剪掉
- 松散的发丝捕捉光线，而人群或岩石等繁忙的背景则保持不变

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
- New Rim Light filter: add up to three colored lights behind your subject, each with its own angle, strength, width and choke
- Glow lets the light bleed into the air around the subject and wrap over its edges, so it sits in the light instead of looking cut out
- Loose strands of hair catch the light, while busy backgrounds like crowds or rocks stay untouched
```
</details>

---
### 📦 [jgraph/drawio-desktop](https://github.com/jgraph/drawio-desktop)
`⭐ Stars: 63,763` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v32.6.1](https://github.com/jgraph/drawio-desktop/releases/tag/v32.6.1) (2026-10-23)`

> **简介**：Official electron build of draw.io

**💡 核心亮点更新 (中文)**：
- Uses electron 44.9.3
- Includes the Electron mitigation for the compromised eMudhra intermediate certificates [GHSA-jr5w-w6x2-84p9]
- Updates to [draw.io core 32.6.1](https://github.com/jgraph/drawio/blob/v32.6.1/ChangeLog). All changes from 32.5.5 to 32.6.1 are added in this build.

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Release Notes for 32.6.1

[Windows Installer](https://github.com/jgraph/drawio-desktop/releases/download/v32.6.1/draw.io-32.6.1-windows-installer.exe)
[Windows No Installer (zip)](https://github.com/jgraph/drawio-desktop/releases/download/v32.6.1/draw.io-32.6.1-windows.zip)
[macOS - Universal](https://github.com/jgraph/drawio-desktop/releases/download/v32.6.1/draw.io-universal-32.6.1.dmg)
Linux - [deb](https://github.com/jgraph/drawio-desktop/releases/download/v32.6.1/drawio-amd64-32.6.1.deb), [AppImage](https://github.com/jgraph/drawio-desktop/releases/download/v32.6.1/drawio-x86_64-32.6.1.AppImage) or [rpm](https://github.com/jgraph/drawio-desktop/releases/download/v32.6.1/drawio-x86_64-32.6.1.rpm)

**ChangeLog:**

- Uses electron 44.9.3
- Includes the Electron mitigation for the compromised eMudhra intermediate certificates [GHSA-jr5w-w6x2-84p9]
- Updates to [draw.io core 32.6.1](https://github.com/jgraph/drawio/blob/v32.6.1/ChangeLog). All changes from 32.5.5 to 32.6.1 are added in this build.

**Testing:**

Verified against the packaged, signed macOS build. Windows and Linux packages were verified from the produced release artifacts, their sizes and update manifests, rather than by running them.

Base checks

- Launch, open a file passed on the command line, add and edit shapes, change styles, undo and redo, copy and paste through the system clipboard, save, reopen, insert, rename and delete pages, and zoom
- Export to PNG, JPEG, SVG, PDF, XML and
```
</details>

---
### 📦 [Stirling-Tools/Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF)
`⭐ Stars: 95,541` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.2.2](https://github.com/Stirling-Tools/Stirling-PDF/releases/tag/v3.2.2) (2026-10-24)`

> **简介**：#1 PDF Application on GitHub that lets you edit PDFs on any device anywhere

**💡 核心亮点更新 (中文)**：
Another small release with some bug fixes

- Fix for some viewer rendering issues 
- New auto fit to width button for viewer
- New annotation shape options like arrow and polyline
- QR code stamp types

What's Changed
Bug Fixes
* fix(i18n): 

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Another small release with some bug fixes

- Fix for some viewer rendering issues 
- New auto fit to width button for viewer
- New annotation shape options like arrow and polyline
- QR code stamp types

## What's Changed
### Bug Fixes
* fix(i18n): expand Turkish translations by @alkank in https://github.com/Stirling-Tools/Stirling-PDF/pull/8123
* fix(viewer): render non-embedded fonts with matching widths by @reecebrowne in https://github.com/Stirling-Tools/Stirling-PDF/pull/8629
### Enhancements
* feat(viewer): Fit to width and fit to page buttons in the viewer by @EthanHealy01 in https://github.com/Stirling-Tools/Stirling-PDF/pull/8485
* Fix race condition in storybook by @jbrunton96 in https://github.com/Stirling-Tools/Stirling-PDF/pull/8619
* build(deps-dev): bump fast-uri from 3.1.7 to 3.1.9 in /frontend by @dependabot[bot] in https://github.com/Stirling-Tools/Stirling-PDF/pull/8580
* build(deps-dev): bump ip-address from 10.7.2 to 10.7.4 in /frontend by @dependabot[bot] in https://github.com/Stirling-Tools/Stirling-PDF/pull/8630
* build(deps): bump dompurify from 3.4.16 to 3.4.17 in /frontend by @dependabot[bot] in https://github.com/Stirling-Tools/Stirling-PDF/pull/8631
* Shard a11y nightlies by @jbrunton96 in https://github.com/Stirling-Tools/Stirling-PDF/pull/8573
* Fix existing CI errors in Rust by @jbrunton96 in https://github.com/Stirling-Tools/Stirling-PDF/pull/8585
* feat(annotate): add Arrow and Polyline tools by @reecebrowne in https://githu
```
</details>

---
### 📦 [halo-dev/halo](https://github.com/halo-dev/halo)
`⭐ Stars: 40,101` &nbsp;|&nbsp; `💻 语言: Java` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.27.1](https://github.com/halo-dev/halo/releases/tag/v2.27.1) (2026-10-23)`

> **简介**：Halo 是一款强大易用的开源建站工具，从个人博客、知识库，到企业官网、在线商城，Halo 都能助您轻松实现，一站式满足您的多样化建站需求。

**💡 核心亮点更新 (中文)**：
- 修复升级 Halo 后登录、注册等页面可能仍使用旧版静态资源的问题 by  in #10391
- 修复按标签查询文章接口的响应文档和生成客户端类型错误地表示为单篇文章的问题 by  in #10393
- 修复在表单中嵌入编辑器时，点击气泡菜单等编辑器按钮可能触发表单提交的问题 by  in #10398

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
**此版本包含安全更新，建议所有用户尽快升级。**

## 问题修复

- 修复升级 Halo 后登录、注册等页面可能仍使用旧版静态资源的问题 by @ruibaby in #10391
- 修复按标签查询文章接口的响应文档和生成客户端类型错误地表示为单篇文章的问题 by @ruibaby in #10393
- 修复在表单中嵌入编辑器时，点击气泡菜单等编辑器按钮可能触发表单提交的问题 by @ruibaby in #10398
- 修复插件列表全选框使用文章管理权限判断的问题，使其与插件管理权限保持一致 by @ruibaby in #10400
- 修复 HTTP/1.1 keep-alive 连接可能停止读取后续请求的问题，并保留本地化错误响应（升级 Spring Boot 至 4.1.2） by @JohnNiang in #10408
- 更新 Docker 镜像中受影响的 eMudhra emSign 中间 CA 证书与根证书，避免继续信任私钥已泄露的证书（CVE-2026-91403） by @JohnNiang in #10414

## 依赖更新

- 升级前端 HTML 净化与 Markdown 相关依赖（dompurify、sanitize-html、markdown-it）至安全修复版本 by @ruibaby in #10407

**Full Changelog**: https://github.com/halo-dev/halo/compare/v2.27.0...v2.27.1
```
</details>

---
### 📦 [zyx0814/dzzoffice](https://github.com/zyx0814/dzzoffice)
`⭐ Stars: 4,053` &nbsp;|&nbsp; `💻 语言: PHP` &nbsp;|&nbsp; `🏷️ 最新版本: [2.4.2](https://github.com/zyx0814/dzzoffice/releases/tag/2.4.2) (2026-10-22)`

> **简介**：dzzoffice

**💡 核心亮点更新 (中文)**：
- 在线应用市场支持搜索应用。
- 优化删除用户逻辑，清理更多关联用户数据，减少冗余数据残留。
- 优化机构用户验证表单的提示信息，提升错误指引清晰度与准确性。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## V2.4.2 主要更新内容
> **发布于: 2026.10.22**
### 应用市场
- 在线应用市场支持搜索应用。
### 机构用户
- 优化删除用户逻辑，清理更多关联用户数据，减少冗余数据残留。
- 优化机构用户验证表单的提示信息，提升错误指引清晰度与准确性。
- 修复部门无法变更为机构（2级部门不能转为1级部门）的问题。
- 修复添加机构部门管理员时权限判断错误（已修正为判断上级权限）。
- 修复普通管理员可修改系统管理员信息的权限越权问题。
### 网盘
- 优化文件管理排序UI与分享页UI。
- 优化网盘搜索点击清空后回到最近使用页面。
- 网盘支持设置是否显示隐藏文件。
- 隐藏文件元数据中的文件路径，提升系统安全性。
- 移除重复加载的文件上传脚本。
- 修复上传文件报错问题。
- 修复上传同名文件进行覆盖时文件内容丢失问题。
- 修复上传同名文件处理功能失效问题。
- 修正网盘取消分享时的错误提示。
- 修复分享文件设置允许重命名时，部分用户不能重命名的问题。
- 修改重命名文件时更新文件修改时间导致数据不一致的问题。
- 修复系统管理员不能清空回收站的问题。
- 修复网盘恢复文件异常问题。
- 修复修改/获取文件夹附属信息异常问题。
- 修复分享文件创建/修改时无权限校验的问题。
- 修复文件选择框路径未选中及数据重复加载问题。
- 修复网络挂载异常提示无权限的问题。
- 修复网络挂载不能正常显示文件列表问题。
### 系统
- 优化安装程序。
- 修正系统报错显示内容，并支持显示更多信息。
- 注册页支持“隐藏”或“选填”邮箱字段。
- 修复认证设置提交报错问题。
- 修复开启缓存时用户修改个人设置后不能及时生效的问题。
- 解决缓存权限数据导致用户权限更新不及时的问题，确保权限实时生效。
- 修复管理页不能退出登录状态的问题（修改 formhash 生成方式）。
- 修复编辑器粘贴的图片不能放大预览的问题。
- 修复开启调试模式后不能访问的问题。
- 修复大写 PHP 文件上传绕过安全检查的执行漏洞。
- 规范数据库 SQL 语句，修复 SQL 注入漏洞（含删除查询双重转义问题）。
- 文件管理、系统日志、评论应用支持 URL 地址变化。
- 规范化代码并修复若干已知问题。
### 系统通知
- 通知模块性能优化（修复定时器递归、增加资源清理）。
### 计划任务
- 修复重复创建任务的问题。
### 默认首页
- 优化默认首页的日期时间显示；按自然日计算首页加入时长。
### 系统设置
- 系统设置添加修改系统配置文件的指引说明。
### 系统日志
- 新增用户信息更新、机构/部门/群组信息修改的操作记录。
- 修复登录日志重复记录问题。
- 修复后台访问操作记录部分参数缺失问题。

### 升级须知
**1. 版本适配：**
- 从 **V2.4.1** 升级至 V2.4.2：无需执行升级程序
- 从 **V2.01 ~ V2.4.0** 版本升级至 V2.4.2：必须执行升级程序

**2. 升级方式：**
- 在线升级：通过「系统工具」→「在线升级」自动完成；
- 离线升级：需手动下载最新源码并覆盖后，再访问`http(s)://您的域名/install/update.php` 执行升级。

**3. 缓存清理：** 升级后，需登录管理后台，前往「系统工具」清理系统缓存（含数据缓
```
</details>

---
### 📦 [emoacht/Monitorian](https://github.com/emoacht/Monitorian)
`⭐ Stars: 4,792` &nbsp;|&nbsp; `💻 语言: C#` &nbsp;|&nbsp; `🏷️ 最新版本: [4.16.8-Installer](https://github.com/emoacht/Monitorian/releases/tag/4.16.8-Installer) (2026-10-31)`

> **简介**：轻松调节多台显示器亮度的 Windows 桌面工具

**💡 核心亮点更新 (中文)**：
- 补充简体中文（zh-Hans）和繁体中文（zh-Hant）语言。感谢！
- 改进内部代码

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
- Supplement Simplified Chinese (zh-Hans) and Traditional Chinese (zh-Hant) langauges. Thank to @380086154!
- Improve internal code
```
</details>

---
### 📦 [YerongAI/Office-Tool](https://github.com/YerongAI/Office-Tool)
`⭐ Stars: 14,638` &nbsp;|&nbsp; `💻 语言: PowerShell` &nbsp;|&nbsp; `🏷️ 最新版本: [v11.8.50.0](https://github.com/YerongAI/Office-Tool/releases/tag/v11.8.50.0) (2026-10-18)`

> **简介**：Office Tool Plus 本地化项目。

**💡 核心亮点更新 (中文)**：
- 调整了外观。
- 其他错误修复和改进。
- 支持根据Windows版本检索合适的Office版本。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Change log

- Adjusted the appearance.
- Other bugs fixed and improvements.

### Deploy

- Supports retrieving the appropriate Office version based on the Windows edition.
- Fixed an issue where Office and Windows version numbers could not be correctly compared in certain cases.
- Removed the setting to pin Office icons to the taskbar.

### Activate

- Support to read and set the Licensing mode for Microsoft 365.

### Toolbox

- If a restart is required when removing Office, a notification will be added to the log output.

## Translation

it-it: @bovirus
pt-br: @igorruckert 
th-th: @dekthaiinchina 
pl-pl: @jakubdriver
```
</details>

---
### 📦 [microsoft/vscode](https://github.com/microsoft/vscode)
`⭐ Stars: 194,470` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [1.144.0](https://github.com/microsoft/vscode/releases/tag/1.144.0) (2026-10-28)`

> **简介**：视觉工作室代码

**💡 核心亮点更新 (中文)**：
https://code.visualstudio.com/updates/v1_144

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
https://code.visualstudio.com/updates/v1_144
```
</details>

---

## <span id="-网络与代理技术">🌐 网络与代理技术</span>

### 📦 [bestruirui/BestSub](https://github.com/bestruirui/BestSub)
`⭐ Stars: 2,136` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.0.6](https://github.com/bestruirui/BestSub/releases/tag/v2.0.6) (2026-10-07)`

> **简介**：最佳子系统，最适合您的网络

**💡 核心亮点更新 (中文)**：
*无重大变化*

    [在 GitHub 上查看更改](https://github.com/bestruirui/BestSub/compare/v2.0.5...v2.0.6)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
*No significant changes*

##### &nbsp;&nbsp;&nbsp;&nbsp;[View changes on GitHub](https://github.com/bestruirui/BestSub/compare/v2.0.5...v2.0.6)
```
</details>

---
### 📦 [SagerNet/sing-box](https://github.com/SagerNet/sing-box)
`⭐ Stars: 39,523` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.14.4](https://github.com/SagerNet/sing-box/releases/tag/v1.14.4) (2026-10-24)`

> **简介**：The universal proxy platform

**💡 核心亮点更新 (中文)**：
* Fixes and improvements

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## :memo: Release Notes

* Fixes and improvements
```
</details>

---
### 📦 [sub-store-org/Sub-Store](https://github.com/sub-store-org/Sub-Store)
`⭐ Stars: 10,813` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [2.44.2](https://github.com/sub-store-org/Sub-Store/releases/tag/2.44.2) (2026-10-25)`

> **简介**：Advanced Subscription Manager for QX, Loon, Surge, Stash, Egern and Shadowrocket!

**💡 核心亮点更新 (中文)**：
* feat: 优化 Gist 逻辑 ([c101811](https://github.com/sub-store-org/Sub-Store/commit/c101811))

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## <small>2.44.2 (2026-10-25)</small>

* feat: 优化 Gist 逻辑 ([c101811](https://github.com/sub-store-org/Sub-Store/commit/c101811))
```
</details>

---
### 📦 [233boy/Xray](https://github.com/233boy/Xray)
`⭐ Stars: 2,790` &nbsp;|&nbsp; `💻 语言: Shell` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.37](https://github.com/233boy/Xray/releases/tag/v1.37) (2026-11-02)`

> **简介**：最好用的 Xray 一键安装脚本 & 管理脚本

**💡 核心亮点更新 (中文)**：
更新
```
xray up sh
```

变化

默认添加 Hysteria2 协议


关注我们

网站: https://233boy.com

群组: https://t.me/tg233boy

频道: https://t.me/tg2333

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 更新
```
xray up sh
```

## 变化

默认添加 Hysteria2 协议


## 关注我们

网站: https://233boy.com

群组: https://t.me/tg233boy

频道: https://t.me/tg2333
```
</details>

---
### 📦 [enfein/mieru](https://github.com/enfein/mieru)
`⭐ Stars: 2,663` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.39.0](https://github.com/enfein/mieru/releases/tag/v3.39.0) (2026-10-23)`

> **简介**：mieru is a socks5 / HTTP / HTTPS proxy to bypass censorship. 見える是一款 socks5 / HTTP / HTTPS 网络代理翻墙工具。

**💡 核心亮点更新 (中文)**：
1. Allow mita proxy server to actively shutdown idle TCP connection (issue 317).
2. Optimize memory allocation of outbound traffic.

---

1. 允许 mita 代理服务器主动关闭空闲 TCP 连接。
2. 优化了出站流量的内存分配。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
1. Allow mita proxy server to actively shutdown idle TCP connection (issue #317).
2. Optimize memory allocation of outbound traffic.

---

1. 允许 mita 代理服务器主动关闭空闲 TCP 连接。
2. 优化了出站流量的内存分配。
```
</details>

---
### 📦 [v2rayA/v2rayA](https://github.com/v2rayA/v2rayA)
`⭐ Stars: 15,784` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.5.13](https://github.com/v2rayA/v2rayA/releases/tag/v2.5.13) (2026-11-02)`

> **简介**：一个基于 Xray 的核心的 Web 客户端，在 Linux、Windows 和 macOS 上具有全局透明代理。

**💡 核心亮点更新 (中文)**：
* 修复（v2ray）：保持系统代理和 tun 互斥，通过 https://github.com/v2rayA/v2rayA/pull/2086
* 壮举：通过 https://github.com/v2rayA/v2rayA/pull/2102 将 xray 核心升级到 v26.10.31

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## What's Changed
* chore(deps): bump serialize-javascript from 7.1.1 to 7.1.2 in /gui by @dependabot[bot] in https://github.com/v2rayA/v2rayA/pull/2074
* fix(v2ray): keep system proxy and tun mutually exclusive by @miaomiaoyaoqimiaomaoxian in https://github.com/v2rayA/v2rayA/pull/2086
* chore(deps): bump source-map-js from 1.0.2 to 1.2.2 in /gui by @dependabot[bot] in https://github.com/v2rayA/v2rayA/pull/2085
* chore(deps): bump github.com/klauspost/compress from 1.17.4 to 1.18.7 in /core by @dependabot[bot] in https://github.com/v2rayA/v2rayA/pull/2089
* feat: upgrade xray core to v26.10.31 by @MarksonHon in https://github.com/v2rayA/v2rayA/pull/2102


**Full Changelog**: https://github.com/v2rayA/v2rayA/compare/v2.5.10...v2.5.13
```
</details>

---
### 📦 [vernesong/OpenClash](https://github.com/vernesong/OpenClash)
`⭐ Stars: 28,039` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.48.002](https://github.com/vernesong/OpenClash/releases/tag/v0.48.002) (2026-10-12)`

> **简介**：OpenWrt 的 Clash 客户端

**💡 核心亮点更新 (中文)**：
* 2026-10-12 11:40 GMT+0800
* [WIKI & SKILL](https://github.com/vernesong/OpenClash/blob/dev/.github/skills/openclash-user-guide/SKILL.md)
* 启动前请先在插件设置页面的版本更新标签下确认`内核编译版本`，您也可以手动下载 [Clash内核](https://github.com/MetaCubeX/mihomo/releases) 后解压到 `/etc/openclash/core/`文件夹，并将二进制文件命名为`clash_meta`

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# 发布时间
* 2026-10-12 11:40 GMT+0800

# 使用手册
* [WIKI & SKILL](https://github.com/vernesong/OpenClash/blob/dev/.github/skills/openclash-user-guide/SKILL.md)

# 安装命令

在路由器上以 root 身份执行（需要 `curl` 与 `ca-bundle`）：

```shell
(curl -fsSL -o /tmp/install.sh https://raw.githubusercontent.com/vernesong/OpenClash/dev/install.sh || curl -fsSL -o /tmp/install.sh https://cdn.jsdelivr.net/gh/vernesong/OpenClash@dev/install.sh) && sh /tmp/install.sh
```

<details>
<summary>手动安装（不使用脚本时）</summary>

安装依赖并下载最新版（iptables 防火墙）：

```shell
# opkg 系统（ipk）
opkg update
opkg install bash iptables dnsmasq-full curl ca-bundle ipset ip-full iptables-mod-tproxy iptables-mod-extra ruby ruby-yaml kmod-tun kmod-inet-diag unzip luci-compat luci luci-base
curl -L --retry 2 https://api.github.com/repos/vernesong/OpenClash/releases/latest -o /tmp/openclash_version
[ -f "/tmp/openclash_version" ] && download_url=$(cat /tmp/openclash_version | jsonfilter -e '@.assets[*].browser_download_url' | grep '\.ipk$') && curl -L --retry 2 "$download_url" -o /tmp/openclash.ipk || echo "OpenClash last version get failed"
[ -f "/tmp/openclash.ipk" ] && opkg install /tmp/openclash.ipk || echo "OpenClash download failed"

# apk 系统（apk）
apk update
apk add bash iptables dnsmasq-full curl ca-bundle ipset ip-full iptables-mod-tproxy iptables-mod-extra ruby ruby-yaml kmod-tun kmod-inet-diag unzip luci-compat luci luci-base
curl -L --retry 2 https://api.github.com/repos/vernesong/OpenClash/releases/latest -o /
```
</details>

---
### 📦 [HyNetworks/hysteria](https://github.com/HyNetworks/hysteria)
`⭐ Stars: 22,823` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [app/v2.13.0](https://github.com/HyNetworks/hysteria/releases/tag/app/v2.13.0) (2026-10-05)`

> **简介**：Hysteria 是一款功能强大、速度快如闪电且抗审查的开源代理软件

**💡 核心亮点更新 (中文)**：
- 修复了现代浏览器和 QUIC 库的 QUIC [协议嗅探](https://hysteria.network/docs/advanced/Full-Server-Config/#protocol-sniffing)，其 ClientHello 跨越多个数据包。基于域的 [ACL](https://hysteria.network/docs/advanced/ACL/) 规则现在适用于其 QUIC 流量
- `sniff.timeout` 现在仅适用于 TCP
- 将[TUN模式](https://hysteria.network/docs/advanced/Full-Client-Config/#tun)升级到最新的上游sing-tun (v0.9.6)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
- Fixed QUIC [protocol sniffing](https://hysteria.network/docs/advanced/Full-Server-Config/#protocol-sniffing) for modern browsers and QUIC libraries, whose ClientHello spans multiple packets. Domain-based [ACL](https://hysteria.network/docs/advanced/ACL/) rules now apply to their QUIC traffic
- `sniff.timeout` now only applies to TCP
- Upgraded [TUN mode](https://hysteria.network/docs/advanced/Full-Client-Config/#tun) to the latest upstream sing-tun (v0.9.6)
- Removed the TUN `route.strict` option, which no longer had any effect
- Updated Chrome QUIC fingerprint parroting to match Chrome 154
- Fixed the client log reporting ECH as not accepted when Chrome parroting is enabled
- Updated quic-go to v0.63.0

---

- 修复 QUIC [协议嗅探](https://hysteria.network/zh/docs/advanced/Full-Server-Config/#sniff)无法识别将 ClientHello 分多个包发送的现代浏览器和 QUIC 库的问题。基于域名的 [ACL](https://hysteria.network/zh/docs/advanced/ACL/) 规则现可正常作用于这些 QUIC 流量
- `sniff.timeout` 现在仅对 TCP 生效
- [TUN 模式](https://hysteria.network/zh/docs/advanced/Full-Client-Config/#tun)升级至最新上游 sing-tun (v0.9.6)
- 移除了 TUN 的 `route.strict` 选项，此选项不再有任何作用
- Chrome QUIC 指纹模仿更新至 Chrome 154
- 修复启用 Chrome 指纹模仿时，客户端日志始终显示 ECH 未开启的问题
- quic-go 更新至 v0.63.0
```
</details>

---
### 📦 [QiuSimons/YAOF](https://github.com/QiuSimons/YAOF)
`⭐ Stars: 2,778` &nbsp;|&nbsp; `💻 语言: Shell` &nbsp;|&nbsp; `🏷️ 最新版本: [25.12.6](https://github.com/QiuSimons/YAOF/releases/tag/25.12.6) (2026-10-18)`

> **简介**：适用于 Nanopi R2C/R2S/R4S/X86 的 OpenWrt

**💡 核心亮点更新 (中文)**：
该版本未提供详细更新说明。

---
### 📦 [Loyalsoldier/v2ray-rules-dat](https://github.com/Loyalsoldier/v2ray-rules-dat)
`⭐ Stars: 20,986` &nbsp;|&nbsp; `💻 语言: Other` &nbsp;|&nbsp; `🏷️ 最新版本: [202611012203](https://github.com/Loyalsoldier/v2ray-rules-dat/releases/tag/202611012203) (2026-11-01)`

> **简介**：🦄 🎃 👻 V2Ray 路由规则文件加强版，可代替 V2Ray 官方 geoip.dat 和 geosite.dat，适用于 V2Ray、Xray-core、mihomo(Clash-Meta)、hysteria、Trojan-Go 和 leaf。Enhanced edition of V2Ray rules dat files, applicable to V2Ray, Xray-core, mihomo(Clash-Meta), hysteria, Trojan-Go and leaf.

**💡 核心亮点更新 (中文)**：
该版本未提供详细更新说明。

---
### 📦 [Openwrt-Passwall/openwrt-passwall](https://github.com/Openwrt-Passwall/openwrt-passwall)
`⭐ Stars: 9,986` &nbsp;|&nbsp; `💻 语言: Lua` &nbsp;|&nbsp; `🏷️ 最新版本: [26.10.29-1](https://github.com/Openwrt-Passwall/openwrt-passwall/releases/tag/26.10.29-1) (2026-10-29)`

> **简介**：暂无项目描述

**💡 核心亮点更新 (中文)**：
* 请按照 [openwrt-passwall-build](https://github.com/moetayuko/openwrt-passwall-build) 仓库的说明，将其提供的软件源添加到设备中，然后直接使用包管理器安装。
* 从 [SourceForge](https://sourceforge.net/projects/openwrt-passwall-build/files/) 下载预构建的软件包。
* 将文件上传到您的设备，使用 Shell 命令进行安装。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
![](https://img.shields.io/github/downloads/Openwrt-Passwall/openwrt-passwall/26.10.29-1/total?style=flat-square)
## :mega: 获取其他软件包 / How to Get Other Packages

### 方式 1：添加软件源 / Method 1: Add Software Source
 * 请按照 [openwrt-passwall-build](https://github.com/moetayuko/openwrt-passwall-build) 仓库的说明，将其提供的软件源添加到设备中，然后直接使用包管理器安装。
  Follow the instructions in the [openwrt-passwall-build](https://github.com/moetayuko/openwrt-passwall-build) repository to add the provided software source to your device, then install directly using the package manager.

### 方式 2：手动下载并安装 / Method 2: Manual Download and Install

* 从 [SourceForge](https://sourceforge.net/projects/openwrt-passwall-build/files/) 下载预构建的软件包。
  Download prebuilt packages from [SourceForge](https://sourceforge.net/projects/openwrt-passwall-build/files/).

* 将文件上传到您的设备，使用 Shell 命令进行安装。
  Upload files to your device, install it with shell command.

ipk
```
opkg install /path/to/package.ipk
```
apk
```
apk add --allow-untrusted /path/to/package.apk
```

:warning: 请将 /path/to/package 替换为实际下载的软件包路径。
- Replace /path/to/package with the actual path of the downloaded packages.

---
## :rocket: 配套固件与工具 / Firmwares & Tools

### :fire: [OpenWrtAction](https://github.com/smallprogram/OpenWrtAction) —— 集成 Passwall 的 CI 固件 / Ready-to-use firmware with Passwall
* 集成官方 OpenWrt 25.12、ImmortalWrt 25.12、Lean (Snapshot) 固件，支持 x86、R2S、R2C、R4S、R5S、R5C、H66K、H68K、H69K、R66S、R68S 等设备，刷入即用。
  Firmware built on official OpenWrt 25.12, ImmortalWrt 25.12
```
</details>

---
### 📦 [2dust/v2rayN](https://github.com/2dust/v2rayN)
`⭐ Stars: 119,763` &nbsp;|&nbsp; `💻 语言: C#` &nbsp;|&nbsp; `🏷️ 最新版本: [7.25.6](https://github.com/2dust/v2rayN/releases/tag/7.25.6) (2026-10-11)`

> **简介**：适用于 Windows、Linux 和 macOS 的 GUI 客户端，支持 Xray 和 sing-box 等

**💡 核心亮点更新 (中文)**：
* 支持 sing-box v1.14，更新的用户注意内核版本 #9736
* 锁定最大 sing-box 版本 v1.14  #10091
* 添加通过代理更新检查更新的选项 - #10090

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
### [关于 跳过证书验证 allowInsecure 参数被移除的说明 ](https://github.com/2dust/v2rayN/discussions/9460)
 
### 本次更新
 
* 支持 sing-box v1.14，更新的用户注意内核版本 #9736
* 锁定最大 sing-box 版本 v1.14  #10091
* 添加通过代理更新检查更新的选项 - #10090
* 在核心设置界面中添加 Mux 设置 - #10055
* 日志和临时文件自动清理时间默认为 7 天
* 调整 Clash API - #10088
* xray core 配置文件格式改为最新版本 #10132
* 为订阅更新添加自定义 HTTP 标头 - #10118
* 添加阿塞拜疆语 (az) UI 本地化 - #10141
* 添加 MASQUE 支持 - #10233
* https://github.com/XTLS/Xray-core/releases/tag/v26.10.10


### [发布文件介绍，不知道下载哪个文件的请看](https://github.com/2dust/v2rayN/wiki/Release-files-introduction)
```
</details>

---

## <span id="-系统与开发者工具">🛠️ 系统与开发者工具</span>

### 📦 [openwrt/openwrt](https://github.com/openwrt/openwrt)
`⭐ Stars: 29,015` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [v25.12.6](https://github.com/openwrt/openwrt/releases/tag/v25.12.6) (2026-10-18)`

> **简介**：该存储库是 https://git.openwrt.org/openwrt/openwrt.git 的镜像，仅供参考，不可签入。  我们将继续在这里接受 Pull 请求。它们将通过暂存树合并到 openwrt.git 中。

**💡 核心亮点更新 (中文)**：
* https://firmware-selector.openwrt.org/?version=25.12.6
* https://downloads.openwrt.org/releases/25.12.6/targets/
* **uhttpd（Web 服务器，默认情况下使用 LuCI 启用）：** uhttpd 已更新到更新版本，修复了五个已发布的建议，所有这些都无需身份验证即可访问：

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Hi,

The OpenWrt community is proud to announce the sixth service release of the OpenWrt 25.12 stable series.

Download firmware images using the OpenWrt Firmware Selector:
  * https://firmware-selector.openwrt.org/?version=25.12.6

Download firmware images directly from our download servers:
  * https://downloads.openwrt.org/releases/25.12.6/targets/


Main changes between OpenWrt 25.12.5 and OpenWrt 25.12.6
=========================================================

Only the main changes are listed below. See the [full changelog](https://openwrt.org/releases/25.12/changelog-25.12.6) for details.


Security fixes
==============

This release fixes several remotely triggerable vulnerabilities in core network
services that are enabled by default. Updating is strongly recommended.

  * **uhttpd (web server, enabled by default with LuCI):** uhttpd was updated to a newer version that fixes five published advisories, all reachable without authentication:
    * **CVE-2026-102338** (High): memory-exhaustion denial of service caused by an unlimited number of HTTP request headers. https://github.com/openwrt/uhttpd/security/advisories/GHSA-vhx4-3p5q-m59q
    * **No CVE assigned** (High): out-of-bounds write caused by a type confusion of the `params` field in `POST /ubus/call/` requests. https://github.com/openwrt/uhttpd/security/advisories/GHSA-2mpg-6wp5-435p
    * **No CVE assigned** (High): unlimited memory growth, because the URL path was leaked on every non
```
</details>

---
### 📦 [ventoy/Ventoy](https://github.com/ventoy/Ventoy)
`⭐ Stars: 80,537` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.1.18](https://github.com/ventoy/Ventoy/releases/tag/v1.1.18) (2026-10-09)`

> **简介**：A new bootable USB solution.

**💡 核心亮点更新 (中文)**：
**Changelog**
1. Experimental support for SteamOS recovery images. (3712 2875 1815)
2. Improve the Linux remount feature to make the ISO partition mountable out of the box on mainstream desktop distros. ([Notes](https://www.ventoy.net/en/doc_linux_

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
**Changelog**
1. Experimental support for SteamOS recovery images. (#3712 #2875 #1815)
2. Improve the Linux remount feature to make the ISO partition mountable out of the box on mainstream desktop distros. ([Notes](https://www.ventoy.net/en/doc_linux_remount.html))
3. Suppress the duplicate disk icons in the sidebar on some Linux desktop distros.
4. Change the ISO partition dm name to stable /dev/mapper/VentoyPart, please refer [Notes](https://www.ventoy.net/en/doc_linux_remount.html)
5. Make the ISO partition mountable for CloneZilla. (#3274)
6. Fix Fedora 45 beta boot issue.
7. Fix the Windows/WinPE secure boot version check failed issue.
8. Fix Persistence intermittently fails on Ubuntu desktop. (#3718)
9. Fix the boot issue for Grml 2026.09. (#3751)
10. Add support for custom Syslinux-based ISO. (#3760)
11. Improvement for latest LinuxConsole release. (#3745)
12. Add check for Boot Conf Replace entries in VentoyPlugson. (#3727 #3593)
       

**SHA256**
```
d86ff9de63d94c8b8f1f6b14d23c55af4b88e8207bf2893890892a6a97b1ad54  ventoy-1.1.18-linux.tar.gz
ee3917bd5a9973c0b2f8f3ef85048bf68ae089ec88f5561ad78b6ad308b51ab5  ventoy-1.1.18-livecd.iso
082c478e8c432e1ac653899fcf50e3a4077a2851bc6112b5ddd30545962164a9  ventoy-1.1.18-windows.zip
```

<br><br><br><br>
------------------------------------------------------------------------------------------------------------------------
Wana boot and install OS through network (PXE/HTTPBoot)? Welcome to my new projec
```
</details>

---

## 🛑 建议清理 / 放弃维护项目

<details>
<summary>⚠️ 点击展开已放弃维护或超过 1 年停更的仓库清单 (136 个)</summary>

| 仓库名称 | Stars | 状态说明 | 操作建议 |
| :--- | :---: | :--- | :---: |
| [cityflow-project/CityFlow](https://github.com/cityflow-project/CityFlow) | 1,030 | 超过 439 天无代码提交 | [进入取消 Star](https://github.com/cityflow-project/CityFlow) |
| [facebookresearch/demucs](https://github.com/facebookresearch/demucs) | 10,401 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/facebookresearch/demucs) |
| [fufankeji/DeepSeek-OCR-Web](https://github.com/fufankeji/DeepSeek-OCR-Web) | 568 | 超过 370 天无代码提交 | [进入取消 Star](https://github.com/fufankeji/DeepSeek-OCR-Web) |
| [JimmyLv/awesome-nano-banana](https://github.com/JimmyLv/awesome-nano-banana) | 8,801 | 超过 419 天无代码提交 | [进入取消 Star](https://github.com/JimmyLv/awesome-nano-banana) |
| [btjawa/BiliTools](https://github.com/btjawa/BiliTools) | 5,026 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/btjawa/BiliTools) |
| [ehang-io/nps](https://github.com/ehang-io/nps) | 34,261 | 超过 886 天无代码提交 | [进入取消 Star](https://github.com/ehang-io/nps) |
| [ReturnFI/Blitz](https://github.com/ReturnFI/Blitz) | 1,089 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/ReturnFI/Blitz) |
| [kkangert/kspider](https://github.com/kkangert/kspider) | 1,264 | 超过 805 天无代码提交 | [进入取消 Star](https://github.com/kkangert/kspider) |
| [xenova/whisper-web](https://github.com/xenova/whisper-web) | 3,344 | 超过 761 天无代码提交 | [进入取消 Star](https://github.com/xenova/whisper-web) |
| [shadowsocks/luci-app-shadowsocks](https://github.com/shadowsocks/luci-app-shadowsocks) | 1,150 | 超过 1253 天无代码提交 | [进入取消 Star](https://github.com/shadowsocks/luci-app-shadowsocks) |
| [sinaptik-ai/pandas-ai](https://github.com/sinaptik-ai/pandas-ai) | 23,927 | 超过 369 天无代码提交 | [进入取消 Star](https://github.com/sinaptik-ai/pandas-ai) |
| [adithya-s-k/marker-api](https://github.com/adithya-s-k/marker-api) | 983 | 超过 747 天无代码提交 | [进入取消 Star](https://github.com/adithya-s-k/marker-api) |
| [yuchannslv5/warpflare](https://github.com/yuchannslv5/warpflare) | 334 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/yuchannslv5/warpflare) |
| [vvbbnn00/WARP-Clash-API](https://github.com/vvbbnn00/WARP-Clash-API) | 8,811 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/vvbbnn00/WARP-Clash-API) |
| [ca110us/epeius](https://github.com/ca110us/epeius) | 1,222 | 超过 805 天无代码提交 | [进入取消 Star](https://github.com/ca110us/epeius) |
| [chika0801/hysteria-install](https://github.com/chika0801/hysteria-install) | 177 | 超过 850 天无代码提交 | [进入取消 Star](https://github.com/chika0801/hysteria-install) |
| [yeahwu/InstallOS](https://github.com/yeahwu/InstallOS) | 86 | 超过 1607 天无代码提交 | [进入取消 Star](https://github.com/yeahwu/InstallOS) |
| [bulianglin/psub](https://github.com/bulianglin/psub) | 1,760 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/bulianglin/psub) |
| [lizongying/my-tv](https://github.com/lizongying/my-tv) | 31,966 | 超过 865 天无代码提交 | [进入取消 Star](https://github.com/lizongying/my-tv) |
| [joevess/IPTV](https://github.com/joevess/IPTV) | 10,278 | 超过 670 天无代码提交 | [进入取消 Star](https://github.com/joevess/IPTV) |
| [lecepin/WeChatVideoDownloader](https://github.com/lecepin/WeChatVideoDownloader) | 4,665 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/lecepin/WeChatVideoDownloader) |
| [linexjlin/GPTs](https://github.com/linexjlin/GPTs) | 32,028 | 超过 766 天无代码提交 | [进入取消 Star](https://github.com/linexjlin/GPTs) |
| [lxfater/Awesome-GPTs](https://github.com/lxfater/Awesome-GPTs) | 1,154 | 超过 1076 天无代码提交 | [进入取消 Star](https://github.com/lxfater/Awesome-GPTs) |
| [ClashDotNetFramework/experimental-clash](https://github.com/ClashDotNetFramework/experimental-clash) | 241 | 超过 1791 天无代码提交 | [进入取消 Star](https://github.com/ClashDotNetFramework/experimental-clash) |
| [zzzgydi/clash-verge](https://github.com/zzzgydi/clash-verge) | 21,865 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/zzzgydi/clash-verge) |
| [ddgth/cf2dns](https://github.com/ddgth/cf2dns) | 5,216 | 超过 665 天无代码提交 | [进入取消 Star](https://github.com/ddgth/cf2dns) |
| [zizifn/edgetunnel](https://github.com/zizifn/edgetunnel) | 9,304 | 超过 704 天无代码提交 | [进入取消 Star](https://github.com/zizifn/edgetunnel) |
| [missuo/Hysteria2](https://github.com/missuo/Hysteria2) | 204 | 超过 795 天无代码提交 | [进入取消 Star](https://github.com/missuo/Hysteria2) |
| [Misaka-blog/hysteria-install](https://github.com/Misaka-blog/hysteria-install) | 629 | 超过 927 天无代码提交 | [进入取消 Star](https://github.com/Misaka-blog/hysteria-install) |
| [MatsuriDayo/nekoray](https://github.com/MatsuriDayo/nekoray) | 15,262 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/MatsuriDayo/nekoray) |
| [FranzKafkaYu/x-ui](https://github.com/FranzKafkaYu/x-ui) | 8,449 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/FranzKafkaYu/x-ui) |
| [rwv/chinese-dos-games](https://github.com/rwv/chinese-dos-games) | 10,350 | 超过 816 天无代码提交 | [进入取消 Star](https://github.com/rwv/chinese-dos-games) |
| [getumbrel/llama-gpt](https://github.com/getumbrel/llama-gpt) | 10,924 | 超过 922 天无代码提交 | [进入取消 Star](https://github.com/getumbrel/llama-gpt) |
| [WangWenBin2017/OpenWrt-SSRPLUS](https://github.com/WangWenBin2017/OpenWrt-SSRPLUS) | 560 | 超过 609 天无代码提交 | [进入取消 Star](https://github.com/WangWenBin2017/OpenWrt-SSRPLUS) |
| [prompt-engineering/click-prompt](https://github.com/prompt-engineering/click-prompt) | 2,389 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/prompt-engineering/click-prompt) |
| [AutodeskAILab/Building-GAN](https://github.com/AutodeskAILab/Building-GAN) | 101 | 超过 1612 天无代码提交 | [进入取消 Star](https://github.com/AutodeskAILab/Building-GAN) |
| [novicezk/midjourney-proxy](https://github.com/novicezk/midjourney-proxy) | 5,373 | 超过 455 天无代码提交 | [进入取消 Star](https://github.com/novicezk/midjourney-proxy) |
| [adams549659584/go-proxy-bingai](https://github.com/adams549659584/go-proxy-bingai) | 8,404 | 超过 957 天无代码提交 | [进入取消 Star](https://github.com/adams549659584/go-proxy-bingai) |
| [tryptech/obs-zoom-and-follow](https://github.com/tryptech/obs-zoom-and-follow) | 440 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/tryptech/obs-zoom-and-follow) |
| [XingangPan/DragGAN](https://github.com/XingangPan/DragGAN) | 35,712 | 超过 897 天无代码提交 | [进入取消 Star](https://github.com/XingangPan/DragGAN) |
| [lewangdev/faster-whisper-youtube](https://github.com/lewangdev/faster-whisper-youtube) | 558 | 超过 1170 天无代码提交 | [进入取消 Star](https://github.com/lewangdev/faster-whisper-youtube) |
| [artidoro/qlora](https://github.com/artidoro/qlora) | 11,064 | 超过 874 天无代码提交 | [进入取消 Star](https://github.com/artidoro/qlora) |
| [langgenius/webapp-conversation](https://github.com/langgenius/webapp-conversation) | 1,102 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/langgenius/webapp-conversation) |
| [3andne/restls](https://github.com/3andne/restls) | 377 | 超过 1092 天无代码提交 | [进入取消 Star](https://github.com/3andne/restls) |
| [jtsang4/claude-to-chatgpt](https://github.com/jtsang4/claude-to-chatgpt) | 1,300 | 超过 805 天无代码提交 | [进入取消 Star](https://github.com/jtsang4/claude-to-chatgpt) |
| [yorunning/clash-conf](https://github.com/yorunning/clash-conf) | 102 | 超过 838 天无代码提交 | [进入取消 Star](https://github.com/yorunning/clash-conf) |
| [svc-develop-team/so-vits-svc](https://github.com/svc-develop-team/so-vits-svc) | 28,068 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/svc-develop-team/so-vits-svc) |
| [xiaye13579/BBLL](https://github.com/xiaye13579/BBLL) | 17,514 | 超过 612 天无代码提交 | [进入取消 Star](https://github.com/xiaye13579/BBLL) |
| [camenduru/MiniGPT-4-colab](https://github.com/camenduru/MiniGPT-4-colab) | 119 | 超过 1190 天无代码提交 | [进入取消 Star](https://github.com/camenduru/MiniGPT-4-colab) |
| [Vision-CAIR/MiniGPT-4](https://github.com/Vision-CAIR/MiniGPT-4) | 25,577 | 超过 790 天无代码提交 | [进入取消 Star](https://github.com/Vision-CAIR/MiniGPT-4) |
| [imfuxiao/Hamster](https://github.com/imfuxiao/Hamster) | 1,641 | 超过 537 天无代码提交 | [进入取消 Star](https://github.com/imfuxiao/Hamster) |
| [acheong08/ChatGPT](https://github.com/acheong08/ChatGPT) | 27,991 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/acheong08/ChatGPT) |
| [microsoft/JARVIS](https://github.com/microsoft/JARVIS) | 25,544 | 超过 460 天无代码提交 | [进入取消 Star](https://github.com/microsoft/JARVIS) |
| [choephix/auto-gpt-webui](https://github.com/choephix/auto-gpt-webui) | 116 | 超过 958 天无代码提交 | [进入取消 Star](https://github.com/choephix/auto-gpt-webui) |
| [facebookresearch/segment-anything](https://github.com/facebookresearch/segment-anything) | 55,090 | 超过 774 天无代码提交 | [进入取消 Star](https://github.com/facebookresearch/segment-anything) |
| [zai-org/ChatGLM-6B](https://github.com/zai-org/ChatGLM-6B) | 40,891 | 超过 858 天无代码提交 | [进入取消 Star](https://github.com/zai-org/ChatGLM-6B) |
| [ihciah/shadow-tls](https://github.com/ihciah/shadow-tls) | 2,681 | 超过 555 天无代码提交 | [进入取消 Star](https://github.com/ihciah/shadow-tls) |
| [jxbbb/ADAPT](https://github.com/jxbbb/ADAPT) | 421 | 超过 873 天无代码提交 | [进入取消 Star](https://github.com/jxbbb/ADAPT) |
| [mayooear/ai-pdf-chatbot-langchain](https://github.com/mayooear/ai-pdf-chatbot-langchain) | 16,585 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/mayooear/ai-pdf-chatbot-langchain) |
| [lencx/ChatGPT](https://github.com/lencx/ChatGPT) | 54,664 | 超过 794 天无代码提交 | [进入取消 Star](https://github.com/lencx/ChatGPT) |
| [nekohasekai/SagerNet](https://github.com/nekohasekai/SagerNet) | 56 | 超过 1757 天无代码提交 | [进入取消 Star](https://github.com/nekohasekai/SagerNet) |
| [P3TERX/Actions-OpenWrt](https://github.com/P3TERX/Actions-OpenWrt) | 7,623 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/P3TERX/Actions-OpenWrt) |
| [R86S/R86S-QuickInstaller](https://github.com/R86S/R86S-QuickInstaller) | 64 | 超过 1178 天无代码提交 | [进入取消 Star](https://github.com/R86S/R86S-QuickInstaller) |
| [WeNeedHome/SummaryOfLoanSuspension](https://github.com/WeNeedHome/SummaryOfLoanSuspension) | 20,332 | 超过 842 天无代码提交 | [进入取消 Star](https://github.com/WeNeedHome/SummaryOfLoanSuspension) |
| [zanzhz1101/LingMaxDNS](https://github.com/zanzhz1101/LingMaxDNS) | 23 | 超过 1573 天无代码提交 | [进入取消 Star](https://github.com/zanzhz1101/LingMaxDNS) |
| [IrineSistiana/mosdns-cn](https://github.com/IrineSistiana/mosdns-cn) | 325 | 超过 1614 天无代码提交 | [进入取消 Star](https://github.com/IrineSistiana/mosdns-cn) |
| [chika0801/Xray-install](https://github.com/chika0801/Xray-install) | 273 | 超过 1066 天无代码提交 | [进入取消 Star](https://github.com/chika0801/Xray-install) |
| [scutan90/DeepLearning-500-questions](https://github.com/scutan90/DeepLearning-500-questions) | 57,700 | 超过 858 天无代码提交 | [进入取消 Star](https://github.com/scutan90/DeepLearning-500-questions) |
| [Chikage0o0/Linux-NetSpeed](https://github.com/Chikage0o0/Linux-NetSpeed) | 3,742 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/Chikage0o0/Linux-NetSpeed) |
| [KFERMercer/OpenWrt-CI](https://github.com/KFERMercer/OpenWrt-CI) | 1,410 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/KFERMercer/OpenWrt-CI) |
| [qTox/qTox](https://github.com/qTox/qTox) | 4,971 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/qTox/qTox) |
| [quericy/one-key-ikev2-vpn](https://github.com/quericy/one-key-ikev2-vpn) | 2,105 | 超过 2177 天无代码提交 | [进入取消 Star](https://github.com/quericy/one-key-ikev2-vpn) |
| [riverscn/openwrt-iptvhelper](https://github.com/riverscn/openwrt-iptvhelper) | 371 | 超过 1893 天无代码提交 | [进入取消 Star](https://github.com/riverscn/openwrt-iptvhelper) |
| [frainzy1477/luci-app-clash](https://github.com/frainzy1477/luci-app-clash) | 1,622 | 超过 1683 天无代码提交 | [进入取消 Star](https://github.com/frainzy1477/luci-app-clash) |
| [Sanster/IOPaint](https://github.com/Sanster/IOPaint) | 23,298 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/Sanster/IOPaint) |
| [LANDrop/LANDrop](https://github.com/LANDrop/LANDrop) | 5,997 | 超过 810 天无代码提交 | [进入取消 Star](https://github.com/LANDrop/LANDrop) |
| [saveweb/review-2021](https://github.com/saveweb/review-2021) | 758 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/saveweb/review-2021) |
| [iranee/qnap-aliyunpan-webdav](https://github.com/iranee/qnap-aliyunpan-webdav) | 274 | 超过 1485 天无代码提交 | [进入取消 Star](https://github.com/iranee/qnap-aliyunpan-webdav) |
| [haoel/haoel.github.io](https://github.com/haoel/haoel.github.io) | 13,077 | 超过 1270 天无代码提交 | [进入取消 Star](https://github.com/haoel/haoel.github.io) |
| [tindy2013/stairspeedtest-reborn](https://github.com/tindy2013/stairspeedtest-reborn) | 3,832 | 超过 1242 天无代码提交 | [进入取消 Star](https://github.com/tindy2013/stairspeedtest-reborn) |
| [P3TERX/warp.sh](https://github.com/P3TERX/warp.sh) | 3,926 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/P3TERX/warp.sh) |
| [TheMRLL/WinXray](https://github.com/TheMRLL/WinXray) | 2,790 | 超过 979 天无代码提交 | [进入取消 Star](https://github.com/TheMRLL/WinXray) |
| [Mikubill/cowtransfer-uploader](https://github.com/Mikubill/cowtransfer-uploader) | 447 | 超过 1726 天无代码提交 | [进入取消 Star](https://github.com/Mikubill/cowtransfer-uploader) |
| [281677160/build-actions](https://github.com/281677160/build-actions) | 388 | 超过 461 天无代码提交 | [进入取消 Star](https://github.com/281677160/build-actions) |
| [vaxilu/x-ui](https://github.com/vaxilu/x-ui) | 19,097 | 超过 804 天无代码提交 | [进入取消 Star](https://github.com/vaxilu/x-ui) |
| [xinntao/Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) | 37,314 | 超过 817 天无代码提交 | [进入取消 Star](https://github.com/xinntao/Real-ESRGAN) |
| [zu1k/proxypool](https://github.com/zu1k/proxypool) | 4,039 | 超过 1301 天无代码提交 | [进入取消 Star](https://github.com/zu1k/proxypool) |
| [TachibanaYoshino/AnimeGAN](https://github.com/TachibanaYoshino/AnimeGAN) | 4,612 | 超过 1551 天无代码提交 | [进入取消 Star](https://github.com/TachibanaYoshino/AnimeGAN) |
| [yuanzhoulvpi2017/tiny_python](https://github.com/yuanzhoulvpi2017/tiny_python) | 173 | 超过 1365 天无代码提交 | [进入取消 Star](https://github.com/yuanzhoulvpi2017/tiny_python) |
| [haiibo/OpenWrt](https://github.com/haiibo/OpenWrt) | 3,161 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/haiibo/OpenWrt) |
| [VergilGao/openwrt-packages](https://github.com/VergilGao/openwrt-packages) | 11 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/VergilGao/openwrt-packages) |
| [VergilGao/openwrt-compiler](https://github.com/VergilGao/openwrt-compiler) | 13 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/VergilGao/openwrt-compiler) |
| [OpenELEC/OpenELEC.tv](https://github.com/OpenELEC/OpenELEC.tv) | 1,620 | 超过 3347 天无代码提交 | [进入取消 Star](https://github.com/OpenELEC/OpenELEC.tv) |
| [github/copilot-docs](https://github.com/github/copilot-docs) | 23,168 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/github/copilot-docs) |
| [Kiougar/luci-wrtbwmon](https://github.com/Kiougar/luci-wrtbwmon) | 356 | 超过 1865 天无代码提交 | [进入取消 Star](https://github.com/Kiougar/luci-wrtbwmon) |
| [EtherDream/jsproxy](https://github.com/EtherDream/jsproxy) | 9,317 | 超过 945 天无代码提交 | [进入取消 Star](https://github.com/EtherDream/jsproxy) |
| [cheat-engine/cheat-engine](https://github.com/cheat-engine/cheat-engine) | 19,429 | 超过 562 天无代码提交 | [进入取消 Star](https://github.com/cheat-engine/cheat-engine) |
| [ffffffff0x/Dork-Admin](https://github.com/ffffffff0x/Dork-Admin) | 1,914 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/ffffffff0x/Dork-Admin) |
| [ffffffff0x/Digital-Privacy](https://github.com/ffffffff0x/Digital-Privacy) | 4,936 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/ffffffff0x/Digital-Privacy) |
| [Autodesk/civilconnection](https://github.com/Autodesk/civilconnection) | 118 | 超过 1431 天无代码提交 | [进入取消 Star](https://github.com/Autodesk/civilconnection) |
| [0xHJK/CleanApps](https://github.com/0xHJK/CleanApps) | 165 | 超过 1897 天无代码提交 | [进入取消 Star](https://github.com/0xHJK/CleanApps) |
| [KANIKIG/Multi-EasyGost](https://github.com/KANIKIG/Multi-EasyGost) | 1,945 | 超过 945 天无代码提交 | [进入取消 Star](https://github.com/KANIKIG/Multi-EasyGost) |
| [Kurokosama/AutoBuild-OpenWRT](https://github.com/Kurokosama/AutoBuild-OpenWRT) | 88 | 超过 1584 天无代码提交 | [进入取消 Star](https://github.com/Kurokosama/AutoBuild-OpenWRT) |
| [differentrain/DeletionTool](https://github.com/differentrain/DeletionTool) | 94 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/differentrain/DeletionTool) |
| [hideuvpn/android-google-play-store](https://github.com/hideuvpn/android-google-play-store) | 3,660 | 超过 1566 天无代码提交 | [进入取消 Star](https://github.com/hideuvpn/android-google-play-store) |
| [XJP-GIT/AntiZhaPian](https://github.com/XJP-GIT/AntiZhaPian) | 3,160 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/XJP-GIT/AntiZhaPian) |
| [jerrykuku/luci-app-ttnode](https://github.com/jerrykuku/luci-app-ttnode) | 89 | 超过 1742 天无代码提交 | [进入取消 Star](https://github.com/jerrykuku/luci-app-ttnode) |
| [KevinSHIT/NaiveSharp](https://github.com/KevinSHIT/NaiveSharp) | 97 | 超过 2187 天无代码提交 | [进入取消 Star](https://github.com/KevinSHIT/NaiveSharp) |
| [prasmussen/gdrive](https://github.com/prasmussen/gdrive) | 8,942 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/prasmussen/gdrive) |
| [tostercx/GTAO_Booster_PoC](https://github.com/tostercx/GTAO_Booster_PoC) | 2,862 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/tostercx/GTAO_Booster_PoC) |
| [ilxp/luci-app-ikoolproxy](https://github.com/ilxp/luci-app-ikoolproxy) | 507 | 超过 597 天无代码提交 | [进入取消 Star](https://github.com/ilxp/luci-app-ikoolproxy) |
| [kiddin9/luci-app-dnsfilter](https://github.com/kiddin9/luci-app-dnsfilter) | 123 | 超过 630 天无代码提交 | [进入取消 Star](https://github.com/kiddin9/luci-app-dnsfilter) |
| [h31105/deployX.sh](https://github.com/h31105/deployX.sh) | 416 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/h31105/deployX.sh) |
| [jerrykuku/openwrt-package](https://github.com/jerrykuku/openwrt-package) | 147 | 超过 1094 天无代码提交 | [进入取消 Star](https://github.com/jerrykuku/openwrt-package) |
| [frainzy1477/luci-app-trojan](https://github.com/frainzy1477/luci-app-trojan) | 120 | 超过 2001 天无代码提交 | [进入取消 Star](https://github.com/frainzy1477/luci-app-trojan) |
| [atrandys/xray](https://github.com/atrandys/xray) | 89 | 超过 1709 天无代码提交 | [进入取消 Star](https://github.com/atrandys/xray) |
| [v2board/v2board](https://github.com/v2board/v2board) | 5,071 | 超过 958 天无代码提交 | [进入取消 Star](https://github.com/v2board/v2board) |
| [ShadowsocksR-Live/iShadowsocksR](https://github.com/ShadowsocksR-Live/iShadowsocksR) | 601 | 超过 916 天无代码提交 | [进入取消 Star](https://github.com/ShadowsocksR-Live/iShadowsocksR) |
| [SuperNG6/Aria2-Trackers](https://github.com/SuperNG6/Aria2-Trackers) | 309 | 超过 2108 天无代码提交 | [进入取消 Star](https://github.com/SuperNG6/Aria2-Trackers) |
| [kakaruoterl/vless_install](https://github.com/kakaruoterl/vless_install) | 29 | 超过 2265 天无代码提交 | [进入取消 Star](https://github.com/kakaruoterl/vless_install) |
| [stupidloud/nanopi-openwrt](https://github.com/stupidloud/nanopi-openwrt) | 5,514 | 超过 929 天无代码提交 | [进入取消 Star](https://github.com/stupidloud/nanopi-openwrt) |
| [atrandys/trojan](https://github.com/atrandys/trojan) | 1,055 | 超过 1298 天无代码提交 | [进入取消 Star](https://github.com/atrandys/trojan) |
| [programthink/zhao](https://github.com/programthink/zhao) | 14,151 | 超过 1918 天无代码提交 | [进入取消 Star](https://github.com/programthink/zhao) |
| [RPRX/v2ray-vless](https://github.com/RPRX/v2ray-vless) | 390 | 超过 1344 天无代码提交 | [进入取消 Star](https://github.com/RPRX/v2ray-vless) |
| [h2y/Shadowrocket-ADBlock-Rules](https://github.com/h2y/Shadowrocket-ADBlock-Rules) | 16,728 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/h2y/Shadowrocket-ADBlock-Rules) |
| [p4gefau1t/trojan-go](https://github.com/p4gefau1t/trojan-go) | 8,385 | 超过 840 天无代码提交 | [进入取消 Star](https://github.com/p4gefau1t/trojan-go) |
| [Jrohy/trojan](https://github.com/Jrohy/trojan) | 5,633 | 超过 931 天无代码提交 | [进入取消 Star](https://github.com/Jrohy/trojan) |
| [mellow-io/mellow](https://github.com/mellow-io/mellow) | 3,535 | 超过 1422 天无代码提交 | [进入取消 Star](https://github.com/mellow-io/mellow) |
| [Dawneng/luci-theme-atmaterial](https://github.com/Dawneng/luci-theme-atmaterial) | 11 | 超过 1474 天无代码提交 | [进入取消 Star](https://github.com/Dawneng/luci-theme-atmaterial) |
| [trojan-gfw/igniter](https://github.com/trojan-gfw/igniter) | 3,273 | 超过 1071 天无代码提交 | [进入取消 Star](https://github.com/trojan-gfw/igniter) |
| [openwrt-develop/luci-theme-atmaterial](https://github.com/openwrt-develop/luci-theme-atmaterial) | 68 | 超过 2419 天无代码提交 | [进入取消 Star](https://github.com/openwrt-develop/luci-theme-atmaterial) |
| [trojan-gfw/trojan-quickstart](https://github.com/trojan-gfw/trojan-quickstart) | 244 | 超过 2020 天无代码提交 | [进入取消 Star](https://github.com/trojan-gfw/trojan-quickstart) |
| [FunctionClub/ZBench](https://github.com/FunctionClub/ZBench) | 1,175 | 超过 2051 天无代码提交 | [进入取消 Star](https://github.com/FunctionClub/ZBench) |
| [veekxt/v2ray-template](https://github.com/veekxt/v2ray-template) | 749 | 超过 2263 天无代码提交 | [进入取消 Star](https://github.com/veekxt/v2ray-template) |
| [HMBSbige/ShadowsocksR-Windows](https://github.com/HMBSbige/ShadowsocksR-Windows) | 6,906 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/HMBSbige/ShadowsocksR-Windows) |
| [trojan-gfw/trojan](https://github.com/trojan-gfw/trojan) | 19,744 | 超过 802 天无代码提交 | [进入取消 Star](https://github.com/trojan-gfw/trojan) |
</details>
