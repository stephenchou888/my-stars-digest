# 📡 Starred 项目雷达看板
> 🖥️ **交互式管理看板 (shadcn/ui)**：[👉 点击进入在线雷达看板 (https://stephenchou888.github.io/my-stars-digest/)](https://stephenchou888.github.io/my-stars-digest/)

> **生成时间**：`2026-10-26` ｜ **关注项目总数**：`369` ｜ **本期更新**：`80` ｜ **弃坑预警**：`135`

| 统计指标 | 数量 | 状态提示 |
| :--- | :---: | :--- |
| 🌟 总关注库 | **369** | [进入 shadcn 在线看板管理](https://stephenchou888.github.io/my-stars-digest/) |
| 🚀 近期有更新 | **80** | 涵盖 6 个分类 |
| 🛑 建议清理/弃坑 | **135** | 建议取消 Star 保持关注列表整洁 |

---
## 🧭 领域分类速览导航

- [🤖 AI 与智能体生态 (41)](#-AI-与智能体生态)
- [📦 实用开源精选 (6)](#-实用开源精选)
- [🎬 影音媒体与下载 (12)](#-影音媒体与下载)
- [📝 效率办公与创作 (8)](#-效率办公与创作)
- [🌐 网络与代理技术 (11)](#-网络与代理技术)
- [🛠️ 系统与开发者工具 (2)](#-系统与开发者工具)

---

## <span id="-AI-与智能体生态">🤖 AI 与智能体生态</span>

### 📦 [Hsiung-Shao/exile-appraiser](https://github.com/Hsiung-Shao/exile-appraiser)
`⭐ Stars: 7` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.3.2](https://github.com/Hsiung-Shao/exile-appraiser/releases/tag/v0.3.2) (2026-10-16)`

> **简介**：ExileAppraiser / 流亡鑑價:Path of Exile 1/2 查價器,支援國際服與台服(繁中/英文客戶端)

**💡 核心亮点更新 (中文)**：
修正

・**詞綴被藏起來**：被偽屬性、護甲 / 閃避等合計吃掉的詞綴與符文詞綴，現在都會列出來。（放在「原始詞綴」卡，預設收起、不勾選）

新增

・**詞綴機制選擇**：每條詞綴可選一般 / 破裂 / 工藝，PoE2 另有褻瀆、增幅。（由底部「機制」開關顯示按鈕）

調整

・**「一般」的查法**：詞綴本身是工藝 / 破裂 / 褻瀆時，選「一般」會排除同機制的物品。
・**工藝二選一**：v0.3.1 的「一般 / 工藝」切換併入機制選擇。

說明：不勾選新列出的詞綴時，查價結果與上一版

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 修正

・**詞綴被藏起來**：被偽屬性、護甲 / 閃避等合計吃掉的詞綴與符文詞綴，現在都會列出來。（放在「原始詞綴」卡，預設收起、不勾選）

## 新增

・**詞綴機制選擇**：每條詞綴可選一般 / 破裂 / 工藝，PoE2 另有褻瀆、增幅。（由底部「機制」開關顯示按鈕）

## 調整

・**「一般」的查法**：詞綴本身是工藝 / 破裂 / 褻瀆時，選「一般」會排除同機制的物品。
・**工藝二選一**：v0.3.1 的「一般 / 工藝」切換併入機制選擇。

說明：不勾選新列出的詞綴時，查價結果與上一版相同。
```
</details>

---
### 📦 [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model)
`⭐ Stars: 43,410` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.7.2](https://github.com/Ebony-Vinyl/dsh-our-free-model/releases/tag/v2.7.2) (2026-10-26)`

> **简介**：在 dsh 里装上这个插件即可，无需登录、注册或填 API Key，就能使用包括 DeepSeek V4.1 Flash、Kimi K3 在内的前沿模型——完全免费，不限量。 All you do is install this plugin in dsh: no login, no sign-up, no API key — the frontier models are just there, DeepSeek V4.1 Flash and Kimi K3 among them. Completely free, with no usage cap.

**💡 核心亮点更新 (中文)**：
- Kilo 与匿名免费模型统一纳入免费池、标签数量和五格状态。
- 水位排除已限流、不可用、地区受限及隐藏的模型。26 个模型中 9 个限流时，17/26 显示为 65%。未探测仅作为候选，不冒充实测可用。
- 探测按模型使用独立上游会话，避免整轮共用配额造成批量限流误判。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# v2.7.2 插件发布

本次只发布插件，桌面安装包和独立产品版本保持原状。

## 修复旧版升级路径

此前旧升级器最多接受 80 个文件、每个文件最多 4 MiB，而 2.7.1 清单有 93 个文件，并包含约 65 MiB 的引擎。无论换哪个下载源，旧用户都会在读取清单时失败。

2.7.2 基于最新主线，将省 Token 模块合并为生成文件，引擎 gzip 压缩后拆成 9 个不超过 4 MiB 的分片。插件清单共 79 个文件，旧版可直接升级，无需先安装过渡版本。引擎首次启动时只读取本地分片，分别校验分片、压缩体和最终可执行文件摘要，按声明的解压上限还原到独立缓存；不从网络补取代码。

发布构建会拒绝超出旧版文件数量或体积预算的内容。历史升级器回归夹具直接取自 1.3.1、2.5.9 的原始 Git 对象，未放宽任何旧限制。运行时备份也补齐了引擎元数据及完整二进制，便于后续升级失败时回滚。

## 包含最新插件修复

- Kilo 与匿名免费模型统一纳入免费池、标签数量和五格状态。
- 水位排除已限流、不可用、地区受限及隐藏的模型。26 个模型中 9 个限流时，17/26 显示为 65%。未探测仅作为候选，不冒充实测可用。
- 探测按模型使用独立上游会话，避免整轮共用配额造成批量限流误判。

## 安装与验证边界

自行安装的旧版用户可在插件升级页检查并升级。由包管理器管理的安装继续通过宿主更新可信 tarball，不绕过托管策略。手工安装请使用本次完整插件包，保留原有用户数据目录，不要只替换入口文件。

发布前需通过完整贡献者检查、生产签名及旧版升级回归，具体证据见 PR 与发布校验记录。已验证的旧版场景包括下载、安装、模块加载、用户数据保留、激活失败回滚、坏分片拒绝和 Windows 引擎启动。测试仅访问本地服务，不代表所有网络环境或真实模型上游均已验证。

## 回退

升级激活失败时自动恢复旧包；恢复遇到文件系统错误时保留已验证备份和错误证据，不报告成功。手工回退使用上一版可信插件包，并保留用户配置、账号和统计数据。

## 本次发布验证

- 完整贡献者测试 98/98、生产签名发布检查 5/5，四项 GitHub CI 均通过。
- 原版 1.3.1、2.5.9 升级回归通过；原版 2.5.9 已从公开固定提交地址完成升级，默认升级源也确认提供 2.7.2。原版 1.3.1 已通过自身默认公开升级源下载、安装并加载 2.7.2；79 项运行时文件均匹配生产清单，用户数据保留。
- 正式 tarball 从固定提交的 LF 字节构建，解包后的全部 79 项运行时文件逐字节匹配生产签名清单，入口模块加载通过。
- 本次仅插件发布，**不提供新的桌面安装包**；桌面端仍为原有版本。
- 未执行真实模型上游调用；不同网络环境仍可能影响下载。

## 下载与校验

| 文件 | 说明 |
| --- | --- |
| `dsh-our-free-model-2.7.2.tgz` | 完整插件包 |
| `SHA256SUMS` | 插件包与来源记录的 SHA-256 |
| `plugin-2.7.2.json` | 固定源码提交、清单摘要、测试及公开升级验证记录 |

```text
a167f743e8e05217f7b11e8f807fffeeb22e77e020a8318d4b5ff1d331f692a1  dsh-our-free-
```
</details>

---
### 📦 [hypit-ai/hypit](https://github.com/hypit-ai/hypit)
`⭐ Stars: 25,679` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.3.1](https://github.com/hypit-ai/hypit/releases/tag/v0.3.1) (2026-10-09)`

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
`⭐ Stars: 19,413` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.0.7](https://github.com/HBAI-Ltd/Toonflow-app/releases/tag/v2.0.7) (2026-10-20)`

> **简介**：短剧、漫剧制作工具 Toonflow：开源 AI 视频创作平台，集成剧本创作、智能分镜、角色与场景资产管理、图像生成和视频生成。融合无限画布、AI Agent 与可视化工作流，支持本地部署、自选模型、跨平台客户端、MCP 与插件扩展。Open-source AI short drama and motion comic creation tool with an infinite canvas, AI agents, storyboarding, image and video generation. Self-hosted and extensible, with a canvas-based approach similar to LibTV and TapNow.

**💡 核心亮点更新 (中文)**：
* fix: 修复 macOS 实体 Ctrl + 滚轮缩放步长暴增异常 by  in https://github.com/HBAI-Ltd/Toonflow-app/pull/323
* 修复 Linux 下画布中键点击意外触发系统剪贴板粘贴文本问题 by  in https://github.com/HBAI-Ltd/Toonflow-app/pull/322
* 阻止鼠标侧键在工作区误触发后退 by  in https://github.com/HBAI-Ltd/Toonflow-app/pull/339

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 📦 下载指南

选择你的设备对应的安装包，点击即可下载：

| 你的设备 | 下载 |
| --- | --- |
| 💻 Windows（64 位） | [⬇️ 下载 Windows 安装包](https://github.com/HBAI-Ltd/Toonflow-app/releases/download/v2.0.7/toonflow-2.0.7-Setup.exe) |
| 🍎 Mac（M 系列芯片） | [⬇️ 下载 M 系列 Mac 安装包](https://github.com/HBAI-Ltd/Toonflow-app/releases/download/v2.0.7/macos-arm64-toonflow.dmg) |
| 🍎 Mac（Intel 芯片） | [⬇️ 下载 Intel Mac 安装包](https://github.com/HBAI-Ltd/Toonflow-app/releases/download/v2.0.7/stable-macos-x64-toonflow.dmg) |
| 📱 Android（ARM64，Android 8 及以上） | [⬇️ 下载 Android APK](https://github.com/HBAI-Ltd/Toonflow-app/releases/download/v2.0.7/toonflow-2.0.7-android-arm64.apk) |

> 💡 手动安装请选择上表中的链接。下方其他文件供软件自动更新使用。

## 🚀 安装说明

- 💻 **Windows**：双击下载的安装包，按提示完成安装。
- 🍎 **Mac**：打开下载的安装包，将 `toonflow.app` 拖入“应用程序”，再从“应用程序”打开。
- 📱 **Android**：在手机上打开 APK，按系统提示允许此来源安装应用。后续版本可直接覆盖安装。

M 系列 Mac 安装包已完成 Developer ID 签名与 Apple 公证。首次打开时，macOS 仍可能提示确认打开从互联网下载的应用。

---


## What's Changed
* fix: 修复 macOS 实体 Ctrl + 滚轮缩放步长暴增异常 by @futureManOne in https://github.com/HBAI-Ltd/Toonflow-app/pull/323
* 修复 Linux 下画布中键点击意外触发系统剪贴板粘贴文本问题 by @miaobuao in https://github.com/HBAI-Ltd/Toonflow-app/pull/322
* 阻止鼠标侧键在工作区误触发后退 by @Clearlove275 in https://github.com/HBAI-Ltd/Toonflow-app/pull/339
* fix: 使用 WebView2 官方 API 比较带通道后缀的版本 by @wwmogu in https://github.com/HBAI-Ltd/Toonflow-app/pull/331

## New Contributors
* @futureManOne made their first contribution in https://github.com/HBAI-Ltd/Toonflow-app/pull/323
* @miaobuao made their first contribution in https://github.co
```
</details>

---
### 📦 [morluto/rea](https://github.com/morluto/rea)
`⭐ Stars: 386,047` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [rea-agents-6.8.0](https://github.com/morluto/rea/releases/tag/rea-agents-6.8.0) (2026-10-25)`

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
`⭐ Stars: 16,605` &nbsp;|&nbsp; `💻 语言: Vue` &nbsp;|&nbsp; `🏷️ 最新版本: [v4.0.9](https://github.com/chatfire-AI/huobao-drama/releases/tag/v4.0.9) (2026-10-25)`

> **简介**：🎬 火宝短剧 - 基于AI的一站式短剧生成平台 《一句话生成完整短剧，从剧本到成片全自动化》  Huobao Drama - An AI-Powered End-to-End Short Drama Generator "One Sentence to Complete Drama: Fully Automated from Script to Final Video"

**💡 核心亮点更新 (中文)**：
- 改进视频任务恢复：保留上游任务与结果，支持重新下载、续查和中断恢复，减少重复生成。
- 修复默认聊天模型选择时的配置传递。
- 改进桌面启动体验：显示启动页面，增加健康检查超时处理和脱敏诊断日志。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
v4.0.9

- 改进视频任务恢复：保留上游任务与结果，支持重新下载、续查和中断恢复，减少重复生成。
- 修复默认聊天模型选择时的配置传递。
- 改进桌面启动体验：显示启动页面，增加健康检查超时处理和脱敏诊断日志。
- 修复 Intel Mac 安装包中的 FFmpeg 与图片处理依赖；Apple Silicon 使用对应架构的 FFmpeg/FFprobe。
- 更新项目文档、FireMux 入口和微信群活码。

安装包：macOS Apple Silicon、macOS Intel、Windows x64。

Docker 镜像：`huobao/huobao-drama:4.0.9`，`latest` 同步更新；支持 `linux/amd64` 和 `linux/arm64`。
```
</details>

---
### 📦 [yetone/magpie](https://github.com/yetone/magpie)
`⭐ Stars: 21,709` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.1.1564](https://github.com/yetone/magpie/releases/tag/v0.1.1564) (2026-10-26)`

> **简介**：Every agent's model. One place. Codex on DeepSeek, Claude Code on Kimi, from the menu bar.

**💡 核心亮点更新 (中文)**：
- **Awake:** Turning off the setting now takes effect immediately instead of being checked every 5 seconds.
- **Filememo:** Changes made by other processes to Magpie's files are now detected immediately instead of being checked every 5 seconds.
- **macOS (Apple Silicon):** `magpie-darwin-arm64.dmg`

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Improvements

- **Awake:** Turning off the setting now takes effect immediately instead of being checked every 5 seconds.
- **Filememo:** Changes made by other processes to Magpie's files are now detected immediately instead of being checked every 5 seconds.

### Install

Download from [usemagpie.ai](https://usemagpie.ai), or `curl -fsSL https://usemagpie.ai/install.sh | sh`. An installed magpie updates itself.

- **macOS (Apple Silicon):** `magpie-darwin-arm64.dmg`
- **macOS (Intel):** `magpie-darwin-amd64.dmg`
- **Windows:** `magpie-windows-amd64.exe` (ARM: `magpie-windows-arm64.exe`)
- **Linux:** `magpie-linux-amd64` / `magpie-linux-arm64` (needs GTK 3 and WebKitGTK 4.1)
- **Terminal only:** `magpie-cli-<os>-<arch>`

<!-- lang:zh -->

## Improvements

- **Awake:** 关闭该设置现在会立即生效，而不是每 5 秒检查一次。
- **Filememo:** 其他进程对 Magpie 文件所做的更改现在会被立即检测到，而不是每 5 秒检查一次。

### 安装

从 [usemagpie.ai](https://usemagpie.ai) 下载，或运行 `curl -fsSL https://usemagpie.ai/install.sh | sh`。已安装的 magpie 会自动更新。



---
The same release, and the feed magpie updates from: https://github.com/yetone/magpie-releases/releases/tag/v0.1.1564
```
</details>

---
### 📦 [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
`⭐ Stars: 257,117` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.22.5](https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.5) (2026-10-23)`

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
`⭐ Stars: 1,075` &nbsp;|&nbsp; `💻 语言: Other` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.8.8](https://github.com/Makememo/MemoAI/releases/tag/v1.8.8) (2026-10-09)`

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
`⭐ Stars: 10,857` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.12.29](https://github.com/genspark-ai/genoffice/releases/tag/v0.12.29) (2026-10-22)`

> **简介**：Free, open-source AI Office suite: Docs, Sheets, Slides, PDF, Markdown and HTML editors with a built-in AI agent, plus a `genoffice` CLI and agent skill so Claude Code, Codex and Cursor can create and edit real .docx/.xlsx/.pptx files locally. Bring your own key. macOS, Windows & Linux.

**💡 核心亮点更新 (中文)**：
- **Docs:** page breaks land where Word puts them across a 50-document production sample (headings stay with their table, rows split at legal cuts, contextual spacing crosses table boundaries, TOC entries and numbered indents follow the style chain, Aptos/Malgun/Calibri-substitute/Nirmala UI metrics, Korean autospace); DOCX→PDF export no longer drops content (reported by  and body text no longer overlaps a header picture (reported by ; edit header/footer table cells in place, insert a picture from the Header & Footer tab and resize inline pictures in headers, footers and cells; the table corner handle scales row heights too; custom (w14) list formats survive reuse and re-save (reported by ; read and write document properties and a pasted field keeps its instruction ; saved Zotero citations stay editable in Word and WPS  and Mendeley fields fold like Zotero's.
- **Sheets:** VLOOKUP over a table or defined name no longer goes blank after a save (reported by , same for DOLLAR and other locale functions; CSV export writes the real values instead of width-fitted displays; one Increase Decimal click no longer jumps to 10 places; Convert to Number survives the save; the status bar shows Sum/Average again; keyboard focus returns to the grid after a ribbon command; the View tab shows every display toggle ; a password-protected workbook is reported as such ; XML spreadsheets under a legacy name open ; a picture in a note survives the next save ; opening a large workbook uses a fraction of the memory.
- **Slides:** chart data labels, data tables, secondary-axis formats, CJK category wrapping and legend placement match PowerPoint; a chart carries its workbook so PowerPoint's Edit Data works ; real 3D models, stored as PowerPoint stores them ; table-style fonts and "X Variable" font names resolve correctly; opening a deck no longer parses every system font, cutting memory on open.

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
GenOffice v0.12.29 stable desktop installers.

## What's New

- **Docs:** page breaks land where Word puts them across a 50-document production sample (headings stay with their table, rows split at legal cuts, contextual spacing crosses table boundaries, TOC entries and numbered indents follow the style chain, Aptos/Malgun/Calibri-substitute/Nirmala UI metrics, Korean autospace); DOCX→PDF export no longer drops content (reported by @jeff-jiang-pointures) and body text no longer overlaps a header picture (reported by @x86law-dev); edit header/footer table cells in place, insert a picture from the Header & Footer tab and resize inline pictures in headers, footers and cells; the table corner handle scales row heights too; custom (w14) list formats survive reuse and re-save (reported by @lkopenec); read and write document properties and a pasted field keeps its instruction (@tokg-venv); saved Zotero citations stay editable in Word and WPS (@tokg-venv) and Mendeley fields fold like Zotero's.
- **Sheets:** VLOOKUP over a table or defined name no longer goes blank after a save (reported by @putude), same for DOLLAR and other locale functions; CSV export writes the real values instead of width-fitted displays; one Increase Decimal click no longer jumps to 10 places; Convert to Number survives the save; the status bar shows Sum/Average again; keyboard focus returns to the grid after a ribbon command; the View tab shows every display toggle (@tokg-venv); a password-protected workbook i
```
</details>

---
### 📦 [ruvnet/RuView](https://github.com/ruvnet/RuView)
`⭐ Stars: 99,625` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [ruview-harness-v0.9.2](https://github.com/ruvnet/RuView/releases/tag/ruview-harness-v0.9.2) (2026-10-12)`

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
`⭐ Stars: 25,112` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [@pascal-app/cli@1.0.6](https://github.com/pascalorg/editor/releases/tag/%40pascal-app/cli%401.0.6) (2026-10-23)`

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
`⭐ Stars: 30,471` &nbsp;|&nbsp; `💻 语言: Kotlin` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.0.4](https://github.com/librepods-org/librepods/releases/tag/v1.0.4) (2026-10-16)`

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
`⭐ Stars: 39,242` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.12.0](https://github.com/linshenkx/prompt-optimizer/releases/tag/v2.12.0) (2026-10-25)`

> **简介**：An AI prompt optimizer for writing better prompts and getting better AI results.

**💡 核心亮点更新 (中文)**：
- View original and optimized prompts in one region. Configuration and toolbars adapt to available space, reducing nested tab switching and leaving more room for content.
- Inspect the prompt source while testing and compare results together, with improved long-text reading, image previews and keyboard-aware controls.
- Reuse existing business components and data services. Wide desktop layouts retain their established split views and interaction patterns.

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## English

### Summary
- This stable release brings the mobile and PWA workflows introduced in beta.1, together with follow-up fixes verified on Android.
- Add mobile layouts across seven workspaces, organized around Optimize and Test, with prompt context and side-by-side results.
- Adapt model, history, template, variable, favorite and data management to phone-sized lists, details and forms.
- Add an installable production Web PWA with offline access to saved local work and save-before-update controls, backed by stronger workspace recovery and cross-window write protection.

### Highlights
- View original and optimized prompts in one region. Configuration and toolbars adapt to available space, reducing nested tab switching and leaving more room for content.
- Inspect the prompt source while testing and compare results together, with improved long-text reading, image previews and keyboard-aware controls.
- Reuse existing business components and data services. Wide desktop layouts retain their established split views and interaction patterns.

### Product Updates
#### Web
- Cover Basic System, Basic User, Context Multi-message, Context Variables, Text-to-image, Image-to-image and Multi-image workspaces.
- Reorganize mobile navigation and mode selection so specific modes are visible together and navigation happens after a concrete selection. Management views support list, detail, edit and return flows.
- Improve phone workflows for model forms, history restoration, template ed
```
</details>

---
### 📦 [RSSNext/Folo](https://github.com/RSSNext/Folo)
`⭐ Stars: 39,171` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [desktop/v1.16.0](https://github.com/RSSNext/Folo/releases/tag/desktop/v1.16.0) (2026-10-16)`

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
`⭐ Stars: 51,367` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [0.31.2](https://github.com/roboflow/supervision/releases/tag/0.31.2) (2026-10-24)`

> **简介**：We write your reusable computer vision tools. 💜

**💡 核心亮点更新 (中文)**：
- **Pascal VOC** export and import use the devkit's box indices, so Detectron2 and other readers see the boxes you wrote.
- Gemini 2.5 and 3.5 masks survive boxes that leave the 0-1000 range instead of failing the whole response.
- Crop and icon annotators draw on grayscale scenes.

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# v0.31.2 — Pascal VOC boxes that match the devkit

A bug-fix release: Pascal VOC boxes now follow the devkit convention, and a batch of crashes on edge-case inputs is gone.

- **Pascal VOC** export and import use the devkit's box indices, so Detectron2 and other readers see the boxes you wrote.
- Gemini 2.5 and 3.5 masks survive boxes that leave the 0-1000 range instead of failing the whole response.
- Crop and icon annotators draw on grayscale scenes.
- Half-precision box centers stay finite instead of turning into `inf`.
- JSON sinks, dataset exports and the video reader stop losing data when something goes wrong.

Drop-in upgrade, with one catch: box-only Pascal VOC objects written by earlier versions now load one pixel larger on the right and bottom edges. The migration guide below shows how to fix them.

## ✨ Spotlights / highlights

### Pascal VOC boxes follow the devkit

`DetectionDataset.as_pascal_voc` and `from_pascal_voc` now treat `<bndbox>` indices as 1-based and inclusive, shifting only `xmin` and `ymin` by one, which is what Detectron2 and other devkit readers expect. Export also rounds corners to the nearest pixel instead of truncating them, so a YOLO box that `from_yolo` loads with float noise no longer grows a pixel. Box-only objects written by 0.31.1 and earlier carry an extra +1 in `xmax` and `ymax`; objects exported from masks already used the devkit maxima. (#2748, #2780)

```python
# `dataset` holds one box [10, 20, 40, 60]
dataset.a
```
</details>

---
### 📦 [MetaCubeX/mihomo](https://github.com/MetaCubeX/mihomo)
`⭐ Stars: 35,194` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.19.33](https://github.com/MetaCubeX/mihomo/releases/tag/v1.19.33) (2026-10-21)`

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
`⭐ Stars: 36,447` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.3.0](https://github.com/microsoft/graphrag/releases/tag/v3.3.0) (2026-10-08)`

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
`⭐ Stars: 153,895` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.5.8](https://github.com/clash-verge-rev/clash-verge-rev/releases/tag/v2.5.8) (2026-10-09)`

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
`⭐ Stars: 78,569` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.1.910-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.910-beta) (2026-10-23)`

> **简介**：Local UI to run and train LLMs and diffusion models. Supports GGUF, MLX, Qwen3.8, DeepSeek-V4.1, MiniMax-H3, Gemma 4, FLUX and more.

**💡 核心亮点更新 (中文)**：
- **Bigger MoE models on Mac**: MLX MoE models too big for memory keep experts on SSD, so Qwen3.8-Flash-Next runs on a 32 GB Mac.
- **Chat-only install**: a much smaller Unsloth Desktop for GGUF chat; add training later in Settings.
- **Flint**: Recursive's 40B coding-agent MoE, runs in 24 GB at 3-bit [Guide](https://unsloth.ai/docs/models/flint)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Recursive's Flint, MOSS-Image and NVIDIA's Nemotron Bolt 4B are here! Run them locally in Unsloth. Also new: a chat-only Unsloth Desktop install, MLX MoE models bigger than your Mac's memory and an OpenAI-compatible fine-tuning API.

## Highlights

- **Bigger MoE models on Mac**: MLX MoE models too big for memory keep experts on SSD, so Qwen3.8-Flash-Next runs on a 32 GB Mac.
- **Chat-only install**: a much smaller Unsloth Desktop for GGUF chat; add training later in Settings.
- **Flint**: Recursive's 40B coding-agent MoE, runs in 24 GB at 3-bit [Guide](https://unsloth.ai/docs/models/flint)
- **MOSS-Image**: 5.1B image model designed for top-tier generation [GGUF](https://huggingface.co/unsloth/MOSS-Image-SFT-GGUF) + [FP8](https://huggingface.co/unsloth/MOSS-Image-SFT-FP8)
- **NVIDIA Nemotron 3.5 Bolt E4B**: NVIDIA's new Gemma 4 E4B fine-tune, 63.2 on Tau2-Bench vs the original's 38.7 [Guide](https://unsloth.ai/docs/models/nemotron-3.5-bolt)
- **MoE expert pruning**: Export a smaller MoE model by removing 25% or 50% of its least useful experts with REAP.
- **UI overhaul**: New + more consistent UI across Unsloth (API, roundness etc)

## Images + video

- Generate images containing English or Chinese text with OpenMOSS's 5.1B MOSS-Image, SFT or Base. [GGUF](https://huggingface.co/unsloth/MOSS-Image-SFT-GGUF) · [Base GGUF](https://huggingface.co/unsloth/MOSS-Image-Base-GGUF)
- MOSS-Image, the new image model, runs on 16 GB GPUs; its GGUFs also run on Macs and com
```
</details>

---
### 📦 [arc53/DocsGPT](https://github.com/arc53/DocsGPT)
`⭐ Stars: 18,334` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [1.1.0](https://github.com/arc53/DocsGPT/releases/tag/1.1.0) (2026-10-25)`

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
`⭐ Stars: 83,493` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.2.20](https://github.com/lobehub/lobehub/releases/tag/v2.2.20) (2026-10-18)`

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
`⭐ Stars: 6,800` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.26.8](https://github.com/Dooy/chatgpt-web-midjourney-proxy/releases/tag/v2.26.8) (2026-09-29)`

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
`⭐ Stars: 29,912` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v4.17.2](https://github.com/labring/FastGPT/releases/tag/v4.17.2) (2026-10-09)`

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
`⭐ Stars: 9,905` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.3.1](https://github.com/yihong0618/bilingual_book_maker/releases/tag/v1.3.1) (2026-09-30)`

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
`⭐ Stars: 37,268` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.4.1](https://github.com/1Panel-dev/1Panel/releases/tag/v2.4.1) (2026-10-22)`

> **简介**：🔥 1Panel is a modern, open-source Linux server management panel and a lightweight AI management platform.

**💡 核心亮点更新 (中文)**：
* System: Upgraded Go to 1.27.3 to fix the crypto/x509 security vulnerability ([CVE-2026-111943](https://www.cve.org/CVERecord?id=CVE-2026-111943))
* 【系统】升级 Go 至 1.27.3，修复 crypto/x509 安全漏洞（[CVE-2026-111943](https://www.cve.org/CVERecord?id=CVE-2026-111943)）

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
[English](#en-v2.4.1) | [中文](#cn-v2.4.1)

<h3 id="en-v2.4.1">Bug Fixes</h3>

* System: Upgraded Go to 1.27.3 to fix the crypto/x509 security vulnerability ([CVE-2026-111943](https://www.cve.org/CVERecord?id=CVE-2026-111943))

<h3 id="cn-v2.4.1">问题修复</h3>

* 【系统】升级 Go 至 1.27.3，修复 crypto/x509 安全漏洞（[CVE-2026-111943](https://www.cve.org/CVERecord?id=CVE-2026-111943)）
```
</details>

---
### 📦 [invoke-ai/InvokeAI](https://github.com/invoke-ai/InvokeAI)
`⭐ Stars: 28,865` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v6.14.2](https://github.com/invoke-ai/InvokeAI/releases/tag/v6.14.2) (2026-09-27)`

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
### 📦 [langgenius/dify](https://github.com/langgenius/dify)
`⭐ Stars: 159,548` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [1.18.0](https://github.com/langgenius/dify/releases/tag/1.18.0) (2026-10-23)`

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
`⭐ Stars: 25,013` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.6.45](https://github.com/nextai-translator/nextai-translator/releases/tag/v0.6.45) (2026-10-24)`

> **简介**：基于 ChatGPT API 的划词翻译浏览器插件和跨平台桌面端应用    -    Browser extension and cross-platform desktop application for translation based on ChatGPT API.

**💡 核心亮点更新 (中文)**：
- Shortened time to first character: the HTTP client is now reused between translations instead of paying a fresh DNS + TCP + TLS handshake each time, the first streamed token is painted immediately instead of waiting out the 120ms batching window, and settings are cached instead of re-read from disk on every request
- Fixed streamed translations that could start mid-sentence because the first chunks arrived before the desktop app had registered its listeners
- Fixed multi-byte characters turning into replacement characters when a network chunk split them, which affected most Chinese, Japanese and Korean translations

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Shorter wait for the first character, and no more garbled Chinese

- Shortened time to first character: the HTTP client is now reused between translations instead of paying a fresh DNS + TCP + TLS handshake each time, the first streamed token is painted immediately instead of waiting out the 120ms batching window, and settings are cached instead of re-read from disk on every request
- Fixed streamed translations that could start mid-sentence because the first chunks arrived before the desktop app had registered its listeners
- Fixed multi-byte characters turning into replacement characters when a network chunk split them, which affected most Chinese, Japanese and Korean translations
- Fixed the desktop abort listener leaking when a request failed, and a few panics on malformed request options
- Added time-to-first-token tracing: each translation reports where its time went - prompt, settings, network setup, provider thinking, first paint - in the devtools console, in the app's stdout, and through window.__translatePerf
```
</details>

---
### 📦 [langchain-ai/langchain](https://github.com/langchain-ai/langchain)
`⭐ Stars: 148,469` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [langchain-core==1.7.0](https://github.com/langchain-ai/langchain/releases/tag/langchain-core%3D%3D1.7.0) (2026-10-22)`

> **简介**：The agent engineering platform.

**💡 核心亮点更新 (中文)**：
- Tool-call args now stream as `tool-call-delta` slices instead of `block-delta` snapshots of the args so far. If you read raw stream events and their `block-delta` args mid-stream, read `tool-call-delta` instead. `.tool_calls.get()` and `.output` are unchanged. To keep snapshots, pin `langchain-core<1.7`.
- Since 1.6.13, iterating `ChatModelStream.tool_calls` yields each call's new args slice, not a snapshot of the args so far.

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Changes since langchain-core==1.6.13

release(core): 1.7.0 (#41418)
feat(core): emit `tool-call-delta` for streamed tool-call args (#41257)

## Notes

- Tool-call args now stream as `tool-call-delta` slices instead of `block-delta` snapshots of the args so far. If you read raw stream events and their `block-delta` args mid-stream, read `tool-call-delta` instead. `.tool_calls.get()` and `.output` are unchanged. To keep snapshots, pin `langchain-core<1.7`.
- Since 1.6.13, iterating `ChatModelStream.tool_calls` yields each call's new args slice, not a snapshot of the args so far.
```
</details>

---
### 📦 [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)
`⭐ Stars: 187,751` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [autogpt-platform-beta-v0.9.0](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.9.0) (2026-10-23)`

> **简介**：AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.

**💡 核心亮点更新 (中文)**：
- **#15824** - Add measures and admin tools against multi-account abuse (by
- **#14553** - Self-host from the Docker Hub image, with a Windows installer (by
- **#14981** - Every block declares its effect; Auto judges cheap outward actions and asks first on costly ones (by

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 🔥 What's New?

### New Features

- **#15824** - Add measures and admin tools against multi-account abuse (by @Pwuts)
- **#14553** - Self-host from the Docker Hub image, with a Windows installer (by @ntindle)
- **#14981** - Every block declares its effect; Auto judges cheap outward actions and asks first on costly ones (by @Pwuts)
- **#15675** - Add admin users page to look up, ban and impersonate a user, with rate limits folded in (by @Pwuts)
- **#15859** - Send the browser tools' traffic through an egress proxy (by @ntindle)
- **#15215** - Redesign usage limits and review upgrade charges (by @Torantulino)
- **#15388** - AutoPilot turns pause at their limits instead of dying, and Keep going picks them up (by @ntindle)
- **#15390** - Resume or send a chat's turn when the budget resets (by @ntindle)
- **#15403** - Add send at reset, the out-of-budget panel for Max, and a running-low hint (by @ntindle)
- **#15585** - Add voice mode to the + menu; model and token usage open as dialogs (by @0ubbe)
- **#15115** - Add per-expert default approval mode for new web chats (by @Abhi1992002)
- **#14551** - Distill private account and Expert skills during dreaming (by @ntindle)
- **#14960** - Add durable per-scope schedule registry for dream and community jobs with lifecycle hooks and backfill (by @ntindle)
- **#14961** - Add durable DreamPass record written from the sync and batch dream paths (by @ntindle)
- **#14970** - Add one guard against overlapping dream passes
```
</details>

---
### 📦 [rockbenben/ChatGPT-Shortcut](https://github.com/rockbenben/ChatGPT-Shortcut)
`⭐ Stars: 8,870` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v4.5.1](https://github.com/rockbenben/ChatGPT-Shortcut/releases/tag/v4.5.1) (2026-10-09)`

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
`⭐ Stars: 2,828` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [userscript-v2.38.0](https://github.com/pionxzh/chatgpt-exporter/releases/tag/userscript-v2.38.0) (2026-10-17)`

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
`⭐ Stars: 47,589` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [2.2.1](https://github.com/zhayujie/CowAgent/releases/tag/2.2.1) (2026-10-14)`

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
`⭐ Stars: 2,534` &nbsp;|&nbsp; `💻 语言: Shell` &nbsp;|&nbsp; `🏷️ 最新版本: [20261024](https://github.com/lxhao61/integrated-examples/releases/tag/20261024) (2026-10-24)`

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
`⭐ Stars: 22,171` &nbsp;|&nbsp; `💻 语言: Shell` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.5.28](https://github.com/mack-a/v2ray-agent/releases/tag/v3.5.28) (2026-10-25)`

> **简介**：Xray、Tuic、hysteria2、sing-box 八合一一键脚本

**💡 核心亮点更新 (中文)**：
fix(脚本): 修复 Xray 多用户删除失败问题

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
fix(脚本): 修复 Xray 多用户删除失败问题
```
</details>

---
### 📦 [electerm/electerm](https://github.com/electerm/electerm)
`⭐ Stars: 15,460` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v5.7.15](https://github.com/electerm/electerm/releases/tag/v5.7.15) (2026-10-26)`

> **简介**：📻Free and open-sourced terminal/ssh/sftp/ftp/telnet/serialport/RDP/VNC/Spice client(Linux, Mac, Windows, Android, HarmonyOS, iOS)

**💡 核心亮点更新 (中文)**：
- SFTP: type any key in the file list to filter it, always on, replacing the old filter icon (#4648) by

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
### New features/UI/Updates

- SFTP: type any key in the file list to filter it, always on, replacing the old filter icon (#4648) by @rebelancap

### Bug fixes

- Fix SSH login for bookmarks without a password (regression from 5.7.5) (#4647)
- Fix socks/http proxy connection when the proxy address is IPv6 (#4643) by @Pharex38
- Don't let session keepalive submit a half-typed command (#4641) by @Pharex38
- Fix version compare when versions have a different number of parts (#4642) by @Pharex38

-----

### 新功能/界面/更新

- SFTP：在文件列表中直接输入关键字即可过滤，默认开启，替换了原来的过滤图标 (#4648)（由 @rebelancap 提供）

### 问题修复

- 修复无密码书签的 SSH 登录问题（5.7.5 引入的回归）(#4647)
- 修复代理地址为 IPv6 时的 socks/http 代理连接问题 (#4643)（由 @Pharex38 提供）
- 会话保活不再提交输入到一半的命令 (#4641)（由 @Pharex38 提供）
- 修复版本号段数不同时的版本比较问题 (#4642)（由 @Pharex38 提供）

-------
Download下载: [https://electerm.org](https://electerm.org)
```
</details>

---
### 📦 [XX-net/XX-Net](https://github.com/XX-net/XX-Net)
`⭐ Stars: 33,454` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [5.16.7](https://github.com/XX-net/XX-Net/releases/tag/5.16.7) (2026-09-28)`

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
`⭐ Stars: 34,782` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [1.1.4](https://github.com/FreeCAD/FreeCAD/releases/tag/1.1.4) (2026-09-28)`

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
### 📦 [XTLS/Xray-core](https://github.com/XTLS/Xray-core)
`⭐ Stars: 42,326` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v26.10.21](https://github.com/XTLS/Xray-core/releases/tag/v26.10.21) (2026-10-21)`

> **简介**：Xray, Penetrates Everything. Also the best v2ray-core. Where the magic happens. An open platform for various uses.

**💡 核心亮点更新 (中文)**：
- **TRX(Tron)/USDT/USDC: `TNrDh5VSfwd4RPrwsohr6poyNTfFefNYan`**
- **TON: `UQApeV-u2gm43aC1uP76xAC1m6vCylstaN1gpfBmre_5IyTH`**
- **BTC: `1JpqcziZZuqv3QQJhZGNGBVdCBrGgkL6cT`**

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
紧急安全更新：[由于前几天印度八张中间证书的私钥因过于简单而被破解](https://github.com/XTLS/Xray-core/pull/7212#issuecomment-6310150214)，本版本内置的 RootCAs 依赖库移除了三张根证书（v26.10.10、v26.10.17 内置有这些证书，已被撤版），并使用 Go 1.27.3 编译以确保即使操作系统 CA 库未更新也会过滤掉问题证书，用户应尽快升级到该版本，月底发 stable release（操作系统的 CA 库可能更新较慢，所以要覆盖掉上一个 latest）

> https://t.me/projectXtls/3592 10.22 直接先把该版本设为了 latest，~似乎也不是不行~，完整的 release notes 等月底或下个月初的版本吧，半年积攒的更新写起来有点酸爽，~其实我几乎不用 AI，或许让 AI 来补，顺便 v26.9.8 多余了也被删了~

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
```
</details>

---
### 📦 [klzgrad/naiveproxy](https://github.com/klzgrad/naiveproxy)
`⭐ Stars: 9,562` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [v154.0.8037.49-5](https://github.com/klzgrad/naiveproxy/releases/tag/v154.0.8037.49-5) (2026-10-22)`

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
`⭐ Stars: 3,072` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.1.1](https://github.com/JustAResearcher/gpu-unlock-ada/releases/tag/v1.1.1) (2026-10-24)`

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
`⭐ Stars: 165` &nbsp;|&nbsp; `💻 语言: Shell` &nbsp;|&nbsp; `🏷️ 最新版本: [2026.10.25-18/27_arm_cortex-a15_neon-vfpv4](https://github.com/kenzok8/compile-package/releases/tag/2026.10.25-18/27_arm_cortex-a15_neon-vfpv4) (2026-10-25)`

> **简介**：small-package仓库，每日更新插件编译

**💡 核心亮点更新 (中文)**：
定时更新插件，推送发布 💤:

[下载链接] (https://dllkids.xyz/packages/arm_cortex-a15_neon-vfpv4/)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
定时更新插件，推送发布 💤:

[下载链接] (https://dllkids.xyz/packages/arm_cortex-a15_neon-vfpv4/)
```
</details>

---
### 📦 [jxxghp/MoviePilot](https://github.com/jxxghp/MoviePilot)
`⭐ Stars: 11,953` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.1.9](https://github.com/jxxghp/MoviePilot/releases/tag/v3.1.9) (2026-10-22)`

> **简介**：NAS媒体库自动化管理工具

**💡 核心亮点更新 (中文)**：
- 新增本地引用链接（reflink）整理方式，支持复制优先尝试写时复制及自动回退，在支持的文件系统上减少复制耗时和空间占用。
- 订阅新增首次下载与洗版来源记录，修复全集洗版规则、整季资源选择及重复资源退避，减少重复下载和通知。
- 刮削新增季图片写入剧集根目录、图片兼容别名和 Fanart 4K 背景图开关；规范图片格式并复用下载，减少重复请求。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 本次更新内容

- 新增本地引用链接（reflink）整理方式，支持复制优先尝试写时复制及自动回退，在支持的文件系统上减少复制耗时和空间占用。
- 订阅新增首次下载与洗版来源记录，修复全集洗版规则、整季资源选择及重复资源退避，减少重复下载和通知。
- 刮削新增季图片写入剧集根目录、图片兼容别名和 Fanart 4K 背景图开关；规范图片格式并复用下载，减少重复请求。
- 完善 115 云盘覆盖、同名文件处理和历史回执恢复，补齐源文件清理的人工复核操作，恢复整理失败后的 AI 接管。
- 修复音乐多碟专辑及发行规格识别，避免音轨混淆和已整理歌曲重复提交；改善 Emby 媒体年份读取。
- 优化 Agent 交互任务与后台服务隔离、流式反馈及 Telegram 最终消息更新，完善飞书资源选择卡片信息。
- 支持从部署 secrets 文件读取敏感配置并避免回写配置文件；新增 Cheaper Inference 提供商，改进 ChatGPT OAuth 刷新和默认模型配置。
- 修复站点连通性检测、分类透传、用户等级与分享率显示，完善站点统计、插件版本历史操作及豆瓣评论布局。
- 修复 DoH 对 CNAME 应答的处理，解析器全部失败后自动冷却并回退系统 DNS，减少重复超时和告警。
- 升级前后端安全依赖与 moviepilot-rust 0.3.10，完善容器系统包更新及镜像基线校验，修复 TMDB 请求超时和跨设备符号链接移动问题。

## 完整变更记录

- fix(setup): 更新 Anthropic 默认模型为 claude-sonnet-4-6 by @pcbeingused333 ([a8f260b](https://github.com/jxxghp/MoviePilot/commit/a8f260b01d6b0e2b10e13a09ad841a275c0e0aa4))
- fix(telegram): omit buttons without valid actions (#7074) by @jxxghp ([9e02d26](https://github.com/jxxghp/MoviePilot/commit/9e02d26292180dac8f6b74d2640106d47be9610e))
- feat(subscribe): record initial and upgrade download provenance (#7061) by @jxxghp ([379c26a](https://github.com/jxxghp/MoviePilot/commit/379c26a300df98ba742bf83966e74fc06bce9145))
- feat(storage): 本地存储增加引用链接(reflink)整理方式 (#7077) by @AkimioJR ([114c2ce](https://github.com/jxxghp/MoviePilot/commit/114c2cebe59d8e4c4a2d8ed7cc50e4f92ba1775b))
- fix(storage): 修复 reflink 同存储回退语义与测试稳定性 (#7081) by @jxxghp ([6e5c9d0](https://github.com/jxxghp/MoviePilot/commit/6e5c9d0afb21349ee71bb006fc79051ee54c61ff))
- fix(download): 复用
```
</details>

---
### 📦 [sandboxie-plus/Sandboxie](https://github.com/sandboxie-plus/Sandboxie)
`⭐ Stars: 19,794` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.18.8](https://github.com/sandboxie-plus/Sandboxie/releases/tag/v1.18.8) (2026-10-17)`

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
`⭐ Stars: 4,894` &nbsp;|&nbsp; `💻 语言: C#` &nbsp;|&nbsp; `🏷️ 最新版本: [10.0.10](https://github.com/HMBSbige/NatTypeTester/releases/tag/10.0.10) (2026-10-08)`

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
`⭐ Stars: 12,454` &nbsp;|&nbsp; `💻 语言: C#` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.1.0](https://github.com/KnifeLemon/Filee/releases/tag/v2.1.0) (2026-10-24)`

> **简介**：Free, open-source file converter. Convert 263 formats offline by drag & drop — images, PDF, Word, Excel, PowerPoint, HWP/HWPX, video, audio, e-books and archives. No upload, no Office needed.

**💡 核心亮点更新 (中文)**：
What's Changed

<!-- update
level: recommended
ko: Windows용 파일에 코드 서명이 들어가서 스마트 앱 컨트롤이나 백신이 Filee를 막는 일이 줄어요
ko: 스캔본과 그림의 글자를 인식(OCR)해서 검색되는 PDF와 편집할 수 있는 문서로 만들어요
ko: 사진·동영상·오디오를 압축하고 합치고 정보를 지울 수 있고, 동영상에서 클립을 잘라 낼 수 있어요
ko: PDF 페이지를 편집하고, 어떤 PDF에든

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## What's Changed

<!-- update
level: recommended
ko: Windows용 파일에 코드 서명이 들어가서 스마트 앱 컨트롤이나 백신이 Filee를 막는 일이 줄어요
ko: 스캔본과 그림의 글자를 인식(OCR)해서 검색되는 PDF와 편집할 수 있는 문서로 만들어요
ko: 사진·동영상·오디오를 압축하고 합치고 정보를 지울 수 있고, 동영상에서 클립을 잘라 낼 수 있어요
ko: PDF 페이지를 편집하고, 어떤 PDF에든 워터마크·쪽 번호·암호를 넣을 수 있어요
ko: PDF의 표가 엑셀 시트가 되고, 큰 엑셀 파일을 훨씬 빨리 PDF로 바꿔요
ko: PDF로 저장하기 전에 스프레드시트 페이지를 배치하고, 저장할 AutoCAD 버전을 고를 수 있어요
ko: 원본 바꾸기를 켜면 결과가 원본 자리에 들어가고 원본은 휴지통으로 가요
ko: FITS 천체 사진, iCalendar, HAR, USM 게임 동영상, 자수·플로터 파일을 지원하고 CAD 레이아웃마다 PDF 한 쪽을 만들어요
ko: 프랑스어, 번체 중국어, 네팔어, 태국어, 튀르키예어, 유럽 포르투갈어와 Material You 테마, 창 크기 조절을 지원해요
ko: Linux에서는 Filee 안에서 업데이트하고, GNOME·Hyprland Wayland에서 끌기 제스처를 쓸 수 있어요(실험 기능)
ko: 중국어 텍스트가 한글로 읽히던 문제, Word 기호가 빠지던 문제, 트레이에서 창이 두 개 뜨던 문제 등을 고쳤어요
en: Windows files are now code-signed, so Smart App Control and antivirus programs block Filee less often
en: Recognize text in scans and pictures (OCR): searchable PDFs and documents you can edit
en: Compress, merge and clean up photos, videos and audio, and cut a clip out of a video
en: Edit PDF pages, and add a watermark, page numbers or a password to any PDF
en: Tables in PDFs become Excel sheets, and large Excel files turn into PDFs much faster
en: Lay out spreadsheet pages before saving a PDF, and choose the AutoCAD version to save in
en: Replace the original: the result takes its place and the original goes to the Recycle Bin
en: FITS astrophotos, iCalendar, HAR, USM game videos, embroidery and plotter files, and a PDF page per CAD layout
en: Fre
```
</details>

---
### 📦 [guohuiyuan/go-music-dl](https://github.com/guohuiyuan/go-music-dl)
`⭐ Stars: 5,638` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.1.3](https://github.com/guohuiyuan/go-music-dl/releases/tag/v1.1.3) (2026-10-19)`

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
`⭐ Stars: 21,927` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.21.0](https://github.com/LibreSpark/LibreTV/releases/tag/v2.21.0) (2026-10-23)`

> **简介**：一分钟搭建影视站，支持Docker等部署方式

**💡 核心亮点更新 (中文)**：
获取方式

Docker（多架构 linux/amd64 / linux/arm64）

```bash
docker pull docker.io/bestzwei/libretv:2.21.0
docker pull ghcr.io/librespark/libretv:2.21.0
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
docker pull docker.io/bestzwei/libretv:2.21.0
docker pull ghcr.io/librespark/libretv:2.21.0
```

两个 registry 的镜像内容一致（同一组 digest），`latest` 也指向本版本。

### 免 Docker（下方附件，Node 18+）

```bash
sha256sum -c SHA256SUMS
tar -xzf libretv-2.21.0-standalone.tar.gz -C libretv
cd libretv && PASSWORD=your-password PORT=8080 node server.js
```

预构建包与 CPU 架构无关（x86_64 / arm64 / armv7），环境变量与 Docker 部署一致。

> 镜像由 docker-publish 工作流在同一 tag 上构建，刚发布时可能还要 5–10 分钟才可拉取。

## 变更

完整对比：https://github.com/LibreSpark/LibreTV/compare/v2.20.2...v2.21.0
```
</details>

---
### 📦 [dyang886/Game-Cheats-Manager](https://github.com/dyang886/Game-Cheats-Manager)
`⭐ Stars: 15,683` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.5.4](https://github.com/dyang886/Game-Cheats-Manager/releases/tag/v2.5.4) (2026-10-11)`

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
`⭐ Stars: 46,663` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2026.10.25-8480.1f481e4](https://github.com/DIYgod/RSSHub/releases/tag/v2026.10.25-8480.1f481e4) (2026-10-25)`

> **简介**：🧡 Everything is RSSible

**💡 核心亮点更新 (中文)**：
- ghcr.io/diygod/rsshub:1f481e461da07398cdbc3961414e397b9eb91948
- ghcr.io/diygod/rsshub:chromium-bundled-1f481e461da07398cdbc3961414e397b9eb91948
- diygod/rsshub:1f481e461da07398cdbc3961414e397b9eb91948

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Source commit: 1f481e461da07398cdbc3961414e397b9eb91948

Published multi-platform images:
- ghcr.io/diygod/rsshub:1f481e461da07398cdbc3961414e397b9eb91948
- ghcr.io/diygod/rsshub:chromium-bundled-1f481e461da07398cdbc3961414e397b9eb91948
- diygod/rsshub:1f481e461da07398cdbc3961414e397b9eb91948
- diygod/rsshub:chromium-bundled-1f481e461da07398cdbc3961414e397b9eb91948

Use these commit-specific image tags to reproduce this release. Daily Docker tags may be updated by subsequent builds.
```
</details>

---
### 📦 [amir1376/ab-download-manager](https://github.com/amir1376/ab-download-manager)
`⭐ Stars: 18,799` &nbsp;|&nbsp; `💻 语言: Kotlin` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.11.1](https://github.com/amir1376/ab-download-manager/releases/tag/v1.11.1) (2026-10-14)`

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
### 📦 [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp)
`⭐ Stars: 202,208` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [2026.10.21](https://github.com/yt-dlp/yt-dlp/releases/tag/2026.10.21) (2026-10-21)`

> **简介**：A feature-rich command-line audio/video downloader

**💡 核心亮点更新 (中文)**：
- Security: Old yt-dlp executables are vulnerable to man-in-the-middle attacks
- A man-in-the-middle/MITM attack is when your internet traffic is intercepted by an attacker that impersonates the website(s) you browse and sends you malicious data instead.
- If you think you may be targeted by such an attack, it is strongly recommended to avoid using the self-updater (e.g. the `-U`, `--update`, `--update-to` command-line options), and instead manually download and install this release's executable.

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
[![Installation](https://img.shields.io/badge/-Which%20file%20to%20download%3F-white.svg?style=for-the-badge)](https://github.com/yt-dlp/yt-dlp#installation "Installation instructions") [![Discord](https://img.shields.io/discord/807245652072857610?color=blue&labelColor=555555&label=&logo=discord&style=for-the-badge)](https://discord.gg/H5MNcFW63r "Discord") [![Donate](https://img.shields.io/badge/_-Donate-red.svg?logo=githubsponsors&labelColor=555555&style=for-the-badge)](https://github.com/yt-dlp/yt-dlp/blob/master/Maintainers.md#maintainers "Donate") [![Documentation](https://img.shields.io/badge/-Docs-brightgreen.svg?style=for-the-badge&logo=GitBook&labelColor=555555)](https://github.com/yt-dlp/yt-dlp/tree/2026.10.21#readme "Documentation") [![Nightly](https://img.shields.io/badge/Nightly%20builds-purple.svg?style=for-the-badge)](https://github.com/yt-dlp/yt-dlp-nightly-builds/releases/latest "Nightly builds") [![Master](https://img.shields.io/badge/Master%20builds-lightblue.svg?style=for-the-badge)](https://github.com/yt-dlp/yt-dlp-master-builds/releases/latest "Master builds")

#### A description of the various files is in the [README](https://github.com/yt-dlp/yt-dlp#release-files)

The zipimport Unix executable and release tarball contain code licensed under ISC and MIT. The PyInstaller-bundled executables are subject to these and other licenses, all of which are compiled in [THIRD_PARTY_LICENSES.txt](https://github.com/yt-dlp/yt-dlp/blob/6ccd977303412151ee23352c6257dd
```
</details>

---
### 📦 [obsproject/obs-studio](https://github.com/obsproject/obs-studio)
`⭐ Stars: 78,226` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [33.0.0](https://github.com/obsproject/obs-studio/releases/tag/33.0.0) (2026-10-23)`

> **简介**：OBS Studio - Free and open source software for live streaming and screen recording

**💡 核心亮点更新 (中文)**：
* Updated CEF from 127/6533 to 150/7871 [WizardCM] ([#13900](https://github.com/obsproject/obs-studio/pull/13900))
* Complete overhaul to plugin loading [FiniteSingularity/PatTheMav] ([#13594](https://github.com/obsproject/obs-studio/pull/13594))
* Improved how source snapping works in the preview [Warchamp7] ([#12298](https://github.com/obsproject/obs-studio/pull/12298))

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
33.0 New Features
-----------------

* Updated CEF from 127/6533 to 150/7871 [WizardCM] ([#13900](https://github.com/obsproject/obs-studio/pull/13900))
  + This is a massive update to the underlying framework used for browser sources and docks from the July 2024 release to September 2026
  + All of this work is on the backend and should be invisible to users. Please be sure to report any new weirdness or problems you run into with browser sources!
* Complete overhaul to plugin loading [FiniteSingularity/PatTheMav] ([#13594](https://github.com/obsproject/obs-studio/pull/13594))
  + First-party plugins are now in a new folder named core
  + Third-party plugins have an updated installation location and folder structure
  + Existing third-party plugins will continue to load from the legacy locations until OBS Studio 34.0
  + More information is available in our [knowledge base article](https://obsproject.com/kb/legacy-plugin-locations)
* Improved how source snapping works in the preview [Warchamp7] ([#12298](https://github.com/obsproject/obs-studio/pull/12298))
  + New visual indicator added
  + Sources now snap along the entire axis instead of only when directly touching
  + Sources no longer snap to hidden sources
* Improved behavior of spinboxes for number values [Warchamp7] ([#12337](https://github.com/obsproject/obs-studio/pull/12337))
  + Typing is no longer mysteriously blocked in some situations
  + Numbers are no longer cut off in some situations
  + Va
```
</details>

---
### 📦 [jerrykuku/luci-theme-argon](https://github.com/jerrykuku/luci-theme-argon)
`⭐ Stars: 5,553` &nbsp;|&nbsp; `💻 语言: CSS` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.1.0](https://github.com/jerrykuku/luci-theme-argon/releases/tag/v3.1.0) (2026-10-22)`

> **简介**：Argon is a clean and tidy OpenWrt LuCI theme that allows users to customize their login interface with images or videos.   It also supports automatic and manual switching between light and dark modes.

**💡 核心亮点更新 (中文)**：
- Add stable release checks and online theme installation under **System → Argon Config → Theme updates**, using the firmware's native APK or OPKG package manager and preserving Argon settings.
- Verify package SHA256 and size before installation, reject downgrades, and show installation progress and logs with monitoring that resumes after a page refresh.
- 新增稳定版检查与在线安装，可在**系统 → Argon 配置 → 主题更新**中通过固件原生 APK 或 OPKG 包管理器升级，并保留 Argon 设置。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Added / 新功能

- Add stable release checks and online theme installation under **System → Argon Config → Theme updates**, using the firmware's native APK or OPKG package manager and preserving Argon settings.
- Verify package SHA256 and size before installation, reject downgrades, and show installation progress and logs with monitoring that resumes after a page refresh.

- 新增稳定版检查与在线安装，可在**系统 → Argon 配置 → 主题更新**中通过固件原生 APK 或 OPKG 包管理器升级，并保留 Argon 设置。
- 新增安装包校验、降级保护、安装进度和日志，刷新页面后可继续跟踪安装状态。

## Changed / 改进

- Improve compatibility with stable OpenWrt firmware.

- 改善稳定版 OpenWrt 固件上的兼容性。

## Fixed / 修复

- Fix dashboard action spacing and overview layouts.
- Fix dynamic list controls and custom IP/MAC input borders across narrow screens, light/dark modes and RTL layouts.

- 修复 Dashboard 操作区间距和概览布局。
- 修复动态列表控件及自定义 IP/MAC 输入框边框，兼顾窄屏、亮暗色和 RTL 布局。

## Upgrade notes / 升级说明

**First upgrade:** users on v3.0.0 or earlier must install v3.1.0 manually once. Later releases can be installed through Theme updates. Online installation updates the theme package; install separate translation packages in the usual way.

**首次升级：** v3.0.0 及更早版本用户需先手动安装一次 v3.1.0，之后可使用主题更新功能在线升级。在线安装仅更新主题主包，独立语言包仍按原方式安装。

## Installation / 安装说明

| Firmware / 固件 | Package / 安装包 |
| --- | --- |
| Native `opkg`, including OpenWrt 23.05 / 24.10 and GL.iNet firmware based on them / 原生使用 `opkg` 的固件 | `.ipk` → `opkg install` |
| Native APK v3 with `apk-tools 3.x` / 原生使用 APK v3 的固件 | `.apk` → `apk add --allow-untrusted` |
```
</details>

---
### 📦 [qier222/YesPlayMusic](https://github.com/qier222/YesPlayMusic)
`⭐ Stars: 33,456` &nbsp;|&nbsp; `💻 语言: Vue` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.4.11](https://github.com/qier222/YesPlayMusic/releases/tag/v0.4.11) (2026-10-10)`

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
`⭐ Stars: 57,424` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.0.1](https://github.com/agalwood/Motrix/releases/tag/v2.0.1) (2026-10-25)`

> **简介**：A full-featured download manager.

**💡 核心亮点更新 (中文)**：
* fix(snap): accept canonical workflow run paths by  in https://github.com/agalwood/Motrix/pull/2409
* fix(release): allow time for verified artifact transfers by  in https://github.com/agalwood/Motrix/pull/2410
* fix(release): validate snap scope and allow larger source headers by  in https://github.com/agalwood/Motrix/pull/2411

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# Motrix 2.0.1

English | [简体中文](https://github.com/agalwood/Motrix/blob/v2.0.1/docs/release-notes/2.0.1.zh-CN.md)

Motrix 2.0.1 is a maintenance release for the desktop app and headless Server.
It improves download recovery, desktop stability, and memory use, and updates
application and packaging dependencies.

## Changes since 2.0.0

- Improves HTTP resume metadata checks and preserves resource identity across
  cross-origin redirects, including redirects back to the original host.
  Failed verification now reports diagnostic reasons without exposing secrets;
  unverifiable partial files remain protected from unsafe resume.
- Allows verified legacy HTTP downloads to resume through the Migration
  Assistant when the original partial file and checkpoint pass the supported
  recovery checks. Importing a task still leaves it paused until activation.
- Adds recovery after repeated graphics crashes, with hardware acceleration
  controls in Appearance settings.
- Bounds cached migration data and plugin logs, releases idle runtime
  resources, and improves tray renderer cleanup to reduce memory use.
- Bundles aria2 **1.37.0-motrix.21**, including DNS timer recovery for the
  select event loop. Managed aria2 processes now stop when their desktop or
  Server host exits unexpectedly.
- Uses the package name `motrix` consistently for native Linux packages.
- Updates electron-builder, electron-updater, React Hook Form, i18next,
  react-i18next, and Biome. Plugin test fixtures now share
```
</details>

---
### 📦 [subhra74/xdm](https://github.com/subhra74/xdm)
`⭐ Stars: 8,075` &nbsp;|&nbsp; `💻 语言: Kotlin` &nbsp;|&nbsp; `🏷️ 最新版本: [9.0.8](https://github.com/subhra74/xdm/releases/tag/9.0.8) (2026-10-25)`

> **简介**：Fast, reliable download accelerator and video downloader, trusted for 13+ years

**💡 核心亮点更新 (中文)**：
Downloads

| Installer | Notes |
|---|---|
| [xdm-app-9.0.8-arm64.dmg](https://github.com/subhra74/xdm/releases/download/9.0.8/xdm-app-9.0.8-arm64.dmg) | For Apple Silicon (M1 or later) mac |
| [xdm-app-9.0.8-x64.dmg](https://github.com/subhra74

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Downloads

| Installer | Notes |
|---|---|
| [xdm-app-9.0.8-arm64.dmg](https://github.com/subhra74/xdm/releases/download/9.0.8/xdm-app-9.0.8-arm64.dmg) | For Apple Silicon (M1 or later) mac |
| [xdm-app-9.0.8-x64.dmg](https://github.com/subhra74/xdm/releases/download/9.0.8/xdm-app-9.0.8-x64.dmg) | For Intel mac |
| [xdm-9.0.8-arm64.msi](https://github.com/subhra74/xdm/releases/download/9.0.8/xdm-9.0.8-arm64.msi) | For Windows ARM (Windows 10/11) |
| [xdm-9.0.8-x64.msi](https://github.com/subhra74/xdm/releases/download/9.0.8/xdm-9.0.8-x64.msi) | For Windows x64 (Windows 10/11) |
| [xdm-app_9.0.8_amd64.deb](https://github.com/subhra74/xdm/releases/download/9.0.8/xdm-app_9.0.8_amd64.deb) | For Debian / Ubuntu / Linux Mint x64 |
| [xdm-app_9.0.8_arm64.deb](https://github.com/subhra74/xdm/releases/download/9.0.8/xdm-app_9.0.8_arm64.deb) | For Debian / Ubuntu / Linux Mint ARM |
| [xdm-app-9.0.8-1.aarch64.rpm](https://github.com/subhra74/xdm/releases/download/9.0.8/xdm-app-9.0.8-1.aarch64.rpm) | For Fedora / RHEL / openSUSE ARM |
| [xdm-app-9.0.8-1.x86_64.rpm](https://github.com/subhra74/xdm/releases/download/9.0.8/xdm-app-9.0.8-1.x86_64.rpm) | For Fedora / RHEL / openSUSE x64 |
| [xdm-app-9.0.8-1-aarch64.pkg.tar.zst](https://github.com/subhra74/xdm/releases/download/9.0.8/xdm-app-9.0.8-1-aarch64.pkg.tar.zst) | For Arch Linux / Manjaro ARM |
| [xdm-app-9.0.8-1-x86_64.pkg.tar.zst](https://github.com/subhra74/xdm/releases/download/9.0.8/xdm-app-9.0.8-1-x86_64.pkg.tar.z
```
</details>

---

## <span id="-效率办公与创作">📝 效率办公与创作</span>

### 📦 [robbietilton/Compositor](https://github.com/robbietilton/Compositor)
`⭐ Stars: 17,901` &nbsp;|&nbsp; `💻 语言: Swift` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.5.10](https://github.com/robbietilton/Compositor/releases/tag/v1.5.10) (2026-10-26)`

> **简介**：The Photoshop alternative for Mac

**💡 核心亮点更新 (中文)**：
- Filter › Sharpen: an unsharp mask with Amount and Radius, also as an adjustment layer.
- Align and Distribute layers, from the Align button in the Move tool's bar or the Layer menu.
- Crop to any ratio with Custom…, plus a 2.39:1 widescreen preset; the ratios are grouped by shape, and Original is now Canvas.

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
- Filter › Sharpen: an unsharp mask with Amount and Radius, also as an adjustment layer.
- Align and Distribute layers, from the Align button in the Move tool's bar or the Layer menu.
- Crop to any ratio with Custom…, plus a 2.39:1 widescreen preset; the ratios are grouped by shape, and Original is now Canvas.
- Tidier tool bars: flip buttons as icons, and number fields sized to fit.
```
</details>

---
### 📦 [jgraph/drawio-desktop](https://github.com/jgraph/drawio-desktop)
`⭐ Stars: 63,651` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v32.6.1](https://github.com/jgraph/drawio-desktop/releases/tag/v32.6.1) (2026-10-23)`

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
`⭐ Stars: 95,019` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.2.2](https://github.com/Stirling-Tools/Stirling-PDF/releases/tag/v3.2.2) (2026-10-24)`

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
`⭐ Stars: 40,020` &nbsp;|&nbsp; `💻 语言: Java` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.27.1](https://github.com/halo-dev/halo/releases/tag/v2.27.1) (2026-10-23)`

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
`⭐ Stars: 4,052` &nbsp;|&nbsp; `💻 语言: PHP` &nbsp;|&nbsp; `🏷️ 最新版本: [2.4.2](https://github.com/zyx0814/dzzoffice/releases/tag/2.4.2) (2026-10-22)`

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
`⭐ Stars: 4,781` &nbsp;|&nbsp; `💻 语言: C#` &nbsp;|&nbsp; `🏷️ 最新版本: [4.16.2-Installer](https://github.com/emoacht/Monitorian/releases/tag/4.16.2-Installer) (2026-10-12)`

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
`⭐ Stars: 14,596` &nbsp;|&nbsp; `💻 语言: PowerShell` &nbsp;|&nbsp; `🏷️ 最新版本: [v11.8.50.0](https://github.com/YerongAI/Office-Tool/releases/tag/v11.8.50.0) (2026-10-18)`

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
`⭐ Stars: 194,311` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [1.143.1](https://github.com/microsoft/vscode/releases/tag/1.143.1) (2026-10-22)`

> **简介**：Visual Studio Code

**💡 核心亮点更新 (中文)**：
https://code.visualstudio.com/updates/v1_143

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
https://code.visualstudio.com/updates/v1_143
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
`⭐ Stars: 39,245` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.14.4](https://github.com/SagerNet/sing-box/releases/tag/v1.14.4) (2026-10-24)`

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
`⭐ Stars: 10,757` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [2.44.2](https://github.com/sub-store-org/Sub-Store/releases/tag/2.44.2) (2026-10-25)`

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
### 📦 [enfein/mieru](https://github.com/enfein/mieru)
`⭐ Stars: 2,636` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.39.0](https://github.com/enfein/mieru/releases/tag/v3.39.0) (2026-10-23)`

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
`⭐ Stars: 15,745` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.5.10](https://github.com/v2rayA/v2rayA/releases/tag/v2.5.10) (2026-10-09)`

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
`⭐ Stars: 27,938` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.48.002](https://github.com/vernesong/OpenClash/releases/tag/v0.48.002) (2026-10-12)`

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
`⭐ Stars: 22,735` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [app/v2.13.0](https://github.com/HyNetworks/hysteria/releases/tag/app/v2.13.0) (2026-10-05)`

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
`⭐ Stars: 2,772` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [25.12.6](https://github.com/QiuSimons/YAOF/releases/tag/25.12.6) (2026-10-18)`

> **简介**：适用于 Nanopi R2C/R2S/R4S/X86 的 OpenWrt

**💡 核心亮点更新 (中文)**：
该版本未提供详细更新说明。

---
### 📦 [Loyalsoldier/v2ray-rules-dat](https://github.com/Loyalsoldier/v2ray-rules-dat)
`⭐ Stars: 20,942` &nbsp;|&nbsp; `💻 语言: Other` &nbsp;|&nbsp; `🏷️ 最新版本: [202610242205](https://github.com/Loyalsoldier/v2ray-rules-dat/releases/tag/202610242205) (2026-10-24)`

> **简介**：🦄 🎃 👻 V2Ray 路由规则文件加强版，可代替 V2Ray 官方 geoip.dat 和 geosite.dat，适用于 V2Ray、Xray-core、mihomo(Clash-Meta)、hysteria、Trojan-Go 和 leaf。Enhanced edition of V2Ray rules dat files, applicable to V2Ray, Xray-core, mihomo(Clash-Meta), hysteria, Trojan-Go and leaf.

**💡 核心亮点更新 (中文)**：
该版本未提供详细更新说明。

---
### 📦 [Openwrt-Passwall/openwrt-passwall](https://github.com/Openwrt-Passwall/openwrt-passwall)
`⭐ Stars: 9,980` &nbsp;|&nbsp; `💻 语言: Lua` &nbsp;|&nbsp; `🏷️ 最新版本: [26.10.22-2](https://github.com/Openwrt-Passwall/openwrt-passwall/releases/tag/26.10.22-2) (2026-10-22)`

> **简介**：暂无项目描述

**💡 核心亮点更新 (中文)**：
* 请按照 [openwrt-passwall-build](https://github.com/moetayuko/openwrt-passwall-build) 仓库的说明，将其提供的软件源添加到设备中，然后直接使用包管理器安装。
* 从 [SourceForge](https://sourceforge.net/projects/openwrt-passwall-build/files/) 下载预构建的软件包。
* 将文件上传到您的设备，使用 Shell 命令进行安装。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
![](https://img.shields.io/github/downloads/Openwrt-Passwall/openwrt-passwall/26.10.22-2/total?style=flat-square)
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
`⭐ Stars: 119,107` &nbsp;|&nbsp; `💻 语言: C#` &nbsp;|&nbsp; `🏷️ 最新版本: [7.25.6](https://github.com/2dust/v2rayN/releases/tag/7.25.6) (2026-10-11)`

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
`⭐ Stars: 28,933` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [v25.12.6](https://github.com/openwrt/openwrt/releases/tag/v25.12.6) (2026-10-18)`

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
`⭐ Stars: 80,350` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.1.18](https://github.com/ventoy/Ventoy/releases/tag/v1.1.18) (2026-10-09)`

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
<summary>⚠️ 点击展开已放弃维护或超过 1 年停更的仓库清单 (135 个)</summary>

| 仓库名称 | Stars | 状态说明 | 操作建议 |
| :--- | :---: | :--- | :---: |
| [cityflow-project/CityFlow](https://github.com/cityflow-project/CityFlow) | 1,029 | 超过 432 天无代码提交 | [进入取消 Star](https://github.com/cityflow-project/CityFlow) |
| [facebookresearch/demucs](https://github.com/facebookresearch/demucs) | 10,402 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/facebookresearch/demucs) |
| [JimmyLv/awesome-nano-banana](https://github.com/JimmyLv/awesome-nano-banana) | 8,804 | 超过 412 天无代码提交 | [进入取消 Star](https://github.com/JimmyLv/awesome-nano-banana) |
| [btjawa/BiliTools](https://github.com/btjawa/BiliTools) | 5,042 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/btjawa/BiliTools) |
| [ehang-io/nps](https://github.com/ehang-io/nps) | 34,261 | 超过 879 天无代码提交 | [进入取消 Star](https://github.com/ehang-io/nps) |
| [ReturnFI/Blitz](https://github.com/ReturnFI/Blitz) | 1,092 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/ReturnFI/Blitz) |
| [kkangert/kspider](https://github.com/kkangert/kspider) | 1,265 | 超过 798 天无代码提交 | [进入取消 Star](https://github.com/kkangert/kspider) |
| [xenova/whisper-web](https://github.com/xenova/whisper-web) | 3,344 | 超过 754 天无代码提交 | [进入取消 Star](https://github.com/xenova/whisper-web) |
| [shadowsocks/luci-app-shadowsocks](https://github.com/shadowsocks/luci-app-shadowsocks) | 1,150 | 超过 1246 天无代码提交 | [进入取消 Star](https://github.com/shadowsocks/luci-app-shadowsocks) |
| [adithya-s-k/marker-api](https://github.com/adithya-s-k/marker-api) | 984 | 超过 740 天无代码提交 | [进入取消 Star](https://github.com/adithya-s-k/marker-api) |
| [yuchannslv5/warpflare](https://github.com/yuchannslv5/warpflare) | 334 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/yuchannslv5/warpflare) |
| [vvbbnn00/WARP-Clash-API](https://github.com/vvbbnn00/WARP-Clash-API) | 8,818 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/vvbbnn00/WARP-Clash-API) |
| [ca110us/epeius](https://github.com/ca110us/epeius) | 1,223 | 超过 798 天无代码提交 | [进入取消 Star](https://github.com/ca110us/epeius) |
| [chika0801/hysteria-install](https://github.com/chika0801/hysteria-install) | 178 | 超过 843 天无代码提交 | [进入取消 Star](https://github.com/chika0801/hysteria-install) |
| [yeahwu/InstallOS](https://github.com/yeahwu/InstallOS) | 86 | 超过 1600 天无代码提交 | [进入取消 Star](https://github.com/yeahwu/InstallOS) |
| [bulianglin/psub](https://github.com/bulianglin/psub) | 1,762 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/bulianglin/psub) |
| [lizongying/my-tv](https://github.com/lizongying/my-tv) | 31,972 | 超过 857 天无代码提交 | [进入取消 Star](https://github.com/lizongying/my-tv) |
| [joevess/IPTV](https://github.com/joevess/IPTV) | 10,284 | 超过 663 天无代码提交 | [进入取消 Star](https://github.com/joevess/IPTV) |
| [lecepin/WeChatVideoDownloader](https://github.com/lecepin/WeChatVideoDownloader) | 4,667 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/lecepin/WeChatVideoDownloader) |
| [linexjlin/GPTs](https://github.com/linexjlin/GPTs) | 32,033 | 超过 759 天无代码提交 | [进入取消 Star](https://github.com/linexjlin/GPTs) |
| [lxfater/Awesome-GPTs](https://github.com/lxfater/Awesome-GPTs) | 1,152 | 超过 1069 天无代码提交 | [进入取消 Star](https://github.com/lxfater/Awesome-GPTs) |
| [ClashDotNetFramework/experimental-clash](https://github.com/ClashDotNetFramework/experimental-clash) | 241 | 超过 1784 天无代码提交 | [进入取消 Star](https://github.com/ClashDotNetFramework/experimental-clash) |
| [zzzgydi/clash-verge](https://github.com/zzzgydi/clash-verge) | 21,874 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/zzzgydi/clash-verge) |
| [ddgth/cf2dns](https://github.com/ddgth/cf2dns) | 5,211 | 超过 657 天无代码提交 | [进入取消 Star](https://github.com/ddgth/cf2dns) |
| [zizifn/edgetunnel](https://github.com/zizifn/edgetunnel) | 9,282 | 超过 697 天无代码提交 | [进入取消 Star](https://github.com/zizifn/edgetunnel) |
| [missuo/Hysteria2](https://github.com/missuo/Hysteria2) | 204 | 超过 788 天无代码提交 | [进入取消 Star](https://github.com/missuo/Hysteria2) |
| [Misaka-blog/hysteria-install](https://github.com/Misaka-blog/hysteria-install) | 629 | 超过 920 天无代码提交 | [进入取消 Star](https://github.com/Misaka-blog/hysteria-install) |
| [MatsuriDayo/nekoray](https://github.com/MatsuriDayo/nekoray) | 15,280 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/MatsuriDayo/nekoray) |
| [FranzKafkaYu/x-ui](https://github.com/FranzKafkaYu/x-ui) | 8,457 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/FranzKafkaYu/x-ui) |
| [rwv/chinese-dos-games](https://github.com/rwv/chinese-dos-games) | 10,339 | 超过 809 天无代码提交 | [进入取消 Star](https://github.com/rwv/chinese-dos-games) |
| [getumbrel/llama-gpt](https://github.com/getumbrel/llama-gpt) | 10,919 | 超过 915 天无代码提交 | [进入取消 Star](https://github.com/getumbrel/llama-gpt) |
| [WangWenBin2017/OpenWrt-SSRPLUS](https://github.com/WangWenBin2017/OpenWrt-SSRPLUS) | 562 | 超过 602 天无代码提交 | [进入取消 Star](https://github.com/WangWenBin2017/OpenWrt-SSRPLUS) |
| [prompt-engineering/click-prompt](https://github.com/prompt-engineering/click-prompt) | 2,389 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/prompt-engineering/click-prompt) |
| [AutodeskAILab/Building-GAN](https://github.com/AutodeskAILab/Building-GAN) | 101 | 超过 1605 天无代码提交 | [进入取消 Star](https://github.com/AutodeskAILab/Building-GAN) |
| [novicezk/midjourney-proxy](https://github.com/novicezk/midjourney-proxy) | 5,371 | 超过 448 天无代码提交 | [进入取消 Star](https://github.com/novicezk/midjourney-proxy) |
| [adams549659584/go-proxy-bingai](https://github.com/adams549659584/go-proxy-bingai) | 8,408 | 超过 949 天无代码提交 | [进入取消 Star](https://github.com/adams549659584/go-proxy-bingai) |
| [tryptech/obs-zoom-and-follow](https://github.com/tryptech/obs-zoom-and-follow) | 440 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/tryptech/obs-zoom-and-follow) |
| [XingangPan/DragGAN](https://github.com/XingangPan/DragGAN) | 35,720 | 超过 890 天无代码提交 | [进入取消 Star](https://github.com/XingangPan/DragGAN) |
| [lewangdev/faster-whisper-youtube](https://github.com/lewangdev/faster-whisper-youtube) | 560 | 超过 1162 天无代码提交 | [进入取消 Star](https://github.com/lewangdev/faster-whisper-youtube) |
| [artidoro/qlora](https://github.com/artidoro/qlora) | 11,054 | 超过 867 天无代码提交 | [进入取消 Star](https://github.com/artidoro/qlora) |
| [langgenius/webapp-conversation](https://github.com/langgenius/webapp-conversation) | 1,102 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/langgenius/webapp-conversation) |
| [3andne/restls](https://github.com/3andne/restls) | 375 | 超过 1085 天无代码提交 | [进入取消 Star](https://github.com/3andne/restls) |
| [jtsang4/claude-to-chatgpt](https://github.com/jtsang4/claude-to-chatgpt) | 1,300 | 超过 798 天无代码提交 | [进入取消 Star](https://github.com/jtsang4/claude-to-chatgpt) |
| [yorunning/clash-conf](https://github.com/yorunning/clash-conf) | 102 | 超过 831 天无代码提交 | [进入取消 Star](https://github.com/yorunning/clash-conf) |
| [svc-develop-team/so-vits-svc](https://github.com/svc-develop-team/so-vits-svc) | 28,068 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/svc-develop-team/so-vits-svc) |
| [xiaye13579/BBLL](https://github.com/xiaye13579/BBLL) | 17,511 | 超过 605 天无代码提交 | [进入取消 Star](https://github.com/xiaye13579/BBLL) |
| [camenduru/MiniGPT-4-colab](https://github.com/camenduru/MiniGPT-4-colab) | 119 | 超过 1183 天无代码提交 | [进入取消 Star](https://github.com/camenduru/MiniGPT-4-colab) |
| [Vision-CAIR/MiniGPT-4](https://github.com/Vision-CAIR/MiniGPT-4) | 25,578 | 超过 783 天无代码提交 | [进入取消 Star](https://github.com/Vision-CAIR/MiniGPT-4) |
| [imfuxiao/Hamster](https://github.com/imfuxiao/Hamster) | 1,641 | 超过 530 天无代码提交 | [进入取消 Star](https://github.com/imfuxiao/Hamster) |
| [acheong08/ChatGPT](https://github.com/acheong08/ChatGPT) | 27,971 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/acheong08/ChatGPT) |
| [microsoft/JARVIS](https://github.com/microsoft/JARVIS) | 25,500 | 超过 453 天无代码提交 | [进入取消 Star](https://github.com/microsoft/JARVIS) |
| [choephix/auto-gpt-webui](https://github.com/choephix/auto-gpt-webui) | 116 | 超过 951 天无代码提交 | [进入取消 Star](https://github.com/choephix/auto-gpt-webui) |
| [facebookresearch/segment-anything](https://github.com/facebookresearch/segment-anything) | 55,063 | 超过 767 天无代码提交 | [进入取消 Star](https://github.com/facebookresearch/segment-anything) |
| [zai-org/ChatGLM-6B](https://github.com/zai-org/ChatGLM-6B) | 40,905 | 超过 851 天无代码提交 | [进入取消 Star](https://github.com/zai-org/ChatGLM-6B) |
| [ihciah/shadow-tls](https://github.com/ihciah/shadow-tls) | 2,681 | 超过 548 天无代码提交 | [进入取消 Star](https://github.com/ihciah/shadow-tls) |
| [jxbbb/ADAPT](https://github.com/jxbbb/ADAPT) | 421 | 超过 866 天无代码提交 | [进入取消 Star](https://github.com/jxbbb/ADAPT) |
| [mayooear/ai-pdf-chatbot-langchain](https://github.com/mayooear/ai-pdf-chatbot-langchain) | 16,581 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/mayooear/ai-pdf-chatbot-langchain) |
| [lencx/ChatGPT](https://github.com/lencx/ChatGPT) | 54,661 | 超过 787 天无代码提交 | [进入取消 Star](https://github.com/lencx/ChatGPT) |
| [nekohasekai/SagerNet](https://github.com/nekohasekai/SagerNet) | 56 | 超过 1750 天无代码提交 | [进入取消 Star](https://github.com/nekohasekai/SagerNet) |
| [P3TERX/Actions-OpenWrt](https://github.com/P3TERX/Actions-OpenWrt) | 7,621 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/P3TERX/Actions-OpenWrt) |
| [R86S/R86S-QuickInstaller](https://github.com/R86S/R86S-QuickInstaller) | 65 | 超过 1171 天无代码提交 | [进入取消 Star](https://github.com/R86S/R86S-QuickInstaller) |
| [WeNeedHome/SummaryOfLoanSuspension](https://github.com/WeNeedHome/SummaryOfLoanSuspension) | 20,337 | 超过 835 天无代码提交 | [进入取消 Star](https://github.com/WeNeedHome/SummaryOfLoanSuspension) |
| [zanzhz1101/LingMaxDNS](https://github.com/zanzhz1101/LingMaxDNS) | 23 | 超过 1566 天无代码提交 | [进入取消 Star](https://github.com/zanzhz1101/LingMaxDNS) |
| [IrineSistiana/mosdns-cn](https://github.com/IrineSistiana/mosdns-cn) | 325 | 超过 1607 天无代码提交 | [进入取消 Star](https://github.com/IrineSistiana/mosdns-cn) |
| [chika0801/Xray-install](https://github.com/chika0801/Xray-install) | 273 | 超过 1059 天无代码提交 | [进入取消 Star](https://github.com/chika0801/Xray-install) |
| [alesimula/wsa_pacman](https://github.com/alesimula/wsa_pacman) | 4,190 | 超过 1038 天无代码提交 | [进入取消 Star](https://github.com/alesimula/wsa_pacman) |
| [scutan90/DeepLearning-500-questions](https://github.com/scutan90/DeepLearning-500-questions) | 57,688 | 超过 851 天无代码提交 | [进入取消 Star](https://github.com/scutan90/DeepLearning-500-questions) |
| [Chikage0o0/Linux-NetSpeed](https://github.com/Chikage0o0/Linux-NetSpeed) | 3,746 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/Chikage0o0/Linux-NetSpeed) |
| [KFERMercer/OpenWrt-CI](https://github.com/KFERMercer/OpenWrt-CI) | 1,409 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/KFERMercer/OpenWrt-CI) |
| [qTox/qTox](https://github.com/qTox/qTox) | 4,971 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/qTox/qTox) |
| [quericy/one-key-ikev2-vpn](https://github.com/quericy/one-key-ikev2-vpn) | 2,104 | 超过 2169 天无代码提交 | [进入取消 Star](https://github.com/quericy/one-key-ikev2-vpn) |
| [riverscn/openwrt-iptvhelper](https://github.com/riverscn/openwrt-iptvhelper) | 371 | 超过 1885 天无代码提交 | [进入取消 Star](https://github.com/riverscn/openwrt-iptvhelper) |
| [frainzy1477/luci-app-clash](https://github.com/frainzy1477/luci-app-clash) | 1,623 | 超过 1676 天无代码提交 | [进入取消 Star](https://github.com/frainzy1477/luci-app-clash) |
| [Sanster/IOPaint](https://github.com/Sanster/IOPaint) | 23,297 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/Sanster/IOPaint) |
| [LANDrop/LANDrop](https://github.com/LANDrop/LANDrop) | 5,992 | 超过 803 天无代码提交 | [进入取消 Star](https://github.com/LANDrop/LANDrop) |
| [saveweb/review-2021](https://github.com/saveweb/review-2021) | 758 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/saveweb/review-2021) |
| [iranee/qnap-aliyunpan-webdav](https://github.com/iranee/qnap-aliyunpan-webdav) | 274 | 超过 1478 天无代码提交 | [进入取消 Star](https://github.com/iranee/qnap-aliyunpan-webdav) |
| [haoel/haoel.github.io](https://github.com/haoel/haoel.github.io) | 13,077 | 超过 1263 天无代码提交 | [进入取消 Star](https://github.com/haoel/haoel.github.io) |
| [tindy2013/stairspeedtest-reborn](https://github.com/tindy2013/stairspeedtest-reborn) | 3,831 | 超过 1235 天无代码提交 | [进入取消 Star](https://github.com/tindy2013/stairspeedtest-reborn) |
| [P3TERX/warp.sh](https://github.com/P3TERX/warp.sh) | 3,927 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/P3TERX/warp.sh) |
| [TheMRLL/WinXray](https://github.com/TheMRLL/WinXray) | 2,793 | 超过 971 天无代码提交 | [进入取消 Star](https://github.com/TheMRLL/WinXray) |
| [Mikubill/cowtransfer-uploader](https://github.com/Mikubill/cowtransfer-uploader) | 447 | 超过 1718 天无代码提交 | [进入取消 Star](https://github.com/Mikubill/cowtransfer-uploader) |
| [281677160/build-actions](https://github.com/281677160/build-actions) | 389 | 超过 453 天无代码提交 | [进入取消 Star](https://github.com/281677160/build-actions) |
| [vaxilu/x-ui](https://github.com/vaxilu/x-ui) | 19,089 | 超过 797 天无代码提交 | [进入取消 Star](https://github.com/vaxilu/x-ui) |
| [xinntao/Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) | 37,220 | 超过 810 天无代码提交 | [进入取消 Star](https://github.com/xinntao/Real-ESRGAN) |
| [zu1k/proxypool](https://github.com/zu1k/proxypool) | 4,038 | 超过 1294 天无代码提交 | [进入取消 Star](https://github.com/zu1k/proxypool) |
| [TachibanaYoshino/AnimeGAN](https://github.com/TachibanaYoshino/AnimeGAN) | 4,612 | 超过 1544 天无代码提交 | [进入取消 Star](https://github.com/TachibanaYoshino/AnimeGAN) |
| [yuanzhoulvpi2017/tiny_python](https://github.com/yuanzhoulvpi2017/tiny_python) | 173 | 超过 1358 天无代码提交 | [进入取消 Star](https://github.com/yuanzhoulvpi2017/tiny_python) |
| [haiibo/OpenWrt](https://github.com/haiibo/OpenWrt) | 3,161 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/haiibo/OpenWrt) |
| [VergilGao/openwrt-packages](https://github.com/VergilGao/openwrt-packages) | 11 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/VergilGao/openwrt-packages) |
| [VergilGao/openwrt-compiler](https://github.com/VergilGao/openwrt-compiler) | 13 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/VergilGao/openwrt-compiler) |
| [OpenELEC/OpenELEC.tv](https://github.com/OpenELEC/OpenELEC.tv) | 1,620 | 超过 3340 天无代码提交 | [进入取消 Star](https://github.com/OpenELEC/OpenELEC.tv) |
| [github/copilot-docs](https://github.com/github/copilot-docs) | 23,173 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/github/copilot-docs) |
| [Kiougar/luci-wrtbwmon](https://github.com/Kiougar/luci-wrtbwmon) | 356 | 超过 1858 天无代码提交 | [进入取消 Star](https://github.com/Kiougar/luci-wrtbwmon) |
| [EtherDream/jsproxy](https://github.com/EtherDream/jsproxy) | 9,321 | 超过 938 天无代码提交 | [进入取消 Star](https://github.com/EtherDream/jsproxy) |
| [cheat-engine/cheat-engine](https://github.com/cheat-engine/cheat-engine) | 19,387 | 超过 554 天无代码提交 | [进入取消 Star](https://github.com/cheat-engine/cheat-engine) |
| [ffffffff0x/Dork-Admin](https://github.com/ffffffff0x/Dork-Admin) | 1,915 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/ffffffff0x/Dork-Admin) |
| [ffffffff0x/Digital-Privacy](https://github.com/ffffffff0x/Digital-Privacy) | 4,938 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/ffffffff0x/Digital-Privacy) |
| [Autodesk/civilconnection](https://github.com/Autodesk/civilconnection) | 117 | 超过 1424 天无代码提交 | [进入取消 Star](https://github.com/Autodesk/civilconnection) |
| [0xHJK/CleanApps](https://github.com/0xHJK/CleanApps) | 165 | 超过 1890 天无代码提交 | [进入取消 Star](https://github.com/0xHJK/CleanApps) |
| [KANIKIG/Multi-EasyGost](https://github.com/KANIKIG/Multi-EasyGost) | 1,948 | 超过 938 天无代码提交 | [进入取消 Star](https://github.com/KANIKIG/Multi-EasyGost) |
| [Kurokosama/AutoBuild-OpenWRT](https://github.com/Kurokosama/AutoBuild-OpenWRT) | 88 | 超过 1577 天无代码提交 | [进入取消 Star](https://github.com/Kurokosama/AutoBuild-OpenWRT) |
| [differentrain/DeletionTool](https://github.com/differentrain/DeletionTool) | 94 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/differentrain/DeletionTool) |
| [hideuvpn/android-google-play-store](https://github.com/hideuvpn/android-google-play-store) | 3,646 | 超过 1559 天无代码提交 | [进入取消 Star](https://github.com/hideuvpn/android-google-play-store) |
| [XJP-GIT/AntiZhaPian](https://github.com/XJP-GIT/AntiZhaPian) | 3,161 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/XJP-GIT/AntiZhaPian) |
| [jerrykuku/luci-app-ttnode](https://github.com/jerrykuku/luci-app-ttnode) | 89 | 超过 1735 天无代码提交 | [进入取消 Star](https://github.com/jerrykuku/luci-app-ttnode) |
| [KevinSHIT/NaiveSharp](https://github.com/KevinSHIT/NaiveSharp) | 96 | 超过 2180 天无代码提交 | [进入取消 Star](https://github.com/KevinSHIT/NaiveSharp) |
| [prasmussen/gdrive](https://github.com/prasmussen/gdrive) | 8,944 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/prasmussen/gdrive) |
| [tostercx/GTAO_Booster_PoC](https://github.com/tostercx/GTAO_Booster_PoC) | 2,865 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/tostercx/GTAO_Booster_PoC) |
| [ilxp/luci-app-ikoolproxy](https://github.com/ilxp/luci-app-ikoolproxy) | 507 | 超过 590 天无代码提交 | [进入取消 Star](https://github.com/ilxp/luci-app-ikoolproxy) |
| [kiddin9/luci-app-dnsfilter](https://github.com/kiddin9/luci-app-dnsfilter) | 123 | 超过 623 天无代码提交 | [进入取消 Star](https://github.com/kiddin9/luci-app-dnsfilter) |
| [h31105/deployX.sh](https://github.com/h31105/deployX.sh) | 416 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/h31105/deployX.sh) |
| [jerrykuku/openwrt-package](https://github.com/jerrykuku/openwrt-package) | 148 | 超过 1087 天无代码提交 | [进入取消 Star](https://github.com/jerrykuku/openwrt-package) |
| [frainzy1477/luci-app-trojan](https://github.com/frainzy1477/luci-app-trojan) | 120 | 超过 1994 天无代码提交 | [进入取消 Star](https://github.com/frainzy1477/luci-app-trojan) |
| [atrandys/xray](https://github.com/atrandys/xray) | 89 | 超过 1702 天无代码提交 | [进入取消 Star](https://github.com/atrandys/xray) |
| [v2board/v2board](https://github.com/v2board/v2board) | 5,062 | 超过 951 天无代码提交 | [进入取消 Star](https://github.com/v2board/v2board) |
| [ShadowsocksR-Live/iShadowsocksR](https://github.com/ShadowsocksR-Live/iShadowsocksR) | 600 | 超过 909 天无代码提交 | [进入取消 Star](https://github.com/ShadowsocksR-Live/iShadowsocksR) |
| [SuperNG6/Aria2-Trackers](https://github.com/SuperNG6/Aria2-Trackers) | 309 | 超过 2101 天无代码提交 | [进入取消 Star](https://github.com/SuperNG6/Aria2-Trackers) |
| [kakaruoterl/vless_install](https://github.com/kakaruoterl/vless_install) | 29 | 超过 2258 天无代码提交 | [进入取消 Star](https://github.com/kakaruoterl/vless_install) |
| [stupidloud/nanopi-openwrt](https://github.com/stupidloud/nanopi-openwrt) | 5,515 | 超过 922 天无代码提交 | [进入取消 Star](https://github.com/stupidloud/nanopi-openwrt) |
| [atrandys/trojan](https://github.com/atrandys/trojan) | 1,055 | 超过 1290 天无代码提交 | [进入取消 Star](https://github.com/atrandys/trojan) |
| [programthink/zhao](https://github.com/programthink/zhao) | 14,076 | 超过 1911 天无代码提交 | [进入取消 Star](https://github.com/programthink/zhao) |
| [RPRX/v2ray-vless](https://github.com/RPRX/v2ray-vless) | 389 | 超过 1337 天无代码提交 | [进入取消 Star](https://github.com/RPRX/v2ray-vless) |
| [h2y/Shadowrocket-ADBlock-Rules](https://github.com/h2y/Shadowrocket-ADBlock-Rules) | 16,720 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/h2y/Shadowrocket-ADBlock-Rules) |
| [p4gefau1t/trojan-go](https://github.com/p4gefau1t/trojan-go) | 8,384 | 超过 833 天无代码提交 | [进入取消 Star](https://github.com/p4gefau1t/trojan-go) |
| [Jrohy/trojan](https://github.com/Jrohy/trojan) | 5,632 | 超过 924 天无代码提交 | [进入取消 Star](https://github.com/Jrohy/trojan) |
| [mellow-io/mellow](https://github.com/mellow-io/mellow) | 3,535 | 超过 1415 天无代码提交 | [进入取消 Star](https://github.com/mellow-io/mellow) |
| [Dawneng/luci-theme-atmaterial](https://github.com/Dawneng/luci-theme-atmaterial) | 11 | 超过 1467 天无代码提交 | [进入取消 Star](https://github.com/Dawneng/luci-theme-atmaterial) |
| [trojan-gfw/igniter](https://github.com/trojan-gfw/igniter) | 3,275 | 超过 1064 天无代码提交 | [进入取消 Star](https://github.com/trojan-gfw/igniter) |
| [openwrt-develop/luci-theme-atmaterial](https://github.com/openwrt-develop/luci-theme-atmaterial) | 68 | 超过 2412 天无代码提交 | [进入取消 Star](https://github.com/openwrt-develop/luci-theme-atmaterial) |
| [trojan-gfw/trojan-quickstart](https://github.com/trojan-gfw/trojan-quickstart) | 244 | 超过 2013 天无代码提交 | [进入取消 Star](https://github.com/trojan-gfw/trojan-quickstart) |
| [FunctionClub/ZBench](https://github.com/FunctionClub/ZBench) | 1,177 | 超过 2044 天无代码提交 | [进入取消 Star](https://github.com/FunctionClub/ZBench) |
| [veekxt/v2ray-template](https://github.com/veekxt/v2ray-template) | 749 | 超过 2256 天无代码提交 | [进入取消 Star](https://github.com/veekxt/v2ray-template) |
| [HMBSbige/ShadowsocksR-Windows](https://github.com/HMBSbige/ShadowsocksR-Windows) | 6,913 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/HMBSbige/ShadowsocksR-Windows) |
| [trojan-gfw/trojan](https://github.com/trojan-gfw/trojan) | 19,747 | 超过 795 天无代码提交 | [进入取消 Star](https://github.com/trojan-gfw/trojan) |
</details>
