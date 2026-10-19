# 📡 Starred 项目雷达看板
> **生成时间**：`2026-10-19` ｜ **关注项目总数**：`361` ｜ **本期更新**：`70` ｜ **弃坑预警**：`136`

| 统计指标 | 数量 | 状态提示 |
| :--- | :---: | :--- |
| 🌟 总关注库 | **361** | 监控运行中 |
| 🚀 近期有更新 | **70** | 涵盖 6 个分类 |
| 🛑 建议清理/弃坑 | **136** | 建议取消 Star 保持关注列表整洁 |

---
## 🧭 领域分类速览导航

- [🤖 AI 与智能体生态 (35)](#-AI-与智能体生态)
- [🎬 影音媒体与下载 (8)](#-影音媒体与下载)
- [📝 效率办公与创作 (8)](#-效率办公与创作)
- [🌐 网络与代理技术 (11)](#-网络与代理技术)
- [📦 实用开源精选 (6)](#-实用开源精选)
- [🛠️ 系统与开发者工具 (2)](#-系统与开发者工具)

---

## <span id="-AI-与智能体生态">🤖 AI 与智能体生态</span>

### 📦 [hypit-ai/hypit](https://github.com/hypit-ai/hypit)
`⭐ Stars: 23,788` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.3.1](https://github.com/hypit-ai/hypit/releases/tag/v0.3.1) (2026-10-09)`

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
`⭐ Stars: 18,261` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.0.6](https://github.com/HBAI-Ltd/Toonflow-app/releases/tag/v2.0.6) (2026-10-13)`

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
| 💻 Windows（64 位） | [⬇️ 下载 Windows 安装包](https://github.com/HBAI-Ltd/Toonflow-app/releases/download/v2.0.6/toonflow-2.0.6-Setup.exe) |
| 🍎 Mac（M 系列芯片） | [⬇️ 下载 M 系列 Mac 安装包](https://github.com/HBAI-Ltd/Toonflow-app/releases/download/v2.0.6/macos-arm64-toonflow.dmg) |
| 🍎 Mac（Intel 芯片） | [⬇️ 下载 Intel Mac 安装包](https://github.com/HBAI-Ltd/Toonflow-app/releases/download/v2.0.6/stable-macos-x64-toonflow.dmg) |
| 📱 Android（ARM64，Android 8 及以上） | [⬇️ 下载 Android APK](https://github.com/HBAI-Ltd/Toonflow-app/releases/download/v2.0.6/toonflow-2.0.6-android-arm64.apk) |

> 💡 手动安装请选择上表中的链接。下方其他文件供软件自动更新使用。

## 🚀 安装说明

- 💻 **Windows**：双击下载的安装包，按提示完成安装。
- 🍎 **Mac**：打开下载的安装包，将 `toonflow.app` 拖入“应用程序”，再从“应用程序”打开。
- 📱 **Android**：在手机上打开 APK，按系统提示允许此来源安装应用。后续版本可直接覆盖安装。

M 系列 Mac 安装包已完成 Developer ID 签名与 Apple 公证。首次打开时，macOS 仍可能提示确认打开从互联网下载的应用。

---


**Full Changelog**: https://github.com/HBAI-Ltd/Toonflow-app/compare/v2.0.5...v2.0.6
```
</details>

---
### 📦 [morluto/rea](https://github.com/morluto/rea)
`⭐ Stars: 329,661` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [rea-agents-6.7.0](https://github.com/morluto/rea/releases/tag/rea-agents-6.7.0) (2026-10-18)`

> **简介**：使用代理对任何内容进行逆向工程，从应用程序行为到本机二进制文件。

**💡 核心亮点更新 (中文)**：
- 客户端配置编辑遵循 MCP 客户端使用的重复成员语义。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## [6.7.0](https://github.com/morluto/rea/compare/rea-agents-6.6.0...rea-agents-6.7.0) (2026-10-18)

### Highlights

- Client configuration edits follow the duplicate-member semantics used by MCP clients.

### Changes

- Includes the [6.6.0 changes and migration notes](https://github.com/morluto/rea/releases/tag/rea-agents-6.6.0). That version was tagged but was not published to npm.

### Fixes

- **Client configuration:** Setup edits the last repeated JSON/JSONC member, matching the value clients actually read. Setup and uninstall refuse a removal that would reactivate a shadowed duplicate, preserving the original configuration. ([#4957](https://github.com/morluto/rea/pull/4957), [morluto/rea#4952](https://github.com/morluto/rea/issues/4952)). Thanks @kaoru0822-kitauji, @xu91102.

Full contribution record: [4 commits and 1 merged PR](https://github.com/morluto/rea/blob/rea-agents-6.7.0/docs/releases/6.7.0.contributions.json).

## [6.6.0](https://github.com/morluto/rea/compare/rea-agents-6.5.0...rea-agents-6.6.0) (2026-10-18)

### Highlights

- Add Kuna as a caller-supplied static-analysis provider.
- Query selected JavaScript facts and multiple APK locale tables without repeating the underlying analysis.
- Extend Ghidra analysis to Windows ARM PE targets and explicit raw m68k images.
- Preserve completed Evidence, cancellation reasons and retryable cleanup across provider and CLI finalization.

### Changes

- **Kuna analysis:** Use a caller-installed Kuna for procedure listi
```
</details>

---
### 📦 [chatfire-AI/huobao-drama](https://github.com/chatfire-AI/huobao-drama)
`⭐ Stars: 16,366` &nbsp;|&nbsp; `💻 语言: Vue` &nbsp;|&nbsp; `🏷️ 最新版本: [v4.0.8](https://github.com/chatfire-AI/huobao-drama/releases/tag/v4.0.8) (2026-10-05)`

> **简介**：🎬 火宝短剧 - 基于AI的一站式短剧生成平台 《一句话生成完整短剧，从剧本到成片全自动化》  Huobao Drama - An AI-Powered End-to-End Short Drama Generator "One Sentence to Complete Drama: Fully Automated from Script to Final Video"

**💡 核心亮点更新 (中文)**：
火宝快捷配置支持国内/国外节点选择：默认跟随界面语言（中文→firemux.cn，其他→firemux.com），一键写入的推荐配置与获取 Key 链接随节点生成

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
火宝快捷配置支持国内/国外节点选择：默认跟随界面语言（中文→firemux.cn，其他→firemux.com），一键写入的推荐配置与获取 Key 链接随节点生成
```
</details>

---
### 📦 [yetone/magpie](https://github.com/yetone/magpie)
`⭐ Stars: 16,646` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.1.1292](https://github.com/yetone/magpie/releases/tag/v0.1.1292) (2026-10-19)`

> **简介**：每个代理的模型。一处。来自菜单栏的 DeepSeek 上的 Codex、Kimi 上的 Claude Code。

**💡 核心亮点更新 (中文)**：
- 特工的名字现在出现在他们的图标旁边，使他们更容易识别。
- 登录字段和按钮现在具有相同的高度和均匀的间距。
- 修复了发送到 Kimi 的引用工具架构可能缺少其类型信息的问题。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Improvements
- Agent names now appear beside their icons, making them easier to identify.
- Sign-in fields and buttons are now the same height and evenly spaced.

## Bug Fixes
- Fixed an issue where referenced tool schemas sent to Kimi could be missing their type information.

### Install

Download from [usemagpie.ai](https://usemagpie.ai), or `curl -fsSL https://usemagpie.ai/install.sh | sh`. An installed magpie updates itself.

- **macOS (Apple Silicon):** `magpie-darwin-arm64.dmg`
- **macOS (Intel):** `magpie-darwin-amd64.dmg`
- **Windows:** `magpie-windows-amd64.exe` (ARM: `magpie-windows-arm64.exe`)
- **Linux:** `magpie-linux-amd64` / `magpie-linux-arm64` (needs GTK 3 and WebKitGTK 4.1)
- **Terminal only:** `magpie-cli-<os>-<arch>`

<!-- lang:zh -->

## Improvements
- 智能体名称现在显示在其图标旁边，使其更易于识别。
- 登录字段和按钮现在高度相同且间距均匀。

## Bug Fixes
- 修复了发送到 Kimi 的引用工具模式可能缺少其类型信息的问题。

### 安装

从 [usemagpie.ai](https://usemagpie.ai) 下载，或运行 `curl -fsSL https://usemagpie.ai/install.sh | sh`。已安装的 magpie 会自动更新。



---
The same release, and the feed magpie updates from: https://github.com/yetone/magpie-releases/releases/tag/v0.1.1292
```
</details>

---
### 📦 [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
`⭐ Stars: 255,097` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.22.2](https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.2) (2026-10-15)`

> **简介**：与您共同成长的代理商

**💡 核心亮点更新 (中文)**：
- **网关在重新启动后再次启动。** 重新启动后，Linux 可以将早期的 PID 交给不相关的进程，网关可能会将其误认为是正在运行的网关，因此受监督的网关（systemd、launchd、Docker）拒绝启动。 Hermes 现在会记录它启动的启动情况，当它无法判断时，它会询问主机锁，只有实时网关才拥有该主机锁。 ([#138594](https://github.com/NousResearch/hermes-agent/pull/138594)，修复[#133744](https://github.com/NousResearch/hermes-agent/issues/133744))
- **长本地模型轮流在笔记本电脑上生存。** 本地请求始终以提示读取进度进行流式传输（在状态行中显示），停顿计时器会跳过机器休眠的时间，恢复的本地服务器会进行另一次尝试，而不是在以后的每条消息中都失败的断路器，并且当服务器仍在读取长对话时，压缩不再超时。在 Windows 统一内存计算机上，模型启动和提示缓存的大小可用于释放内存。 ([#138560](https://github.com/NousResearch/hermes-agent/pull/138560))

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# Hermes Agent v0.22.2

**Release Date:** October 15, 2026

v0.22.1 was built from the wrong commit. It shipped unreleased gateway work, and the Microsoft Store app could stick on "Connecting." 0.22.2 is the release 0.22.1 was meant to be.

> **Known issue:** Sessions that ran under the 0.22.1 gateway can't be deleted in 0.22.2.

<!-- HERMES_BUILDS_TABLE -->

## Highlights

- **The gateway starts after a reboot again.** After a restart, Linux can hand an early PID to an unrelated process, and the gateway could mistake it for a running gateway, so a supervised gateway (systemd, launchd, Docker) refused to start. Hermes now records the boot it started in, and when it can't tell, it asks the host lock, which only a live gateway holds. ([#138594](https://github.com/NousResearch/hermes-agent/pull/138594), fixes [#133744](https://github.com/NousResearch/hermes-agent/issues/133744))
- **Long local-model turns survive on laptops.** Local requests always stream with prompt-reading progress (shown in the status line), stall timers skip time the machine was asleep, a recovered local server gets another try instead of a breaker that failed every later message, and compression no longer times out while the server is still reading a long conversation. On Windows unified-memory machines, model launch and the prompt cache are sized to free memory. ([#138560](https://github.com/NousResearch/hermes-agent/pull/138560))

Below is everything in the 0.22 release line since v0.22.0: the fixes 0.22.
```
</details>

---
### 📦 [Makememo/MemoAI](https://github.com/Makememo/MemoAI)
`⭐ Stars: 1,074` &nbsp;|&nbsp; `💻 语言: Other` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.8.8](https://github.com/Makememo/MemoAI/releases/tag/v1.8.8) (2026-10-09)`

> **简介**：MemoAI 视频翻译文本、字幕和注释变得简单。

**💡 核心亮点更新 (中文)**：
- 转录历史管理
- 添加了鼠标和键盘快捷键的自定义

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## New Features

- Transcription history management
- Added customization for mouse and keyboard shortcuts

## Improvements

- Added a sidebar quick-action panel to the transcription panel
- Updated the settings UI, simplified custom provider model fetching, and added balance queries for some providers

## Fixes

- Fixed custom LLM providers being unable to translate
```
</details>

---
### 📦 [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)
`⭐ Stars: 9,996` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.11.829](https://github.com/genspark-ai/genoffice/releases/tag/v0.11.829) (2026-10-15)`

> **简介**：免费的开源 AI Office 套件：带有内置 AI 代理的文档、表格、幻灯片、PDF、Markdown 和 HTML 编辑器，以及“genoffice”CLI 和代理技能，以便 Claude Code、Codex 和 Cursor 可以在本地创建和编辑真正的 .docx/.xlsx/.pptx 文件。带上你自己的钥匙。 macOS、Windows 和 Linux。

**💡 核心亮点更新 (中文)**：
- **文档：**“主页”选项卡和“文件”菜单中的“转换”菜单；插入表格单元格的图片保留在单元格中（由 报告；主页 > 边框格式化每个选定的单元格，而不仅仅是最后一个单元格（由 报告）；注释和跟踪更改的用户名设置，与表格和幻灯片共享（由 报告；邮件合并引擎和 MERGEFIELD 保留为带有超链接的字段，由 请求；状态栏显示所选/总单词，如 Word；隐藏模型中的选择；交互式思维导图在 AI 助手中；保存会保留插入符号所用的字体，编辑的段落会保留其注释引用格式；keepNext 链、页面锚定浮动表和缓存目录页码的行为与 Word 类似；单独的 autoSpaceDE/DN、编号制表符停止位；
- **工作表：** 使用 ROW()/COLUMN() 的条件格式公式是从 1 开始的，因此标题填充不再消失（由 报告）；Excel 错误文字不再读取为定义的名称；打印表保留其列宽；OpenDocument 文件 (.ods/.odt/.odp) 作为可编辑的 OOXML 副本打开。
- **幻灯片：** 根据 PowerPoint 测量的图表标题和图例几何形状、图表 userShapes 叠加、丰富的数据标签、小型大写字母、隐藏的轴线和线条图例键。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
GenOffice v0.11.829 stable desktop installers.

## What's New

- **Docs:** a Convert menu on the Home tab and in the File menu; a picture inserted into a table cell stays in the cell (reported by @cchamm); Home > Borders formats every selected cell, not just the last one (reported by @truongharper); a user name setting for comments and tracked changes, shared with Sheets and Slides (reported by @JustinJIA731); the mail-merge engine and MERGEFIELD kept as a field with its hyperlink (@tokg-venv, requested by @hou0); the status bar shows selected/total words like Word (@tokg-venv); hide a selection from the model (@tokg-venv); an interactive mind map in the AI assistant (@tokg-venv); a save keeps the font the caret is typed with and an edited paragraph keeps its note-reference formatting (@tokg-venv); paragraphs are pushed whole at equal-width column seams; keepNext chains, page-anchored floating tables and cached TOC page numbers behave like Word; Cambria Math, Calibri Arabic and Korean Latin metrics, separate autoSpaceDE/DN, numbering tab stops; the DFKai-SB PostScript alias maps to its family (@widechaos).
- **Sheets:** conditional-format formulas using ROW()/COLUMN() are 1-based, so header fills no longer vanish (reported by @rickygai); Excel error literals are no longer read as defined names; print tables keep their column widths; OpenDocument files (.ods/.odt/.odp) open as editable OOXML copies (@tokg-venv).
- **Slides:** chart title and legend geometry measured against Po
```
</details>

---
### 📦 [ruvnet/RuView](https://github.com/ruvnet/RuView)
`⭐ Stars: 98,726` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [ruview-harness-v0.9.2](https://github.com/ruvnet/RuView/releases/tag/ruview-harness-v0.9.2) (2026-10-12)`

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
`⭐ Stars: 24,976` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [@pascal-app/cli@1.0.4](https://github.com/pascalorg/editor/releases/tag/%40pascal-app/cli%401.0.4) (2026-10-13)`

> **简介**：开源 3D 建筑编辑器，具有本地 CLI、MCP 工具以及适用于人类和 AI 代理的实用工作流程。

**💡 核心亮点更新 (中文)**：
`@pascal-app/cli@1.0.4` 的 Pascal Web 编辑器运行时。当命令第一次启动编辑器时，CLI 会下载“pascal-web-runtime-1.0.4.tar.gz”，并根据 npm 包内发布的摘要进行验证。离线安装可以通过t

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
The Pascal web editor runtime for `@pascal-app/cli@1.0.4`. The CLI downloads `pascal-web-runtime-1.0.4.tar.gz` the first time a command starts the editor and verifies it against the digest published inside the npm package. Offline installs can pass the archive directly: `pascal editor --runtime pascal-web-runtime-1.0.4.tar.gz`.
```
</details>

---
### 📦 [librepods-org/librepods](https://github.com/librepods-org/librepods)
`⭐ Stars: 30,366` &nbsp;|&nbsp; `💻 语言: Kotlin` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.0.4](https://github.com/librepods-org/librepods/releases/tag/v1.0.4) (2026-10-16)`

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
`⭐ Stars: 38,525` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.11.12](https://github.com/linshenkx/prompt-optimizer/releases/tag/v2.11.12) (2026-10-19)`

> **简介**：人工智能提示优化器，用于编写更好的提示并获得更好的人工智能结果。

**💡 核心亮点更新 (中文)**：
- 将一种网络配置应用于桌面实例中的模型请求，包括模型发现、连接测试、提示优化以及文本和图像生成。
- 绕过精确域或通配符子域的代理。本地和私有 IP 地址直接连接。
- 连接测试显示请求是否使用直接连接、系统代理或手动代理。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## English

### Summary
- Add desktop model network settings for environments where company model endpoints require direct connections while other models need a proxy.
- Choose system, direct, or manual HTTP proxy routing and configure domain bypass rules under Model Manager → Network Settings.

### Highlights
- Apply one network configuration to model requests in the desktop instance, including model discovery, connection tests, prompt optimization, and text and image generation.
- Bypass proxies for exact domains or wildcard subdomains. Local and private IP addresses connect directly.
- Connection tests show whether the request used a direct connection, system proxy, or manual proxy.

### Product Updates
#### Desktop
- Add Network Settings to Model Manager, with system routing as the default.
- Support unauthenticated HTTP proxies in manual mode. System mode resolves system proxy and PAC rules for each target address.
- Save settings on the local machine and apply them after restarting the desktop app. Restarting from the settings window is blocked while model requests are running.
- Scope these settings to model requests. Application updates and cloud backups retain their existing network configuration.

#### Web
- No functional changes.

#### Extension
- No functional changes.

#### Core/Infra
- Remove duplicate language-switching links from the README.

### Fixes
- Allow company model endpoints to avoid an unsuitable system proxy through direct mode or domain bypass rule
```
</details>

---
### 📦 [RSSNext/Folo](https://github.com/RSSNext/Folo)
`⭐ Stars: 39,121` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [desktop/v1.16.0](https://github.com/RSSNext/Folo/releases/tag/desktop/v1.16.0) (2026-10-16)`

> **简介**：🧡 Folo is the AI RSS Reader

**💡 核心亮点更新 (中文)**：
- 双因素身份验证设置现在有一个“复制设置密钥”按钮，适用于无法扫描二维码的身份验证器应用程序
- Smoother timeline, sidebar, reader and AI chat: fewer re-renders while answers stream, entries update or the selection changes, and the search index is built only when search opens
- Much better keyboard and screen reader support: icon-only buttons, switches and window controls are named, and menus, pickers, the update notice and shortcut recording work from the keyboard

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# What's new in v1.16.0

## Shiny new things

- Two-factor authentication setup now has a "Copy setup key" button for authenticator apps that can't scan the QR code

## Improvements

- Smoother timeline, sidebar, reader and AI chat: fewer re-renders while answers stream, entries update or the selection changes, and the search index is built only when search opens
- Much better keyboard and screen reader support: icon-only buttons, switches and window controls are named, and menus, pickers, the update notice and shortcut recording work from the keyboard
- Clearer errors: the server's validation errors show under the field they concern, invalid handles, list titles, category names and regex patterns are explained, and a timeline, sidebar or entry that fails to load offers a retry
- Follow, inbox and action forms ask before closing with unsaved changes, and deleting a custom AI shortcut or integration asks first
- The window reopens on the display it was on, maximized if it was
- Typing a website address into Discover lists the site's feeds, and a new feed address opens its preview
- The entry list follows your Date Format setting
- Features that need a paid plan, such as hiding a list from the timeline, following a list privately, BYOK and AI tasks, are now labeled and offer an upgrade
- Exported files are named after Folo, such as folo.opml

## No longer broken

- Fixed timelines opened from Discover, the AI page and other pages showing the wrong view with an empty header and
```
</details>

---
### 📦 [roboflow/supervision](https://github.com/roboflow/supervision)
`⭐ Stars: 51,247` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [0.31.0](https://github.com/roboflow/supervision/releases/tag/0.31.0) (2026-10-16)`

> **简介**：我们为您编写可重复使用的计算机视觉工具。 💜

**💡 核心亮点更新 (中文)**：
- **`sv.DepthMap`** 测量任何图像上每个检测的距离和颜色深度，无需 OpenCV。
- **`PolygonZone`** 和`LineZone` 在相机平移时在正确的位置继续计数。
- **`KeyPointMeanAveragePrecision`** 按照 `pycocotools` 的方式对姿势模型进行评分。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# v0.31.0 — Depth, moving cameras and pose mAP

supervision now sees depth: load depth maps from your model or stereo rig, measure how far each object is, and draw the map.

- **`sv.DepthMap`** measures the distance to every detection and colours depth over any image, no OpenCV needed.
- **`PolygonZone`** and `LineZone` keep counting in the right place while the camera pans.
- **`KeyPointMeanAveragePrecision`** scores pose models the way `pycocotools` does.
- **Kosmos-2**, Gemini 3.6/3.7 and MediaPipe hands now load straight into `Detections` and `KeyPoints`.
- **`MeanAveragePrecision`** runs far faster on crowded images and lets you raise the detection cap.

It's a drop-in upgrade if 0.30.x showed you no deprecation warnings, apart from four output changes. `sv.ByteTrack` with the `supervision.tracker` package, `supervision.keypoint`, `sv.LMM`, the legacy `sv.MeanAveragePrecision` and a few helpers are gone; the Migration guide has the swaps.

## ✨ Spotlights / highlights

<img width="950" height="543" alt="image" src="https://github.com/user-attachments/assets/b3eec2cf-ae25-43ba-8494-aec69766991b" />

### Depth maps: load, measure and draw

`sv.DepthMap` holds metric depth, stereo disparity or relative depth for one frame, and keeps track of which one it is. `sv.DepthCamera` converts disparity to metres, `measure_detections` writes the median depth under each object to `detections.data` (`"depth_m"` when the map can give metres), and `sv.DepthAnnotator` co
```
</details>

---
### 📦 [MetaCubeX/mihomo](https://github.com/MetaCubeX/mihomo)
`⭐ Stars: 34,998` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.19.32](https://github.com/MetaCubeX/mihomo/releases/tag/v1.19.32) (2026-09-30)`

> **简介**：Honkai 的简单 Python Pydantic 模型：Star Rail 解析来自 Mihomo API 的数据。

**💡 核心亮点更新 (中文)**：
* 3025efad feat：添加负载平衡哈希键以将会话固定在入站用户上（#3133）

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## What's Changed
* 3025efad feat: add load-balance hash-key to pin a session on the inbound user (#3133) by @简直蠢丶

## BUG & Fix
* 409ee57e fix: populate HWCap from auxv on linux by @artbred
* 41b8a059 fix: account for TCP options in effective MSS by @wwqgtxx
* 5019cc09 fix: potential race condition in c.idleSession.Len() in idleCleanupExpTime() for anytls (#3225) by @Chenx Dust
* 60f70cec fix: align unconnected UDP and raw IP ICMP errors with Linux for mipstack by @wwqgtxx
* 88dcbf7f fix: default listener tun to mips stack (#3264) by @Jiawen Geng
* 8d57a8c5 fix: exclude opcode from P_DATA_V1 AEAD additional data for OpenVPN (#3237) by @FlyingSB
* 8fa048d3 fix: half-close in sing-mux by @proxi
* ac652970 fix: nil pconn deref when ctx is canceled during h2 ClientConn setup by @BESTRUI
* afe94daf fix: set udp InUser metadata for mieru inbound (#3236) by @Ryoma Dev
* fbb67422 fix: restart EasyTier outbound after silent overlay failure (#3215) by @MiaM1ku

## Maintenance
* 13417699 chore: support RX checksum offload for mipstack by @wwqgtxx
* 3c947c76 chore: convert support xhttp `extra.headers` (#3230) by @Peter Solomon
* 63bd52ec chore: change default IP stack mode to mips and support `congestion-controller` option for tun by @wwqgtxx
* 91dd03a9 chore: support lazy receive buffer reads for mipstack and gvisor by @wwqgtxx
* f103639c chore: update mieru version (#3242) by @enfein

**Full Changelog**: https://github.com/MetaCubeX/mihomo/compare/v1.19.31...v1.19.32
```
</details>

---
### 📦 [microsoft/graphrag](https://github.com/microsoft/graphrag)
`⭐ Stars: 36,383` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.3.0](https://github.com/microsoft/graphrag/releases/tag/v3.3.0) (2026-10-08)`

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
`⭐ Stars: 152,436` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.5.8](https://github.com/clash-verge-rev/clash-verge-rev/releases/tag/v2.5.8) (2026-10-09)`

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
`⭐ Stars: 78,243` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.1.908-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.908-beta) (2026-10-15)`

> **简介**：用于运行和训练法学硕士和扩散模型的本地 UI。支持 GGUF、MLX、Qwen3.8、DeepSeek-V4、MiniMax-H3、Gemma 4、FLUX 等。

**💡 核心亮点更新 (中文)**：
- **NVIDIA Nemotron 3.5 Bolt**：在 24 GB 内存上运行。 [指南](https://unsloth.ai/docs/models/nemotron-3.5-bolt)
- **NVIDIA Nemotron 3.5 Super VL**：120B（12B 活动）[指南](https://unsloth.ai/docs/models/nemotron-3.5-super-vl)
- **Meta Muse Spark Open**：816B（42.7B 活动）- 在 256GB 上运行 [指南](https://unsloth.ai/docs/models/muse-spark-open)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Run NVIDIA's new Nemotron 3.5 models and Meta's new Muse Spark Open locally in Unsloth. New: text-diffusion LLMs, DeepSpeed training and better prompt caching for coding agents.

## Highlights

- **NVIDIA Nemotron 3.5 Bolt**: Run on 24 GB of memory. [Guide](https://unsloth.ai/docs/models/nemotron-3.5-bolt)
- **NVIDIA Nemotron 3.5 Super VL**: 120B (12B active) [Guide](https://unsloth.ai/docs/models/nemotron-3.5-super-vl)
- **Meta Muse Spark Open**: 816B (42.7B active) - runs on 256GB [Guide](https://unsloth.ai/docs/models/muse-spark-open)
- **Better prompt caching for coding agents**: Claude Code, Codex etc. on local GGUF models re-process far less of each prompt.
- **Browser use**: Always allow properly works, cursor, and separate tabs for each chat.
- **Images through your connections**: generate with sd-server, Ollama, Lemonade and other image servers.
- **Diffusion LLMs**: train and chat with LLaDA, Dream, SDAR and more, with a live denoising canvas.

## Nemotron 3.5

- Run NVIDIA Nemotron 3.5 Super VL, a 120B model with 12B active parameters and up to 1M tokens of context, built for document understanding, computer use and long-running agents. Super VL runs in about 64 GB of memory at 1-bit, or 128 GB at 4-bit. [Guide](https://unsloth.ai/docs/models/nemotron-3.5-super-vl) · [GGUF](https://huggingface.co/unsloth/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF)
- Run NVIDIA Nemotron 3.5 Bolt, a 74B model with 9B active parameters and 128K context, compressed from
```
</details>

---
### 📦 [arc53/DocsGPT](https://github.com/arc53/DocsGPT)
`⭐ Stars: 18,323` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [1.0.0](https://github.com/arc53/DocsGPT/releases/tag/1.0.0) (2026-10-08)`

> **简介**：用于代理、助理和企业搜索的私人人工智能平台。内置代理生成器、深入研究、文档分析、多模型支持以及代理的 API 连接。

**💡 核心亮点更新 (中文)**：
* Guardrail 文档位于 https://github.com/arc53/DocsGPT/pull/2785
* feat(widget)：将搜索栏与小部件主题对齐，通过 https://github.com/arc53/DocsGPT/pull/2782 添加语音搜索
* 重构（设置）：拆分为每个域模块，通过 https://github.com/arc53/DocsGPT/pull/2802 生成设置参考

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## What's Changed
* Guardrail docs by @pabik in https://github.com/arc53/DocsGPT/pull/2785
* feat(widget): align search bar with widget theme, add voice search by @ManishMadan2882 in https://github.com/arc53/DocsGPT/pull/2782
* refactor(settings): split into per-domain modules, generate the settings reference by @arc53-machine in https://github.com/arc53/DocsGPT/pull/2802
* docsgpt backup and restore by @dartpain in https://github.com/arc53/DocsGPT/pull/2799
* feat: docsgpt up --native by @dartpain in https://github.com/arc53/DocsGPT/pull/2800
* feat: docsgpt dev, doctor and restart for the development loop by @dartpain in https://github.com/arc53/DocsGPT/pull/2803
* UI refinements by @ManishMadan2882 in https://github.com/arc53/DocsGPT/pull/2795
* correct license for widget by @pabik in https://github.com/arc53/DocsGPT/pull/2805
* fix(graphrag): make graph retrieval and extraction work in a default install by @dartpain in https://github.com/arc53/DocsGPT/pull/2804
* feat: personal access tokens (scoped API tokens for CLI and CI/CD) by @arc53-machine in https://github.com/arc53/DocsGPT/pull/2812
* feat: admin-set usage quotas per user and per team by @dartpain in https://github.com/arc53/DocsGPT/pull/2816
* chore: Zed project config, .editorconfig and shared pyright settings by @arc53-machine in https://github.com/arc53/DocsGPT/pull/2817
* logo upd by @pabik in https://github.com/arc53/DocsGPT/pull/2818
* Move settings and admin navigation into the sidebar by @dartpain in htt
```
</details>

---
### 📦 [lobehub/lobehub](https://github.com/lobehub/lobehub)
`⭐ Stars: 83,319` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.2.20](https://github.com/lobehub/lobehub/releases/tag/v2.2.20) (2026-10-18)`

> **简介**：🤯 LobeHub 是您的首席代理运营商，通过招聘、调度和报告整个 AI 团队，将您的代理组织为 7×24 小时运营。

**💡 核心亮点更新 (中文)**：
- **批量推出的目标** — 目标在您启动之前一直处于草稿状态，并且目标可以批量推出一项重复任务。每个批次都会停在一个决策门处，供所有者审查。 （#20840、#20704、#20917、#20833）
- **小部件和仪表板** — 主页和项目仪表板、代理小部件工具、聊天预览和新的“lh 小部件”/“lh 仪表板”命令。 （＃20421，＃20771）
- **LLM 中继到您的设备** — 服务器端运行、预设任务、模型列表和 Ollama 下载现在可以使用仅在浏览器选项卡或桌面应用程序中可用的模型。 （#20453、#20454、#20455、#20456、#20457）

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 📦 Release v2.2.20

This release was automatically published from PR #21078.

### Changes
See PR description: https://github.com/lobehub/lobehub/pull/21078

### Commit Message
# 🚀 LobeHub Release (20261018)

**Release Date:** October 18, 2026  
**Since v2.2.19:** 419 merged PRs · 14 contributors

> Agents now reach further across your devices, and the app opens faster. Topics, documents and device data load from local copies first, and server runs can use models that only exist on your device.

---

## ✨ Highlights

- **Goals with batch rollout** — A goal stays a draft until you start it, and a Goal can roll out one repeated task in batches. Each batch stops at a decision gate for the owner to review. (#20840, #20704, #20917, #20833)
- **Widgets & dashboards** — Home and project dashboards, an agent widget tool, chat previews, and new `lh widget` / `lh dashboard` commands. (#20421, #20771)
- **LLM relay to your device** — Server-side runs, preset tasks, model lists and Ollama downloads can now use models that are only available in your browser tab or desktop app. (#20453, #20454, #20455, #20456, #20457)
- **Remote terminals & device maintenance** — Open interactive shells on connected devices from the web, and update or restart CLI daemons from device settings. (#20600, #20527, #20528)
- **Local-first loading** — Topics, agent documents, devices, git status and home recents load from local replicas first, so pages show content before the network responds. (#20449, #20869, #
```
</details>

---
### 📦 [Dooy/chatgpt-web-midjourney-proxy](https://github.com/Dooy/chatgpt-web-midjourney-proxy)
`⭐ Stars: 6,798` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.26.8](https://github.com/Dooy/chatgpt-web-midjourney-proxy/releases/tag/v2.26.8) (2026-09-29)`

> **简介**：一个UI全部由chatgpt web、midjourney、gpts、suno、luma、runway、viggle、flux、ideogram、realtime、pika、udio完成；同时支持Web/PWA/Linux/Win/MacOS平台

**💡 核心亮点更新 (中文)**：
- 😄 支持：seedance视频官方接口入口
- 😄 支持：minimax视频官方接口入口

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# 2.26.8
- 😄 支持：seedance视频官方接口入口
- 😄 支持：minimax视频官方接口入口
```
</details>

---
### 📦 [labring/FastGPT](https://github.com/labring/FastGPT)
`⭐ Stars: 29,859` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v4.17.2](https://github.com/labring/FastGPT/releases/tag/v4.17.2) (2026-10-09)`

> **简介**：FastGPT is a knowledge-based platform built on the LLMs, offers a comprehensive suite of out-of-the-box capabilities such as data processing, RAG retrieval, and visual AI workflow orchestration, letting you easily develop and deploy complex question-answering systems without the need for extensive setup or configuration.

**💡 核心亮点更新 (中文)**：
* fix(dataset): prevent duplicate loading on dataset list scroll by  in https://github.com/labring/FastGPT/pull/7899
* fix: include model name in model probe errors by  in https://github.com/labring/FastGPT/pull/7915
* fix(global): formatNumberWithUnit 进位到下一单位时显示成 10000万 / 1000K by  in https://github.com/labring/FastGPT/pull/7911

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 📦 升级指南

### 镜像更新

- 更新 fastgpt-app（FastGPT 主服务）镜像 tag: v4.17.2
- 更新 fastgpt-pro（FastGPT 商业版）镜像 tag: v4.17.2

### 升级脚本

本次升级包含以下手动触发升级脚本（可在「管理员 > 版本升级」中查看与执行）：

1. **历史分块训练任务迁移**（`20261008_migrate_chunk_training`）：将存量旧版 chunk 训练任务平滑转换为关联正式数据行的新模式。属于手动触发任务（不阻塞服务启动），请在确认集群中所有旧版本 FastGPT App 与 Pro 实例已完全停止、旧任务租约过期后再点击执行。
2. **知识库重建状态迁移**（`20261009_migrate_dataset_rebuild_status`）：依赖上述训练任务迁移完成，属于手动触发任务（不阻塞服务启动），将历史知识库数据行中的旧版 `rebuilding` 标记和过渡状态统一迁移至全新的 `indexStatus` 重建状态体系。

## 🚀 新增内容

1. **知识库数据提前落库与训练链路重构**：
   - 解析分块、图片导入及备份/模板导入在内容解析完成后立即落库为可见数据行，全流程绑定唯一 `dataId`；训练完成后直接把向量与索引写回同一条数据，彻底避免长训练周期中无数据、训练中断残留孤儿数据的问题。
   - 新增数据索引三态流转（`parsed` -> `indexing` -> `indexed`）：待索引数据在检索层天然隔离不被召回，前端提供只读查看，后端对编辑、删除数据及修改索引提供安全拦截；训练失败数据支持直接编辑或删除。
   - QA 拆分一对多优化：源数据直接复用为首条拆分项，其余叶子节点新建预落库数据，入队、数据写入与源任务清理收敛在单数据库事务中。
   - 知识库模型切换与同义词重建优化：仅对已完成索引（`indexed`）的数据触发重建，待索引数据不参与重建链；同义词重建时自动复用未变更的向量数据，大幅降低重算开销。
   - 训练进度精细化看板：训练弹窗支持按处理模式（Vector、QA 等）分类展示当前阶段的训练进度，优化训练错误查看与重试体验。
2. **知识库与文件列表搜索支持限定在当前目录及子树**：在知识库列表或文件集合列表指定目录下搜索时，范围自动限制为当前路径自身及其全部子文件夹下的内容，命中结果平铺展示；在根目录下搜索则保持检索全量内容。底层采用高效内存分桶与层序遍历，并包含成环与最大深度/节点数截断保护。

## ⚙️ 优化

1. 核心控制台与管理页面迁移至客户端渲染（CSR）并启用浅路由（shallow routing）：将智能体、技能、MCP、系统工具、模板市场、评测等工作台页面，账号中心各模块，管理员后台以及定价页全面迁移为客户端渲染，避免页面切换时的完整 SSR 往返请求与白屏重渲染，显著提升交互响应速度。
2. 国际化（i18n）资源加载性能优化：将客户端语言包打包为单一 chunk 预加载，统一采用安全翻译 hook（`useSafeTranslation`），移除冗余的 namespace 异步网络请求，减少初始化开销并消除水合闪烁。
3. 异步任务队列（BullMQ）失败保留策略优化：提取共享的 BullMQ 队列与 Worker 默认配置，将所有后台任务（应用删除、知识库删除、知识库同步、评测、S3 文件
```
</details>

---
### 📦 [yihong0618/bilingual_book_maker](https://github.com/yihong0618/bilingual_book_maker)
`⭐ Stars: 9,889` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.3.1](https://github.com/yihong0618/bilingual_book_maker/releases/tag/v1.3.1) (2026-09-30)`

> **简介**：使用人工智能翻译制作双语 epub 书籍

**💡 核心亮点更新 (中文)**：
- 自述文件的 `--plan-classify` 和 `--use_context session` 条目再次是原始的 Params 文本，就像 #574 压缩它们之前一样。去除PDF阅读版截图；文本描述了输出。
- 翻译时发现的小修复：命令行页面中双倍的“the”/“flags”，Jev 页面中双倍的“for a run”，带有旧页面标题的链接文本，以及 README-CN 的 `--context-compact-at` 最小值（1500，CLI 强制执行）。
- 命名文档路径的运行时消息现在命名为“docs/en/...”。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Follow-up to #574 in three parts: three reuse-safety fixes on the `--to-epub` route with the CI job that now runs the route end to end; the user documentation in two languages, published to the one wiki; and the Docker images rebuilt as three, with the PDF ones no longer downloading PyTorch on every CI run.

## Part 1: the PDF route

### An edited `source.md` is never overwritten

A bundle's `source.md` is the operator's file once extraction is done: the docs say to fix headings there before paying for a translation. Until now a rerun that decided to extract again (settings changed, page range changed, the PDF or parser changed, `extract` asked for again) replaced it silently.

Now `guard_source_replacement` compares the file's text hash with the `source.working_sha256` the bundle recorded when the file was written. Equal: extraction may replace it. Different: the run stops with `SOURCE_EDITED`, naming the reason it wanted to extract and the two ways out (rerun with the settings the bundle was made with, or `tools/pdf_to_book.py translate <bundle>`; to extract afresh, move the bundle aside). A bundle with no baseline on record stops with `SOURCE_BASELINE_UNKNOWN`: unknown is not untouched. There is no override flag. The guard is asked at the start of `prepare`, `import_markdown` and `extract_pdf`, and once more after the docling conversion, right before the old assets are cleared, because a conversion takes minutes and an edit made meanwhile must not be lost either. B
```
</details>

---
### 📦 [1Panel-dev/1Panel](https://github.com/1Panel-dev/1Panel)
`⭐ Stars: 37,204` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.3.2](https://github.com/1Panel-dev/1Panel/releases/tag/v2.3.2) (2026-09-24)`

> **简介**：🔥 1Panel 是一个现代化的开源 Linux 服务器管理面板和轻量级 AI 管理平台。

**💡 核心亮点更新 (中文)**：
* 面板设置：添加了对通过 https://github.com/1Panel-dev/1Panel/pull/13872 创建多个 API 密钥的支持
* 虚拟机管理：增加了对挂载多个 CD-ROM ISO 映像的支持
* 概述：改进了磁盘命令失败的日志记录，位于 https://github.com/1Panel-dev/1Panel/pull/13889

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
[English](#en-v2.3.2) | [中文](#cn-v2.3.2)

<h3 id="en-v2.3.2">New Features</h3>

* Panel Settings: Added support for creating multiple API keys by @lan-yonghui in https://github.com/1Panel-dev/1Panel/pull/13872
* Virtual Machine Management: Added support for mounting multiple CD-ROM ISO images by @ssongliu

### Enhancements

* Overview: Improved logging for disk command failures by @ssongliu in https://github.com/1Panel-dev/1Panel/pull/13889
* File Browser: Improved task messages for file copy, move, compress, and decompress by @lan-yonghui in https://github.com/1Panel-dev/1Panel/pull/13885
* Firewall: Optimized firewall state reads and batch verification logic by @ssongliu in https://github.com/1Panel-dev/1Panel/pull/13881
* System: Removed the minimum upgrade backup copies limit by @ssongliu in https://github.com/1Panel-dev/1Panel/pull/13907

### Bug Fixes

* Models: Fixed the Ollama page failing to open properly in some scenarios by @zhengkunwang223 in https://github.com/1Panel-dev/1Panel/pull/13855
* Models: Fixed vLLM uninstall failures in some scenarios by @zhengkunwang223
* App Store: Fixed application upgrade failures in some scenarios by @zhengkunwang223 in https://github.com/1Panel-dev/1Panel/pull/13888
* Websites: Fixed incorrect priority between HTTP-to-HTTPS redirects and website redirects by @A-Words in https://github.com/1Panel-dev/1Panel/pull/13847
* Certificates: Fixed auto-renewing certificates still triggering expiry alerts by @lan-yonghu
```
</details>

---
### 📦 [invoke-ai/InvokeAI](https://github.com/invoke-ai/InvokeAI)
`⭐ Stars: 28,752` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v6.14.2](https://github.com/invoke-ai/InvokeAI/releases/tag/v6.14.2) (2026-09-27)`

> **简介**：Invoke 是稳定扩散模型的领先创意引擎，使专业人士、艺术家和爱好者能够使用最新的人工智能驱动技术生成和创建视觉媒体。该解决方案提供了业界领先的WebUI，并作为多个商业产品的基础。

**💡 核心亮点更新 (中文)**：
* 您现在可以导入自定义字体以与 Canvas 文本工具一起使用
* 您现在可以通过提供参考图像将图像的样式转移到 krea-2

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
This release fixes a number of bugs in version 6.14.1 and adds a couple of useful new features.

## New Features in this release
* You can now import custom fonts for use with the Canvas text tool (@DustyShoe)
* You can now transfer an image's style to krea-2 by providing a reference image (@Pfannkuchensack)

## Bug fixes
* Keep a password-change token when a routine refresh lands first by @MohammadHijjawi97 in https://github.com/invoke-ai/InvokeAI/pull/9599
* Reject path traversal in object-serializer names and model keys by @lstein in https://github.com/invoke-ai/InvokeAI/pull/9595
* Clarify proxy destination policy without blocking local proxies by @wunianze666-netizen in https://github.com/invoke-ai/InvokeAI/pull/9554
* Accept epoch-changing token refreshes by @wunianze666-netizen in https://github.com/invoke-ai/InvokeAI/pull/9560
* Remove FP4 Mistral starter, fix model rename validation, limit Z-Image to Qwen3 4B encoders by @Pfannkuchensack in https://github.com/invoke-ai/InvokeAI/pull/9587
* Stop the SDNQ guards from aborting folder-encoder identification by @Pfannkuchensack in https://github.com/invoke-ai/InvokeAI/pull/9561
* img2img posterization - noise scaling and sigma schedule by @Pfannkuchensack in https://github.com/invoke-ai/InvokeAI/pull/9556
* Make I hotkey work in Canvas, Gallery, and Viewer by @DustyShoe in https://github.com/invoke-ai/InvokeAI/pull/9569
* Make room in VRAM for the quantized Qwen2.5-VL encoder and release it afterwards (#914
```
</details>

---
### 📦 [langchain-ai/langchain](https://github.com/langchain-ai/langchain)
`⭐ Stars: 148,069` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [langchain-core==1.6.12](https://github.com/langchain-ai/langchain/releases/tag/langchain-core%3D%3D1.6.12) (2026-10-16)`

> **简介**：代理工程平台。

**💡 核心亮点更新 (中文)**：
自 langchain-core==1.6.11 以来的变化

版本（核心）：1.6.12 (41277)
修复（核心）：在内容块开始事件上传播额外内容（41272）

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Changes since langchain-core==1.6.11

release(core): 1.6.12 (#41277)
fix(core): propagate extras on content-block-start events (#41272)
```
</details>

---
### 📦 [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)
`⭐ Stars: 187,650` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [autogpt-platform-beta-v0.8.4](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.8.4) (2026-10-14)`

> **简介**：AutoGPT 的愿景是为每个人提供易于使用和构建的人工智能。我们的使命是提供工具，以便您可以专注于重要的事情。

**💡 核心亮点更新 (中文)**：
- **#15089** - 在转弯运行时运行 Copilot 聊天，该聊天在一个连接上的光标处恢复（通过
- **#15199** - 专家集成首先通过 MCP 连接（通过
- **#15248** - 将“提供反馈”添加到帐户菜单（修补程序）（通过

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# 🚀 Release `autogpt-platform-beta-v0.8.4`

**Date:** October 2026

---

## 🔥 What's New?

### New Features
- **#15089** - Run Copilot chat on a turn runtime that resumes at its cursor on one connection (by @Pwuts)
- **#15199** - Expert integrations connect through MCP first (by @0ubbe)
- **#15248** - Add “Give feedback” to the account menu (hotfix) (by @kcze)
- **#15216** - Keep Otto and expert replies short (by @0ubbe)
- **#15217** - Make the expert hire card short and Typeform-like (by @0ubbe)
- **#15249** - Send onboarding role to MailerLite and PostHog; exclude Iran and Russia from MailerLite (by @ntindle)
- **#15204** - Redesign wallet with chat usage and credits (by @Torantulino)
- **#15196** - Move onboarding paywall after personalization (by @Torantulino)
- **#15061** - Approval cards label/word tool arguments from the tool schema (by @Pwuts)
- **#15358** - Canceling a trial keeps access until the trial ends (by @itsababseh)
- **#15361** - Sub-session waits for a slot when the user’s slots are full (by @Pwuts)
- **#15043** - Approved call chain row expands to show what ran (by @Pwuts)
- **#15349** - Add “Chats” to the collapsed sidebar (by @itsababseh)
- **#15441** - Show “Thinking…” instead of backend status lines in Copilot (by @0ubbe)
- **#15442** - Restyle chat markdown tables (by @0ubbe)
- **#15462** - Give Copilot turns and graph node runs their own Sentry traces (by @ntindle)
- **#15460** - Tag Sentry events with deployed commit and al
```
</details>

---
### 📦 [rockbenben/ChatGPT-Shortcut](https://github.com/rockbenben/ChatGPT-Shortcut)
`⭐ Stars: 8,838` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v4.5.1](https://github.com/rockbenben/ChatGPT-Shortcut/releases/tag/v4.5.1) (2026-10-09)`

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
`⭐ Stars: 2,813` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [userscript-v2.38.0](https://github.com/pionxzh/chatgpt-exporter/releases/tag/userscript-v2.38.0) (2026-10-17)`

> **简介**：导出并分享您的 ChatGPT 对话历史记录

**💡 核心亮点更新 (中文)**：
* 将 TavernAI JSONL 添加到批量导出（[c8bd69c](https://github.com/pionxzh/chatgpt-exporter/commit/c8bd69c36702b417aa20e2af3d35d77ea7c06d93)），关闭[#404](https://github.com/pionxzh/chatgpt-exporter/issues/404)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## [2.38.0](https://github.com/pionxzh/chatgpt-exporter/compare/userscript-v2.37.1...userscript-v2.38.0) (2026-10-17)


### Features

* add TavernAI JSONL to bulk export ([c8bd69c](https://github.com/pionxzh/chatgpt-exporter/commit/c8bd69c36702b417aa20e2af3d35d77ea7c06d93)), closes [#404](https://github.com/pionxzh/chatgpt-exporter/issues/404)


### Bug Fixes

* keep the bulk export buttons together when the bar wraps ([9e8d822](https://github.com/pionxzh/chatgpt-exporter/commit/9e8d822280d150f8d87f1e3e42164805f6670a67))
```
</details>

---
### 📦 [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent)
`⭐ Stars: 47,464` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [2.2.1](https://github.com/zhayujie/CowAgent/releases/tag/2.2.1) (2026-10-14)`

> **简介**：开源个人人工智能助理和代理线束。计划任务，运行工具和技能，利用记忆和知识进行自我进化。多代理、多模式、多渠道。轻量级、可扩展、单行安装。

**💡 核心亮点更新 (中文)**：
- **自动收集**：您的特工创建的文档、网页、图像和视频会自动显示在所有特工的一条时间线上的工件中。
- **预览和回溯**：按类型或代理进行过滤、搜索、就地预览，然后跳回到生成文件的对话（感谢#3732）。
- **固定和管理**：固定、重命名或删除工件；对话中的文件卡可将您直接带到 Artifacts 中。 Artifacts 页面默认隐藏，可以在菜单编辑器中打开。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
🌐 [English](https://docs.cowagent.ai/releases/v2.2.1) | [中文](https://docs.cowagent.ai/zh/releases/v2.2.1)

## 📁 Artifacts

A new **Artifacts** page brings together the files created in your conversations, in both the Web console and the desktop client:

- **Automatic collection**: documents, web pages, images, and videos your Agents create show up in Artifacts automatically, on one timeline across all Agents.
- **Preview and trace back**: filter by type or Agent, search, preview in place, and jump back to the conversation that produced a file (Thanks @rudycelekli #3732).
- **Pin and manage**: pin, rename, or remove artifacts; a file card in a conversation takes you straight to it in Artifacts. The Artifacts page is hidden by default and can be turned on in the menu editor.

<img src="https://cdn.jsdelivr.net/gh/zhayujie/cowagent-assets@main/screenshots/en/web-console-artifacts.png" alt="Artifacts" width="800" />

Related docs: [Web Console - Artifacts](https://docs.cowagent.ai/channels/web#artifacts)

## 🧭 Custom Menu & Console Improvements

- **Custom menu**: customize the groups, order, names, icons, and visibility of menu entries in the Web console and desktop client, with one shared configuration; artifacts and web links can be added as menu entries. See [Custom Menu](https://docs.cowagent.ai/extensions/custom-menu).
- **Token usage**: each reply shows the tokens actually used in that turn, including cache hits. Thanks @Harbor404 (#3440)
- **Mermaid diag
```
</details>

---
### 📦 [lxhao61/integrated-examples](https://github.com/lxhao61/integrated-examples)
`⭐ Stars: 2,533` &nbsp;|&nbsp; `💻 语言: Shell` &nbsp;|&nbsp; `🏷️ 最新版本: [20261006](https://github.com/lxhao61/integrated-examples/releases/tag/20261006) (2026-10-06)`

> **简介**：以 Nginx 或 Caddy(v2 版) 配合 V2Ray(v4 版) 或 Xray、Caddy(v2 版) 加专用插件、Hysteria 等打造常用科学上网的优化配置及最优组合示例，且提供集成特定插件的 Caddy(v2 版) 文件，分享给大家食用及自己备份。

**💡 核心亮点更新 (中文)**：
以 Caddy 发行版 v2.11.7 源码加插件 forwardproxy、caddy-trojan、caddy-webdav、caddy-cloudflare-ip、caddy-trusted-cloudfront、caddy-dns/cloudflare、caddy-dns/duckdns、caddy-dns/tencentcloud、caddy-events-exec、caddy-l4、jsonc-adapter 基于稳定版 go1.27.1 定制编译而成，其额外应用及特点如下：
1、

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
以 Caddy 发行版 v2.11.7 源码加插件 forwardproxy、caddy-trojan、caddy-webdav、caddy-cloudflare-ip、caddy-trusted-cloudfront、caddy-dns/cloudflare、caddy-dns/duckdns、caddy-dns/tencentcloud、caddy-events-exec、caddy-l4、jsonc-adapter 基于稳定版 go1.27.1 定制编译而成，其额外应用及特点如下：
1、支持 NaiveProxy 应用（服务端）。采用官方指定源码，其源码更新及时、但不支持 UoT。
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
### 📦 [electerm/electerm](https://github.com/electerm/electerm)
`⭐ Stars: 15,393` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v5.6.10](https://github.com/electerm/electerm/releases/tag/v5.6.10) (2026-10-15)`

> **简介**：📻免费开源终端/ssh/sftp/ftp/telnet/串口/RDP/VNC/Spice客户端(Linux, Mac, Windows, Android, HarmonyOS, iOS)

**💡 核心亮点更新 (中文)**：
- 支持 electterm 云同步客户端数据加密
- 支持书签中的私钥/证书文件路径
- 支持箭头/回车键在书签面板中选择/打开书签

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
### New features/UI/Updates

- Support client side data encrypt for electerm cloud sync
- Support privateKey/certificate file path in bookmark
- Support arrow/enter keys to select/open bookmark in bookmark panel
- Support payload check before sync to cloud

### Bug fixes

- Fix bookmark duplicated render by @davinyue
- Fix support for webdav http sync
- Fix ssh MFA logic
- Fix cursor hide issue when open folder select dialog in Windows (#4605)

-----

### 新功能/界面/更新

- 支持 electerm 云同步的客户端数据加密
- 支持书签中使用私钥/证书文件路径
- 支持在书签面板中使用方向键/回车选择/打开书签
- 同步到云端前支持数据量检查

### 问题修复

- 修复书签重复渲染问题（由 @davinyue 提供）
- 修复 webdav http 同步支持
- 修复 ssh MFA（多因素认证）逻辑
- 修复 Windows 下打开文件夹选择对话框时光标隐藏问题 (#4605)

-------

Download下载: [https://electerm.org](https://electerm.org)
```
</details>

---
### 📦 [XX-net/XX-Net](https://github.com/XX-net/XX-Net)
`⭐ Stars: 33,452` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [5.16.7](https://github.com/XX-net/XX-Net/releases/tag/5.16.7) (2026-09-28)`

> **简介**：绕过 GFW 的代理工具。

**💡 核心亮点更新 (中文)**：
* fix: check WebSocket MASK bit before reading masking key (RFC 6455 §5.2) by  in https://github.com/XX-net/XX-Net/pull/14170
* 修正 listen_ip 为 IPv6 地址时 simple_http_server 格式化失败 by  in https://github.com/XX-net/XX-Net/pull/14004
* fix: Python 3 compatibility and robustness improvements by  in https://github.com/XX-net/XX-Net/pull/14184

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Support Mac arm64 CPU

## What's Changed
* fix: check WebSocket MASK bit before reading masking key (RFC 6455 §5.2) by @AAtomical in https://github.com/XX-net/XX-Net/pull/14170
* 修正 listen_ip 为 IPv6 地址时 simple_http_server 格式化失败 by @UjuiUjuMandan in https://github.com/XX-net/XX-Net/pull/14004
* fix: Python 3 compatibility and robustness improvements by @Dolores-Abernathy1 in https://github.com/XX-net/XX-Net/pull/14184

## New Contributors
* @AAtomical made their first contribution in https://github.com/XX-net/XX-Net/pull/14170
* @UjuiUjuMandan made their first contribution in https://github.com/XX-net/XX-Net/pull/14004
* @Dolores-Abernathy1 made their first contribution in https://github.com/XX-net/XX-Net/pull/14184

**Full Changelog**: https://github.com/XX-net/XX-Net/compare/5.16.6...5.16.7
```
</details>

---
### 📦 [FreeCAD/FreeCAD](https://github.com/FreeCAD/FreeCAD)
`⭐ Stars: 34,507` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [1.1.4](https://github.com/FreeCAD/FreeCAD/releases/tag/1.1.4) (2026-09-28)`

> **简介**：FreeCAD 的官方源代码，一个免费的开源多平台 3D 参数化建模器。

**💡 核心亮点更新 (中文)**：
* 在 #30899 中修复 coin 4.0.10 的 COIN3D_MICRO_VERSION 正则表达式（由 PR [#31571](https://github.com/FreeCAD/FreeCAD/pull/31571) 反向移植）
* 核心：通过 #29628 提高 fps 标签的性能（由 PR [#31657](https://github.com/FreeCAD/FreeCAD/pull/31657) 反向移植）
* Gui：在 #31559 中修复链接组子项的可见性图标（由 PR [#31684](https://github.com/FreeCAD/FreeCAD/pull/31684) 反向移植）

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
FreeCAD 1.1.4 is the last planned maintenance release in the 1.1.x series. It includes two security fixes addressing file-handling vulnerabilities that can be triggered by opening a maliciously crafted FCStd file. All previously-released versions are affected by these issues, so we strongly recommend that all users upgrade, especially anyone who opens FreeCAD files from untrusted or unknown sources.

## How to download
The assets section below is automatically populated as the builds complete: if you don't see a download for your system, please be patient, the builds can take several hours to complete. Windows and macOS builds are signed by The FreeCAD project association AISBL.

## What's Changed
* fix COIN3D_MICRO_VERSION regex for coin 4.0.10 by @moench-tegeder in #30899 (backported by PR [#31571](https://github.com/FreeCAD/FreeCAD/pull/31571))
* core: Improve performance of fps label by @ipatch in #29628 (backported by PR [#31657](https://github.com/FreeCAD/FreeCAD/pull/31657))
* Gui: Fix visibility icons for link group sub-items by @maxwxyz in #31559 (backported by PR [#31684](https://github.com/FreeCAD/FreeCAD/pull/31684))
* TechDraw: Projection Group jumps to origin by @WandererFan in #27094 (backported by PR [#31687](https://github.com/FreeCAD/FreeCAD/pull/31687))
* [Gui] fix TinkerCAD nav style to consistently show the context menu … by @Syres916 in #31631 (backported by PR [#31706](https://github.com/FreeCAD/FreeCAD/pull/31706))
* Fix regression with 3mf
```
</details>

---
### 📦 [klzgrad/naiveproxy](https://github.com/klzgrad/naiveproxy)
`⭐ Stars: 9,531` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [v154.0.8037.49-4](https://github.com/klzgrad/naiveproxy/releases/tag/v154.0.8037.49-4) (2026-10-07)`

> **简介**：默默发财

**💡 核心亮点更新 (中文)**：
通过更高的接收窗口和 BBR 拥塞控制，将 QUIC 吞吐量提高到接近 TLS 性能。建议用户将 Caddy 服务器更新至 [v2.11.7-naive](https://github.com/klzgrad/forwardproxy/releases/tag/v2.11.7-naive)。

软化o

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Improved QUIC throughput to near TLS performance with higher receive window and BBR congestion control. Users are recommended to update Caddy server to [v2.11.7-naive](https://github.com/klzgrad/forwardproxy/releases/tag/v2.11.7-naive).

Softened old tunnel cleanup that breaks long-lived user connections. Now in old tunnels, long-lived connections are only closed after 1/10 idle timeout.
```
</details>

---

## <span id="-影音媒体与下载">🎬 影音媒体与下载</span>

### 📦 [paulrosen/abcjs](https://github.com/paulrosen/abcjs)
`⭐ Stars: 2,364` &nbsp;|&nbsp; `💻 语言: HTML` &nbsp;|&nbsp; `🏷️ 最新版本: [v6.7.1](https://github.com/paulrosen/abcjs/releases/tag/v6.7.1) (2026-09-21)`

> **简介**：用于渲染 abc 乐谱的 javascript

**💡 核心亮点更新 (中文)**：
错误修复

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
bug fixes
```
</details>

---
### 📦 [guohuiyuan/go-music-dl](https://github.com/guohuiyuan/go-music-dl)
`⭐ Stars: 5,481` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.1.3](https://github.com/guohuiyuan/go-music-dl/releases/tag/v1.1.3) (2026-10-19)`

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
### 📦 [dyang886/Game-Cheats-Manager](https://github.com/dyang886/Game-Cheats-Manager)
`⭐ Stars: 15,491` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.5.4](https://github.com/dyang886/Game-Cheats-Manager/releases/tag/v2.5.4) (2026-10-11)`

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
`⭐ Stars: 46,579` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2026.10.19-8445.09c896b](https://github.com/DIYgod/RSSHub/releases/tag/v2026.10.19-8445.09c896b) (2026-10-19)`

> **简介**：🧡 一切都是RSSible

**💡 核心亮点更新 (中文)**：
-ghcr.io/diygod/rsshub:09c896b3b6cd25a6b6c0db73fcded5ffe296fdc9
- ghcr.io/diygod/rsshub:chromium-bundled-09c896b3b6cd25a6b6c0db73fcded5ffe296fdc9
-diygod/rsshub:09c896b3b6cd25a6b6c0db73fcded5ffe296fdc9

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Source commit: 09c896b3b6cd25a6b6c0db73fcded5ffe296fdc9

Published multi-platform images:
- ghcr.io/diygod/rsshub:09c896b3b6cd25a6b6c0db73fcded5ffe296fdc9
- ghcr.io/diygod/rsshub:chromium-bundled-09c896b3b6cd25a6b6c0db73fcded5ffe296fdc9
- diygod/rsshub:09c896b3b6cd25a6b6c0db73fcded5ffe296fdc9
- diygod/rsshub:chromium-bundled-09c896b3b6cd25a6b6c0db73fcded5ffe296fdc9

Use these commit-specific image tags to reproduce this release. Daily Docker tags may be updated by subsequent builds.
```
</details>

---
### 📦 [amir1376/ab-download-manager](https://github.com/amir1376/ab-download-manager)
`⭐ Stars: 18,638` &nbsp;|&nbsp; `💻 语言: Kotlin` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.11.1](https://github.com/amir1376/ab-download-manager/releases/tag/v1.11.1) (2026-10-14)`

> **简介**：下载管理器可加快您的下载速度

**💡 核心亮点更新 (中文)**：
- Linux 上的目录选择器崩溃 (#1479)
- 空闲检测在 Linux 上无法正常工作 (#1479)
- 更新翻译

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 1.11.1

### Fixed

- Directory picker crash on Linux (#1479)
- Idle detection not working properly on Linux (#1479)

### Improved

- Updated translations
- Minor improvements to the desktop settings UI
```
</details>

---
### 📦 [lyswhut/lx-music-desktop](https://github.com/lyswhut/lx-music-desktop)
`⭐ Stars: 54,577` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.12.6](https://github.com/lyswhut/lx-music-desktop/releases/tag/v2.12.6) (2026-09-19)`

> **简介**：一个基于 Electron 的音乐软件

**💡 核心亮点更新 (中文)**：
- 优化 tx 推荐歌单列表
- 优化禁用透明窗口的窗口边框显示效果
- 修复打开某些 kg 歌单时歌曲丢失的问题

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
目前新项目 Any Listen 的桌面版、Web 版已实现 LX Music 的大部分功能，并额外支持 WebDAV 歌曲播放、WebDAV 数据同步、独立播放列表等功能。
以后的开发精力将主要集中在新项目上，之前大家在 LX Music 提的功能我们也会考虑在新项目中添加。
对于日常使用 LX Music 的人可以试试迁移到 Any Listen，若遇到任何问题可以发 issue 反馈。
Any Listen 的项目地址为 https://github.com/any-listen/any-listen

### 优化

- 优化 tx 推荐歌单列表
- 优化禁用透明窗口的窗口边框显示效果

### 修复

- 修复打开某些 kg 歌单时歌曲丢失的问题
- 修复 Windows 7 无法启动的问题
- 修复禁用透明窗口时按 F11 无法全屏的问题

### 安装包快捷链接

- Windows x64: [lx-music-desktop-v2.12.6-x64-Setup.exe](https://github.com/lyswhut/lx-music-desktop/releases/download/v2.12.6/lx-music-desktop-v2.12.6-x64-Setup.exe)
- MacOS arm64: [lx-music-desktop-2.12.6-arm64.dmg](https://github.com/lyswhut/lx-music-desktop/releases/download/v2.12.6/lx-music-desktop-2.12.6-arm64.dmg)
- Linux amd64 deb: [lx-music-desktop_2.12.6_amd64.deb](https://github.com/lyswhut/lx-music-desktop/releases/download/v2.12.6/lx-music-desktop_2.12.6_amd64.deb)

### File MD5

```

EE6E6C58B4EBCBADD689A26904245412  lx-music-desktop-v2.12.6-arm64-Setup.exe
FC8D5CA1486C20A80A3872CAC164BD96  lx-music-desktop-v2.12.6-x64-Setup.exe
E465D42988B2DEB1524C3FB93FB8C93C  lx-music-desktop-v2.12.6-win_arm64-green.7z
D45A6D2069F029152E114D8E6E4D3285  lx-music-desktop-v2.12.6-win_x64-green.7z
555B3AE80DABAADC12BD9FAC054844B7  lx-music-desktop-v2.12.6-win7_x64-Setup.exe
3FC618E78ACCDC3BCB84FE28506DD968  lx-music-desktop-v2.12.6-win7_x64-green.7z
98C8CCAA07D25C9D8B3D93AE4145275E  lx-music-desktop-v2.12.6-win7_x86-green.7z

MD5 (lx-music-desktop-2.12.6-arm64
```
</details>

---
### 📦 [jerrykuku/luci-theme-argon](https://github.com/jerrykuku/luci-theme-argon)
`⭐ Stars: 5,535` &nbsp;|&nbsp; `💻 语言: CSS` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.0.0](https://github.com/jerrykuku/luci-theme-argon/releases/tag/v3.0.0) (2026-10-16)`

> **简介**：Argon 是一个干净整洁的 OpenWrt LuCI 主题，允许用户使用图像或视频自定义其登录界面。   它还支持明暗模式自动和手动切换。

**💡 核心亮点更新 (中文)**：
* 修复（级联）：在 https://github.com/jerrykuku/luci-theme-argon/pull/709 中为 argon 配置表单添加底部间距
* feat(sysauth): 在登录页面上渲染身份验证登录插件 https://github.com/jerrykuku/luci-theme-argon/pull/710
* 修复（sysauth）：避免在 https://github.com/jerrykuku/luci-theme-argon/pull/712 中的集中登录输入上出现蓝色轮廓

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Argon 3.0

- Integrate Argon Config, wallpaper uploads and custom branding into the theme package, with a compatibility package for existing installations.
- Add classic-sidebar and centered-card login layouts, persistent light/dark/system appearance switching, and automatic dark accent colors.
- Improve desktop and mobile layouts, shared controls, tables, tabs, dialogs and most third-party LuCI applications.
- Replace icon fonts with SVG menu/control icons and complete Argon Config translations.
- Refresh the English/Chinese README, desktop demo, screenshots and development guides.
- Fix translation package versions and upgrade ordering; verify every language package before publication.
- Reduce package size with a WebP login background and optimized WOFF2 fonts, retaining all font characters and rendering instructions.

- 将 Argon Config、背景上传和自定义图标集成到主题，提供旧版配置插件迁移包。
- 提供经典侧栏、居中卡片两套登录布局，持久化亮色／暗色／跟随系统切换，以及自动暗色配色。
- 优化桌面与手机布局、通用控件、表格、标签页、弹窗和大多数第三方 LuCI 应用的适配。
- 使用 SVG 菜单／控件图标替代图标字体，补全 Argon Config 翻译。
- 更新中英文 README、桌面演示动画、截图和开发说明。
- 修复语言包版本及升级顺序，发布前逐包核验全部语言包版本。
- 使用 WebP 登录背景并精简 WOFF2 字体，保留全部字符和渲染指令，减小安装包体积。

This v3.0.0 rebuild uses package revision **2**: IPK `3.0.0-2`, APK `3.0.0-r2`. Translation versions are `v3.0.0-2` (IPK) and `3.0.0-r2` (APK), allowing normal upgrades from the original `unknown` / `0` language packages.

本次 v3.0.0 重发采用安装包修订号 **2**：IPK 为 `3.0.0-2`，APK 为 `3.0.0-r2`。语言包分别为 `v3.0.0-2`（IPK）和 `3.0.0-r2`（APK），可从原 `unknown`／`0` 语言包正常升级。

## Installation / 安装
```
</details>

---
### 📦 [qier222/YesPlayMusic](https://github.com/qier222/YesPlayMusic)
`⭐ Stars: 33,410` &nbsp;|&nbsp; `💻 语言: Vue` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.4.11](https://github.com/qier222/YesPlayMusic/releases/tag/v0.4.11) (2026-10-10)`

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

## <span id="-效率办公与创作">📝 效率办公与创作</span>

### 📦 [robbietilton/Compositor](https://github.com/robbietilton/Compositor)
`⭐ Stars: 17,434` &nbsp;|&nbsp; `💻 语言: Swift` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.5.3](https://github.com/robbietilton/Compositor/releases/tag/v1.5.3) (2026-10-15)`

> **简介**：适用于 Mac 的 Photoshop 替代品

**💡 核心亮点更新 (中文)**：
- 通过 GPU 加速对大图像进行更快的 Camera Raw 预览，保留现有的调整结果。
- 拖动滑块时，Camera Raw 预览保持全分辨率。
- 更快的直方图和范围更新。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
- Faster Camera Raw previews on large images with GPU acceleration, preserving existing adjustment results.
- Camera Raw previews stay at full resolution while dragging sliders.
- Faster histogram and scope updates.
- New Smooth Corners option for rectangles, with iOS-style rounded corners.
- Cleaner shape controls, with the fill swatch first in all three shape modes.
- Scroll the Layers panel by dragging with the middle mouse button.
- Zoom cursors update immediately when changing drag direction.
```
</details>

---
### 📦 [jgraph/drawio-desktop](https://github.com/jgraph/drawio-desktop)
`⭐ Stars: 63,554` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v32.5.5](https://github.com/jgraph/drawio-desktop/releases/tag/v32.5.5) (2026-10-18)`

> **简介**：Draw.io 的官方电子版本

**💡 核心亮点更新 (中文)**：
- 使用电子44.9.0
- 修复了动画 GIF 和视频导出，该导出因“文件数据无效”而失败 [jgraph/drawio-desktop#2580]
- 修复了从 31.5.2 开始保存库失败并出现错误的问题 [jgraph/drawio-desktop#2581]

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Release Notes for 32.5.5

[Windows Installer](https://github.com/jgraph/drawio-desktop/releases/download/v32.5.5/draw.io-32.5.5-windows-installer.exe)
[Windows No Installer (zip)](https://github.com/jgraph/drawio-desktop/releases/download/v32.5.5/draw.io-32.5.5-windows.zip)
[macOS - Universal](https://github.com/jgraph/drawio-desktop/releases/download/v32.5.5/draw.io-universal-32.5.5.dmg)
Linux - [deb](https://github.com/jgraph/drawio-desktop/releases/download/v32.5.5/drawio-amd64-32.5.5.deb), [AppImage](https://github.com/jgraph/drawio-desktop/releases/download/v32.5.5/drawio-x86_64-32.5.5.AppImage) or [rpm](https://github.com/jgraph/drawio-desktop/releases/download/v32.5.5/drawio-x86_64-32.5.5.rpm)

**ChangeLog:**

- Uses electron 44.9.0
- Fixes the animated GIF and video export, which failed with "Invalid file data" [jgraph/drawio-desktop#2580]
- Fixes saving libraries, which failed with an error since 31.5.2 [jgraph/drawio-desktop#2581]
- Closes the window when Discard Changes is chosen after a save followed by a quick edit, which kept the window open and stopped every later close and quit from working [jgraph/drawio#5806]
- Updates to [draw.io core 32.5.5](https://github.com/jgraph/drawio/blob/v32.5.5/ChangeLog). All changes from 32.4.1 to 32.5.5 are added in this build.

**Testing:**

Verified against the packaged, signed macOS build. Windows and Linux packages were verified from the produced release artifacts, their sizes and update manifests, rathe
```
</details>

---
### 📦 [Stirling-Tools/Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF)
`⭐ Stars: 94,514` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.2.0](https://github.com/Stirling-Tools/Stirling-PDF/releases/tag/v3.2.0) (2026-10-15)`

> **简介**：GitHub 上排名第一的 PDF 应用程序，可让您在任何地方的任何设备上编辑 PDF

**💡 核心亮点更新 (中文)**：
又一个好作品发布！
旧的多功能工具已被完全重新设计的页面编辑器所取代。它现在重新支持图像、重命名文件和一系列 QOL UI 更改，使重新排列和管理文档变得更加容易。请让我们知道

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Another good release!
The old multi-tool has been replaced by a completely redesigned Page Editor. It now resupports images, renaming files, and a bunch of QOL UI changes making it much easier to rearrange and manage your documents. Please let us know what you think and if you have any issues with it!

Some big changes in how we handle password-protected PDF, They can now be opened for viewing and used with common tools without having to remove the password first, and your existing PDF permission settings are kept when unlocking.

Other changes are: 
- Stirling Sign now emails participants and requesters as a signing request progresses
- Drop files anywhere on the workbench, plus a redesigned add-files button
- Compression now tells you when it could not shrink a file
- Tidied booklet imposition UI with guide diagrams
- Optional redirectBaseUrl for OAuth2 and SAML when running behind reverse proxies
- Faster startup and lower memory use in the viewer and text editor
- Refreshed icons and chat UI improvements

We also fixed some bugs including
- Desktop crashing when reordering files on Mac
- Form drafts being lost before saves completed
- Signatures being lost when adjusting page size and scale
- Sign tool crashing when navigating away
- Chat not updating the file version correctly
- S3 uploads failing on retry

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### Bug Fixes
* fix(desktop): avoid W
```
</details>

---
### 📦 [halo-dev/halo](https://github.com/halo-dev/halo)
`⭐ Stars: 39,949` &nbsp;|&nbsp; `💻 语言: Java` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.27.0](https://github.com/halo-dev/halo/releases/tag/v2.27.0) (2026-10-14)`

> **简介**：Halo 是一款强大易用的开源建站工具，从个人博客、知识库，到企业官网、在线商城，Halo 都能助您轻松实现，一站式满足您的多样化建站需求。

**💡 核心亮点更新 (中文)**：
- 已启用 TOTP 或验证邮箱的用户，在修改密码和管理个人访问令牌前需安全确认；确认后 30 分钟内无需再次确认 by  in #10333
- 为评论和回复提供统一固定链接，方便从通知和 Console 跳转到对应讨论 by  in #10318
- 支持在 Console 中编辑评论和回复 by  in #10302

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 新特性

- 已启用 TOTP 或验证邮箱的用户，在修改密码和管理个人访问令牌前需安全确认；确认后 30 分钟内无需再次确认 by @JohnNiang in #10333
- 为评论和回复提供统一固定链接，方便从通知和 Console 跳转到对应讨论 by @ruibaby in #10318
- 支持在 Console 中编辑评论和回复 by @ruibaby in #10302
- 编辑器图片集支持为单张图片设置替代文本 by @ruibaby in #10303
- 编辑器图片集支持替换单张图片 by @ruibaby in #10304
- 支持在编辑菜单项时切换链接、内置路由及内容类型 by @ruibaby in #10305
- 菜单项支持绑定文章归档、分类列表和标签列表，主题路由设置变化后链接会自动更新 by @ruibaby in #10284
- 上传附件前可修改文件名 by @ruibaby in #10288
- Console 支持超级管理员以其他用户身份登录，并在切换期间显示提示横幅和退出入口 by @JohnNiang in #10354
- 评论管理支持将评论和回复设为私密，并可在创建回复时选择私密回复 by @ruibaby in #10348

## 功能优化

- 附件库复制的视频 HTML 默认包含播放控件 by @ruibaby in #10323
- 附件库复制的音频 HTML 默认包含播放控件 by @ruibaby in #10324
- 完善邮箱验证、注册登录、评论和附件上传等操作的多语言错误提示 by @ruibaby in #10320
- 优化 Console 加载体验，无需主题信息的页面不再等待主题加载 by @ruibaby in #10296
- 新安装的默认本地存储策略仅允许上传图片（不含 SVG）、视频和音频，单个文件最大为 200MB；已有站点的存储策略配置保持不变 by @ruibaby in #10365
- 移除旧「用户设置」和「文章设置」中的附件存储项；仍使用旧配置的站点需改用「附件配置」中的对应策略和分组，旧个人中心上传接口也统一使用「个人中心附件配置」 by @ruibaby in #10346
- 编辑器支持在表格自适应模式下调整列宽，保持表格总宽度为 100%，并在容器宽度变化后保留列宽比例 by @ruibaby in #10369
- 缩短新生成的个人访问令牌（PAT）长度，已有令牌仍可使用至撤销或过期 by @JohnNiang in #10367
- 超级管理员在 Console 用户管理中重置密码时不再需要二次安全验证，个人中心修改密码仍保留安全验证 by @ruibaby in #10368
- 更新默认预置的评论、代码高亮、超链接卡片、AI 基础功能及应用市场插件版本 by @ruibaby in #10350

## 问题修复

- 修复默认本地存储策略的配置在重启后被还原的问题 by @bedhere in #10253
- 修复按作者筛选文章或页面时，未列出仅被设为作者但未参与编辑的内容的问题 by @ryanchou1994 in #10274
- 修复投稿者可通过个人中心自行置顶文章或绕过发布权限的问题 by @ruibaby in #10344
- 修复拥有文章或页面查看权限的用户无法预览他人创建的未发布内容的问题 by @ruibaby in #10337
- 修复“待审核”评论筛选遗漏含待审核回复的评论树的问题 by @kin
```
</details>

---
### 📦 [emoacht/Monitorian](https://github.com/emoacht/Monitorian)
`⭐ Stars: 4,767` &nbsp;|&nbsp; `💻 语言: C#` &nbsp;|&nbsp; `🏷️ 最新版本: [4.16.2-Installer](https://github.com/emoacht/Monitorian/releases/tag/4.16.2-Installer) (2026-10-12)`

> **简介**：轻松调节多台显示器亮度的 Windows 桌面工具

**💡 核心亮点更新 (中文)**：
- 改进内部代码

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
- Improve internal code
```
</details>

---
### 📦 [YerongAI/Office-Tool](https://github.com/YerongAI/Office-Tool)
`⭐ Stars: 14,545` &nbsp;|&nbsp; `💻 语言: PowerShell` &nbsp;|&nbsp; `🏷️ 最新版本: [v11.8.50.0](https://github.com/YerongAI/Office-Tool/releases/tag/v11.8.50.0) (2026-10-18)`

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
### 📦 [TDesktop-x64/tdesktop](https://github.com/TDesktop-x64/tdesktop)
`⭐ Stars: 2,979` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.2.10](https://github.com/TDesktop-x64/tdesktop/releases/tag/v1.2.10) (2026-09-21)`

> **简介**：64Gram（非官方 Telegram 桌面）

**💡 核心亮点更新 (中文)**：
v1.2.10 (TDesktop v7.2.9)

没有变更日志:)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
v1.2.10 (TDesktop v7.2.9)

No changelog :)
```
</details>

---
### 📦 [microsoft/vscode](https://github.com/microsoft/vscode)
`⭐ Stars: 193,936` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [1.142.0](https://github.com/microsoft/vscode/releases/tag/1.142.0) (2026-10-14)`

> **简介**：视觉工作室代码

**💡 核心亮点更新 (中文)**：
https://code.visualstudio.com/updates/v1_142

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
https://code.visualstudio.com/updates/v1_142
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
`⭐ Stars: 39,003` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.14.3](https://github.com/SagerNet/sing-box/releases/tag/v1.14.3) (2026-10-09)`

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
`⭐ Stars: 10,721` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [2.42.6](https://github.com/sub-store-org/Sub-Store/releases/tag/2.42.6) (2026-10-18)`

> **简介**：QX、Loon、Surge、Stash、Egern 和 Shadowrocket 的高级订阅管理器！

**💡 核心亮点更新 (中文)**：
<小>2.42.6（2026-10-18）</小>

* 发布：凹凸版本 ([1f0318b](https://github.com/sub-store-org/Sub-Store/commit/1f0318b))

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## <small>2.42.6 (2026-10-18)</small>

* release: bump version ([1f0318b](https://github.com/sub-store-org/Sub-Store/commit/1f0318b))
```
</details>

---
### 📦 [enfein/mieru](https://github.com/enfein/mieru)
`⭐ Stars: 2,607` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.38.1](https://github.com/enfein/mieru/releases/tag/v3.38.1) (2026-10-11)`

> **简介**：mieru is a socks5 / HTTP / HTTPS proxy to bypass censorship. 見える是一款 socks5 / HTTP / HTTPS 网络代理翻墙工具。

**💡 核心亮点更新 (中文)**：
1. Fix a bug of possible infinite read retry when QUIC is used as dialer proxy.
2. Fix several issues about socks5 user authentication and private IP address protection.
3. Fix race condition in time series metrics.

---

1. 修复了当使用 QUIC 拨号代理时，可

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
1. Fix a bug of possible infinite read retry when QUIC is used as dialer proxy.
2. Fix several issues about socks5 user authentication and private IP address protection.
3. Fix race condition in time series metrics.

---

1. 修复了当使用 QUIC 拨号代理时，可能会无限重试读取数据的问题。 
2. 修复了 socks5 用户验证和私有 IP 地址保护的一些问题。
3. 修复了时间序列指标中的竞争条件。
```
</details>

---
### 📦 [v2rayA/v2rayA](https://github.com/v2rayA/v2rayA)
`⭐ Stars: 15,705` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.5.10](https://github.com/v2rayA/v2rayA/releases/tag/v2.5.10) (2026-10-09)`

> **简介**：A web client for its own Xray-based core with global transparent proxy on Linux, Windows and macOS.

**💡 核心亮点更新 (中文)**：
* feat: separate DNS service from interception by  in https://github.com/v2rayA/v2rayA/pull/2082
* fix(db): drop obsolete legacy outbound tables to prevent foreign key constraint failed (787) on node deletion by  in https://github.com/v2rayA/v2rayA/pull/2080

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## What's Changed
* feat: separate DNS service from interception by @ILIKEFUTANARI in https://github.com/v2rayA/v2rayA/pull/2082
* fix(db): drop obsolete legacy outbound tables to prevent foreign key constraint failed (787) on node deletion by @ArianPashae in https://github.com/v2rayA/v2rayA/pull/2080

## New Contributors
* @ILIKEFUTANARI made their first contribution in https://github.com/v2rayA/v2rayA/pull/2082
* @ArianPashae made their first contribution in https://github.com/v2rayA/v2rayA/pull/2080

**Full Changelog**: https://github.com/v2rayA/v2rayA/compare/v2.5.9...v2.5.10
```
</details>

---
### 📦 [vernesong/OpenClash](https://github.com/vernesong/OpenClash)
`⭐ Stars: 27,837` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.48.002](https://github.com/vernesong/OpenClash/releases/tag/v0.48.002) (2026-10-12)`

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

```SHELL
# [iptables for ipk]
opkg update
opkg install bash iptables dnsmasq-full curl ca-bundle ipset ip-full iptables-mod-tproxy iptables-mod-extra ruby ruby-yaml kmod-tun kmod-inet-diag unzip luci-compat luci luci-base
curl -L --retry 2 https://api.github.com/repos/vernesong/OpenClash/releases/latest -o /tmp/openclash_version
[ -f "/tmp/openclash_version" ] && download_url=$(cat /tmp/openclash_version | jsonfilter -e '@.assets[*].browser_download_url' | grep '\.ipk$') && curl -L --retry 2 "$download_url" -o /tmp/openclash.ipk || echo "OpenClash last version get failed"
[ -f "/tmp/openclash.ipk" ] && opkg install /tmp/openclash.ipk || echo "OpenClash download failed"

```
```SHELL
# [iptables for apk]
apk update
apk add bash iptables dnsmasq-full curl ca-bundle ipset ip-full iptables-mod-tproxy iptables-mod-extra ruby ruby-yaml kmod-tun kmod-inet-diag unzip luci-compat luci luci-base
curl -L --retry 2 https://api.github.com/repos/vernesong/OpenClash/releases/latest -o /tmp/openclash_version
[ -f "/tmp/openclash_version" ] && download_url=$(cat /tmp/openclash_version | jsonfilter -e '@.assets[*].browser_download_url' | grep '\.apk$') && curl -L --retry 2 "$download_url" -o /tmp/openclash.apk || echo "OpenClash last version get failed"
[ -f "/tmp/openclash.apk" ] && apk add -q --force-overwrit
```
</details>

---
### 📦 [HyNetworks/hysteria](https://github.com/HyNetworks/hysteria)
`⭐ Stars: 22,678` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [app/v2.13.0](https://github.com/HyNetworks/hysteria/releases/tag/app/v2.13.0) (2026-10-05)`

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
`⭐ Stars: 2,774` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [25.12.6](https://github.com/QiuSimons/YAOF/releases/tag/25.12.6) (2026-10-18)`

> **简介**：适用于 Nanopi R2C/R2S/R4S/X86 的 OpenWrt

**💡 核心亮点更新 (中文)**：
该版本未提供详细更新说明。

---
### 📦 [Loyalsoldier/v2ray-rules-dat](https://github.com/Loyalsoldier/v2ray-rules-dat)
`⭐ Stars: 20,894` &nbsp;|&nbsp; `💻 语言: Other` &nbsp;|&nbsp; `🏷️ 最新版本: [202610182205](https://github.com/Loyalsoldier/v2ray-rules-dat/releases/tag/202610182205) (2026-10-18)`

> **简介**：🦄 🎃 👻 V2Ray 路由规则文件加强版，可代替 V2Ray 官方 geoip.dat 和 geosite.dat，适用于 V2Ray、Xray-core、mihomo(Clash-Meta)、hysteria、Trojan-Go 和 leaf。Enhanced edition of V2Ray rules dat files, applicable to V2Ray, Xray-core, mihomo(Clash-Meta), hysteria, Trojan-Go and leaf.

**💡 核心亮点更新 (中文)**：
该版本未提供详细更新说明。

---
### 📦 [Openwrt-Passwall/openwrt-passwall](https://github.com/Openwrt-Passwall/openwrt-passwall)
`⭐ Stars: 9,967` &nbsp;|&nbsp; `💻 语言: Lua` &nbsp;|&nbsp; `🏷️ 最新版本: [26.10.16-2](https://github.com/Openwrt-Passwall/openwrt-passwall/releases/tag/26.10.16-2) (2026-10-16)`

> **简介**：暂无项目描述

**💡 核心亮点更新 (中文)**：
* 请按照 [openwrt-passwall-build](https://github.com/moetayuko/openwrt-passwall-build) 仓库的说明，将其提供的软件源添加到设备中，然后直接使用包管理器安装。
* 从 [SourceForge](https://sourceforge.net/projects/openwrt-passwall-build/files/) 下载预构建的软件包。
* 将文件上传到您的设备，使用 Shell 命令进行安装。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
![](https://img.shields.io/github/downloads/Openwrt-Passwall/openwrt-passwall/26.10.16-2/total?style=flat-square)
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
```
</details>

---
### 📦 [2dust/v2rayN](https://github.com/2dust/v2rayN)
`⭐ Stars: 118,575` &nbsp;|&nbsp; `💻 语言: C#` &nbsp;|&nbsp; `🏷️ 最新版本: [7.25.6](https://github.com/2dust/v2rayN/releases/tag/7.25.6) (2026-10-11)`

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

## <span id="-实用开源精选">📦 实用开源精选</span>

### 📦 [NeverSinkDev/NeverSink-Filter-for-PoE2](https://github.com/NeverSinkDev/NeverSink-Filter-for-PoE2)
`⭐ Stars: 2,858` &nbsp;|&nbsp; `💻 语言: Other` &nbsp;|&nbsp; `🏷️ 最新版本: [0.10.4a](https://github.com/NeverSinkDev/NeverSink-Filter-for-PoE2/releases/tag/0.10.4a) (2026-10-15)`

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
`⭐ Stars: 165` &nbsp;|&nbsp; `💻 语言: Shell` &nbsp;|&nbsp; `🏷️ 最新版本: [2026.10.19-15/33_aarch64_generic](https://github.com/kenzok8/compile-package/releases/tag/2026.10.19-15/33_aarch64_generic) (2026-10-19)`

> **简介**：small-package仓库，每日更新插件编译

**💡 核心亮点更新 (中文)**：
定时更新插件，推送发布 💤:

[下载链接] (https://dllkids.xyz/packages/aarch64_generic/)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
定时更新插件，推送发布 💤:

[下载链接] (https://dllkids.xyz/packages/aarch64_generic/)
```
</details>

---
### 📦 [jxxghp/MoviePilot](https://github.com/jxxghp/MoviePilot)
`⭐ Stars: 11,900` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.1.8](https://github.com/jxxghp/MoviePilot/releases/tag/v3.1.8) (2026-10-19)`

> **简介**：NAS媒体库自动化管理工具

**💡 核心亮点更新 (中文)**：
- 优化 Emby、Jellyfin、Plex、Navidrome 查询，按首页展示、媒体查重、入库同步等场景获取所需信息，减少不必要的查询与解析开销。
- 修复自动整理音乐时未同步本地封面的问题，按本地音乐封面设置随音乐文件同步封面。
- 修复 TXT、LRC、Lyricsfile 等歌词文件的权限，遵循部署的 UMASK 设置，避免不同用户运行的媒体服务器无法读取歌词。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 本次更新内容

- 优化 Emby、Jellyfin、Plex、Navidrome 查询，按首页展示、媒体查重、入库同步等场景获取所需信息，减少不必要的查询与解析开销。
- 修复自动整理音乐时未同步本地封面的问题，按本地音乐封面设置随音乐文件同步封面。
- 修复 TXT、LRC、Lyricsfile 等歌词文件的权限，遵循部署的 UMASK 设置，避免不同用户运行的媒体服务器无法读取歌词。
- 修复热门订阅年份的返回类型，恢复相关数据的正常展示。
- 修复 Transmission 空文件列表被解释为“全部文件”的问题；未匹配到目标集数时保持任务暂停，避免错误下载或排除文件。
- 改进 Agent 执行图、模型与中间件的资源管理，完善构建取消、缓存替换和会话关闭时的回收，避免提前关闭仍在使用的资源。

## 完整变更记录

- refactor(agent): centralize graph resource ownership (#7062) by @DDSRem ([e1b703a](https://github.com/jxxghp/MoviePilot/commit/e1b703aacc4589fec01a1d9753b54d96cf21e94d))
- fix(music): sync local covers during automatic transfers (#7064) by @jxxghp ([05967cd](https://github.com/jxxghp/MoviePilot/commit/05967cdc0f10c93b55a7a01acd34c57d5f15df67))
- fix(music): honor umask when publishing lyric sidecars (#7065) by @yangn0 ([3b41159](https://github.com/jxxghp/MoviePilot/commit/3b4115957ff0901667c2e31d584e15718bbdc124))
- perf(mediaserver): add caller-controlled query projections (#7068) by @Aqr-K ([bf4ef42](https://github.com/jxxghp/MoviePilot/commit/bf4ef4214e561b75fbf7ba973cd0bbc9ecb62236))
- fix: restore popular years and safe Transmission selection by @jxxghp ([4f98486](https://github.com/jxxghp/MoviePilot/commit/4f98486e25a9e41b640288691ed5c77663ab712f))
- chore(release): publish v3.1.8 by @jxxghp ([3fa49db](https://github.com/jxxghp/MoviePilot/commit/3fa49db3afe0f7dfa8b7e7ce8fe6f43ceed7dfaf))
- fix(filemanager): skip subitems that vanish during local listing (#7076) by @JontyLee ([6b107e3](https://github.com/j
```
</details>

---
### 📦 [openwrt/openwrt](https://github.com/openwrt/openwrt)
`⭐ Stars: 28,822` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [v25.12.6](https://github.com/openwrt/openwrt/releases/tag/v25.12.6) (2026-10-18)`

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
### 📦 [sandboxie-plus/Sandboxie](https://github.com/sandboxie-plus/Sandboxie)
`⭐ Stars: 19,717` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.18.8](https://github.com/sandboxie-plus/Sandboxie/releases/tag/v1.18.8) (2026-10-17)`

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
`⭐ Stars: 4,885` &nbsp;|&nbsp; `💻 语言: C#` &nbsp;|&nbsp; `🏷️ 最新版本: [10.0.10](https://github.com/HMBSbige/NatTypeTester/releases/tag/10.0.10) (2026-10-08)`

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

## <span id="-系统与开发者工具">🛠️ 系统与开发者工具</span>

### 📦 [Icalingua-plus-plus/Icalingua-plus-plus](https://github.com/Icalingua-plus-plus/Icalingua-plus-plus)
`⭐ Stars: 3,382` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.26.8](https://github.com/Icalingua-plus-plus/Icalingua-plus-plus/releases/tag/v2.26.8) (2026-09-23)`

> **简介**：QQ等客户端。 ：电子：

**💡 核心亮点更新 (中文)**：
* 优化 缓解版本过低的问题
* 修复 文件管理器的 XSS 漏洞
* 修复 多实例下语音转换可能出现的重命名失败问题

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## What's Changed
* 优化 缓解版本过低的问题
* 修复 文件管理器的 XSS 漏洞
* 修复 多实例下语音转换可能出现的重命名失败问题
* 修复 滑块、登录频繁验证，触发 237 后可以短信验证
* 修复 Windows ARM64 安装后缺少主程序和 DLL 的问题 by @XuSai1998 in #841

**Full Changelog**: https://github.com/Icalingua-plus-plus/Icalingua-plus-plus/compare/v2.26.6...v2.26.8
```
</details>

---
### 📦 [ventoy/Ventoy](https://github.com/ventoy/Ventoy)
`⭐ Stars: 80,170` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.1.18](https://github.com/ventoy/Ventoy/releases/tag/v1.1.18) (2026-10-09)`

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
| [cityflow-project/CityFlow](https://github.com/cityflow-project/CityFlow) | 1,029 | 超过 425 天无代码提交 | [进入取消 Star](https://github.com/cityflow-project/CityFlow) |
| [facebookresearch/demucs](https://github.com/facebookresearch/demucs) | 10,396 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/facebookresearch/demucs) |
| [JimmyLv/awesome-nano-banana](https://github.com/JimmyLv/awesome-nano-banana) | 8,804 | 超过 405 天无代码提交 | [进入取消 Star](https://github.com/JimmyLv/awesome-nano-banana) |
| [btjawa/BiliTools](https://github.com/btjawa/BiliTools) | 5,056 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/btjawa/BiliTools) |
| [ehang-io/nps](https://github.com/ehang-io/nps) | 34,248 | 超过 872 天无代码提交 | [进入取消 Star](https://github.com/ehang-io/nps) |
| [ReturnFI/Blitz](https://github.com/ReturnFI/Blitz) | 1,091 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/ReturnFI/Blitz) |
| [kkangert/kspider](https://github.com/kkangert/kspider) | 1,265 | 超过 791 天无代码提交 | [进入取消 Star](https://github.com/kkangert/kspider) |
| [xenova/whisper-web](https://github.com/xenova/whisper-web) | 3,346 | 超过 747 天无代码提交 | [进入取消 Star](https://github.com/xenova/whisper-web) |
| [shadowsocks/luci-app-shadowsocks](https://github.com/shadowsocks/luci-app-shadowsocks) | 1,150 | 超过 1239 天无代码提交 | [进入取消 Star](https://github.com/shadowsocks/luci-app-shadowsocks) |
| [adithya-s-k/marker-api](https://github.com/adithya-s-k/marker-api) | 984 | 超过 733 天无代码提交 | [进入取消 Star](https://github.com/adithya-s-k/marker-api) |
| [yuchannslv5/warpflare](https://github.com/yuchannslv5/warpflare) | 334 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/yuchannslv5/warpflare) |
| [vvbbnn00/WARP-Clash-API](https://github.com/vvbbnn00/WARP-Clash-API) | 8,817 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/vvbbnn00/WARP-Clash-API) |
| [ca110us/epeius](https://github.com/ca110us/epeius) | 1,225 | 超过 791 天无代码提交 | [进入取消 Star](https://github.com/ca110us/epeius) |
| [chika0801/hysteria-install](https://github.com/chika0801/hysteria-install) | 178 | 超过 836 天无代码提交 | [进入取消 Star](https://github.com/chika0801/hysteria-install) |
| [yeahwu/InstallOS](https://github.com/yeahwu/InstallOS) | 85 | 超过 1593 天无代码提交 | [进入取消 Star](https://github.com/yeahwu/InstallOS) |
| [bulianglin/psub](https://github.com/bulianglin/psub) | 1,765 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/bulianglin/psub) |
| [lizongying/my-tv](https://github.com/lizongying/my-tv) | 31,962 | 超过 851 天无代码提交 | [进入取消 Star](https://github.com/lizongying/my-tv) |
| [joevess/IPTV](https://github.com/joevess/IPTV) | 10,282 | 超过 656 天无代码提交 | [进入取消 Star](https://github.com/joevess/IPTV) |
| [lecepin/WeChatVideoDownloader](https://github.com/lecepin/WeChatVideoDownloader) | 4,669 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/lecepin/WeChatVideoDownloader) |
| [linexjlin/GPTs](https://github.com/linexjlin/GPTs) | 32,037 | 超过 752 天无代码提交 | [进入取消 Star](https://github.com/linexjlin/GPTs) |
| [lxfater/Awesome-GPTs](https://github.com/lxfater/Awesome-GPTs) | 1,152 | 超过 1062 天无代码提交 | [进入取消 Star](https://github.com/lxfater/Awesome-GPTs) |
| [ClashDotNetFramework/experimental-clash](https://github.com/ClashDotNetFramework/experimental-clash) | 241 | 超过 1778 天无代码提交 | [进入取消 Star](https://github.com/ClashDotNetFramework/experimental-clash) |
| [zzzgydi/clash-verge](https://github.com/zzzgydi/clash-verge) | 21,876 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/zzzgydi/clash-verge) |
| [ddgth/cf2dns](https://github.com/ddgth/cf2dns) | 5,206 | 超过 651 天无代码提交 | [进入取消 Star](https://github.com/ddgth/cf2dns) |
| [zizifn/edgetunnel](https://github.com/zizifn/edgetunnel) | 9,265 | 超过 691 天无代码提交 | [进入取消 Star](https://github.com/zizifn/edgetunnel) |
| [missuo/Hysteria2](https://github.com/missuo/Hysteria2) | 203 | 超过 781 天无代码提交 | [进入取消 Star](https://github.com/missuo/Hysteria2) |
| [Misaka-blog/hysteria-install](https://github.com/Misaka-blog/hysteria-install) | 628 | 超过 913 天无代码提交 | [进入取消 Star](https://github.com/Misaka-blog/hysteria-install) |
| [MatsuriDayo/nekoray](https://github.com/MatsuriDayo/nekoray) | 15,294 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/MatsuriDayo/nekoray) |
| [FranzKafkaYu/x-ui](https://github.com/FranzKafkaYu/x-ui) | 8,463 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/FranzKafkaYu/x-ui) |
| [rwv/chinese-dos-games](https://github.com/rwv/chinese-dos-games) | 10,333 | 超过 803 天无代码提交 | [进入取消 Star](https://github.com/rwv/chinese-dos-games) |
| [getumbrel/llama-gpt](https://github.com/getumbrel/llama-gpt) | 10,920 | 超过 908 天无代码提交 | [进入取消 Star](https://github.com/getumbrel/llama-gpt) |
| [WangWenBin2017/OpenWrt-SSRPLUS](https://github.com/WangWenBin2017/OpenWrt-SSRPLUS) | 563 | 超过 595 天无代码提交 | [进入取消 Star](https://github.com/WangWenBin2017/OpenWrt-SSRPLUS) |
| [prompt-engineering/click-prompt](https://github.com/prompt-engineering/click-prompt) | 2,387 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/prompt-engineering/click-prompt) |
| [AutodeskAILab/Building-GAN](https://github.com/AutodeskAILab/Building-GAN) | 101 | 超过 1598 天无代码提交 | [进入取消 Star](https://github.com/AutodeskAILab/Building-GAN) |
| [novicezk/midjourney-proxy](https://github.com/novicezk/midjourney-proxy) | 5,368 | 超过 442 天无代码提交 | [进入取消 Star](https://github.com/novicezk/midjourney-proxy) |
| [adams549659584/go-proxy-bingai](https://github.com/adams549659584/go-proxy-bingai) | 8,413 | 超过 943 天无代码提交 | [进入取消 Star](https://github.com/adams549659584/go-proxy-bingai) |
| [tryptech/obs-zoom-and-follow](https://github.com/tryptech/obs-zoom-and-follow) | 440 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/tryptech/obs-zoom-and-follow) |
| [XingangPan/DragGAN](https://github.com/XingangPan/DragGAN) | 35,726 | 超过 883 天无代码提交 | [进入取消 Star](https://github.com/XingangPan/DragGAN) |
| [lewangdev/faster-whisper-youtube](https://github.com/lewangdev/faster-whisper-youtube) | 560 | 超过 1156 天无代码提交 | [进入取消 Star](https://github.com/lewangdev/faster-whisper-youtube) |
| [artidoro/qlora](https://github.com/artidoro/qlora) | 11,048 | 超过 860 天无代码提交 | [进入取消 Star](https://github.com/artidoro/qlora) |
| [langgenius/webapp-conversation](https://github.com/langgenius/webapp-conversation) | 1,101 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/langgenius/webapp-conversation) |
| [3andne/restls](https://github.com/3andne/restls) | 375 | 超过 1079 天无代码提交 | [进入取消 Star](https://github.com/3andne/restls) |
| [jtsang4/claude-to-chatgpt](https://github.com/jtsang4/claude-to-chatgpt) | 1,301 | 超过 792 天无代码提交 | [进入取消 Star](https://github.com/jtsang4/claude-to-chatgpt) |
| [yorunning/clash-conf](https://github.com/yorunning/clash-conf) | 102 | 超过 824 天无代码提交 | [进入取消 Star](https://github.com/yorunning/clash-conf) |
| [svc-develop-team/so-vits-svc](https://github.com/svc-develop-team/so-vits-svc) | 28,072 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/svc-develop-team/so-vits-svc) |
| [xiaye13579/BBLL](https://github.com/xiaye13579/BBLL) | 17,476 | 超过 598 天无代码提交 | [进入取消 Star](https://github.com/xiaye13579/BBLL) |
| [camenduru/MiniGPT-4-colab](https://github.com/camenduru/MiniGPT-4-colab) | 120 | 超过 1176 天无代码提交 | [进入取消 Star](https://github.com/camenduru/MiniGPT-4-colab) |
| [Vision-CAIR/MiniGPT-4](https://github.com/Vision-CAIR/MiniGPT-4) | 25,584 | 超过 777 天无代码提交 | [进入取消 Star](https://github.com/Vision-CAIR/MiniGPT-4) |
| [imfuxiao/Hamster](https://github.com/imfuxiao/Hamster) | 1,639 | 超过 524 天无代码提交 | [进入取消 Star](https://github.com/imfuxiao/Hamster) |
| [acheong08/ChatGPT](https://github.com/acheong08/ChatGPT) | 27,938 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/acheong08/ChatGPT) |
| [microsoft/JARVIS](https://github.com/microsoft/JARVIS) | 25,456 | 超过 446 天无代码提交 | [进入取消 Star](https://github.com/microsoft/JARVIS) |
| [choephix/auto-gpt-webui](https://github.com/choephix/auto-gpt-webui) | 116 | 超过 944 天无代码提交 | [进入取消 Star](https://github.com/choephix/auto-gpt-webui) |
| [Moonvy/OpenPromptStudio](https://github.com/Moonvy/OpenPromptStudio) | 6,703 | 超过 904 天无代码提交 | [进入取消 Star](https://github.com/Moonvy/OpenPromptStudio) |
| [facebookresearch/segment-anything](https://github.com/facebookresearch/segment-anything) | 55,036 | 超过 760 天无代码提交 | [进入取消 Star](https://github.com/facebookresearch/segment-anything) |
| [zai-org/ChatGLM-6B](https://github.com/zai-org/ChatGLM-6B) | 40,909 | 超过 844 天无代码提交 | [进入取消 Star](https://github.com/zai-org/ChatGLM-6B) |
| [ihciah/shadow-tls](https://github.com/ihciah/shadow-tls) | 2,681 | 超过 541 天无代码提交 | [进入取消 Star](https://github.com/ihciah/shadow-tls) |
| [jxbbb/ADAPT](https://github.com/jxbbb/ADAPT) | 421 | 超过 860 天无代码提交 | [进入取消 Star](https://github.com/jxbbb/ADAPT) |
| [mayooear/ai-pdf-chatbot-langchain](https://github.com/mayooear/ai-pdf-chatbot-langchain) | 16,582 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/mayooear/ai-pdf-chatbot-langchain) |
| [lencx/ChatGPT](https://github.com/lencx/ChatGPT) | 54,638 | 超过 780 天无代码提交 | [进入取消 Star](https://github.com/lencx/ChatGPT) |
| [nekohasekai/SagerNet](https://github.com/nekohasekai/SagerNet) | 54 | 超过 1743 天无代码提交 | [进入取消 Star](https://github.com/nekohasekai/SagerNet) |
| [P3TERX/Actions-OpenWrt](https://github.com/P3TERX/Actions-OpenWrt) | 7,621 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/P3TERX/Actions-OpenWrt) |
| [R86S/R86S-QuickInstaller](https://github.com/R86S/R86S-QuickInstaller) | 65 | 超过 1164 天无代码提交 | [进入取消 Star](https://github.com/R86S/R86S-QuickInstaller) |
| [WeNeedHome/SummaryOfLoanSuspension](https://github.com/WeNeedHome/SummaryOfLoanSuspension) | 20,341 | 超过 828 天无代码提交 | [进入取消 Star](https://github.com/WeNeedHome/SummaryOfLoanSuspension) |
| [zanzhz1101/LingMaxDNS](https://github.com/zanzhz1101/LingMaxDNS) | 23 | 超过 1559 天无代码提交 | [进入取消 Star](https://github.com/zanzhz1101/LingMaxDNS) |
| [IrineSistiana/mosdns-cn](https://github.com/IrineSistiana/mosdns-cn) | 325 | 超过 1601 天无代码提交 | [进入取消 Star](https://github.com/IrineSistiana/mosdns-cn) |
| [chika0801/Xray-install](https://github.com/chika0801/Xray-install) | 273 | 超过 1052 天无代码提交 | [进入取消 Star](https://github.com/chika0801/Xray-install) |
| [alesimula/wsa_pacman](https://github.com/alesimula/wsa_pacman) | 4,190 | 超过 1031 天无代码提交 | [进入取消 Star](https://github.com/alesimula/wsa_pacman) |
| [scutan90/DeepLearning-500-questions](https://github.com/scutan90/DeepLearning-500-questions) | 57,673 | 超过 844 天无代码提交 | [进入取消 Star](https://github.com/scutan90/DeepLearning-500-questions) |
| [Chikage0o0/Linux-NetSpeed](https://github.com/Chikage0o0/Linux-NetSpeed) | 3,746 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/Chikage0o0/Linux-NetSpeed) |
| [KFERMercer/OpenWrt-CI](https://github.com/KFERMercer/OpenWrt-CI) | 1,409 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/KFERMercer/OpenWrt-CI) |
| [qTox/qTox](https://github.com/qTox/qTox) | 4,968 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/qTox/qTox) |
| [quericy/one-key-ikev2-vpn](https://github.com/quericy/one-key-ikev2-vpn) | 2,104 | 超过 2163 天无代码提交 | [进入取消 Star](https://github.com/quericy/one-key-ikev2-vpn) |
| [riverscn/openwrt-iptvhelper](https://github.com/riverscn/openwrt-iptvhelper) | 371 | 超过 1879 天无代码提交 | [进入取消 Star](https://github.com/riverscn/openwrt-iptvhelper) |
| [frainzy1477/luci-app-clash](https://github.com/frainzy1477/luci-app-clash) | 1,623 | 超过 1669 天无代码提交 | [进入取消 Star](https://github.com/frainzy1477/luci-app-clash) |
| [Sanster/IOPaint](https://github.com/Sanster/IOPaint) | 23,305 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/Sanster/IOPaint) |
| [LANDrop/LANDrop](https://github.com/LANDrop/LANDrop) | 5,986 | 超过 796 天无代码提交 | [进入取消 Star](https://github.com/LANDrop/LANDrop) |
| [saveweb/review-2021](https://github.com/saveweb/review-2021) | 759 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/saveweb/review-2021) |
| [iranee/qnap-aliyunpan-webdav](https://github.com/iranee/qnap-aliyunpan-webdav) | 274 | 超过 1472 天无代码提交 | [进入取消 Star](https://github.com/iranee/qnap-aliyunpan-webdav) |
| [haoel/haoel.github.io](https://github.com/haoel/haoel.github.io) | 13,076 | 超过 1257 天无代码提交 | [进入取消 Star](https://github.com/haoel/haoel.github.io) |
| [tindy2013/stairspeedtest-reborn](https://github.com/tindy2013/stairspeedtest-reborn) | 3,836 | 超过 1228 天无代码提交 | [进入取消 Star](https://github.com/tindy2013/stairspeedtest-reborn) |
| [P3TERX/warp.sh](https://github.com/P3TERX/warp.sh) | 3,930 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/P3TERX/warp.sh) |
| [TheMRLL/WinXray](https://github.com/TheMRLL/WinXray) | 2,792 | 超过 965 天无代码提交 | [进入取消 Star](https://github.com/TheMRLL/WinXray) |
| [Mikubill/cowtransfer-uploader](https://github.com/Mikubill/cowtransfer-uploader) | 447 | 超过 1712 天无代码提交 | [进入取消 Star](https://github.com/Mikubill/cowtransfer-uploader) |
| [281677160/build-actions](https://github.com/281677160/build-actions) | 390 | 超过 447 天无代码提交 | [进入取消 Star](https://github.com/281677160/build-actions) |
| [vaxilu/x-ui](https://github.com/vaxilu/x-ui) | 19,079 | 超过 791 天无代码提交 | [进入取消 Star](https://github.com/vaxilu/x-ui) |
| [xinntao/Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) | 37,145 | 超过 803 天无代码提交 | [进入取消 Star](https://github.com/xinntao/Real-ESRGAN) |
| [zu1k/proxypool](https://github.com/zu1k/proxypool) | 4,036 | 超过 1287 天无代码提交 | [进入取消 Star](https://github.com/zu1k/proxypool) |
| [TachibanaYoshino/AnimeGAN](https://github.com/TachibanaYoshino/AnimeGAN) | 4,611 | 超过 1537 天无代码提交 | [进入取消 Star](https://github.com/TachibanaYoshino/AnimeGAN) |
| [yuanzhoulvpi2017/tiny_python](https://github.com/yuanzhoulvpi2017/tiny_python) | 173 | 超过 1352 天无代码提交 | [进入取消 Star](https://github.com/yuanzhoulvpi2017/tiny_python) |
| [haiibo/OpenWrt](https://github.com/haiibo/OpenWrt) | 3,163 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/haiibo/OpenWrt) |
| [VergilGao/openwrt-packages](https://github.com/VergilGao/openwrt-packages) | 11 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/VergilGao/openwrt-packages) |
| [VergilGao/openwrt-compiler](https://github.com/VergilGao/openwrt-compiler) | 13 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/VergilGao/openwrt-compiler) |
| [OpenELEC/OpenELEC.tv](https://github.com/OpenELEC/OpenELEC.tv) | 1,618 | 超过 3334 天无代码提交 | [进入取消 Star](https://github.com/OpenELEC/OpenELEC.tv) |
| [github/copilot-docs](https://github.com/github/copilot-docs) | 23,175 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/github/copilot-docs) |
| [Kiougar/luci-wrtbwmon](https://github.com/Kiougar/luci-wrtbwmon) | 356 | 超过 1851 天无代码提交 | [进入取消 Star](https://github.com/Kiougar/luci-wrtbwmon) |
| [EtherDream/jsproxy](https://github.com/EtherDream/jsproxy) | 9,325 | 超过 932 天无代码提交 | [进入取消 Star](https://github.com/EtherDream/jsproxy) |
| [cheat-engine/cheat-engine](https://github.com/cheat-engine/cheat-engine) | 19,344 | 超过 548 天无代码提交 | [进入取消 Star](https://github.com/cheat-engine/cheat-engine) |
| [ffffffff0x/Dork-Admin](https://github.com/ffffffff0x/Dork-Admin) | 1,916 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/ffffffff0x/Dork-Admin) |
| [ffffffff0x/Digital-Privacy](https://github.com/ffffffff0x/Digital-Privacy) | 4,940 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/ffffffff0x/Digital-Privacy) |
| [Autodesk/civilconnection](https://github.com/Autodesk/civilconnection) | 117 | 超过 1417 天无代码提交 | [进入取消 Star](https://github.com/Autodesk/civilconnection) |
| [0xHJK/CleanApps](https://github.com/0xHJK/CleanApps) | 165 | 超过 1883 天无代码提交 | [进入取消 Star](https://github.com/0xHJK/CleanApps) |
| [KANIKIG/Multi-EasyGost](https://github.com/KANIKIG/Multi-EasyGost) | 1,949 | 超过 931 天无代码提交 | [进入取消 Star](https://github.com/KANIKIG/Multi-EasyGost) |
| [Kurokosama/AutoBuild-OpenWRT](https://github.com/Kurokosama/AutoBuild-OpenWRT) | 89 | 超过 1570 天无代码提交 | [进入取消 Star](https://github.com/Kurokosama/AutoBuild-OpenWRT) |
| [differentrain/DeletionTool](https://github.com/differentrain/DeletionTool) | 94 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/differentrain/DeletionTool) |
| [hideuvpn/android-google-play-store](https://github.com/hideuvpn/android-google-play-store) | 3,625 | 超过 1552 天无代码提交 | [进入取消 Star](https://github.com/hideuvpn/android-google-play-store) |
| [XJP-GIT/AntiZhaPian](https://github.com/XJP-GIT/AntiZhaPian) | 3,159 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/XJP-GIT/AntiZhaPian) |
| [jerrykuku/luci-app-ttnode](https://github.com/jerrykuku/luci-app-ttnode) | 89 | 超过 1728 天无代码提交 | [进入取消 Star](https://github.com/jerrykuku/luci-app-ttnode) |
| [KevinSHIT/NaiveSharp](https://github.com/KevinSHIT/NaiveSharp) | 96 | 超过 2173 天无代码提交 | [进入取消 Star](https://github.com/KevinSHIT/NaiveSharp) |
| [prasmussen/gdrive](https://github.com/prasmussen/gdrive) | 8,943 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/prasmussen/gdrive) |
| [tostercx/GTAO_Booster_PoC](https://github.com/tostercx/GTAO_Booster_PoC) | 2,865 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/tostercx/GTAO_Booster_PoC) |
| [ilxp/luci-app-ikoolproxy](https://github.com/ilxp/luci-app-ikoolproxy) | 507 | 超过 584 天无代码提交 | [进入取消 Star](https://github.com/ilxp/luci-app-ikoolproxy) |
| [kiddin9/luci-app-dnsfilter](https://github.com/kiddin9/luci-app-dnsfilter) | 123 | 超过 617 天无代码提交 | [进入取消 Star](https://github.com/kiddin9/luci-app-dnsfilter) |
| [h31105/deployX.sh](https://github.com/h31105/deployX.sh) | 416 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/h31105/deployX.sh) |
| [jerrykuku/openwrt-package](https://github.com/jerrykuku/openwrt-package) | 148 | 超过 1080 天无代码提交 | [进入取消 Star](https://github.com/jerrykuku/openwrt-package) |
| [frainzy1477/luci-app-trojan](https://github.com/frainzy1477/luci-app-trojan) | 120 | 超过 1987 天无代码提交 | [进入取消 Star](https://github.com/frainzy1477/luci-app-trojan) |
| [atrandys/xray](https://github.com/atrandys/xray) | 89 | 超过 1695 天无代码提交 | [进入取消 Star](https://github.com/atrandys/xray) |
| [v2board/v2board](https://github.com/v2board/v2board) | 5,058 | 超过 944 天无代码提交 | [进入取消 Star](https://github.com/v2board/v2board) |
| [ShadowsocksR-Live/iShadowsocksR](https://github.com/ShadowsocksR-Live/iShadowsocksR) | 600 | 超过 902 天无代码提交 | [进入取消 Star](https://github.com/ShadowsocksR-Live/iShadowsocksR) |
| [SuperNG6/Aria2-Trackers](https://github.com/SuperNG6/Aria2-Trackers) | 309 | 超过 2094 天无代码提交 | [进入取消 Star](https://github.com/SuperNG6/Aria2-Trackers) |
| [kakaruoterl/vless_install](https://github.com/kakaruoterl/vless_install) | 29 | 超过 2251 天无代码提交 | [进入取消 Star](https://github.com/kakaruoterl/vless_install) |
| [stupidloud/nanopi-openwrt](https://github.com/stupidloud/nanopi-openwrt) | 5,515 | 超过 915 天无代码提交 | [进入取消 Star](https://github.com/stupidloud/nanopi-openwrt) |
| [atrandys/trojan](https://github.com/atrandys/trojan) | 1,055 | 超过 1284 天无代码提交 | [进入取消 Star](https://github.com/atrandys/trojan) |
| [programthink/zhao](https://github.com/programthink/zhao) | 14,071 | 超过 1904 天无代码提交 | [进入取消 Star](https://github.com/programthink/zhao) |
| [RPRX/v2ray-vless](https://github.com/RPRX/v2ray-vless) | 389 | 超过 1330 天无代码提交 | [进入取消 Star](https://github.com/RPRX/v2ray-vless) |
| [h2y/Shadowrocket-ADBlock-Rules](https://github.com/h2y/Shadowrocket-ADBlock-Rules) | 16,716 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/h2y/Shadowrocket-ADBlock-Rules) |
| [p4gefau1t/trojan-go](https://github.com/p4gefau1t/trojan-go) | 8,383 | 超过 827 天无代码提交 | [进入取消 Star](https://github.com/p4gefau1t/trojan-go) |
| [Jrohy/trojan](https://github.com/Jrohy/trojan) | 5,635 | 超过 917 天无代码提交 | [进入取消 Star](https://github.com/Jrohy/trojan) |
| [mellow-io/mellow](https://github.com/mellow-io/mellow) | 3,537 | 超过 1408 天无代码提交 | [进入取消 Star](https://github.com/mellow-io/mellow) |
| [Dawneng/luci-theme-atmaterial](https://github.com/Dawneng/luci-theme-atmaterial) | 11 | 超过 1460 天无代码提交 | [进入取消 Star](https://github.com/Dawneng/luci-theme-atmaterial) |
| [trojan-gfw/igniter](https://github.com/trojan-gfw/igniter) | 3,275 | 超过 1057 天无代码提交 | [进入取消 Star](https://github.com/trojan-gfw/igniter) |
| [openwrt-develop/luci-theme-atmaterial](https://github.com/openwrt-develop/luci-theme-atmaterial) | 68 | 超过 2405 天无代码提交 | [进入取消 Star](https://github.com/openwrt-develop/luci-theme-atmaterial) |
| [trojan-gfw/trojan-quickstart](https://github.com/trojan-gfw/trojan-quickstart) | 244 | 超过 2006 天无代码提交 | [进入取消 Star](https://github.com/trojan-gfw/trojan-quickstart) |
| [FunctionClub/ZBench](https://github.com/FunctionClub/ZBench) | 1,177 | 超过 2037 天无代码提交 | [进入取消 Star](https://github.com/FunctionClub/ZBench) |
| [veekxt/v2ray-template](https://github.com/veekxt/v2ray-template) | 749 | 超过 2249 天无代码提交 | [进入取消 Star](https://github.com/veekxt/v2ray-template) |
| [HMBSbige/ShadowsocksR-Windows](https://github.com/HMBSbige/ShadowsocksR-Windows) | 6,921 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/HMBSbige/ShadowsocksR-Windows) |
| [trojan-gfw/trojan](https://github.com/trojan-gfw/trojan) | 19,750 | 超过 789 天无代码提交 | [进入取消 Star](https://github.com/trojan-gfw/trojan) |
</details>
