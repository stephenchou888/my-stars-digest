# 📡 Starred 项目雷达看板
> 🖥️ **交互式管理看板 (shadcn/ui)**：[👉 点击进入在线雷达看板 (https://stephenchou888.github.io/my-stars-digest/)](https://stephenchou888.github.io/my-stars-digest/)

> **生成时间**：`2026-11-17` ｜ **关注项目总数**：`432` ｜ **本期更新**：`114` ｜ **弃坑预警**：`138`

| 统计指标 | 数量 | 状态提示 |
| :--- | :---: | :--- |
| 🌟 总关注库 | **432** | [进入 shadcn 在线看板管理](https://stephenchou888.github.io/my-stars-digest/) |
| 🚀 近期有更新 | **114** | 涵盖 6 个分类 |
| 🛑 建议清理/弃坑 | **138** | 建议取消 Star 保持关注列表整洁 |

---
## 🧭 领域分类速览导航

- [🤖 AI 与智能体生态 (65)](#-AI-与智能体生态)
- [📝 效率办公与创作 (14)](#-效率办公与创作)
- [🛠️ 系统与开发者工具 (5)](#-系统与开发者工具)
- [📦 实用开源精选 (6)](#-实用开源精选)
- [🎬 影音媒体与下载 (14)](#-影音媒体与下载)
- [🌐 网络与代理技术 (10)](#-网络与代理技术)

---

## <span id="-AI-与智能体生态">🤖 AI 与智能体生态</span>

### 📦 [open-webui/open-webui](https://github.com/open-webui/open-webui)
`⭐ Stars: 158,904` &nbsp;|&nbsp; `💻 语言: Svelte` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.13.3](https://github.com/open-webui/open-webui/releases/tag/v0.13.3) (2026-11-08)`

> **简介**：用户友好的 AI 界面（支持 Ollama、OpenAI API...）

**💡 核心亮点更新 (中文)**：
- 🦾 **自动化中的代理。** 自动化编辑器现在允许您选择终端和工作文件夹，然后选择那里可用的编码代理。计划运行使用已保存的终端和文件夹，并在开始之前检查终端和代理是否仍然可用。代理自动化将其结果发送到聊天室；普通型号仍可使用频道目的地。 [提交](https://github.com/open-webui/open-webui/commit/21fc016141c73a0e11b428c61bde20527bbc228a)
- 📂 **在聊天期间更改终端和文件夹。** 您现在可以在发送消息后（包括在临时聊天中）选择不同的终端或工作文件夹。在生成回复时，两个控件均保持禁用状态。 [提交](https://github.com/open-webui/open-webui/commit/a518ff1630b74ed6edd62538c5da4bb26cc6dd20)
- 🇧🇷 **巴西葡萄牙语翻译。** 添加了终端和文件夹控件、Git 操作、电子表格编辑、语音注释、选项卡快捷方式、通知声音和工具设置的缺失翻译。更新了文档检索、工具权限和语音设置的说明。 [#33945](https://github.com/open-webui/open-webui/pull/33945)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
### Added

- 🦾 **Agents in automations.** The automation editor now lets you choose a terminal and working folder, then select a coding agent available there. Scheduled runs use that saved terminal and folder, and check that the terminal and agent are still available before starting. Agent automations send their results to a chat; channel destinations remain available for ordinary models. [Commit](https://github.com/open-webui/open-webui/commit/21fc016141c73a0e11b428c61bde20527bbc228a)
- 📂 **Change terminal and folder during a chat.** You can now choose a different terminal or working folder after sending messages, including in temporary chats. Both controls remain disabled while a reply is being generated. [Commit](https://github.com/open-webui/open-webui/commit/a518ff1630b74ed6edd62538c5da4bb26cc6dd20)
- 🇧🇷 **Brazilian Portuguese translations.** Added missing translations for terminal and folder controls, Git actions, spreadsheet editing, voice notes, tab shortcuts, notification sounds and tool settings. Updated the explanations for document retrieval, tool permissions and voice settings. [#33945](https://github.com/open-webui/open-webui/pull/33945)

### Fixed

- 📂 **Files tabs follow terminal changes.** Switching a chat to another terminal now updates its open Files tabs to show that terminal's files, instead of leaving the previous terminal's folders on screen. With a terminal set to "Per chat", the Files tab also switches to the chat's own files after the first message.
```
</details>

---
### 📦 [NVIDIA/SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator)
`⭐ Stars: 3,148` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.9.0](https://github.com/NVIDIA/SkillEvaluator/releases/tag/v0.9.0) (2026-11-13)`

> **简介**：用于评估 AI 代理技能和插件的多层框架，具有质量门、语义重叠检测、综合评估数据集生成以及衡量技能如何影响代理行为的实时代理评估。

**💡 核心亮点更新 (中文)**：
- **构建和审查更好的评估数据集。** 声明对脚本执行、工作区文件和最终响应的确定性检查。生成基于技能说明、作者意图或痕迹的数据集；导入生产痕迹作为经过编辑的审查候选者；并且只有在明确的人工审查之后才能提高期望。在写入新文件之前预览旧数据集迁移。
- **随着时间的推移跟踪技能改进。** 使用“--compare-to”和“compare-versions”比较保留的技能版本，浏览运行历史记录，并使用“--reuse-baseline”重用兼容的无技能基线。版本比较与针对无技能基线的技能提升保持分开。
- **控制评估支出。** 设置令牌、判断调用、尝试和定价成本预算。当限制停止运行时，报告会保留部分结果。令牌使用情况按案例和代理显示，并标识了缺失的计数器和重用基线使用情况。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# SkillEvaluator 0.9.0

SkillEvaluator 0.9.0 expands how you build evaluation datasets, compare skill versions, and understand why an agent passed or failed. It adds controls for evaluation budgets, reusable baselines, and clearer evidence across terminal, HTML, JSON, Markdown, and benchmark reports.

For PyPI users upgrading from 0.7.2, this release also includes the changes shipped in the GitHub-only 0.8.0 release.

## Highlights

- **Build and review better evaluation datasets.** Declare deterministic checks for script execution, workspace files, and final responses. Generate datasets grounded in skill instructions, author intent, or traces; import production traces as redacted review candidates; and promote expectations only after explicit human review. Preview legacy dataset migrations before writing a new file.
- **Track skill improvements over time.** Compare retained skill versions with `--compare-to` and `compare-versions`, browse run history, and reuse a compatible no-skill baseline with `--reuse-baseline`. Version comparisons remain separate from Skill Lift against a no-skill baseline.
- **Control evaluation spending.** Set token, judge-call, attempt, and priced-cost budgets. Reports retain partial results when limits stop a run. Token usage is shown per case and agent, with missing counters and reused-baseline usage identified.
- **Understand the evidence behind each result.** Reports show met, unmet, unchecked, and inapplicable expectations; dataset coverage and
```
</details>

---
### 📦 [Tencent/LoopForge](https://github.com/Tencent/LoopForge)
`⭐ Stars: 2,754` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.3.8](https://github.com/Tencent/LoopForge/releases/tag/v0.3.8) (2026-11-12)`

> **简介**：用于编码代理交付的自托管工作流程。使用脚本和人工审批门来编排 CodeBuddy、Codex 和 Claude Code。包括编码助理的本地工作流程。

**💡 核心亮点更新 (中文)**：
* 修复（deps）：通过 https://github.com/Tencent/LoopForge/pull/166 修补易受攻击的聊天机器人测试工具链
* 修复（运行时）：在 https://github.com/Tencent/LoopForge/pull/133 中存在备用路径持有者时保持 index.lock
* ci（平台）：通过 https://github.com/Tencent/LoopForge/pull/140 运行存储库绑定和第二用户 e2e API 测试

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Install

```bash
git clone --branch v0.3.8 https://github.com/Tencent/LoopForge.git
cd LoopForge
./start.sh
```

Platform image: `ghcr.io/tencent/loopforge:0.3.8` (pinned in `compose.yaml`).

Digest: `ghcr.io/tencent/loopforge@sha256:481ecb6334a21308acb93f164f5dc74f508109d3e108089981a7ea87de095963`.

Where `ghcr.io` is slow, set `MIRROR` to a registry host that replaces it (for example `MIRROR=ghcr.nju.edu.cn ./start.sh`). This trusts that host: the download is tagged as the pinned name. Check it with `docker image inspect --format '{{index .RepoDigests 0}}' ghcr.io/tencent/loopforge:0.3.8` and compare the digest after `@`. Existing installations: check out `v0.3.8`, run `./start.sh`, and apply the new files under `migrations/` listed in [CHANGELOG.md](https://github.com/Tencent/LoopForge/blob/v0.3.8/CHANGELOG.md).

## What's Changed
* fix(deps): patch vulnerable chatbot test toolchain by @hxy91819 in https://github.com/Tencent/LoopForge/pull/166
* ci: mirror the platform image to TCR after publishing GHCR by @cocofhu in https://github.com/Tencent/LoopForge/pull/205
* fix(runtime): keep index.lock while an alternate-path holder is live by @Robert0622 in https://github.com/Tencent/LoopForge/pull/133
* ci(platform): run repository-bound and second-user e2e API tests by @Robert0622 in https://github.com/Tencent/LoopForge/pull/140
* fix(chatbot): clear the missing-key notice once quick access saves a key by @Robert0622 in https://github.com/Tencent/LoopForge/pull/184
* fix(acc
```
</details>

---
### 📦 [Pabldi08/AirSend](https://github.com/Pabldi08/AirSend)
`⭐ Stars: 74` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.3.0](https://github.com/Pabldi08/AirSend/releases/tag/v0.3.0) (2026-11-13)`

> **简介**：AirSend 是一款在 Windows 中使用 Airplay2 conexion 的应用程序

**💡 核心亮点更新 (中文)**：
- 发送所有系统音频或在 Windows 11 上选择一个应用程序。
- 持续静音后释放扬声器并手动恢复。
- 停止从系统托盘播放。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# AirSend 0.3.0

AirSend for Windows now has a native WinUI interface.

- Send all system audio or choose one app on Windows 11.
- Release the speaker after sustained silence and resume manually.
- Stop playback from the system tray.
- Use a shared PTP reference for synchronized playback and inspect clock health in Diagnostics.
- Review recent audio issues and retransmissions, and mark audible distortion from any screen.
- Request a receiver buffer from 100 ms. Saved settings below that limit from earlier builds are migrated from 0 or 50 ms to 100 ms.

Quit the previous instance from the system tray, then run AirSend-0.3.0-Setup-x64.exe. Setup installs WinUI for the current Windows user and adds a Start menu shortcut. Your existing AirSend settings are preserved.


Source revision: 4b3ae3c833e1c28ac818261d79d3b78627e497bf. AirSend and the bundled AirPlay engine use GPL-3.0-or-later. License and provenance are included with the installed application.

[Installer source](https://github.com/Pabldi08/AirSend/blob/985c6ee/native/AirSend.nsi)
```
</details>

---
### 📦 [AppFlowy-IO/AppFlowy](https://github.com/AppFlowy-IO/AppFlowy)
`⭐ Stars: 79,071` &nbsp;|&nbsp; `💻 语言: Dart` &nbsp;|&nbsp; `🏷️ 最新版本: [0.15.1](https://github.com/AppFlowy-IO/AppFlowy/releases/tag/0.15.1) (2026-11-15)`

> **简介**：通过 AI 将项目、wiki 和团队结合在一起。 AppFlowy 是人工智能协作工作空间，您可以在不失去对数据控制的情况下实现更多目标。领先的开源 Notion 替代品。

**💡 核心亮点更新 (中文)**：
- **提要讨论** — 在卡片上的弹出窗口中打开评论线程，弹出窗口关闭时会保留回复和草稿。
- **数据库行操作** - 启用从列表和图库组标题创建行，添加复制链接到云和自托管工作区中的图库卡，并按分组列表顺序保留查看导航。
- **数据库历史记录** — 澄清了行计数覆盖了整个保存的数据库，并且行页内容有自己的历史记录。保留预览选项卡和名称与保存的版本相关联，不包括嵌入其他位置的链接视图。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
### 🚀 v0.15.1

#### Improvements

- **Feed discussions** — Opened comment threads in a popover on the card, with replies and drafts retained when the popover was dismissed.
- **Database row actions** — Enabled row creation from List and Gallery group headers, added Copy link to Gallery cards in cloud and self-hosted workspaces, and kept peek navigation in grouped List order.
- **Database history** — Clarified that row counts covered the whole saved database and that row-page content had its own history. Kept preview tabs and names tied to the saved version, excluding linked views embedded elsewhere.

#### Bug Fixes

- Fixed missing Gallery groups, empty-group visibility, and loading additional cards within large groups. Corrected List property alignment and gaps around empty Gallery and Feed properties.
- Preserved pending text, number, and rollup filter values when closing their editors, and prevented blank checklist tasks.
- Corrected date-only formula comparisons to use calendar days, while retaining precise comparisons when either date included a time.
- Restored reciprocal relation links when duplicating database rows.
- Preserved embedded databases and linked views in row templates opened and edited across Web and Desktop.
- Restored Person names in database history, row properties, and group headers.
- Recovered page references from outdated access denials and kept copied subpages visible after duplication completed.
- Fixed restored tabs that stayed b
```
</details>

---
### 📦 [siyuan-note/siyuan](https://github.com/siyuan-note/siyuan)
`⭐ Stars: 47,268` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.8.10](https://github.com/siyuan-note/siyuan/releases/tag/v3.8.10) (2026-11-10)`

> **简介**：An open-source, privacy-first, self-hosted knowledge workspace where humans and AI agents work together 开源、隐私优先、自托管的知识工作空间，让人与智能体在此协作

**💡 核心亮点更新 (中文)**：
概述

此版本添加了丰富的文档标题、数据库子项和相关视图、工作区级 AI 长期记忆以及内置的轻量级 Markdown 编辑器。

文档树更有效地处理大型目录，同时统一文档

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Overview

This release adds rich document titles, database sub-items and related views, workspace-level AI long-term memory, and a built-in lightweight Markdown editor.

Document trees handle large directories more efficiently, while unified document and block breadcrumbs make navigation more consistent. Other improvements include mobile bottom sheets, HTTP requests in templates, custom PDF page sizes, LAN sync address selection, and bazaar compatibility filtering.

## Changelogs

Below are the detailed changes in this version.

### Enhancement

* [Support unified document and block breadcrumbs](https://github.com/siyuan-note/siyuan/issues/3007)
* [Support rich document titles and preserve slashes in notebook names](https://github.com/siyuan-note/siyuan/issues/20837)
* [Improve document tree browsing performance and access to large directories](https://github.com/siyuan-note/siyuan/issues/20884)
* [Support breadcrumb button visibility and ordering in appearance profiles](https://github.com/siyuan-note/siyuan/issues/20916)
* [Support converting embed blocks to regular blocks or block references](https://github.com/siyuan-note/siyuan/issues/21018)
* [Support configuring an Exa API key for built-in web search](https://github.com/siyuan-note/siyuan/issues/21026)
* [Support database sub-items](https://github.com/siyuan-note/siyuan/issues/21038)
* [Support HTTP requests in templates](https://github.com/siyuan-note/siyuan/issues/21058)
* [Support workspace-lev
```
</details>

---
### 📦 [Jarvis322/macos-sysdata](https://github.com/Jarvis322/macos-sysdata)
`⭐ Stars: 2,253` &nbsp;|&nbsp; `💻 语言: Swift` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.13.1](https://github.com/Jarvis322/macos-sysdata/releases/tag/v1.13.1) (2026-11-12)`

> **简介**：查看 macOS 系统数据中到底有什么，并将其逐项删除。一个免费的菜单栏应用程序，可以解释每个类别并在运行之前显示每个命令。

**💡 核心亮点更新 (中文)**：
- **菜单栏开关在窗口中工作。** 从窗口设置中关闭“在菜单栏中显示”现在会立即删除图标，然后重新打开它会将其恢复，而不是等待重新启动。感谢（＃30）。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
- **The menu bar switch works from the window.** Turning off "Show in menu bar" from the window's settings now removes the icon straight away, and turning it back on brings it back, instead of waiting for a relaunch. Thanks to @MaiwulanjiangMaiming (#30).


## Install
```bash
brew install --cask Jarvis322/tap/sysdata
```
or open `SysDataMenu-1.13.1.dmg` and drag the app to Applications. The zip is the same app for anyone scripting the download. Signed and notarized. Requires macOS 14 or later.
```
</details>

---
### 📦 [openfilm/openfilm](https://github.com/openfilm/openfilm)
`⭐ Stars: 8,019` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.3.2](https://github.com/openfilm/openfilm/releases/tag/v0.3.2) (2026-11-09)`

> **简介**：开源人工智能视频代理：将任何编码代理变成视频代理，并使用编辑器来更改其制作的任何内容。

**💡 核心亮点更新 (中文)**：
- [#433](https://github.com/openfilm/openfilm/pull/433) [`758b1a3`](https://github.com/openfilm/openfilm/commit/758b1a3888819bf191db191f690c4ca2fcb292af) 谢谢[](https://github.com/riverisbuilding)！ - 在 Windows 上切换选项卡或通过加号按钮打开项目时，向前移动目标项目。项目菜单可以将当前编辑复制到同一组中的独立项目中。
- [#433](https://github.com/openfilm/openfilm/pull/433) [`758b1a3`](https://github.com/openfilm/openfilm/commit/758b1a3888819bf191db191f690c4ca2fcb292af) 谢谢[](https://github.com/riverisbuilding)！ - 引用 Windows 网络共享上拒绝系统链接的原始文件和文件夹。这些参考适用于预览和导出。
- [#433](https://github.com/openfilm/openfilm/pull/433) [`758b1a3`](https://github.com/openfilm/openfilm/commit/758b1a3888819bf191db191f690c4ca2fcb292af) 谢谢[](https://github.com/riverisbuilding)！ - 在编辑器外部进行更改后刷新打开的时间线，重试失败的读取，并在较旧的响应迟到时保留较新的编辑。画布和编辑保留单独的面板尺寸。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
OpenFilm 0.3.2 improves project switching on Windows, brings more of the edit across to other editors, and makes the canvas and asset library work together.

**Projects and workspace.** Open and switch project tabs more reliably on Windows. Duplicate a project from its menu, or reference media on a network share that disallows system links. The chat divider resizes the workspace and asset drawer together, and the inspector scrolls with a trackpad.

**Canvas and timeline.** Canvas writing nodes take text, image and video references. Videos rest on their opening frame, play on hover and can give you a still. Show in Assets finds the matching file and briefly highlights it. Organize compatible tracks with undo, select ranges of layers, and see mixed audio waveforms on compound clips.

**Editing-project exports.** Exports keep effects and visible subtitles automatically. Reference the original files or copy complete sources. Jianying and CapCut retain subtitle styling, and supported Jianying clip settings stay editable.

**Assets and services.** Large projects load visible thumbnails first. Library previews can be retried, and a paused viewer redraws when its images finish loading. Canvas model choices update as soon as a service connects. TBC mischief 1 and Grok Imagine Video 1.5 Lite are available with your OpenRouter key.

Check for updates in the desktop app or use the installers below. CLI users can run `npm i -g openfilm`.

Thanks to @yunloong-Y and @WEBGRS for their pull r
```
</details>

---
### 📦 [Parcha-ai/agentrun](https://github.com/Parcha-ai/agentrun)
`⭐ Stars: 1,192` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [cli-v0.1.10](https://github.com/Parcha-ai/agentrun/releases/tag/cli-v0.1.10) (2026-11-06)`

> **简介**：AgentRun 是一个开源平台，可以增强您的代理。它在您最喜欢的特工装备之上增加了自我完善、持久的执行力和控制平面。您的代理变得更加智能、容错能力更强，并且每次运行时使用的令牌更少。

**💡 核心亮点更新 (中文)**：
AgentRun 观察 CLI 0.1.10 与节点启动器 @parcha/agentrun-cli 0.1.1。

使用设备身份验证或显式配置的注册凭据将选定的 Claude Code 和 Codex 会话连接到 AgentRun 工作区。观察再

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
AgentRun observation CLI 0.1.10 with the Node launcher @parcha/agentrun-cli 0.1.1.

Connect selected Claude Code and Codex sessions to an AgentRun workspace using device authentication or an explicitly configured enrollment credential. Observation reports activity; it does not execute or control agents. Session selection, metadata consent, and login startup remain explicit choices.

## Installation

Verified platform: Linux x64 with glibc, Node.js 20 or newer. The launcher provisions Python 3.12, verifies release checksums, and installs a persistent runtime outside the npm cache. macOS, Windows, and other architectures are not supported by this launcher release.

The npm launcher is published as `@parcha/agentrun-cli@0.1.1`:

```sh
npx --yes @parcha/agentrun-cli@0.1.1 --help
```

The GitHub-hosted package also works directly:

```sh
npx --yes --package https://github.com/Parcha-ai/agentrun/releases/download/cli-v0.1.10/parcha-agentrun-cli-0.1.1.tgz agentrun --help
```

For enrollment, use `connect --device-auth --origin <your-api-origin> --workspace-id <your-workspace-id>`. Keep any selected `--state-dir` on subsequent commands. Device approval uses a browser on any device and requires no local callback server.

## Release integrity and source

`release.json` names each runtime artifact and its SHA-256. The launcher accepts only this repository's pinned CLI release URLs and one HTTPS redirect to GitHub's exact release-assets.githubusercontent.com host. Explicit preview downlo
```
</details>

---
### 📦 [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)
`⭐ Stars: 57,918` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [chrome-devtools-mcp-v1.13.0](https://github.com/ChromeDevTools/chrome-devtools-mcp/releases/tag/chrome-devtools-mcp-v1.13.0) (2026-11-11)`

> **简介**：用于编码代理的 Chrome DevTools

**💡 核心亮点更新 (中文)**：
* 添加基于 DevTools BreakpointManager 构建的日志点 ([#3211](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/3211)) ([0877ee0](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/0877ee00d2e43c1c04bba275e7d08cc1033e36e9))
* 添加页面范围的网络模拟（[#3384](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/3384)） ([1d692d3](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/1d692d31ae370105afcf4d826dc36f1c4c22e21a))
* 支持上游网络模拟响应（[#3420](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/3420)） ([c4bf342](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/c4bf342b0854620d2e41262a971e1b24b705f957))

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## [1.13.0](https://github.com/ChromeDevTools/chrome-devtools-mcp/compare/chrome-devtools-mcp-v1.12.0...chrome-devtools-mcp-v1.13.0) (2026-11-11)


### 🎉 Features

* add logpoints built on the DevTools BreakpointManager ([#3211](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/3211)) ([0877ee0](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/0877ee00d2e43c1c04bba275e7d08cc1033e36e9))
* add page-scoped network mocks ([#3384](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/3384)) ([1d692d3](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/1d692d31ae370105afcf4d826dc36f1c4c22e21a))
* support upstream network mock responses ([#3420](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/3420)) ([c4bf342](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/c4bf342b0854620d2e41262a971e1b24b705f957))


### 🛠️ Fixes

* **config:** accept config files with a UTF-8 BOM ([#3365](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/3365)) ([63170b1](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/63170b11a2fa74d5ceea757194d7b25f3e145f68))
* **console:** stop resolving a cyclic Error.cause chain after 10 causes ([#3338](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/3338)) ([172656a](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/172656ab38a4ff666f88dc9032fa841834a69495))
* disable set_logpoints when --no-javascript-evaluation is set ([#3415](https://github.com/ChromeDevTools/
```
</details>

---
### 📦 [y5ez3g/facadecode](https://github.com/y5ez3g/facadecode)
`⭐ Stars: 421` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [extension/0.1.5](https://github.com/y5ez3g/facadecode/releases/tag/extension/0.1.5) (2026-11-14)`

> **简介**：VS Code 的多代理协调器。运行 Claude Code、Codex 和其他代理 CLI，这些 CLI 可以跨窗口和计算机启动、发送消息并相互操作。

**💡 核心亮点更新 (中文)**：
- 修复了当指针离开面板时机器人眼睛不会返回中心的问题。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
- Fixed robot eyes not returning to center when the pointer leaves the panel.

---

[Build and verification](https://github.com/y5ez3g/facadecode/actions/runs/43532833424) · `942f4699` · checksums: `SHA256SUMS`.
```
</details>

---
### 📦 [GoogleChrome/modern-web-guidance](https://github.com/GoogleChrome/modern-web-guidance)
`⭐ Stars: 21,562` &nbsp;|&nbsp; `💻 语言: Other` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.0.1](https://github.com/GoogleChrome/modern-web-guidance/releases/tag/v1.0.1) (2026-11-16)`

> **简介**：让您的编码代理了解最新的网络最佳实践

**💡 核心亮点更新 (中文)**：
* 引入了新的 **[js](https://github.com/GoogleChrome/modern-web-guidance/blob/v1.0.1/skills/modern-web-guidance/guides/js/js.md) 指南，提供了在 Web 应用程序中编写干净、高效和可维护的 JavaScript 的最佳实践和现代架构模式。
* 更新了 **[modern-web-guidance](https://github.com/GoogleChrome/modern-web-guidance/blob/v1.0.1/skills/modern-web-guidance/SKILL.md)** 技能以指定英语面向操作的查询，并更新了技能版本哈希。
* 更新了 **[translator](https://github.com/GoogleChrome/modern-web-guidance/blob/v1.0.1/skills/modern-web-guidance/guides/built-in-ai/translator.md)** 指南，以强制将“lang”属性应用到容器元素，并使用匹配的 BCP 47 语言代码来翻译内容。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# Release Notes: `v1.0.1`

## 🆕 New Guides

* Introduced a new guide for **[js](https://github.com/GoogleChrome/modern-web-guidance/blob/v1.0.1/skills/modern-web-guidance/guides/js/js.md)** providing best practices and modern architectural patterns for writing clean, efficient, and maintainable JavaScript in web applications.

## 🔄 Updated Guides

* Updated the **[modern-web-guidance](https://github.com/GoogleChrome/modern-web-guidance/blob/v1.0.1/skills/modern-web-guidance/SKILL.md)** skill to specify English action-oriented queries and updated the skill version hash.
* Updated the **[translator](https://github.com/GoogleChrome/modern-web-guidance/blob/v1.0.1/skills/modern-web-guidance/guides/built-in-ai/translator.md)** guide to mandate applying the `lang` attribute to the container element with the matching BCP 47 language code for translated content.
* Updated the **[css-layout](https://github.com/GoogleChrome/modern-web-guidance/blob/v1.0.1/skills/modern-web-guidance/guides/css/css-layout.md)** guide to recommend `flip-block, flip-inline, flip-block flip-inline` as a robust default for `position-try-fallbacks` in anchor positioning.
* Updated the **[autofill-sign-up-form](https://github.com/GoogleChrome/modern-web-guidance/blob/v1.0.1/skills/modern-web-guidance/guides/forms/autofill-sign-up-form.md)** guide to correct a typo in the full name input's `name` attribute example.
* Updated the **[slider](https://github.com/GoogleChrome/modern-web-guidance/blob/v1.0.1/skills/m
```
</details>

---
### 📦 [Lee-xeo/Claude-Cage](https://github.com/Lee-xeo/Claude-Cage)
`⭐ Stars: 6,271` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.1.8](https://github.com/Lee-xeo/Claude-Cage/releases/tag/v0.1.8) (2026-11-16)`

> **简介**：Cage：为 Claude 特化的轻量化虚拟机，彻底杜绝网络泄露。多平台适配，支持多账号管理、远程部署、移动端操控。

**💡 核心亮点更新 (中文)**：
- 工作台底部时钟可在“设置 → 通用”切换 12/24 小时制，保存后立即生效，并在重新打开时保留选择。
- 降低原生环境轮询与画面传输开销，优化空闲内存回收。Windows 浏览器画面跟随查看设备的屏幕像素密度，保留清晰度和输入位置的一致性。
- 桌面应用更新支持中断续传和重试，以无数据传输的时长判断停滞。Windows 更新支持可信发布者证书续期；Linux 发现新版时提供发行页入口，仍通过系统包手动安装。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# Cage v0.1.8

这是 v0.1.8 正式版，包含 v0.1.7 之后合入主线的改动，提供 macOS、Windows、Linux 和 Android 安装包。

## 主要改动

- 工作台底部时钟可在“设置 → 通用”切换 12/24 小时制，保存后立即生效，并在重新打开时保留选择。
- 降低原生环境轮询与画面传输开销，优化空闲内存回收。Windows 浏览器画面跟随查看设备的屏幕像素密度，保留清晰度和输入位置的一致性。
- 桌面应用更新支持中断续传和重试，以无数据传输的时长判断停滞。Windows 更新支持可信发布者证书续期；Linux 发现新版时提供发行页入口，仍通过系统包手动安装。
- Android 增加设置页检查更新及下载、校验和系统安装入口。旧 APK 没有“检查更新”时，需要先从官网下载新版并覆盖安装一次。
- 完善 macOS 物理出口网卡筛选、IPv6 安全检查和浏览器硬件渲染参数。图形加速是否生效仍由系统、驱动和 Chromium 决定。
- 同步主线中的项目与账户操作、登录回跳、代理恢复、macOS 屏幕共享入口和 Windows SSH 远程环境改进。

- 通过 Agent CLI 选择单节点出口时，会清除原多跳链；选择已在链中的节点也能正常完成。需要多跳时继续使用链式代理设置。
- Linux 基础软件包安装失败时，显示失败命令、涉及的软件包及已脱敏的输出末尾，帮助区分 DNS、连接和软件源问题。该改进提供排查证据，不能保证网络或软件源故障自动恢复。
- 修复手动 Windows ISO 安装时应答文件被安装程序忽略的问题，保留磁盘、版本等手动安装选择。
- 补充 Windows 客机官方 Desktop 无法打开共享项目时的处理说明：共享项目通过终端使用，Desktop 可选择客机本地目录；该说明未增加 Desktop 的共享目录支持。

## 安装与更新

macOS 安装包面向 Apple Silicon，Windows 安装器面向 x64，Linux 提供 x86_64 DEB，Android 提供 arm64 APK。Intel Mac 的实验源码与 CI 构建已合入，当前公开安装包不包含 Intel Mac 发行物。

桌面端手动覆盖安装前，请保存工作、停止环境并退出 Cage。使用 macOS 或 Windows 应用内更新时，请保存工作后点击更新按钮；校验通过后，应用会自动停止环境、安装并重启。账户、配置、项目、登录凭据与持久磁盘保留。Windows v0.1.7 用户需先按[维护指南](https://github.com/Lee-xeo/Claude-Cage/blob/main/docs/guide/maintenance.md)使用完整安装器手动升级一次。Android 覆盖安装沿用既有签名身份；iOS 继续采用本地 Xcode 构建方式。

## 验证范围

本版本功能改动已通过 macOS、Windows 和 Linux CI。发行包的签名、macOS 公证、摘要及公开下载校验结果记录在[对应的 GitHub Release](https://github.com/Lee-xeo/Claude-Cage/releases/tag/v0.1.8)。本机已完成组合代码的 Go 全量与竞态测试、前端单测和构建、实际 Chromium 画面与密度测试、时钟交互、隔离 CLI、macOS 更新回滚及安装/重装/卸载数据保留测试。

本次发布未完成全部原生界面的实机验收。托管 CI、容器
```
</details>

---
### 📦 [duyunzhoudyz/dyz-gongwen-skills](https://github.com/duyunzhoudyz/dyz-gongwen-skills)
`⭐ Stars: 890` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.1.0](https://github.com/duyunzhoudyz/dyz-gongwen-skills/releases/tag/v1.1.0) (2026-11-04)`

> **简介**：公文写作 Skills｜AI 公文写作助手：防编造、守保密、GB/T 9704 一键排版，覆盖 22 种文书，支持 Claude Code / Codex / Cursor

**💡 核心亮点更新 (中文)**：
- 仓库与套件更名为 dyz-gongwen-skills，旧地址 GitHub 会自动跳转。已经安装过的用户需重新执行 `/plugin marketplace add duyunzhoudyz/dyz-gongwen-skills`。22 个 skill 自己的名称（gongwen、gongwen-draft 等）不变。
- **内容补齐**：核验日期统一；各包 `calendar.md` 扩充；模板补正误对照；5 个包 `evals` 新增 27 条用例，共 116 条；配有机检脚本的包补必错、必过标本测试。
- **soe 边界修复**：国企包与其他行业包、核心 skill 的转交边界，用例 17 的转交目标由 gongwen-university 改为 gongwen-minutes；复核中发现的编造倾向已补规则。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# dyz-gongwen-skills v1.1.0

> **保密提示**
>
> 涉密信息严禁输入任何联网 AI 工具。带密级标识、标注“内部资料”“工作秘密”的材料，不要粘贴到任何公网大模型。处理内部材料请用单位内网部署的模型，本项目的提示词版和离线包可以直接在内网模型上使用。完整说明见 [使用须知](https://github.com/duyunzhoudyz/dyz-gongwen-skills/blob/main/使用须知.md)。

> **更名通知**
>
> 仓库与套件已更名为 **dyz-gongwen-skills**（原 gongwen-skills），旧地址 GitHub 会自动跳转。22 个 skill 自己的名称（`gongwen`、`gongwen-draft` 等）不变。
>
> **已经安装过的 Claude Code 用户需要重新执行：**
>
> ```text
> /plugin marketplace add duyunzhoudyz/dyz-gongwen-skills
> ```
>
> 插件安装名随之变为 `gongwen@dyz-gongwen-skills`，行业包为 `gongwen-hospital@dyz-gongwen-skills` 等，详见下方“安装”。

落地页：https://duyunzhoudyz.github.io/dyz-gongwen-skills/

## 一句话定位

给机关、事业单位、国企文字工作者用的开源公文写作 Skills 集合。懂条例国标，懂单位差异，懂岗位角色；不编造，守保密，帮你做减法。

## 本版更新

v1.1.0 是行业包专项修订：五个行业包均升为 Stable（国企包 soe 经补规则、复测后升级），国企包版本升到 1.1.0。

### 更名

- 仓库与套件更名为 dyz-gongwen-skills，旧地址 GitHub 会自动跳转。已经安装过的用户需重新执行 `/plugin marketplace add duyunzhoudyz/dyz-gongwen-skills`。22 个 skill 自己的名称（gongwen、gongwen-draft 等）不变。

### 行业包

- **内容补齐**：核验日期统一；各包 `calendar.md` 扩充；模板补正误对照；5 个包 `evals` 新增 27 条用例，共 116 条；配有机检脚本的包补必错、必过标本测试。
- **soe 边界修复**：国企包与其他行业包、核心 skill 的转交边界，用例 17 的转交目标由 gongwen-university 改为 gongwen-minutes；复核中发现的编造倾向已补规则。
- **hospital 整改口径统一**：整改状态的口径按 gongwen-rectify 统一（用例 12）。
- **k12 速查卡改名**：`references/quick-ref.md` 改名为 `quick-cards.md`，与其他行业包一致。

### 工具与文档

- `tools/validate.py` 新增三项检查：成熟度标签一致性（README 标签与 `manifest.json` 的 `status`）、共享副本登记、行业包工程门槛。
- 升级标准修订：`CONTRIBUTING.md` 的 Stable 标准改为数字标准加行业包工程门槛，不再等一线反馈和人工盲评，升级后持续收集。
- 文档中的提示词版字符上限更正为 2
```
</details>

---
### 📦 [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop)
`⭐ Stars: 24,828` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.3.1](https://github.com/vercel-labs/agent-desktop/releases/tag/v1.3.1) (2026-11-13)`

> **简介**：计算机使用 CLI 进行 AI 代理

**💡 核心亮点更新 (中文)**：
* 修复：在 https://github.com/vercel-labs/agent-desktop/pull/672 中，启动器退出后保持已启动的沙箱运行
* 杂务（发布）：1.3.1 来自 https://github.com/vercel-labs/agent-desktop/pull/680

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## What's Changed
* chore(deps): bump rustix to 1.1.6 for RUSTSEC-2026-0486 by @lahfir in https://github.com/vercel-labs/agent-desktop/pull/670
* fix: keep a started sandbox running after its launcher exits by @lahfir in https://github.com/vercel-labs/agent-desktop/pull/672
* chore(release): 1.3.1 by @lahfir in https://github.com/vercel-labs/agent-desktop/pull/680


**Full Changelog**: https://github.com/vercel-labs/agent-desktop/compare/v1.3.0...v1.3.1
```
</details>

---
### 📦 [JimLiu/baocut](https://github.com/JimLiu/baocut)
`⭐ Stars: 1,782` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [baocut-v3.19.2-build.97](https://github.com/JimLiu/baocut/releases/tag/baocut-v3.19.2-build.97) (2026-11-15)`

> **简介**：BaoCut：具有可编辑时间线的人工智能视频代理。转录、字幕、翻译、配音、剪辑和动画。

**💡 核心亮点更新 (中文)**：
- 代理现在将长翻译分批写入视频（第一批，然后从下一个未翻译句子开始追加批次），而不是一次非常大的写入，并继续进行，直到覆盖每个句子。部分书面翻译仍列为正在运行，并在回合结束时报告为未完成的工作，而不是默默停止。 ([来源](https://github.com/jimliu/baocut/commit/dcf05c4bb1bae72cdce4c0bce5f86fa479cc32ad))
- 座席批量翻译时，字幕面板、条带芯片、显卡、视频状态和任务列表会显示“已翻译的 N/M 句”以及百分比。在第一批到达之前，它们会显示句子总数和不确定栏。 ([来源](https://github.com/jimliu/baocut/commit/079107f9e9b486b47a298daea21c82a1a7165d65))
- 当无法读取登录 shell 环境时，例如，当 BaoCut 从 Finder 或 Dock 启动时，BaoCut 不再在进程的生命周期内保留该失败：它会在短暂的冷却后重试。当登录 shell 和进程 PATH 后，当这些文件夹存在时，它还会在“/opt/homebrew/bin”、“/usr/local/bin”和“/home/linuxbrew/.linuxbrew/bin”中查找 ffmpeg 和 ffprobe。 `BAOCUT_FFMPEG` 和 `BAOCUT_FFPROBE` 仍然优先。运行时日志现在记录 shell 探测失败的原因以及引擎在何处找到 ffprobe 和 ffmpeg。 （[#139]（https://github.com/JimLiu/baocut/issues/139），[来源]（https://github.com/jimliu/baocut/commit/4b31b2f18a9fba271ee4e1be6a5e48291ebdf8e6）， [来源](https://github.com/jimliu/baocut/commit/b3fdb9f1060ae1b7f38e6df23e1dd54aee0d1bba))

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## BaoCut 3.19.2 (build 97)

### Subtitle translation
- Agents now write long translations into the video in batches (the first batch, then appended batches resuming from the next untranslated sentence) instead of one very large write, and keep going until every sentence is covered. A partly written translation stays listed as running and is reported as unfinished work at the end of the turn instead of stopping silently. ([source](https://github.com/jimliu/baocut/commit/dcf05c4bb1bae72cdce4c0bce5f86fa479cc32ad))
- While an agent translates in batches, the subtitle panel, its strip chip, the video card, the video status and the task list show "translated N / M sentences" with a percentage. Before the first batch arrives they show the sentence total and an indeterminate bar. ([source](https://github.com/jimliu/baocut/commit/079107f9e9b486b47a298daea21c82a1a7165d65))

### Video engine tools
- When the login shell environment cannot be read, for example when BaoCut starts from Finder or the Dock, BaoCut no longer keeps that failure for the life of the process: it retries after a short cooldown. It also looks for ffmpeg and ffprobe in `/opt/homebrew/bin`, `/usr/local/bin` and `/home/linuxbrew/.linuxbrew/bin` when those folders exist, after the login shell and process PATH. `BAOCUT_FFMPEG` and `BAOCUT_FFPROBE` still take priority. The Runtime log now records why the shell probe failed and where the engine found ffprobe and ffmpeg. ([#139](https://github.com/JimLiu/baocut/issues/139
```
</details>

---
### 📦 [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)
`⭐ Stars: 24,526` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.1.166](https://github.com/milind-soni/OpenMausBot/releases/tag/v0.1.166) (2026-11-17)`

> **简介**：开源 Grok Bot 替代品，带有机器人可以使用的虚拟机

**💡 核心亮点更新 (中文)**：
- **默认情况下，机器人发布到您的 Netlify 帐户的站点是公开的。** 知道链接的任何人都可以打开它们，即使您的 Netlify 团队保护新站点也是如此。请求一个私人网站，机器人会保持其私密性，并记住该选择。
- **聊天中的实时预览。** 当机器人发布您的网站或页面之一时，其回复会显示一个带有“打开”和“在浏览器中打开”的小型实时预览。
- **每个请求都包含较少的固定文本：** 新机器人的内置指令大约小 18%，Chief 大约小 15%，并且保留每条规则。现在，某些工具仅在需要时加载，并且很少更改的文本将被缓存而不是重新发送。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## What's new in 0.1.166

### Publish sites and apps
- **Sites a bot publishes to your Netlify account are public by default.** Anyone with the link can open them, even when your Netlify team protects new sites. Ask for a private site and the bot keeps it private, and remembers that choice.
- **A live preview in the chat.** When a bot publishes one of your sites or pages, its reply shows a small live preview with Open and Open in browser.

### Fewer tokens, same rules
- **Each request carries less fixed text:** a new bot's built-in instructions are about 18% smaller and a Chief's about 15%, with every rule kept. Some tools are now loaded only when needed, and text that rarely changes is cached instead of re-sent.

### Settings you can find
- **Every "Settings → …" the app and its bots mention is a real place**, in every language that has it.

### Chat and sidebar
- **The chat header and sidebar are easier to read:** the open conversation reads as selected, a red dot marks a bot whose last turn failed, a bot's other threads are one tap away in Simple mode, and department lines get a clearer mark.
- **A context button** in the message box shows what fills the window, with Compact and Start fresh.
- **Pinned messages move into a header menu; pages end at the message box and open from a clean card.**
- **Read this aloud** appears in a message's hover bar once a voice is set up.
- **Chats get titles automatically.**

### Bots and rooms
- **Room jobs run side by side by default**,
```
</details>

---
### 📦 [yuchen-ya/reelterminal](https://github.com/yuchen-ya/reelterminal)
`⭐ Stars: 25` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.5.0](https://github.com/yuchen-ya/reelterminal/releases/tag/v1.5.0) (2026-11-17)`

> **简介**：ReelTerminal — 您的 AI 视频的最后一站。具有共享人类/代理控制的代理本机视频整理编辑器。

**💡 核心亮点更新 (中文)**：
- CLI 可在一次编辑中调整多个相邻片段，按最终布局检查重叠；被拒绝的批次不会保留部分编辑。
- `timeline.retimeByAnchors` 按明确的源时间与时间线锚点生成分段或速度曲线，适合将画面节点对齐音乐。转场可选择严格检查源余量，或明确允许借用片段内容并移动后续片段。
- `audio.process.remix` 将音乐重组为指定时长，支持节拍、小节范围、尾奏和响度参数；完成后通过 `audio.process.register` 明确注册，不自动替换时间线音频。重混是节拍拼接，不保证适合任意音乐；使用前请试听。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# ReelTerminal 1.5.0

## 时间线与声音

- CLI 可在一次编辑中调整多个相邻片段，按最终布局检查重叠；被拒绝的批次不会保留部分编辑。
- `timeline.retimeByAnchors` 按明确的源时间与时间线锚点生成分段或速度曲线，适合将画面节点对齐音乐。转场可选择严格检查源余量，或明确允许借用片段内容并移动后续片段。
- `audio.process.remix` 将音乐重组为指定时长，支持节拍、小节范围、尾奏和响度参数；完成后通过 `audio.process.register` 明确注册，不自动替换时间线音频。重混是节拍拼接，不保证适合任意音乐；使用前请试听。
- Ducking 可在最后一段声音结束后抬升背景音乐并淡出，包括零时长抬升。

## 动画、导入与交付

- `media.render_html` 可逐帧生成本地 HTML/CSS/SVG 动画：支持 CSS 动画、SMIL 及时间/进度变量。透明视频使用 WebM；MP4 不保留透明通道。页面脚本和外部网络资源仍不开放。
- 透明 WebM 在预览、静帧和导出中保留底层画面；生成的 WebM 同时固定 SDR BT.709 像素转换和色彩标记，减少解码路径间的颜色偏差。
- SVG 描边支持路径起点、终点与周期偏移关键帧，用于路径生长或擦除。
- `export.start` 可为 MP4 附加 PNG/JPEG 封面，并输出 SRT 字幕与章节文本。字幕与章节使用本次导出开始时的工程内容，不会混入之后的编辑；已有附件路径不会被静默覆盖。
- 桌面 CLI 的本地媒体导入上限提高至 8 GiB，大文件从本地路径流式复制。源文件在复制中改变时拒绝发布不完整副本。大小上限不保证任意编码可解码或流畅编辑。
- CLI 的复杂 JSON 推荐使用 `--stdin` 或 `--file`，减少 PowerShell/cmd 引号改写问题。

以上新增结构化操作通过 CLI 提供；使用应用的启动提示连接助手，再按共享命令帮助发现参数。写入仍需要对应工程的编辑权限和版本检查。

## 使用限制

FFmpeg/ffprobe 等可选工具需要单独安装和配置，见[外部依赖](https://github.com/yuchen-ya/reelterminal/blob/49cd32db21d7ebc1a04388db9edbdc300fb0fe69/docs/EXTERNAL-DEPENDENCIES.md)。视频保持 SDR 8-bit 边界；缺少完整色彩标记的源可能在预览与导出间出现色差，HDR/10-bit 色彩保留不支持。请一并规范源像素和色彩标记，并在交付前检查输出，见[色彩说明](https://github.com/yuchen-ya/reelterminal/blob/49cd32db21d7ebc1a04388db9edbdc300fb0fe69/docs/COLOR.md)。软件渲染需要额外 CPU 工作，高分辨率播放可能无法实时。

Windows x64 发行包未签名，系统可能显示发布者或 SmartScreen 提示；请从官方发行页下载并核对校验和。升级前保留工程与素材，见[升级与备份指南](https://github.com/yuchen-ya/reelterminal/blob/49cd32db21d7ebc1a04388db9edbdc300fb0fe69/docs/WINDOWS-UPGRADE.md)。其他平台以发行页实际列
```
</details>

---
### 📦 [KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)
`⭐ Stars: 5,764` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.9.1](https://github.com/KKKKhazix/agent-autoloop/releases/tag/v1.9.1) (2026-11-17)`

> **简介**：让你的命令行 Agent 在后台自己接活、自己跟进到底；平时不烦你，遇到拿不准的事才发卡片找你拍板。

**💡 核心亮点更新 (中文)**：
- 当工作人员无法恢复旧会话并且新会话也无法启动时（比如 Codex 碰巧丢失），它不再向集线器提供它在本地创建的会话 ID；原始会话将被保留，下一次重试将恢复它（#315，由 bluRays 在#306 中发现）。
- 从发布 tarball 安装的副本（不带 .git）可以通过“AGENT_AUTOLOOP_RELEASE”告诉“--version”它是哪个版本（#305）。
- 交付：当标记为就绪的 PR 最终没有检查运行或根本没有所需的作业时，检查也会在 10 分钟后再次触发 (#322)。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 改了什么

- 接着旧会话做却接不上、新会话也没跑起来时（比如 Codex 程序刚好不在），接单程序不再把自己编的会话号交给中台，原会话保住，下次重派还在原会话里接着做（#315，问题由 bluRays 在 #306 里找到）。
- 从 Release 压缩包装出来、没有 .git 的副本，可以用环境变量 `AGENT_AUTOLOOP_RELEASE` 告诉 `--version` 是哪一版（#305）。
- 交付插件：PR 转成就绪后，连检查记录或必需任务都没建出来的，10 分钟后也会重新触发一次检查（#322）。
- 补了几处测试没覆盖到的检查（#304、#307、#313）。

感谢 bluRays、guicaiyue、argszero。

## What's changed

- When a worker can't resume the old session and the new one doesn't start either (say Codex happens to be missing), it no longer hands the hub a session id it made up locally; the original session is kept and the next retry resumes it (#315, found by bluRays in #306).
- A copy installed from a Release tarball, without .git, can tell `--version` which release it is through `AGENT_AUTOLOOP_RELEASE` (#305).
- Delivery: when a PR marked ready ends up with no check run or required job at all, checks are triggered again after 10 minutes as well (#322).
- Tests now cover a few checks they never reached (#304, #307, #313).

Thanks to bluRays, guicaiyue and argszero.
```
</details>

---
### 📦 [alchaincyf/huashu-motion](https://github.com/alchaincyf/huashu-motion)
`⭐ Stars: 2,822` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.5.1](https://github.com/alchaincyf/huashu-motion/releases/tag/v0.5.1) (2026-11-16)`

> **简介**：让你的agent一键直出商业级产品宣传片：会作曲，能指着画面改。Commercial-grade launch films by your coding agent — point at the frame to change it.

**💡 核心亮点更新 (中文)**：
- `om render` 不能再以退出代码 0 结束，同时在 `out/` 中留下空（0 字节）文件。如果进程在渲染完成之前结束，无论出于何种原因，占位符文件都会被删除，退出代码为 1，并且一条消息表明渲染在完成之前停止 (#3)。
- 长渲染不再打印“MaxListenersExceededWarning：...关闭侦听器添加到[ChildProcess]”。每次等待编码器都会留下一个侦听器；现在它们已被删除。该警告是无害的，但会出现在大型电影的每个渲染中，看起来像一个错误（#3）。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Fixed

- `om render` can no longer end with exit code 0 while leaving an empty (0-byte) file in `out/`. If the process ends before the render has finished, for whatever reason, the placeholder file is removed, the exit code is 1, and a message says the render stopped before it finished (#3).
- A long render no longer prints `MaxListenersExceededWarning: ... close listeners added to [ChildProcess]`. Each wait for the encoder left a listener behind; they are now removed. The warning was harmless but showed up on every render of a large film and looked like an error (#3).

## Update

```
npm i -g huashu-motion@0.5.1
```
or `git pull --ff-only` in your clone.
```
</details>

---
### 📦 [wquguru/cicada](https://github.com/wquguru/cicada)
`⭐ Stars: 2,375` &nbsp;|&nbsp; `💻 语言: Swift` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.10.1](https://github.com/wquguru/cicada/releases/tag/v1.10.1) (2026-11-14)`

> **简介**：知了 Cicada · 任何会议和直播的实时字幕、同声传译、AI 会议纪要，Mac、Windows、Linux、Android 免费开源。Live subtitles, interpreting and meeting notes for any call or stream, on Mac, Windows, Linux and Android.

**💡 核心亮点更新 (中文)**：
- 在音频服务或设备重置后收听 PC 重新连接，而不是录制静音 ([95e45b9](https://github.com/wquguru/cicada/commit/95e45b99e115cd315c94eae83cbc1cdb3963d232))
- 一条通知说明为什么收听停止，并且断开的房间麦克风显示为关闭（[058b233](https://github.com/wquguru/cicada/commit/058b233961be6814899d4c27fe165c2e2e564a7a))
- 允许使用麦克风但从未使用过的应用程序不再算作通话，因此会议自行结束 ([663ef93](https://github.com/wquguru/cicada/commit/663ef932ab1ffc247ed4c3809beaaa03286a1614))

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
### Mac

No changes; released to keep every platform on the same version.

### Windows

#### Fixed

- Listening to the PC reconnects after the audio service or a device resets, instead of recording silence ([95e45b9](https://github.com/wquguru/cicada/commit/95e45b99e115cd315c94eae83cbc1cdb3963d232))
- A notice says why listening stopped, and a disconnected room mic shows as off ([058b233](https://github.com/wquguru/cicada/commit/058b233961be6814899d4c27fe165c2e2e564a7a))
- An app allowed the microphone but never used no longer counts as in a call, so meetings end on their own ([663ef93](https://github.com/wquguru/cicada/commit/663ef932ab1ffc247ed4c3809beaaa03286a1614))

### Android

No changes; released to keep every platform on the same version.

### Linux

No changes; released to keep every platform on the same version.

---

**Full changelog**: https://github.com/wquguru/cicada/compare/v1.10.0...v1.10.1

中文更新说明：https://cicada.indaloop.app/changelog/


**Mac** (macOS 14.4 or later): download `Cicada-1.10.1-macOS-AppleSilicon.dmg` (Apple silicon) or `Cicada-1.10.1-macOS-Intel.dmg` (Intel), open it and drag **知了 Cicada** into **Applications**. First launch: **System Settings › Privacy & Security › Open Anyway**.

**Windows** (Windows 10 2004 or later): download `Cicada-1.10.1-Windows-x64.exe` (`Cicada-1.10.1-Windows-ARM64.exe` on Snapdragon laptops) and double-click it; it installs without admin rights. If SmartScreen stops it: **More info › Run anyway**.

**Linux** (Ubuntu
```
</details>

---
### 📦 [SourceWeft/SourceWeft](https://github.com/SourceWeft/SourceWeft)
`⭐ Stars: 508` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.3.0-rc.9](https://github.com/SourceWeft/SourceWeft/releases/tag/v0.3.0-rc.9) (2026-11-16)`

> **简介**：ChatGPT 和 NotebookLM 的开源、自托管替代方案 — 一个 AI 工作站中的代理、技能、MCP 和引用知识。您的模型，您的基础设施。包括公共 MCP 服务器和代理技能目录。

**💡 核心亮点更新 (中文)**：
* 修复（seo）：准确的lastmod、本地化的目录元数据和方面抓取规则（https://github.com/SourceWeft/SourceWeft/pull/282）
* 杂务（计费）：将 Waffo 环境设置与 https://github.com/SourceWeft/SourceWeft/pull/288 中的 CREEM_TEST_MODE 对齐
* 修复（seo）：通过 https://github.com/SourceWeft/SourceWeft/pull/293 保持 React Server 组件有效负载不被抓取

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Self-hosting files for Web/Docker, macOS and Windows installers, and Linux x64 AppImage and .deb packages.

macOS installers are Developer ID signed and notarized. Windows installers have no publisher certificate; Windows may warn or block installation. Historical clients without an update key need one manual overwrite upgrade.
All application update packages have verified Tauri updater signatures. Local device execution runs in a signed sandbox runtime (sourceweft-sandbox-*.tar.gz, verified with the same updater key) that the app downloads and verifies on first use, on macOS (Apple silicon and Intel), Linux x86_64 and Windows (x64 and arm64).
See docker/README.md in the self-hosting archive for installation and upgrade instructions. Translations are provided in separate README files.


## What's Changed
* fix(seo): accurate lastmod, localized catalog metadata, and facet crawl rules by @QThans in https://github.com/SourceWeft/SourceWeft/pull/282
* chore(billing): align Waffo environment setting with CREEM_TEST_MODE by @QThans in https://github.com/SourceWeft/SourceWeft/pull/288
* fix(seo): keep React Server Component payloads out of the crawl by @QThans in https://github.com/SourceWeft/SourceWeft/pull/293
* fix(seo): review follow-ups — content-based lastmod, leaner sync, shared locale parsing by @QThans in https://github.com/SourceWeft/SourceWeft/pull/291
* feat(web): "Listed on SourceWeft" README badge by @QThans in https://github.com/SourceWeft/SourceWeft/pull/292
* fix: r
```
</details>

---
### 📦 [openai/codex](https://github.com/openai/codex)
`⭐ Stars: 135,617` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [rust-v0.169.0](https://github.com/openai/codex/releases/tag/rust-v0.169.0) (2026-11-13)`

> **简介**：在您的终端中运行的轻量级编码代理

**💡 核心亮点更新 (中文)**：
- 选择加入的终端工作区支持多个侧边聊天选项卡。使用键盘或鼠标在它们之间切换，并在重新启动 Codex 后重新打开保存的本地聊天。 （#59784、#60152、#60181）
- 按名称、提示预览或工作目录从代理命令中心搜索旧任务。 (#60286)
- 在全屏记录中打开**折叠回合详细信息**，将已完成的活动折叠在每个提示下方，同时保持答案可见且工具输出可搜索。 （#60554、#60555、#60556、#60557）

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## New Features

- The opt-in terminal workspace supports multiple side-chat tabs. Switch between them with the keyboard or mouse, and reopen saved local side chats after restarting Codex. (#59784, #60152, #60181)
- Search older tasks from the agent command center by name, prompt preview, or working directory. (#60286)
- Turn on **Collapse turn details** in the full-screen transcript to fold completed activity beneath each prompt while keeping answers visible and tool output searchable. (#60554, #60555, #60556, #60557)
- Add or edit custom model providers from the terminal. With custom gateway onboarding enabled, you can create a provider during sign-in and use a device code for supported gateways over SSH or without a local browser. (#59779, #60009, #60186, #60486, #60662)
- Press `Ctrl+S` in the terminal report editor to save a diagnostic ZIP locally, even when uploads are disabled. (#60542)
- With the opt-in Cloud connection on macOS and Linux, send images, choose a model and reasoning effort, and archive or restore Cloud conversations from the terminal. (#59828, #60061, #60635, #60651)

## Bug Fixes

- `codex exec` keeps project configuration and MCP servers disabled in untrusted directories, even with `--sandbox workspace-write`. Use `--trust` with `codex exec` or `codex review` to explicitly save project trust. (#60041)
- **Yes, clear context and implement** now hands the full approved plan to the fresh session and keeps the current session open if the handoff fails. (#
```
</details>

---
### 📦 [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)
`⭐ Stars: 16,037` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.4.7](https://github.com/akitaonrails/ai-memory/releases/tag/v3.4.7) (2026-11-15)`

> **简介**：用于代理编码 CLI 的长期记忆解决方案，并促进不同代理供应商之间的切换

**💡 核心亮点更新 (中文)**：
校验和 (SHA256)
````
7066fd012659f78631afb8b5a50cc06c36a489ad90c01f334b1c14b93434c237 ai-内存-3.4.7-1.aarch64.rpm
ebc119283d55c0d72eff89b04c64c84b08828a180f0067e474752332d7bb4cd3 ai-memory-3.4.7-1.x86_64.rpm
93463c368436db50a70824c65dbcd153e685

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Checksums (SHA256)
```
7066fd012659f78631afb8b5a50cc06c36a489ad90c01f334b1c14b93434c237  ai-memory-3.4.7-1.aarch64.rpm
ebc119283d55c0d72eff89b04c64c84b08828a180f0067e474752332d7bb4cd3  ai-memory-3.4.7-1.x86_64.rpm
93463c368436db50a70824c65dbcd153e685cb186c59e86ce06cb286ced446e4  ai-memory-claude-plugin.zip
b38d2aedd8603cc5aa8026426ead4361e5198905da2294d2961314d19a0e2725  ai-memory-hooks.tar.gz
5b8b9030c247b091ac2bacbf181f52f8fdba9d4ed47cdef23faab874d4c94d9f  ai-memory-install-hooks
020615f4d761b48629e09981ec5d7f8702faa197ff9613e6b793fe326175eedf  ai-memory-linux-aarch64.tar.gz
97d1954d4bdef549f4b39d169434ca6741d0755dd3135ab78da8c22e812f8bad  ai-memory-linux-x86_64.tar.gz
7f3c279f04e13781c9b0b75d7b9ff9e4c2bf99629c018e92073b7da2f538673d  ai-memory-macos-aarch64.tar.gz
91610afc01148f910a3250bb525c74c328aac418c7279ea67e531f9292422a55  ai-memory-macos-x86_64.tar.gz
69f41ea75c8422d8ff21543fcc2423f99ff1c3ac83b388a5097c49bc8e31e715  ai-memory-windows-x86_64.zip
6a91c44ffa2e85d3b5a6ce26a4ccff0286b91d08d276d2bb4d47c346b036ee8b  ai-memory-wrapper.cmd
5e405aa237a2399f13084f71ae89545cbca77683c8251b4c4572cb51aedc8de4  ai-memory-wrapper.ps1
e08e77b4fd93dd8aa9be9bb160ab831770e2ba9763592d138cfb8acb26f20248  ai-memory-wrapper
c05aedd9a572d5807986910d5099adac132ae558d677bc2d0f64a6d53eaf0d3b  install.ps1
bac95bc26ed8ab5751117283a3568fa52c341b38294440cd1bb808056d0f0395  install.sh
```

## Install
```bash
# Linux/macOS, no root: checksum-verified release binary under ~/.local, then one-step set
```
</details>

---
### 📦 [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)
`⭐ Stars: 59,945` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.7.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.7.3) (2026-11-15)`

> **简介**：DeepTutor：终身个性化辅导。 https://deeptutor.info/。

**💡 核心亮点更新 (中文)**：
- **完整应用程序：** 停止 DeepTutor 并备份运行时主目录，然后运行 ​​`python -m pip install --upgrade "deeptutor[full]==1.7.3"`。保持相同的`DEEPTUTOR_HOME`；在重新启动之前使用“python -m pip check”和“deeptutor module list”进行验证。附加功能轮也必须符合 1.7.3。
- **旧版安装：** 1.6.15 及更早版本需要在安装模块化系列之前卸载旧的 `deeptutor-cli` 软件包。使用[v1.7.0](past_releases/ver1-7-0.md)中的手动迁移；旧的更新工作线程无法追溯获取新的迁移逻辑。在同一环境中使用“deeptutor[full,parse]==1.7.3”` 恢复具有可选解析的完整应用程序。
- **源和 Docker：**源用户安装 `requirements/full.txt`，然后安装 `python -m pip install -e 。 --no-deps`，并在 Node.js 22 上使用 `npm ci --legacy-peer-deps` 刷新 `web/`。Docker 用户拉取 `ghcr.io/hkuds/deeptutor:1.7.3` 或 `:latest` 并使用现有数据卷重新创建容器。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# DeepTutor v1.7.3 Release Notes

**Release Date:** 2026.11.16

Building on [v1.7.2](past_releases/ver1-7-2.md), v1.7.3 makes reading and book editing more flexible, expands search and agent connections, and improves learning records, model streams, and desktop upgrades.

## What's New

### Read, zoom, and revisit question help

The PDF reader adds continuous zoom, text-fit controls, and an image viewer. Annotation updates and multi-material selection are more reliable. Reading quizzes keep answer keys on the server and preserve question-linked help separately from attempts; authorized guardians can review reading progress, quiz records, and help activity.

### Review book changes before applying them

Edit generated chapters and sections without rebuilding the whole book. Structure changes and page-chat proposals show a reviewable diff before application, and the most recent unchanged edit can be undone. New empty sections generate when opened; math rendering and page-chat continuation also receive fixes.

### More search providers and connected agents

Search adds DeepSeek, SpecStream, and SearchApi, including SearchApi web, news, and scholar modes. Web Fetch gains a selectable DeepSeek backend, and Standard Compute joins model setup. A configured Agent Client Protocol (ACP) process can be consulted as a local subagent. MCP OAuth refresh and reconnection are more reliable after consent and restarts.

### Conversations and practice retain their context

Choose supported reas
```
</details>

---
### 📦 [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)
`⭐ Stars: 112,556` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.6.1](https://github.com/Panniantong/Agent-Reach/releases/tag/v1.6.1) (2026-11-01)`

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
`⭐ Stars: 24` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.3.11](https://github.com/Hsiung-Shao/exile-appraiser/releases/tag/v0.3.11) (2026-11-16)`

> **简介**：ExileAppraiser / 流亡鑑價:Path of Exile 1/2 查價器,支援國際服與台服(繁中/英文客戶端)

**💡 核心亮点更新 (中文)**：
修正

・**PoE1 阿茲瓦特史記 3.30 改名的房間顯示為未解析**：創造之搖籃、皇家熔爐、宏偉反應爐；另修正「異常研究所」。
・**PoE1 壁壘地圖的固定詞綴顯示為未解析**：例如「地圖含有巴倫的壁壘」。
・**PoE1 箭袋固定詞綴「箭矢穿透一個額外目標」顯示為未解析**。
・**PoE1 珠寶「+% 單手近戰武器暴擊加成」等 20 多條詞綴顯示為未解析**：補上 3.30 的繁中寫法。
・**視窗模式的相關物品蓋住查價內容**。

新增

・**查價面板顯示神聖石匯率**：面板最上

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 修正

・**PoE1 阿茲瓦特史記 3.30 改名的房間顯示為未解析**：創造之搖籃、皇家熔爐、宏偉反應爐；另修正「異常研究所」。
・**PoE1 壁壘地圖的固定詞綴顯示為未解析**：例如「地圖含有巴倫的壁壘」。
・**PoE1 箭袋固定詞綴「箭矢穿透一個額外目標」顯示為未解析**。
・**PoE1 珠寶「+#% 單手近戰武器暴擊加成」等 20 多條詞綴顯示為未解析**：補上 3.30 的繁中寫法。
・**視窗模式的相關物品蓋住查價內容**。

## 新增

・**查價面板顯示神聖石匯率**：面板最上方顯示 1 神聖石換多少混沌石。（PoE2 為崇高石；只在國際服）
・**PoE1 地圖的「輿圖掉落物」與「更多 綢帶」**：輿圖掉落物可當查價條件，預設勾選。
・**建立桌面捷徑**：設定 › 一般新增按鈕；安裝檔每次安裝都會建立桌面與開始功能表捷徑。

## 調整

・**查價的「交易」鈕改用強調色**，固定在掛單標題列第 2 行左側。
・**新版本提醒停留 5 秒後淡出**。（原本 8 秒）

說明：設定檔、正則書籤與分享碼沿用舊格式。新補的詞綴多數沒有實機樣本，遇到未解析或查不到請用面板上的回報按鈕。偶爾按了查價熱鍵沒有彈出面板的問題尚未找到原因，這一版只加了診斷記錄，遇到時請到「設定 › 記錄」搜尋「全域熱鍵沒觸發」並回報。
```
</details>

---
### 📦 [microsoft/skill-recorder](https://github.com/microsoft/skill-recorder)
`⭐ Stars: 5,842` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.9.2](https://github.com/microsoft/skill-recorder/releases/tag/v0.9.2) (2026-11-12)`

> **简介**：桌面应用程序，记录您的屏幕上工作会话，并使用 GitHub Copilot SDK 将其重建为意图 + 有序步骤，然后为 Microsoft Autopilot（例如 Scout、Microsoft Copilot Cowork 或 Copilot Studio）构建可重用的技能或自动化。

**💡 核心亮点更新 (中文)**：
- **防止重复的 Skill Recorder 实例。** Electron 的本机单实例锁是在记录器初始化之前获取的。另一次启动会显示现有的记录器或活动记录控件，而不是创建另一个主进程、托盘和记录器。
- **恢复现有窗口。**重复启动恢复最小化的记录器；启动期间收到的请求将在初始化后处理。再次启动不会启动、停止或放弃录制，并且在关闭期间不会重新打开窗口。
- **明确 Windows 升级。** 新安装和同一提交重新安装均通过手动启动说明完成，而不是自动打开另一个副本。现有的快捷方式警告仍然可见，并且当无法创建快捷方式时，会提供安全引用的后备命令。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Commit-pinned installation

Copy the complete command for your operating system into PowerShell (Windows) or Terminal (macOS/Ubuntu). Use the same command to install or update.

### Windows 11 x64 or ARM64

```powershell
$commit="63bbb50111713b02f3bc0ebbd5f354f4eb038f99"; $env:SKILL_RECORDER_COMMIT=$commit; irm "https://raw.githubusercontent.com/microsoft/skill-recorder/$commit/install.ps1" | iex
```

**Windows now finishes installation without opening the app.** Follow the prominent `@`-bordered completion notice: finish recording, choose **Quit** in every running Skill Recorder copy, wait for them to close, then open **Skill Recorder (Source)** from the desktop or Start menu. If shortcut creation fails, use the manual launch command printed by the installer. Reopen the app, not the installer.

### macOS or Ubuntu

Quit older running copies before updating, then run:

```sh
commit="63bbb50111713b02f3bc0ebbd5f354f4eb038f99"; curl -fsSL "https://raw.githubusercontent.com/microsoft/skill-recorder/$commit/install.sh" | SKILL_RECORDER_COMMIT="$commit" bash
```

The macOS/Ubuntu installer retains its existing automatic-launch behavior.

For script inspection and hash verification before execution, use the [inspect-first instructions](https://github.com/microsoft/skill-recorder/blob/63bbb50111713b02f3bc0ebbd5f354f4eb038f99/INSTALL.md#inspect-first-installation). Installer SHA-256 values are listed below.

## Fixes

- **Prevent duplicate Skill Recorder i
```
</details>

---
### 📦 [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model)
`⭐ Stars: 78,103` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.8.5-macos-unofficial](https://github.com/Ebony-Vinyl/dsh-our-free-model/releases/tag/v2.8.5-macos-unofficial) (2026-11-15)`

> **简介**：在 dsh 里装上这个插件即可，无需登录、注册或填 API Key，就能使用包括 DeepSeek V4.1 Flash、Kimi K3 在内的前沿模型——完全免费，不限量。 All you do is install this plugin in dsh: no login, no sign-up, no API key — the frontier models are just there, DeepSeek V4.1 Flash and Kimi K3 among them. Completely free, with no usage cap.

**💡 核心亮点更新 (中文)**：
- 构建来源 / Source: v2.8.5 @ 8cb6ac429257e6af9aba6e7746a18f8e6aee9c67
- 构建记录 / CI run: https://github.com/Ebony-Vinyl/dsh-our-free-model/actions/runs/43673101657
- SHA256: 696df3e521a238de1f46c12a7031d3f6fa2e0032e92a1b109aaec937cfdab6c4

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 非官方社区构建 / Unofficial community build

这不是仓库作者发布的官方安装包。作者自 2.4.0 起将桌面安装包限制为 Windows-only，Mac 用户停留在 2.3.0。本 dmg 由本仓库的 GitHub Actions 从公开源码构建，可审计、可复现。

This is NOT an official release by the repository author. The author restricted desktop installers to Windows-only since 2.4.0, leaving Mac users on 2.3.0. This dmg is built by GitHub Actions from public, auditable source.

| 项 / Item | 值 / Value |
|---|---|
| 版本 / Version | 2.8.5 |
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
- 构建来源 / Source: v2.8.5 @ 8cb6ac429257e6af9aba6e7746a18f8e6aee9c67
- 构建记录 / CI run: https://github.com/Ebony-Vinyl/dsh-our-free-model/actions/runs/43673101657
- SHA256: 696df3e521a238de1f46c12a7031d3f6fa2e0032e92a1b109aaec937cfdab6c4
```
</details>

---
### 📦 [hypit-ai/hypit](https://github.com/hypit-ai/hypit)
`⭐ Stars: 30,337` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.3.3](https://github.com/hypit-ai/hypit/releases/tag/v0.3.3) (2026-11-16)`

> **简介**：使用人工智能代理克隆任何病毒视频。不仅仅是一个脚本，而是整个工作流程：交换面孔、文字、幕后花絮，在一个命令中发送 100 个变体，并获得 1 亿次观看。

**💡 核心亮点更新 (中文)**：
- 将模型包和 HypiHub 提供商中的巴赫视频生成限制为 1080p。
- 需要第一帧进行帧引导生成，并接受可选的最后一帧。
- 更新 Bach Surface 定义、示例和依赖版本。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Changes

- Restrict Bach video generation to 1080p in the model package and HypiHub provider.
- Require a first frame for frame-guided generation and accept an optional last frame.
- Update Bach Surface definitions, examples and dependency versions.

## npm packages

- @hypit/hypit 0.3.3
- @hypit/bach 0.1.1
- @hypit/provider-hypihub 0.2.2
- @hypit/video 0.2.2

PR #499
```
</details>

---
### 📦 [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app)
`⭐ Stars: 22,076` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.0.10](https://github.com/HBAI-Ltd/Toonflow-app/releases/tag/v2.0.10) (2026-11-05)`

> **简介**：短剧、漫剧制作工具 Toonflow：开源 AI 视频创作平台，集成剧本创作、智能分镜、角色与场景资产管理、图像生成和视频生成。融合无限画布、AI Agent 与可视化工作流，支持本地部署、自选模型、跨平台客户端、MCP 与插件扩展。Open-source AI short drama and motion comic creation tool with an infinite canvas, AI agents, storyboarding, image and video generation. Self-hosted and extensible, with a canvas-based approach similar to LibTV and TapNow.

**💡 核心亮点更新 (中文)**：
- 💻 **Windows**：双击下载的安装包，按提示完成安装。ARM64 需要 .NET Framework 4.8.1，较新的 Windows 11 已内置。
- 🍎 **Mac（macOS 14 及以上）**：打开下载的 `.dmg` 镜像，将 `toonflow.app` 拖入“应用程序”，复制完成后再从“应用程序”打开。
- 🐧 **Linux（Debian / Ubuntu）**：选择对应架构的 DEB，在下载目录执行 `sudo apt install ./toonflow-版本号-linux-架构.deb`，安装后从应用菜单打开。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 📦 下载指南

选择你的设备对应的安装包，点击即可下载：

| 你的设备 | 下载 |
| --- | --- |
| 💻 Windows（Intel / AMD，x64） | [⬇️ 下载 Windows x64 安装包](https://github.com/HBAI-Ltd/Toonflow-app/releases/download/v2.0.10/toonflow-2.0.10-Setup.exe) |
| 💻 Windows（ARM64） | [⬇️ 下载 Windows ARM64 安装包](https://github.com/HBAI-Ltd/Toonflow-app/releases/download/v2.0.10/toonflow-2.0.10-win-arm64-Setup.exe) |
| 🍎 Mac（M 系列芯片） | [⬇️ 下载 M 系列 Mac 安装包](https://github.com/HBAI-Ltd/Toonflow-app/releases/download/v2.0.10/toonflow-2.0.10-macos-arm64.dmg) |
| 🍎 Mac（Intel 芯片） | [⬇️ 下载 Intel Mac 安装包](https://github.com/HBAI-Ltd/Toonflow-app/releases/download/v2.0.10/toonflow-2.0.10-macos-x64.dmg) |
| 🐧 Linux（Intel / AMD，x64） | [⬇️ 下载 Linux x64 DEB](https://github.com/HBAI-Ltd/Toonflow-app/releases/download/v2.0.10/toonflow-2.0.10-linux-x64.deb) |
| 🐧 Linux（ARM64） | [⬇️ 下载 Linux ARM64 DEB](https://github.com/HBAI-Ltd/Toonflow-app/releases/download/v2.0.10/toonflow-2.0.10-linux-arm64.deb) |
| 📱 Android（ARM64，Android 8 及以上） | [⬇️ 下载 Android APK](https://github.com/HBAI-Ltd/Toonflow-app/releases/download/v2.0.10/toonflow-2.0.10-android-arm64.apk) |

> 💡 手动安装请选择上表中的链接。下方其他文件供软件自动更新使用。

## 🚀 安装说明

- 💻 **Windows**：双击下载的安装包，按提示完成安装。ARM64 需要 .NET Framework 4.8.1，较新的 Windows 11 已内置。
- 🍎 **Mac（macOS 14 及以上）**：打开下载的 `.dmg` 镜像，将 `toonflow.app` 拖入“应用程序”，复制完成后再从“应用程序”打开。
- 🐧 **Linux（Debian / Ubuntu）**：选择对应架构的 DEB，在下载目录执行 `sudo apt install ./toonflow-版本号-linux-架构.deb`，安装后从应用菜单打开。
- 📱 **Android**：在手机上打开 APK，按系统提示允许此来源安装应用。后续版本可直接覆盖安装。

两种 Mac 应用与 DMG
```
</details>

---
### 📦 [morluto/rea](https://github.com/morluto/rea)
`⭐ Stars: 465,228` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [rea-agents-6.9.0](https://github.com/morluto/rea/releases/tag/rea-agents-6.9.0) (2026-11-12)`

> **简介**：使用代理对任何内容进行逆向工程，从应用程序行为到本机二进制文件。

**💡 核心亮点更新 (中文)**：
- 根据记录的应用程序状态构建和测试桌面任务，包括下载的 Linux 应用程序、可重复使用的构建计算机以及每次捕获的多个任务。
- 离线检查更多已交付的工件：独立应用程序包、嵌入式固件、NTFS 收购、API 合同和 V8 代码缓存容器。
- 使本机和运行时调查以保留的证据为基础，并提供分页结果、明确的覆盖范围和可恢复的资源限制。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## [6.9.0](https://github.com/morluto/rea/compare/rea-agents-6.8.0...rea-agents-6.9.0) (2026-11-11)

### Highlights

- Build and test desktop tasks from recorded application state, including downloaded Linux apps, reusable build computers and multiple tasks per capture.
- Inspect more shipped artifacts offline: standalone application bundles, embedded firmware, NTFS acquisitions, API contracts and V8 code-cache containers.
- Keep native and runtime investigations grounded in retained Evidence, with paged results, explicit coverage and recoverable resource limits.

### Changes

- Analyze targets and create private runtimes on fixed local ReFS volumes as well as NTFS, preserving persistent ACL, file identity, snapshot and cleanup checks. [#10086](https://github.com/morluto/rea/pull/10086). Thanks @QianNangong.
- Capture, export and witness desktop tasks inside a build computer; keep an agentenv computer available through MCP and prepare a build host from one command. [#8954](https://github.com/morluto/rea/pull/8954), [#9041](https://github.com/morluto/rea/pull/9041), [#9045](https://github.com/morluto/rea/pull/9045), [#9049](https://github.com/morluto/rea/pull/9049), [#9199](https://github.com/morluto/rea/pull/9199). Thanks @earakely-scale.
- Install desktop apps from SHA-256-pinned AppImages or upstream archives, retain selected package dependencies, and isolate explicitly declared build secrets. [#9215](https://github.com/morluto/rea/pull/9215), [#9112](https://github.com/mor
```
</details>

---
### 📦 [chatfire-AI/huobao-drama](https://github.com/chatfire-AI/huobao-drama)
`⭐ Stars: 17,624` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v4.0.11](https://github.com/chatfire-AI/huobao-drama/releases/tag/v4.0.11) (2026-11-05)`

> **简介**：🎬 火宝短剧 - 基于AI的一站式短剧生成平台 《一句话生成完整短剧，从剧本到成片全自动化》  Huobao Drama - An AI-Powered End-to-End Short Drama Generator "One Sentence to Complete Drama: Fully Automated from Script to Final Video"

**💡 核心亮点更新 (中文)**：
- 安装包和自动更新源迁移到 `installer.firemux.site`。
- 更新检查优先使用国内 CDN，保留 GitHub Releases 备用更新源。
- 同步内置服务的版本检查地址。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# HuobaoDrama 4.0.11

- 安装包和自动更新源迁移到 `installer.firemux.site`。
- 更新检查优先使用国内 CDN，保留 GitHub Releases 备用更新源。
- 同步内置服务的版本检查地址。

提供 macOS Apple Silicon、macOS Intel 和 Windows x64 安装包，以及 macOS 应用内更新 ZIP。

安装包沿用项目现有未签名配置。校验值见 SHA256SUMS 文件。
```
</details>

---
### 📦 [yetone/magpie](https://github.com/yetone/magpie)
`⭐ Stars: 37,946` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.1.4366](https://github.com/yetone/magpie/releases/tag/v0.1.4366) (2026-11-17)`

> **简介**：每个代理的模型。一处。来自菜单栏的 DeepSeek 上的 Codex、Kimi 上的 Claude Code。

**💡 核心亮点更新 (中文)**：
- 在窗口中提供的模型现在加入其模型的现有组（例如，具有 1M 上下文的 Claude Haiku 5.5）。
- **macOS（Apple Silicon）：** `magpie-darwin-arm64.dmg`
- **macOS（英特尔）：** `magpie-darwin-amd64.dmg`

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Improvements
- Models offered at a window now join their model’s existing group (e.g., Claude Haiku 5.5 with 1M context).

### Install

Download from [usemagpie.ai](https://usemagpie.ai), or `curl -fsSL https://usemagpie.ai/install.sh | sh`. An installed magpie updates itself.

- **macOS (Apple Silicon):** `magpie-darwin-arm64.dmg`
- **macOS (Intel):** `magpie-darwin-amd64.dmg`
- **Windows:** `magpie-windows-amd64.exe` (ARM: `magpie-windows-arm64.exe`)
- **Linux:** `magpie-linux-amd64` / `magpie-linux-arm64` (needs GTK 3 and WebKitGTK 4.1)
- **Terminal only:** `magpie-cli-<os>-<arch>`

Thanks to Will, whose reports and code went into this release. Everyone who helped: [contributors](https://usemagpie.ai/docs/contributors).

<!-- lang:zh -->

## Improvements
- 在窗口中提供的模型现在会加入其对应型号的现有组（例如，具有 1M 上下文的 Claude Haiku 5.5）。

### 安装

从 [usemagpie.ai](https://usemagpie.ai) 下载，或运行 `curl -fsSL https://usemagpie.ai/install.sh | sh`。已安装的 magpie 会自动更新。

感谢 Will：这次更新里有你的反馈与代码。所有贡献者见[贡献墙](https://usemagpie.ai/docs/zh/contributors)。



---
The same release, and the feed magpie updates from: https://github.com/yetone/magpie-releases/releases/tag/v0.1.4366
```
</details>

---
### 📦 [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
`⭐ Stars: 264,067` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.23.2](https://github.com/NousResearch/hermes-agent/releases/tag/v0.23.2) (2026-11-16)`

> **简介**：与您共同成长的代理商

**💡 核心亮点更新 (中文)**：
- 由 8 月版本使用裸“自定义”提供商创建的桌面聊天可以在更新后再次发送（#156545）。
- 在待办事项或内存调用旁边流式传输的桌面或 TUI 回复现在会稳定下来，而不是保留“停止”按钮 (#156553)。
- Telegram 和其他编辑流聊天中的崩溃不再显示重复的“已恢复回复”；再次按时显示在单词中间包含键前缀的单词 (`program_id`) (#156546)。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# Hermes Agent v0.23.2

**Release Date:** November 16, 2026

> Patch release. This tag rolls up the ~1,989 PRs merged since v0.23.1 into a stable release for the GitHub release (CLI and installers), the Microsoft Store app, Docker and Hermes Cloud. Full curated notes for this window ship with v0.24.0.

<!-- HERMES_BUILDS_TABLE -->

## About this release

Measured at commit `ae2a81ccc00`, the window since v0.23.1 contains **7,918 non-merge commits** across **5,211 changed files** (+239,733 / −22,788), **1,989 merged PRs** and **940 closed issues**.

Also in the window, undocumented here on purpose: durable subagents that survive a gateway restart or crash and can be continued on their own conversation, one prompt-cache clock per session, `hermes fallback check` for fallback-chain readiness, `hermes update --force` to stop gateways at once instead of draining, one-time browser_vault codes entered from Telegram and Discord, opt-in shared Telegram DM threads, the Gemini Interactions API by default for Gemini 3 and later plus Gemini 4 Carbon, fast mode for Claude Mythos 5.2, per-job cron options (`wrap_response`, a fresh thread per run), new plugin APIs (`ctx.fork_session`, `ctx.redact_text()`, `ctx.register_idle_task`), compatibility shims so updates work across module moves, a slimmer macOS bundle that installs Chromium on first use, and a large batch of new plugin-catalog entries.

**Full curated release notes for this window ship with v0.24.0**, which will document everything
```
</details>

---
### 📦 [Makememo/MemoAI](https://github.com/Makememo/MemoAI)
`⭐ Stars: 1,082` &nbsp;|&nbsp; `💻 语言: Other` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.8.11](https://github.com/Makememo/MemoAI/releases/tag/v1.8.11) (2026-11-16)`

> **简介**：MemoAI 视频翻译文本、字幕和注释变得简单。

**💡 核心亮点更新 (中文)**：
- 添加了可拖动的播放间隙指示器，可快速查找字幕
- 添加了可搜索的字体选择器，具有预览、字体清除和更好的字形回退功能

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## New Features

- Added a draggable playback gap indicator with quick subtitle seeking
- Added a searchable font picker with previews, font clearing, and better glyph fallback

## Improvements

- Improved translation stability, progress tracking, and cancellation
- Updated provider models and JSON-based thinking configuration
```
</details>

---
### 📦 [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)
`⭐ Stars: 12,486` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.13.18](https://github.com/genspark-ai/genoffice/releases/tag/v0.13.18) (2026-11-12)`

> **简介**：免费的开源 AI Office 套件：带有内置 AI 代理的文档、表格、幻灯片、PDF、Markdown 和 HTML 编辑器，以及“genoffice”CLI 和代理技能，以便 Claude Code、Codex 和 Cursor 可以在本地创建和编辑真正的 .docx/.xlsx/.pptx 文件。带上你自己的钥匙。 macOS、Windows 和 Linux。

**💡 核心亮点更新 (中文)**：
- **幻灯片：** 旧版 PowerPoint 97-2003 `.ppt` 文件现在可以通过“打开”对话框、拖放、文件关联或 CLI 打开，作为可编辑的“.pptx”副本；转换在锚点处带有形状、纯色、渐变、图案和纹理填充、图片和 WMF/EMF 图稿、文本样式、项目符号和自动编号、制表位和缩进、轮廓、背景和母版/布局继承，并在 150 多个真实平台上对照 PowerPoint 进行检查；从 **文件 → 导出为视频 (MP4)…** 将演示文稿导出为 MP4 视频 — 包括幻灯片计时、过渡、动画和录制的旁白，1080p 或 720p，本地编码（由 要求）；带有幻灯片顺序选项的 4 和 9 合讲义；换行遵循运行语言，并找到 macOS 26 可下载字体；文本字距调整、制表位和 Office 字体查找与 PowerPoint 更匹配。
- **文档：** 另存为在 Word 旁边提供 PDF、HTML 和 Markdown；故事视图会在您写作时隐藏格式；从上下文菜单更新目录；在表格单元格上拖动可以选择其中的文本，;跟踪的更改到达内联对象，；打印作业说明文档的纸张尺寸； EMF+图片绘制其跳过记录；本地化的中日韩字体名称通过系统字体表解析；上下文子菜单保留在窗口内；在另外两个 100 个文档的比较中，表格、重复的标题、脚注、CJK 换行、阿拉伯语、孟加拉语和缺失字体替换的布局更接近 Word。
- **工作表：**切片器和时间线在保存过程中持续存在；使用跨工作簿范围选择器中断和更改外部链接的源；分隔导入流，显示进度并可以停止； x14条件格式可以删除，报告者；打印区域遵循重命名的工作表；打开后立即排序可以保持公式和共享公式组完整，； CSV/PDF导出和打印等待公式结果；从 Office 应用程序粘贴的图片在保存后仍然存在；工作簿打开速度更快；细胞环境 m

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
GenOffice v0.13.18 stable desktop installers. The headline of this release is legacy `.ppt` support: PowerPoint 97-2003 presentations open and convert to editable `.pptx`.

## What's New

- **Slides:** legacy PowerPoint 97-2003 `.ppt` files now open — from the Open dialog, drag and drop, file association or the CLI — as an editable `.pptx` copy (@tokg-venv); the conversion carries shapes at their anchors, solid, gradient, pattern and texture fills, pictures and WMF/EMF artwork, text styles, bullets and auto-numbering, tab stops and indents, outlines, backgrounds and master/layout inheritance, checked against PowerPoint on 150+ real decks; export a presentation as an MP4 video from **File → Export as Video (MP4)…** — slide timings, transitions, animations and recorded narration included, 1080p or 720p, encoded locally (requested by @mictienhung); 4- and 9-up handouts with a slide order option (@tokg-venv); line breaking follows the run's language and macOS 26 downloadable fonts are found (@gloomydumber); text kerning, tab stops and Office font lookup match PowerPoint more closely.
- **Docs:** Save As offers PDF, HTML and Markdown next to Word; a story view hides the formatting while you write (@tokg-venv); update the table of contents from its context menu (@aniruddhaadak80); a drag across table cells selects text across them (@aniruddhaadak80, @Xtzdd); tracked changes reach inline objects (@widechaos, @tokg-venv); print jobs state the document's paper size (@tokg-venv); EMF+
```
</details>

---
### 📦 [pascalorg/editor](https://github.com/pascalorg/editor)
`⭐ Stars: 25,569` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [@pascal-app/cli@1.1.4](https://github.com/pascalorg/editor/releases/tag/%40pascal-app/cli%401.1.4) (2026-11-12)`

> **简介**：适用于 AECO、扫描到 BIM 的开源 3D 建筑软件。代理友好、浏览器优先、MCP、CLI。

**💡 核心亮点更新 (中文)**：
`@pascal-app/cli@1.1.4` 的 Pascal Web 编辑器运行时。当命令第一次启动编辑器时，CLI 会下载“pascal-web-runtime-1.1.4.tar.gz”，并根据 npm 包内发布的摘要进行验证。离线安装可以通过t

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
The Pascal web editor runtime for `@pascal-app/cli@1.1.4`. The CLI downloads `pascal-web-runtime-1.1.4.tar.gz` the first time a command starts the editor and verifies it against the digest published inside the npm package. Offline installs can pass the archive directly: `pascal editor --runtime pascal-web-runtime-1.1.4.tar.gz`.
```
</details>

---
### 📦 [linshenkx/prompt-optimizer](https://github.com/linshenkx/prompt-optimizer)
`⭐ Stars: 41,782` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.15.2](https://github.com/linshenkx/prompt-optimizer/releases/tag/v2.15.2) (2026-11-09)`

> **简介**：人工智能提示优化器，用于编写更好的提示并获得更好的人工智能结果。

**💡 核心亮点更新 (中文)**：
- 读取长流响应和源视图，而不会出现水平溢出。
- 停止普通工作区和全屏视图中的单个文本流。
- 搜索和浏览花园灵感和竞技场评估提示到位。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## English

### Summary

This patch restores automatic wrapping and Stop controls for streaming output, updates two security-sensitive dependencies, and includes Garden browsing improvements and optional GPT Image 2.6 GIF output added since v2.15.1.

### Highlights

- Read long streamed responses and source views without horizontal overflow.
- Stop an individual text stream in ordinary workspaces and fullscreen views.
- Search and browse Garden inspiration and Arena evaluation prompts in place.
- Select GIF output for compatible GPT Image 2.6 endpoints while retaining PNG as the default.

### Product Updates

#### Desktop

- Apply the shared output, Garden browsing and image-output improvements.

#### Web

- Switch between recommended and all Garden prompts, search the catalog, load additional results and retry failed requests.
- Preserve browsing position and loaded results when closing and reopening the popover in the same workspace and language.

#### Extension

- Apply the shared output and Garden browsing improvements.

#### Core/Infra

- Preserve animated GIF data through image previews, storage and downloads. Compatible endpoints can use optional frame-count and frame-delay parameters.
- Pin Vue I18n to 11.4.14 and override transitive Hono Node Server to 2.1.3, including its MCP SDK dependency path.

### Fixes

- Enable CodeMirror line wrapping for streamed and read-only source output, including long paragraphs and URLs. Fixes [#374](https://github.com/linshenkx/prompt
```
</details>

---
### 📦 [RSSNext/Folo](https://github.com/RSSNext/Folo)
`⭐ Stars: 39,307` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [desktop/v1.18.0](https://github.com/RSSNext/Folo/releases/tag/desktop/v1.18.0) (2026-11-15)`

> **简介**：🧡 Folo 是人工智能 RSS 阅读器

**💡 核心亮点更新 (中文)**：
- 将文章保存到 Notion：在“设置”→“集成”中连接一个 Notion 集成，选择一个数据库并映射其字段；凭据保留在此设备上，不会同步到您的帐户
- 删除了日文和中文翻译从未使用的复数变体
- 修复了自动播放设置不适用于条目正文中嵌入的视频播放器的问题

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# What's new in v1.18.0

## Shiny new things

- Save articles to Notion: connect a Notion integration in Settings → Integrations, pick a database and map its fields; the credentials stay on this device and are not synced to your account

## Improvements

- Removed plural variants the Japanese and Chinese translations never use

## No longer broken

- Fixed the autoplay setting not applying to video players embedded in entry bodies
- Fixed keyboard shortcuts not switching entries in the Pictures and Videos views
- Fixed the profile menu shifting when the wallet loads
- Fixed the 2FA prompt reopening in a loop when deleting the account
- Fixed links on hosts other than t.me being treated as Telegram links
- Fixed the Chinese message for removing a feed from a list

## Thanks

Special thanks to volunteer contributors @Lucas-Fong, @amannn and @Dev-next-gen for their valuable contributions
```
</details>

---
### 📦 [roboflow/supervision](https://github.com/roboflow/supervision)
`⭐ Stars: 51,645` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [0.31.7](https://github.com/roboflow/supervision/releases/tag/0.31.7) (2026-11-11)`

> **简介**：我们为您编写可重复使用的计算机视觉工具。 💜

**💡 核心亮点更新 (中文)**：
- **MeanAveragePrecision** 使用 pycocotools 大小桶和 COCO 人群 IoU 来实现定向框人群目标。
- 当多边形坐标达到其整数限制时，**PolygonZone** 保持其完整遮罩。
- 关键点选择和 **CSVSink** 现在会根据他们过去默默误读的输入提出问题。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# v0.31.7: pycocotools-matching mAP, stricter key point and CSV inputs, and edge-case fixes for zones and dataset exports

A fixes-only patch: mAP now matches pycocotools more closely, and several zone, key point and export edge cases stop failing.

- **MeanAveragePrecision** uses pycocotools size buckets and the COCO crowd IoU for oriented-box crowd targets.
- **PolygonZone** keeps its full mask when polygon coordinates reach their integer limit.
- Key point selection and **CSVSink** now raise on inputs they used to silently misread.
- **DetectionDataset** exports keep box area for empty COCO masks and, with simplification on, bridge more mask holes.
- The OpenCV-free `contourArea` and `convertScaleAbs` fallbacks agree with OpenCV in more cases.

Drop-in upgrade, but check the Migration guide if you compare mAP values, pass extra CSV fields or select key points with boolean masks.

## ✨ Spotlights / highlights

### `MeanAveragePrecision` matches `pycocotools` more closely

`sv.metrics.MeanAveragePrecision` now puts objects in the small, medium and large buckets that `pycocotools` gives them: a prediction's own geometry (box, mask or oriented-box polygon) decides, and its `data["area"]` is ignored. Target `data["area"]` is read as float64, so an area such as `9216.0004` is no longer scored as both medium and large. With `MetricTarget.ORIENTED_BOUNDING_BOXES`, targets with `data["iscrowd"]` set use the COCO crowd IoU, so a prediction inside a crowd region is ig
```
</details>

---
### 📦 [MetaCubeX/mihomo](https://github.com/MetaCubeX/mihomo)
`⭐ Stars: 35,850` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.19.34](https://github.com/MetaCubeX/mihomo/releases/tag/v1.19.34) (2026-11-11)`

> **简介**：Honkai 的简单 Python Pydantic 模型：Star Rail 解析来自 Mihomo API 的数据。

**💡 核心亮点更新 (中文)**：
* 2d1a22e3 feat：支持多用户使用 Shadowsocks 监听器 (#3383) by Caesar
* f1f640b1 feat：添加 Snell 版本 6 支持（出站 + 入站）(#3410)
* ff179c43 feat: 将 ss 密码生成功能添加到命令行工具 (#3372)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## What's Changed
* 2d1a22e3 feat: support multiple users for shadowsocks listener (#3383) by @Romanov Caesar
* f1f640b1 feat: add Snell version 6 support (outbound + inbound) (#3410) by @YONG
* ff179c43 feat: add ss-password generation functionality to the command line tool (#3372) by @Zephyruso

## BUG & Fix
* 478af2a5 fix: auto route rules for tun by @wwqgtxx
* 5b79f3c3 fix: tfo-go not working on go1.26.9+ and go1.27.2+ by @wwqgtxx
* 6780eeeb fix: prevent SOCKS domain length arithmetic overflow (#3359) by @SaladDay
* 69c16319 fix: keep bytes that arrive with the HTTP proxy's CONNECT response (#3382) by @Gtio
* 9002a4fe fix: easytier drain unused host packets to prevent data-plane stalls (#3400) by @Chikage0o0
* b6a15182 fix: i386 struct define of PROCESS_MEMORY_COUNTERS by @wwqgtxx
* c3bdf779 fix: skip empty age secret key in DecryptBytes (#3450) by @Sloan Gray
* ca8d7c41 fix: ssh clients do not close when underlying connection writing errors by @wwqgtxx
* de439c88 fix: drain cached data before reading upstream by @wwqgtxx
* e9b9a1a8 fix: convert httpupgrade share links to ws with v2ray-http-upgrade (#3415) by @Aleksey Fedorov

## Maintenance
* 0455d0d2 chore: bump embedded easytier-go core to keep guest memory off the Go heap (#3454) by @MiaM1ku
* 91e85eeb chore: allow mieru inbound to actively close idle TCP connection (#3354) by @enfein
* 94666818 chore: code cleanup by @wwqgtxx
* f7ec2b9a chore: update utls to go1.26-based by @wwqgtxx

**Full Changelog**: https://githu
```
</details>

---
### 📦 [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev)
`⭐ Stars: 158,937` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.5.10](https://github.com/clash-verge-rev/clash-verge-rev/releases/tag/v2.5.10) (2026-11-03)`

> **简介**：基于 Tauri 的现代 GUI 客户端，设计用于在 Windows、macOS 和 Linux 中运行，以提供定制的代理体验

**💡 核心亮点更新 (中文)**：
- 修复全局模式缺少 `GLOBAL` 策略组，无法单独选择全局出口
- 修复服务模式下，SSH 节点的 `private-key` 使用私钥文件时内核无法启动
- 修复服务模式下，内核更新的 GEO 数据库不会同步回应用目录，导致使用新分类的规则无法通过校验

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## v2.5.10

<details>
<summary><strong> 🐞 修复问题 </strong></summary>

- 修复全局模式缺少 `GLOBAL` 策略组，无法单独选择全局出口
- 修复服务模式下，SSH 节点的 `private-key` 使用私钥文件时内核无法启动
- 修复服务模式下，内核更新的 GEO 数据库不会同步回应用目录，导致使用新分类的规则无法通过校验
- 修复订阅的 DNS 配置变化后，「DNS 覆写」实际已关闭但开关仍显示开启且没有提示

**🖥️ Windows**

- Windows：修复安装程序重新安装或覆盖时未提示退出运行中应用，导致卸载报错或覆盖失败

</details>

<details>
<summary><strong> ✨ 新增功能 </strong></summary>


</details>

<details>
<summary><strong> 🚀 优化改进 </strong></summary>


</details>

## 下载地址

### Windows (不再支持Win7)
#### 正常版本(推荐)
- [64位(常用)](https://github.com/clash-verge-rev/clash-verge-rev/releases/download/v2.5.10/Clash.Verge_2.5.10_x64-setup.exe) | [ARM64(不常用)](https://github.com/clash-verge-rev/clash-verge-rev/releases/download/v2.5.10/Clash.Verge_2.5.10_arm64-setup.exe)

#### 内置Webview2版(体积较大，仅在企业版系统或无法安装webview2时使用)
- [64位](https://github.com/clash-verge-rev/clash-verge-rev/releases/download/v2.5.10/Clash.Verge_2.5.10_x64_fixed_webview2-setup.exe) | [ARM64](https://github.com/clash-verge-rev/clash-verge-rev/releases/download/v2.5.10/Clash.Verge_2.5.10_arm64_fixed_webview2-setup.exe)

### macOS
- [Apple M芯片](https://github.com/clash-verge-rev/clash-verge-rev/releases/download/v2.5.10/Clash.Verge_2.5.10_aarch64.dmg) | [Intel芯片](https://github.com/clash-verge-rev/clash-verge-rev/releases/download/v2.5.10/Clash.Verge_2.5.10_x64.dmg)

### Linux
#### DEB包(Debian系) 使用 apt ./路径 安装
- [64位](https://github.com/clash-verge-rev/clash-verge-rev/releases/download/v2.5.10/Clash.Verge_2.5.10_amd64.deb) | [ARM64](htt
```
</details>

---
### 📦 [unslothai/unsloth](https://github.com/unslothai/unsloth)
`⭐ Stars: 79,663` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.1.918-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.918-beta) (2026-11-16)`

> **简介**：用于运行和训练法学硕士和扩散模型的本地 UI。支持 GGUF、MLX、Qwen3.8、DeepSeek-V4.1、MiniMax-H3、Gemma 4、FLUX 等。

**💡 核心亮点更新 (中文)**：
- **印迹：** 更改和交换 Qwen Flash 和 DeepSeek 的印迹。
- **计算机使用（测试版）：** 本地视觉模型和连接的提供商现在可以看到您的屏幕并与应用程序交互。默认关闭，有权限控制。
- **游戏引擎 + 创意应用程序：** 通过 MCP 连接 Unreal Engine、Unity、Godot 和 Roblox，以及 Blender。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
This update brings **computer use (beta)**, letting local models see your screen and interact with apps, plus MCP integrations for Unity, Unreal Engine, Blender and Roblox.

MiniMax-H3-Image now supports GGUF, FP8 and INT8, with LoRA training. We've also introduced a new model picker, redesigned Connections and improved project folders.

## Highlights

- **Engram:** Change and swap engrams for Qwen Flash and DeepSeek.
- **Computer use (beta):** Local vision models and connected providers can now see your screen and interact with apps. Off by default, with permission controls.
- **Game engines + creative apps:** Connect Unreal Engine, Unity, Godot and Roblox through MCP, alongside Blender.
- **MiniMax-H3-Image:** GGUF support for CPU, Mac and AMD, plus FP8 and INT8 weights for NVIDIA. LoRA training is also supported.
- **New model picker:** Switch models directly from the composer, with Favorites, On Device, Discover and Connected tabs.
- **Revamped Connections:** Live connection status, a redesigned provider gallery and 9 new providers.
- **Auto compaction:** Long conversations are automatically summarized, with configurable limits for each connection.
- **New project folders:** Browse project files, search folders and view Git changes from a redesigned Files tab.

## Computer Use (Beta)

Models can now see your screen and control the mouse and keyboard across macOS, Windows and Linux.

- Supports local GGUF, safetensors and MLX vision models, plus connecte
```
</details>

---
### 📦 [arc53/DocsGPT](https://github.com/arc53/DocsGPT)
`⭐ Stars: 18,374` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [1.1.0](https://github.com/arc53/DocsGPT/releases/tag/1.1.0) (2026-10-25)`

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
`⭐ Stars: 85,691` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.3.3](https://github.com/lobehub/lobehub/releases/tag/v2.3.3) (2026-11-12)`

> **简介**：🤯 LobeHub - 您团队中的超级代理。将超级代理添加到您的团队已使用的聊天中。他们自己承担工作，并且每周都会变得更好。

**💡 核心亮点更新 (中文)**：
- **直接渠道** — 每个客服人员和群组现在都有一个 IM 风格的对话界面：堆叠的标题头像、标题中的输入、带有“+”菜单的卡片编辑器、日期分隔符、列表行上的回复活动。 （＃22559，＃22583，＃22556，＃22440）
- **每个代理回复策略** - 每个代理决定何时唤醒：首先拥有自己的规则，后续保持沉默，未寻址的消息得到一个主要响应者，并且运行时记录唤醒发生的原因。 （＃22551，＃22454，＃22847）
- **代理身份和邮件** — 代理在身份组下获得地址、收件箱和个人资料页面；邮件唤醒运行将他们的结论发布回所有者的频道，并且只能看到他们自己的邮箱。 （#22009、#22010、#22578、#22686）

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Release v2.3.3

From PR #22891: https://github.com/lobehub/lobehub/pull/22891

# 🚀 LobeHub Release (20261112)

**Release Date:** November 12, 2026  
**Since v2.3.2:** 253 merged PRs · 252 commits · 12 contributors

> A week spent turning chat into a real workspace: direct Channels with their own reply rules, an inbox identity for every agent, and projects that can be created straight from a repository.

---

## ✨ Highlights

- **Direct Channels** — every agent and group now has an IM-style conversation surface: stacked header avatars, typing in the header, card composer with a `+` menu, day dividers, reply activity on list rows. (#22559, #22583, #22556, #22440)
- **Per-agent reply strategy** — each Agent decides when to wake: own rules first, follow-ups stay silent, unaddressed messages get one primary responder, and the runtime records why a wake happened. (#22551, #22454, #22847)
- **Agent identity & mail** — agents get an address, an inbox, and a Profile page under an Identity group; mail-woken runs post what they concluded back to the owner's Channel and only ever see their own mailbox. (#22009, #22010, #22578, #22686)
- **Projects from GitHub** — create a project from a repository, pick its work location, edit or remove working directories, and link tasks to projects with picker, badges and grouping. (#21552, #22612, #22725, #22383)
- **Knowledge base ordering** — natural prefix sorting, sort controls and drag-and-drop reordering, plus a caller-scoped business knowled
```
</details>

---
### 📦 [hiddify/hiddify-app](https://github.com/hiddify/hiddify-app)
`⭐ Stars: 34,095` &nbsp;|&nbsp; `💻 语言: Dart` &nbsp;|&nbsp; `🏷️ 最新版本: [v5.5.5](https://github.com/hiddify/hiddify-app/releases/tag/v5.5.5) (2026-11-04)`

> **简介**：多平台自动代理客户端，支持Sing-box、X-ray、TUIC、Hysteria、Reality、Trojan、SSH等。开源、安全、无广告。

**💡 核心亮点更新 (中文)**：
**根据您的操作系统下载：**

**根据您的操作系统下载：**

下载

<!-- 资产：开始 -->
<表>
<thead><tr><th>操作系统</th><th>下载</th><th>下载</th><th>VirusTotal</th></tr></thead>
<正文>
<tr>
  <td rowspan="4">安德烈

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
**Download based on your OS:**

**بر اساس سیستم عامل خود دانلود کنید:**

## Downloads

<!-- ASSETS:BEGIN -->
<table>
<thead><tr><th>OS</th><th>Download</th><th>Downloads</th><th>VirusTotal</th></tr></thead>
<tbody>
<tr>
  <td rowspan="4">Android</td>
  <td><a href="https://github.com/hiddify/hiddify-app/releases/download/v5.5.5/Hiddify-Android-universal.apk">APK Universal</a></td>
  <td><a href="https://github.com/hiddify/hiddify-app/releases/download/v5.5.5/Hiddify-Android-universal.apk"><img src="https://img.shields.io/github/downloads/hiddify/hiddify-app/v5.5.5/Hiddify-Android-universal.apk?displayAssetName=false&label=%20&color=green&v=17938308871725" alt="downloads"></a></td>
  <td><a href="https://www.virustotal.com/gui/file/d22cea2205863248c813d3a620dd1211d98ae2cb6e448f86deb5c191e9c6a992/detection"><img src="https://img.shields.io/badge/0%2F67-brightgreen" alt="VirusTotal"></a></td>
</tr>
<tr>
  <td><a href="https://github.com/hiddify/hiddify-app/releases/download/v5.5.5/Hiddify-Android-arm64.apk">APK ARMv8</a></td>
  <td><a href="https://github.com/hiddify/hiddify-app/releases/download/v5.5.5/Hiddify-Android-arm64.apk"><img src="https://img.shields.io/github/downloads/hiddify/hiddify-app/v5.5.5/Hiddify-Android-arm64.apk?displayAssetName=false&label=%20&color=green&v=17938308871725" alt="downloads"></a></td>
  <td><a href="https://www.virustotal.com/gui/file/d607fcbbb3566bc79dd8070979e74e5afed25f59c0643da950aae430a4260c0d/detection"><img src="https:/
```
</details>

---
### 📦 [labring/FastGPT](https://github.com/labring/FastGPT)
`⭐ Stars: 30,051` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v4.17.4](https://github.com/labring/FastGPT/releases/tag/v4.17.4) (2026-11-05)`

> **简介**：FastGPT 是一个建立在法学硕士基础上的知识平台，提供一整套开箱即用的功能，例如数据处理、RAG 检索和可视化 AI 工作流程编排，让您轻松开发和部署复杂的问答系统，无需进行大量设置或配置。

**💡 核心亮点更新 (中文)**：
- 更新 fastgpt-app（FastGPT 主服务）镜像 tag: v4.17.4
- 更新 fastgpt-pro（FastGPT 商业版）镜像 tag: v4.17.4

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 升级指南

### 镜像更新

- 更新 fastgpt-app（FastGPT 主服务）镜像 tag: v4.17.4
- 更新 fastgpt-pro（FastGPT 商业版）镜像 tag: v4.17.4

## ⚡ 优化

1. **[列表体验]** 优化列表滚动分页监听，减少滚动过程中的组件重渲染，提升滚动流畅度。

## 🐛 修复

1. **[对话体验]** 修复免登录分享对话中的全局变量、交互表单使用模型选择器时，未携带分享鉴权信息，导致模型列表或已选模型名称加载失败的问题。
2. **[对话体验]** 修复免登录分享对话顶部变量面板按普通对话规则展示变量的问题，外部变量不再向分享用户显示。
3. **[对话体验]** 修复免登录分享对话中删除消息、重试及编辑后发送失败的问题。
4. **[列表体验]** 修复部分列表在内容缩短后无法继续滚动加载、分页失败后仍自动重复请求的问题。
5. **[账号与团队]** 修复联系方式弹窗关闭按钮因正文滚动而偏移或被裁剪的问题。
6. **[账号与团队]** 修复登录和修改成员名时，使用中文输入法按回车确认候选词会误提交表单的问题；确认候选词后再次按回车可正常提交。
7. **[Agent]** 修复部分工作流工具在编辑器中配置正常，但运行时被错误过滤、无法调用的问题。
8. **[工具调用]** 修复工具参数 JSON Schema 格式不规范导致模型请求失败的问题。


**Full Changelog**: https://github.com/labring/FastGPT/compare/v4.17.3...v4.17.4
```
</details>

---
### 📦 [yihong0618/bilingual_book_maker](https://github.com/yihong0618/bilingual_book_maker)
`⭐ Stars: 9,944` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.3.2](https://github.com/yihong0618/bilingual_book_maker/releases/tag/v1.3.2) (2026-10-30)`

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
`⭐ Stars: 37,461` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.5.1](https://github.com/1Panel-dev/1Panel/releases/tag/v2.5.1) (2026-11-12)`

> **简介**：🔥 1Panel is a modern, open-source Linux server management panel and a lightweight AI management platform. 1Panel 是专门为 AI 服务器打造的管理面板。

**💡 核心亮点更新 (中文)**：
* 模型：添加了对连接外部 vLLM 实例并在概述中监控它们的支持 https://github.com/1Panel-dev/1Panel/pull/14402
* 模型：改进了 GPU 组卡布局和基于拓扑的排序，参见 https://github.com/1Panel-dev/1Panel/pull/14404
* 模型：改进了 vLLM 部署列表，并通过以下方式选择了图像拉取

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
[English](#en-v2.5.1) | [中文](#cn-v2.5.1)

<h3 id="en-v2.5.1">New Features</h3>

* Models: Added support for connecting external vLLM instances and monitoring them in Overview by @ssongliu in https://github.com/1Panel-dev/1Panel/pull/14402

### Enhancements

* Models: Improved GPU group card layouts and topology-based ordering by @ssongliu in https://github.com/1Panel-dev/1Panel/pull/14404
* Models: Improved the vLLM deployment list and made image pulling opt-in by @ssongliu

### Bug Fixes

* Models: Fixed issues with vLLM custom image synchronization and default image resets when switching versions by @ssongliu in https://github.com/1Panel-dev/1Panel/pull/14406
* Models: Fixed incorrect version matching for GB10 dual-node vLLM deployments and upgrades by @ssongliu in https://github.com/1Panel-dev/1Panel/pull/14407
* MCP Management: Fixed installation failures caused by a nonexistent default image version by @lan-yonghui in https://github.com/1Panel-dev/1Panel/pull/14411、https://github.com/1Panel-dev/1Panel/pull/14416
* Multi-Node: Fixed prerelease version handling during node upgrades by @ssongliu

<h3 id="cn-v2.5.1">新增功能</h3>

* 【模型】支持接入外部 vLLM 实例并纳入概览监控 by @ssongliu in https://github.com/1Panel-dev/1Panel/pull/14402

### 功能优化

* 【模型】优化 GPU 分组卡片布局并按拓扑排序 by @ssongliu in https://github.com/1Panel-dev/1Panel/pull/14404
* 【模型】优化 vLLM 部署列表展示并默认关闭镜像拉取选项 by @ssongliu

### 问题修复

* 【模型】修复了 vLLM 自定义镜像同步及版本切换时默认镜像重置异常的问题 by @ssongliu in https://github.com/1
```
</details>

---
### 📦 [invoke-ai/InvokeAI](https://github.com/invoke-ai/InvokeAI)
`⭐ Stars: 29,103` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v6.14.4](https://github.com/invoke-ai/InvokeAI/releases/tag/v6.14.4) (2026-11-03)`

> **简介**：Invoke 是一款领先的创意引擎，它使用图像和视频生成模型，使专业人士、艺术家和爱好者能够使用最新的人工智能驱动技术生成和创建视觉媒体。该解决方案提供了业界领先的应用程序接口，并作为多个商业产品的基础。

**💡 核心亮点更新 (中文)**：
* 修复（deps）：将 Starlette 限制在 1.8 以下，以保持 Web UI 在 https://github.com/invoke-ai/InvokeAI/pull/10132 中加载

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
This is a maintenance release of InvokeAI. It fixes a [startup crash](https://github.com/invoke-ai/InvokeAI/issues/10119) that occurred when upgrading from 6.14.2 to 6.14.3 caused by a bug in the Starlette library.

## What's Changed
* chore(version): bump to 6.14.3 by @lstein in https://github.com/invoke-ai/InvokeAI/pull/10073
* fix(deps): cap Starlette below 1.8 to keep the web UI loading by @lstein in https://github.com/invoke-ai/InvokeAI/pull/10132


**Full Changelog**: https://github.com/invoke-ai/InvokeAI/compare/v6.14.3...v6.14.4
```
</details>

---
### 📦 [The-Vibe-Company/quivr](https://github.com/The-Vibe-Company/quivr)
`⭐ Stars: 39,654` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.0.3](https://github.com/The-Vibe-Company/quivr/releases/tag/v2.0.3) (2026-11-16)`

> **简介**：一个开源引擎，可将连续的内容流转化为搜索和监控。持久摄取、混合搜索、警报以及格式、模型和业务规则的插件。

**💡 核心亮点更新 (中文)**：
- **Go 1.27.4** 构建每个 Quivr 二进制文件和图像（GO-2026-6859，在 `net/http` 中）。
- **PostgreSQL 17.12** 替换数据库映像中的 17.11。它附带 zlib 1.4 (CVE-2026-4738)。这是 PostgreSQL 的次要版本：磁盘上的数据保持原样。
- **SeaweedFS**，存储原始文件，获取 zlib 1.4 (CVE-2026-4738) 和 brotli v1.2.7 (GO-2026-6888)。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Quivr 2.0.3

2.0.3 is a security and fix release. It changes no API, no configuration and no stored data. Upgrade any 2.0.x installation to it.

### Security fixes

- **Go 1.27.4** builds every Quivr binary and image (GO-2026-6859, in `net/http`).
- **PostgreSQL 17.12** replaces 17.11 in the database image. It ships zlib 1.4 (CVE-2026-4738). This is a PostgreSQL minor release: the data on disk stays as it is.
- **SeaweedFS**, which stores original files, gets zlib 1.4 (CVE-2026-4738) and brotli v1.2.7 (GO-2026-6888).

### Fixed

- **Forms in the demo work over plain HTTP.**
  - **Before:** on an address other than HTTPS or localhost, adding a source, adding a text, creating an alert or editing a connector failed with « crypto.randomUUID is not a function ». Browsers offer that function only on secure pages.
  - **Now:** the demo makes its keys another way when the browser lacks it.
- **The demo's alerts use the alerts plugin version Quivr ships.** Before, a deployment with no setting asked for an older version, and the engine refused every alert as « not installed ».

### Upgrade from 2.0.x

Deploy the 2.0.3 images, or the 2.0.3 compose bundle attached to this release for a single machine. Restarting the database container on PostgreSQL 17.12 needs no dump or migration. The search database and Quivr's data stay as they are.

The release images are signed and carry SBOMs, as described in [Security of Quivr releases](https://docs.quivr.thevibecompany.co/run-quivr/security).
```
</details>

---
### 📦 [langgenius/dify](https://github.com/langgenius/dify)
`⭐ Stars: 161,348` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [1.19.0](https://github.com/langgenius/dify/releases/tag/1.19.0) (2026-11-04)`

> **简介**：在一个协作工作空间上构建 Agentic 工作流程、RAG 管道，并提供丰富的 AI 模型和工具支持。在云、VPC 或自托管上部署，因此团队无需重建堆栈即可从原型转向生产。

**💡 核心亮点更新 (中文)**：
- **遵循层次结构。** 展开称为“工作流程工具”以查看调用工具范围下的内部执行步骤。
- **了解每次调用。** 重复调用和失败保留其在跟踪中的位置。
- **保留 LLM 上下文。** 检查格式化的提示和响应、令牌使用以及项目、跟踪和观察链接。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
**Dify 1.19.0 brings nested workflow tracing to your observability tools.** Follow a workflow into the Workflow Tools it calls, inspect the steps inside each invocation, and keep the LLM context alongside the execution tree.

This release also makes Workflow Tools portable with App packages, adds Skill Hub automation, and makes Agent files easier to upload and preview. The bundled plugin daemon is upgraded to **0.6.14-local**.

[Release highlights](#user-content-release-highlights) · [Upgrade guide](#user-content-upgrade-guide) · [Detailed changes](#user-content-detailed-changes)

<a id="release-highlights"></a>

## Release highlights

### Nested workflow tracing

**See what happens inside a Workflow Tool, all the way down to its LLM calls.**

Building on the Console drilldown introduced in 1.18.0, new external traces now include the persisted execution steps inside called Workflow Tools. Child steps appear beneath the Tool span that invoked them, preserving the hierarchy across nested and repeated calls. (#44673)

![Langfuse trace tree showing a workflow, nested Middle and Child Workflow Tools, and the selected LLM call with formatted prompts and responses](https://raw.githubusercontent.com/langgenius/dify/dcfb52e62726c91b43db20f3c087acf285428df1/docs/assets/pr-44673-langfuse-nested-prompts.jpg)

*From the outer workflow to a nested LLM call: the execution tree and formatted messages, together in Langfuse. Screenshot from [#44673](https://github.com/langgen
```
</details>

---
### 📦 [nextai-translator/nextai-translator](https://github.com/nextai-translator/nextai-translator)
`⭐ Stars: 25,065` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.6.55](https://github.com/nextai-translator/nextai-translator/releases/tag/v0.6.55) (2026-11-02)`

> **简介**：基于 ChatGPT API 的划词翻译浏览器插件和跨平台桌面端应用    -    Browser extension and cross-platform desktop application for translation based on ChatGPT API.

**💡 核心亮点更新 (中文)**：
- Windows OCR：当英语是第一 Windows 显示语言时识别中文（以及其他已安装的 OCR 语言）；以前只返回数字和拉丁单词，或者什么也没有返回（#1902，#1950，谢谢
- Windows OCR：识别文本中每个中文/日文字符之间不再有空格 (#1950)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
v0.6.55

- Windows OCR: recognize Chinese (and other installed OCR languages) when English is the first Windows display language; previously only digits and Latin words came back, or nothing (#1902, #1950, thanks @zhouzhendiao)
- Windows OCR: no more spaces between every Chinese/Japanese character in recognized text (#1950)
```
</details>

---
### 📦 [langchain-ai/langchain](https://github.com/langchain-ai/langchain)
`⭐ Stars: 149,760` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [langchain-core==1.8.1](https://github.com/langchain-ai/langchain/releases/tag/langchain-core%3D%3D1.8.1) (2026-11-15)`

> **简介**：代理工程平台。

**💡 核心亮点更新 (中文)**：
自 langchain-core==1.8.0 以来的变化

版本（核心）：1.8.1（41855）
杂务（deps）：将 /libs/core 中的 soupsieve 从 4.0 提升到 4.1 (41850)
feat(core)：通过 `langsmith_gateway` 覆盖每个上下文 LangSmith 网关 (41836)
杂务（deps）：从 2 开始碰撞汤筛。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Changes since langchain-core==1.8.0

release(core): 1.8.1 (#41855)
chore(deps): bump soupsieve from 4.0 to 4.1 in /libs/core (#41850)
feat(core): per-context LangSmith gateway override via `langsmith_gateway` (#41836)
chore(deps): bump soupsieve from 2.9 to 4.0 in /libs/core (#41833)
```
</details>

---
### 📦 [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)
`⭐ Stars: 188,072` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [autogpt-platform-beta-v0.11.3](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.11.3) (2026-11-15)`

> **简介**：AutoGPT 的愿景是为每个人提供易于使用和构建的人工智能。我们的使命是提供工具，以便您可以专注于重要的事情。

**💡 核心亮点更新 (中文)**：
- **#15384** - 添加本机移动服务器基础（通过
- **#16683** - 支持本机和浏览器使用 Apple 登录（通过
- **#16677** - 让奥托用视觉卡回答（通过

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# 🚀 Release `autogpt-platform-beta-v0.11.3`

**Date:** November 15, 2026

---

## 🔒 Security

This release fixes several privately reported security issues. We'll publish the advisories once the fixes are live in production.

---

## 🔥 What's New?

### New Features

- **#15384** - Add native mobile server foundations (by @ntindle)
- **#16683** - Support native and browser Sign in with Apple (by @ntindle)
- **#16677** - Let Otto answer with visual cards (by @0ubbe)
- **#16768** - Close and erase an account without the confirmation email (erase-account --no-email) (by @kcze)
- **#16767** - One-off to delete bucket folders of deleted accounts (by @kcze)
- **#16688** - Reset an expert to how it arrived (by @Bentlybro)
- **#16792** - Add Gemini 4 Hydrogen support (by @ntindle)
- **#16741** - Add Gemini 4 Carbon support (by @ntindle)
- **#16791** - Show every expert's chats in the sidebar with real counts and per-expert paging (by @ntindle)
- **#13050** - Add remote Local PC execution targets (by @ntindle)
- **#16793** - Open account deletion to every user (SECRT-3488) (by @kcze)

### Enhancements

- **#16711** - Show a stone expert in the thinker's colour while thinking (by @0ubbe)
- **#16387** - Label Otto's Team card stats as the team's totals (by @Pwuts)
- **#16727** - Stream workspace downloads, profile continuously, make cache metrics admin-only (by @Pwuts)

### Bug Fixes

- **#14226** - Isolate billing state across account switches (by @ntindle)
- **#15440** - Self-host auth
```
</details>

---
### 📦 [rockbenben/ChatGPT-Shortcut](https://github.com/rockbenben/ChatGPT-Shortcut)
`⭐ Stars: 8,956` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v4.5.2](https://github.com/rockbenben/ChatGPT-Shortcut/releases/tag/v4.5.2) (2026-11-04)`

> **简介**：Stop writing prompts from scratch — a searchable prompt library for ChatGPT, Claude, Gemini and Cursor · Русский 한국어 العربية हिन्दी ไทย ｜ 别再从头写提示词：现成的拿来就用，好用的收进自己的库

**💡 核心亮点更新 (中文)**：
**完整变更日志**：https://github.com/rockbenben/ChatGPT-Shortcut/compare/v4.5.1...v4.5.2

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
**Full Changelog**: https://github.com/rockbenben/ChatGPT-Shortcut/compare/v4.5.1...v4.5.2
```
</details>

---
### 📦 [pionxzh/chatgpt-exporter](https://github.com/pionxzh/chatgpt-exporter)
`⭐ Stars: 2,892` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [userscript-v2.38.3](https://github.com/pionxzh/chatgpt-exporter/releases/tag/userscript-v2.38.3) (2026-11-04)`

> **简介**：导出并分享您的 ChatGPT 对话历史记录

**💡 核心亮点更新 (中文)**：
* 返回到 jszip 3.9.1，以便 zip 导出在用户脚本沙箱中完成 ([2e9b8e9](https://github.com/pionxzh/chatgpt-exporter/commit/2e9b8e9bdd4ddf6b19c6d407f22abd068f0f06a8))，关闭[#419](https://github.com/pionxzh/chatgpt-exporter/issues/419)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## [2.38.3](https://github.com/pionxzh/chatgpt-exporter/compare/userscript-v2.38.2...userscript-v2.38.3) (2026-11-04)


### Bug Fixes

* go back to jszip 3.9.1 so zip exports finish in the userscript sandbox ([2e9b8e9](https://github.com/pionxzh/chatgpt-exporter/commit/2e9b8e9bdd4ddf6b19c6d407f22abd068f0f06a8)), closes [#419](https://github.com/pionxzh/chatgpt-exporter/issues/419)
```
</details>

---
### 📦 [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent)
`⭐ Stars: 47,970` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [2.2.2](https://github.com/zhayujie/CowAgent/releases/tag/2.2.2) (2026-10-30)`

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
`⭐ Stars: 2,536` &nbsp;|&nbsp; `💻 语言: Shell` &nbsp;|&nbsp; `🏷️ 最新版本: [20261108](https://github.com/lxhao61/integrated-examples/releases/tag/20261108) (2026-11-08)`

> **简介**：以 Nginx 或 Caddy(v2 版) 配合 V2Ray(v4 版) 或 Xray、Caddy(v2 版) 加专用插件、Hysteria 等打造常用科学上网的优化配置及最优组合示例，且提供集成特定插件的 Caddy(v2 版) 文件，分享给大家食用及自己备份。

**💡 核心亮点更新 (中文)**：
以 Caddy 发行版 v2.11.9 源码加插件 forwardproxy、caddy-trojan、caddy-webdav、caddy-cloudflare-ip、caddy-trusted-cloudfront、caddy-dns/cloudflare、caddy-dns/duckdns、caddy-dns/tencentcloud、caddy-events-exec、caddy-l4、jsonc-adapter 基于稳定版 go1.27.3 定制编译而成，其额外应用及特点如下：
1、

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
以 Caddy 发行版 v2.11.9 源码加插件 forwardproxy、caddy-trojan、caddy-webdav、caddy-cloudflare-ip、caddy-trusted-cloudfront、caddy-dns/cloudflare、caddy-dns/duckdns、caddy-dns/tencentcloud、caddy-events-exec、caddy-l4、jsonc-adapter 基于稳定版 go1.27.3 定制编译而成，其额外应用及特点如下：
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
`⭐ Stars: 22,431` &nbsp;|&nbsp; `💻 语言: Shell` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.5.41](https://github.com/mack-a/v2ray-agent/releases/tag/v3.5.41) (2026-11-09)`

> **简介**：Xray、Tuic、hysteria2、sing-box 八合一一键脚本

**💡 核心亮点更新 (中文)**：
fix(脚本): 修复 Hysteria2 端口跳跃、订阅配置及 Geo 更新问题

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
fix(脚本): 修复 Hysteria2 端口跳跃、订阅配置及 Geo 更新问题
```
</details>

---
### 📦 [electerm/electerm](https://github.com/electerm/electerm)
`⭐ Stars: 15,653` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v5.11.8](https://github.com/electerm/electerm/releases/tag/v5.11.8) (2026-11-16)`

> **简介**：📻免费开源终端/ssh/sftp/ftp/telnet/串口/RDP/VNC/Spice客户端(Linux, Mac, Windows, Android, HarmonyOS, iOS)

**💡 核心亮点更新 (中文)**：
- 为 AI 代理添加过滤书签导出工具 (#4728)
- 记住两次访问之间的小部件表单值 (#4725)
- #4717 当整个端口窗口被阻止时回退到随机端口 (#4720)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
### Major updates

- Serial: new session toolbar for serial tabs: DTR/RTS/break control, CTS/DSR/DCD status LEDs, ascii/hex/dec/bin views and raw hex/dec/bin/ascii send (#4680) (by @mkneppe)
- Add per-bookmark custom server watchers (#4730)
- Rename a file by clicking it again when it is already selected (#4729)
- Add a column value filter to the remote monitor detail tables (#4723)
- Rewrite widget API

### New features/UI/Updates

- Add a filtered bookmark export tool to the AI agent (#4728)
- Remember widget form values between visits (#4725)
- #4717 Fall back to random ports when the whole port window is blocked (#4720)
- Improve app init speed
- Improve code split

### Bug fixes

- fix(terminal): start local shell in the bookmark directory and open ctrl+clicked local paths (#4737) (by @mkneppe)
- fix(ai): never run a tool call whose arguments were cut off
- fix(ai): show the provider error body for failed streaming chat requests (by @pcbeingused333)
- fix(ai): report an empty response.incomplete in the Responses stream (by @pcbeingused333)
- fix(ai): refuse an Anthropic tool call cut off by max_tokens (by @pcbeingused333)
- Fix UI when the right panel is pinned (#4735)
- Resolve web urls through the host's sub-path helper (#4721)
- Keep the pinned right panel header clear of the Windows caption buttons (#4724)
- Fix tab close button hit area (#4718) (by @forever765)
- Fix terminal search performance, avoid stuck

-----

### 重大更新

- 串口：新增串
```
</details>

---
### 📦 [pymumu/smartdns](https://github.com/pymumu/smartdns)
`⭐ Stars: 11,423` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [Release48.5-RC1](https://github.com/pymumu/smartdns/releases/tag/Release48.5-RC1) (2026-11-09)`

> **简介**：A local DNS server to obtain the fastest website IP for the best Internet experience, support DoT, DoH, DoQ. 一个本地DNS服务器，获取最快的网站IP，获得最佳上网体验，支持DoH，DoT，DoQ。

**💡 核心亮点更新 (中文)**：
* 修复（conf）：在 https://github.com/pymumu/smartdns/pull/2497 中为 server-http3 保留 HTTP/3，并使用 https:// URL

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 更新内容 
* 修复HTTP2，HTTP3协议相关的BUG
* 修改一些crash问题。

## What's Changed
* fix(conf): keep HTTP/3 for server-http3 with an https:// URL by @Dv2Corn in https://github.com/pymumu/smartdns/pull/2497

## New Contributors
* @Dv2Corn made their first contribution in https://github.com/pymumu/smartdns/pull/2497


**欢迎参与贡献**：https://github.com/pymumu/smartdns/issues/1918
**贡献请加QQ群**：1033365479

smartdns帮助文档：https://pymumu.github.io/smartdns/
非静态版本下载：https://github.com/PikuZheng/smartdns/releases/
APK包安装方法：https://pymumu.github.io/smartdns/install/openwrt/

**Full Changelog**: https://github.com/pymumu/smartdns/compare/Release48.4...Release48.5-RC1
```
</details>

---
### 📦 [XTLS/Xray-core](https://github.com/XTLS/Xray-core)
`⭐ Stars: 42,966` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v26.11.9](https://github.com/XTLS/Xray-core/releases/tag/v26.11.9) (2026-11-09)`

> **简介**：X射线，穿透一切。也是最好的 v2ray 核心。魔法发生的地方。适合多种用途的开放平台。

**💡 核心亮点更新 (中文)**：
- **TRX(Tron)/USDT/USDC: `TNrDh5VSfwd4RPrwsohr6poyNTfFefNYan`**
- **TON：`UQApeV-u2gm43aC1uP76xAC1m6vCylstaN1gpfBmre_5IyTH`**
- **BTC：`1JpqcziZZuqv3QQJhZGNGBVdCBrGgkL6cT`**

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
### [XDRIVE transport: Release notes & more optimizations for the Google Drive backend](https://github.com/XTLS/Xray-core/pull/7352)

### [Chrome 155+ fingerprint by default, untargeted by TSPU yet](https://github.com/XTLS/Xray-core/issues/7259#issuecomment-6733195752)

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
- **SOL/USDT/USDC: `3x5NuXHzB5APG6vRinPZcsUv5uk
```
</details>

---
### 📦 [klzgrad/naiveproxy](https://github.com/klzgrad/naiveproxy)
`⭐ Stars: 9,653` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [v154.0.8037.49-5](https://github.com/klzgrad/naiveproxy/releases/tag/v154.0.8037.49-5) (2026-10-22)`

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

## <span id="-效率办公与创作">📝 效率办公与创作</span>

### 📦 [Trulsaa/obsidian-icloud-contacts](https://github.com/Trulsaa/obsidian-icloud-contacts)
`⭐ Stars: 35` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [0.4.22](https://github.com/Trulsaa/obsidian-icloud-contacts/releases/tag/0.4.22) (2026-11-01)`

> **简介**：Obsidian 插件，可从 iCloud 导入联系人并管理每个联系人的注释。

**💡 核心亮点更新 (中文)**：
该版本未提供详细更新说明。

---
### 📦 [ufebri/ray-vault-sync](https://github.com/ufebri/ray-vault-sync)
`⭐ Stars: 3` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [1.4.0](https://github.com/ufebri/ray-vault-sync/releases/tag/1.4.0) (2026-11-08)`

> **简介**：为您的 Obsidian 保管库轻松、免费、跨设备 GitHub 同步。

**💡 核心亮点更新 (中文)**：
* 壮举：通过 https://github.com/ufebri/ray-vault-sync/pull/12 强化同步并添加新鲜度状态

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## What's Changed
* feat: harden sync and add freshness status by @ufebri in https://github.com/ufebri/ray-vault-sync/pull/12


**Full Changelog**: https://github.com/ufebri/ray-vault-sync/compare/1.3.0...1.4.0
```
</details>

---
### 📦 [huamidev/GestaltX](https://github.com/huamidev/GestaltX)
`⭐ Stars: 7,978` &nbsp;|&nbsp; `💻 语言: Swift` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.1.1](https://github.com/huamidev/GestaltX/releases/tag/v1.1.1) (2026-11-13)`

> **简介**：适用于 iOS 27.x 的 MobileGestalt 编辑器，具有区域代码调整、设备预设、备份功能。

**💡 核心亮点更新 (中文)**：
- 应用程序音频库：用自定义音频替换通知声音。列表中未显示的应用程序可以使用捕获指南来获取其通知声音路径。
- 配对和设备连接：用于获取所需路径。
- 不区分大小写的缓存 UUID 比较 (#131)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
English | [简体中文](https://github.com/huamidev/GestaltX/blob/main/CHANGELOG_ZH-CN.md)

Build `11140102`.

### Added

- App Audio Library: replace notification sounds with custom audio. Apps not shown in the list can use the capture guide to obtain their notification-sound paths.
- Pairing & Device Connection: used to obtain required paths.

### Changed

- Case-insensitive cache UUID comparison (#131)
- Reject trailing text in date fields (#132)
- Share-inbox fallback (#133)
- Validate backup metadata filenames (#134)
- Reduce cache descriptor string-scan allocations (#135)
- Reuse one preview snapshot for field search (#136)
- Preserve field edits over layout presets (#137)
- Preserve existing plist keys when editing fields (#138)
- Reduce allocations in exact plist comparisons (#139)
- Traverse document differences once (#140)
- Fix Face ID failing after enabling Apple Intelligence (#128)
- Add missing localization for #128 (#146)
- Pairing paths are migrated when a reinstall moves the app data container.

### Fixed

- Fix pairing failure in side-loaded release builds.
- Add the missing Face ID recovery localization strings.
- Fix audio file selection in side-loaded builds.
- Refresh captured sounds immediately and cache the app audio list.
- Show LocalDevVPN guidance and stop capture when the tunnel does not connect.
```
</details>

---
### 📦 [RongleCat/grok-bot-anywhere](https://github.com/RongleCat/grok-bot-anywhere)
`⭐ Stars: 68` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.1.5](https://github.com/RongleCat/grok-bot-anywhere/releases/tag/v0.1.5) (2026-11-13)`

> **简介**：Grok Bot Anywhere：带有 macOS 原生 Composer 和动态微信共享目的地的 Electron 桌面客户端

**💡 核心亮点更新 (中文)**：
- 设置 → 常规 支持添加多个 Grok Bot 账号，每个账号可勾选/取消勾选。
- 勾选账号的 Bot 会合并到主界面侧栏；多个勾选账号时先按账号分组，再在账号内应用原来的「分组模式」。
- 只有一个勾选账号时保持原来的单账号结构，不显示账号头。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# Grok Bot Anywhere 0.1.5 更新说明

状态：Current。发布日期：2026-11-13。

0.1.5 是一次结构性更新：GBA 开始支持多个 Grok Bot 账号；微信分享菜单增加「保存到本地」；CLI 改为通过本机 API 复用 GBA 多账号，旧的静态凭据 CLI 已被替换。

## 下载

| 平台 | 文件 |
| --- | --- |
| macOS Apple Silicon（M1–M4） | `Grok Bot Anywhere-0.1.5-arm64.dmg` |
| macOS Intel | `Grok Bot Anywhere-0.1.5.dmg` |
| Windows 10/11 x64 | `Grok Bot Anywhere-0.1.5-win.zip` |

macOS 两个 DMG 由 CI 做 Developer ID 签名、公证和 stapler。Windows zip 仍未签名；SmartScreen/SAC 可能拦截，需要自行解除锁定或用你的证书签名。

## 多账号

- 设置 → 常规 支持添加多个 Grok Bot 账号，每个账号可勾选/取消勾选。
- 勾选账号的 Bot 会合并到主界面侧栏；多个勾选账号时先按账号分组，再在账号内应用原来的「分组模式」。
- 只有一个勾选账号时保持原来的单账号结构，不显示账号头。
- 每个账号的凭据单独加密保存在 `accounts/<id>.enc`；旧单账号 `account.enc` 会在首次成功连接后迁移。
- 分享菜单、收件箱、通知、Explorer 菜单、原生伴侣、深链和发送路由都带账号作用域；单个账号断开或移除不会影响其他账号。
- 同名 Bot/分组按账号隔离，不再跨账号互相隐藏。

## 微信「保存到本地」

- 设置 → 分享菜单新增「保存到本地」开关。
- 开启后微信分享菜单多一项「保存到本地」；支持默认位置或每次打开目录选择器，选择器默认从上次目录开始。
- 单文件直接保存，多文件放进时间戳子目录，纯文字存 `.txt`，同名文件自动加序号，不覆盖。
- 只对微信转发生效；不创建 receipt、不进入发送记录、不投递 Bot。
- 开启保存后 Bot 菜单槽上限为 11，保存项占第 12 行。
- 受 macOS 分享扩展限制，Finder 里也可能出现该入口；从 Finder 点击会被拒绝。该限制需要在后续版本用前台 App 动态启停进一步收紧。

## CLI 与本地 API

- 新增本地 API：主进程监听本机 socket，CLI 通过 `userData/local-api.token` 鉴权，不保存明文凭据。
- 新增 `gba` 命令行；`grok-bot` 现在是 `gba` 的别名，旧的 0.3.0 静态 CLI 与 `profiles/default.json` 已移除。
- 当前开放 38 个方法：账号、Bot、recipient、收件、发送/等待、runtime、分享菜单、设置等；详见 `docs/subsystems/local-api.md`。
- Skill 仅保留 gba 内容；Agent 调用时使用 `gba` 或 `grok-bot`，并始终加 `--json`。
- 交互式 zsh 里 `gba` 可能被 Git 别名 `git branch --all` 抢占；用 `grok-bot`
```
</details>

---
### 📦 [JamesQiu2005/SpektraLab](https://github.com/JamesQiu2005/SpektraLab)
`⭐ Stars: 1,895` &nbsp;|&nbsp; `💻 语言: Swift` &nbsp;|&nbsp; `🏷️ 最新版本: [spektralab-v2.4.1](https://github.com/JamesQiu2005/SpektraLab/releases/tag/spektralab-v2.4.1) (2026-11-16)`

> **简介**：SpektraLab — macOS 电影和打印模拟器。 SwiftUI 应用程序 + Metal/C++ 渲染引擎，链接进来，运行时没有 Python。 andreavolpato/spektrafilm 的一个分支。

**💡 核心亮点更新 (中文)**：
- **Watermarks (水印)**: keep your signature or logo as a PNG with a transparent background in **Settings › Watermarks**, and place one on a photograph from the Layers panel's **＋ › Watermark**. A watermark sits on the **Finished** picture (over the print, untouched by the film) or on the **Negative** (laid into the scene before the film, so the film develops it with the photograph, grain and all).拖动它来移动它，拖动它的点来转动它（**⇧** 为 15° 步长），并用您自己的颜色填充它。它绘制在画布上并写入每个导出的文件中，包括 HDR。
- **Cine formats (电影)**: **Format › Cine** has **Super 8**, **16mm**, **35mm** cine, **70mm** and **70mm 15-perf**, each with its own frame, perforations and frame lines.
- **柯达 Portra 160NC、160VC、400NC 和 400VC**，色彩自然、生动的 Portras，具有自己的胶片边缘。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
SpektraLab 2.4.1 for the Mac.

- **Watermarks (水印)**: keep your signature or logo as a PNG with a transparent background in **Settings › Watermarks**, and place one on a photograph from the Layers panel's **＋ › Watermark**. A watermark sits on the **Finished** picture (over the print, untouched by the film) or on the **Negative** (laid into the scene before the film, so the film develops it with the photograph, grain and all). Drag it to move it, drag its dot to turn it (**⇧** for 15° steps), and fill it with a colour of your own. It is drawn on the canvas and written into every exported file, HDR included.
- **Cine formats (电影)**: **Format › Cine** has **Super 8**, **16mm**, **35mm** cine, **70mm** and **70mm 15-perf**, each with its own frame, perforations and frame lines.
- **Kodak Portra 160NC, 160VC, 400NC and 400VC**, the natural- and vivid-colour Portras, with their own film edge.
- **Light Leak (漏光)**: **Shuffle** (the dice) gives the photograph a new leak with each press, and **Camera's Own** in its menu goes back; **Spot** now works on every format; and **Edge Burn** (边缘漏光), light fogging the film's edge, sits beside the leak's kind with its own switch and strength.
- **Film and Paper as grids**: the stock browser shows half-size cards in columns under each maker's name, each strip as tall as you drag it. **Favourite** a film or paper from its card, and your **Favourites** shelf comes first. **No Paper** is always offered, first on the paper strip.
- **Copy Settings
```
</details>

---
### 📦 [robbietilton/Compositor](https://github.com/robbietilton/Compositor)
`⭐ Stars: 18,717` &nbsp;|&nbsp; `💻 语言: Swift` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.6.10](https://github.com/robbietilton/Compositor/releases/tag/v1.6.10) (2026-11-17)`

> **简介**：适用于 Mac 的 Photoshop 替代品

**💡 核心亮点更新 (中文)**：
- 更大的拖动区域可以更轻松地将图层和文件夹拖动到图层面板中的第一个插槽
- 拖放文件夹底部的图层：放开文件夹最后一层下方间隙的上半部分，将其放入内部，或放开下半部分，将其放入外部
- 下降线缩进以显示图层将放置在哪个文件夹中

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
- Larger drag area to allow easier dragging of layers and folders to first slot in layer panel
- Drag and drop a layer at the bottom of a folder: let go in the upper half of the gap under the folder's last layer to put it inside, or the lower half to put it outside
- The drop line indents to show which folder a layer will land in
- A dragged layer is see-through, so you can see the list under it
- A dragged layer stays full size as it leaves the Layers panel and comes back
- New Canvas remembers the last size you used
```
</details>

---
### 📦 [jgraph/drawio-desktop](https://github.com/jgraph/drawio-desktop)
`⭐ Stars: 64,036` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v32.6.10](https://github.com/jgraph/drawio-desktop/releases/tag/v32.6.10) (2026-11-04)`

> **简介**：Draw.io 的官方电子版本

**💡 核心亮点更新 (中文)**：
- 使用电子44.10.2
- 使用 --all-pages -f svg 将所有页面导出为一个 SVG，并包含每个页面的视图，以便图像中的 file.svg#Page-2 显示第二页 [jgraph/drawio#5821]
- 阻止命令行导出挂在格式错误的 PNG 文件上

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Release Notes for 32.6.10

[Windows Installer](https://github.com/jgraph/drawio-desktop/releases/download/v32.6.10/draw.io-32.6.10-windows-installer.exe)
[Windows No Installer (zip)](https://github.com/jgraph/drawio-desktop/releases/download/v32.6.10/draw.io-32.6.10-windows.zip)
[macOS - Universal](https://github.com/jgraph/drawio-desktop/releases/download/v32.6.10/draw.io-universal-32.6.10.dmg)
Linux - [deb](https://github.com/jgraph/drawio-desktop/releases/download/v32.6.10/drawio-amd64-32.6.10.deb), [AppImage](https://github.com/jgraph/drawio-desktop/releases/download/v32.6.10/drawio-x86_64-32.6.10.AppImage) or [rpm](https://github.com/jgraph/drawio-desktop/releases/download/v32.6.10/drawio-x86_64-32.6.10.rpm)

**ChangeLog:**

- Uses electron 44.10.2
- Exports all pages as one SVG with --all-pages -f svg, with a view for each page, so that file.svg#Page-2 in an image shows the second page [jgraph/drawio#5821]
- Stops the command line export from hanging on malformed PNG files
- Updates to [draw.io core 32.6.10](https://github.com/jgraph/drawio/blob/v32.6.10/ChangeLog). All changes from 32.6.1 to 32.6.10 are added in this build.

**Testing:**

Verified against the packaged, signed macOS build. Windows and Linux packages were verified from the produced release artifacts, their sizes and update manifests, rather than by running them.

Base checks

- Launch, open a file passed on the command line, add and edit shapes, change styles, undo and redo, copy a
```
</details>

---
### 📦 [Stirling-Tools/Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF)
`⭐ Stars: 96,822` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.3.0](https://github.com/Stirling-Tools/Stirling-PDF/releases/tag/v3.3.0) (2026-11-05)`

> **简介**：GitHub 上排名第一的 PDF 应用程序，可让您在任何地方的任何设备上编辑 PDF

**💡 核心亮点更新 (中文)**：
Stirling Office Convert（仍为测试版）已升级。您现在还可以选择它作为许多其他工具的转换器，例如电子邮件、HTML、Markdown 和电子书到 PDF 以及 PDF 到 HTML/Markdown/XML/EPUB/AZW3 和 PDF/A。请与前任比较一下

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Stirling Office Convert (still beta) has been upgraded. You can also now pick it as the converter in lots of other tools such as Email, HTML, Markdown and ebooks to PDF plus PDF to HTML/Markdown/XML/EPUB/AZW3, and PDF/A. Please compare it with the existing converter and let us know!

Our roadmap is to turn Office Convert on by default next week, and then, if no changes are required, fully remove LibreOffice and other dependencies the week after. So now is the best time to try it and report (And send example files) any conversions that don't look correct!

Other changes are:
- SSO auto-login now works even when username/password login is enabled (admins can still reach the password form via /login?all)
- JPDFium upgrade and support and Windows ARM64 support, This update also brings better redaction, merge/split improvements and lower memory on big files 
- Faster and more accurate mobile scanning, with no more 9MB OpenCV bundled
- Faster requests with far fewer database reads and new entity caching
- Quieter startup and runtime logs
- Spring Boot, Docker base image and lots of other dependency updates
- Updated translations for all languages

We also fixed some bugs including
- Convert sending multiple or mixed file uploads to the wrong conversion
- Ebook settings resetting the selected output format
- "Include all recipients" not controlling CC/BCC in email to PDF
- PDF/UA font embedding making form fields no longer fillable
- Certificate signing rejecting u
```
</details>

---
### 📦 [halo-dev/halo](https://github.com/halo-dev/halo)
`⭐ Stars: 40,318` &nbsp;|&nbsp; `💻 语言: Java` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.27.3](https://github.com/halo-dev/halo/releases/tag/v2.27.3) (2026-11-13)`

> **简介**：Halo 是一款强大易用的开源建站工具，从个人博客、知识库，到企业官网、在线商城，Halo 都能助您轻松实现，一站式满足您的多样化建站需求。

**💡 核心亮点更新 (中文)**：
- 自动清理不再使用的邮箱验证、邮箱登录、安全确认及密码重置通知订阅，避免历史记录长期累积 by  in #10490
- 修复了已知安全问题
- 修复导入或创建文章时作者为空可能导致发布超时的问题 by  in #10457

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
**此版本包含安全更新，建议所有用户尽快升级。**

## 功能优化

- 自动清理不再使用的邮箱验证、邮箱登录、安全确认及密码重置通知订阅，避免历史记录长期累积 by @ruibaby in #10490

## 问题修复

- 修复了已知安全问题
- 修复导入或创建文章时作者为空可能导致发布超时的问题 by @ruibaby in #10457
- 修复控制台和用户中心中复选框选中后仍显示灰色边框的问题 by @ruibaby in #10475
- 修复主题端评论列表按创建时间排序时请求失败的问题 by @ruibaby in #10476
- 修复系统初始化中断后无法继续完成的问题，支持重新进入初始化页面继续执行 by @ruibaby in #10488

## 依赖更新

- 升级 Thymeleaf 至 3.1.6.RELEASE by @ruibaby in #10462
- 更新部分前端依赖 by @ruibaby in #10450

**Full Changelog**: https://github.com/halo-dev/halo/compare/v2.27.2...v2.27.3
```
</details>

---
### 📦 [zyx0814/dzzoffice](https://github.com/zyx0814/dzzoffice)
`⭐ Stars: 4,057` &nbsp;|&nbsp; `💻 语言: PHP` &nbsp;|&nbsp; `🏷️ 最新版本: [2.4.2](https://github.com/zyx0814/dzzoffice/releases/tag/2.4.2) (2026-10-22)`

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
`⭐ Stars: 4,812` &nbsp;|&nbsp; `💻 语言: C#` &nbsp;|&nbsp; `🏷️ 最新版本: [4.16.11-Installer](https://github.com/emoacht/Monitorian/releases/tag/4.16.11-Installer) (2026-11-08)`

> **简介**：轻松调节多台显示器亮度的 Windows 桌面工具

**💡 核心亮点更新 (中文)**：
- 补充俄语 (ru-RU) 和乌克兰语 (uk-UA)。感谢！
- 改进内部代码：监视器一一出现。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
- Supplement Russian (ru-RU) and Ukrainian (uk-UA) langauges. Thank to @pasharm!
- Improve internal code: Monitors appear one by one.
```
</details>

---
### 📦 [YerongAI/Office-Tool](https://github.com/YerongAI/Office-Tool)
`⭐ Stars: 14,757` &nbsp;|&nbsp; `💻 语言: PowerShell` &nbsp;|&nbsp; `🏷️ 最新版本: [v11.9.15.0](https://github.com/YerongAI/Office-Tool/releases/tag/v11.9.15.0) (2026-11-11)`

> **简介**：Office Tool Plus 本地化项目。

**💡 核心亮点更新 (中文)**：
- 修复了在 Windows 10 中最大化或恢复时应用程序窗口闪烁的问题。
- 修复了应用程序无法在 Windows 11 21H2 上启动的问题。第1144章
- 修复了帮助文档的错误链接。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Change log

- Fixed an issue where application window would flicker when being maximized or restored in Windows 10.
- Fixed an issue where application cannot launch on Windows 11 21H2. #1144
- Fixed an incorrect link to the help documentation.

### Deploy

- Supports detecting the Windows editions, which serves as a basis for checking the Office version number.
- Fixed an issue where the Office data failed to load when the application data is null.

### Toolbox

- Optimized the log output when removing Office.

## Translation

it-it: @bovirus
ru-ru: @iDolmatov 
ko-kr: @VenusGirl
```
</details>

---
### 📦 [TDesktop-x64/tdesktop](https://github.com/TDesktop-x64/tdesktop)
`⭐ Stars: 3,017` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.2.13](https://github.com/TDesktop-x64/tdesktop/releases/tag/v1.2.13) (2026-11-14)`

> **简介**：64Gram（非官方 Telegram 桌面）

**💡 核心亮点更新 (中文)**：
* **Windows:** 将 `%APPDATA%\Telegram Desktop` 重命名为 `%APPDATA%\64Gram`
* **macOS:** 将 `~/Library/Application Support/Telegram Desktop` 重命名为 `~/Library/Application Support/64Gram`
* **Linux：** 无需执行任何操作（数据路径已于 2022 年迁移回）。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
v1.2.13 (TDesktop v7.4.4)

1. [Fix] Built-in updater
2. [Change] Rename binary and application data path to 64Gram (FINALLY!)

**NOTE:**
Due to changes in the built-in updater, you **MUST** manually reinstall 64Gram this time to receive future auto-updates.

Additionally, the application data path has changed. 
To keep your login session and settings without logging in again, 
please **completely quit 64Gram first**, 
then rename the parent data folder before launching the new version:

* **Windows:** Rename `%APPDATA%\Telegram Desktop` to `%APPDATA%\64Gram`
* **macOS:** Rename `~/Library/Application Support/Telegram Desktop` to `~/Library/Application Support/64Gram`
* **Linux:** No action required (the data path was already migrated back in 2022).
```
</details>

---
### 📦 [microsoft/vscode](https://github.com/microsoft/vscode)
`⭐ Stars: 195,537` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [1.146.0](https://github.com/microsoft/vscode/releases/tag/1.146.0) (2026-11-11)`

> **简介**：视觉工作室代码

**💡 核心亮点更新 (中文)**：
https://code.visualstudio.com/updates/v1_146

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
https://code.visualstudio.com/updates/v1_146
```
</details>

---

## <span id="-系统与开发者工具">🛠️ 系统与开发者工具</span>

### 📦 [Kianuni/Erosion-CN](https://github.com/Kianuni/Erosion-CN)
`⭐ Stars: 2,236` &nbsp;|&nbsp; `💻 语言: Swift` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.0.2](https://github.com/Kianuni/Erosion-CN/releases/tag/v1.0.2) (2026-11-17)`

> **简介**：iOS / iPadOS 系统配置与 MobileGestalt 研究工具箱（中英双语 · 防白苹果安全加固版） | Bootloop-safe iOS / iPadOS System Configuration & MobileGestalt Toolbox (Bilingual EN/ZH)

**💡 核心亮点更新 (中文)**：
- Added **「开屏广告缓存精准锁死 / Splash Ad Cache Blocker」** quick entries under **Tweaks → App Saves & Cleanup** (`功能修改 → 应用存档与空间清理`) and **File Browser → Quick Access** (`文件浏览 → 快捷访问`).
- Combines curated per-app splash-ad paths (Weibo, Zhihu, NetEase Cloud Music, QQ Music, Bilibili, Xiaohongshu, Taobao/Idlefish, JD, Meituan/Dianping, Amap, Baidu/Tieba/Netdisk, Ximalaya, Hupu, Douban) with shallow POSIX SDK detection (`KSAdSDK`, `BUAdSDK`/`Pangle`, `GDTMobSDK`/`TADCache`, `BaiduMobAd`, `SplashAd`, `LaunchAd`, etc.) — strictly excluding `SplashBoard`, WebKit, Cookies, `Downloads`, container roots, and symlinks.
- Supports one-tap **Locate** in File Browser (`定位目录`), wipe + **`0555` Read-Only Lock** (`一键锁死`), **`0755` Restore** (`恢复读写`), per-app/global batch controls, and a manual inspection toggle for unmatched apps. *(Note: disk `chmod` only blocks cached splash ad files; server-streamed/in-memory ads are unaffected.)*

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Erosion-CN v1.0.2 (Build 27)

> [!IMPORTANT]
> **System Compatibility / 系统兼容性提示**  
> - **Supported / 完整支持**: `iOS / iPadOS 27.0 – 27.2.1` and `27.3 beta 1` (`24C503*`).  
> - **Patched / 已封堵**: Apple patched `worse_query` starting in **`iOS 27.3 beta 2` (`24C5049d+`)**. Do **NOT** update past `27.3 beta 1` if you rely on Erosion-CN.

---

### What's New / 更新内容

1. **Per-App Splash Ad Cache Blocker (`chmod`) / 开屏广告缓存精准锁死 (`AdCacheBlockerView`)**
   - Added **「开屏广告缓存精准锁死 / Splash Ad Cache Blocker」** quick entries under **Tweaks → App Saves & Cleanup** (`功能修改 → 应用存档与空间清理`) and **File Browser → Quick Access** (`文件浏览 → 快捷访问`).
   - Combines curated per-app splash-ad paths (Weibo, Zhihu, NetEase Cloud Music, QQ Music, Bilibili, Xiaohongshu, Taobao/Idlefish, JD, Meituan/Dianping, Amap, Baidu/Tieba/Netdisk, Ximalaya, Hupu, Douban) with shallow POSIX SDK detection (`KSAdSDK`, `BUAdSDK`/`Pangle`, `GDTMobSDK`/`TADCache`, `BaiduMobAd`, `SplashAd`, `LaunchAd`, etc.) — strictly excluding `SplashBoard`, WebKit, Cookies, `Downloads`, container roots, and symlinks.
   - Supports one-tap **Locate** in File Browser (`定位目录`), wipe + **`0555` Read-Only Lock** (`一键锁死`), **`0755` Restore** (`恢复读写`), per-app/global batch controls, and a manual inspection toggle for unmatched apps. *(Note: disk `chmod` only blocks cached splash ad files; server-streamed/in-memory ads are unaffected.)*

2. **Wi-Fi HTTP File Sharing Auth, Browser Tips & Layout Fix / Wi-Fi 无线互传认证兼容、浏览器说明与按钮优化**
   - **Flexible Basic
```
</details>

---
### 📦 [physicsdolphin/nv-uefi-unlocker](https://github.com/physicsdolphin/nv-uefi-unlocker)
`⭐ Stars: 2,602` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.1.11](https://github.com/physicsdolphin/nv-uefi-unlocker/releases/tag/v2.1.11) (2026-11-08)`

> **简介**：适用于 Windows Linux Hackintosh 和所有 EFI 可启动系统 (Rust) 的 UEFI 预驱动程序 NVIDIA GPU 解锁器：SEC2 洗涤器 -> FWSEC/WPR2 -> 签名引导程序 -> V67 四写入负载，回读验证。在大多数 RTX 20 30 40 系列上经过验证。

**💡 核心亮点更新 (中文)**：
- Windows：扫描 DriverStore，从 `.inf` 解析 `DriverVer`，多仓库取最新；
- Linux：`/usr/lib|/lib|/run/current-system` firmware 下 `sort -V` 取最高版本；
- 本地路径 = **badge 模式**：版本钉定豁免（实测依据见下），fwimage+fwsignature 由同一容器天然成对；

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# nv-uefi-unlocker v2.1.11

**v2.1.11 — 制盘下载与 GSP 来源的结构性升级（本地优先）+ TU106 台架五版本 GSP 谱系实测**

## 主要变化 / What's new

### 1. 本地驱动 GSP 成为默认资产来源（badge 模式）/ Local driver GSP is now the default asset source ("badge mode")

多数制盘机都装着 NVIDIA 驱动——驱动仓库里本来就带着分代 GSP 固件（Windows `C:\Windows\System32\DriverStore\FileRepository\nv*inf_amd64_*\gsp_ga10x.bin + gsp_tu10x.bin`；Linux `/usr/lib/firmware/nvidia/<版本>/gsp_*.bin`，NixOS 等另探 `/run/current-system/firmware/`）。**v2.1.11 起 `make-usbroot` 默认优先取本地驱动的 GSP，找不到才回退网络下载**：

- Windows：扫描 DriverStore，从 `.inf` 解析 `DriverVer`，多仓库取最新；
- Linux：`/usr/lib|/lib|/run/current-system` firmware 下 `sort -V` 取最高版本；
- 本地路径 = **badge 模式**：版本钉定豁免（实测依据见下），fwimage+fwsignature 由同一容器天然成对；
- pre-52x 老驱动（单一多代 `gsp.bin`，无 `.fwimage` 段）会被指名拒绝并回退下载链；
- **显式参数**：`-UtilsSource arch|run|cachyos|local`（bash `--utils-source`）可钉定任一通道，`local` = 只用本地驱动 GSP；下载通道的哈希闸语义不变。

**效果**：装了 N 卡驱动的机器上，315 MB 的 nvidia-utils 下载默认消失，只剩 26 MB kernel-source（booter/BL/scrubber 的 BINDATA 内嵌在 `nvlddmkm.sys` 里，不是可拷贝文件，仍走钉定下载）。实测兼容的旧 assets 二进制同样可用（`gsp-sections` 早已存在，无新依赖）。

Most stick-building machines already have the NVIDIA driver installed, and the driver store ships the split GSP firmware ELFs. `make-usbroot` now tries the LOCAL driver's GSP first and falls back to the pinned downloads only when no local store is found: `auto = local DriverStore (badge mode) -> Arch archive -> first-party NVIDIA .run -> CachyOS cache`; pin one route with `-UtilsSource arch|run|cachyos|local`. Local is badge mode (vers
```
</details>

---
### 📦 [Icalingua-plus-plus/Icalingua-plus-plus](https://github.com/Icalingua-plus-plus/Icalingua-plus-plus)
`⭐ Stars: 3,383` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.26.10](https://github.com/Icalingua-plus-plus/Icalingua-plus-plus/releases/tag/v2.26.10) (2026-11-15)`

> **简介**：QQ等客户端。 ：电子：

**💡 核心亮点更新 (中文)**：
* 增加 收藏管理功能
* 增加 QQ 闪传功能
* 增加 新的协议

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## What's Changed
* 增加 收藏管理功能
* 增加 QQ 闪传功能
* 增加 新的协议
* 修复 milky 私聊房间名字处理异常的问题
* 修复 多图消息的编辑重发只有一张图的问题
* 修复 部分商城表情无法查看的问题
* 优化 夜间模式表现
* 优化 搜索索引的消息总数计算，避免全表 count 占满连接池 by @shenjackyuanjie in https://github.com/Icalingua-plus-plus/Icalingua-plus-plus/pull/843
* 优化 闪传与收藏管理页面交互 by @ttimochan in https://github.com/Icalingua-plus-plus/Icalingua-plus-plus/pull/853

**Full Changelog**: https://github.com/Icalingua-plus-plus/Icalingua-plus-plus/compare/v2.26.8...v2.26.10
```
</details>

---
### 📦 [assimp/assimp](https://github.com/assimp/assimp)
`⭐ Stars: 13,329` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [v6.0.6](https://github.com/assimp/assimp/releases/tag/v6.0.6) (2026-11-09)`

> **简介**：官方开放资产导入器库存储库。将 40 多种 3D 文件格式加载到一个统一且干净的数据结构中。

**💡 核心亮点更新 (中文)**：
* 修复俳句上的构建 https://github.com/assimp/assimp/pull/5255
* 减少 JoinVerticesProcess::ProcessMesh() 中的内存消耗 https://github.com/assimp/assimp/pull/5252
* 修复：在 https://github.com/assimp/assimp/pull/5258 中添加对无效输入参数的检查

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## What's Changed
* Fix building on Haiku by @Begasus in https://github.com/assimp/assimp/pull/5255
* Reduce memory consumption in JoinVerticesProcess::ProcessMesh() signi… by @ockeymm in https://github.com/assimp/assimp/pull/5252
* Fix: Add check for invalid input argument by @kimkulling in https://github.com/assimp/assimp/pull/5258
* Replace an assert by a error log. by @kimkulling in https://github.com/assimp/assimp/pull/5260
* Extension of skinning data export to GLB/GLTF format by @fvbj in https://github.com/assimp/assimp/pull/5243
* Fix output floating-point values to fbx by @Riv1s-sSsA01 in https://github.com/assimp/assimp/pull/5265
* Update ImproveCacheLocality.cpp by @kimkulling in https://github.com/assimp/assimp/pull/5268
* Update Readme.md by @kimkulling in https://github.com/assimp/assimp/pull/5277
* Deep arsdk bone double free by @kimkulling in https://github.com/assimp/assimp/pull/5291
* Fix Spelling error by @JulianKnodt in https://github.com/assimp/assimp/pull/5295
* use size in order to be compatible with float and double by @sloriot in https://github.com/assimp/assimp/pull/5270
* Fix: Add missing transformation for normalized normals. by @kimkulling in https://github.com/assimp/assimp/pull/5301
* Fix: Implicit Conversion Error by @Ipomoea in https://github.com/assimp/assimp/pull/5271
* Fix add checks for indices by @kimkulling in https://github.com/assimp/assimp/pull/5306
* Update FBXBinaryTokenizer.cpp by @kimkulling in https://github.com/as
```
</details>

---
### 📦 [openwrt/openwrt](https://github.com/openwrt/openwrt)
`⭐ Stars: 29,237` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [v25.12.6](https://github.com/openwrt/openwrt/releases/tag/v25.12.6) (2026-10-18)`

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

## <span id="-实用开源精选">📦 实用开源精选</span>

### 📦 [a3974892-cmd/wakeloom](https://github.com/a3974892-cmd/wakeloom)
`⭐ Stars: 61` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.21.5](https://github.com/a3974892-cmd/wakeloom/releases/tag/v1.21.5) (2026-11-09)`

> **简介**：暂无项目描述

**💡 核心亮点更新 (中文)**：
- 修复旧用户更新后的桌面图标：刷新 Windows 的旧 EXE 图标缓存，将指向当前程序的桌面快捷方式更新为 W 图标，保留启动目标与参数。
- 仅发布 Windows；保留 Colab 本地和网关模式，不包含已撤回的 Kaggle 接入。
- AI 对话新增代码块复制、双方消息时间及上下文整理，保留近期完整问答和失败反馈，显示实际带入的历史、附件与技能内容。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
- 修复旧用户更新后的桌面图标：刷新 Windows 的旧 EXE 图标缓存，将指向当前程序的桌面快捷方式更新为 W 图标，保留启动目标与参数。
- 仅发布 Windows；保留 Colab 本地和网关模式，不包含已撤回的 Kaggle 接入。
- AI 对话新增代码块复制、双方消息时间及上下文整理，保留近期完整问答和失败反馈，显示实际带入的历史、附件与技能内容。
- 附件可按内容读取 APK、EXE 等程序文件的静态结构和文字；不会执行上传程序，不代表模型能读取所有二进制内容。
- 为已接入的 Qwen3.8、DeepSeek-R1-70B-Q5 增加可选自动执行：文件、终端与独立浏览器工具，检查执行结果，阻止重复失败，暂停求助并在补充后继续。用户须单独开启；实际执行效果取决于模型。
- 自动执行日志支持收起、隐藏和调整高度；任务设置窗口不会因点击背景误关闭。
- 新增独立的 Qwen 1M 纯文字实验配置，修正运行时上下文对齐校验；不修改原有文字/视觉配置。需要足够的 GPU 和内存，1M 长输入效果仍待实际验证。
- 改善大模型导入的磁盘占用与容量检查；在校验完成后复用已下载文件，保留失败回退和空间保护。
- 本地 GPU 申请使用独立超时及 HTTP/1.1 兼容连接；网络断开后查询同一次申请，避免盲目重发，增加诊断信息。不能改变 Colab 的账户限制或 GPU 库存。
- 桌面更新保留现有设置、聊天、附件和技能；自动执行与界面改进无需重新部署正常运行的网关。需要新启动套件或 1M 配置的网关用户请按配套说明单独升级。
```
</details>

---
### 📦 [storytold/craft-anything](https://github.com/storytold/craft-anything)
`⭐ Stars: 35,274` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.6.1](https://github.com/storytold/craft-anything/releases/tag/v0.6.1) (2026-11-12)`

> **简介**：制作任何东西：了解任何软件的工作原理，并制作自己的软件。

**💡 核心亮点更新 (中文)**：
* 通过 https://github.com/storytold/craft-anything/pull/1348 将 Mach-O 零填充部分保留在文件支持的部分数据 (R3.12) 之外
* 在填充添加的 SQLite 列（R3.12）时读取小数位分隔符 https://github.com/storytold/craft-anything/pull/1318
* 在报告 Rust 依赖项 (R3.12) 之前验证 Cargo 包版本：https://github.com/storytold/craft-anything/pull/1329

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## What's Changed
* Keep Mach-O zero-fill sections out of file-backed section data (R3.12) by @Afloat16 in https://github.com/storytold/craft-anything/pull/1348
* Read decimal digit separators when filling added SQLite columns (R3.12) by @Afloat16 in https://github.com/storytold/craft-anything/pull/1318
* Verify Cargo package versions before reporting Rust dependencies (R3.12) by @Afloat16 in https://github.com/storytold/craft-anything/pull/1329
* Read the Swift standard type SQ as Equatable (R3.12) by @Chr0mium24 in https://github.com/storytold/craft-anything/pull/1350
* Let a Deep build through Claude Code start subagents again (R2.2, #1105) by @justinjohn0306 in https://github.com/storytold/craft-anything/pull/1351
* Decode Swift protocols named in a protocol list (R3.12) by @Chr0mium24 in https://github.com/storytold/craft-anything/pull/1353
* Read the kind letter of Swift addressors (R3.12) by @Chr0mium24 in https://github.com/storytold/craft-anything/pull/1354
* Name the right generic parameter in Swift associated types (R3.12) by @Chr0mium24 in https://github.com/storytold/craft-anything/pull/1355
* Name Swift allocating initialisers init outside classes (R3.12) by @Chr0mium24 in https://github.com/storytold/craft-anything/pull/1356
* Keep parentheses around Swift optional function types (R3.12) by @Chr0mium24 in https://github.com/storytold/craft-anything/pull/1357
* Decode Swift enum case symbols (R3.12) by @Chr0mium24 in https://github.com/storytold/craft-anything/p
```
</details>

---
### 📦 [JustAResearcher/gpu-unlock-ada](https://github.com/JustAResearcher/gpu-unlock-ada)
`⭐ Stars: 4,925` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.1.1](https://github.com/JustAResearcher/gpu-unlock-ada/releases/tag/v1.1.1) (2026-10-24)`

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
### 📦 [kenzok8/compile-package](https://github.com/kenzok8/compile-package)
`⭐ Stars: 165` &nbsp;|&nbsp; `💻 语言: Shell` &nbsp;|&nbsp; `🏷️ 最新版本: [2026.11.17-18/27_arm_cortex-a5_vfpv4](https://github.com/kenzok8/compile-package/releases/tag/2026.11.17-18/27_arm_cortex-a5_vfpv4) (2026-11-17)`

> **简介**：small-package仓库，每日更新插件编译

**💡 核心亮点更新 (中文)**：
定时更新插件，推送发布 💤:

[下载链接] (https://dllkids.xyz/packages/arm_cortex-a5_vfpv4/)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
定时更新插件，推送发布 💤:

[下载链接] (https://dllkids.xyz/packages/arm_cortex-a5_vfpv4/)
```
</details>

---
### 📦 [jxxghp/MoviePilot](https://github.com/jxxghp/MoviePilot)
`⭐ Stars: 12,085` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.2.7](https://github.com/jxxghp/MoviePilot/releases/tag/v3.2.7) (2026-11-17)`

> **简介**：NAS媒体库自动化管理工具

**💡 核心亮点更新 (中文)**：
- 通知与渠道授权：在用户管理中统一处理机器人使用申请、审批、权限及停用，支持关联已有网页账号，并迁移原有渠道白名单；修复微信、Slack、VoceChat、Synology Chat 无标题通知的显示。
- 媒体识别与分类：共享并缓存非 TMDB 来源到 TMDB 的转换关系，详情页可跳转到对应 TMDB 条目；减少跨来源重复订阅，修复儿童剧集被优先分入普通电视剧分类的问题。
- 订阅刷新：自动刷新按站点错峰，夜间降低频率，慢站独立退避，减少重复匹配；恢复缺失或过期的站点 RSS 地址，完善异常恢复。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 本次更新内容

以下汇总主项目 v3.2.6 首次发布后（北京时间 2026 年 11 月 12 日 14:13 起）的前后端及 App 变化；iOS App 使用独立版本号，本次涉及 v1.2.3。

- 通知与渠道授权：在用户管理中统一处理机器人使用申请、审批、权限及停用，支持关联已有网页账号，并迁移原有渠道白名单；修复微信、Slack、VoceChat、Synology Chat 无标题通知的显示。
- 媒体识别与分类：共享并缓存非 TMDB 来源到 TMDB 的转换关系，详情页可跳转到对应 TMDB 条目；减少跨来源重复订阅，修复儿童剧集被优先分入普通电视剧分类的问题。
- 订阅刷新：自动刷新按站点错峰，夜间降低频率，慢站独立退避，减少重复匹配；恢复缺失或过期的站点 RSS 地址，完善异常恢复。
- 下载与选集：统一 qBittorrent、Transmission、rTorrent 的剧集文件选择，保留已有任务状态及附件；修复累计集号、季集映射、手工末集号和整季包的下载范围及缺集统计。
- 音乐整理：手动整理新增严格匹配、忽略时长、按顺序对齐三种曲目匹配方式，支持直接指定最终目录并继承整理默认设置；修正 CUE 开关在非音乐任务中的显示。
- 文件整理：兼容 FUSE 挂载文件的 ctime 变化，修复重新整理时的失效软链接；重新规划复用已核实的媒体标识，手动 AI 纠错可在重试额度耗尽后再授权一次；修正整理历史日期与状态展示。
- 115 存储：上传完成回调异常时核验远端文件，无法确认的结果保留源文件并提示人工复核，避免误报成功或自动重复上传。
- 搜索与站点：完善 FluxTorrent 连接检测、令牌认证、共享流控和网关异常重试；搜索翻页失败时保留已获取的结果，隐藏当前场景不适用的规则提示。
- 媒体播放：打通后端流媒体接口、前端播放入口与 iOS 原生播放器，可从媒体详情、文件管理、整理历史及 App 搜索进入播放；支持本地及 STRM 视频、音乐、字幕、音轨、倍速、续播和同步歌词，新增 App 内悬浮小窗；完善媒体服务器搜索及 Jellyfin 扩展类型媒体库路由。
- App 多语言：新增简体中文、繁体中文和英语切换，与当前实例网页共享语言设置，原生菜单、连接页、通知、搜索、小组件和播放器文案同步更新，并按实例记忆选择。
- 插件市场：加快插件元数据、图标及项目链接加载，调整插件卡片与作者信息展示，改善浅色、深色和玻璃主题下的可读性。
- 界面与交互：将玻璃材质与画质选项集中到主题定制面板，统一卡片、输入框和状态标签样式；优化工作流预览、媒体详情操作和移动端选集信息布局，修复 App 长按订阅卡片时的形变，用户卡片接入原生菜单。
- AI 模型：新增 TrustedRouter 服务商，DeepSeek 默认模型更新为 deepseek-v4-flash。
- 运行稳定性：站点长时间限流时延后任务，减少线程占用；Redis 连续读取失败时退避，Docker 启用原生崩溃堆栈诊断，并更新相关依赖。

## 完整变更记录

- fix(indexer): stabilize FluxTorrent API access (#7404) by @jxxghp ([4580c8d](https://github.com/jxxghp/MoviePilot/commit/4580c8d4c5b261e1b0de7dbe0e5d47e93451d4e7))
- fix(download): preserve tasks and a
```
</details>

---
### 📦 [sandboxie-plus/Sandboxie](https://github.com/sandboxie-plus/Sandboxie)
`⭐ Stars: 19,979` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.18.8](https://github.com/sandboxie-plus/Sandboxie/releases/tag/v1.18.8) (2026-10-17)`

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

## <span id="-影音媒体与下载">🎬 影音媒体与下载</span>

### 📦 [ziyuanhuishequ/release-downloader](https://github.com/ziyuanhuishequ/release-downloader)
`⭐ Stars: 45` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.6.3](https://github.com/ziyuanhuishequ/release-downloader/releases/tag/v1.6.3) (2026-11-08)`

> **简介**：批量下载多个仓库的 GitHub Release 文件，并按系统与架构自动归档。免安装单文件，像素风界面，Windows 平台。

**💡 核心亮点更新 (中文)**：
- **线路从 8 条扩到 20 条**，测速每条只读 1MB，8 秒没反应就判不通、自动沉底
- **504/502/503 立刻换线**：5xx 只在同一条线路上补试 1 次（0.7 秒），4xx 直接换，不再死磕
- **挂掉的线路自动拉黑**：本轮任务后面的文件直接跳过它，不重复踩坑

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 这次修的是「下载提示 HTTP 504」

504 是**加速线路的网关超时**：那条线路去 GitHub 取数据没按时拿到，返回了 504。
不是文件坏了，也不是软件出错。常见原因是镜像站当时挂了/限流，或者你的网络出口拦了 GitHub 相关域名。

### 以前为什么会卡很久才报错

旧版遇到 504 会在**同一条线路**上重试 3 次，8 条线路就是 24 次超时请求，
真实网络下要白等好几分钟，最后只丢出一个 `HTTP 504`。

### 现在怎么处理

- **线路从 8 条扩到 20 条**，测速每条只读 1MB，8 秒没反应就判不通、自动沉底
- **504/502/503 立刻换线**：5xx 只在同一条线路上补试 1 次（0.7 秒），4xx 直接换，不再死磕
- **挂掉的线路自动拉黑**：本轮任务后面的文件直接跳过它，不重复踩坑
- **连撞 3 条线路级失败就停**，不在 20 条线路上挨个等超时
- **自动重试一次**：整轮网络类失败后等 2 秒、清空黑名单再试一遍，状态列显示「自动重试中…」
- **提示改成中文**：`所有线路都超时（HTTP 504）· 网络受限或镜像临时故障，稍后再点「开始下载」可续传`

### 还可以自己补线路

exe 同目录放 `routes.txt`，一行一条，`名称|前缀` 或只写前缀：

```
我的线路|https://gh.example.com/
https://another.example.com/
```

保存后重开（或点「重新测速」）即可参与测速，能用的排前面。镜像换域名不用等软件更新。
`GitHub下载整理工具.exe --routes` 可打印当前生效的线路表。

### 实测（`tools/err_srv.py`）

| 场景 | 请求数 | 结果 |
| --- | --- | --- |
| 单线路全 504 | 2（旧版 3） | 0.8 秒给出中文原因 |
| 3 条线路全 504 | 6（旧版 9） | 2.4 秒 |
| 20 条线路全 504 | 12（旧版 60） | 6.4 秒（含一次自动重试） |
| 20MB 全 504 | 26（旧版 88） | 2 秒放弃分片 + 单连接兜底 |
| 前 3 条 504、第 4 条正常 | 26 | 6.4 秒下完，md5 一致 |
| 一次抖动（第 1 个请求 504） | 2 | 自动重试后成功，md5 一致 |

**下载**：`GitHub-Release-Downloader-v1.6.3.exe`，双击即用，免安装。
```
</details>

---
### 📦 [threerocks/sweety-handdraw-video](https://github.com/threerocks/sweety-handdraw-video)
`⭐ Stars: 1,238` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.1.0](https://github.com/threerocks/sweety-handdraw-video/releases/tag/v3.1.0) (2026-11-11)`

> **简介**：从主题或文章制作完整手绘讲解视频：按部位描线、逐字书写、VoiceStudio 配音、五项内置制作依赖。

**💡 核心亮点更新 (中文)**：
- **油画**：块面写生的顺序：起稿 → 脸 → 头发 → 五官 → 衣服 → 背景 → 推近深入 → 落款。每笔有自己的压力、含色量和弯度；脸从暗部成片往外长，手离开一块区域时不留洞；轮廓不再是锯齿；最后几笔厚涂亮部。
- **素描**：一笔就是一支铅笔的一条线，石墨叠加变深，不从成品里「取」深浅。先起形，头发先用笔侧铺色调再画发丝，五官早早定下深色；揉擦、提亮时换纸擦笔和橡皮。
- **动漫插画**：草稿 → 线稿（每根线一笔画完，有入笔和出锋）→ 平涂（每块先沿边走一笔，再一条不抬笔的来回路线涂满，背景先整片涂满再画上面的植物）→ 阴影、高光 → 渐变 → 眼睛 → 签名。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# v3.1.0

新增人像绘画实验室（`labs/oil-portrait/`）：给一张人像照片，得到一部「一笔一笔画出来」的过程视频，三种画法：油画、素描、动漫插画。整个流程是一条命令，换用较小的模型来驱动也能得到同样的片子。

手绘口播 Skill 本身（`skills/sweety-handdraw-video/`）与 v3.0.2 相同，安装包只更新了版本号。人像绘画在仓库里运行，不在安装包里。

## 1. 一条命令出片

```bash
python3 labs/oil-portrait/make.py setup                          # 第一次：检查环境，缺人脸关键点环境会自动装
python3 labs/oil-portrait/make.py run 照片.jpg --kind sketch      # oil | sketch | anime | all
python3 labs/oil-portrait/make.py status                         # 每个任务的验收结论和成片路径
```

流程：照片裁成 2:3（以脸为中心）→ 图像模型画线稿、分区图、目标画 → 自动标注五官 → 规划笔画 → 出片 → 配乐 → 封面 → 验收。成片在 `output/paint/`：带音乐的 `film.mp4`、无声版、成品图、目标画、无水印封面和验收报告。

以前要靠人（或驱动工具的模型）看图决定的事，现在都在代码里：

| 以前 | 现在 |
|---|---|
| 看图手写眼睛、嘴、鼻子、脸的坐标 | `annotate.py`：人脸关键点（MediaPipe，单独的环境）加分区图算出来，带合理性检查（左右眼、上下顺序、都在脸内） |
| 按照片改提示词（「按照片补充…」） | 固定的通用提示词 |
| 看生成的图能不能用 | 自动校验：和照片对不对得上（偏了就挪回去）、是不是这张照片、分区图是不是四种纯色；不合格重画，最多 3 次 |
| 选裁剪、签名位置、音乐、手 | 固定规则 |
| 看成片好不好 | `check.py` 九项验收：片长、开场封面、结尾停留、手的移动、漏涂、和目标画的相似度、眼睛标注落在瞳孔上、响度、交付文件 |

给模型的操作手册是 `labs/oil-portrait/RUNBOOK.md`，仓库根目录的 `CLAUDE.md` 指向它。

## 2. 三种画法

- **油画**：块面写生的顺序：起稿 → 脸 → 头发 → 五官 → 衣服 → 背景 → 推近深入 → 落款。每笔有自己的压力、含色量和弯度；脸从暗部成片往外长，手离开一块区域时不留洞；轮廓不再是锯齿；最后几笔厚涂亮部。
- **素描**：一笔就是一支铅笔的一条线，石墨叠加变深，不从成品里「取」深浅。先起形，头发先用笔侧铺色调再画发丝，五官早早定下深色；揉擦、提亮时换纸擦笔和橡皮。
- **动漫插画**：草稿 → 线稿（每根线一笔画完，有入笔和出锋）→ 平涂（每块先沿边走一笔，再一条不抬笔的来回路线涂满，背景先整片涂满再画上面的植物）→ 阴影、高光 → 渐变 → 眼睛 → 签名。

三种都是：开场先显示成品 0.5 秒再淡出到空白画布，结尾镜头缓推、展示成品 6 秒。

## 3. 没有手，只有笔尖

用户转来的网友反馈：「其实没有那只手是更好的……用苹果的笔触来代替，一笔笔画完。」现在默认不再画握笔的手，只显示平板绘画软件那样的笔尖光标：落笔时是笔刷大小的圆圈加当前颜色
```
</details>

---
### 📦 [KnifeLemon/Filee](https://github.com/KnifeLemon/Filee)
`⭐ Stars: 28,325` &nbsp;|&nbsp; `💻 语言: C#` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.5.0](https://github.com/KnifeLemon/Filee/releases/tag/v2.5.0) (2026-11-16)`

> **简介**：免费的开源文件转换器。通过拖放功能离线转换 263 格式 — 图像、PDF、Word、Excel、PowerPoint、HWP/HWPX、视频、音频、电子书和档案。无需上传，无需 Office。

**💡 核心亮点更新 (中文)**：
发生了什么变化

<!--更新
级别：必填
zh: 安全修复：防止安装程序权限问题和操纵文档/压缩文件导致内存/磁盘耗尽。
zh: 预设库：浏览并安装其他人共享的预设或分享您自己的预设（设置 → 预设）
ko：Windows ARM64（Snapdragon等）的安装文件和便携式ZIP单独发布。
zh: 新格式：VTF、Ge

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## What's Changed

<!-- update
level: required
ko: 보안 수정: 설치 프로그램의 권한 문제, 조작된 문서·압축 파일로 메모리·디스크를 고갈시키는 문제를 막았어요
ko: 프리셋 갤러리: 다른 사람이 공유한 프리셋을 둘러보고 설치하거나 내 프리셋을 공유해요 (설정 → 프리셋)
ko: Windows ARM64(Snapdragon 등)용 설치 파일과 포터블 ZIP이 따로 나와요
ko: 새 형식: VTF, Gerber, JSON Canvas, G-code, Wisenet .nov, KuGou .krc, .nupkg·.apks·.aab, GIMP .xcf, Paint.NET .pdn, .ani, .xm, .osm, .ino·.pde 등
ko: 새 언어: 몽골어
ko: 변환한 뒤 원본을 휴지통으로 옮기는 옵션, 압축 정도를 매번 고르기, PDF/A 프리셋, PDF·동영상을 여러 개로 나누기
ko: 소리 파일 자르기와 아이폰 벨소리(M4R), 동영상 합치기에 음악 넣기, 이미지 도넛에 PDF 합치기
ko: 폴더를 다시 ZIP으로 묶고, 포터블 모드, 다운로드 프록시, Filee Connect(휴대폰과 주고받기)가 생겼어요
ko: HWPX 줄바꿈, PPTX 제목 위치, Word 표 스타일, PDF/A 링크 등 여러 문제를 고쳤어요
en: Security fixes: the installer no longer lets other programs abuse its admin rights, and crafted documents and archives can no longer exhaust memory or disk
en: Preset gallery: browse and install presets other people shared, or share your own (Settings → Presets)
en: Native Windows on ARM64 Setup and Portable ZIP
en: New formats: VTF, Gerber, JSON Canvas, G-code, Wisenet .nov, KuGou .krc, .nupkg/.apks/.aab, GIMP .xcf, Paint.NET .pdn, .ani, .xm, .osm, .ino/.pde and more
en: New language: Mongolian
en: Move the original to the Trash after converting, choose the compression each time, a PDF/A preset, and splitting PDFs and videos into parts
en: Cut sounds and make iPhone ringtones (M4R), music under Merge videos, and Merge PDF on the images donut
en: Folders zip again, plus portable mode, a proxy for Filee's downloa
```
</details>

---
### 📦 [guohuiyuan/go-music-dl](https://github.com/guohuiyuan/go-music-dl)
`⭐ Stars: 6,537` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.1.7](https://github.com/guohuiyuan/go-music-dl/releases/tag/v1.1.7) (2026-11-16)`

> **简介**：一个基于 Go 语言的全网音乐搜索与下载工具。支持 CLI 命令行与 Web 服务双模式，内置网易云、QQ、酷狗、Bilibili、汽水音乐等 10+ 个主流平台，支持多源并发搜索与无损音质解析。music-dl交流群：755087923

**💡 核心亮点更新 (中文)**：
* 056b10a6fc5f0be8aca207ec2d319bba51efbd51 为第240号问题新增测试并实现相关功能 - 为视频生成弹窗、外观预览、播放列表空状态以及下载记录新增了UI测试。 - 修改弹窗关闭逻辑，改用独立的关闭处理函数。 - 优化歌曲列表模板，可根据播放列表状态进行条件渲染。 - 改进视频生成弹窗内的音量控件，保证宽度稳定，并增加收藏与下载操作按钮。 - 重构外观设置相关的JavaScript代码，支持无需保存即可预览效果。 - 更新CSS样式，统一各组件样式，包含播放速度控件和下载记录模块。
* 3c1f265b88e5d439f58dc43434d493f2a32b8f4d 优化收藏和下载功能，增加错误提示，调整模态框样式
* 2153b85f09b5f305469c0b82d58cc99909e63d58 优化设置模态框的行为，确保用户选择的设置标签在配置请求完成前保持不变

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Changelog
* 056b10a6fc5f0be8aca207ec2d319bba51efbd51 为第240号问题新增测试并实现相关功能 - 为视频生成弹窗、外观预览、播放列表空状态以及下载记录新增了UI测试。 - 修改弹窗关闭逻辑，改用独立的关闭处理函数。 - 优化歌曲列表模板，可根据播放列表状态进行条件渲染。 - 改进视频生成弹窗内的音量控件，保证宽度稳定，并增加收藏与下载操作按钮。 - 重构外观设置相关的JavaScript代码，支持无需保存即可预览效果。 - 更新CSS样式，统一各组件样式，包含播放速度控件和下载记录模块。
* 3c1f265b88e5d439f58dc43434d493f2a32b8f4d 优化收藏和下载功能，增加错误提示，调整模态框样式
* 2153b85f09b5f305469c0b82d58cc99909e63d58 优化设置模态框的行为，确保用户选择的设置标签在配置请求完成前保持不变
* a796e6115040df153748ba6b952c974429083f88 优化音源顺序，新增音质设置功能，更新相关测试和前端逻辑
* a4741b44952bbd8ea6d5cc1466a6e3ce5697840e 修复依赖版本，更新音乐库至 v1.1.2
* 6dc08cd8ae62de78caf21d242883887d24ca6923 功能：新增下载记录的文件定位功能，并优化文件打开逻辑 - 新增用于定位下载记录文件的接口。 - 优化文件打开机制，可根据操作系统分别处理文件夹与单个文件。 - 更新界面，移除独立的打开文件夹按钮，替换为下载文件定位操作。 - 完善文件解析的异常处理，并为新增功能补充测试用例。 - 更新页面模板与样式，适配下载管理界面的改动。
* bb5c19e13dd2ca60a2993caa9c29276c94f76b49 功能：新增音频音质配置以及降级机制
* 0634f7b12caac1e579d64e2c6092b39699bac2a2 新增支持专辑艺人功能，优化文件命名模板，更新相关测试和前端逻辑
* af5d31db5a646aefd22d5201f8d1fafd1351d8fb 新增本地音乐文件定位功能，支持通过 POST 请求揭示文件路径，并更新相关前端逻辑和测试
* 559996b04bb7151ba94dcd79219f137c0d3bf9df 新增音频质量源支持，包括5sing、Jamendo、JOOX和Bilibili，并更新相关测试
* cb8d86d4f4c70bf3b136620321ea0c152d8c9b55 更新 music-lib 依赖至 v1.1.3-0.20261116162321-90b29428b646，并同步更新 go.sum 文件
* 7a5253f7e2d817d760b75d18b3f3419143ef8412 更新音乐库依赖至 v1.1.3，修正版本号和哈希值
```
</details>

---
### 📦 [LibreSpark/LibreTV](https://github.com/LibreSpark/LibreTV)
`⭐ Stars: 25,174` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.23.2](https://github.com/LibreSpark/LibreTV/releases/tag/v2.23.2) (2026-11-14)`

> **简介**：一分钟搭建影视站，支持Docker等部署方式

**💡 核心亮点更新 (中文)**：
获取方式

Docker（多架构 linux/amd64 / linux/arm64）

```bash
docker pull docker.io/bestzwei/libretv:2.23.2
docker pull ghcr.io/librespark/libretv:2.23.2
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
docker pull docker.io/bestzwei/libretv:2.23.2
docker pull ghcr.io/librespark/libretv:2.23.2
```

两个 registry 的镜像内容一致（同一组 digest），`latest` 也指向本版本。

### 免 Docker（下方附件，Node 18+）

```bash
sha256sum -c SHA256SUMS
tar -xzf libretv-2.23.2-standalone.tar.gz -C libretv
cd libretv && PASSWORD=your-password PORT=8080 node server.js
```

预构建包与 CPU 架构无关（x86_64 / arm64 / armv7），环境变量与 Docker 部署一致。

> 镜像由 docker-publish 工作流在同一 tag 上构建，刚发布时可能还要 5–10 分钟才可拉取。

## 变更

完整对比：https://github.com/LibreSpark/LibreTV/compare/v2.23.1...v2.23.2
```
</details>

---
### 📦 [dyang886/Game-Cheats-Manager](https://github.com/dyang886/Game-Cheats-Manager)
`⭐ Stars: 16,523` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.5.5](https://github.com/dyang886/Game-Cheats-Manager/releases/tag/v2.5.5) (2026-11-14)`

> **简介**：轻松下载和管理单人游戏秘籍，方便您

**💡 核心亮点更新 (中文)**：
- 在“设置”中添加了“优化下载路由”选项，默认情况下处于启用状态，可通过 Cloudflare IP 选择优化中国的下载速度
- 优化并行下载逻辑
- 删除了“仅使用 IPv4 进行网络连接”选项

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Patch Update

### English
- Added an `Optimize download routes` option in Settings, on by default, to optimize download speed in China with Cloudflare ip selection
- Optimized parallel download logic
- Removed `Use IPv4 only for network connections` option
- The app is now signed with certificate

### 简体中文
- 设置中新增 `优化下载线路` 选项，默认开启，旨在提升国内下载速度，使用 Cloudflare ip 优选
- 移除了 `网络连接仅使用 IPv4` 选项
- 优化并行下载逻辑
- 软件现在添加了签名证书
```
</details>

---
### 📦 [DIYgod/RSSHub](https://github.com/DIYgod/RSSHub)
`⭐ Stars: 47,069` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2026.11.17-8661.cf95739](https://github.com/DIYgod/RSSHub/releases/tag/v2026.11.17-8661.cf95739) (2026-11-17)`

> **简介**：🧡 一切都是RSSible

**💡 核心亮点更新 (中文)**：
-ghcr.io/diygod/rsshub:cf957392f2d1a42085f182fca83caa6e7a293359
- ghcr.io/diygod/rsshub:chromium-bundled-cf957392f2d1a42085f182fca83caa6e7a293359
-diygod/rsshub：cf957392f2d1a42085f182fca83caa6e7a293359

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Source commit: cf957392f2d1a42085f182fca83caa6e7a293359

Published multi-platform images:
- ghcr.io/diygod/rsshub:cf957392f2d1a42085f182fca83caa6e7a293359
- ghcr.io/diygod/rsshub:chromium-bundled-cf957392f2d1a42085f182fca83caa6e7a293359
- diygod/rsshub:cf957392f2d1a42085f182fca83caa6e7a293359
- diygod/rsshub:chromium-bundled-cf957392f2d1a42085f182fca83caa6e7a293359

Use these commit-specific image tags to reproduce this release. Daily Docker tags may be updated by subsequent builds.
```
</details>

---
### 📦 [amir1376/ab-download-manager](https://github.com/amir1376/ab-download-manager)
`⭐ Stars: 19,341` &nbsp;|&nbsp; `💻 语言: Kotlin` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.11.4](https://github.com/amir1376/ab-download-manager/releases/tag/v1.11.4) (2026-11-03)`

> **简介**：下载管理器可加快您的下载速度

**💡 核心亮点更新 (中文)**：
- 修复了深色主题上的二维码渲染问题。
- 更新翻译
- 提高了读取多个二维码的速度。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 1.11.4

A hotfix for [v1.11.3](https://github.com/amir1376/ab-download-manager/releases/v1.11.3)

### Fixed

- Fixed QR code rendering on dark themes.

### Improved

- Updated translations
- Improved the speed of reading multiple QR codes.

## 1.11.3

### Added

- Added a Network section to the desktop settings page

### Fixed

- Fixed incorrect category icon names being saved to storage. If you notice any mismatched category icons, right-click
  the category and select **Reset to Defaults**

### Improved

- Updated translations
- Improved the QR Code scanner UI/UX on Android (#1516)
- Improved QR Code sharing, allowing users to share multiple download credentials across multiple QR Codes (#1520)
```
</details>

---
### 📦 [gyroflow/gyroflow](https://github.com/gyroflow/gyroflow)
`⭐ Stars: 9,736` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.7.0](https://github.com/gyroflow/gyroflow/releases/tag/v1.7.0) (2026-11-07)`

> **简介**：使用陀螺仪数据进行视频稳定

**💡 核心亮点更新 (中文)**：
- **新相机：** Canon、Z CAM、HOVERAir、XTRA 等，见下文
- **光学稳定** - 新的稳定算法无需运动数据，实际上很好。它在大多数具有良好跟踪点和良好镜头轮廓的视频上产生与基于陀螺仪的稳定相似的结果。在“运动数据 -> 光学校正”中启用。这修复了所有 O4 问题、振动、陀螺仪不良、O4 Lite、DJI Neo 震动、FPV 上的 Hero 7、使用 RockSteady 的 DJI、使用 OSS 的索尼等。如果帧中有移动的主体，您可以编辑每个跟踪点并将其从解决方案中删除。需要有效的镜头配置文件。
- **新的“最佳路径”平滑** - 立即规划整个剪辑的相机路径：它在相同变焦下比“默认”消除更多的抖动，永远不会落后于平移，并将帧保持在变焦限制内。在“稳定”面板中选择它并尝试您的镜头 - 它与默认的感觉完全不同。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
### ✨ Improvements
- **New cameras:** Canon, Z CAM, HOVERAir, XTRA and more, see below
- **Optical stabilization** - New algorithm for stabilization without motion data that's actually good. It produces similar results to gyro-based stabilization on most videos with good tracking points and good lens profile. Enable in `Motion data -> Optical correction`. This fixes all O4 issues, vibrations, bad gyro, O4 Lite, DJI Neo shakes, Hero 7 on FPV, DJI with RockSteady, Sony with OSS etc. If you have a moving subject in frame, you can edit every tracked point and remove it from the solution. Valid lens profile is required.
- **New "Optimal path" smoothing** - plans the camera path for the whole clip at once: it removes much more shake than "Default" at the same zoom, never lags behind pans, and keeps the frame within the zoom limit. Select it in the "Stabilization" panel and try on your footage - it has a completely different feel than Default.
- **GoPro now uses official calibrations** - Lens profiles are more acurate and all new GoPro models are supported without changes to Gyroflow
- **All [Sony issues](https://github.com/gyroflow/gyroflow/issues/849) have been fixed**, including Dynamic Active support
- **Sony lens breathing compensation**, using the data recorded by the supported lenses
- **RED gyro data is now accurately timed**, autosync is no longer needed
- **Focal length stabilization** - smooths out fast zooms and zoom "pumping" by cropping. Works with every file t
```
</details>

---
### 📦 [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp)
`⭐ Stars: 208,565` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [2026.10.26](https://github.com/yt-dlp/yt-dlp/releases/tag/2026.10.26) (2026-10-26)`

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
`⭐ Stars: 79,652` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [33.0.1](https://github.com/obsproject/obs-studio/releases/tag/33.0.1) (2026-10-29)`

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
`⭐ Stars: 5,628` &nbsp;|&nbsp; `💻 语言: CSS` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.1.4](https://github.com/jerrykuku/luci-theme-argon/releases/tag/v3.1.4) (2026-11-13)`

> **简介**：Argon 是一个干净整洁的 OpenWrt LuCI 主题，允许用户使用图像或视频自定义其登录界面。   它还支持明暗模式自动和手动切换。

**💡 核心亮点更新 (中文)**：
- 修复提示条遮挡下拉菜单、表格下拉选项显示不完整的问题（#740、#741）。
- 适配新版 LuCI 仪表盘，修复布局及组件配置交互（#742）。
- 改善 Firefox ESR 的主题切换、组合控件、下拉菜单及端口统计显示（#739）。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 修复与改进

- 修复提示条遮挡下拉菜单、表格下拉选项显示不完整的问题（#740、#741）。
- 适配新版 LuCI 仪表盘，修复布局及组件配置交互（#742）。
- 改善 Firefox ESR 的主题切换、组合控件、下拉菜单及端口统计显示（#739）。
- 增加视频背景播放/暂停与键盘跳转导航，优化实时图表更新性能。

## Fixes and improvements

- Fix inline alerts obscuring dropdowns and clipped dropdown options in tables (#740, #741).
- Support newer LuCI dashboard layouts and configurable widget interactions (#742).
- Improve Firefox ESR appearance controls, joined inputs, dropdowns and port statistics (#739).
- Add background video playback controls and a keyboard skip link, and reduce realtime chart layout work.

v3.1.0 及以上可在线升级。安装说明：[中文](https://github.com/jerrykuku/luci-theme-argon/blob/v3.1.4/README_ZH.md#安装) · [English](https://github.com/jerrykuku/luci-theme-argon/blob/v3.1.4/README.md#install)
```
</details>

---
### 📦 [agalwood/Motrix](https://github.com/agalwood/Motrix)
`⭐ Stars: 58,419` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.4.3](https://github.com/agalwood/Motrix/releases/tag/v2.4.3) (2026-11-17)`

> **简介**：功能齐全的下载管理器。

**💡 核心亮点更新 (中文)**：
* 修复（下载）：改进进度并防止重复的暂停请求，网址为 https://github.com/agalwood/Motrix/pull/2525
* 壮举（下载）：通过 https://github.com/agalwood/Motrix/pull/2527 保持统计数据与任务详细信息可见
* feat(server): 支持自定义访问密码 https://github.com/agalwood/Motrix/pull/2529

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# Motrix 2.4.3

English | [简体中文](https://github.com/agalwood/Motrix/blob/main/docs/release-notes/2.4.3.zh-CN.md)

## Changes since 2.4.2

- Support custom Server access passwords while retaining the existing generated-password and CLI management flow.
- Keep Server shutdown handlers active while pending writes and other cleanup drain, preventing an atomic file write from interrupting graceful shutdown.
- Add an option to keep download statistics visible while task details are open.
- Display download progress with one decimal place, refresh active progress more frequently, and coalesce duplicate pause requests across controls.
- Adapt fnOS integration to SDK **0.6.0**, including standalone browser directory authorization, cancellation and popup handling, clearer unsupported file-action messages, and live host theme synchronization. Native iframe and mobile hosts retain direct file capabilities.
- Update **Electron to 45.3.3**, **i18next to 27.1.3**, and **react-i18next to 18.0.2**. These updates include language-code handling fixes and translation resource subscription fixes.
- Upgrade the plugin call graph to **React Flow 13.0.1**, preserving node selection and dragging, application themes, and the existing view spacing.
- Refresh Biome and user-event test tooling. Keep **vscode-jsonrpc 9.0.3** unchanged.

## Upgrade compatibility

**Back up your profile and download files before upgrading.** The bundled engine
uses SQLite **schema 6**. When upgrading an older engine databas
```
</details>

---
### 📦 [subhra74/xdm](https://github.com/subhra74/xdm)
`⭐ Stars: 8,569` &nbsp;|&nbsp; `💻 语言: Kotlin` &nbsp;|&nbsp; `🏷️ 最新版本: [9.0.11](https://github.com/subhra74/xdm/releases/tag/9.0.11) (2026-11-15)`

> **简介**：自 2013 年以来，快速、可靠的下载加速器和视频下载器

**💡 核心亮点更新 (中文)**：
下载

|安装人员|笔记|
|---|---|
| [xdm-app-9.0.11-arm64.dmg](https://github.com/subhra74/xdm/releases/download/9.0.11/xdm-app-9.0.11-arm64.dmg) |适用于 Apple Silicon（M1 或更高版本）mac |
| [xdm-app-9.0.11-x64.dmg](https://github.com/subhra74/

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Downloads

| Installer | Notes |
|---|---|
| [xdm-app-9.0.11-arm64.dmg](https://github.com/subhra74/xdm/releases/download/9.0.11/xdm-app-9.0.11-arm64.dmg) | For Apple Silicon (M1 or later) mac |
| [xdm-app-9.0.11-x64.dmg](https://github.com/subhra74/xdm/releases/download/9.0.11/xdm-app-9.0.11-x64.dmg) | For Intel mac |
| [xdm-9.0.11-arm64.msi](https://github.com/subhra74/xdm/releases/download/9.0.11/xdm-9.0.11-arm64.msi) | For Windows ARM (Windows 10/11) |
| [xdm-9.0.11-x64.msi](https://github.com/subhra74/xdm/releases/download/9.0.11/xdm-9.0.11-x64.msi) | For Windows x64 (Windows 10/11) |
| [xdmsetup-9.0.11.msi](https://github.com/subhra74/xdm/releases/download/9.0.11/xdmsetup-9.0.11.msi) | Same as the x64 MSI; for XDM 8 (Microsoft Store) update notices |
| [xdm-app_9.0.11_amd64.deb](https://github.com/subhra74/xdm/releases/download/9.0.11/xdm-app_9.0.11_amd64.deb) | For Debian / Ubuntu / Linux Mint x64 |
| [xdm-app_9.0.11_arm64.deb](https://github.com/subhra74/xdm/releases/download/9.0.11/xdm-app_9.0.11_arm64.deb) | For Debian / Ubuntu / Linux Mint ARM |
| [xdm-app-9.0.11-1.aarch64.rpm](https://github.com/subhra74/xdm/releases/download/9.0.11/xdm-app-9.0.11-1.aarch64.rpm) | For Fedora / RHEL / openSUSE ARM |
| [xdm-app-9.0.11-1.x86_64.rpm](https://github.com/subhra74/xdm/releases/download/9.0.11/xdm-app-9.0.11-1.x86_64.rpm) | For Fedora / RHEL / openSUSE x64 |
| [xdm-app-9.0.11-1-aarch64.pkg.tar.zst](https://github.com/subhra74/xdm/releases/download/9.0.11/xdm-app-9.0.11
```
</details>

---

## <span id="-网络与代理技术">🌐 网络与代理技术</span>

### 📦 [SagerNet/sing-box](https://github.com/SagerNet/sing-box)
`⭐ Stars: 40,045` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.14.4](https://github.com/SagerNet/sing-box/releases/tag/v1.14.4) (2026-10-24)`

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
`⭐ Stars: 10,918` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [2.44.16](https://github.com/sub-store-org/Sub-Store/releases/tag/2.44.16) (2026-11-16)`

> **简介**：QX、Loon、Surge、Stash、Egern 和 Shadowrocket 的高级订阅管理器！

**💡 核心亮点更新 (中文)**：
* feat: Surge/Surfboard 处理不合法的节点名 ([2a173b8](https://github.com/sub-store-org/Sub-Store/commit/2a173b8))

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## <small>2.44.16 (2026-11-16)</small>

* feat: Surge/Surfboard 处理不合法的节点名 ([2a173b8](https://github.com/sub-store-org/Sub-Store/commit/2a173b8))
```
</details>

---
### 📦 [233boy/Xray](https://github.com/233boy/Xray)
`⭐ Stars: 2,833` &nbsp;|&nbsp; `💻 语言: Shell` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.37](https://github.com/233boy/Xray/releases/tag/v1.37) (2026-11-02)`

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
`⭐ Stars: 2,707` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.39.0](https://github.com/enfein/mieru/releases/tag/v3.39.0) (2026-10-23)`

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
`⭐ Stars: 15,865` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.5.15](https://github.com/v2rayA/v2rayA/releases/tag/v2.5.15) (2026-11-13)`

> **简介**：一个基于 Xray 的核心的 Web 客户端，在 Linux、Windows 和 macOS 上具有全局透明代理。

**💡 核心亮点更新 (中文)**：
* 修复（gui）：在 https://github.com/v2rayA/v2rayA/pull/2114 中删除停放的 v2raya.org 并链接 daeuniverse.org
* 修复（资产）：不要在 https://github.com/v2rayA/v2rayA/pull/2115 中创建丢失的 XDG 运行时目录
* 修复(docker): 在 https://github.com/v2rayA/v2rayA/pull/2116 中安装 iproute2 以实现 TUN 模式

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## What's Changed
* fix(gui): drop the parked v2raya.org and link daeuniverse.org by @Zakkaus in https://github.com/v2rayA/v2rayA/pull/2114
* fix(asset): do not create a missing XDG runtime directory by @Zakkaus in https://github.com/v2rayA/v2rayA/pull/2115
* fix(docker): install iproute2 for TUN mode by @Zakkaus in https://github.com/v2rayA/v2rayA/pull/2116
* docs: tighten the contribution rules for assisted pull requests by @Zakkaus in https://github.com/v2rayA/v2rayA/pull/2117
* fix(vless): keep the ECH parameter in share links and the core config by @Zakkaus in https://github.com/v2rayA/v2rayA/pull/2118
* fix(gui): keep the proxies source and mount long node lists a page at a time by @Zakkaus in https://github.com/v2rayA/v2rayA/pull/2119
* fix(openwrt): include LAN bridges in TPROXY by default by @wywywywycloud in https://github.com/v2rayA/v2rayA/pull/2057


**Full Changelog**: https://github.com/v2rayA/v2rayA/compare/v2.5.14...v2.5.15
```
</details>

---
### 📦 [HyNetworks/hysteria](https://github.com/HyNetworks/hysteria)
`⭐ Stars: 22,941` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [app/v2.14.0](https://github.com/HyNetworks/hysteria/releases/tag/app/v2.14.0) (2026-11-15)`

> **简介**：Hysteria 是一款功能强大、速度快如闪电且抗审查的开源代理软件

**💡 核心亮点更新 (中文)**：
- 将 [ACL](https://hysteria.network/docs/advanced/ACL/) 切换到基于 [expr](https://expr-lang.org/) 的新引擎
- 规则现在是表达式，使用“acl.rules”或“acl.rulesFile”设置。除了目的地和协议之外，它们还可以匹配客户端的身份验证 ID 和地址，例如通过不同的出站路由每个用户
- 添加了“hysteria acl test”以[检查请求将使用哪个规则和出站](https://hysteria.network/docs/advanced/ACL/#testing-rules)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
- Switched [ACL](https://hysteria.network/docs/advanced/ACL/) to a new engine based on [expr](https://expr-lang.org/)
    - Rules are now expressions, set with `acl.rules` or `acl.rulesFile`. Besides the destination and protocol, they can match on the client's authentication ID and address, e.g. to route each user through a different outbound
    - Added `hysteria acl test` to [check which rule and outbound a request would use](https://hysteria.network/docs/advanced/ACL/#testing-rules)
    - The [legacy syntax](https://hysteria.network/docs/advanced/ACL/#legacy-syntax) (`acl.file` and `acl.inline`) still works. Legacy rules can be [mixed into `acl.rules`](https://hysteria.network/docs/advanced/ACL/#mixing-legacy-rules-into-rules), or converted with [`hysteria acl translate`](https://hysteria.network/docs/advanced/ACL/#converting-legacy-rules)
    - Fixed legacy port ranges starting at 0 (e.g. `udp/0-100`) matching every port
- Improved UDP forwarding performance by reducing per-packet overhead (about 30% more packets per second for small-packet upload)
- Updated quic-go to v0.65.0

---

- [ACL](https://hysteria.network/zh/docs/advanced/ACL/) 改用基于 [expr](https://expr-lang.org/) 的全新引擎
    - 规则现在以表达式的形式编写，通过 `acl.rules` 或 `acl.rulesFile` 设置。除目标地址和协议外，还可以根据客户端的验证 ID 和地址进行匹配，例如让不同用户走不同出站
    - 新增 `hysteria acl test`，用于[测试某个请求会使用哪条规则和哪个出站](https://hysteria.network/zh/docs/advanced/ACL/#testing-rules)
    - [旧版语法](https://hysteria.network/zh/docs/advanced/ACL/#legacy-syntax)（`acl.fi
```
</details>

---
### 📦 [Anankke/SSPanel-UIM](https://github.com/Anankke/SSPanel-UIM)
`⭐ Stars: 10,447` &nbsp;|&nbsp; `💻 语言: PHP` &nbsp;|&nbsp; `🏷️ 最新版本: [26.3.0](https://github.com/Anankke/SSPanel-UIM/releases/tag/26.3.0) (2026-11-13)`

> **简介**：多用途代理服务管理系统

**💡 核心亮点更新 (中文)**：
- amd64 和 arm64 的官方镜像“ghcr.io/anankke/sspanel-uim”，带有 Compose 部署，请参阅“docker/README.md”
- 迁移在第一次失败时停止，并在下次运行时恢复
- `xcat Migration` 因参数缺失或未知而退出 2

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Upgrade from 26.2.0 with `bash update.sh release 26.3.0 2025073100`. No schema change.

### Added

- Official image `ghcr.io/anankke/sspanel-uim` for amd64 and arm64, with a Compose deployment, see `docker/README.md`

### Changed

- Migrations stop at the first failure and resume from it on the next run
- `xcat Migration` exits 2 on a missing or unknown argument
- Admin balance edits are recorded as adjustments with a note

### Fixed

- HTTP 500 when saving a user in the admin panel
- Balance and traffic accounting under concurrent requests
- Sorting and ban end time in the admin log tables
```
</details>

---
### 📦 [QiuSimons/YAOF](https://github.com/QiuSimons/YAOF)
`⭐ Stars: 2,783` &nbsp;|&nbsp; `💻 语言: Shell` &nbsp;|&nbsp; `🏷️ 最新版本: [25.12.6](https://github.com/QiuSimons/YAOF/releases/tag/25.12.6) (2026-10-18)`

> **简介**：适用于 Nanopi R2C/R2S/R4S/X86 的 OpenWrt

**💡 核心亮点更新 (中文)**：
该版本未提供详细更新说明。

---
### 📦 [Loyalsoldier/v2ray-rules-dat](https://github.com/Loyalsoldier/v2ray-rules-dat)
`⭐ Stars: 21,052` &nbsp;|&nbsp; `💻 语言: Other` &nbsp;|&nbsp; `🏷️ 最新版本: [202611162204](https://github.com/Loyalsoldier/v2ray-rules-dat/releases/tag/202611162204) (2026-11-16)`

> **简介**：🦄 🎃 👻 V2Ray 路由规则文件加强版，可代替 V2Ray 官方 geoip.dat 和 geosite.dat，适用于 V2Ray、Xray-core、mihomo(Clash-Meta)、hysteria、Trojan-Go 和 leaf。Enhanced edition of V2Ray rules dat files, applicable to V2Ray, Xray-core, mihomo(Clash-Meta), hysteria, Trojan-Go and leaf.

**💡 核心亮点更新 (中文)**：
该版本未提供详细更新说明。

---
### 📦 [Openwrt-Passwall/openwrt-passwall](https://github.com/Openwrt-Passwall/openwrt-passwall)
`⭐ Stars: 10,006` &nbsp;|&nbsp; `💻 语言: Lua` &nbsp;|&nbsp; `🏷️ 最新版本: [26.11.11-1](https://github.com/Openwrt-Passwall/openwrt-passwall/releases/tag/26.11.11-1) (2026-11-10)`

> **简介**：暂无项目描述

**💡 核心亮点更新 (中文)**：
* 请按照 [openwrt-passwall-build](https://github.com/moetayuko/openwrt-passwall-build) 仓库的说明，将其提供的软件源添加到设备中，然后直接使用包管理器安装。
* 从 [SourceForge](https://sourceforge.net/projects/openwrt-passwall-build/files/) 下载预构建的软件包。
* 将文件上传到您的设备，使用 Shell 命令进行安装。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
![](https://img.shields.io/github/downloads/Openwrt-Passwall/openwrt-passwall/26.11.11-1/total?style=flat-square)
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

## 🛑 建议清理 / 放弃维护项目

<details>
<summary>⚠️ 点击展开已放弃维护或超过 1 年停更的仓库清单 (138 个)</summary>

| 仓库名称 | Stars | 状态说明 | 操作建议 |
| :--- | :---: | :--- | :---: |
| [remotely-save/remotely-save](https://github.com/remotely-save/remotely-save) | 8,328 | 超过 737 天无代码提交 | [进入取消 Star](https://github.com/remotely-save/remotely-save) |
| [cityflow-project/CityFlow](https://github.com/cityflow-project/CityFlow) | 1,034 | 超过 454 天无代码提交 | [进入取消 Star](https://github.com/cityflow-project/CityFlow) |
| [facebookresearch/demucs](https://github.com/facebookresearch/demucs) | 10,414 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/facebookresearch/demucs) |
| [fufankeji/DeepSeek-OCR-Web](https://github.com/fufankeji/DeepSeek-OCR-Web) | 570 | 超过 386 天无代码提交 | [进入取消 Star](https://github.com/fufankeji/DeepSeek-OCR-Web) |
| [JimmyLv/awesome-nano-banana](https://github.com/JimmyLv/awesome-nano-banana) | 8,792 | 超过 434 天无代码提交 | [进入取消 Star](https://github.com/JimmyLv/awesome-nano-banana) |
| [btjawa/BiliTools](https://github.com/btjawa/BiliTools) | 4,990 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/btjawa/BiliTools) |
| [ehang-io/nps](https://github.com/ehang-io/nps) | 34,254 | 超过 901 天无代码提交 | [进入取消 Star](https://github.com/ehang-io/nps) |
| [ReturnFI/Blitz](https://github.com/ReturnFI/Blitz) | 1,086 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/ReturnFI/Blitz) |
| [kkangert/kspider](https://github.com/kkangert/kspider) | 1,262 | 超过 820 天无代码提交 | [进入取消 Star](https://github.com/kkangert/kspider) |
| [xenova/whisper-web](https://github.com/xenova/whisper-web) | 3,345 | 超过 777 天无代码提交 | [进入取消 Star](https://github.com/xenova/whisper-web) |
| [shadowsocks/luci-app-shadowsocks](https://github.com/shadowsocks/luci-app-shadowsocks) | 1,150 | 超过 1268 天无代码提交 | [进入取消 Star](https://github.com/shadowsocks/luci-app-shadowsocks) |
| [sinaptik-ai/pandas-ai](https://github.com/sinaptik-ai/pandas-ai) | 23,955 | 超过 385 天无代码提交 | [进入取消 Star](https://github.com/sinaptik-ai/pandas-ai) |
| [adithya-s-k/marker-api](https://github.com/adithya-s-k/marker-api) | 979 | 超过 762 天无代码提交 | [进入取消 Star](https://github.com/adithya-s-k/marker-api) |
| [yuchannslv5/warpflare](https://github.com/yuchannslv5/warpflare) | 335 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/yuchannslv5/warpflare) |
| [vvbbnn00/WARP-Clash-API](https://github.com/vvbbnn00/WARP-Clash-API) | 8,793 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/vvbbnn00/WARP-Clash-API) |
| [chika0801/hysteria-install](https://github.com/chika0801/hysteria-install) | 177 | 超过 865 天无代码提交 | [进入取消 Star](https://github.com/chika0801/hysteria-install) |
| [yeahwu/InstallOS](https://github.com/yeahwu/InstallOS) | 86 | 超过 1622 天无代码提交 | [进入取消 Star](https://github.com/yeahwu/InstallOS) |
| [bulianglin/psub](https://github.com/bulianglin/psub) | 1,756 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/bulianglin/psub) |
| [chatchat-space/Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat) | 38,714 | 超过 372 天无代码提交 | [进入取消 Star](https://github.com/chatchat-space/Langchain-Chatchat) |
| [lizongying/my-tv](https://github.com/lizongying/my-tv) | 31,949 | 超过 880 天无代码提交 | [进入取消 Star](https://github.com/lizongying/my-tv) |
| [joevess/IPTV](https://github.com/joevess/IPTV) | 10,275 | 超过 685 天无代码提交 | [进入取消 Star](https://github.com/joevess/IPTV) |
| [lecepin/WeChatVideoDownloader](https://github.com/lecepin/WeChatVideoDownloader) | 4,659 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/lecepin/WeChatVideoDownloader) |
| [linexjlin/GPTs](https://github.com/linexjlin/GPTs) | 32,015 | 超过 781 天无代码提交 | [进入取消 Star](https://github.com/linexjlin/GPTs) |
| [imDazui/Tvlist-awesome-m3u-m3u8](https://github.com/imDazui/Tvlist-awesome-m3u-m3u8) | 30,407 | 超过 368 天无代码提交 | [进入取消 Star](https://github.com/imDazui/Tvlist-awesome-m3u-m3u8) |
| [lxfater/Awesome-GPTs](https://github.com/lxfater/Awesome-GPTs) | 1,155 | 超过 1091 天无代码提交 | [进入取消 Star](https://github.com/lxfater/Awesome-GPTs) |
| [ClashDotNetFramework/experimental-clash](https://github.com/ClashDotNetFramework/experimental-clash) | 241 | 超过 1807 天无代码提交 | [进入取消 Star](https://github.com/ClashDotNetFramework/experimental-clash) |
| [zzzgydi/clash-verge](https://github.com/zzzgydi/clash-verge) | 21,849 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/zzzgydi/clash-verge) |
| [ddgth/cf2dns](https://github.com/ddgth/cf2dns) | 5,215 | 超过 680 天无代码提交 | [进入取消 Star](https://github.com/ddgth/cf2dns) |
| [zizifn/edgetunnel](https://github.com/zizifn/edgetunnel) | 9,339 | 超过 720 天无代码提交 | [进入取消 Star](https://github.com/zizifn/edgetunnel) |
| [missuo/Hysteria2](https://github.com/missuo/Hysteria2) | 204 | 超过 810 天无代码提交 | [进入取消 Star](https://github.com/missuo/Hysteria2) |
| [Misaka-blog/hysteria-install](https://github.com/Misaka-blog/hysteria-install) | 630 | 超过 942 天无代码提交 | [进入取消 Star](https://github.com/Misaka-blog/hysteria-install) |
| [MatsuriDayo/nekoray](https://github.com/MatsuriDayo/nekoray) | 15,236 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/MatsuriDayo/nekoray) |
| [FranzKafkaYu/x-ui](https://github.com/FranzKafkaYu/x-ui) | 8,429 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/FranzKafkaYu/x-ui) |
| [rwv/chinese-dos-games](https://github.com/rwv/chinese-dos-games) | 10,357 | 超过 832 天无代码提交 | [进入取消 Star](https://github.com/rwv/chinese-dos-games) |
| [getumbrel/llama-gpt](https://github.com/getumbrel/llama-gpt) | 10,924 | 超过 937 天无代码提交 | [进入取消 Star](https://github.com/getumbrel/llama-gpt) |
| [WangWenBin2017/OpenWrt-SSRPLUS](https://github.com/WangWenBin2017/OpenWrt-SSRPLUS) | 560 | 超过 624 天无代码提交 | [进入取消 Star](https://github.com/WangWenBin2017/OpenWrt-SSRPLUS) |
| [prompt-engineering/click-prompt](https://github.com/prompt-engineering/click-prompt) | 2,386 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/prompt-engineering/click-prompt) |
| [AutodeskAILab/Building-GAN](https://github.com/AutodeskAILab/Building-GAN) | 100 | 超过 1627 天无代码提交 | [进入取消 Star](https://github.com/AutodeskAILab/Building-GAN) |
| [novicezk/midjourney-proxy](https://github.com/novicezk/midjourney-proxy) | 5,375 | 超过 471 天无代码提交 | [进入取消 Star](https://github.com/novicezk/midjourney-proxy) |
| [adams549659584/go-proxy-bingai](https://github.com/adams549659584/go-proxy-bingai) | 8,392 | 超过 972 天无代码提交 | [进入取消 Star](https://github.com/adams549659584/go-proxy-bingai) |
| [tryptech/obs-zoom-and-follow](https://github.com/tryptech/obs-zoom-and-follow) | 441 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/tryptech/obs-zoom-and-follow) |
| [XingangPan/DragGAN](https://github.com/XingangPan/DragGAN) | 35,689 | 超过 912 天无代码提交 | [进入取消 Star](https://github.com/XingangPan/DragGAN) |
| [lewangdev/faster-whisper-youtube](https://github.com/lewangdev/faster-whisper-youtube) | 558 | 超过 1185 天无代码提交 | [进入取消 Star](https://github.com/lewangdev/faster-whisper-youtube) |
| [artidoro/qlora](https://github.com/artidoro/qlora) | 11,069 | 超过 889 天无代码提交 | [进入取消 Star](https://github.com/artidoro/qlora) |
| [langgenius/webapp-conversation](https://github.com/langgenius/webapp-conversation) | 1,101 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/langgenius/webapp-conversation) |
| [3andne/restls](https://github.com/3andne/restls) | 378 | 超过 1108 天无代码提交 | [进入取消 Star](https://github.com/3andne/restls) |
| [jtsang4/claude-to-chatgpt](https://github.com/jtsang4/claude-to-chatgpt) | 1,299 | 超过 821 天无代码提交 | [进入取消 Star](https://github.com/jtsang4/claude-to-chatgpt) |
| [yorunning/clash-conf](https://github.com/yorunning/clash-conf) | 104 | 超过 853 天无代码提交 | [进入取消 Star](https://github.com/yorunning/clash-conf) |
| [svc-develop-team/so-vits-svc](https://github.com/svc-develop-team/so-vits-svc) | 28,031 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/svc-develop-team/so-vits-svc) |
| [xiaye13579/BBLL](https://github.com/xiaye13579/BBLL) | 17,515 | 超过 627 天无代码提交 | [进入取消 Star](https://github.com/xiaye13579/BBLL) |
| [camenduru/MiniGPT-4-colab](https://github.com/camenduru/MiniGPT-4-colab) | 120 | 超过 1205 天无代码提交 | [进入取消 Star](https://github.com/camenduru/MiniGPT-4-colab) |
| [Vision-CAIR/MiniGPT-4](https://github.com/Vision-CAIR/MiniGPT-4) | 25,559 | 超过 806 天无代码提交 | [进入取消 Star](https://github.com/Vision-CAIR/MiniGPT-4) |
| [imfuxiao/Hamster](https://github.com/imfuxiao/Hamster) | 1,644 | 超过 553 天无代码提交 | [进入取消 Star](https://github.com/imfuxiao/Hamster) |
| [acheong08/ChatGPT](https://github.com/acheong08/ChatGPT) | 27,998 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/acheong08/ChatGPT) |
| [microsoft/JARVIS](https://github.com/microsoft/JARVIS) | 25,680 | 超过 475 天无代码提交 | [进入取消 Star](https://github.com/microsoft/JARVIS) |
| [choephix/auto-gpt-webui](https://github.com/choephix/auto-gpt-webui) | 116 | 超过 973 天无代码提交 | [进入取消 Star](https://github.com/choephix/auto-gpt-webui) |
| [facebookresearch/segment-anything](https://github.com/facebookresearch/segment-anything) | 55,145 | 超过 789 天无代码提交 | [进入取消 Star](https://github.com/facebookresearch/segment-anything) |
| [zai-org/ChatGLM-6B](https://github.com/zai-org/ChatGLM-6B) | 40,846 | 超过 873 天无代码提交 | [进入取消 Star](https://github.com/zai-org/ChatGLM-6B) |
| [ihciah/shadow-tls](https://github.com/ihciah/shadow-tls) | 2,682 | 超过 570 天无代码提交 | [进入取消 Star](https://github.com/ihciah/shadow-tls) |
| [jxbbb/ADAPT](https://github.com/jxbbb/ADAPT) | 421 | 超过 889 天无代码提交 | [进入取消 Star](https://github.com/jxbbb/ADAPT) |
| [mayooear/ai-pdf-chatbot-langchain](https://github.com/mayooear/ai-pdf-chatbot-langchain) | 16,580 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/mayooear/ai-pdf-chatbot-langchain) |
| [lencx/ChatGPT](https://github.com/lencx/ChatGPT) | 54,669 | 超过 809 天无代码提交 | [进入取消 Star](https://github.com/lencx/ChatGPT) |
| [nekohasekai/SagerNet](https://github.com/nekohasekai/SagerNet) | 56 | 超过 1772 天无代码提交 | [进入取消 Star](https://github.com/nekohasekai/SagerNet) |
| [P3TERX/Actions-OpenWrt](https://github.com/P3TERX/Actions-OpenWrt) | 7,611 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/P3TERX/Actions-OpenWrt) |
| [R86S/R86S-QuickInstaller](https://github.com/R86S/R86S-QuickInstaller) | 64 | 超过 1193 天无代码提交 | [进入取消 Star](https://github.com/R86S/R86S-QuickInstaller) |
| [WeNeedHome/SummaryOfLoanSuspension](https://github.com/WeNeedHome/SummaryOfLoanSuspension) | 20,314 | 超过 857 天无代码提交 | [进入取消 Star](https://github.com/WeNeedHome/SummaryOfLoanSuspension) |
| [zanzhz1101/LingMaxDNS](https://github.com/zanzhz1101/LingMaxDNS) | 23 | 超过 1588 天无代码提交 | [进入取消 Star](https://github.com/zanzhz1101/LingMaxDNS) |
| [IrineSistiana/mosdns-cn](https://github.com/IrineSistiana/mosdns-cn) | 324 | 超过 1630 天无代码提交 | [进入取消 Star](https://github.com/IrineSistiana/mosdns-cn) |
| [chika0801/Xray-install](https://github.com/chika0801/Xray-install) | 271 | 超过 1081 天无代码提交 | [进入取消 Star](https://github.com/chika0801/Xray-install) |
| [scutan90/DeepLearning-500-questions](https://github.com/scutan90/DeepLearning-500-questions) | 57,716 | 超过 873 天无代码提交 | [进入取消 Star](https://github.com/scutan90/DeepLearning-500-questions) |
| [Chikage0o0/Linux-NetSpeed](https://github.com/Chikage0o0/Linux-NetSpeed) | 3,737 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/Chikage0o0/Linux-NetSpeed) |
| [KFERMercer/OpenWrt-CI](https://github.com/KFERMercer/OpenWrt-CI) | 1,407 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/KFERMercer/OpenWrt-CI) |
| [qTox/qTox](https://github.com/qTox/qTox) | 4,970 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/qTox/qTox) |
| [quericy/one-key-ikev2-vpn](https://github.com/quericy/one-key-ikev2-vpn) | 2,105 | 超过 2192 天无代码提交 | [进入取消 Star](https://github.com/quericy/one-key-ikev2-vpn) |
| [riverscn/openwrt-iptvhelper](https://github.com/riverscn/openwrt-iptvhelper) | 371 | 超过 1908 天无代码提交 | [进入取消 Star](https://github.com/riverscn/openwrt-iptvhelper) |
| [frainzy1477/luci-app-clash](https://github.com/frainzy1477/luci-app-clash) | 1,621 | 超过 1698 天无代码提交 | [进入取消 Star](https://github.com/frainzy1477/luci-app-clash) |
| [Sanster/IOPaint](https://github.com/Sanster/IOPaint) | 23,288 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/Sanster/IOPaint) |
| [LANDrop/LANDrop](https://github.com/LANDrop/LANDrop) | 5,999 | 超过 825 天无代码提交 | [进入取消 Star](https://github.com/LANDrop/LANDrop) |
| [saveweb/review-2021](https://github.com/saveweb/review-2021) | 756 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/saveweb/review-2021) |
| [iranee/qnap-aliyunpan-webdav](https://github.com/iranee/qnap-aliyunpan-webdav) | 273 | 超过 1501 天无代码提交 | [进入取消 Star](https://github.com/iranee/qnap-aliyunpan-webdav) |
| [haoel/haoel.github.io](https://github.com/haoel/haoel.github.io) | 13,082 | 超过 1286 天无代码提交 | [进入取消 Star](https://github.com/haoel/haoel.github.io) |
| [tindy2013/stairspeedtest-reborn](https://github.com/tindy2013/stairspeedtest-reborn) | 3,820 | 超过 1258 天无代码提交 | [进入取消 Star](https://github.com/tindy2013/stairspeedtest-reborn) |
| [P3TERX/warp.sh](https://github.com/P3TERX/warp.sh) | 3,918 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/P3TERX/warp.sh) |
| [TheMRLL/WinXray](https://github.com/TheMRLL/WinXray) | 2,785 | 超过 994 天无代码提交 | [进入取消 Star](https://github.com/TheMRLL/WinXray) |
| [Mikubill/cowtransfer-uploader](https://github.com/Mikubill/cowtransfer-uploader) | 448 | 超过 1741 天无代码提交 | [进入取消 Star](https://github.com/Mikubill/cowtransfer-uploader) |
| [281677160/build-actions](https://github.com/281677160/build-actions) | 388 | 超过 476 天无代码提交 | [进入取消 Star](https://github.com/281677160/build-actions) |
| [vaxilu/x-ui](https://github.com/vaxilu/x-ui) | 19,074 | 超过 820 天无代码提交 | [进入取消 Star](https://github.com/vaxilu/x-ui) |
| [xinntao/Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) | 37,542 | 超过 832 天无代码提交 | [进入取消 Star](https://github.com/xinntao/Real-ESRGAN) |
| [zu1k/proxypool](https://github.com/zu1k/proxypool) | 4,041 | 超过 1316 天无代码提交 | [进入取消 Star](https://github.com/zu1k/proxypool) |
| [TachibanaYoshino/AnimeGAN](https://github.com/TachibanaYoshino/AnimeGAN) | 4,609 | 超过 1566 天无代码提交 | [进入取消 Star](https://github.com/TachibanaYoshino/AnimeGAN) |
| [yuanzhoulvpi2017/tiny_python](https://github.com/yuanzhoulvpi2017/tiny_python) | 173 | 超过 1381 天无代码提交 | [进入取消 Star](https://github.com/yuanzhoulvpi2017/tiny_python) |
| [haiibo/OpenWrt](https://github.com/haiibo/OpenWrt) | 3,162 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/haiibo/OpenWrt) |
| [VergilGao/openwrt-packages](https://github.com/VergilGao/openwrt-packages) | 11 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/VergilGao/openwrt-packages) |
| [VergilGao/openwrt-compiler](https://github.com/VergilGao/openwrt-compiler) | 13 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/VergilGao/openwrt-compiler) |
| [OpenELEC/OpenELEC.tv](https://github.com/OpenELEC/OpenELEC.tv) | 1,619 | 超过 3363 天无代码提交 | [进入取消 Star](https://github.com/OpenELEC/OpenELEC.tv) |
| [github/copilot-docs](https://github.com/github/copilot-docs) | 23,158 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/github/copilot-docs) |
| [Kiougar/luci-wrtbwmon](https://github.com/Kiougar/luci-wrtbwmon) | 355 | 超过 1880 天无代码提交 | [进入取消 Star](https://github.com/Kiougar/luci-wrtbwmon) |
| [EtherDream/jsproxy](https://github.com/EtherDream/jsproxy) | 9,317 | 超过 961 天无代码提交 | [进入取消 Star](https://github.com/EtherDream/jsproxy) |
| [cheat-engine/cheat-engine](https://github.com/cheat-engine/cheat-engine) | 19,486 | 超过 577 天无代码提交 | [进入取消 Star](https://github.com/cheat-engine/cheat-engine) |
| [ffffffff0x/Dork-Admin](https://github.com/ffffffff0x/Dork-Admin) | 1,914 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/ffffffff0x/Dork-Admin) |
| [ffffffff0x/Digital-Privacy](https://github.com/ffffffff0x/Digital-Privacy) | 4,935 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/ffffffff0x/Digital-Privacy) |
| [Autodesk/civilconnection](https://github.com/Autodesk/civilconnection) | 121 | 超过 1446 天无代码提交 | [进入取消 Star](https://github.com/Autodesk/civilconnection) |
| [0xHJK/CleanApps](https://github.com/0xHJK/CleanApps) | 165 | 超过 1912 天无代码提交 | [进入取消 Star](https://github.com/0xHJK/CleanApps) |
| [KANIKIG/Multi-EasyGost](https://github.com/KANIKIG/Multi-EasyGost) | 1,942 | 超过 960 天无代码提交 | [进入取消 Star](https://github.com/KANIKIG/Multi-EasyGost) |
| [Kurokosama/AutoBuild-OpenWRT](https://github.com/Kurokosama/AutoBuild-OpenWRT) | 88 | 超过 1599 天无代码提交 | [进入取消 Star](https://github.com/Kurokosama/AutoBuild-OpenWRT) |
| [differentrain/DeletionTool](https://github.com/differentrain/DeletionTool) | 94 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/differentrain/DeletionTool) |
| [hideuvpn/android-google-play-store](https://github.com/hideuvpn/android-google-play-store) | 3,688 | 超过 1581 天无代码提交 | [进入取消 Star](https://github.com/hideuvpn/android-google-play-store) |
| [XJP-GIT/AntiZhaPian](https://github.com/XJP-GIT/AntiZhaPian) | 3,162 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/XJP-GIT/AntiZhaPian) |
| [jerrykuku/luci-app-ttnode](https://github.com/jerrykuku/luci-app-ttnode) | 89 | 超过 1757 天无代码提交 | [进入取消 Star](https://github.com/jerrykuku/luci-app-ttnode) |
| [KevinSHIT/NaiveSharp](https://github.com/KevinSHIT/NaiveSharp) | 97 | 超过 2202 天无代码提交 | [进入取消 Star](https://github.com/KevinSHIT/NaiveSharp) |
| [prasmussen/gdrive](https://github.com/prasmussen/gdrive) | 8,939 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/prasmussen/gdrive) |
| [tostercx/GTAO_Booster_PoC](https://github.com/tostercx/GTAO_Booster_PoC) | 2,862 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/tostercx/GTAO_Booster_PoC) |
| [ilxp/luci-app-ikoolproxy](https://github.com/ilxp/luci-app-ikoolproxy) | 502 | 超过 613 天无代码提交 | [进入取消 Star](https://github.com/ilxp/luci-app-ikoolproxy) |
| [kiddin9/luci-app-dnsfilter](https://github.com/kiddin9/luci-app-dnsfilter) | 124 | 超过 646 天无代码提交 | [进入取消 Star](https://github.com/kiddin9/luci-app-dnsfilter) |
| [h31105/deployX.sh](https://github.com/h31105/deployX.sh) | 417 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/h31105/deployX.sh) |
| [jerrykuku/openwrt-package](https://github.com/jerrykuku/openwrt-package) | 147 | 超过 1109 天无代码提交 | [进入取消 Star](https://github.com/jerrykuku/openwrt-package) |
| [frainzy1477/luci-app-trojan](https://github.com/frainzy1477/luci-app-trojan) | 120 | 超过 2017 天无代码提交 | [进入取消 Star](https://github.com/frainzy1477/luci-app-trojan) |
| [atrandys/xray](https://github.com/atrandys/xray) | 89 | 超过 1724 天无代码提交 | [进入取消 Star](https://github.com/atrandys/xray) |
| [v2board/v2board](https://github.com/v2board/v2board) | 5,065 | 超过 973 天无代码提交 | [进入取消 Star](https://github.com/v2board/v2board) |
| [ShadowsocksR-Live/iShadowsocksR](https://github.com/ShadowsocksR-Live/iShadowsocksR) | 601 | 超过 931 天无代码提交 | [进入取消 Star](https://github.com/ShadowsocksR-Live/iShadowsocksR) |
| [SuperNG6/Aria2-Trackers](https://github.com/SuperNG6/Aria2-Trackers) | 308 | 超过 2123 天无代码提交 | [进入取消 Star](https://github.com/SuperNG6/Aria2-Trackers) |
| [kakaruoterl/vless_install](https://github.com/kakaruoterl/vless_install) | 29 | 超过 2280 天无代码提交 | [进入取消 Star](https://github.com/kakaruoterl/vless_install) |
| [stupidloud/nanopi-openwrt](https://github.com/stupidloud/nanopi-openwrt) | 5,506 | 超过 944 天无代码提交 | [进入取消 Star](https://github.com/stupidloud/nanopi-openwrt) |
| [atrandys/trojan](https://github.com/atrandys/trojan) | 1,056 | 超过 1313 天无代码提交 | [进入取消 Star](https://github.com/atrandys/trojan) |
| [programthink/zhao](https://github.com/programthink/zhao) | 14,170 | 超过 1933 天无代码提交 | [进入取消 Star](https://github.com/programthink/zhao) |
| [RPRX/v2ray-vless](https://github.com/RPRX/v2ray-vless) | 390 | 超过 1359 天无代码提交 | [进入取消 Star](https://github.com/RPRX/v2ray-vless) |
| [h2y/Shadowrocket-ADBlock-Rules](https://github.com/h2y/Shadowrocket-ADBlock-Rules) | 16,738 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/h2y/Shadowrocket-ADBlock-Rules) |
| [p4gefau1t/trojan-go](https://github.com/p4gefau1t/trojan-go) | 8,388 | 超过 856 天无代码提交 | [进入取消 Star](https://github.com/p4gefau1t/trojan-go) |
| [Jrohy/trojan](https://github.com/Jrohy/trojan) | 5,627 | 超过 946 天无代码提交 | [进入取消 Star](https://github.com/Jrohy/trojan) |
| [mellow-io/mellow](https://github.com/mellow-io/mellow) | 3,536 | 超过 1437 天无代码提交 | [进入取消 Star](https://github.com/mellow-io/mellow) |
| [Dawneng/luci-theme-atmaterial](https://github.com/Dawneng/luci-theme-atmaterial) | 11 | 超过 1489 天无代码提交 | [进入取消 Star](https://github.com/Dawneng/luci-theme-atmaterial) |
| [trojan-gfw/igniter](https://github.com/trojan-gfw/igniter) | 3,275 | 超过 1086 天无代码提交 | [进入取消 Star](https://github.com/trojan-gfw/igniter) |
| [openwrt-develop/luci-theme-atmaterial](https://github.com/openwrt-develop/luci-theme-atmaterial) | 68 | 超过 2434 天无代码提交 | [进入取消 Star](https://github.com/openwrt-develop/luci-theme-atmaterial) |
| [trojan-gfw/trojan-quickstart](https://github.com/trojan-gfw/trojan-quickstart) | 244 | 超过 2035 天无代码提交 | [进入取消 Star](https://github.com/trojan-gfw/trojan-quickstart) |
| [FunctionClub/ZBench](https://github.com/FunctionClub/ZBench) | 1,173 | 超过 2066 天无代码提交 | [进入取消 Star](https://github.com/FunctionClub/ZBench) |
| [veekxt/v2ray-template](https://github.com/veekxt/v2ray-template) | 748 | 超过 2278 天无代码提交 | [进入取消 Star](https://github.com/veekxt/v2ray-template) |
| [HMBSbige/ShadowsocksR-Windows](https://github.com/HMBSbige/ShadowsocksR-Windows) | 6,893 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/HMBSbige/ShadowsocksR-Windows) |
| [trojan-gfw/trojan](https://github.com/trojan-gfw/trojan) | 19,746 | 超过 818 天无代码提交 | [进入取消 Star](https://github.com/trojan-gfw/trojan) |
</details>
