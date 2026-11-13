# 📡 Starred 项目雷达看板
> 🖥️ **交互式管理看板 (shadcn/ui)**：[👉 点击进入在线雷达看板 (https://stephenchou888.github.io/my-stars-digest/)](https://stephenchou888.github.io/my-stars-digest/)

> **生成时间**：`2026-11-13` ｜ **关注项目总数**：`416` ｜ **本期更新**：`100` ｜ **弃坑预警**：`136`

| 统计指标 | 数量 | 状态提示 |
| :--- | :---: | :--- |
| 🌟 总关注库 | **416** | [进入 shadcn 在线看板管理](https://stephenchou888.github.io/my-stars-digest/) |
| 🚀 近期有更新 | **100** | 涵盖 6 个分类 |
| 🛑 建议清理/弃坑 | **136** | 建议取消 Star 保持关注列表整洁 |

---
## 🧭 领域分类速览导航

- [🤖 AI 与智能体生态 (55)](#-AI-与智能体生态)
- [📦 实用开源精选 (8)](#-实用开源精选)
- [📝 效率办公与创作 (12)](#-效率办公与创作)
- [🎬 影音媒体与下载 (13)](#-影音媒体与下载)
- [🛠️ 系统与开发者工具 (3)](#-系统与开发者工具)
- [🌐 网络与代理技术 (9)](#-网络与代理技术)

---

## <span id="-AI-与智能体生态">🤖 AI 与智能体生态</span>

### 📦 [y5ez3g/facadecode](https://github.com/y5ez3g/facadecode)
`⭐ Stars: 326` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [extension/0.1.3](https://github.com/y5ez3g/facadecode/releases/tag/extension/0.1.3) (2026-11-11)`

> **简介**：VS Code 的多代理协调器。运行 Claude Code、Codex 和其他代理 CLI，这些 CLI 可以跨窗口和计算机启动、发送消息并相互操作。

**💡 核心亮点更新 (中文)**：
- **Facade 的所有设置都在一个文件中。** Facade 主目录中的 `facade.json` （默认为 `~/.facade/facade.json`）包含 `yolo`、`names` 和 `clis`。 **打开设置** 在 Facade Code 中打开编辑器的设置，并且 **在facade.json 中编辑** 打开文件，并在需要时创建它。完成、悬停帮助和检查都随之而来。保存适用于随后启动的代理。
- **您自己的 CLI。** 使用其他名称添加内置程序，例如通过“env”在另一个与 Anthropic 兼容的 API 上添加 Claude Code，或通过“args”使用带有配置文件的 Codex，或者使用“type: "custom"”的任何其他程序。另一个名称下的内置保留了 CLI 的工具、文件夹信任、状态、恢复和 Pin，因此另一个 API 密钥上的 Codex 不再显示红点。新文件列出了每个内置函数的每个字段，并带有注释示例。
- **文件中的错误表明它们在哪里。** 文件错误会停止每次启动并命名其行和列，并提供通往文件的路径。一个条目中的错误只会导致该条目不可用。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
- **All of Facade's settings are in one file.** `facade.json` in the Facade home (`~/.facade/facade.json` by default) holds `yolo`, `names` and `clis`. **Open Settings** opens the editor's Settings at Facade Code, and **Edit in facade.json** opens the file, creating it if needed. Completion, hover help and checks come with it. A save applies to agents started afterwards.
- **CLIs of your own.** Add a built-in under another name, such as Claude Code on another Anthropic-compatible API through `env` or Codex with a profile through `args`, or any other program with `type: "custom"`. A built-in under another name keeps that CLI's tools, folder trust, status, Resume and Pin, so Codex on another API key no longer shows a red dot. The new file lists every field of each built-in and has commented examples.
- **Mistakes in the file say where they are.** A file error stops every start and names its line and column, with a way to the file. An error in one entry makes only that entry unavailable.
- **Icons for every CLI.** Six CLI logos and 16 Facade robots, shown in New Agent, Resume, Go to Agent, cards and terminal tabs. In the panel, the robots look toward the pointer; where your system reduces motion they stay still.
- **Your 0.1.2 settings move over.** The first read writes them into a new `facade.json`, never over an existing one, and says once what moved. The old settings show as deprecated.
- **Facade: Home** chooses the Facade home, ahead of `FACADE_HOME` and `~/.facade`. The 14
```
</details>

---
### 📦 [GoogleChrome/modern-web-guidance](https://github.com/GoogleChrome/modern-web-guidance)
`⭐ Stars: 7,332` &nbsp;|&nbsp; `💻 语言: Other` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.0.0](https://github.com/GoogleChrome/modern-web-guidance/releases/tag/v1.0.0) (2026-11-10)`

> **简介**：让您的编码代理了解最新的网络最佳实践

**💡 核心亮点更新 (中文)**：
* **代码库现代化扫描器（`legacy-scan`）**：`npx Modern-web-guidance Legacy-scan [path]` 静态检测旧版 Web 平台模式，并将每个发现映射到具有现代替换的指南。它涵盖了当今大约 20% 具有确定性遗留规则的指南。 **[modern-web-guidance](https://github.com/GoogleChrome/modern-web-guidance/blob/v1.0.0/skills/modern-web-guidance/SKILL.md)** 技能为代理添加了匹配的 4 步工作流程：扫描、验证、报告、现代化。
* **更小、更快的搜索**：搜索现在在零依赖嵌入模型加上 BM25（而不是 TensorFlow.js）上运行。它仍然完全离线，npm 下载量从 23.5 MB 下降到 8.8 MB。
* **易失性功能选择加入（`set-allow-volatile-features`）**：过去 3 个月内发布或仍在稳定状态的单引擎功能指南保持可搜索，但“retrieve”需要明确的“.mwgrc”选择加入，与 Origin Trial 门控相匹配。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# Release Notes: `v1.0.0`

Modern Web Guidance is out of preview! Version 1.0 ships 203 use-case guides covering 250 web platform features, and the project is now stewarded by the Google Chrome, Microsoft Edge, Mozilla Firefox, and MDN teams alongside the web development community. Per-agent and per-guide eval results are public on the new [eval dashboard](https://googlechrome.github.io/modern-web-guidance-src/).

## 🛠️ CLI & Skill Updates

* **Codebase modernization scanner (`legacy-scan`)**: `npx modern-web-guidance@latest legacy-scan [path]` statically detects legacy web platform patterns and maps each finding to the guide with the modern replacement. It covers the roughly 20% of guides that have deterministic legacy rules today. The **[modern-web-guidance](https://github.com/GoogleChrome/modern-web-guidance/blob/v1.0.0/skills/modern-web-guidance/SKILL.md)** skill adds a matching 4-step workflow for agents: scan, verify, report, modernize.
* **Smaller, faster search**: Search now runs on a zero-dependency embedding model plus BM25 instead of TensorFlow.js. It is still fully offline, and the npm download drops from 23.5 MB to 8.8 MB.
* **Volatile feature opt-in (`set-allow-volatile-features`)**: Guides for single-engine features that shipped in the last 3 months or are still stabilizing stay searchable, but `retrieve` requires an explicit `.mwgrc` opt-in, matching Origin Trial gating.
* **Search query refinement in `SKILL.md`**: Agents now translate implied intent
```
</details>

---
### 📦 [Lee-xeo/Claude-Cage](https://github.com/Lee-xeo/Claude-Cage)
`⭐ Stars: 4,769` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.1.7](https://github.com/Lee-xeo/Claude-Cage/releases/tag/v0.1.7) (2026-11-11)`

> **简介**：Cage：为 Claude 特化的轻量化虚拟机，彻底杜绝网络泄露。多平台适配，支持多账号管理、远程部署、移动端操控。

**💡 核心亮点更新 (中文)**：
- **重新打开已有环境。** 基础模板缺失或安装未完成时，已有虚拟机仍可从自己的磁盘启动。创建或重置环境需要可用模板，重置会在停止或删除原环境之前完成这项检查。
- **下载大工具包。** 支持分段的服务器最多可用 4 个连接并行下载。中断后可以复用已保存的进度；服务器不支持分段时自动回退为单连接。下载完成后仍会校验整个文件。实际提速幅度取决于线路和服务器限速。
- **在终端使用 GitHub。** 新环境默认安装 GitHub CLI，已有环境更新工具后也可使用。在 Cage 终端运行 `gh auth login`，用自己的 GitHub 账号授权后即可按仓库权限处理提交、PR 和 Issue。[终端使用说明](https://lee-xeo.github.io/Claude-Cage/docs/workbench/)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# Cage v0.1.7

这是 Cage 的首个正式发行版。macOS、Windows 和 Linux 用户可以从[官网](https://lee-xeo.github.io/Claude-Cage/#download)选择安装包。Android 提供 arm64 APK，iPhone 用户可按[手机连接指南](https://lee-xeo.github.io/Claude-Cage/docs/mobile/)在 Xcode 中签名安装。

## 从候选版升级

先保存工作并退出 Cage，再安装对应系统的正式版。继续使用原有配置、账户和客机磁盘。打开工作台后，如果提示更新环境工具，可在“设置 → 环境版本”中完成更新。

- **重新打开已有环境。** 基础模板缺失或安装未完成时，已有虚拟机仍可从自己的磁盘启动。创建或重置环境需要可用模板，重置会在停止或删除原环境之前完成这项检查。
- **下载大工具包。** 支持分段的服务器最多可用 4 个连接并行下载。中断后可以复用已保存的进度；服务器不支持分段时自动回退为单连接。下载完成后仍会校验整个文件。实际提速幅度取决于线路和服务器限速。
- **在终端使用 GitHub。** 新环境默认安装 GitHub CLI，已有环境更新工具后也可使用。在 Cage 终端运行 `gh auth login`，用自己的 GitHub 账号授权后即可按仓库权限处理提交、PR 和 Issue。[终端使用说明](https://lee-xeo.github.io/Claude-Cage/docs/workbench/)
- **安装官方最新 Claude。** Claude Code 和 Claude Desktop 在实际下载安装时解析官方最新版本，已安装的更新版本会保留。下载或验证失败时可修复网络后重试，无需重建账户或环境。
- **切换代理节点。** 固定出口规则随所选节点保存。切换节点后，Cage 会核对该节点的出口，再恢复联网，避免把上一个节点绑定的地址用于新节点。
- **首次设置与恢复。** macOS 改进了项目文件夹授权窗口和固定出口确认流程。Windows 修复了安装接续时的注册助手超时，以及 Windows PowerShell 5.1 读取组件清单脚本失败的问题。
- **终端与客机画面。** 改进终端选区复制、Windows 主机连接 Linux 客机剪贴板、原生客机的光标显示与滚轮响应，并减少画面短暂停顿导致的重连。
- **Windows 画面与中文输入。** 改进 Desktop 在不同缩放比例下的显示、工具栏和中文输入；浏览器滚动时复用连续画面，减少重复截图。原生菜单在不同 Windows 显示缩放配置下的人工验收仍待补充。

发行附件包含桌面安装包、Android APK、对应源码归档和 `SHA256SUMS`。已有安装遇到问题时，请保留配置和客机磁盘，记录操作详情中的第一条错误。[故障排查](https://lee-xeo.github.io/Claude-Cage/docs/troubleshooting/) · [与 v0.1.7-rc.1 的源码对比](https://github.com/Lee-xeo/Claude-Cage/compare/v0.1.7-rc.1...v0.1.7)

## 已验证范围

所有安装包均由[同一源码提交](https://github.com/Lee-xeo/Claude-Cage/commit/9ade09f52981262916
```
</details>

---
### 📦 [duyunzhoudyz/dyz-gongwen-skills](https://github.com/duyunzhoudyz/dyz-gongwen-skills)
`⭐ Stars: 747` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.1.0](https://github.com/duyunzhoudyz/dyz-gongwen-skills/releases/tag/v1.1.0) (2026-11-04)`

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
`⭐ Stars: 22,708` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.3.0](https://github.com/vercel-labs/agent-desktop/releases/tag/v1.3.0) (2026-11-12)`

> **简介**：计算机使用 CLI 进行 AI 代理

**💡 核心亮点更新 (中文)**：
* 修复（macos）：解决本机菜单并通过 https://github.com/vercel-labs/agent-desktop/pull/376 验证生命周期转换
* perf(macos)：使用 libproc 读取应用程序进程清单，而不是在 https://github.com/vercel-labs/agent-desktop/pull/573 中生成 ps
* 文档：说每个本地帐户都可以通过 https://github.com/vercel-labs/agent-desktop/pull/589 到达 --cdp 端口

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## What's Changed
* fix(macos): resolve native menus and verify lifecycle transitions by @lahfir in https://github.com/vercel-labs/agent-desktop/pull/376
* perf(macos): read the app process inventory with libproc instead of spawning ps by @Railly in https://github.com/vercel-labs/agent-desktop/pull/573
* docs: say every local account can reach the --cdp port by @lahfir in https://github.com/vercel-labs/agent-desktop/pull/589
* fix: close reachable invalid state transitions in sessions, refs, trace, mcp and waits by @lahfir in https://github.com/vercel-labs/agent-desktop/pull/602
* Upgrade the docs to TypeScript 7 by @ctate in https://github.com/vercel-labs/agent-desktop/pull/622
* feat: add the sandbox command by @lahfir in https://github.com/vercel-labs/agent-desktop/pull/505
* feat(sandbox): add the macOS VM sandbox by @lahfir in https://github.com/vercel-labs/agent-desktop/pull/506
* test: run the post-action settle budget tests on the virtual clock by @lahfir in https://github.com/vercel-labs/agent-desktop/pull/642
* chore(release): 1.3.0 by @lahfir in https://github.com/vercel-labs/agent-desktop/pull/641


**Full Changelog**: https://github.com/vercel-labs/agent-desktop/compare/v1.2.0...v1.3.0
```
</details>

---
### 📦 [JimLiu/baocut](https://github.com/JimLiu/baocut)
`⭐ Stars: 1,760` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [baocut-v3.19.1-build.96](https://github.com/JimLiu/baocut/releases/tag/baocut-v3.19.1-build.96) (2026-11-11)`

> **简介**：BaoCut：具有可编辑时间线的人工智能视频代理。转录、字幕、翻译、配音、剪辑和动画。

**💡 核心亮点更新 (中文)**：
- 当 YouTube 在以“请求的格式不可用”结束之前报告登录检查、帐户 Cookie 过期或签名质询失败时，下载现在会因登录 (`LINK_LOGIN_REQUIRED`) 或工具更新 (`LINK_TOOL_UPDATE_REQUIRED`) 问题而失败，并显示原因，而不是将链接报告为不可用。原因会在长格式探测日志中保留下来，并且具体的最终错误（例如 HTTP 403 或超时）仍然优先。错误代码、浏览器选择和重试规则保持不变。 ([#137](https://github.com/JimLiu/baocut/pull/137) 作者：XiChuan9)
- 下载错误消息和详细信息中的链接经过更可靠的编辑，包括凭据中带有原始引号的链接以及因日志长度限制而被切断的链接。 ([来源](https://github.com/jimliu/baocut/commit/f72368098e9b8a02ac355dfa2552ab834ac2b30a))
- 顶级“baocut”帮助再次适合 40 行。 ([#136](https://github.com/JimLiu/baocut/pull/136))

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## BaoCut 3.19.1 (build 96)

### Video downloads
- When YouTube reports a sign-in check, expired account cookies or a failed n/signature challenge before ending with "Requested format is not available", the download now fails as a login (`LINK_LOGIN_REQUIRED`) or tool-update (`LINK_TOOL_UPDATE_REQUIRED`) problem and shows that cause, instead of reporting the link as unavailable. The cause survives long format-probe logs, and a concrete final error such as HTTP 403 or a timeout still takes priority. Error codes, browser selection and retry rules are unchanged. ([#137](https://github.com/JimLiu/baocut/pull/137) by XiChuan9)
- Links in download error messages and details are redacted more reliably, including links with raw quotes in their credentials and links cut off by the log length limit. ([source](https://github.com/jimliu/baocut/commit/f72368098e9b8a02ac355dfa2552ab834ac2b30a))

### Command line
- The top-level `baocut` help fits within 40 lines again. ([#136](https://github.com/JimLiu/baocut/pull/136))

### Requirements and verification limits
- macOS: Apple Silicon, macOS 14 or later; signed and notarized packages are published after native validation.
- Windows: unsigned packages; AVX2 and the Microsoft Visual C++ v14 x64 Redistributable are required. CUDA/Vulkan variants require compatible GPU drivers.
- ffmpeg/ffprobe and an agent engine remain external dependencies.
- Automated release checks do not cover full UI/export workflows, live model or GPU inference, live Yo
```
</details>

---
### 📦 [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)
`⭐ Stars: 21,712` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.1.154](https://github.com/milind-soni/OpenMausBot/releases/tag/v0.1.154) (2026-11-12)`

> **简介**：开源 Grok Bot 替代品，带有机器人可以使用的虚拟机

**💡 核心亮点更新 (中文)**：
- **三组，始终按相同顺序：**您所在的位置（此计算机或云）、您的帐户和此应用程序。每一页都说明了它的适用范围。
- **简单模式显示的页面较少。** 打开“设置”底部的高级模式即可查看其余内容。
- **一个 ​​AI 页面**，用于引擎、提供商密钥和模型。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## What's new in 0.1.154

### Settings, reorganised
- **Three groups, always in the same order:** the place you are in (This computer or a Cloud), Your account, and This app. Every page says what it applies to.
- **Simple mode shows fewer pages.** Turn on Advanced mode at the bottom of Settings to see the rest.
- **One AI page** for engines, provider keys and models.
- **Search settings** from the top of the window. A result names the page it lives on.
- **Phone & devices is in the profile menu,** so pairing a phone is two clicks from anywhere.

### Replies appear as they are written
- **A bot's reply now streams into the chat** instead of arriving all at once, in chats and in rooms.
- **Streamed text is shown as the bot produces it.** Saved secrets are masked once the message is saved, as before.

### Put a site or web app online
- **Publish to Netlify.** A bot can put a site or web app online on your own Netlify account.
- **Included hosting.** On a Cloud plan, a bot can publish to the hosting your plan includes, with no Netlify account of your own.
- **Published apps.** One page lists everything your bots have put online, with a preview beside the chat and Delete.

### Pairing a phone is clearer
- **Only the pairing code is a QR code now.** The desktop app no longer shows store codes or download links: install MausBot from the App Store or Google Play, then pair.
- **The pairing screen says what to scan with:** open MausBot on your phone and scan the code from inside the a
```
</details>

---
### 📦 [yuchen-ya/reelterminal](https://github.com/yuchen-ya/reelterminal)
`⭐ Stars: 25` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.4.3](https://github.com/yuchen-ya/reelterminal/releases/tag/v1.4.3) (2026-11-12)`

> **简介**：ReelTerminal — 您的 AI 视频的最后一站。具有共享人类/代理控制的代理本机视频整理编辑器。

**💡 核心亮点更新 (中文)**：
- 以图片为主的任务默认显示图片总览，支持按状态筛选、文件名搜索、自然排序、多选和 Shift 范围选择。
- 可以对明确选中的项目批量保留、返工或丢弃，也可先确认范围，再保留剩余待审图片。单次最多 1,000 项，不会静默拆成多个保存；失败不会产生部分批量决定。
- 批量决定支持整体撤销和重做；已有更新决定、源文件变化或口径变化时，会提示冲突并保留较新的状态。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# ReelTerminal 1.4.3

## 图片审阅

- 以图片为主的任务默认显示图片总览，支持按状态筛选、文件名搜索、自然排序、多选和 Shift 范围选择。
- 可以对明确选中的项目批量保留、返工或丢弃，也可先确认范围，再保留剩余待审图片。单次最多 1,000 项，不会静默拆成多个保存；失败不会产生部分批量决定。
- 批量决定支持整体撤销和重做；已有更新决定、源文件变化或口径变化时，会提示冲突并保留较新的状态。
- 批注和批量操作按当前选择显示。最近批注只填入草稿，不会代替人工确认。检查器支持查看原图、缩放和逐项继续。
- 缩略图按需加载，浏览总览不再为每张原图写入预处理副本。

这些操作属于真实文件夹中的当前审阅任务，不恢复已退役的实验性独立批次功能。丢弃决定不会删除原始文件。

## 使用与分发说明

- 模型分析仍需单独配置和明确授权；手动审阅不需要模型服务。
- 保存结果不确定时，先核对本次决定；已保存的决定不重复提交，确认未提交后才能显式重试。
- Windows x64 构建未签名，系统可能显示 SmartScreen 提示。升级前请备份项目及数据，参阅 [Windows 升级指南](https://github.com/yuchen-ya/reelterminal/blob/v1.4.3/docs/WINDOWS-UPGRADE.md)。
- 平台及下载以正式发行页实际资产为准；FFmpeg/ffprobe 等可选组件需另外配置，参阅 [外部依赖说明](https://github.com/yuchen-ya/reelterminal/blob/v1.4.3/docs/EXTERNAL-DEPENDENCIES.md)。

视频色彩仍限 SDR 8-bit。缺少完整色彩标记的素材，预览与导出可能出现色差；交付前应一起规范化素材像素与色彩标记并检查输出。暂不支持保持 HDR/10-bit 色彩，见 [色彩说明](https://github.com/yuchen-ya/reelterminal/blob/v1.4.3/docs/COLOR.md)。

## 视频编辑

- 修正软件渲染下，带完整 BT.709 标记的 SDR 视频饱和色偏差，覆盖预览、缩略图和导出。
- 从导出界面返回目录时关闭残留遮罩，避免遮挡视频预览。

软件渲染需要额外的 CPU 运算，高分辨率视频不保证实时播放。

## Changes

- Add an image-first review grid with natural filename sorting, filtering, search, explicit selection and Shift ranges.
- Save up to 1,000 selected decisions together, with batch undo/redo and conflict checks that preserve newer state.
- Keep recent-note reuse separate from decision confirmation and load visible thumbnails without generating preprocessing copies for every original.
- Inspect original pixels on demand and continue through individual images.
-
```
</details>

---
### 📦 [KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)
`⭐ Stars: 4,763` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.8.2](https://github.com/KKKKhazix/agent-autoloop/releases/tag/v1.8.2) (2026-11-12)`

> **简介**：让你的命令行 Agent 在后台自己接活、自己跟进到底；平时不烦你，遇到拿不准的事才发卡片找你拍板。

**💡 核心亮点更新 (中文)**：
- ZCode 支持：内置 ZCode 代理适配器；读取停止在对象中间的 ZCode 输出不再挂起。
- 规则可以设置一个可选的会话“标题”，放在提示的第一行，这样在第一条消息之后命名会话的客户端就可以区分运行。
- 规则暂停时跳过的事件现在可见并且可以重播：“resume”和“status”列出了它们，并且有一个新的“agent-autoloop replay <rule> --since <time>”（也通过 HTTP 和 MCP）。打印的重播命令与复制的一样工作，包括 Windows。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 更新内容

- 新增 ZCode 接单：内置 ZCode Agent 适配器；ZCode 输出停在对象中间时，读取不再卡住。
- 规则可以写可选的会话标题 `title`，放在提示词第一行，按第一条消息给会话起名的客户端能分清每个事项。
- 暂停期间跳过的事件现在看得到、能补跑：`resume` 和 `status` 会列出暂停期间跳过的事件，新增 `agent-autoloop replay <规则> --since <时间>`（也有接口和 MCP 版本）。打印的补跑命令照抄就能用，Windows 上也一样。
- 交付：GitHub 的检查一直排队不动时，自动重新触发一次；仍不动就立刻退回并说明原因，不再白等两个多小时。
- 交付：修复复查会话的归属和交付终态。
- 协议文档补上 healthz 和 state 的两个字段。

感谢 Flandern1211、sweetpotato222、argszero 的贡献。

## What's changed

- ZCode support: a built-in ZCode agent adapter; reading ZCode output that stops in the middle of an object no longer hangs.
- Rules can set an optional session `title`, put on the prompt's first line, so clients that name a session after its first message can tell runs apart.
- Events skipped while a rule was paused are now visible and can be replayed: `resume` and `status` list them, and there is a new `agent-autoloop replay <rule> --since <time>` (also over HTTP and MCP). The printed replay command works as copied, Windows included.
- Delivery: when GitHub leaves a check queued with no jobs, it is re-triggered once; if it still doesn't start, the PR is handed back at once with the reason instead of waiting over two hours.
- Delivery: fixed which session a follow-up review belongs to, and delivery end states.
- The protocol now documents two more fields of healthz and state.

Thanks to Flandern1211, sweetpotato222 and argszero.
```
</details>

---
### 📦 [alchaincyf/huashu-motion](https://github.com/alchaincyf/huashu-motion)
`⭐ Stars: 2,671` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.4.0](https://github.com/alchaincyf/huashu-motion/releases/tag/v0.4.0) (2026-11-09)`

> **简介**：让你的agent一键直出商业级产品宣传片：会作曲，能指着画面改。Commercial-grade launch films by your coding agent — point at the frame to change it.

**💡 核心亮点更新 (中文)**：
- 新增一条路径：片子已经做完、检查全过，但看着平，想让配乐、节奏、动效好很多。导演会先用数字写诊断（每秒运动量、哪几段是同一种版式、配乐哪里薄），保住创意和已确认的文案，再重做镜头和总谱。方法在 `references/punch-up.md`。
- SKILL.md 开头改成先讲标准：三个检验（是不是这个产品、能量有没有形状、有没有哪段像幻灯片）、任务分流表、哪些闸门是写死的、闸门之间哪些可以放开做。
- 把整支成片按每秒 4 帧铺成几张接触表，一眼看出哪段不动、哪几段是同一种版式换了内容、哪一帧停在半路很难看。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 这一版改了什么

**已有的片子可以「提级」了**
- 新增一条路径：片子已经做完、检查全过，但看着平，想让配乐、节奏、动效好很多。导演会先用数字写诊断（每秒运动量、哪几段是同一种版式、配乐哪里薄），保住创意和已确认的文案，再重做镜头和总谱。方法在 `references/punch-up.md`。
- SKILL.md 开头改成先讲标准：三个检验（是不是这个产品、能量有没有形状、有没有哪段像幻灯片）、任务分流表、哪些闸门是写死的、闸门之间哪些可以放开做。

**新命令 `om qa --sheet`**
- 把整支成片按每秒 4 帧铺成几张接触表，一眼看出哪段不动、哪几段是同一种版式换了内容、哪一帧停在半路很难看。

**修了四个会影响成片的问题**
- 总谱里的转调 `[K:]` 会漏到后面的声部，让它们从第一小节起就在错的调上。现在转调从它所在的那一拍起对所有声部生效，写一次即可。用到转调的旧谱重新 `om sound` 后，和声会变成正确的音。
- `om sound` 会报出拍数对不上的小节和提前结束的声部。这项检查在自带的两份示例谱和两个风格小样里查出四处错，已修。
- `OM.clock` 的逐帧回调改在整帧动画算完之后执行，回调里可以读元素的实际位置；跟随某个元素的选区框、光标、高亮不再慢一帧或错位。旧项目把 `runtime/om.js` 复制到自己的 `vendor/om.js` 才生效。
- `om render` 的版本号取现有最大值加一。删掉过 v1–v3、留着 v4 时，新渲染是 v5，不再回填成 v1。

## 怎么更新

```bash
git pull --ff-only
```

---

**Punch-up**: a path for making an existing, correct-but-flat film much better (diagnose with numbers, keep the idea and the approved words, rebuild the shots and the score), in `references/punch-up.md`; SKILL.md now opens with the bar, three tests, a job table and the fixed gates. **`om qa --sheet`** tiles the whole render at 4 frames a second. **Fixes**: an inline `[K:]` holds from its beat for every voice and no longer leaks into the next voice (scores that change key will sound different, and right, after `om sound`); `om sound` warns about bars that do not add up (four fixed in the shipped examples); `OM.clock` draws after every tween of the frame on a seek (copy `runtime/om.js` over an old project's `vendor/om.js`); `om render` numbers the next output one
```
</details>

---
### 📦 [wquguru/cicada](https://github.com/wquguru/cicada)
`⭐ Stars: 2,196` &nbsp;|&nbsp; `💻 语言: Swift` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.9.0](https://github.com/wquguru/cicada/releases/tag/v1.9.0) (2026-11-12)`

> **简介**：知了 Cicada · 任何会议和直播的实时字幕、同声传译、AI 会议纪要，Mac、Windows、Linux、Android 免费开源。Live subtitles, interpreting and meeting notes for any call or stream, on Mac, Windows, Linux and Android.

**💡 核心亮点更新 (中文)**：
- 录音播放时，正在播放的整行都会亮起，然后单击该行上的任意位置即可播放 ([4e0aa4f](https://github.com/wquguru/cicada/commit/4e0aa4f7685ed57cbaf0ded0d684afade8f4d904))
- Notes可以使用自己的模型，或另一个具有自己的地址和密钥的OpenAI兼容服务（[21642b9](https://github.com/wquguru/cicada/commit/21642b9bf74e0623d6bdbaee9cb04b150f5c8b3e))
- 口译可以免提运行：Cicada 听会议时，只需开始说话，翻译会在一秒钟的暂停后停止 ([a44d0e8](https://github.com/wquguru/cicada/commit/a44d0e8b8abdabe8bf6445ab1f4adaf8303555ca))

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
### Mac

#### New

- While a recording plays back, the whole line being played lights up and a click anywhere on a line plays from there ([4e0aa4f](https://github.com/wquguru/cicada/commit/4e0aa4f7685ed57cbaf0ded0d684afade8f4d904))
- Notes can use their own model, or another OpenAI-compatible service with its own address and key ([21642b9](https://github.com/wquguru/cicada/commit/21642b9bf74e0623d6bdbaee9cb04b150f5c8b3e))
- Interpreting can run hands-free: while Cicada listens to a meeting, just start talking and the translation goes out after a one-second pause ([a44d0e8](https://github.com/wquguru/cicada/commit/a44d0e8b8abdabe8bf6445ab1f4adaf8303555ca))
- After each meeting, notes and transcript can be saved as Markdown into a folder you pick, such as an Obsidian vault ([3b48808](https://github.com/wquguru/cicada/commit/3b488088d89396d851520db7d1dfa8ac8711787f))

#### Fixed

- A short reply in a voice not yet known no longer joins the answer before it in the live transcript ([ab787d4](https://github.com/wquguru/cicada/commit/ab787d4ad960da95b62e0fc4cf9731b15948cc4d))
- The meeting record no longer moves a word from one speaker's sentence into the next speaker's line ([4cb8512](https://github.com/wquguru/cicada/commit/4cb8512b0d2b587a16b30046198bf57462bcee3b))
- What you say with the talk key while the other side talks is no longer dropped as silence ([3c6bb56](https://github.com/wquguru/cicada/commit/3c6bb56db093f30ddf595500f3ae6a022dab280c))
- Cicada no longer quits when
```
</details>

---
### 📦 [openai/codex](https://github.com/openai/codex)
`⭐ Stars: 135,050` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [rust-v0.167.2](https://github.com/openai/codex/releases/tag/rust-v0.167.2) (2026-11-11)`

> **简介**：在您的终端中运行的轻量级编码代理

**💡 核心亮点更新 (中文)**：
- Codex 现在默认在 Google Cloud Vertex AI 上增量发送工具更新。要选择退出，请在“config.toml”中的“[features]”下设置“incremental_tools_legacy_gcp = false”。 （[#60617]（https://github.com/openai/codex/pull/60617），[#60848]（https://github.com/openai/codex/pull/60848））

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## New Features

- Codex now sends tool updates incrementally by default on Google Cloud Vertex AI. To opt out, set `incremental_tools_legacy_gcp = false` under `[features]` in `config.toml`. ([#60617](https://github.com/openai/codex/pull/60617), [#60848](https://github.com/openai/codex/pull/60848))

## Changelog

Full Changelog: https://github.com/openai/codex/compare/rust-v0.167.1...rust-v0.167.2
```
</details>

---
### 📦 [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)
`⭐ Stars: 15,748` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.4.5](https://github.com/akitaonrails/ai-memory/releases/tag/v3.4.5) (2026-11-10)`

> **简介**：用于代理编码 CLI 的长期记忆解决方案，并促进不同代理供应商之间的切换

**💡 核心亮点更新 (中文)**：
校验和 (SHA256)
````
897759e08968b146405d53e5417653f1b5d28ea4254baba1bb5b6d3a367411b4 ai-内存-3.4.5-1.aarch64.rpm
14755b246e52a8c5969c1cea094d08002d8fe9e85924dae744858930efb33a0b ai-内存-3.4.5-1.x86_64.rpm
28862a1b83331ca71af1e526313672df340a

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Checksums (SHA256)
```
897759e08968b146405d53e5417653f1b5d28ea4254baba1bb5b6d3a367411b4  ai-memory-3.4.5-1.aarch64.rpm
14755b246e52a8c5969c1cea094d08002d8fe9e85924dae744858930efb33a0b  ai-memory-3.4.5-1.x86_64.rpm
28862a1b83331ca71af1e526313672df340aca4de9aab2ecb82ed755b3ce7126  ai-memory-claude-plugin.zip
a1199c3a9602590d71dd15d5efb3cbd1ffa1ca3a20ae635b85b2a44f060c6788  ai-memory-hooks.tar.gz
5b8b9030c247b091ac2bacbf181f52f8fdba9d4ed47cdef23faab874d4c94d9f  ai-memory-install-hooks
956439346e5f67a743c242f82424e1a29227db971158116c5a0fe3bc185aa41f  ai-memory-linux-aarch64.tar.gz
43af583f2c1c22949cecc89ad99027a076bd2510d7ba3dabff04e735e03eab76  ai-memory-linux-x86_64.tar.gz
7b5fd2fc39dca4b5e7a098fe49b411d849c770f1ba125b85a562c08ad2cd3ad6  ai-memory-macos-aarch64.tar.gz
6b5e885f61491a0dda0b6989e8d89f6a546354a635c4044eb87742dd30d54471  ai-memory-macos-x86_64.tar.gz
2166ba0cdd2e65029bd2350fe256abb97c9dbb7a346d8f588b625ae7527acef3  ai-memory-windows-x86_64.zip
6a91c44ffa2e85d3b5a6ce26a4ccff0286b91d08d276d2bb4d47c346b036ee8b  ai-memory-wrapper.cmd
5e405aa237a2399f13084f71ae89545cbca77683c8251b4c4572cb51aedc8de4  ai-memory-wrapper.ps1
982cfeb1515a062fdb348e4622d130682660d30a1ce104d8ff0a11d997d409a7  ai-memory-wrapper
c05aedd9a572d5807986910d5099adac132ae558d677bc2d0f64a6d53eaf0d3b  install.ps1
e54ceb55bce61c3b541caa99444f6ec18562d19de1aa15a87fb3ab32897885b3  install.sh
```

## Install
```bash
# Linux/macOS, no root: checksum-verified release binary under ~/.local, then one-step set
```
</details>

---
### 📦 [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)
`⭐ Stars: 58,651` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.7.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.7.2) (2026-11-06)`

> **简介**：DeepTutor：终身个性化辅导。 https://deeptutor.info/。

**💡 核心亮点更新 (中文)**：
- **完整应用程序：** 停止 DeepTutor 并备份运行时主目录，然后运行 ​​`python -m pip install --upgrade "deeptutor[full]==1.7.2"`。保持相同的`DEEPTUTOR_HOME`；在重新启动之前使用“python -m pip check”和“deeptutor module list”进行验证。任何附加功能轮也必须匹配版本 1.7.2。
- **旧版安装：** 从 1.6.15 或更早版本升级必须先卸载旧版 `deeptutor-cli` 软件包，然后再安装模块化软件包系列。按照 [v1.7.0](past_releases/ver1-7-0.md) 中的迁移命令进行操作。
- **源安装：**安装 `requirements/full.txt`，然后安装 `python -m pip install -e 。 --无部门`。在更改模块之前停止活动服务器和 CLI 轮流。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# DeepTutor v1.7.2 Release Notes

**Release Date:** 2026.11.06

Building on [v1.7.1](ver1-7-1.md), v1.7.2 adds selected-text read-aloud, easier model setup, and more reliable guided learning, retrieval, and updates. Desktop releases now require Apple Silicon and Intel Mac installers alongside both Windows downloads.

## What's New

### Complete desktop downloads and sturdier Windows support

GitHub Releases provide Apple Silicon and Intel DMGs, a Windows installer, and a Windows portable ZIP. The release workflow checks every platform and all versioned downloads and stable aliases. Windows fixes cover session and migration locks, plugin environments, Python executable discovery, non-UTF-8 output, and paths containing spaces.

### Read just the passage you need

Select text in Chat, Mastery Path, or Reading and choose **Read aloud** to hear it through your configured speech provider. Chat read-aloud also remembers playback speed per conversation in the current browser. Voice rendering handles escaped percent signs and degree notation more naturally, and Video Lesson's Edge fallback selects a voice matching the lesson language.

### Easier provider setup and broader compatibility

Settings discovers available models after credential edits and lets you import several at once. New custom providers default to automatic protocol selection. NVIDIA NIM adds text retrieval embeddings with distinct query and passage roles; newer DashScope image models use their matching generation prot
```
</details>

---
### 📦 [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)
`⭐ Stars: 111,354` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.6.1](https://github.com/Panniantong/Agent-Reach/releases/tag/v1.6.1) (2026-11-01)`

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
`⭐ Stars: 12` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.3.4](https://github.com/Hsiung-Shao/exile-appraiser/releases/tag/v0.3.4) (2026-10-30)`

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
### 📦 [microsoft/skill-recorder](https://github.com/microsoft/skill-recorder)
`⭐ Stars: 5,775` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.9.2](https://github.com/microsoft/skill-recorder/releases/tag/v0.9.2) (2026-11-12)`

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
`⭐ Stars: 71,321` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.8.3](https://github.com/Ebony-Vinyl/dsh-our-free-model/releases/tag/v2.8.3) (2026-11-08)`

> **简介**：在 dsh 里装上这个插件即可，无需登录、注册或填 API Key，就能使用包括 DeepSeek V4.1 Flash、Kimi K3 在内的前沿模型——完全免费，不限量。 All you do is install this plugin in dsh: no login, no sign-up, no API key — the frontier models are just there, DeepSeek V4.1 Flash and Kimi K3 among them. Completely free, with no usage cap.

**💡 核心亮点更新 (中文)**：
- 引擎整体跟上上游修复(pin `6a900e0d` → `eef99e4`):两屏引导会被自动应答,TUI 交互模式恢复可用——订阅额度按交互模式的 `cli` 入口计费,比 `-p` 的 `sdk-cli` 省近一半。
- 升级时自动清掉旧版本留下的失败退避标记:升级完立即可用,不用等退避期过夜。
- 端到端验证:全新引导环境连跑 3 次,3/3 完整跑通(TUI 起来、消息发送、流式回复)。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 修复

### Claude 订阅 TUI 交互模式卡 45 秒后回退 -p(根治)

新版 Claude Code(2.1.316+)首次运行多了一屏「安全须知,按回车继续」和「终端设置,按 Esc 跳过」。旧引擎不认识这两屏:Claude 等按键、引擎等输入提示符,两边互等 45 秒后放弃并退回 `-p`;连续失败还会进入最长 24 小时"直接走 -p"的退避——这就是「claude 的 tui 用不了,只能用 p」的根因。

- 引擎整体跟上上游修复(pin `6a900e0d` → `eef99e4`):两屏引导会被自动应答,TUI 交互模式恢复可用——订阅额度按交互模式的 `cli` 入口计费,比 `-p` 的 `sdk-cli` 省近一半。
- 升级时自动清掉旧版本留下的失败退避标记:升级完立即可用,不用等退避期过夜。
- 端到端验证:全新引导环境连跑 3 次,3/3 完整跑通(TUI 起来、消息发送、流式回复)。

### 发布套件

- 引擎增大后发布清单曾溢出到 81 个文件(旧升级器硬上限 80,会让老版本用户拒绝安装),现按需用 zopfli 重压回 7×4 MiB 预算——仍是标准 gzip,校验逻辑不变。
- 修复发布套件夹具服务器的 keep-alive 竞态(大下载后的检查耗尽 Node 默认 5 秒空闲超时导致 ECONNRESET)。

## 上游同步

magpie 引擎 8 天上游全部跟进,含 5 个 claudetui 修复与 +3 内置预设(LongCat / Volcengine Ark Decision / Voyage)。

## 安装

- npm:`dsh plugin --profile <profile> add @ebony-vinyl/dsh-our-free-model@2.8.3`
- 本地 tarball:`dsh-our-free-model-2.8.3.tgz`(与本 Release 同源同版本)
- 应用内:设置 → 插件升级,一键升级
- npm 上那个裸名 `dsh-our-free-model` 仍是第三方打包,请勿安装。

**全量校验**:115/115 套件通过;发布清单 80 文件、34,036,022 字节,Ed25519 签名有效;1.3.1/2.5.9 真实升级器完成真实下载安装验收。
```
</details>

---
### 📦 [hypit-ai/hypit](https://github.com/hypit-ai/hypit)
`⭐ Stars: 29,548` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.3.2](https://github.com/hypit-ai/hypit/releases/tag/v0.3.2) (2026-11-11)`

> **简介**：使用人工智能代理克隆任何病毒视频。不仅仅是一个脚本，而是整个工作流程：交换面孔、文字、幕后花絮，在一个命令中发送 100 个变体，并获得 1 亿次观看。

**💡 核心亮点更新 (中文)**：
- 添加 Bach 1.0 Pro 作为默认 Hypit 依赖项，包含文本、框架和参考 SVML 表面并通过 HypiHub 生成。仅最后一帧的生成需要 4K。参考图像、视频和音频都可以设置“开始时间”偏移量。
- HypiHub 上的 PixVerse V6 接受“种子”和“多剪辑”。 `aspect-ratio="auto"` 需要至少一个视频参考，并且 `multi-clip` 不能与视频参考组合。
- 添加可嵌入的 HTML 文档输出并与 Studio 共享 HTML 播放处理。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Install or update with `npm install -g @hypit/hypit@0.3.2`.

- Add Bach 1.0 Pro as a default Hypit dependency, with text, frame, and reference SVML surfaces and generation through HypiHub. Last-frame-only generation requires 4K. Reference images, videos, and audio can each set a `start-time` offset.
- PixVerse V6 on HypiHub accepts `seed` and `multi-clip`. `aspect-ratio="auto"` requires at least one video reference, and `multi-clip` cannot be combined with video references.
- Add embeddable HTML document output and share HTML playback handling with Studio.
- Reuse video frames when they already satisfy media normalization requirements.

The release includes `@hypit/bach@0.1.0`, `@hypit/pixverse@0.2.1`, `@hypit/provider-hypihub@0.2.1`, `@hypit/video@0.2.1`, `@hypit/html-document@0.1.0`, `@hypit/html-program@0.1.1`, `@hypit/studio@0.2.1`, and `@hypit/media-local@0.2.1`.

Repository checks and package verification passed on Linux and Windows.
```
</details>

---
### 📦 [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app)
`⭐ Stars: 21,570` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.0.10](https://github.com/HBAI-Ltd/Toonflow-app/releases/tag/v2.0.10) (2026-11-05)`

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
`⭐ Stars: 455,285` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [rea-agents-6.9.0](https://github.com/morluto/rea/releases/tag/rea-agents-6.9.0) (2026-11-12)`

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
`⭐ Stars: 17,276` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v4.0.11](https://github.com/chatfire-AI/huobao-drama/releases/tag/v4.0.11) (2026-11-05)`

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
`⭐ Stars: 35,413` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.1.3961](https://github.com/yetone/magpie/releases/tag/v0.1.3961) (2026-11-13)`

> **简介**：每个代理的模型。一处。来自菜单栏的 DeepSeek 上的 Codex、Kimi 上的 Claude Code。

**💡 核心亮点更新 (中文)**：
- 添加了英语、中文和日语版本的 API 中继页面。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Features
- Added an API relay page available in English, Chinese, and Japanese.

## Improvements
- Optimized model provider listings to share a single copy of each provider.

### Install

Download from [usemagpie.ai](https://usemagpie.ai), or `curl -fsSL https://usemagpie.ai/install.sh | sh`. An installed magpie updates itself.

- **macOS (Apple Silicon):** `magpie-darwin-arm64.dmg`
- **macOS (Intel):** `magpie-darwin-amd64.dmg`
- **Windows:** `magpie-windows-amd64.exe` (ARM: `magpie-windows-arm64.exe`)
- **Linux:** `magpie-linux-amd64` / `magpie-linux-arm64` (needs GTK 3 and WebKitGTK 4.1)
- **Terminal only:** `magpie-cli-<os>-<arch>`

<!-- lang:zh -->

## 功能
- 新增了一个提供英语、中文和日语版本的 API 中转页面。

## 改进
- 优化了模型提供商列表，使每个提供商共享一个单一副本。

### 安装

从 [usemagpie.ai](https://usemagpie.ai) 下载，或运行 `curl -fsSL https://usemagpie.ai/install.sh | sh`。已安装的 magpie 会自动更新。



---
The same release, and the feed magpie updates from: https://github.com/yetone/magpie-releases/releases/tag/v0.1.3961
```
</details>

---
### 📦 [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
`⭐ Stars: 262,971` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.23.1](https://github.com/NousResearch/hermes-agent/releases/tag/v0.23.1) (2026-11-10)`

> **简介**：与您共同成长的代理商

**💡 核心亮点更新 (中文)**：
- Microsoft Store 应用程序：通过商店更新。
- 从安装程序安装的桌面应用程序（.exe / .dmg）：此版本中没有变化；它会随着下一个捆绑版本的更新而更新。
- CLI：`hermes update`，或重新运行安装程序一行。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# Hermes Agent v0.23.1

**Release Date:** November 9, 2026

> Patch release. This tag rolls up the ~618 PRs merged since v0.23.0 into a stable release for the GitHub release (CLI and installers), the Microsoft Store app, Docker and Hermes Cloud. Full curated notes for this window ship with v0.24.0.

**What this patch ships for plugin users:** since the plugin catalog's site deploy on November 9, the published `plugin-catalog.json` was larger than the 2 MiB cap clients accept, so every install silently fell back to the catalog it shipped with. `hermes plugins install <name>` could not find plugins added since your last update, installed the pin your release shipped instead of the current one, and missed newer `removed` entries. This release raises the cap to 16 MiB, so the live catalog is used again ([#151860](https://github.com/NousResearch/hermes-agent/pull/151860), fixes [#151856](https://github.com/NousResearch/hermes-agent/issues/151856), thanks @100yenadmin). Installs that stay on v0.23.0 or older keep falling back until they update.

<!-- HERMES_BUILDS_TABLE -->

## About this release

Measured at commit `3b421578588`, the window since v0.23.0 contains **2,578 non-merge commits** across **2,781 changed files** (+151,690 / −62,595), **618 merged PRs** and **409 closed issues**.

Also in the window, undocumented here on purpose: Esc backtrack in the TUI and classic CLI (replacing the rewind list picker), group chats that run on a gateway without Desktop and can seat bots
```
</details>

---
### 📦 [Makememo/MemoAI](https://github.com/Makememo/MemoAI)
`⭐ Stars: 1,082` &nbsp;|&nbsp; `💻 语言: Other` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.8.10](https://github.com/Makememo/MemoAI/releases/tag/v1.8.10) (2026-11-03)`

> **简介**：MemoAI 视频翻译文本、字幕和注释变得简单。

**💡 核心亮点更新 (中文)**：
- 添加了 Sherpa ONNX 和 CrispASR 转录引擎支持

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## New Features

- Added Sherpa ONNX and CrispASR transcription engine support

## Improvements

- Improved folder management with model folder migration and a reworked model management UI
- Unified the player presentation
- Improved ASS subtitle rendering performance
```
</details>

---
### 📦 [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)
`⭐ Stars: 12,249` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.13.18](https://github.com/genspark-ai/genoffice/releases/tag/v0.13.18) (2026-11-12)`

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
`⭐ Stars: 25,476` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [@pascal-app/cli@1.1.4](https://github.com/pascalorg/editor/releases/tag/%40pascal-app/cli%401.1.4) (2026-11-12)`

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
### 📦 [librepods-org/librepods](https://github.com/librepods-org/librepods)
`⭐ Stars: 30,725` &nbsp;|&nbsp; `💻 语言: Kotlin` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.0.4](https://github.com/librepods-org/librepods/releases/tag/v1.0.4) (2026-10-16)`

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
`⭐ Stars: 41,347` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.15.2](https://github.com/linshenkx/prompt-optimizer/releases/tag/v2.15.2) (2026-11-09)`

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
`⭐ Stars: 39,283` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [desktop/v1.17.0](https://github.com/RSSNext/Folo/releases/tag/desktop/v1.17.0) (2026-11-02)`

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
`⭐ Stars: 51,602` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [0.31.7](https://github.com/roboflow/supervision/releases/tag/0.31.7) (2026-11-11)`

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
`⭐ Stars: 35,726` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.19.34](https://github.com/MetaCubeX/mihomo/releases/tag/v1.19.34) (2026-11-11)`

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
`⭐ Stars: 158,025` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.5.10](https://github.com/clash-verge-rev/clash-verge-rev/releases/tag/v2.5.10) (2026-11-03)`

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
`⭐ Stars: 79,400` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.1.917-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.917-beta) (2026-11-11)`

> **简介**：用于运行和训练法学硕士和扩散模型的本地 UI。支持 GGUF、MLX、Qwen3.8、DeepSeek-V4.1、MiniMax-H3、Gemma 4、FLUX 等。

**💡 核心亮点更新 (中文)**：
- **新 Qwen3.8-27B** 动态 v3.1 GGUF。
- **更快的聊天：** 对流式传输、滚动、菜单和对话框的性能进行了重大改进，尤其是在长时间对话中。
- **更光滑的玻璃：** 减少打字、滚动和生成时的延迟。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Qwen3.8-27B is here with Dynamic v3.1 GGUFs, ready to run locally with Unsloth. This release also brings major performance improvements, smoother Glass rendering, revamped code blocks and Thinking UI, HTML/PDF chat exports, and new image generation and coding agent features.

## Highlights
- **New Qwen3.8-27B** Dynamic v3.1 GGUFs.
- **Faster chats:** Major performance improvements to streaming, scrolling, menus and dialogs, especially in long conversations.
- **Smoother Glass:** Reduced lag while typing, scrolling and generating.
- **Revamped code blocks and Thinking:** Independently scrolling, expandable panels with improved syntax highlighting.
- **HTML and PDF exports:** Export chats directly from the chat menu.
- **Image queue:** Queue upcoming image generations while another is rendering.
- **Claude Code and Codex on MLX:** Run coding agents with MLX models through `unsloth start`.

## Chat & UI

- Streaming performance no longer degrades as conversations grow.
- Smoother scrolling with background images, with or without Glass.
- Faster menus, dialogs and browser pane loading.
- Read aloud starts after the first sentence instead of waiting for the entire response.
- Chat preferences, time format and spell check now sync with your account.

## Images & Video

- FLUX.2 and FLUX.3 use **36–43% less VRAM** during image decoding at the same speed.
- Queue image generations from the Images page or API.
- INT8 and FP8 image models now load on older NVIDIA
```
</details>

---
### 📦 [arc53/DocsGPT](https://github.com/arc53/DocsGPT)
`⭐ Stars: 18,375` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [1.1.0](https://github.com/arc53/DocsGPT/releases/tag/1.1.0) (2026-10-25)`

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
`⭐ Stars: 85,170` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.3.3](https://github.com/lobehub/lobehub/releases/tag/v2.3.3) (2026-11-12)`

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
`⭐ Stars: 33,959` &nbsp;|&nbsp; `💻 语言: Dart` &nbsp;|&nbsp; `🏷️ 最新版本: [v5.5.5](https://github.com/hiddify/hiddify-app/releases/tag/v5.5.5) (2026-11-04)`

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
`⭐ Stars: 30,033` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v4.17.4](https://github.com/labring/FastGPT/releases/tag/v4.17.4) (2026-11-05)`

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
`⭐ Stars: 9,937` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.3.2](https://github.com/yihong0618/bilingual_book_maker/releases/tag/v1.3.2) (2026-10-30)`

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
`⭐ Stars: 37,444` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.5.1](https://github.com/1Panel-dev/1Panel/releases/tag/v2.5.1) (2026-11-12)`

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
`⭐ Stars: 29,079` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v6.14.4](https://github.com/invoke-ai/InvokeAI/releases/tag/v6.14.4) (2026-11-03)`

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
`⭐ Stars: 39,646` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.0.2](https://github.com/The-Vibe-Company/quivr/releases/tag/v2.0.2) (2026-10-30)`

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
`⭐ Stars: 161,059` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [1.19.0](https://github.com/langgenius/dify/releases/tag/1.19.0) (2026-11-04)`

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
`⭐ Stars: 25,045` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.6.55](https://github.com/nextai-translator/nextai-translator/releases/tag/v0.6.55) (2026-11-02)`

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
`⭐ Stars: 149,421` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [langchain-core==1.8.0](https://github.com/langchain-ai/langchain/releases/tag/langchain-core%3D%3D1.8.0) (2026-11-11)`

> **简介**：代理工程平台。

**💡 核心亮点更新 (中文)**：
**`langchain-core` 1.8.0 放弃了对 Python 3.10 的支持**，该版本已终止生命周期。现在支持的最低版本是 Python 3.11。 Python 3.10 上的用户将继续解析“langchain-core”1.7.x。

自 langchain-core==1.7.7 以来的变化

相对

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
**`langchain-core` 1.8.0 drops support for Python 3.10**, which has reached end-of-life. The minimum supported version is now Python 3.11. Users on Python 3.10 will continue to resolve `langchain-core` 1.7.x.

Changes since langchain-core==1.7.7

release(core): 1.8.0 (#41796)
feat(core): Remove EOL Python 3.10 support (#41267)
feat(core): add decision models (#41765)
```
</details>

---
### 📦 [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)
`⭐ Stars: 188,013` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [autogpt-platform-beta-v0.11.2](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.11.2) (2026-11-11)`

> **简介**：AutoGPT 的愿景是为每个人提供易于使用和构建的人工智能。我们的使命是提供工具，以便您可以专注于重要的事情。

**💡 核心亮点更新 (中文)**：
- **#16308** - 计划优先试用：付费专区上的入门任务和专家，删除雇佣步骤，在试用开始时雇佣团队，主页从专家拥有的排名任务开始（由
- **#16650** - 将 Wix 添加到 MCP 目录（通过
- **#16654** - 奥托在大脑转储的不够屏幕上回复（由

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# 🚀 Release `autogpt-platform-beta-v0.11.2`

**Date:** January 2025

---

## 🔥 What's New?

### New Features
- **#16308** - Plan-first trial: starter tasks and experts on the paywall, hire step removed, team hired on trial start, Home starts with ranked tasks owned by experts (by @itsababseh)
- **#16650** - Add Wix to the MCP catalog (by @ntindle)
- **#16654** - Otto replies on the brain dump's not-enough screen (by @itsababseh)
- **#15459** - Self-serve account deletion with an optional exit question (by @itsababseh)
- **#16698** - Send a PostHog event whenever a usage limit refuses or pauses work (SECRT-3411) (by @kcze)
- **#16269** - Continue with Microsoft, with the Microsoft 365 offer as a movable onboarding step (by @ntindle)
- **#16348** - Add in-app feedback prompts (by @0ubbe)
- **#16461** - Limit how many E2B sandboxes run at once, per deployment and per account (by @Pwuts)
- **#16689** - Open a new Expert's chat from its card and the sidebar, and create and start in one click (by @itsababseh)
- **#16702** - Set the plan tier on the PostHog person (SECRT-3411) (by @kcze)
- **#15454** - Let the HubSpot blocks sign in with HubSpot OAuth (by @Bentlybro)
- **#15487** - Erase closed accounts after #15459's 14 days, keeping a ban record (erase-account CLI and job) (by @kcze)

### Enhancements
- **#16700** - Add Meta Muse Ember model support (by @ntindle)
- **#16699** - Add Claude Fable 5.2 support (by @ntindle)
- **#15761** - Overlap independent s
```
</details>

---
### 📦 [rockbenben/ChatGPT-Shortcut](https://github.com/rockbenben/ChatGPT-Shortcut)
`⭐ Stars: 8,940` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v4.5.2](https://github.com/rockbenben/ChatGPT-Shortcut/releases/tag/v4.5.2) (2026-11-04)`

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
`⭐ Stars: 2,878` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [userscript-v2.38.3](https://github.com/pionxzh/chatgpt-exporter/releases/tag/userscript-v2.38.3) (2026-11-04)`

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
`⭐ Stars: 47,900` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [2.2.2](https://github.com/zhayujie/CowAgent/releases/tag/2.2.2) (2026-10-30)`

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
`⭐ Stars: 2,535` &nbsp;|&nbsp; `💻 语言: Shell` &nbsp;|&nbsp; `🏷️ 最新版本: [20261108](https://github.com/lxhao61/integrated-examples/releases/tag/20261108) (2026-11-08)`

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
`⭐ Stars: 22,345` &nbsp;|&nbsp; `💻 语言: Shell` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.5.41](https://github.com/mack-a/v2ray-agent/releases/tag/v3.5.41) (2026-11-09)`

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
`⭐ Stars: 15,615` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v5.10.0](https://github.com/electerm/electerm/releases/tag/v5.10.0) (2026-11-10)`

> **简介**：📻免费开源终端/ssh/sftp/ftp/telnet/串口/RDP/VNC/Spice客户端(Linux, Mac, Windows, Android, HarmonyOS, iOS)

**💡 核心亮点更新 (中文)**：
- 小部件：新的“在线”选项卡可浏览 widgets.electterm.org 注册表并一键安装小部件。在安装之前，它会显示源存储库、固定提交和文件列表以供审查，警告小部件的 main.js 以完整的 Node 权限运行，并根据注册表哈希验证每个下载的文件；已撤销的小部件被标记
- 安全性：在 Web 会话选项卡中输入的 HTTP 基本凭据现在绑定到它们输入的源，因此跨源请求和重定向不再接收它们；来宾权限检查也被拒绝 (GHSA-3mh6-qf3v-q6cr)
- 修复人工智能预设仍然提供退役的 Gemini 和 Claude 模型，并替换为当前模型（#4716）

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
### Major updates

- Widgets: a new "Online" tab browses the widgets.electerm.org registry and installs a widget in one click. Before installing, it shows the source repository, pinned commit and file list for review, warns that a widget's main.js runs with full Node privileges, and verifies every downloaded file against the registry hash; revoked widgets are flagged

### Bug fixes

- Security: HTTP Basic credentials entered in a web-session tab are now bound to the origin they were typed for, so cross-origin requests and redirects no longer receive them; guest permission checks are denied as well (GHSA-3mh6-qf3v-q6cr)
- Fix AI presets still offering retired Gemini and Claude models, replaced with current ones (#4716) by @pcbeingused333

-----

### 重大更新

- 小组件：新增「在线」标签页，可浏览 widgets.electerm.org 目录并一键安装。安装前会展示来源仓库、锁定的 commit 与文件列表供确认，并提示小组件的 main.js 会以完整 Node 权限运行；安装时会按目录哈希校验每个文件，已撤销的小组件会给出提示

### 问题修复

- 安全：修复 Web 会话标签中输入的 HTTP Basic 凭据会被附加到该标签所有请求（包括跨站请求与重定向）的问题，现在凭据仅用于输入时对应的 origin；同时补齐访客权限检查的拦截 (GHSA-3mh6-qf3v-q6cr)
- 修复 AI 预设中仍提供已下线的 Gemini / Claude 模型的问题，更新为当前可用模型 (#4716)（由 @pcbeingused333 提供）

-------
Download下载: [https://electerm.org](https://electerm.org)
```
</details>

---
### 📦 [pymumu/smartdns](https://github.com/pymumu/smartdns)
`⭐ Stars: 11,411` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [Release48.5-RC1](https://github.com/pymumu/smartdns/releases/tag/Release48.5-RC1) (2026-11-09)`

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
`⭐ Stars: 42,864` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v26.11.9](https://github.com/XTLS/Xray-core/releases/tag/v26.11.9) (2026-11-09)`

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
`⭐ Stars: 9,635` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [v154.0.8037.49-5](https://github.com/klzgrad/naiveproxy/releases/tag/v154.0.8037.49-5) (2026-10-22)`

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

### 📦 [Kianuni/Erosion-CN](https://github.com/Kianuni/Erosion-CN)
`⭐ Stars: 1,723` &nbsp;|&nbsp; `💻 语言: Swift` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.9.1](https://github.com/Kianuni/Erosion-CN/releases/tag/v0.9.1) (2026-11-12)`

> **简介**：iOS / iPadOS 系统配置与 MobileGestalt 研究工具箱（简体中文防白苹果安全加固版）

**💡 核心亮点更新 (中文)**：
- 在所有原生支持 Apple 智能的 iPhone（`iPhone 15 Pro` 至 `iPhone 18 Pro Max` 全系列）原厂 `CacheData` 中，`Personal Translator`（`M1n2sAqf33NAOgZRGxQYBA`，槽位 `#266`）原厂默认为 `true (0x01)`，而 `Audio Intelligence`（`rb2tKZxlj0Gm2tBmUQSLqQ`，槽位 `#178`）原厂默认为 `false (0x00)`。
- 此前跨 iOS 版本 OTA 升级（旧 `OriginalGestalt.plist` 的 `CacheUUID` 变化）或非 18 Pro 机型执行一键配齐时，可能将 `#266` 误写为 `false (0x00)` 并污染本地 `UserDefaults` 基线快照，触发 `GenerativeModels / ModelCatalog` 本地预检 0ms 熔断报错（端侧快速消除正常，但**照片高质量消除、扩图延伸、重构及相机 `SIRI` 模式**瞬间报错）。
- `v0.9.1` 已锁定全系原生 AI iPhone 的硬件原厂基线（`#266 = true`、`#178 = false`，免疫跨版本备份不匹配与污染缓存），并在恢复出厂 / 重建缓存 / 重生备份时自动清理本地槽位基线记录。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Erosion-CN v0.9.1 更新日志 · Bilingual Release Notes (Build 23)

### 🇨🇳 简体中文

#### 🛠️ 关键 Bug 修复：原生 AI 机型 `Personal Translator (#266)` 基线锁定与双向自愈（修复 #16 / #22）
1. **修复旧版（`v0.8.3 – v0.8.5`）误关槽位 `#266` 导致相册云端工具与相机 Siri「0 秒瞬间报错」的问题**：
   - 在所有原生支持 Apple 智能的 iPhone（`iPhone 15 Pro` 至 `iPhone 18 Pro Max` 全系列）原厂 `CacheData` 中，`Personal Translator`（`M1n2sAqf33NAOgZRGxQYBA`，槽位 `#266`）原厂默认为 `true (0x01)`，而 `Audio Intelligence`（`rb2tKZxlj0Gm2tBmUQSLqQ`，槽位 `#178`）原厂默认为 `false (0x00)`。
   - 此前跨 iOS 版本 OTA 升级（旧 `OriginalGestalt.plist` 的 `CacheUUID` 变化）或非 18 Pro 机型执行一键配齐时，可能将 `#266` 误写为 `false (0x00)` 并污染本地 `UserDefaults` 基线快照，触发 `GenerativeModels / ModelCatalog` 本地预检 0ms 熔断报错（端侧快速消除正常，但**照片高质量消除、扩图延伸、重构及相机 `SIRI` 模式**瞬间报错）。
   - `v0.9.1` 已锁定全系原生 AI iPhone 的硬件原厂基线（`#266 = true`、`#178 = false`，免疫跨版本备份不匹配与污染缓存），并在恢复出厂 / 重建缓存 / 重生备份时自动清理本地槽位基线记录。
2. **新增双向异常检测与「一键配齐 / 修复」自愈提示**：
   - 顶部「Apple 智能激活四要素体检」卡片、实时 `MGCopyAnswer` 核验与防呆护栏现可**双向检测**槽位偏移（无论 `#178` 被强开为 `true` 还是原生 AI 机型的 `#266` 被误关为 `false`）；
   - 受旧版影响的用户升级 `v0.9.1` 后，打开 `MobileGestalt` 点击顶部 **「一键配齐 / 修复」→「应用」→ 手动关机冷重启** 即可完整恢复原厂基线。
3. **单包中英双语同步更新**：新增诊断提示词条已 100% 同步内置简体中文 (`zh-Hans`) 与英文 (`en`) 双语翻译。

---

### 🌐 English

#### 🛠️ Critical Bug Fix: `Personal Translator (#266)` Factory Baseline Lock & Two-Way Auto-Heal (Fixes #16 / #22)
1. **Fixed instant 0ms failure in Photos Cloud Tools (High-Quality Clean Up / Extend / Reframe) & Camera `SIRI` caused by slot `#266` downgrade**:
   - On all native Apple Intelligence iPhones (`iPhone 15 P
```
</details>

---
### 📦 [a3974892-cmd/wakeloom](https://github.com/a3974892-cmd/wakeloom)
`⭐ Stars: 60` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.21.5](https://github.com/a3974892-cmd/wakeloom/releases/tag/v1.21.5) (2026-11-09)`

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
`⭐ Stars: 29,842` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.6.1](https://github.com/storytold/craft-anything/releases/tag/v0.6.1) (2026-11-12)`

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
`⭐ Stars: 4,881` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.1.1](https://github.com/JustAResearcher/gpu-unlock-ada/releases/tag/v1.1.1) (2026-10-24)`

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
`⭐ Stars: 2,850` &nbsp;|&nbsp; `💻 语言: Other` &nbsp;|&nbsp; `🏷️ 最新版本: [0.10.4a](https://github.com/NeverSinkDev/NeverSink-Filter-for-PoE2/releases/tag/0.10.4a) (2026-10-15)`

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
`⭐ Stars: 165` &nbsp;|&nbsp; `💻 语言: Shell` &nbsp;|&nbsp; `🏷️ 最新版本: [2026.11.12-22/21_arm_cortex-a9_vfpv3-d16](https://github.com/kenzok8/compile-package/releases/tag/2026.11.12-22/21_arm_cortex-a9_vfpv3-d16) (2026-11-12)`

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
`⭐ Stars: 12,069` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.2.6](https://github.com/jxxghp/MoviePilot/releases/tag/v3.2.6) (2026-11-12)`

> **简介**：NAS媒体库自动化管理工具

**💡 核心亮点更新 (中文)**：
- 站点接入：新增 Piggo 实验室 API、HDArea REST API 和 FluxTorrent 兼容层接入，完善相关站点的搜索、下载和用户数据支持，适配好学迁移后的站点协议。
- 资源展示：修复 HDWinG 免费及双倍上传标识识别，补齐 Piggo 资源标签；前端正确区分资源标签与促销状态，保留未知促销状态，站点数据刷新失败时展示具体原因。
- 搜索过滤：自动迁移旧版过滤规则 ID，搜索结果明确提示失效规则及规则组，便于定位和修复规则配置问题。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 本次更新内容

以下汇总主项目 v3.2.5 发布后（北京时间 2026 年 11 月 7 日 06:27 起）的前后端及 App 变化；iOS App 使用独立版本号，本次涉及 v1.2.2。

- 站点接入：新增 Piggo 实验室 API、HDArea REST API 和 FluxTorrent 兼容层接入，完善相关站点的搜索、下载和用户数据支持，适配好学迁移后的站点协议。
- 资源展示：修复 HDWinG 免费及双倍上传标识识别，补齐 Piggo 资源标签；前端正确区分资源标签与促销状态，保留未知促销状态，站点数据刷新失败时展示具体原因。
- 搜索过滤：自动迁移旧版过滤规则 ID，搜索结果明确提示失效规则及规则组，便于定位和修复规则配置问题。
- 下载与订阅：修复累计集号转换后的单集选取及下载历史；暂停的磁力任务可先获取元数据再选集；订阅下载整包时只选择订阅范围内的剧集，并完善订阅身份转换重试。
- 种子下载：换票失败及临时下载地址失效时提供脱敏诊断和短时冷却，不再误加入损坏种子黑名单；兼容繁体首次下载确认页面。
- 文件整理：手动整理默认跟随目标目录的刮削设置，未刮削时提示可后续补刮；修复硬链接覆盖整理残留暂存与备份文件的问题。
- 音乐识别与整理：完善多文件专辑匹配，修复音乐 STRM 曲序丢失和重复扩展名；统一伴随文件处理，手动批次保留歌词、封面等文件，歌词后缀支持配置。
- 音乐刮削与纠错：按所选发行版本校正碟号、曲序、曲名与艺人，并遵守标签覆盖策略，有歧义的曲目保留原标签；封面缩略图缺失时回退原图，保留纠错预览提示并兼容伴随文件变化。
- 插件与仪表板：缓存插件静态资源和评分，评分并发加载，远程组件加载失败可原地重试；减少仪表板轮询及媒体缩略图请求竞争，修复插件分身延迟相对导入问题。
- 媒体库与接口：修复 Jellyfin 混合内容库路由，入库查询返回条目所属服务器，季集列表补充 TMDB 单集 ID。
- AI 助手：新增 cheapaimodel、UberLLM 模型服务商，修复 Gemini 会话搜索参数及空字符串参数兼容问题。
- 配置安全：防止 AI 工具用空配置或脱敏凭据占位符覆盖插件设置，完善工具执行回执和重复调用保护。
- 运行稳定性：浏览器任务增加排队、超时监控与异常回收；115 限流冷却期间快速返回，避免长时间占用工作线程；修正过滤与字幕模块健康状态。
- 界面反馈：修复日历加载进度与实际条目不一致的问题，完善站点刷新、搜索诊断和整理结果提示。
- App 显示：修复旧系统弹窗底色透明的问题；优化 iOS 16–25 底栏磨砂材质和明暗主题适配，修复原生搜索分类选中时图标与文字消失的问题。
- App 弹窗：补齐进入子弹窗、返回父弹窗及高度变化的动画，并适配系统“减弱动态效果”。

## 完整变更记录

- fix(transfer): 修复硬链接覆盖整理误留暂存与备份 (#7322) by @jxxghp ([379ef94](https://github.com/jxxghp/MoviePilot/commit/379ef94c9cc06149b40f42f7931cbfa941348496))
- fix(plugin): cache static resources and rating snapshots (#7324) by @jxxghp ([41516bb](https://github.com/jxxghp/MoviePilot/commit/41516bbc299d6eac221
```
</details>

---
### 📦 [sandboxie-plus/Sandboxie](https://github.com/sandboxie-plus/Sandboxie)
`⭐ Stars: 19,946` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.18.8](https://github.com/sandboxie-plus/Sandboxie/releases/tag/v1.18.8) (2026-10-17)`

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

## <span id="-效率办公与创作">📝 效率办公与创作</span>

### 📦 [huamidev/GestaltX](https://github.com/huamidev/GestaltX)
`⭐ Stars: 6,946` &nbsp;|&nbsp; `💻 语言: Swift` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.0.7](https://github.com/huamidev/GestaltX/releases/tag/v1.0.7) (2026-11-12)`

> **简介**：适用于 iOS 27.x 的 MobileGestalt 编辑器，具有区域代码调整、设备预设、备份功能。

**💡 核心亮点更新 (中文)**：
- 修复了 iOS 27.3 上的容器发现，以便壁纸和应用程序启动图像可以再次找到其容器。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
English | [简体中文](https://github.com/huamidev/GestaltX/blob/v1.0.7/CHANGELOG_ZH-CN.md)

Build `11130112`.

### Fixed

- Fix container discovery on iOS 27.3 so wallpaper and App Launch Images can locate their containers again.
```
</details>

---
### 📦 [RongleCat/grok-bot-anywhere](https://github.com/RongleCat/grok-bot-anywhere)
`⭐ Stars: 58` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.1.4](https://github.com/RongleCat/grok-bot-anywhere/releases/tag/v0.1.4) (2026-11-06)`

> **简介**：Grok Bot Anywhere：带有 macOS 原生 Composer 和动态微信共享目的地的 Electron 桌面客户端

**💡 核心亮点更新 (中文)**：
- 入口在 Bot 的「更多」菜单里，选「编辑头像」。
- 26 个形状、11 个颜色全部可选；形状网格和颜色点都按官方面板的结构排列。
- 南瓜可以选黑、蓝、紫、品红、绿等颜色，不再强制橙色；柄仍保持深灰褐。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# Grok Bot Anywhere 0.1.4 更新说明

状态：Current。发布日期：2026-11-06。

0.1.4 增加应用内头像编辑器：不用打开官方客户端，就能直接给 Bot 换形状和颜色。编辑器开放全部 26 个形状和 11 个颜色，包含官方编辑器已经隐藏的南瓜。macOS 双架构包和 Windows x64 包同时更新。

## 下载

| 平台 | 文件 |
| --- | --- |
| macOS Apple Silicon（M1–M4） | `Grok Bot Anywhere-0.1.4-arm64.dmg` |
| macOS Intel | `Grok Bot Anywhere-0.1.4.dmg` |
| Windows 10/11 x64 | `Grok Bot Anywhere-0.1.4-win.zip` |

macOS 两个 DMG 都已做 Developer ID 签名、Apple 公证和 stapler。下载后把应用拖进「应用程序」覆盖旧版，覆盖前先完全退出旧版。

Windows 包是未签名 zip。解压后如果 SmartScreen 或 Smart App Control 拦截，需要自行解除锁定或用你的证书签名后再运行；公共分发没有代码签名时仍可能被系统拦截。

下载与安装步骤见 [Grok Bot Anywhere 下载与使用教程](https://jcng5q8n0f3z.feishu.cn/wiki/HwHmwM4dcidx8Wko50QcJlgGnyd)。也可以在 [GitHub Release v0.1.4](https://github.com/RongleCat/grok-bot-anywhere/releases/tag/v0.1.4) 下载同样的三个文件。

## 校验

| 文件 | SHA-256 |
| --- | --- |
| `Grok Bot Anywhere-0.1.4-arm64.dmg` | `3774a87d24d6f4c1d12b44403e85ebb855237d6701b5314ca197cd2f35ab635b` |
| `Grok Bot Anywhere-0.1.4.dmg` | `f7417f39743133f705de2f7f39a2208be50e6b6389bbae644018d935e7e1ef8b` |
| `Grok Bot Anywhere-0.1.4-win.zip` | `765066c0eb6c8eacaca32da5683b29670236c9c253c47ac84949301ae26bd687` |

## Windows 安装

1. 解压 zip 到普通目录，不要直接在压缩包里运行。
2. 如果文件带「来自其他计算机」标记，右键属性里解除锁定，或用 `Unblock-File`。
3. 需要代码签名时，用你自己的代码签名证书给 `Grok Bot Anywhere.exe` 签名；自签只适合本机或内网，公共分发仍会被 SmartScreen/SAC 拦。
4. 未签名包不会自动更新，升级时重新下载并覆盖。

## 头像编辑器

- 入口在 Bot 的「更多」菜单里，选「编辑头像」。
- 26 个形状、11 个颜色全部可选；形状网格和颜色点都按官方面板的结构排列。
- 南瓜可以选黑、蓝、紫、品红、绿等颜色，不再强制橙色；柄仍保持深灰褐。
- 选择形状或颜色后即时预览，保存写回账号；主窗口、输入框和原生头像桥会同
```
</details>

---
### 📦 [JamesQiu2005/SpektraLab](https://github.com/JamesQiu2005/SpektraLab)
`⭐ Stars: 1,769` &nbsp;|&nbsp; `💻 语言: Swift` &nbsp;|&nbsp; `🏷️ 最新版本: [spektralab-v2.3.2](https://github.com/JamesQiu2005/SpektraLab/releases/tag/spektralab-v2.3.2) (2026-11-10)`

> **简介**：SpektraLab — macOS 电影和打印模拟器。 SwiftUI 应用程序 + Metal/C++ 渲染引擎，链接进来，运行时没有 Python。 andreavolpato/spektrafilm 的一个分支。

**💡 核心亮点更新 (中文)**：
- **SpektraLab 现在可以在 Intel Mac 上运行。** 在 2.3.2 之前，引擎拒绝在 Intel Mac 上启动。它对快速数学 GPU 代码的启动检查依赖于那些 Mac 上的 GPU 不做的事情，因此正确构建的引擎被用来代替损坏的引擎。检查被重写，因此它不再依赖于此，并且仍然拒绝使用快速数学构建的引擎。感谢 zhanglm 的修复（#104）。
- **测试于：** 配备 AMD Radeon RX 590 eGPU 的 Mac mini 2018。英特尔构建也在 Rosetta 下的 Apple 芯片上进行了检查，引擎的全尺寸渲染与 Apple 芯片构建完全匹配。其他英特尔 Mac，特别是英特尔集成显卡，尚未尝试过。如果您的行为不当，请打开一个问题并说明您拥有的 Mac 和 GPU。
- 在 Intel 上和在 Apple 芯片上仍然需要 macOS 15 或更高版本。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
SpektraLab 2.3.2 for the Mac: **Intel Mac compatibility.**

- **SpektraLab now runs on Intel Macs.** Before 2.3.2 the engine refused to start on an Intel Mac. Its start-up check for fast-math GPU code relied on something the GPU on those Macs doesn't do, so a correctly built engine was taken for a broken one. The check is rewritten so it no longer depends on that, and still refuses an engine built with fast math. Thanks to zhanglm for the fix (#104).
- **Tested on:** a Mac mini 2018 with an AMD Radeon RX 590 eGPU. The Intel build was also checked on Apple silicon under Rosetta, where the engine's full-size render matches the Apple silicon build to the bit. Other Intel Macs, and Intel integrated graphics in particular, have not been tried yet. If yours misbehaves, please open an issue and say which Mac and GPU you have.
- macOS 15 or later is still required, on Intel as on Apple silicon.

Everything in [2.3.1](https://github.com/JamesQiu2005/SpektraLab/releases/tag/spektralab-v2.3.1) and [2.3.0](https://github.com/JamesQiu2005/SpektraLab/releases/tag/spektralab-v2.3.0) is unchanged. **HDR files are Apple gain-map files only, for now: Lightroom and Camera Raw cannot read SpektraLab's gain map as of today.**

**Download:** `SpektraLab-2.3.2-universal.dmg`, one download for Apple silicon and Intel Macs (macOS 15 or later). Signed with Developer ID and notarised by Apple.
SHA-256 `9bc09e71f04b5c84c718e492b30b644dc03fd03ddbf4e415d925b4e1f2c71fe6`
```
</details>

---
### 📦 [robbietilton/Compositor](https://github.com/robbietilton/Compositor)
`⭐ Stars: 18,629` &nbsp;|&nbsp; `💻 语言: Swift` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.6.6](https://github.com/robbietilton/Compositor/releases/tag/v1.6.6) (2026-11-08)`

> **简介**：适用于 Mac 的 Photoshop 替代品

**💡 核心亮点更新 (中文)**：
- 打开 PNG 或其他图像在文件后命名画布，导出和保存以其名称和文件夹开始
- 导出为会记住您上次使用的格式，并使用 Photoshop 熟悉的快捷键 ⌥⇧⌘S 打开

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
- Opening a PNG or other image names the canvas after the file, and Export and Save start with its name and folder
- Export As remembers the format you last used and opens with ⌥⇧⌘S, Photoshop's familiar shortcut
```
</details>

---
### 📦 [jgraph/drawio-desktop](https://github.com/jgraph/drawio-desktop)
`⭐ Stars: 63,960` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v32.6.10](https://github.com/jgraph/drawio-desktop/releases/tag/v32.6.10) (2026-11-04)`

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
`⭐ Stars: 96,445` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.3.0](https://github.com/Stirling-Tools/Stirling-PDF/releases/tag/v3.3.0) (2026-11-05)`

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
`⭐ Stars: 40,256` &nbsp;|&nbsp; `💻 语言: Java` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.27.2](https://github.com/halo-dev/halo/releases/tag/v2.27.2) (2026-11-02)`

> **简介**：Halo 是一款强大易用的开源建站工具，从个人博客、知识库，到企业官网、在线商城，Halo 都能助您轻松实现，一站式满足您的多样化建站需求。

**💡 核心亮点更新 (中文)**：
- 修复 Iconify 表单输入和数组标签直接渲染未经清洗的 SVG 内容的问题 by  in #10418
- 修复主题预览路径可以越过主题目录的问题，异常路径现在会回退到当前启用的主题 by  in #10434
- 修复自定义模板路径可能包含目录穿越、绝对路径、反斜杠或片段选择器的问题 by  in #10435

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
**此版本包含安全更新，建议所有用户尽快升级。**

## 问题修复

- 修复 Iconify 表单输入和数组标签直接渲染未经清洗的 SVG 内容的问题 by @ruibaby in #10418
- 修复主题预览路径可以越过主题目录的问题，异常路径现在会回退到当前启用的主题 by @ruibaby in #10434
- 修复自定义模板路径可能包含目录穿越、绝对路径、反斜杠或片段选择器的问题 by @ruibaby in #10435
- 修复站点 favicon 和首页 SEO 属性值未转义的问题 by @ruibaby in #10438
- 修复使用远程数据的 Select 表单项在快速滚动到底部时可能无法自动加载下一页的问题 by @ruibaby in #10422
- 修复部分弹窗在内容动态切换时显示异常的问题 by @ruibaby in #10424
- 修复选择 Iconify 图标时因 SVG 地址使用冒号而请求失败的问题 by @ruibaby in #10428
- 修复 Switch 组件的无障碍状态未正确反映当前开关值的问题 by @ruibaby in #10431
- 回复通知现在会在回复通过审核后再发送，待审核的回复不再提前发送邮件或站内通知 by @ruibaby in #10439

**Full Changelog**: https://github.com/halo-dev/halo/compare/v2.27.1...v2.27.2
```
</details>

---
### 📦 [zyx0814/dzzoffice](https://github.com/zyx0814/dzzoffice)
`⭐ Stars: 4,061` &nbsp;|&nbsp; `💻 语言: PHP` &nbsp;|&nbsp; `🏷️ 最新版本: [2.4.2](https://github.com/zyx0814/dzzoffice/releases/tag/2.4.2) (2026-10-22)`

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
`⭐ Stars: 4,811` &nbsp;|&nbsp; `💻 语言: C#` &nbsp;|&nbsp; `🏷️ 最新版本: [4.16.11-Installer](https://github.com/emoacht/Monitorian/releases/tag/4.16.11-Installer) (2026-11-08)`

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
`⭐ Stars: 14,716` &nbsp;|&nbsp; `💻 语言: PowerShell` &nbsp;|&nbsp; `🏷️ 最新版本: [v11.9.15.0](https://github.com/YerongAI/Office-Tool/releases/tag/v11.9.15.0) (2026-11-11)`

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
`⭐ Stars: 3,015` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.2.12](https://github.com/TDesktop-x64/tdesktop/releases/tag/v1.2.12) (2026-11-07)`

> **简介**：64Gram（非官方 Telegram 桌面）

**💡 核心亮点更新 (中文)**：
v1.2.12 (TDesktop v7.4.1)

1.【修复】重复反应
2.【修复】讨论按钮
3.【修复】查看消息
4. [修复]聊天ID位置（第二次尝试）

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
v1.2.12 (TDesktop v7.4.1)

1. [Fix] duplicate reaction
2. [Fix] discussion button
3. [Fix] View message
4. [Fix] chat id position (2nd attempt)
```
</details>

---
### 📦 [microsoft/vscode](https://github.com/microsoft/vscode)
`⭐ Stars: 195,339` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [1.146.0](https://github.com/microsoft/vscode/releases/tag/1.146.0) (2026-11-11)`

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

## <span id="-影音媒体与下载">🎬 影音媒体与下载</span>

### 📦 [ziyuanhuishequ/release-downloader](https://github.com/ziyuanhuishequ/release-downloader)
`⭐ Stars: 33` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.6.3](https://github.com/ziyuanhuishequ/release-downloader/releases/tag/v1.6.3) (2026-11-08)`

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
`⭐ Stars: 1,205` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.1.0](https://github.com/threerocks/sweety-handdraw-video/releases/tag/v3.1.0) (2026-11-11)`

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
`⭐ Stars: 26,355` &nbsp;|&nbsp; `💻 语言: C#` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.4.0](https://github.com/KnifeLemon/Filee/releases/tag/v2.4.0) (2026-11-09)`

> **简介**：免费的开源文件转换器。通过拖放功能离线转换 263 格式 — 图像、PDF、Word、Excel、PowerPoint、HWP/HWPX、视频、音频、电子书和档案。无需上传，无需 Office。

**💡 核心亮点更新 (中文)**：
发生了什么变化

<!--更新
级别：必填
zh: 安全修复：更新签名验证，防止文档读取 PC/网络上的文件、文件过大等问题。
ko：修复了 Calibre 引擎安装/更新失败的问题。
zh: 修复了升级用户看不到翻译预设的问题
zh: 添加背景：为照片添加渐变、颜色、图片背景、边距、圆角和阴影。
en: 主屏幕

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## What's Changed

<!-- update
level: required
ko: 보안 수정: 업데이트 서명 확인, 문서가 PC·네트워크의 파일을 읽는 문제, 크기를 부풀린 파일 등을 막았어요
ko: Calibre 엔진 설치·업데이트가 실패하던 문제를 고쳤어요
ko: 업그레이드한 사용자에게 번역 프리셋이 보이지 않던 문제를 고쳤어요
ko: 배경 넣기: 사진에 그라데이션, 색, 그림 배경과 여백, 둥근 모서리, 그림자를 더해요
ko: 홈 화면에서 파일을 목록으로 모아 순서를 정한 뒤 변환해요
ko: PDF 나누기: 끌어다 놓을 때마다 페이지 범위를 물어요
ko: Word → PDF·HWPX: 머리글, 그림 자르기, 줄 간격, 각주 번호, 수식 번호 등 레이아웃을 많이 고쳤어요
ko: 새 형식: 서명된 .p7m, FLIC 애니메이션, DBML, Krita 백업(.kra~), 속성 목록(.plist), .java, .jif
ko: 새 도구: 오프라인 AI 이미지 확대(최대 4배), 폴더·압축 파일로 ISO 만들기, 메타데이터 보고 남길 항목 고르기
ko: PDF 합치기: 책갈피, 문서 안 링크, 양식 필드를 지켜요
ko: 새 언어: 벵골어, 페르시아어
en: Security fixes: update signatures are checked, documents can't read other files on the PC or network, and inflated files are refused
en: Installing or updating the Calibre engine no longer fails
en: The Translate preset now reaches libraries upgraded from 2.2 or earlier
en: Add background: gradient, colour or picture backgrounds with padding, rounded corners and a shadow
en: Home page: collect files in a list and set their order before converting
en: Split PDF asks for the pages each time you drop a file
en: Word to PDF and HWPX: many layout fixes for headers, cropped pictures, line spacing, footnote and equation numbers
en: New formats: signed .p7m, FLIC animations, DBML, Krita backups (.kra~), property lists (.plist), .java, .jif
en: New tools: offline AI image upscaling (up to 4x), ISO images from folders and archives, and Metadata to see and choose what a file keeps
en: Merge PDF
```
</details>

---
### 📦 [guohuiyuan/go-music-dl](https://github.com/guohuiyuan/go-music-dl)
`⭐ Stars: 6,249` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.1.5](https://github.com/guohuiyuan/go-music-dl/releases/tag/v1.1.5) (2026-11-09)`

> **简介**：一个基于 Go 语言的全网音乐搜索与下载工具。支持 CLI 命令行与 Web 服务双模式，内置网易云、QQ、酷狗、Bilibili、汽水音乐等 10+ 个主流平台，支持多源并发搜索与无损音质解析。music-dl交流群：755087923

**💡 核心亮点更新 (中文)**：
* 78f39f2e3488ec507fa4604a91fe405f7ef8f701 优化 Spotify 搜索功能，更新相关提示信息，支持匿名访问；新增错误处理逻辑，提升用户体验
* 81eedc60f5799ce12463d7023f211747a894128a 新增 Spotify 支持，包括搜索、下载、歌词解析等功能，并更新相关测试用例
* 119f1c143a626959e56cc91271d1cbb851952197 新增定时播放功能，包括前端界面、调度逻辑及相关样式，支持用户设置播放时间和重复选项

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Changelog
* 78f39f2e3488ec507fa4604a91fe405f7ef8f701 优化 Spotify 搜索功能，更新相关提示信息，支持匿名访问；新增错误处理逻辑，提升用户体验
* 81eedc60f5799ce12463d7023f211747a894128a 新增 Spotify 支持，包括搜索、下载、歌词解析等功能，并更新相关测试用例
* 119f1c143a626959e56cc91271d1cbb851952197 新增定时播放功能，包括前端界面、调度逻辑及相关样式，支持用户设置播放时间和重复选项
* 216fd04f4ce56c6a6182afe9b6c1f9754b0946e4 新增打开下载目录功能，更新相关 API、前端界面及样式，优化用户体验
* e48d327d92b23da36ae1592ce19b0d40a899ea65 新增歌词下载文件名模板功能，优化歌词文件名生成逻辑
* 2433238c300715196a9d323212b4ec1497f5dacb 新增自动切换功能的相关数据处理逻辑，优化歌曲检查流程，支持更灵活的错误处理
* 615e53f506680cf3b1019e0f80c0163541ecbdd7 新增设置模态框的响应式加载逻辑，优化打开下载目录功能的用户体验
* c445dddb66eec1b34c04fb16a72577f1115285c7 更新应用版本至 1.1.5
* 6aa70be2bda208ca6573654d93cff0709969eccb 重构定时播放功能为定时停止，更新相关 UI、逻辑及测试，优化用户体验
```
</details>

---
### 📦 [LibreSpark/LibreTV](https://github.com/LibreSpark/LibreTV)
`⭐ Stars: 24,609` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.22.0](https://github.com/LibreSpark/LibreTV/releases/tag/v2.22.0) (2026-11-08)`

> **简介**：一分钟搭建影视站，支持Docker等部署方式

**💡 核心亮点更新 (中文)**：
获取方式

Docker（多架构 linux/amd64 / linux/arm64）

```bash
docker pull docker.io/bestzwei/libretv:2.22.0
docker pull ghcr.io/librespark/libretv:2.22.0
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
docker pull docker.io/bestzwei/libretv:2.22.0
docker pull ghcr.io/librespark/libretv:2.22.0
```

两个 registry 的镜像内容一致（同一组 digest），`latest` 也指向本版本。

### 免 Docker（下方附件，Node 18+）

```bash
sha256sum -c SHA256SUMS
tar -xzf libretv-2.22.0-standalone.tar.gz -C libretv
cd libretv && PASSWORD=your-password PORT=8080 node server.js
```

预构建包与 CPU 架构无关（x86_64 / arm64 / armv7），环境变量与 Docker 部署一致。

> 镜像由 docker-publish 工作流在同一 tag 上构建，刚发布时可能还要 5–10 分钟才可拉取。

## 变更

完整对比：https://github.com/LibreSpark/LibreTV/compare/v2.21.2...v2.22.0
```
</details>

---
### 📦 [DIYgod/RSSHub](https://github.com/DIYgod/RSSHub)
`⭐ Stars: 46,968` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2026.11.12-8637.9b47c74](https://github.com/DIYgod/RSSHub/releases/tag/v2026.11.12-8637.9b47c74) (2026-11-12)`

> **简介**：🧡 一切都是RSSible

**💡 核心亮点更新 (中文)**：
-ghcr.io/diygod/rsshub:9b47c74ddc4dc34d9b97791de96964a0654486e1
- ghcr.io/diygod/rsshub:chromium-bundled-9b47c74ddc4dc34d9b97791de96964a0654486e1
- diygod/rsshub:9b47c74ddc4dc34d9b97791de96964a0654486e1

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Source commit: 9b47c74ddc4dc34d9b97791de96964a0654486e1

Published multi-platform images:
- ghcr.io/diygod/rsshub:9b47c74ddc4dc34d9b97791de96964a0654486e1
- ghcr.io/diygod/rsshub:chromium-bundled-9b47c74ddc4dc34d9b97791de96964a0654486e1
- diygod/rsshub:9b47c74ddc4dc34d9b97791de96964a0654486e1
- diygod/rsshub:chromium-bundled-9b47c74ddc4dc34d9b97791de96964a0654486e1

Use these commit-specific image tags to reproduce this release. Daily Docker tags may be updated by subsequent builds.
```
</details>

---
### 📦 [amir1376/ab-download-manager](https://github.com/amir1376/ab-download-manager)
`⭐ Stars: 19,238` &nbsp;|&nbsp; `💻 语言: Kotlin` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.11.4](https://github.com/amir1376/ab-download-manager/releases/tag/v1.11.4) (2026-11-03)`

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
`⭐ Stars: 9,724` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.7.0](https://github.com/gyroflow/gyroflow/releases/tag/v1.7.0) (2026-11-07)`

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
`⭐ Stars: 207,307` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [2026.10.26](https://github.com/yt-dlp/yt-dlp/releases/tag/2026.10.26) (2026-10-26)`

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
`⭐ Stars: 79,473` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [33.0.1](https://github.com/obsproject/obs-studio/releases/tag/33.0.1) (2026-10-29)`

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
`⭐ Stars: 5,613` &nbsp;|&nbsp; `💻 语言: CSS` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.1.3](https://github.com/jerrykuku/luci-theme-argon/releases/tag/v3.1.3) (2026-11-06)`

> **简介**：Argon 是一个干净整洁的 OpenWrt LuCI 主题，允许用户使用图像或视频自定义其登录界面。   它还支持明暗模式自动和手动切换。

**💡 核心亮点更新 (中文)**：
- 修复部分固件升级后 Argon 翻译丢失，保留已有翻译，并在后续在线升级时同步语言包（#737）。
- 修复部分固件因下载器缺少 HTTPS 支持而无法获取在线壁纸的问题（#738）。
- 修复网桥 VLAN 下拉菜单文字逐字竖排的问题（#738）。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 修复

- 修复部分固件升级后 Argon 翻译丢失，保留已有翻译，并在后续在线升级时同步语言包（#737）。
- 修复部分固件因下载器缺少 HTTPS 支持而无法获取在线壁纸的问题（#738）。
- 修复网桥 VLAN 下拉菜单文字逐字竖排的问题（#738）。

## Fixed

- Preserve bundled Argon translations during upgrades and synchronize language packages in subsequent online updates (#737).
- Fix online wallpapers failing on firmware that selects a downloader without HTTPS support (#738).
- Keep bridge VLAN dropdown labels readable instead of wrapping one character per line (#738).

v3.1.0 及以上可在线升级。安装说明：[中文](https://github.com/jerrykuku/luci-theme-argon/blob/v3.1.3/README_ZH.md#安装) · [English](https://github.com/jerrykuku/luci-theme-argon/blob/v3.1.3/README.md#install)
```
</details>

---
### 📦 [agalwood/Motrix](https://github.com/agalwood/Motrix)
`⭐ Stars: 58,192` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.4.1](https://github.com/agalwood/Motrix/releases/tag/v2.4.1) (2026-11-09)`

> **简介**：功能齐全的下载管理器。

**💡 核心亮点更新 (中文)**：
* 修复（引擎）：将 aria2 与 Windows 连接故障转移捆绑在一起，通过 https://github.com/agalwood/Motrix/pull/2515
* 杂务（发布）：升级翻译依赖项并在 https://github.com/agalwood/Motrix/pull/2516 中准备 2.4.1

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# Motrix 2.4.1

English | [简体中文](https://github.com/agalwood/Motrix/blob/main/docs/release-notes/2.4.1.zh-CN.md)

## Changes since 2.4.0

- Bundle **aria2 1.37.0-motrix.24**. On Windows, the engine tries the remaining resolved addresses for a host after a connection fails. It reports a network error if all candidates fail. Existing DNS and IPv6 defaults are preserved.
- Upgrade to **i18next 27.0.1** and **react-i18next 18.0.1**. The desktop app, Web UI and Server CLI continue to fall back to `en-US` for missing translations.
- Refresh the form validation, IP database, proxy and WebSocket dependencies, along with the Vite build tools and the jsdom test environment.

## Upgrade compatibility

**Back up your profile and download files before upgrading.** The bundled engine
uses SQLite **schema 6**. When upgrading an older engine database, retain its
complete pre-upgrade backup; older engines cannot open schema 6. Stop all engines
before restoring a verified backup to a separate path for a downgrade. Do not
reset or delete the upgraded database as a substitute for recovery.

Users migrating from Motrix v1 should follow the
[migration guide](https://github.com/agalwood/Motrix/blob/v2.4.1/docs/legacy-migration.md)
and retain the original profile and engine database backups.

## Downloads and updates

Desktop packages support macOS 13 or later, Windows 10 or later, and Linux, with
native x64 and ARM64 builds. No 32-bit desktop packages are provided. Official
macOS packages require s
```
</details>

---
### 📦 [subhra74/xdm](https://github.com/subhra74/xdm)
`⭐ Stars: 8,442` &nbsp;|&nbsp; `💻 语言: Kotlin` &nbsp;|&nbsp; `🏷️ 最新版本: [v9.0.10](https://github.com/subhra74/xdm/releases/tag/v9.0.10) (2026-11-12)`

> **简介**：自 2013 年以来，快速、可靠的下载加速器和视频下载器

**💡 核心亮点更新 (中文)**：
下载

|安装人员 |笔记|
|---|---|
| [xdm-app-9.0.10-arm64.dmg](https://github.com/subhra74/xdm/releases/download/v9.0.10/xdm-app-9.0.10-arm64.dmg) |适用于 Apple Silicon（M1 或更高版本）mac |
| [xdm-app-9.0.10-x64.dmg](https://github.com/subhra74

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Downloads

| Installer | Notes |
|---|---|
| [xdm-app-9.0.10-arm64.dmg](https://github.com/subhra74/xdm/releases/download/v9.0.10/xdm-app-9.0.10-arm64.dmg) | For Apple Silicon (M1 or later) mac |
| [xdm-app-9.0.10-x64.dmg](https://github.com/subhra74/xdm/releases/download/v9.0.10/xdm-app-9.0.10-x64.dmg) | For Intel mac |
| [xdm-9.0.10-arm64.msi](https://github.com/subhra74/xdm/releases/download/v9.0.10/xdm-9.0.10-arm64.msi) | For Windows ARM (Windows 10/11) |
| [xdm-9.0.10-x64.msi](https://github.com/subhra74/xdm/releases/download/v9.0.10/xdm-9.0.10-x64.msi) | For Windows x64 (Windows 10/11) |
| [xdmsetup-9.0.10.msi](https://github.com/subhra74/xdm/releases/download/v9.0.10/xdmsetup-9.0.10.msi) | Same as the x64 MSI; for XDM 8 (Microsoft Store) update notices |
| [xdm-app_9.0.10_amd64.deb](https://github.com/subhra74/xdm/releases/download/v9.0.10/xdm-app_9.0.10_amd64.deb) | For Debian / Ubuntu / Linux Mint x64 |
| [xdm-app_9.0.10_arm64.deb](https://github.com/subhra74/xdm/releases/download/v9.0.10/xdm-app_9.0.10_arm64.deb) | For Debian / Ubuntu / Linux Mint ARM |
| [xdm-app-9.0.10-1.aarch64.rpm](https://github.com/subhra74/xdm/releases/download/v9.0.10/xdm-app-9.0.10-1.aarch64.rpm) | For Fedora / RHEL / openSUSE ARM |
| [xdm-app-9.0.10-1.x86_64.rpm](https://github.com/subhra74/xdm/releases/download/v9.0.10/xdm-app-9.0.10-1.x86_64.rpm) | For Fedora / RHEL / openSUSE x64 |
| [xdm-app-9.0.10-1-aarch64.pkg.tar.zst](https://github.com/subhra74/xdm/releases/download/v9.0.10/xdm-
```
</details>

---

## <span id="-系统与开发者工具">🛠️ 系统与开发者工具</span>

### 📦 [physicsdolphin/nv-uefi-unlocker](https://github.com/physicsdolphin/nv-uefi-unlocker)
`⭐ Stars: 2,394` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.1.11](https://github.com/physicsdolphin/nv-uefi-unlocker/releases/tag/v2.1.11) (2026-11-08)`

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
### 📦 [assimp/assimp](https://github.com/assimp/assimp)
`⭐ Stars: 13,321` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [v6.0.6](https://github.com/assimp/assimp/releases/tag/v6.0.6) (2026-11-09)`

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
`⭐ Stars: 29,192` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [v25.12.6](https://github.com/openwrt/openwrt/releases/tag/v25.12.6) (2026-10-18)`

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

## <span id="-网络与代理技术">🌐 网络与代理技术</span>

### 📦 [SagerNet/sing-box](https://github.com/SagerNet/sing-box)
`⭐ Stars: 39,914` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.14.4](https://github.com/SagerNet/sing-box/releases/tag/v1.14.4) (2026-10-24)`

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
`⭐ Stars: 10,889` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [2.44.8](https://github.com/sub-store-org/Sub-Store/releases/tag/2.44.8) (2026-11-12)`

> **简介**：QX、Loon、Surge、Stash、Egern 和 Shadowrocket 的高级订阅管理器！

**💡 核心亮点更新 (中文)**：
*壮举：Surge支持VLESS； Surge Trust Tunnel 支持 client-random-auth-key ([091e6f8](https://github.com/sub-store-org/Sub-Store/commit/091e6f8))

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## <small>2.44.8 (2026-11-12)</small>

* feat: Surge 支持 VLESS; Surge Trust Tunnel 支持 client-random-auth-key ([091e6f8](https://github.com/sub-store-org/Sub-Store/commit/091e6f8))
```
</details>

---
### 📦 [233boy/Xray](https://github.com/233boy/Xray)
`⭐ Stars: 2,815` &nbsp;|&nbsp; `💻 语言: Shell` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.37](https://github.com/233boy/Xray/releases/tag/v1.37) (2026-11-02)`

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
`⭐ Stars: 2,687` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.39.0](https://github.com/enfein/mieru/releases/tag/v3.39.0) (2026-10-23)`

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
`⭐ Stars: 15,843` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.5.14](https://github.com/v2rayA/v2rayA/releases/tag/v2.5.14) (2026-11-09)`

> **简介**：一个基于 Xray 的核心的 Web 客户端，在 Linux、Windows 和 macOS 上具有全局透明代理。

**💡 核心亮点更新 (中文)**：
* iptables：当旧版 mangle 不可用时，回退到 nft，网址为 https://github.com/v2rayA/v2rayA/pull/2107

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## What's Changed
* iptables: fall back to nft when legacy mangle is unavailable by @HougeLangley in https://github.com/v2rayA/v2rayA/pull/2107
* chore(deps): bump follow-redirects from 1.16.0 to 1.16.2 in /gui by @dependabot[bot] in https://github.com/v2rayA/v2rayA/pull/2104
* chore(deps): bump vue-i18n from 11.4.12 to 11.4.14 in /gui by @dependabot[bot] in https://github.com/v2rayA/v2rayA/pull/2103
* chore(deps): bump serialize-javascript from 7.1.2 to 7.1.4 in /gui by @dependabot[bot] in https://github.com/v2rayA/v2rayA/pull/2100
* chore(deps): bump fast-uri from 3.1.8 to 3.1.9 in /gui by @dependabot[bot] in https://github.com/v2rayA/v2rayA/pull/2099
* chore(deps-dev): bump happy-dom from 20.14.5 to 21.0.4 in /gui by @dependabot[bot] in https://github.com/v2rayA/v2rayA/pull/2098
* chore(deps-dev): bump vite from 6.4.3 to 6.4.4 in /gui by @dependabot[bot] in https://github.com/v2rayA/v2rayA/pull/2090
* chore(deps-dev): bump vite from 6.4.4 to 6.4.5 in /gui by @dependabot[bot] in https://github.com/v2rayA/v2rayA/pull/2108

## New Contributors
* @HougeLangley made their first contribution in https://github.com/v2rayA/v2rayA/pull/2107

**Full Changelog**: https://github.com/v2rayA/v2rayA/compare/v2.5.13...v2.5.14
```
</details>

---
### 📦 [Anankke/SSPanel-UIM](https://github.com/Anankke/SSPanel-UIM)
`⭐ Stars: 10,446` &nbsp;|&nbsp; `💻 语言: PHP` &nbsp;|&nbsp; `🏷️ 最新版本: [26.3.0](https://github.com/Anankke/SSPanel-UIM/releases/tag/26.3.0) (2026-11-13)`

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
`⭐ Stars: 21,040` &nbsp;|&nbsp; `💻 语言: Other` &nbsp;|&nbsp; `🏷️ 最新版本: [202611122204](https://github.com/Loyalsoldier/v2ray-rules-dat/releases/tag/202611122204) (2026-11-12)`

> **简介**：🦄 🎃 👻 V2Ray 路由规则文件加强版，可代替 V2Ray 官方 geoip.dat 和 geosite.dat，适用于 V2Ray、Xray-core、mihomo(Clash-Meta)、hysteria、Trojan-Go 和 leaf。Enhanced edition of V2Ray rules dat files, applicable to V2Ray, Xray-core, mihomo(Clash-Meta), hysteria, Trojan-Go and leaf.

**💡 核心亮点更新 (中文)**：
该版本未提供详细更新说明。

---
### 📦 [Openwrt-Passwall/openwrt-passwall](https://github.com/Openwrt-Passwall/openwrt-passwall)
`⭐ Stars: 10,003` &nbsp;|&nbsp; `💻 语言: Lua` &nbsp;|&nbsp; `🏷️ 最新版本: [26.11.11-1](https://github.com/Openwrt-Passwall/openwrt-passwall/releases/tag/26.11.11-1) (2026-11-10)`

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
<summary>⚠️ 点击展开已放弃维护或超过 1 年停更的仓库清单 (136 个)</summary>

| 仓库名称 | Stars | 状态说明 | 操作建议 |
| :--- | :---: | :--- | :---: |
| [cityflow-project/CityFlow](https://github.com/cityflow-project/CityFlow) | 1,034 | 超过 450 天无代码提交 | [进入取消 Star](https://github.com/cityflow-project/CityFlow) |
| [facebookresearch/demucs](https://github.com/facebookresearch/demucs) | 10,408 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/facebookresearch/demucs) |
| [fufankeji/DeepSeek-OCR-Web](https://github.com/fufankeji/DeepSeek-OCR-Web) | 570 | 超过 381 天无代码提交 | [进入取消 Star](https://github.com/fufankeji/DeepSeek-OCR-Web) |
| [JimmyLv/awesome-nano-banana](https://github.com/JimmyLv/awesome-nano-banana) | 8,795 | 超过 430 天无代码提交 | [进入取消 Star](https://github.com/JimmyLv/awesome-nano-banana) |
| [btjawa/BiliTools](https://github.com/btjawa/BiliTools) | 5,004 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/btjawa/BiliTools) |
| [ehang-io/nps](https://github.com/ehang-io/nps) | 34,257 | 超过 896 天无代码提交 | [进入取消 Star](https://github.com/ehang-io/nps) |
| [ReturnFI/Blitz](https://github.com/ReturnFI/Blitz) | 1,088 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/ReturnFI/Blitz) |
| [kkangert/kspider](https://github.com/kkangert/kspider) | 1,262 | 超过 815 天无代码提交 | [进入取消 Star](https://github.com/kkangert/kspider) |
| [xenova/whisper-web](https://github.com/xenova/whisper-web) | 3,345 | 超过 772 天无代码提交 | [进入取消 Star](https://github.com/xenova/whisper-web) |
| [shadowsocks/luci-app-shadowsocks](https://github.com/shadowsocks/luci-app-shadowsocks) | 1,150 | 超过 1264 天无代码提交 | [进入取消 Star](https://github.com/shadowsocks/luci-app-shadowsocks) |
| [sinaptik-ai/pandas-ai](https://github.com/sinaptik-ai/pandas-ai) | 23,950 | 超过 380 天无代码提交 | [进入取消 Star](https://github.com/sinaptik-ai/pandas-ai) |
| [adithya-s-k/marker-api](https://github.com/adithya-s-k/marker-api) | 981 | 超过 758 天无代码提交 | [进入取消 Star](https://github.com/adithya-s-k/marker-api) |
| [yuchannslv5/warpflare](https://github.com/yuchannslv5/warpflare) | 334 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/yuchannslv5/warpflare) |
| [vvbbnn00/WARP-Clash-API](https://github.com/vvbbnn00/WARP-Clash-API) | 8,800 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/vvbbnn00/WARP-Clash-API) |
| [chika0801/hysteria-install](https://github.com/chika0801/hysteria-install) | 177 | 超过 860 天无代码提交 | [进入取消 Star](https://github.com/chika0801/hysteria-install) |
| [yeahwu/InstallOS](https://github.com/yeahwu/InstallOS) | 86 | 超过 1618 天无代码提交 | [进入取消 Star](https://github.com/yeahwu/InstallOS) |
| [bulianglin/psub](https://github.com/bulianglin/psub) | 1,757 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/bulianglin/psub) |
| [chatchat-space/Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat) | 38,713 | 超过 367 天无代码提交 | [进入取消 Star](https://github.com/chatchat-space/Langchain-Chatchat) |
| [lizongying/my-tv](https://github.com/lizongying/my-tv) | 31,960 | 超过 875 天无代码提交 | [进入取消 Star](https://github.com/lizongying/my-tv) |
| [joevess/IPTV](https://github.com/joevess/IPTV) | 10,273 | 超过 681 天无代码提交 | [进入取消 Star](https://github.com/joevess/IPTV) |
| [lecepin/WeChatVideoDownloader](https://github.com/lecepin/WeChatVideoDownloader) | 4,660 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/lecepin/WeChatVideoDownloader) |
| [linexjlin/GPTs](https://github.com/linexjlin/GPTs) | 32,017 | 超过 776 天无代码提交 | [进入取消 Star](https://github.com/linexjlin/GPTs) |
| [lxfater/Awesome-GPTs](https://github.com/lxfater/Awesome-GPTs) | 1,155 | 超过 1087 天无代码提交 | [进入取消 Star](https://github.com/lxfater/Awesome-GPTs) |
| [ClashDotNetFramework/experimental-clash](https://github.com/ClashDotNetFramework/experimental-clash) | 241 | 超过 1802 天无代码提交 | [进入取消 Star](https://github.com/ClashDotNetFramework/experimental-clash) |
| [zzzgydi/clash-verge](https://github.com/zzzgydi/clash-verge) | 21,859 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/zzzgydi/clash-verge) |
| [ddgth/cf2dns](https://github.com/ddgth/cf2dns) | 5,215 | 超过 675 天无代码提交 | [进入取消 Star](https://github.com/ddgth/cf2dns) |
| [zizifn/edgetunnel](https://github.com/zizifn/edgetunnel) | 9,329 | 超过 715 天无代码提交 | [进入取消 Star](https://github.com/zizifn/edgetunnel) |
| [missuo/Hysteria2](https://github.com/missuo/Hysteria2) | 204 | 超过 806 天无代码提交 | [进入取消 Star](https://github.com/missuo/Hysteria2) |
| [Misaka-blog/hysteria-install](https://github.com/Misaka-blog/hysteria-install) | 630 | 超过 938 天无代码提交 | [进入取消 Star](https://github.com/Misaka-blog/hysteria-install) |
| [MatsuriDayo/nekoray](https://github.com/MatsuriDayo/nekoray) | 15,242 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/MatsuriDayo/nekoray) |
| [FranzKafkaYu/x-ui](https://github.com/FranzKafkaYu/x-ui) | 8,432 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/FranzKafkaYu/x-ui) |
| [rwv/chinese-dos-games](https://github.com/rwv/chinese-dos-games) | 10,355 | 超过 827 天无代码提交 | [进入取消 Star](https://github.com/rwv/chinese-dos-games) |
| [getumbrel/llama-gpt](https://github.com/getumbrel/llama-gpt) | 10,923 | 超过 933 天无代码提交 | [进入取消 Star](https://github.com/getumbrel/llama-gpt) |
| [WangWenBin2017/OpenWrt-SSRPLUS](https://github.com/WangWenBin2017/OpenWrt-SSRPLUS) | 560 | 超过 620 天无代码提交 | [进入取消 Star](https://github.com/WangWenBin2017/OpenWrt-SSRPLUS) |
| [prompt-engineering/click-prompt](https://github.com/prompt-engineering/click-prompt) | 2,385 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/prompt-engineering/click-prompt) |
| [AutodeskAILab/Building-GAN](https://github.com/AutodeskAILab/Building-GAN) | 100 | 超过 1623 天无代码提交 | [进入取消 Star](https://github.com/AutodeskAILab/Building-GAN) |
| [novicezk/midjourney-proxy](https://github.com/novicezk/midjourney-proxy) | 5,375 | 超过 466 天无代码提交 | [进入取消 Star](https://github.com/novicezk/midjourney-proxy) |
| [adams549659584/go-proxy-bingai](https://github.com/adams549659584/go-proxy-bingai) | 8,394 | 超过 967 天无代码提交 | [进入取消 Star](https://github.com/adams549659584/go-proxy-bingai) |
| [tryptech/obs-zoom-and-follow](https://github.com/tryptech/obs-zoom-and-follow) | 441 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/tryptech/obs-zoom-and-follow) |
| [XingangPan/DragGAN](https://github.com/XingangPan/DragGAN) | 35,698 | 超过 908 天无代码提交 | [进入取消 Star](https://github.com/XingangPan/DragGAN) |
| [lewangdev/faster-whisper-youtube](https://github.com/lewangdev/faster-whisper-youtube) | 558 | 超过 1180 天无代码提交 | [进入取消 Star](https://github.com/lewangdev/faster-whisper-youtube) |
| [artidoro/qlora](https://github.com/artidoro/qlora) | 11,068 | 超过 885 天无代码提交 | [进入取消 Star](https://github.com/artidoro/qlora) |
| [langgenius/webapp-conversation](https://github.com/langgenius/webapp-conversation) | 1,101 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/langgenius/webapp-conversation) |
| [3andne/restls](https://github.com/3andne/restls) | 378 | 超过 1103 天无代码提交 | [进入取消 Star](https://github.com/3andne/restls) |
| [jtsang4/claude-to-chatgpt](https://github.com/jtsang4/claude-to-chatgpt) | 1,299 | 超过 816 天无代码提交 | [进入取消 Star](https://github.com/jtsang4/claude-to-chatgpt) |
| [yorunning/clash-conf](https://github.com/yorunning/clash-conf) | 103 | 超过 848 天无代码提交 | [进入取消 Star](https://github.com/yorunning/clash-conf) |
| [svc-develop-team/so-vits-svc](https://github.com/svc-develop-team/so-vits-svc) | 28,043 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/svc-develop-team/so-vits-svc) |
| [xiaye13579/BBLL](https://github.com/xiaye13579/BBLL) | 17,517 | 超过 622 天无代码提交 | [进入取消 Star](https://github.com/xiaye13579/BBLL) |
| [camenduru/MiniGPT-4-colab](https://github.com/camenduru/MiniGPT-4-colab) | 120 | 超过 1201 天无代码提交 | [进入取消 Star](https://github.com/camenduru/MiniGPT-4-colab) |
| [Vision-CAIR/MiniGPT-4](https://github.com/Vision-CAIR/MiniGPT-4) | 25,560 | 超过 801 天无代码提交 | [进入取消 Star](https://github.com/Vision-CAIR/MiniGPT-4) |
| [imfuxiao/Hamster](https://github.com/imfuxiao/Hamster) | 1,643 | 超过 548 天无代码提交 | [进入取消 Star](https://github.com/imfuxiao/Hamster) |
| [acheong08/ChatGPT](https://github.com/acheong08/ChatGPT) | 27,996 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/acheong08/ChatGPT) |
| [microsoft/JARVIS](https://github.com/microsoft/JARVIS) | 25,636 | 超过 471 天无代码提交 | [进入取消 Star](https://github.com/microsoft/JARVIS) |
| [choephix/auto-gpt-webui](https://github.com/choephix/auto-gpt-webui) | 116 | 超过 969 天无代码提交 | [进入取消 Star](https://github.com/choephix/auto-gpt-webui) |
| [facebookresearch/segment-anything](https://github.com/facebookresearch/segment-anything) | 55,129 | 超过 785 天无代码提交 | [进入取消 Star](https://github.com/facebookresearch/segment-anything) |
| [zai-org/ChatGLM-6B](https://github.com/zai-org/ChatGLM-6B) | 40,853 | 超过 868 天无代码提交 | [进入取消 Star](https://github.com/zai-org/ChatGLM-6B) |
| [ihciah/shadow-tls](https://github.com/ihciah/shadow-tls) | 2,681 | 超过 566 天无代码提交 | [进入取消 Star](https://github.com/ihciah/shadow-tls) |
| [jxbbb/ADAPT](https://github.com/jxbbb/ADAPT) | 421 | 超过 884 天无代码提交 | [进入取消 Star](https://github.com/jxbbb/ADAPT) |
| [mayooear/ai-pdf-chatbot-langchain](https://github.com/mayooear/ai-pdf-chatbot-langchain) | 16,585 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/mayooear/ai-pdf-chatbot-langchain) |
| [lencx/ChatGPT](https://github.com/lencx/ChatGPT) | 54,673 | 超过 805 天无代码提交 | [进入取消 Star](https://github.com/lencx/ChatGPT) |
| [nekohasekai/SagerNet](https://github.com/nekohasekai/SagerNet) | 56 | 超过 1767 天无代码提交 | [进入取消 Star](https://github.com/nekohasekai/SagerNet) |
| [P3TERX/Actions-OpenWrt](https://github.com/P3TERX/Actions-OpenWrt) | 7,616 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/P3TERX/Actions-OpenWrt) |
| [R86S/R86S-QuickInstaller](https://github.com/R86S/R86S-QuickInstaller) | 64 | 超过 1189 天无代码提交 | [进入取消 Star](https://github.com/R86S/R86S-QuickInstaller) |
| [WeNeedHome/SummaryOfLoanSuspension](https://github.com/WeNeedHome/SummaryOfLoanSuspension) | 20,320 | 超过 852 天无代码提交 | [进入取消 Star](https://github.com/WeNeedHome/SummaryOfLoanSuspension) |
| [zanzhz1101/LingMaxDNS](https://github.com/zanzhz1101/LingMaxDNS) | 23 | 超过 1583 天无代码提交 | [进入取消 Star](https://github.com/zanzhz1101/LingMaxDNS) |
| [IrineSistiana/mosdns-cn](https://github.com/IrineSistiana/mosdns-cn) | 324 | 超过 1625 天无代码提交 | [进入取消 Star](https://github.com/IrineSistiana/mosdns-cn) |
| [chika0801/Xray-install](https://github.com/chika0801/Xray-install) | 271 | 超过 1077 天无代码提交 | [进入取消 Star](https://github.com/chika0801/Xray-install) |
| [scutan90/DeepLearning-500-questions](https://github.com/scutan90/DeepLearning-500-questions) | 57,714 | 超过 869 天无代码提交 | [进入取消 Star](https://github.com/scutan90/DeepLearning-500-questions) |
| [Chikage0o0/Linux-NetSpeed](https://github.com/Chikage0o0/Linux-NetSpeed) | 3,739 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/Chikage0o0/Linux-NetSpeed) |
| [KFERMercer/OpenWrt-CI](https://github.com/KFERMercer/OpenWrt-CI) | 1,408 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/KFERMercer/OpenWrt-CI) |
| [qTox/qTox](https://github.com/qTox/qTox) | 4,969 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/qTox/qTox) |
| [quericy/one-key-ikev2-vpn](https://github.com/quericy/one-key-ikev2-vpn) | 2,105 | 超过 2187 天无代码提交 | [进入取消 Star](https://github.com/quericy/one-key-ikev2-vpn) |
| [riverscn/openwrt-iptvhelper](https://github.com/riverscn/openwrt-iptvhelper) | 371 | 超过 1903 天无代码提交 | [进入取消 Star](https://github.com/riverscn/openwrt-iptvhelper) |
| [frainzy1477/luci-app-clash](https://github.com/frainzy1477/luci-app-clash) | 1,622 | 超过 1693 天无代码提交 | [进入取消 Star](https://github.com/frainzy1477/luci-app-clash) |
| [Sanster/IOPaint](https://github.com/Sanster/IOPaint) | 23,287 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/Sanster/IOPaint) |
| [LANDrop/LANDrop](https://github.com/LANDrop/LANDrop) | 6,002 | 超过 820 天无代码提交 | [进入取消 Star](https://github.com/LANDrop/LANDrop) |
| [saveweb/review-2021](https://github.com/saveweb/review-2021) | 756 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/saveweb/review-2021) |
| [iranee/qnap-aliyunpan-webdav](https://github.com/iranee/qnap-aliyunpan-webdav) | 273 | 超过 1496 天无代码提交 | [进入取消 Star](https://github.com/iranee/qnap-aliyunpan-webdav) |
| [haoel/haoel.github.io](https://github.com/haoel/haoel.github.io) | 13,083 | 超过 1281 天无代码提交 | [进入取消 Star](https://github.com/haoel/haoel.github.io) |
| [tindy2013/stairspeedtest-reborn](https://github.com/tindy2013/stairspeedtest-reborn) | 3,822 | 超过 1253 天无代码提交 | [进入取消 Star](https://github.com/tindy2013/stairspeedtest-reborn) |
| [P3TERX/warp.sh](https://github.com/P3TERX/warp.sh) | 3,921 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/P3TERX/warp.sh) |
| [TheMRLL/WinXray](https://github.com/TheMRLL/WinXray) | 2,788 | 超过 989 天无代码提交 | [进入取消 Star](https://github.com/TheMRLL/WinXray) |
| [Mikubill/cowtransfer-uploader](https://github.com/Mikubill/cowtransfer-uploader) | 448 | 超过 1736 天无代码提交 | [进入取消 Star](https://github.com/Mikubill/cowtransfer-uploader) |
| [281677160/build-actions](https://github.com/281677160/build-actions) | 388 | 超过 471 天无代码提交 | [进入取消 Star](https://github.com/281677160/build-actions) |
| [vaxilu/x-ui](https://github.com/vaxilu/x-ui) | 19,081 | 超过 815 天无代码提交 | [进入取消 Star](https://github.com/vaxilu/x-ui) |
| [xinntao/Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) | 37,480 | 超过 828 天无代码提交 | [进入取消 Star](https://github.com/xinntao/Real-ESRGAN) |
| [zu1k/proxypool](https://github.com/zu1k/proxypool) | 4,039 | 超过 1312 天无代码提交 | [进入取消 Star](https://github.com/zu1k/proxypool) |
| [TachibanaYoshino/AnimeGAN](https://github.com/TachibanaYoshino/AnimeGAN) | 4,610 | 超过 1562 天无代码提交 | [进入取消 Star](https://github.com/TachibanaYoshino/AnimeGAN) |
| [yuanzhoulvpi2017/tiny_python](https://github.com/yuanzhoulvpi2017/tiny_python) | 173 | 超过 1376 天无代码提交 | [进入取消 Star](https://github.com/yuanzhoulvpi2017/tiny_python) |
| [haiibo/OpenWrt](https://github.com/haiibo/OpenWrt) | 3,161 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/haiibo/OpenWrt) |
| [VergilGao/openwrt-packages](https://github.com/VergilGao/openwrt-packages) | 11 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/VergilGao/openwrt-packages) |
| [VergilGao/openwrt-compiler](https://github.com/VergilGao/openwrt-compiler) | 13 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/VergilGao/openwrt-compiler) |
| [OpenELEC/OpenELEC.tv](https://github.com/OpenELEC/OpenELEC.tv) | 1,619 | 超过 3358 天无代码提交 | [进入取消 Star](https://github.com/OpenELEC/OpenELEC.tv) |
| [github/copilot-docs](https://github.com/github/copilot-docs) | 23,159 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/github/copilot-docs) |
| [Kiougar/luci-wrtbwmon](https://github.com/Kiougar/luci-wrtbwmon) | 355 | 超过 1876 天无代码提交 | [进入取消 Star](https://github.com/Kiougar/luci-wrtbwmon) |
| [EtherDream/jsproxy](https://github.com/EtherDream/jsproxy) | 9,317 | 超过 956 天无代码提交 | [进入取消 Star](https://github.com/EtherDream/jsproxy) |
| [cheat-engine/cheat-engine](https://github.com/cheat-engine/cheat-engine) | 19,458 | 超过 572 天无代码提交 | [进入取消 Star](https://github.com/cheat-engine/cheat-engine) |
| [ffffffff0x/Dork-Admin](https://github.com/ffffffff0x/Dork-Admin) | 1,914 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/ffffffff0x/Dork-Admin) |
| [ffffffff0x/Digital-Privacy](https://github.com/ffffffff0x/Digital-Privacy) | 4,934 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/ffffffff0x/Digital-Privacy) |
| [Autodesk/civilconnection](https://github.com/Autodesk/civilconnection) | 121 | 超过 1442 天无代码提交 | [进入取消 Star](https://github.com/Autodesk/civilconnection) |
| [0xHJK/CleanApps](https://github.com/0xHJK/CleanApps) | 165 | 超过 1908 天无代码提交 | [进入取消 Star](https://github.com/0xHJK/CleanApps) |
| [KANIKIG/Multi-EasyGost](https://github.com/KANIKIG/Multi-EasyGost) | 1,943 | 超过 956 天无代码提交 | [进入取消 Star](https://github.com/KANIKIG/Multi-EasyGost) |
| [Kurokosama/AutoBuild-OpenWRT](https://github.com/Kurokosama/AutoBuild-OpenWRT) | 88 | 超过 1595 天无代码提交 | [进入取消 Star](https://github.com/Kurokosama/AutoBuild-OpenWRT) |
| [differentrain/DeletionTool](https://github.com/differentrain/DeletionTool) | 94 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/differentrain/DeletionTool) |
| [hideuvpn/android-google-play-store](https://github.com/hideuvpn/android-google-play-store) | 3,681 | 超过 1576 天无代码提交 | [进入取消 Star](https://github.com/hideuvpn/android-google-play-store) |
| [XJP-GIT/AntiZhaPian](https://github.com/XJP-GIT/AntiZhaPian) | 3,164 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/XJP-GIT/AntiZhaPian) |
| [jerrykuku/luci-app-ttnode](https://github.com/jerrykuku/luci-app-ttnode) | 89 | 超过 1753 天无代码提交 | [进入取消 Star](https://github.com/jerrykuku/luci-app-ttnode) |
| [KevinSHIT/NaiveSharp](https://github.com/KevinSHIT/NaiveSharp) | 97 | 超过 2198 天无代码提交 | [进入取消 Star](https://github.com/KevinSHIT/NaiveSharp) |
| [prasmussen/gdrive](https://github.com/prasmussen/gdrive) | 8,938 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/prasmussen/gdrive) |
| [tostercx/GTAO_Booster_PoC](https://github.com/tostercx/GTAO_Booster_PoC) | 2,863 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/tostercx/GTAO_Booster_PoC) |
| [ilxp/luci-app-ikoolproxy](https://github.com/ilxp/luci-app-ikoolproxy) | 505 | 超过 608 天无代码提交 | [进入取消 Star](https://github.com/ilxp/luci-app-ikoolproxy) |
| [kiddin9/luci-app-dnsfilter](https://github.com/kiddin9/luci-app-dnsfilter) | 124 | 超过 641 天无代码提交 | [进入取消 Star](https://github.com/kiddin9/luci-app-dnsfilter) |
| [h31105/deployX.sh](https://github.com/h31105/deployX.sh) | 417 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/h31105/deployX.sh) |
| [jerrykuku/openwrt-package](https://github.com/jerrykuku/openwrt-package) | 147 | 超过 1105 天无代码提交 | [进入取消 Star](https://github.com/jerrykuku/openwrt-package) |
| [frainzy1477/luci-app-trojan](https://github.com/frainzy1477/luci-app-trojan) | 120 | 超过 2012 天无代码提交 | [进入取消 Star](https://github.com/frainzy1477/luci-app-trojan) |
| [atrandys/xray](https://github.com/atrandys/xray) | 89 | 超过 1719 天无代码提交 | [进入取消 Star](https://github.com/atrandys/xray) |
| [v2board/v2board](https://github.com/v2board/v2board) | 5,066 | 超过 968 天无代码提交 | [进入取消 Star](https://github.com/v2board/v2board) |
| [ShadowsocksR-Live/iShadowsocksR](https://github.com/ShadowsocksR-Live/iShadowsocksR) | 602 | 超过 927 天无代码提交 | [进入取消 Star](https://github.com/ShadowsocksR-Live/iShadowsocksR) |
| [SuperNG6/Aria2-Trackers](https://github.com/SuperNG6/Aria2-Trackers) | 309 | 超过 2118 天无代码提交 | [进入取消 Star](https://github.com/SuperNG6/Aria2-Trackers) |
| [kakaruoterl/vless_install](https://github.com/kakaruoterl/vless_install) | 29 | 超过 2276 天无代码提交 | [进入取消 Star](https://github.com/kakaruoterl/vless_install) |
| [stupidloud/nanopi-openwrt](https://github.com/stupidloud/nanopi-openwrt) | 5,509 | 超过 940 天无代码提交 | [进入取消 Star](https://github.com/stupidloud/nanopi-openwrt) |
| [atrandys/trojan](https://github.com/atrandys/trojan) | 1,055 | 超过 1308 天无代码提交 | [进入取消 Star](https://github.com/atrandys/trojan) |
| [programthink/zhao](https://github.com/programthink/zhao) | 14,169 | 超过 1929 天无代码提交 | [进入取消 Star](https://github.com/programthink/zhao) |
| [RPRX/v2ray-vless](https://github.com/RPRX/v2ray-vless) | 390 | 超过 1354 天无代码提交 | [进入取消 Star](https://github.com/RPRX/v2ray-vless) |
| [h2y/Shadowrocket-ADBlock-Rules](https://github.com/h2y/Shadowrocket-ADBlock-Rules) | 16,737 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/h2y/Shadowrocket-ADBlock-Rules) |
| [p4gefau1t/trojan-go](https://github.com/p4gefau1t/trojan-go) | 8,387 | 超过 851 天无代码提交 | [进入取消 Star](https://github.com/p4gefau1t/trojan-go) |
| [Jrohy/trojan](https://github.com/Jrohy/trojan) | 5,629 | 超过 942 天无代码提交 | [进入取消 Star](https://github.com/Jrohy/trojan) |
| [mellow-io/mellow](https://github.com/mellow-io/mellow) | 3,535 | 超过 1433 天无代码提交 | [进入取消 Star](https://github.com/mellow-io/mellow) |
| [Dawneng/luci-theme-atmaterial](https://github.com/Dawneng/luci-theme-atmaterial) | 11 | 超过 1485 天无代码提交 | [进入取消 Star](https://github.com/Dawneng/luci-theme-atmaterial) |
| [trojan-gfw/igniter](https://github.com/trojan-gfw/igniter) | 3,273 | 超过 1081 天无代码提交 | [进入取消 Star](https://github.com/trojan-gfw/igniter) |
| [openwrt-develop/luci-theme-atmaterial](https://github.com/openwrt-develop/luci-theme-atmaterial) | 68 | 超过 2429 天无代码提交 | [进入取消 Star](https://github.com/openwrt-develop/luci-theme-atmaterial) |
| [trojan-gfw/trojan-quickstart](https://github.com/trojan-gfw/trojan-quickstart) | 244 | 超过 2031 天无代码提交 | [进入取消 Star](https://github.com/trojan-gfw/trojan-quickstart) |
| [FunctionClub/ZBench](https://github.com/FunctionClub/ZBench) | 1,173 | 超过 2062 天无代码提交 | [进入取消 Star](https://github.com/FunctionClub/ZBench) |
| [veekxt/v2ray-template](https://github.com/veekxt/v2ray-template) | 749 | 超过 2274 天无代码提交 | [进入取消 Star](https://github.com/veekxt/v2ray-template) |
| [HMBSbige/ShadowsocksR-Windows](https://github.com/HMBSbige/ShadowsocksR-Windows) | 6,897 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/HMBSbige/ShadowsocksR-Windows) |
| [trojan-gfw/trojan](https://github.com/trojan-gfw/trojan) | 19,746 | 超过 813 天无代码提交 | [进入取消 Star](https://github.com/trojan-gfw/trojan) |
</details>
