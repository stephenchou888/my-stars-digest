# 📡 Starred 项目雷达看板
> 🖥️ **交互式管理看板 (shadcn/ui)**：[👉 点击进入在线雷达看板 (https://stephenchou888.github.io/my-stars-digest/)](https://stephenchou888.github.io/my-stars-digest/)

> **生成时间**：`2026-11-23` ｜ **关注项目总数**：`443` ｜ **本期更新**：`122` ｜ **弃坑预警**：`140`

| 统计指标 | 数量 | 状态提示 |
| :--- | :---: | :--- |
| 🌟 总关注库 | **443** | [进入 shadcn 在线看板管理](https://stephenchou888.github.io/my-stars-digest/) |
| 🚀 近期有更新 | **122** | 涵盖 6 个分类 |
| 🛑 建议清理/弃坑 | **140** | 建议取消 Star 保持关注列表整洁 |

---
## 🧭 领域分类速览导航

- [🤖 AI 与智能体生态 (70)](#-AI-与智能体生态)
- [🎬 影音媒体与下载 (18)](#-影音媒体与下载)
- [📝 效率办公与创作 (14)](#-效率办公与创作)
- [🌐 网络与代理技术 (10)](#-网络与代理技术)
- [📦 实用开源精选 (6)](#-实用开源精选)
- [🛠️ 系统与开发者工具 (4)](#-系统与开发者工具)

---

## <span id="-AI-与智能体生态">🤖 AI 与智能体生态</span>

### 📦 [nexu-io/open-design](https://github.com/nexu-io/open-design)
`⭐ Stars: 109,061` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [open-design-v0.27.2](https://github.com/nexu-io/open-design/releases/tag/open-design-v0.27.2) (2026-11-19)`

> **简介**：第一个协作式人工智能设计代理工作区。本地优先和开源。与您的团队和 AI 代理一起创建动作、原型、网站、应用程序、仪表板、演示文稿、图像和视频。在一个工作区中共享工作、交换反馈并进行迭代。

**💡 核心亮点更新 (中文)**：
- **Mac Windows 在显示更改后恢复清晰度。** 唤醒或显示器移动不再需要使应用程序以错误的比例拉伸；重新聚焦为渲染器提供了另一个匹配其所在显示器的机会。 (#9409)
- **已安装的 macOS 更新具有更稳定的交接。** 有效负载更新现在贯穿已安装应用程序的生命周期，因此失败的一代可以恢复，而不会因交接中断而陷入下一次启动。 (#8936) 谢谢。
- **配额重置时间保留重要的分钟数。** 当距离重置还有几天时，配额面板现在仍然会告诉您剩余的分钟数，而不是让截止日期感觉不那么精确。 (#9328)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
### 🌟 Codename: *Clearer Quotas, Sharper Displays*

0.27.2 is a focused reliability patch for the 0.27 line. No new surface—just clearer signals when a limit resets, a project action fails, a display changes, or a Mac app updates itself.

## 🐛 Fixed

### 🖥️ Desktop and presentation

- **Mac windows recover their sharpness after a display change.** A wake or monitor move no longer has to leave the app stretched at the wrong scale; refocusing gives the renderer another chance to match the display it is on. (#9409)
- **Installed macOS updates have a steadier handoff.** Payload updates now run through the installed app’s lifecycle, so a failed generation can recover without trapping the next launch on a broken handoff. (#8936) Thanks @PerishCode.

### 💳 Workspace and billing

- **Quota reset times keep the minutes that matter.** When a reset is days away, the quota panel now still tells you the remaining minutes instead of making the deadline feel less precise than it is. (#9328)
- **A failed move to team space now looks like a failure.** Project-card menu errors use the same clear error treatment as the rest of the workspace, so the next action is easier to judge. (#9409)

> 📥 **Download:** Tag `open-design-v0.27.2`.
>
> | Platform | Architecture | Assets |
> |---|---|---|
> | macOS | Apple silicon | [DMG](https://github.com/nexu-io/open-design/releases/download/open-design-v0.27.2/open-design-0.27.2-mac-arm64.dmg) · [SHA-256](https://github.com/nexu-io/open-design/releases/down
```
</details>

---
### 📦 [Likely7/Veyra-NRVideo](https://github.com/Likely7/Veyra-NRVideo)
`⭐ Stars: 5,519` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.2.0](https://github.com/Likely7/Veyra-NRVideo/releases/tag/v2.2.0) (2026-11-20)`

> **简介**：通过 DLSS 5 将 PS5 GTA6 提升至 120FPS。先进的 Windows 视频播放器和捕捉增强工具，具有视频、图像和捕捉卡源的实时预览功能。结合 AI 驱动的超分辨率、DLSS5 图像增强和帧生成，提供下一代视觉体验。

**💡 核心亮点更新 (中文)**：
- Windows 11 x64、DirectX 12。选 Veyra 实际使用的 GPU 的包。安装器可选择路径和桌面快捷方式，开始菜单和 Windows「已安装的应用」提供卸载入口。便携版解压到新建的可写目录，运行根目录的 **Veyra.exe**。
- 从旧便携版升级时，关闭旧版后按需复制 `runtime_local/user-data-2.0.0` 和 `runtime_local/luts` 到新目录的 `runtime_local`。同分版安装器可在原路径覆盖安装。已装 2.2.0 测试版的用户请用本页正式安装器覆盖一次，以取得内置发行公钥。
- 「设置 → 关于 → 检查更新」支持验证并下载之后的稳定版，正常退出后应用，启动失败时可回退。下载线路可选 GitHub、GH-Proxy 和 GHFast。镜像失败时重试直连，更新清单使用 Ed25519 签名，程序另外核对 ZIP 的包型、大小和 SHA-256。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Windows 安装器、实时字幕翻译、虚拟摄像机、全屏缩放，以及从 2.1.9 以来的采集、串流、录制和导出修复。

## 下载与升级 / Download and upgrade

| Veyra 使用的显卡 / GPU | 安装器 / Setup | 便携版 / Portable |
| --- | --- | --- |
| NVIDIA | [NVIDIA Setup EXE](https://github.com/Likely7/Veyra-NRVideo/releases/download/v2.2.0/Veyra-2.2.0-NVIDIA-win64-setup.exe) | [NVIDIA ZIP](https://github.com/Likely7/Veyra-NRVideo/releases/download/v2.2.0/Veyra-2.2.0-NVIDIA-win64-portable.zip) |
| AMD | [AMD Setup EXE](https://github.com/Likely7/Veyra-NRVideo/releases/download/v2.2.0/Veyra-2.2.0-AMD-win64-setup.exe) | [AMD ZIP](https://github.com/Likely7/Veyra-NRVideo/releases/download/v2.2.0/Veyra-2.2.0-AMD-win64-portable.zip) |

- Windows 11 x64、DirectX 12。选 Veyra 实际使用的 GPU 的包。安装器可选择路径和桌面快捷方式，开始菜单和 Windows「已安装的应用」提供卸载入口。便携版解压到新建的可写目录，运行根目录的 **Veyra.exe**。
- 从旧便携版升级时，关闭旧版后按需复制 `runtime_local/user-data-2.0.0` 和 `runtime_local/luts` 到新目录的 `runtime_local`。同分版安装器可在原路径覆盖安装。已装 2.2.0 测试版的用户请用本页正式安装器覆盖一次，以取得内置发行公钥。
- 「设置 → 关于 → 检查更新」支持验证并下载之后的稳定版，正常退出后应用，启动失败时可回退。下载线路可选 GitHub、GH-Proxy 和 GHFast。镜像失败时重试直连，更新清单使用 Ed25519 签名，程序另外核对 ZIP 的包型、大小和 SHA-256。
- 这次 Windows 安装器尚未做 Authenticode 发布者签名。可按 [SHA256SUMS.txt](https://github.com/Likely7/Veyra-NRVideo/releases/download/v2.2.0/SHA256SUMS.txt) 核对下载文件。

Use the package for the GPU selected by Veyra. Run Setup or extract the portable ZIP into a writable folder and run **Veyra.exe**. To carry settings forward from the old portable layout, copy the data and LUT folders above after closing Veyra. Settings → About offers sig
```
</details>

---
### 📦 [open-webui/open-webui](https://github.com/open-webui/open-webui)
`⭐ Stars: 159,313` &nbsp;|&nbsp; `💻 语言: Svelte` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.13.4](https://github.com/open-webui/open-webui/releases/tag/v0.13.4) (2026-11-17)`

> **简介**：用户友好的 AI 界面（支持 Ollama、OpenAI API...）

**💡 核心亮点更新 (中文)**：
- **使用 Tether 自带您自己的计算机。** Tether 将您自己的计算机变成 Open WebUI 的一部分：来自 Ollama、LM Studio 或任何 OpenAI 兼容服务器的模型、您在 Tether 应用程序中添加的 OpenAPI 和 MCP 工具服务器以及开放终端服务器现在仅显示在模型选择器中、+ 菜单的工具列表以及您连接的任何 Open WebUI 的终端菜单中，无论您在什么设备上打开它，并且 Open WebUI 通过 Tether 访问它们，因此它们的地址、命令和密钥永远不会离开你的电脑。这需要 Tether 0.1.14 或更高版本，或者 MCP 服务器需要 0.1.16，工具服务器和终端需要打开“ENABLE_TOOL_SERVERS”，并且 ID 与 Open WebUI 中已有模型匹配的 Tether 模型保持隐藏。 Tether 取代了直接连接。 [#34397](https://github.com/open-webui/open-webui/issues/34397)
- **您自己计算机上的沙盒代理。** Tether 0.1.13 或更高版本可以将计算机上的终端锁定到沙箱中，因此模型和编码代理可以在您的真实文件中工作，而无需到达计算机的其余部分：在 macOS 和支持的 Windows 设备上，打开终端及其启动的所有内容（包括编码代理）只能接触您选择的一个文件夹，离线运行，除非您打开网络访问并且不接受任何传入连接，无需 Docker、虚拟机或管理员设置。如果沙箱无法强制执行，终端将保持停止状态，而不是在没有沙箱的情况下安静地运行，并且浏览器和桌面控制在打开时保持关闭状态。在 Tether 中的“设置”>“打开终端”>“沙盒”下将其打开。
- **通过 Tether 实现本地 MCP 服务器。** Open WebUI 现在可以使用通过 stdio（许多 MCP 服务器的分布方式）作为本地命令运行的 MCP 服务器，通过 Tether 0.1.16 或更高版本在计算机上启动它们，无需 mcpo 等代理，也无需打开端口。在“设置”>“集成”>“工具”下的 Tether 中使用其命令添加一个，或通过其 Web 地址连接 MCP 服务器，然后从 + 菜单的“工具”列表中选择它。 L

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
### Added

- **Bring your own computer with Tether.** Tether turns your own computer into part of Open WebUI: models from Ollama, LM Studio or any OpenAI-compatible server, OpenAPI and MCP tool servers and Open Terminal servers that you add in the Tether app now show up just for you in the model selector, the Tools list of the + menu and the terminal menu of any Open WebUI you connect, from whatever device you open it on, and Open WebUI reaches them through Tether, so their addresses, commands and keys never leave your computer. This needs Tether 0.1.14 or later, or 0.1.16 for MCP servers, tool servers and terminals need "ENABLE_TOOL_SERVERS" turned on, and a Tether model whose ID matches a model already in Open WebUI stays hidden. Tether replaces Direct Connections. [#34397](https://github.com/open-webui/open-webui/issues/34397)
- **Sandboxed agents on your own computer.** Tether 0.1.13 or later can lock the terminal on your computer into a sandbox, so models and coding agents work in your real files without reaching the rest of your machine: on macOS and supported Windows devices, Open Terminal and everything it launches, coding agents included, can only touch the one folder you pick, run offline unless you turn on Network access and accept no incoming connections, with no Docker, virtual machine or administrator setup needed. If the sandbox cannot be enforced, the terminal stays stopped instead of quietly running without it, and browser and desktop control stay off while
```
</details>

---
### 📦 [NVIDIA/SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator)
`⭐ Stars: 4,424` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.0.1](https://github.com/NVIDIA/SkillEvaluator/releases/tag/v1.0.1) (2026-11-18)`

> **简介**：用于评估 AI 代理技能和插件的多层框架，包括质量门、安全扫描、线束兼容性检查、语义重叠检测、综合评估数据集生成以及衡量技能如何影响代理行为的实时代理评估。提供可重用的 CI 模板，将每次检查带到任何存储库。

**💡 核心亮点更新 (中文)**：
- **HarnessCheck：**查找可能导致您的技能在 **Claude Code、Codex、Copilot CLI、Hermes、OpenClaw 和 OpenCode** 中被遗漏、拒绝或截断的兼容性问题。版本化配置文件检查发现路径、前言、描述和内容限制、调用设置、插件组件以及与其他已安装技能的冲突。研究结果解释了每个安全带的作用以及如何修复它。运行“skillvaluatorharness-check./my-skill”，或在第 1 层报告中查看结果。这些静态检查不需要模型密钥，并且在默认策略下是建议性的。 [HarnessCheck 指南](https://docs.nvidia.com/skills/skillevaluator/harness-check)
- **NeMo Gym 集成：** 使用“--backend nemo-gym”运行第 3 层评估，使用共享评分和报告。 [所需设置](https://docs.nvidia.com/skills/skillevaluator/tier3-runtime#execution-backends)
- **更多地控制质量：**使用“--quality-config”配置代币预算、描述限制、保留名称术语和分数扣除。使用“--profileregistry”来满足更严格的作者和技能 ID 要求。 [质量规则](https://github.com/NVIDIA/SkillEvaluator/pull/611) · [注册政策](https://github.com/NVIDIA/SkillEvaluator/pull/499)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
> 🎉 **Introducing SkillEvaluator v1.0.1, our first complete release in the 1.0 series.**

Understand how your skills load, measure how they perform, and bring automated evaluation into your workflow with **HarnessCheck**, **NeMo Gym integration**, and improved **agent-assisted evaluation and repository CI**.

**[PyPI v1.0.1](https://pypi.org/project/skillevaluator/1.0.1/) · [Download CI bundle v1.0.1](https://github.com/NVIDIA/SkillEvaluator/releases/download/v1.0.1/skillevaluator-ci-1.0.1.zip) · [Documentation](https://docs.nvidia.com/skills/skillevaluator/)**

## Highlights

- **HarnessCheck:** find compatibility issues that can cause your skill to be missed, rejected, or truncated across **Claude Code, Codex, Copilot CLI, Hermes, OpenClaw, and OpenCode**. Versioned profiles check discovery paths, frontmatter, description and content limits, invocation settings, plugin components, and conflicts with other installed skills. Findings explain what each harness does and how to fix it. Run `skillevaluator harness-check ./my-skill`, or see the results in Tier 1 reports. These static checks need no model key and are advisory under the default policy. [HarnessCheck guide](https://docs.nvidia.com/skills/skillevaluator/harness-check)
- **NeMo Gym integration:** run Tier 3 evaluations with `--backend nemo-gym`, using shared grading and reports. [Required setup](https://docs.nvidia.com/skills/skillevaluator/tier3-runtime#execution-backends)
- **More control over quality:** configure to
```
</details>

---
### 📦 [Tencent/LoopForge](https://github.com/Tencent/LoopForge)
`⭐ Stars: 5,787` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.4.0](https://github.com/Tencent/LoopForge/releases/tag/v0.4.0) (2026-11-17)`

> **简介**：用于编码代理交付的自托管工作流程。使用脚本和人工审批门来编排 CodeBuddy、Codex 和 Claude Code。包括编码助理的本地工作流程。

**💡 核心亮点更新 (中文)**：
* feat(chat)：通过 https://github.com/Tencent/LoopForge/pull/183 安装对话失败时丢失的 CLI
* feat(git)：通过 https://github.com/Tencent/LoopForge/pull/207 支持带有每个主机用户密钥的 SSH 存储库
* 修复（安全）：限制代理 CLI 配置通过 https://github.com/Tencent/LoopForge/pull/209 写入 home

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Install

```bash
git clone --branch v0.4.0 https://github.com/Tencent/LoopForge.git
cd LoopForge
./start.sh
```

Platform image: `ghcr.io/tencent/loopforge:0.4.0` (pinned in `compose.yaml`).

Digest: `ghcr.io/tencent/loopforge@sha256:87b6a3e3cba201d03f8f8d22929881f576021fc78c7c42e82f78329abbf4bda4`.

Where `ghcr.io` is slow, set `MIRROR` to a registry host that replaces it (for example `MIRROR=ghcr.nju.edu.cn ./start.sh`). This trusts that host: the download is tagged as the pinned name. Check it with `docker image inspect --format '{{index .RepoDigests 0}}' ghcr.io/tencent/loopforge:0.4.0` and compare the digest after `@`. Existing installations: check out `v0.4.0`, run `./start.sh`, and apply the new files under `migrations/` listed in [CHANGELOG.md](https://github.com/Tencent/LoopForge/blob/v0.4.0/CHANGELOG.md).

## Upgrading from 0.3.9-rc.1

0.4.0 includes everything in the `v0.3.9-rc.1` prerelease. 0.3.9 will not get a final release, so installations on `v0.3.9-rc.1` can upgrade straight to 0.4.0.

## What's Changed
* feat(chat): install a missing CLI from the conversation failure by @crispinhu27 in https://github.com/Tencent/LoopForge/pull/183
* feat(git): support SSH repositories with per-host user keys by @crispinhu27 in https://github.com/Tencent/LoopForge/pull/207
* fix(security): confine agent CLI config writes to home by @crispinhu27 in https://github.com/Tencent/LoopForge/pull/209
* fix(repo): keep credentials out of repository clone URLs by @Robert0622 in htt
```
</details>

---
### 📦 [Pabldi08/AirSend](https://github.com/Pabldi08/AirSend)
`⭐ Stars: 76` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.3.0](https://github.com/Pabldi08/AirSend/releases/tag/v0.3.0) (2026-11-13)`

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
`⭐ Stars: 79,399` &nbsp;|&nbsp; `💻 语言: Dart` &nbsp;|&nbsp; `🏷️ 最新版本: [0.15.1](https://github.com/AppFlowy-IO/AppFlowy/releases/tag/0.15.1) (2026-11-15)`

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
`⭐ Stars: 47,347` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.8.11](https://github.com/siyuan-note/siyuan/releases/tag/v3.8.11) (2026-11-19)`

> **简介**：An open-source, privacy-first, self-hosted knowledge workspace where humans and AI agents work together 开源、隐私优先、自托管的知识工作空间，让人与智能体在此协作

**💡 核心亮点更新 (中文)**：
升级通知

数据库格式

- **主键富文本（格式 15 和 16）。** 早期预览版本以格式 15 保存的内联富文本仍然可读。在主键中保存新的块富文本，包括带图像的文本，升级

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Upgrade notice

### Database formats

- **Primary-key rich text (formats 15 and 16).** Inline rich text saved in format 15 by earlier preview builds remains readable. Saving new block rich text in a primary key, including text with images, upgrades the database to at least format 16. [Primary-key compatibility](https://github.com/siyuan-note/siyuan/issues/21136)
- **Inline images in ordinary text fields (format 17).** Saving the first inline image in an ordinary text field upgrades that database to format 17. [Text field compatibility](https://github.com/siyuan-note/siyuan/issues/21527)

Simply opening a database does not trigger these upgrades. Version 3.8.10 supports database formats up to 14. A client can only open databases in formats it supports. Update every device that syncs or accesses the same data before using the new formats. Back up your workspace beforehand. To roll back, restore a complete pre-upgrade snapshot.

### Other compatibility changes

- **AI long-term memory.** Restoring a workspace snapshot now rolls back both memory records and their revocation state. Restoring a snapshot from before a memory was forgotten can make it available again if it still passes the usual validity checks. [Long-term memory](https://github.com/siyuan-note/siyuan/blob/64fe75eb55fc783a345ea00fb4db8b60268dd65c/docs/LONG-TERM-MEMORY.md)
- **Kernel API.** JSON requests handled by API contracts have a 32 MiB body limit, with a 64 KiB limit for `loginAuth`. Requests exc
```
</details>

---
### 📦 [Jarvis322/macos-sysdata](https://github.com/Jarvis322/macos-sysdata)
`⭐ Stars: 2,313` &nbsp;|&nbsp; `💻 语言: Swift` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.13.1](https://github.com/Jarvis322/macos-sysdata/releases/tag/v1.13.1) (2026-11-12)`

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
`⭐ Stars: 9,052` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.4.1](https://github.com/openfilm/openfilm/releases/tag/v0.4.1) (2026-11-20)`

> **简介**：开源人工智能视频代理：将任何编码代理变成视频代理，编辑人员可以更改其制作的任何内容。

**💡 核心亮点更新 (中文)**：
- **更快的时间线预览。** 浏览可用帧并释放以赋予所选位置优先权。 Studio 可以在章节打开时显示缓存的帧，在播放期间预加载即将出现的页面，并在预览赶上时保持上一张图片可见。图片上的加载消息消失了。
- **导出时间线范围。** 使用“I”和“O”或“时间范围”菜单设置入点和出点。在 macOS 上使用“⌘M”或在 Windows 上使用“Ctrl+M”打开导出以导出标记的范围。
- **继续中断的任务。** 使用在作曲家中选择的模型和推理工作，停止任务并在同一对话中恢复它。如果您切换代理，新代理将获取原始请求并保存进度。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
OpenFilm 0.4.1 makes timeline previews more responsive, adds export for a marked range, and makes it easier to continue work after an interruption.

## Highlights

- **Faster timeline previews.** Scrub through available frames and release to give the chosen position priority. Studio can show a cached frame while a chapter opens, preloads upcoming pages during playback, and keeps the previous picture visible while the preview catches up. The loading message over the picture is gone.
- **Export a timeline range.** Set the in and out points with `I` and `O` or the Time Range menu. Open Export with `⌘M` on macOS or `Ctrl+M` on Windows to export the marked range.
- **Continue an interrupted task.** Stop a task and resume it in the same conversation using the model and reasoning effort selected in the composer. If you switch agents, the new agent gets the original request and saved progress.
- **Smoother editing.** Drag a clip over the middle of another to preview a replacement or near an edge to insert it. Linked clips follow the main track as it moves, and selecting a marker previews its frame before playback starts there.

Thanks to everyone who sent reports and pull requests. Thanks especially to @hobostay for the fix that prevents Studio from getting stuck while trimming edit history. [#505](https://github.com/openfilm/openfilm/pull/505)

## Install or update

Run `npx -y openfilm@latest` for the CLI, or download the desktop installer from Assets below. Existing desktop instal
```
</details>

---
### 📦 [Parcha-ai/agentrun](https://github.com/Parcha-ai/agentrun)
`⭐ Stars: 1,258` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [cli-v0.1.10](https://github.com/Parcha-ai/agentrun/releases/tag/cli-v0.1.10) (2026-11-06)`

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
`⭐ Stars: 58,919` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [chrome-devtools-mcp-v1.13.0](https://github.com/ChromeDevTools/chrome-devtools-mcp/releases/tag/chrome-devtools-mcp-v1.13.0) (2026-11-11)`

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
`⭐ Stars: 523` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [extension/0.1.5](https://github.com/y5ez3g/facadecode/releases/tag/extension/0.1.5) (2026-11-14)`

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
`⭐ Stars: 25,233` &nbsp;|&nbsp; `💻 语言: Other` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.0.1](https://github.com/GoogleChrome/modern-web-guidance/releases/tag/v1.0.1) (2026-11-16)`

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
`⭐ Stars: 7,888` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.2.0](https://github.com/Lee-xeo/Claude-Cage/releases/tag/v0.2.0) (2026-11-22)`

> **简介**：Cage：为 Claude 特化的轻量化虚拟机，彻底杜绝网络泄露。多平台适配，支持多账号管理、远程部署、移动端操控。

**💡 核心亮点更新 (中文)**：
- **默认隔离环境调整为纯终端 Debian 13。** 既有环境与个人数据（`~/.claude-cage`）保留不变，升级不会清空账户、会话历史或持久磁盘；如需全新环境说明，请参考 [环境系统说明](https://claude-cage.com/docs/guest-systems/)。需要本机软件与桌面能力时，请使用插件。
- **Windows v0.1.7 及更早版本用户**请从本版本附件下载安装程序，退出 Cage 后手动安装；详细步骤见 [Windows 使用指南](https://claude-cage.com/docs/windows/)。
- **Intel Mac 支持。** 源码构建、打包校验与应用内更新链路已纳入 Intel Mac 正式支持范围；本版本附件提供 Apple Silicon（`arm64`）官方签名公证 DMG、Windows 签名安装包、Linux Debian 软件包及 Android 官方签名 APK。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# Cage v0.2.0

Cage v0.2.0 正式发布，带来完整的插件平台与插件市场、远程主机与本机 SSH 导入、虚拟机硬盘上限手动增减、工作台视觉与交互全面升级、多账号与独立 Claude Desktop 实例强化、更广泛的代理与出口兼容能力，以及 14 语种本地化全面完善。

## 重要变更与升级提示

- **默认隔离环境调整为纯终端 Debian 13。** 既有环境与个人数据（`~/.claude-cage`）保留不变，升级不会清空账户、会话历史或持久磁盘；如需全新环境说明，请参考 [环境系统说明](https://claude-cage.com/docs/guest-systems/)。需要本机软件与桌面能力时，请使用插件。
- **Windows v0.1.7 及更早版本用户**请从本版本附件下载安装程序，退出 Cage 后手动安装；详细步骤见 [Windows 使用指南](https://claude-cage.com/docs/windows/)。
- **Intel Mac 支持。** 源码构建、打包校验与应用内更新链路已纳入 Intel Mac 正式支持范围；本版本附件提供 Apple Silicon（`arm64`）官方签名公证 DMG、Windows 签名安装包、Linux Debian 软件包及 Android 官方签名 APK。

## 主要改进

- **插件平台、插件市场与默认预装能力。**
  - 环境内的 Claude 可通过插件调用本机工具或运行在环境内的插件；支持插件市场检索、分类筛选、引擎切换、安装/更新/卸载、单工具细粒度启停、插件设置与密钥配置，以及本机调用前审批与记住授权。
  - 新增默认预装可卸载插件、内置 `cage-plugin`（查找与创建插件）及受控 `use-cage` 插件；支持远程主机插件运行、自动增量同步、审批回流与本机插件反向桥接。
  - 支持编号 Claude Desktop MCP 配置同步，以及在终端中通过斜杠显式调用 MCP Prompts。
- **虚拟机资源：手动调整硬盘空间上限（扩容与释放）。**
  - 在「设置 → 资源」中新增「硬盘上限」配置项（与 CPU、内存并列），实时显示本次启动的硬盘上限、环境内用量与宿主机实际磁盘占用。
  - 调大上限后客机启动自动扩展根分区与文件系统；调小上限带安全余量校验与二次确认，通过离线缩容、GPT 分区表迁移、`fstrim` 与宿主镜像空洞回收/重压缩（macOS APFS `F_PUNCHHOLE`、Linux `fallocate`、QEMU `qcow2`）安全释放宿主磁盘空间，并在执行前自动备份、失败自动回滚。
- **工作台视觉与交互升级。**
  - 全面打磨工作台首页、账户、账号管理、设置与代理节点分组的视觉设计语言，简化就绪页卡片，清理侧栏操作按钮冗余内联悬停文字（保留纯图标与悬浮气泡提示）。
  - 工作台侧栏支持鼠标拖拽调整宽度（`216px–520px` 且自适应视口上限，双击恢复默认宽度并持久化保存，支持键盘无障碍调节）。
  - Windows 系统托盘右键菜单外观升级并与应用主题配色自动同步。
- **远程主机与独立 Claude Desktop 实例。**
  - 支持从本机 `~/.ssh/config` 直接导入远程主机，固定 SSH 主机公钥时按公钥类型准确限定协商算法。
  - 支持多账号共享会话历史、记忆、技能、指令与钩子（登录凭据与组织托管内容保持隔离），支持安全
```
</details>

---
### 📦 [duyunzhoudyz/dyz-gongwen-skills](https://github.com/duyunzhoudyz/dyz-gongwen-skills)
`⭐ Stars: 958` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.2.0](https://github.com/duyunzhoudyz/dyz-gongwen-skills/releases/tag/v1.2.0) (2026-11-22)`

> **简介**：公文写作 Skills｜AI 公文写作助手：防编造、守保密、GB/T 9704 一键排版，覆盖 22 种文书，支持 Claude Code / Codex / Cursor

**💡 核心亮点更新 (中文)**：
- **去 Agent 化三档交付与内网知识库**：
- `dist/prompts-lite/`：22 份 ≤4000 字手写精修精简版（适配内网模型 4K～8K 系统提示词框限制）。
- `dist/prompts-bundles/`：4 套高频一站式单对话合集（法定公文、综合材料、核稿润色、落实整改），不用反复切换对话。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# dyz-gongwen-skills v1.2.0

> **保密提示**
>
> 涉密信息严禁输入任何联网 AI 工具。带密级标识、标注“内部资料”“工作秘密”的材料，不要粘贴到任何公网大模型。处理内部材料请用单位内网部署的模型，本项目的提示词版、信创工具箱和离线包（`dyz-gongwen-skills-offline-1.2.0.zip`）可以直接在政务内网使用。完整说明见 [使用须知](https://github.com/duyunzhoudyz/dyz-gongwen-skills/blob/main/使用须知.md)。

> **升级提示（RAG 知识库用户）**
>
> `dist/rag-kb/chunks` 在 v1.2.0 中新增规范用词分块并整体重新编号（如 `09-ai-tone.md` 改为 `10-ai-tone.md`）。已向 FastGPT、MaxKB 导入过旧分块的，请先删除旧知识库条目再导入，避免重复。

---

## 本版亮点

v1.2.0 是一次面向**政务内网与国产信创落地、日常轻快件效率、综合长文笔力与规范用词、五个行业包深度加固**的全链路升级（全仓库 2115 项单元测试、零外联 AST 静态审计及全部 CI 门禁通过）：

### 一、国产信创与政务内网全链路适配
面向银河麒麟、统信 UOS + WPS 及禁用自主智能体的政务内网环境：
- **去 Agent 化三档交付与内网知识库**：
  - `dist/prompts-lite/`：22 份 ≤4000 字手写精修精简版（适配内网模型 4K～8K 系统提示词框限制）。
  - `dist/prompts-bundles/`：4 套高频一站式单对话合集（法定公文、综合材料、核稿润色、落实整改），不用反复切换对话。
  - `dist/rag-kb/`：16 个切片文件共 461 片标准知识片，附 Dify 应用模板（`dify-app-template.yml`，已关闭 Agent 模式）、FastGPT / MaxKB QA 导入 CSV 与扣子开源版导入指引。
- **本机零联网工具箱（`xinchuang/local_toolbox.py`）与双向脱敏**：
  - 附双击启动器（`xinchuang/启动工具箱.sh`、`.desktop`、`.bat`），仅监听 `127.0.0.1:8765`，不联网、不调模型、不落盘；一页集成一键复制内网提示词、直接导入 `.docx`/`.txt`、涉密强拦截、多标签页隔离双向脱敏还原（`shared/scripts/desensitize.py`）、八关机检与文风指纹体检、事实数字核对、**7 档行业专检**、字体自检、HTML 轻排版、国标 Word 排版与 OFD 结构体检。
- **零依赖轻量排版、免宏模板、信创字体与 OFD 体检**：
  - 新增纯 Python 标准库 GB/T 9704 轻量排版 `xinchuang/lite_docx.py`（无 `python-docx`/`lxml` 时自动降级，含龙芯等架构）；新增 `xinchuang/templates/` 5 套免 Python、免宏空白 `.docx` 模板（白头、红头、纪要、签报、综合材料）。
  - `gw_fonts.py` 增加信创字体兜底扫描与方正 GBK 预设；新增兼容 WPS Linux 的 `wps_gongwen_macro.js`、OFD 结构体检脚本 `ofd_check.py`
```
</details>

---
### 📦 [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop)
`⭐ Stars: 26,230` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.3.1](https://github.com/vercel-labs/agent-desktop/releases/tag/v1.3.1) (2026-11-13)`

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
`⭐ Stars: 1,798` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [baocut-v3.20.2-build.100](https://github.com/JimLiu/baocut/releases/tag/baocut-v3.20.2-build.100) (2026-11-23)`

> **简介**：BaoCut：具有可编辑时间线的人工智能视频代理。转录、字幕、翻译、配音、剪辑和动画。

**💡 核心亮点更新 (中文)**：
- **反重力工具和批准：** BaoCut 现在使用 `agy acp`，连接 BaoCut 工具并支持 Plan、Ask 和 Full Access 模式。 BaoCut 工具不再要求第二次本地批准。使用“agy update”将 Antigravity CLI 更新到 **1.5.10 或更高版本**。 [来源](https://github.com/jimliu/baocut/commit/1d01a5d1ab23ef38c879139407010c93dca7dd8e)
- **会话连续性：** 现有的反重力本机对话可以通过 ACP 恢复。创建本机会话时，开发人员说明会输入系统提示符，并且在恢复时不会重复。对这些指令的更改需要新的本机会话。 [来源](https://github.com/jimliu/baocut/commit/1d01a5d1ab23ef38c879139407010c93dca7dd8e)
- **模型和安装：** 模型切换保留推理级模型 ID，推荐使用 Flash 模型，并且 Windows 可以识别 Antigravity 的官方安装程序位置，包括重新定位的用户配置文件。 [来源](https://github.com/jimliu/baocut/commit/1d01a5d1ab23ef38c879139407010c93dca7dd8e)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Changes in 3.20.2 (Build 100)

- **Antigravity tools and approvals:** BaoCut now uses `agy acp`, connecting BaoCut tools and supporting Plan, Ask and Full Access modes. BaoCut tools no longer ask for a second native approval. Update Antigravity CLI to **1.5.10 or later** with `agy update`. [Source](https://github.com/jimliu/baocut/commit/1d01a5d1ab23ef38c879139407010c93dca7dd8e)
- **Session continuity:** Existing Antigravity native conversations can resume through ACP. Developer instructions enter the system prompt when a native session is created and are not duplicated on resume. Changes to those instructions require a new native session. [Source](https://github.com/jimliu/baocut/commit/1d01a5d1ab23ef38c879139407010c93dca7dd8e)
- **Models and installation:** Model switching preserves reasoning-level model IDs, Flash models are recommended, and Windows recognizes Antigravity's official installer location, including relocated user profiles. [Source](https://github.com/jimliu/baocut/commit/1d01a5d1ab23ef38c879139407010c93dca7dd8e)
- **Background commands:** Antigravity turns stay open while commands run in the background, retaining their results and the agent's follow-up. Interrupt cancels the waiting turn; daemon commands and scheduled tasks do not keep it open. [Source](https://github.com/jimliu/baocut/commit/3281f0a20b32b07b42d59d9638c8ed2b3ac0ee2e)

### Known limits

- Antigravity has no steer support: messages sent while a background command runs stay queued until the t
```
</details>

---
### 📦 [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)
`⭐ Stars: 26,982` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.1.177](https://github.com/milind-soni/OpenMausBot/releases/tag/v0.1.177) (2026-11-22)`

> **简介**：开源 Grok Bot 替代品，带有机器人可以使用的虚拟机

**💡 核心亮点更新 (中文)**：
- **查看您的机器人彼此说了些什么。** 当机器人将工作交给队友时，交接会显示为带有队友脸部和姓名的小芯片。单击它即可在聊天中实时阅读他们的对话，然后单击“返回”即可返回到您所在的位置。
- **交接的对话具有真实姓名。** 队友打开的对话以所交接的工作命名。
- **推理坚持。** 在简单模式下，在机器人面板中选择推理级别现在也会使其成为机器人的默认级别，就像模型一样。新的对话从该级别开始。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## What's new in 0.1.177

### Bots and work
- **See what your bots said to each other.** When a bot hands work to a teammate, the hand-off shows as a small chip with the teammate's face and name. Click it to read their conversation right in the chat, live, with "Back" to return to where you were.
- **Handed-off conversations get real names.** A conversation a teammate opens is named after the job it was handed.
- **Reasoning sticks.** In Simple mode, picking a Reasoning level in a bot's panel now also makes it that bot's default, the same way Model does. New conversations start at that level.
- **Chief of Staff mail checks** also read your connected Outlook.
- **A failed turn says why it ended** in its summary.
- **Codex "Compact now"** compacts the conversation in place.
- **Your project's skills win.** With "Use my Claude Code skills" on, a project skill takes priority over your own skill of the same name.
- **Lighter isolated Claude turns:** they no longer load your `~/.claude/rules`.

### Models and providers
- **Gemini 4 Neon** works in Antigravity with its thinking levels, including model names that carry the level (such as "-high").
- **Google AI Studio** is in the main provider list.
- **Devin and other ACP engines** keep their model list when reading it runs slow, and the picker says why a list couldn't be read.
- **DeepSeek's spoken replies** play correctly.

### Vault
- **Bitwarden Secrets Manager** can be a Vault and sign-in source.
- **Getting ready for larger se
```
</details>

---
### 📦 [yuchen-ya/reelterminal](https://github.com/yuchen-ya/reelterminal)
`⭐ Stars: 26` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.5.0](https://github.com/yuchen-ya/reelterminal/releases/tag/v1.5.0) (2026-11-17)`

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
`⭐ Stars: 6,342` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.10.0](https://github.com/KKKKhazix/agent-autoloop/releases/tag/v1.10.0) (2026-11-23)`

> **简介**：让你的命令行 Agent 在后台自己接活、自己跟进到底；平时不烦你，遇到拿不准的事才发卡片找你拍板。

**💡 核心亮点更新 (中文)**：
- 每个工作人员轮询现在仅查看仍在进行中的运行，而不是遍历每个过去的运行目录。由于有数千个旧目录（在 Windows 上可见），磁盘读取使在同一进程中运行的集线器陷入停滞，并且工作线程不断被标记为脱机；未完成的运行现在在启动时恢复一次，以后的轮询不依赖于存在多少旧目录，并且过期的日志会在后台清除（#383）。
- `ops/delivery.json` 中以 `**` 结尾的路径模式（例如 `docs/**`）现在涵盖了它下面的每个级别。它过去只匹配第一级，因此像“docs/a/b.md”这样的文件被视为需要发布的更改，而“review.xhigh”下列出的目录会跳过更深的文件（#379）。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 改了什么

- 接单程序每一轮只看还在进行的任务，不再把历史任务目录挨个翻一遍。历史目录攒到几千个时（Windows 上遇到过），同一进程里的中台会被读盘拖住、接单程序被反复判成离线；现在启动时一次性恢复没做完的任务，之后的轮询不再受历史目录多少影响，过期日志在后台清理（#383）。
- 交付配置 `ops/delivery.json` 里以 `**` 结尾的路径（比如 `docs/**`）现在覆盖下面所有层级。以前只匹配第一层，`docs/a/b.md` 这类深一层的文件会被当成要发版的改动，`review.xhigh` 里写的目录也会漏掉更深的文件（#379）。

感谢 yaoyouzhong、xdAsaah、argszero。

## What's changed

- Each worker poll now looks only at runs still in progress instead of walking every past run directory. With thousands of old directories (seen on Windows), disk reads stalled the hub running in the same process and the worker kept being marked offline; unfinished runs are now recovered once at startup, later polls don't depend on how many old directories exist, and expired logs are cleaned up in the background (#383).
- A path pattern ending in `**` in `ops/delivery.json` (such as `docs/**`) now covers every level below it. It used to match only the first level, so a file like `docs/a/b.md` was treated as a change needing a release, and directories listed under `review.xhigh` skipped deeper files (#379).

Thanks to yaoyouzhong, xdAsaah and argszero.
```
</details>

---
### 📦 [alchaincyf/huashu-motion](https://github.com/alchaincyf/huashu-motion)
`⭐ Stars: 3,041` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.6.1](https://github.com/alchaincyf/huashu-motion/releases/tag/v0.6.1) (2026-11-23)`

> **简介**：让你的agent一键直出商业级产品宣传片：会作曲，能指着画面改。Commercial-grade launch films by your coding agent — point at the frame to change it.

**💡 核心亮点更新 (中文)**：
- 当真实文件名仅包含“om-”时，“om check --source”不再警告“no-real-material”（例如“materials/zoom-in.png”、“assets/bottom-bar.png”、“custom-chart.png”）。媒体过滤器现已固定。谢谢（#5）。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Fix

- `om check --source` no longer warns `no-real-material` when a real file's name merely contains `om-` (for example `materials/zoom-in.png`, `assets/bottom-bar.png`, `custom-chart.png`). The media filter is now anchored. Thanks @liuf8483-alt (#5).

## Update

`npm i -g huashu-motion@latest`, or `git pull --ff-only` in your clone.
```
</details>

---
### 📦 [wquguru/cicada](https://github.com/wquguru/cicada)
`⭐ Stars: 2,471` &nbsp;|&nbsp; `💻 语言: Swift` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.10.1](https://github.com/wquguru/cicada/releases/tag/v1.10.1) (2026-11-14)`

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
`⭐ Stars: 551` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.3.0-rc.10](https://github.com/SourceWeft/SourceWeft/releases/tag/v0.3.0-rc.10) (2026-11-19)`

> **简介**：ChatGPT 和 NotebookLM 的开源、自托管替代方案 — 一个 AI 工作站中的代理、技能、MCP 和引用知识。您的模型，您的基础设施。包括公共 MCP 服务器和代理技能目录。

**💡 核心亮点更新 (中文)**：
* feat(sso)：使用 OIDC 和 SAML 2.0 进行企业单点登录 (#534)，位于 https://github.com/SourceWeft/SourceWeft/pull/586
* feat(connectors)：每个连接器都有一个共享选择组件； Dropbox 在 https://github.com/SourceWeft/SourceWeft/pull/593 中运行（#25）
* 杂务（deps）：将 Next.js 升级到 16.4.5 以清除依赖审核（#601），通过 https://github.com/SourceWeft/SourceWeft/pull/603

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Self-hosting files for Web/Docker, macOS and Windows installers, and Linux x64 AppImage and .deb packages.

macOS installers are Developer ID signed and notarized. Windows installers have no publisher certificate; Windows may warn or block installation. Historical clients without an update key need one manual overwrite upgrade.
All application update packages have verified Tauri updater signatures. Local device execution runs in a signed sandbox runtime (sourceweft-sandbox-*.tar.gz, verified with the same updater key) that the app downloads and verifies on first use, on macOS (Apple silicon and Intel), Linux x86_64 and Windows (x64 and arm64).
See docker/README.md in the self-hosting archive for installation and upgrade instructions. Translations are provided in separate README files.


## What's Changed
* feat(sso): enterprise single sign-on with OIDC and SAML 2.0 (#534) by @QThans in https://github.com/SourceWeft/SourceWeft/pull/586
* feat(connectors): one shared selection component for every connector; Dropbox runs on it (#25) by @QThans in https://github.com/SourceWeft/SourceWeft/pull/593
* chore(deps): upgrade Next.js to 16.4.5 to clear the dependency audit (#601) by @QThans in https://github.com/SourceWeft/SourceWeft/pull/603
* feat(gmail): connect Gmail through Composio with live tools only by @QThans in https://github.com/SourceWeft/SourceWeft/pull/585
* chore(deps): ignore the unpatched picomatch advisory in the audit (#601) by @QThans in https://github.com/SourceWef
```
</details>

---
### 📦 [openai/codex](https://github.com/openai/codex)
`⭐ Stars: 136,189` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [rust-v0.171.0](https://github.com/openai/codex/releases/tag/rust-v0.171.0) (2026-11-20)`

> **简介**：在您的终端中运行的轻量级编码代理

**💡 核心亮点更新 (中文)**：
- 将 GPT-6.2 Sol 和 Astra 添加到模型目录中，并将 Sol 作为默认目录选择。 (#62106)
- 默认情况下启用 TUI 工作区，在主要对话旁边提供可搜索的文档预览、图像预览和子代理记录。 （#61352、#61888、#61889、#61919、#62157）
- 向非 Vim 提示编辑器添加了可配置的撤消和重做快捷方式，包括恢复附件和大型粘贴。 (#61954)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## New Features

- Added GPT-6.2 Sol and Astra to model catalogs, with Sol as the default catalog selection. (#62106)
- Enabled the TUI workspace by default, with searchable document previews, image previews, and subagent transcripts alongside the main conversation. (#61352, #61888, #61889, #61919, #62157)
- Added configurable undo and redo shortcuts to the non-Vim prompt composer, including restoration of attachments and large pastes. (#61954)
- Added `codex exec --remote <ADDR>` to start or resume noninteractive sessions on an existing app server. (#61707)
- Added `/rc` and `/remote` to manage local remote control and display device pairing codes from the TUI. (#62121)
- Added custom MCP status line selection and authoring through `/statusline` when `tui_extensions_statusline` is enabled. (#61979, #61988, #62037)

## Bug Fixes

- Preserved drafts, queued follow-ups, and interrupted input with their original threads when switching or resuming sessions. (#61216)
- Kept permission profiles intact when changing working directories. (#61195)
- Prevented late completion events from cancelling approvals for a newer turn. (#61801)
- Preserved earlier edits in aggregate diffs when steering an active turn. (#61820)
- Fixed scrolling that inserted stray characters, composer caret jumps, and redraws using stale terminal dimensions. (#62139, #62174, #62175)
- Fixed enterprise MCP sign-in for identity providers that issue ID tokens without refresh tokens. (#62129)

## Chores

- Updated s
```
</details>

---
### 📦 [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)
`⭐ Stars: 16,277` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.5.1](https://github.com/akitaonrails/ai-memory/releases/tag/v3.5.1) (2026-11-19)`

> **简介**：用于代理编码 CLI 的长期记忆解决方案，并促进不同代理供应商之间的切换

**💡 核心亮点更新 (中文)**：
校验和 (SHA256)
````
ai-内存-3.5.1-1.aarch64.rpm
a0d38a5f10fff973b74e2fc491d18253d6b7fc39f0edb42ca4b25a2a8beace31 ai-memory-3.5.1-1.x86_64.rpm
7d3328cd754cf78c6c08586027d405ce764b

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Checksums (SHA256)
```
07807c1779d1d8185916629d7b32667e6d6ba2f5249e9b90553526332a985886  ai-memory-3.5.1-1.aarch64.rpm
a0d38a5f10fff973b74e2fc491d18253d6b7fc39f0edb42ca4b25a2a8beace31  ai-memory-3.5.1-1.x86_64.rpm
7d3328cd754cf78c6c08586027d405ce764b19ad877eed41d150f3925792d4d1  ai-memory-claude-plugin.zip
bd90f5c3796a8272db5c8312290ab7156bad369e485768a8d69ca4bfaf799e10  ai-memory-hooks.tar.gz
5b8b9030c247b091ac2bacbf181f52f8fdba9d4ed47cdef23faab874d4c94d9f  ai-memory-install-hooks
120514a9279ee1d8036153da430feef25091477081030337c63bbee1c93be7eb  ai-memory-linux-aarch64.tar.gz
0e82461025db99cc8794b07708b43953ea111ffa7f26592ff896bbf64eb412bb  ai-memory-linux-x86_64.tar.gz
fda158379dc03331e5c71ab6b702a9335c7fc41e75dda4a2b1a7d1e8e98aaf04  ai-memory-macos-aarch64.tar.gz
49ff09af2eb904abf077a4a2a87660cad7800c6d6f4843abcab487f9315577c9  ai-memory-macos-x86_64.tar.gz
867da04c121910b019d4525c7afcdbd300eefebf310b3f5112bd19a043c211ef  ai-memory-windows-x86_64.zip
6a91c44ffa2e85d3b5a6ce26a4ccff0286b91d08d276d2bb4d47c346b036ee8b  ai-memory-wrapper.cmd
5e405aa237a2399f13084f71ae89545cbca77683c8251b4c4572cb51aedc8de4  ai-memory-wrapper.ps1
fca09943b10682903b0c4650b73f0b56c00624f3c5e1550c18bda6b801fdd660  ai-memory-wrapper
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
`⭐ Stars: 61,745` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.7.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.7.4) (2026-11-20)`

> **简介**：DeepTutor：终身个性化辅导。 https://deeptutor.info/。

**💡 核心亮点更新 (中文)**：
- **macOS：** 下载适用于您的 Mac（Apple Silicon 或 Intel）的 v1.7.4 DMG，退出 DeepTutor，并在应用程序中替换旧应用程序。如果 macOS 阻止旧应用程序启动，请直接安装替换应用程序。
- **Windows：** 退出 DeepTutor 并使用 v1.7.4 安装程序或便携式 ZIP。 Windows 安装程序和便携式应用程序使用相同的新运行时验证密钥。
- 安装桌面应用程序本身以接收新的公钥。早期的桌面版本仍然信任已停用的密钥。在升级之前，请避免将核心更新导入到这些版本中。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# DeepTutor v1.7.4 Release Notes

**Release Date:** 2026.11.20

This desktop security update replaces the runtime signing key used by the macOS and Windows apps. On November 20, desktop release credentials were exposed in GitHub Actions artifacts. Those artifacts have been removed.

## What's New

The desktop app verifies runtime updates with a new public key. When it finds a saved runtime signed with the retired key, it installs the verified runtime bundled with the new app and backs up the existing workspace before starting it. Tagged desktop builds now require maintainer approval to access release credentials.

## Upgrade Notes

- **macOS:** Download the v1.7.4 DMG for your Mac (Apple Silicon or Intel), quit DeepTutor, and replace the old app in Applications. If macOS blocks the old app from launching, install the replacement directly.
- **Windows:** Quit DeepTutor and use the v1.7.4 installer or portable ZIP. The Windows installer and portable app use the same new runtime verification key.
- Install the desktop app itself to receive the new public key. Earlier desktop versions still trust the retired key. Until you upgrade, avoid importing core updates into those versions.

**Full Changelog**: https://github.com/HKUDS/DeepTutor/compare/v1.7.3...v1.7.4
```
</details>

---
### 📦 [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)
`⭐ Stars: 114,099` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.6.1](https://github.com/Panniantong/Agent-Reach/releases/tag/v1.6.1) (2026-11-01)`

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
`⭐ Stars: 34` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.3.16](https://github.com/Hsiung-Shao/exile-appraiser/releases/tag/v0.3.16) (2026-11-20)`

> **简介**：ExileAppraiser / 流亡鑑價:Path of Exile 1/2 查價器,支援國際服與台服(繁中/英文客戶端)

**💡 核心亮点更新 (中文)**：
修正

・**PoE1 新通貨無法查價**：Originator's Exalted Orb、Primordial Exalted Orb 可以解析並查價了。（繁中客戶端目前顯示英文名）
・**PoE1 遊戲還沒翻譯的物品無法解析**：繁中客戶端顯示英文名的物品，改用英文名比對。
・**PoE1 勾選三條輔助寶石詞綴後查價失敗**：不再出現「Query is too complex」。
・**PoE1 部分詞綴勾選後查到 0 筆**：補上交易站實際使用的 18 個 id。（例：擊中稀有或傳奇敵人

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 修正

・**PoE1 新通貨無法查價**：Originator's Exalted Orb、Primordial Exalted Orb 可以解析並查價了。（繁中客戶端目前顯示英文名）
・**PoE1 遊戲還沒翻譯的物品無法解析**：繁中客戶端顯示英文名的物品，改用英文名比對。
・**PoE1 勾選三條輔助寶石詞綴後查價失敗**：不再出現「Query is too complex」。
・**PoE1 部分詞綴勾選後查到 0 筆**：補上交易站實際使用的 18 個 id。（例：擊中稀有或傳奇敵人時觸發盜獵者印記）
・**PoE1 巫會之后冠的詞綴顯示為未解析**：「對魔力回復率的增減同時會以 12% 的數值套用至能量護盾充能率」可以解析並帶數值查價。
・**PoE1 帶數值的詞綴顯示為未解析**：補上繁中 59 條、英文 60 條寫法。（例：區域含有 3 個保險箱）
・**PoE1 詞綴名稱後帶「(...)」時顯示為未解析**：進階複製的這個標記出現在任何詞綴上都能解析。

## 調整

・**PoE1 資料更新到 3.30.0d**：補上交易站新列出的詞綴。

說明：這一版的英文客戶端修正是依遊戲資料檔的英文句子驗證的，沒有英文實機樣本；英文客戶端遇到未解析的詞綴請用面板上的回報按鈕。
```
</details>

---
### 📦 [microsoft/skill-recorder](https://github.com/microsoft/skill-recorder)
`⭐ Stars: 5,899` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.9.4](https://github.com/microsoft/skill-recorder/releases/tag/v0.9.4) (2026-11-23)`

> **简介**：桌面应用程序，记录您的屏幕上工作会话，并使用 GitHub Copilot SDK 将其重建为意图 + 有序步骤，然后为 Microsoft Autopilot（例如 Scout、Microsoft Copilot Cowork 或 Copilot Studio）构建可重用的技能或自动化。

**💡 核心亮点更新 (中文)**：
- 即使终端块、分页、时间窗口或摘录边界分割其值，也可以屏蔽检测到的秘密。
- 使用有界、重叠的扫描窗口检测打印的多行私钥。
- 跨终端块保留 ANSI 控制序列状态，因此分割颜色序列不会隐藏标记以防止检测。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# Skill Recorder v0.9.4

This is a **source-only release**. No application installers or portable binaries are attached. GitHub's source archives contain the tagged repository source; the commands below build the application locally.

**Release commit:** `f4f9e2b6ac58f71da8e2bbd9fde34e65390a7ae8`

## Security and compatibility

- Mask detected secrets even when terminal chunks, pagination, time windows, or excerpt boundaries split their values.
- Detect printed multiline private keys using bounded, overlapping scan windows.
- Preserve ANSI control-sequence state across terminal chunks so split color sequences do not hide tokens from detection.
- Mask raw text before JSON escaping and truncation in analysis tools.
- Preserve existing UI/UX flows, tool result formats, saved recordings, pagination, and protection-off behavior. No dependencies or recording formats changed.

These fixes address four independently reproduced redaction gaps in v0.9.3. Protection remains a best-effort safety net: avoid recording real credentials. Upgrading does not remove data previously sent to an AI provider or alter existing local recordings. If real credentials were captured and analyzed, consider them potentially exposed and rotate them according to your organization's security procedures.

## Commit-pinned installation

To upgrade, use the appropriate command below. Finish any active recording and quit running copies before launching the new version. Windows installation does
```
</details>

---
### 📦 [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model)
`⭐ Stars: 84,450` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.9.0](https://github.com/Ebony-Vinyl/dsh-our-free-model/releases/tag/v2.9.0) (2026-11-22)`

> **简介**：在 dsh 里装上这个插件即可，无需登录、注册或填 API Key，就能使用包括 DeepSeek V4.1 Flash、Kimi K3 在内的前沿模型——完全免费，不限量。 All you do is install this plugin in dsh: no login, no sign-up, no API key — the frontier models are just there, DeepSeek V4.1 Flash and Kimi K3 among them. Completely free, with no usage cap.

**💡 核心亮点更新 (中文)**：
- **出口池**：额度按出口 IP 计数，所以一个出口被限流时，车道现在会在**同一回合内**换下一个。出口在设置页按行填写，地址后加 `#pool`（或前缀 `pool+`）表示轮换池端点——每次连接换 IP，因此从不冷却。每回合最多换几个出口可调（1–8）。
- **限流窗口封顶 30 分钟**：上游（或它前面的 CDN/WAF）曾下发 `Retry-After: 70411`，把出口锁近 20 小时，而它 17 分钟后已恢复 200。现在单次 429 最多锁 30 分钟；磁盘上遗留的超长窗口在读取时同样截断。
- **修复回归：请求不可取消**。换出口重构时把调用方的 `AbortSignal` 覆盖成了 `undefined`，导致所有经出口的请求（含 Bun 子进程）无法中止。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## v2.9.0

### 免费车道

- **出口池**：额度按出口 IP 计数，所以一个出口被限流时，车道现在会在**同一回合内**换下一个。出口在设置页按行填写，地址后加 `#pool`（或前缀 `pool+`）表示轮换池端点——每次连接换 IP，因此从不冷却。每回合最多换几个出口可调（1–8）。
- **限流窗口封顶 30 分钟**：上游（或它前面的 CDN/WAF）曾下发 `Retry-After: 70411`，把出口锁近 20 小时，而它 17 分钟后已恢复 200。现在单次 429 最多锁 30 分钟；磁盘上遗留的超长窗口在读取时同样截断。
- **修复回归：请求不可取消**。换出口重构时把调用方的 `AbortSignal` 覆盖成了 `undefined`，导致所有经出口的请求（含 Bun 子进程）无法中止。
- **本地锁有出口了**：车道被本地拒绝时，设置页顶部出现横幅，说明这是插件自己的保护、何时解除，并给出「解除车道锁定」按钮。此前该按钮在未配置出口时是灰的——而那正是最需要它的时候。
- 出口地址填错现在返回 **400** 而不是 500。

### 官方工具面

- **官方名只承载官方定义**：实测调用方工具撞上官方名（`bash` → `shell`）会被上游判成 429。现在只有声明与官方定义逐字一致时才占用官方名，其余一律走 `mcp_<hash>`，官方 13 工具照常逐字注入；重复声明按 wire name 去重。
- **修复回归：真实 MCP 工具名被截断**。`mcp__github__search` 曾被截成 `_github__search`——一个调用方从未声明的工具。句柄改为按完整形状识别，非句柄名原样透传。

### EAC 名册

- 修复整份封印名册被压成单张 `[object Object]` 卡片的缺陷：`parseListing` 现在返回整行供 `buildCatalog` 读取容量，而 `buildEacCatalog` 需要裸 id。两侧都修正，并过滤旧版写入的无效 `sealIds`。

### 公告

- 撤下的紧急公告不再对**已缓存它**的老安装反复弹全屏：缓存超过 2 小时即失去打断权，条目仍留在列表里。

### 来源与许可

- `src/token-saver/rtk` → `compact` 重命名；o2a 身份与工具名模块重写（8 个同名函数全部改名，旧名零残留）。
- `LICENSE` 补第三方许可附录：opencode（MIT）、RTK（Apache-2.0）、9router（MIT）全文与使用说明。附录内联在 `LICENSE` 里而非独立文件，因为旧升级器对发行集有 80 文件硬上限，而发行集正好 80。
- `scripts/probes/` 下 8 个探针脚本标注 9router 来源（MIT 文件头）；它们不进发行集。

### 升级说明

升级不修改现有账号、配置与归档。清单与 `catalog/integrity.json` 已重签（80 文件 / 33947585 字节）。

**验证**：全套测试 124/124；从真实 npm tarball 加载实机 14/14；独立端实机 21/21；宿主挂载实机 14/14；清单按「已安装用户」视角校验 17/17（含签名）。
```
</details>

---
### 📦 [hypit-ai/hypit](https://github.com/hypit-ai/hypit)
`⭐ Stars: 31,163` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.3.3](https://github.com/hypit-ai/hypit/releases/tag/v0.3.3) (2026-11-16)`

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
`⭐ Stars: 22,582` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.0.11](https://github.com/HBAI-Ltd/Toonflow-app/releases/tag/v2.0.11) (2026-11-18)`

> **简介**：短剧、漫剧制作工具 Toonflow：开源 AI 视频创作平台，集成剧本创作、智能分镜、角色与场景资产管理、图像生成和视频生成。融合无限画布、AI Agent 与可视化工作流，支持本地部署、自选模型、跨平台客户端、MCP 与插件扩展。Open-source AI short drama and motion comic creation tool with an infinite canvas, AI agents, storyboarding, image and video generation. Self-hosted and extensible, with a canvas-based approach similar to LibTV and TapNow.

**💡 核心亮点更新 (中文)**：
- 💻 **Windows**：双击下载的安装包，按提示完成安装。ARM64 需要 .NET Framework 4.8.1，较新的 Windows 11 已内置。
- 🍎 **Mac（macOS 14 及以上）**：双击下载的 `.pkg`，按提示继续安装；安装期间会自动下载并准备必要运行时，完成后从“应用程序”打开 Toonflow。
- 🐧 **Linux（Debian / Ubuntu）**：选择对应架构的 DEB，在下载目录执行 `sudo apt install ./toonflow-版本号-linux-架构.deb`。安装后可在「设置 → 关于」更新；使用 2.0.10 的用户需先手动覆盖安装一次。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 📦 下载指南

选择你的设备对应的安装包，点击即可下载：

| 你的设备 | 下载 |
| --- | --- |
| 💻 Windows（Intel / AMD，x64） | [⬇️ 下载 Windows x64 安装包](https://github.com/HBAI-Ltd/Toonflow-app/releases/download/v2.0.11/toonflow-2.0.11-Setup.exe) |
| 💻 Windows（ARM64） | [⬇️ 下载 Windows ARM64 安装包](https://github.com/HBAI-Ltd/Toonflow-app/releases/download/v2.0.11/toonflow-2.0.11-win-arm64-Setup.exe) |
| 🍎 Mac（M 系列芯片） | [⬇️ 下载 M 系列 Mac 安装包](https://github.com/HBAI-Ltd/Toonflow-app/releases/download/v2.0.11/toonflow-2.0.11-macos-arm64.pkg) |
| 🍎 Mac（Intel 芯片） | [⬇️ 下载 Intel Mac 安装包](https://github.com/HBAI-Ltd/Toonflow-app/releases/download/v2.0.11/toonflow-2.0.11-macos-x64.pkg) |
| 🐧 Linux（Intel / AMD，x64） | [⬇️ 下载 Linux x64 DEB](https://github.com/HBAI-Ltd/Toonflow-app/releases/download/v2.0.11/toonflow-2.0.11-linux-x64.deb) |
| 🐧 Linux（ARM64） | [⬇️ 下载 Linux ARM64 DEB](https://github.com/HBAI-Ltd/Toonflow-app/releases/download/v2.0.11/toonflow-2.0.11-linux-arm64.deb) |
| 📱 Android（ARM64，Android 8 及以上） | [⬇️ 下载 Android APK](https://github.com/HBAI-Ltd/Toonflow-app/releases/download/v2.0.11/toonflow-2.0.11-android-arm64.apk) |

> 💡 手动安装请选择上表中的链接。下方其他文件供软件自动更新使用。

## 🚀 安装说明

- 💻 **Windows**：双击下载的安装包，按提示完成安装。ARM64 需要 .NET Framework 4.8.1，较新的 Windows 11 已内置。
- 🍎 **Mac（macOS 14 及以上）**：双击下载的 `.pkg`，按提示继续安装；安装期间会自动下载并准备必要运行时，完成后从“应用程序”打开 Toonflow。
- 🐧 **Linux（Debian / Ubuntu）**：选择对应架构的 DEB，在下载目录执行 `sudo apt install ./toonflow-版本号-linux-架构.deb`。安装后可在「设置 → 关于」更新；使用 2.0.10 的用户需先手动覆盖安装一次。
- 📱 **Android**：在手机上打开 APK，按系统提示允许此来源安
```
</details>

---
### 📦 [morluto/rea](https://github.com/morluto/rea)
`⭐ Stars: 474,663` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [rea-agents-6.10.1](https://github.com/morluto/rea/releases/tag/rea-agents-6.10.1) (2026-11-20)`

> **简介**：使用代理对任何内容进行逆向工程，从应用程序行为到本机二进制文件。

**💡 核心亮点更新 (中文)**：
- 使用三个离线 CLI 和 MCP 工具检查并提取 UEFI 固件卷、文件和 AMI NVRAM。 [#12342](https://github.com/morluto/rea/pull/12342)。谢谢 。
- 检查 Android 启动映像和 OTA 有效负载、NES 2.0 容器以及 Maven、Gradle 和 NuGet 包元数据。 [a88c0a5](https://github.com/morluto/rea/commit/a88c0a55544e16a710ddaad2feb5a2c6e7011f4e)[#9487](https://github.com/morluto/rea/pull/9487) [#11378](https://github.com/morluto/rea/pull/11378) [#10674](https://github.com/morluto/rea/pull/10674) [05be423](https://github.com/morluto/rea/commit/05be423acbdf3a56673bdbd3004e4b500c0f5217)[#10353](https://github.com/morluto/rea/pull/10353) [43b9fa8](https://github.com/morluto/rea/commit/43b9fa87fbbaa74224731a1fe3a8e67a2d336ae3)[#10351](https://github.com/morluto/rea/pull/10351) [#8144](https://github.com/morluto/rea/issues/8144)。谢谢 ， ， ， 。
- 证据修订版 2 给出了文件、进程、调试器和浏览器观察的明确主题身份。请参阅下面的迁移详细信息。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## [6.10.1](https://github.com/morluto/rea/compare/rea-agents-6.10.0...rea-agents-6.10.1) (2026-11-20)

This is the first 6.10 release published to npm. It includes the changes, migration notes, and contributor credits from 6.10.0 below, plus the patch fix.

### Bug Fixes

* **kuna:** use one constant for the serial job count ([#12735](https://github.com/morluto/rea/issues/12735)) ([3e3faf2](https://github.com/morluto/rea/commit/3e3faf2fc32dbadc96a45f51f4361eb64ce6ed32))

---

## [6.10.0](https://github.com/morluto/rea/compare/rea-agents-6.9.0...rea-agents-6.10.0) (2026-11-20)

### Highlights

- Inspect and extract UEFI firmware volumes, files, and AMI NVRAM with three offline CLI and MCP tools. [#12342](https://github.com/morluto/rea/pull/12342). Thanks @bartman081523.
- Inspect Android boot images and OTA payloads, NES 2.0 containers, and Maven, Gradle, and NuGet package metadata. [a88c0a5](https://github.com/morluto/rea/commit/a88c0a55544e16a710ddaad2feb5a2c6e7011f4e) [#9487](https://github.com/morluto/rea/pull/9487) [#11378](https://github.com/morluto/rea/pull/11378) [#10674](https://github.com/morluto/rea/pull/10674) [05be423](https://github.com/morluto/rea/commit/05be423acbdf3a56673bdbd3004e4b500c0f5217) [#10353](https://github.com/morluto/rea/pull/10353) [43b9fa8](https://github.com/morluto/rea/commit/43b9fa87fbbaa74224731a1fe3a8e67a2d336ae3) [#10351](https://github.com/morluto/rea/pull/10351) [#8144](https://github.com/morluto/rea/issues/8144). Thanks @Davmunrey, @gen
```
</details>

---
### 📦 [chatfire-AI/huobao-drama](https://github.com/chatfire-AI/huobao-drama)
`⭐ Stars: 17,859` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v4.0.11](https://github.com/chatfire-AI/huobao-drama/releases/tag/v4.0.11) (2026-11-05)`

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
`⭐ Stars: 40,251` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.1.4708](https://github.com/yetone/magpie/releases/tag/v0.1.4708) (2026-11-23)`

> **简介**：每个代理的模型。一处。来自菜单栏的 DeepSeek 上的 Codex、Kimi 上的 Claude Code。

**💡 核心亮点更新 (中文)**：
- 改进了网关处理组成员错误的方式，以防止错误地传递错误。
- 阐明了如何从另一台计算机访问图书馆 MCP 服务器以及如何检索所有服务器。
- **macOS（Apple Silicon）：** `magpie-darwin-arm64.dmg`

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Bug Fixes
- Improved how the gateway handles errors from group members to prevent them from being passed along incorrectly.

## Documentation
- Clarified how Library MCP servers are accessed from another computer and how to retrieve all of them.

### Install

Download from [usemagpie.ai](https://usemagpie.ai), or `curl -fsSL https://usemagpie.ai/install.sh | sh`. An installed magpie updates itself.

- **macOS (Apple Silicon):** `magpie-darwin-arm64.dmg`
- **macOS (Intel):** `magpie-darwin-amd64.dmg`
- **Windows:** `magpie-windows-amd64.exe` (ARM: `magpie-windows-arm64.exe`)
- **Linux:** `magpie-linux-amd64` / `magpie-linux-arm64` (needs GTK 3 and WebKitGTK 4.1)
- **Terminal only:** `magpie-cli-<os>-<arch>`

<!-- lang:zh -->

## 错误修复
- 改进了网关处理群组成员错误的方式，以防止这些错误被错误地传递。

## 文档
- 澄清了如何从另一台计算机访问 Library MCP 服务器，以及如何检索所有服务器。

### 安装

从 [usemagpie.ai](https://usemagpie.ai) 下载，或运行 `curl -fsSL https://usemagpie.ai/install.sh | sh`。已安装的 magpie 会自动更新。



---
The same release, and the feed magpie updates from: https://github.com/yetone/magpie-releases/releases/tag/v0.1.4708
```
</details>

---
### 📦 [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
`⭐ Stars: 265,527` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.23.3](https://github.com/NousResearch/hermes-agent/releases/tag/v0.23.3) (2026-11-20)`

> **简介**：与您共同成长的代理商

**💡 核心亮点更新 (中文)**：
- Microsoft Store 应用程序：通过商店更新。
- 从安装程序安装的桌面应用程序（.exe / .dmg）：此版本中没有变化；它会随着下一个捆绑版本的更新而更新。
- CLI：`hermes update`，或重新运行安装程序一行。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# Hermes Agent v0.23.3

**Release Date:** November 19, 2026

> Patch release. This tag rolls up the ~370 PRs merged since v0.23.2 into a stable release for the GitHub release (CLI and installers), the Microsoft Store app, Docker and Hermes Cloud. Full curated notes for this window ship with v0.24.0.

<!-- HERMES_BUILDS_TABLE -->

## About this release

Measured at commit `caafe5389ae`, the window since v0.23.2 contains **1,657 non-merge commits** across **3,948 changed files** (+222,379 / −96,154), **370 merged PRs** and **60 closed issues**.

Also in the window, undocumented here on purpose: one prompt-cache lifecycle controller (warming through long tool runs, compaction of idle chats before the 1h cache expires, Nous Portal on the full 1h lifecycle, `prompt_caching.cache_ttl` defaulting to `auto`), compaction that archives the tool results it drops, the proactive tool-result prune on by default, a one-question first-run CLI setup with the free tier included, GPT-6.2 Astra and Sol (+ Pro) on OpenRouter and Nous Portal, a "Waiting on teammates" strip above Bot Chat composers, the Linux AppImage agent payload run from a stable per-build copy, the storage layer split behind a persistence interface with its SQLite backend, dependency security bumps (oauthlib, opentelemetry, tornado), and a large batch of new plugin-catalog entries.

**Full curated release notes for this window ship with v0.24.0**, which will document everything from v0.23.0 onward — highlights, feature areas, a
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
`⭐ Stars: 12,796` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.13.615](https://github.com/genspark-ai/genoffice/releases/tag/v0.13.615) (2026-11-19)`

> **简介**：免费的开源 AI Office 套件：带有内置 AI 代理的文档、表格、幻灯片、PDF、Markdown 和 HTML 编辑器，以及“genoffice”CLI 和代理技能，以便 Claude Code、Codex 和 Cursor 可以在本地创建和编辑真正的 .docx/.xlsx/.pptx 文件。带上你自己的钥匙。 macOS、Windows 和 Linux。

**💡 核心亮点更新 (中文)**：
- **文档：**菜单和功能区选项卡的布局与 Word for Mac 中一样，后面带有 Word 对话框（文档、段落、字体、边框和底纹、项目符号和编号、脚注和尾注、索引和表格等）；比较和合并文档；模板，插入 > 文件并插入 > 图标；分组和对齐浮动对象；佐特罗引文；嵌套表格像Word一样跨页面；更快地输入长文档。
- **工作表：** Excel 的正则表达式函数和 PERCENTOF ；复制的范围也会作为图片出现在 Windows 剪贴板上；旧版“.xls”文件保留其真实颜色；丝带适合较窄的窗户；当网格滚动时，单元格编辑器停留在其单元格上。
- **幻灯片：** 旧版“.ppt”文本解码和大纲修复；新元素获得正确的段落间距。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
GenOffice v0.13.615 stable desktop installers. The headline of this release is Docs: the menu bar, ribbon and right-click menu now follow Word for Mac, with most of Word's dialogs behind them.

## What's New

- **Docs:** menus and ribbon tabs are laid out as in Word for Mac, with Word's dialogs behind them (Document, Paragraph, Font, Borders and Shading, Bullets and Numbering, Footnote and Endnote, Index and Tables and more); Compare and Combine Documents; templates, Insert > File and Insert > Icons; grouping and aligning floating objects; Zotero citations (@pemdesign); nested tables break across pages like Word (@mubaroqadb); faster typing in long documents (@tokg-venv).
- **Sheets:** Excel's regex functions and PERCENTOF (@vinirib); a copied range also lands on the Windows clipboard as a picture (@tokg-venv); legacy `.xls` files keep their real colors; the ribbon fits narrower windows (@mubaroqadb); the cell editor stays on its cell while the grid scrolls (@Xtzdd).
- **Slides:** legacy `.ppt` text decoding and outline fixes (@aniruddhaadak80); new elements get the right paragraph spacing (@widechaos).
- **PDF:** edit the recognized-text layer in place, with a Recognize Text command (@tokg-venv); right-to-left inserts and line-end hyphens (@aniruddhaadak80); smoother upscaled page images (@krakotay); steadier page deletion and text insertion (@widechaos).
- **OpenDocument:** `.odt` tables, lists, spacing, backgrounds and repeated header rows convert more faithfully (@Zhangs-
```
</details>

---
### 📦 [guohuiyuan/go-music-dl](https://github.com/guohuiyuan/go-music-dl)
`⭐ Stars: 6,701` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.1.7](https://github.com/guohuiyuan/go-music-dl/releases/tag/v1.1.7) (2026-11-16)`

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
### 📦 [pascalorg/editor](https://github.com/pascalorg/editor)
`⭐ Stars: 25,686` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [@pascal-app/cli@1.1.6](https://github.com/pascalorg/editor/releases/tag/%40pascal-app/cli%401.1.6) (2026-11-17)`

> **简介**：适用于 AECO、扫描到 BIM 的开源 3D 建筑软件。代理友好、浏览器优先、MCP、CLI。

**💡 核心亮点更新 (中文)**：
`@pascal-app/cli@1.1.6` 的 Pascal Web 编辑器运行时。当命令第一次启动编辑器时，CLI 会下载“pascal-web-runtime-1.1.6.tar.gz”，并根据 npm 包内发布的摘要进行验证。离线安装可以通过t

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
The Pascal web editor runtime for `@pascal-app/cli@1.1.6`. The CLI downloads `pascal-web-runtime-1.1.6.tar.gz` the first time a command starts the editor and verifies it against the digest published inside the npm package. Offline installs can pass the archive directly: `pascal editor --runtime pascal-web-runtime-1.1.6.tar.gz`.
```
</details>

---
### 📦 [linshenkx/prompt-optimizer](https://github.com/linshenkx/prompt-optimizer)
`⭐ Stars: 42,263` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.16.1](https://github.com/linshenkx/prompt-optimizer/releases/tag/v2.16.1) (2026-11-23)`

> **简介**：人工智能提示优化器，用于编写更好的提示并获得更好的人工智能结果。

**💡 核心亮点更新 (中文)**：
- 刷新页面或重新打开桌面应用程序后，从上次停下的地方继续。
- 在恢复的文本测试结果和竞技场中查看报告的令牌使用情况。
- 使用“在桌面大小的工作区上全部运行”旁边的星号来保存多个结果。使用相同提示运行的测试可以共享收藏夹，并且保存对话框组结果使用不同的提示运行。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## English

### Summary

Workspace drafts are saved as you edit and restored after a reload. Test results retain token usage when the provider reports it, and multiple test columns can now be saved to favorites together.

### Highlights

- Pick up where you left off after refreshing the page or reopening the desktop app.
- Review reported token usage on restored text test results and in Arena.
- Use the star next to Run all on desktop-sized workspaces to save multiple results. Tests run with the same prompt can share a favorite, and the save dialog groups results run with different prompts.

### Product Updates

#### Desktop

- The desktop app saves open workspace drafts before closing or restarting for an update.

#### Web

- Save a column's result using the prompt and inputs recorded for that test. Results can still be saved after you edit the workspace.
- Choose which results to keep when saving tests that used different prompts. Each prompt group becomes its own favorite after confirmation. [#381](https://github.com/linshenkx/prompt-optimizer/pull/381)

#### Extension

- Restore workspace drafts and reported text-test token usage across reloads in the extension.

#### Core/Infra

- Expose reported token usage from supported text providers, including non-streaming responses. [#379](https://github.com/linshenkx/prompt-optimizer/pull/379)
- Add Claude model presets and recognize adaptive thinking on more compatible model IDs. [#380](https://github.com/linshenkx/prompt-optimi
```
</details>

---
### 📦 [RSSNext/Folo](https://github.com/RSSNext/Folo)
`⭐ Stars: 39,338` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [desktop/v1.18.0](https://github.com/RSSNext/Folo/releases/tag/desktop/v1.18.0) (2026-11-15)`

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
`⭐ Stars: 51,702` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [0.32.0](https://github.com/roboflow/supervision/releases/tag/0.32.0) (2026-11-18)`

> **简介**：我们为您编写可重复使用的计算机视觉工具。 💜

**💡 核心亮点更新 (中文)**：
- **`PolygonZone`** 计算每个类的进入和退出数量，并报告每个跟踪对象的停留时间。
- **`Detections.from_semantic_segmentation`** 将类映射转换为每个类的一个屏蔽检测； Ultralytics 和 Inference 结果也会加载。
- **`KeyPointsDataset`** 读取和写入 YOLO 姿势数据集。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# v0.32.0: Zone counting, dwell time and semantic segmentation

## 📋 Summary

supervision now counts objects entering and leaving a zone, times how long each one stays, and loads semantic segmentation results.

- **`PolygonZone`** counts entries and exits per class and reports dwell time for every tracked object.
- **`Detections.from_semantic_segmentation`** turns a class map into one masked detection per class; Ultralytics and Inference results load too.
- **`KeyPointsDataset`** reads and writes YOLO pose datasets.
- **`box_weighted_box_fusion`** merges overlapping boxes from several models instead of throwing most of them away.
- **`VertexAnnotator`** and its siblings take a color palette and can color each joint by its index.

Most projects can upgrade as is, but the public `validate_*` helpers, `merge_inner_*` and `KeyPoints.confidence` are gone and a few edge cases changed, so check the Migration guide.

## ✨ Spotlights / highlights

### Zones that count entries, exits and dwell time

`sv.PolygonZone` now follows each `tracker_id` across frames. It counts objects entering and leaving (`in_count`, `out_count` and the per-class versions are named the same as on `sv.LineZone`), reports the current count per class, and measures how long each tracked object has been inside with `time_in_zone`. Pass a `timestamp` to `trigger` for seconds, or leave it out for frames. `occupancy_ratio` reports how much of the zone the detections cover, and `sv.PolygonZoneAnnota
```
</details>

---
### 📦 [MetaCubeX/mihomo](https://github.com/MetaCubeX/mihomo)
`⭐ Stars: 36,012` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.19.34](https://github.com/MetaCubeX/mihomo/releases/tag/v1.19.34) (2026-11-11)`

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
`⭐ Stars: 160,064` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.5.10](https://github.com/clash-verge-rev/clash-verge-rev/releases/tag/v2.5.10) (2026-11-03)`

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
`⭐ Stars: 80,015` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.1.922-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.922-beta) (2026-11-20)`

> **简介**：用于运行和训练法学硕士和扩散模型的本地 UI。支持 GGUF、MLX、Qwen3.8、DeepSeek-V4.1、MiniMax-H3、Gemma 4、FLUX 等。

**💡 核心亮点更新 (中文)**：
- **Inkling 2 Mini** - 内存使用量更少，速度更快。新 26B（5.4 活动）1M 上下文 - [指南](https://unsloth.ai/docs/models/inkling-2-mini)
- **8GB GPU 上的 MiniMax-H3-Image** 在 36.7 秒内呈现新提示（之前为 82.7 秒）
- **在 Linux 和 macOS 上加载 GGUF 图像模型时 RAM 减少 52-66%**

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Run the new Inkling 2 Mini model, the strongest 26.4B model that runs on 16GB RAM.
This release makes image generation faster and lighter on small GPUs. Macs with Apple Silicon can now restyle videos, and chats that use MCP tools no longer reprocess the whole conversation on every message.

## Highlights

- **Inkling 2 Mini** - less memory usage and faster. New 26B (5.4 active) 1M context - [Guide](https://unsloth.ai/docs/models/inkling-2-mini)
- **MiniMax-H3-Image on 8GB GPUs** renders a new prompt in 36.7 s (prev 82.7 s)
- **GGUF image models load with 52-66% less RAM** on Linux and macOS
- **Video Restyle on Mac** re-renders a whole clip in a new style on Apple
- **MCP chats process 83 to 87% fewer prompt tokens** in our tool tests
- **Scanned PDFs in chat** are now read with OCR
- **Theme files** let you share your Appearance settings

## Images

- FLUX.1 takes 16 to 28% less time per step when its weights stream from system RAM.
- FLUX.3 klein INT8 takes 13% less time per step on T4 GPUs.
- GTX 16xx cards no longer fail image renders with a NaN error.
- Picking a new LoRA on an INT8 or FP8 model offers **Reload and generate** instead of an error.

## Video

- Cosmos3-Edge-FP8 runs about 1.45x faster on L4 GPUs.
- Restyle on Mac needs about 42 GiB of GPU memory for bf16, or 31 GiB for q8_0.

## Diffusion LoRA training

- SDXL LoRA training takes 28 to 31% less time per step on T4 and L4.
- **Auto** precision trains FLUX.2-klein 9B in about 30%
```
</details>

---
### 📦 [arc53/DocsGPT](https://github.com/arc53/DocsGPT)
`⭐ Stars: 18,376` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [1.1.0](https://github.com/arc53/DocsGPT/releases/tag/1.1.0) (2026-10-25)`

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
`⭐ Stars: 86,022` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.3.5](https://github.com/lobehub/lobehub/releases/tag/v2.3.5) (2026-11-22)`

> **简介**：🤯 LobeHub - 您团队中的超级代理。将超级代理添加到您的团队已使用的聊天中。他们自己承担工作，并且每周都会变得更好。

**💡 核心亮点更新 (中文)**：
- [x] 添加了使用 UI 库的实际头像生成器的回归测试。在最初的版本中，绿色头像收到“未定义”，其中主题指定“var(--lobe-green)”。
- [x] Ran lint 和 10 个相关的封面颜色测试。
- [x] 针对原始版本和 UI 6.19.0 的此提交进行了相同的独立工作区兼容性检查。原始版本未通过“TS2739”类型检查；该修复通过了类型检查和所有 505 个工作区测试。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Release v2.3.5

From PR #23632: https://github.com/lobehub/lobehub/pull/23632

### Summary

Contribution source: AI-assisted

Backport the cyan, green and red agent cover colors from [#23624](https://github.com/lobehub/lobehub/pull/23624) to the community release branch. A fresh install of `main` can resolve `@lobehub/ui@6.19.0` within the declared dependency range. The old seven-entry palette fails type-checking on that version and returns an undefined cover color for some generated avatars.

The cover uses the corresponding theme token for each new color. Inferring the lookup's keys also supports older UI versions in the release's existing dependency range.

Also backports the canary test for the transaction-scoped share upload lock. Its query now counts the advisory lock for the share under test, allowing unrelated sessions to hold their own locks concurrently.

### Tests

- [x] Added a regression test using the UI library's actual avatar generator. On the original release, a green avatar received `undefined` where the theme specifies `var(--lobe-green)`.
- [x] Ran lint and the 10 related cover-color tests.
- [x] Ran the same standalone workspace compatibility check against the original release and this commit with UI 6.19.0. The original failed type-checking with `TS2739`; the fix passed type-checking and all 505 workspace tests.
- [x] Ran the repository type-check.
- [x] Held two unrelated advisory locks on a separate connection in a dedicated PostgreSQL instance. The
```
</details>

---
### 📦 [hiddify/hiddify-app](https://github.com/hiddify/hiddify-app)
`⭐ Stars: 34,359` &nbsp;|&nbsp; `💻 语言: Dart` &nbsp;|&nbsp; `🏷️ 最新版本: [v5.9.15](https://github.com/hiddify/hiddify-app/releases/tag/v5.9.15) (2026-11-19)`

> **简介**：多平台自动代理客户端，支持Sing-box、X-ray、TUIC、Hysteria、Reality、Trojan、SSH等。开源、安全、无广告。

**💡 核心亮点更新 (中文)**：
- **更智能的保持顶部。** 只有最快的代理运行，其他代理则停止运行。保留的代理
- **21 种新语言。** 现已完成九种翻译。
- **CPU 和电池消耗更轻。** 当没有人看到动画时，动画就会停止。连接按钮的

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# Highlights
- **A smarter Keep top.** Only the fastest proxies run and the others are parked. A kept proxy
  that stops answering is replaced, and the parked ones are checked again every hour. Client
  endpoints, WARP included, take part too.
- **21 new languages.** Nine more translations are now complete.
- **Lighter on CPU and battery.** Animations stop when nobody can see them. The connect button's
  light costs much less to draw. The core uses only as many processors as its load needs and
  paces the reads of busy connections.
- **OpenVPN profiles.** The app reads `.ovpn` files and `ovpn://` links.
- **Psiphon gets through more often.** As the first hop, Psiphon scans CDN edges with Chrome's
  TLS handshake and connects through the ones that answer. You can change its country from the
  home page.
- **WARP keeps searching, and can search deeper.** WARP searches for up to 3 minutes and learns
  which noise and tunnel work on each network. When a WARP or Psiphon search finds nothing, the
  app offers a deep search.
- **Proxies that are not secure are marked.** A proxy that anyone on the way can read gets a red
  *Not secure* mark that explains why. The list shows each proxy's transport and security, such
  as `VLESS · XHTTP · REALITY`.
- **Subscriptions download on hard networks.** The core downloads them with Chrome's TLS
  handshake. When a download fails, the app says why and what to try.
- **The desktop core runs in a process of its own.** The app's
```
</details>

---
### 📦 [Dooy/chatgpt-web-midjourney-proxy](https://github.com/Dooy/chatgpt-web-midjourney-proxy)
`⭐ Stars: 6,801` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.26.9](https://github.com/Dooy/chatgpt-web-midjourney-proxy/releases/tag/v2.26.9) (2026-11-22)`

> **简介**：一个UI全部由chatgpt web、midjourney、gpts、suno、luma、runway、viggle、flux、ideogram、realtime、pika、udio完成；同时支持Web/PWA/Linux/Win/MacOS平台

**💡 核心亮点更新 (中文)**：
- 统一版本
- 更新默认模型

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# 2.26.9
- 统一版本
- 更新默认模型
```
</details>

---
### 📦 [labring/FastGPT](https://github.com/labring/FastGPT)
`⭐ Stars: 30,086` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v4.17.4](https://github.com/labring/FastGPT/releases/tag/v4.17.4) (2026-11-05)`

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
`⭐ Stars: 9,949` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.3.2](https://github.com/yihong0618/bilingual_book_maker/releases/tag/v1.3.2) (2026-10-30)`

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
`⭐ Stars: 37,505` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.5.1](https://github.com/1Panel-dev/1Panel/releases/tag/v2.5.1) (2026-11-12)`

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
`⭐ Stars: 29,145` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v6.14.4](https://github.com/invoke-ai/InvokeAI/releases/tag/v6.14.4) (2026-11-03)`

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
### 📦 [eosphoros-ai/DB-GPT](https://github.com/eosphoros-ai/DB-GPT)
`⭐ Stars: 20,323` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.8.3](https://github.com/eosphoros-ai/DB-GPT/releases/tag/v0.8.3) (2026-11-17)`

> **简介**：用于下一代 AI + 数据产品的开源代理 AI 数据助手。

**💡 核心亮点更新 (中文)**：
- 改进证据验证和报告恢复（#3348）
- 添加可配置的元数据有效负载索引 (#3305)
- 添加结构化和可追溯的数据分析报告（#3295）

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## ✨ Enhancements

- improve evidence verification and report recovery (#3348)
- add configurable metadata payload indexes (#3305)
- Add structured and traceable data analysis reports (#3295)
- add dashboard workspace with Next.js 16 toolchain upgrade (#3278)
- add Keenable Search MCP connector template (#3227)
- tag Valkey clients with lib-name client\_info\_tag (#3282)
- add llm wiki index for knowledge module (#3276)
- add configurable runtime execution (#3272)
- add Serply search tool (#3243)
- add llm provider ui (#3241)
- add Synthorai as a proxy LLM provider (#3210)
- add observability trace for agent (#3212)

## 🐞 Bug fixes

- harden agent tool calling and report generation (#3373)
- preserve chart order in chat dashboards (#3381)
- return text from BaseOutputParser in streaming calls (#3363)
- confine get\_file to the session working directory (#3357)
- use the page offset when ranking hot apps (#3324)
- keep SQL comment stripping inside the \<sql> tag of api-call blocks (#3274)
- reject missing graph config (#3352)
- raise agentic completion budget and default generation timeout (#3341)
- unify builder skills and harden template creation (#3298)
- patch path traversal and SQL injection vulnerabilities (#3339)
- install tzdata and configure container timezone (#3219)
- treat bare ``` fences as code blocks in the markdown header splitter (#3273)
- fix knowledge space scoping and benchmark security (#3271)
- fix skills upload security (#32
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
`⭐ Stars: 161,718` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [1.20.0](https://github.com/langgenius/dify/releases/tag/1.20.0) (2026-11-18)`

> **简介**：在一个协作工作空间上构建 Agentic 工作流程、RAG 管道，并提供丰富的 AI 模型和工具支持。在云、VPC 或自托管上部署，因此团队无需重建堆栈即可从原型转向生产。

**💡 核心亮点更新 (中文)**：
**Dify 1.20.0 让您的跟踪保持流畅，让您的知识库更安全。** 将跟踪导出到任何 OpenTelemetry 收集器，让 Langfuse 在其遗留摄取端点退役后继续工作，并在上传的知识文件出现之前扫描它们是否存在恶意软件。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
**Dify 1.20.0 keeps your traces flowing and your knowledge bases safer.** Export traces to any OpenTelemetry collector, keep Langfuse working after its legacy ingestion endpoint retirement, and scan uploaded knowledge files for malware before they are indexed. Chatflows can show Agent tool activity as it happens, and personal access tokens let scripts and agents call the Dify OpenAPI on your behalf. The bundled plugin daemon is upgraded to **0.6.15-local**.

[New Features](#user-content-new-features) · [Configuration and Integration Changes](#user-content-configuration-and-integration-changes) · [Database Migrations](#user-content-database-migrations) · [Upgrade Guide](#user-content-upgrade-guide)

## New Features

### New HITL: bring approvals into your team's messaging tools

**Integrate human review into your workflows via email and the messaging tools your team already uses.** New HITL introduces shared channels, centralized contacts, notification templates, and verified approval forms—allowing your team to configure recipients once and reuse them across Human Input nodes, and is now enabled by default (`NEXT_PUBLIC_ENABLE_HITL_IM=true`). (#44864, #45945)

* **Reach approvers where they work.** Configure email and an IM platform—**Slack, Feishu/Lark, Microsoft Teams, DingTalk, or WeCom**—to deliver workflow review requests through your team's existing channels.
* **Manage recipients in Contacts.** Sync IM directories and select approvers from a shared contact l
```
</details>

---
### 📦 [nextai-translator/nextai-translator](https://github.com/nextai-translator/nextai-translator)
`⭐ Stars: 25,071` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.6.55](https://github.com/nextai-translator/nextai-translator/releases/tag/v0.6.55) (2026-11-02)`

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
`⭐ Stars: 149,986` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [langchain-core==1.8.4](https://github.com/langchain-ai/langchain/releases/tag/langchain-core%3D%3D1.8.4) (2026-11-19)`

> **简介**：代理工程平台。

**💡 核心亮点更新 (中文)**：
自 langchain-core==1.8.3 以来的变化

版本（核心）：1.8.4（41964）
feat(core)：标准化消息完成事件的完成原因（41926）
feat(langchain)：使用源元数据标记合成 HITL 工具消息 (41928)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Changes since langchain-core==1.8.3

release(core): 1.8.4 (#41964)
feat(core): standardize finish reason on message-finish events (#41926)
feat(langchain): tag synthetic HITL tool messages with source metadata (#41928)
```
</details>

---
### 📦 [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)
`⭐ Stars: 188,147` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [autogpt-platform-beta-v0.12.0](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.12.0) (2026-11-19)`

> **简介**：AutoGPT 的愿景是为每个人提供易于使用和构建的人工智能。我们的使命是提供工具，以便您可以专注于重要的事情。

**💡 核心亮点更新 (中文)**：
- **更快开始。** 注册步骤更少（不再需要输入两次密码），注册和登录页面立即显示，并且设置不再卡在“正在加载您的设置...”上。注册 Google，您可以在同一步骤中连接 Gmail、云端硬盘和日历。 （#16829、#16831、#16968、#16845、#16877）
- **更安全的登录。** 添加新的帐户登录方式（Google、Microsoft、GitHub 或 Discord）现在需要从收件箱中获取六位数代码，除非该提供商运行您的邮箱（通过 Google 提供 Gmail，通过 Microsoft 提供 Outlook.com）。每当添加新的登录方法时，您也会收到一封电子邮件。 (#16860)
- **永远不会丢失消息。** 如果 Otto 无法确认您的消息已送达，只需单击“再次发送”即可发送消息（包括文件），无需发送两次。 “思考……”现在会一直持续到奥托开始回答为止，所以你总是知道它正在发挥作用。 （＃17041，＃16962，＃17038）

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## ⚠️ Breaking change

**The frontend no longer reads `TRUST_X_FORWARDED_FOR`** (#16530, @Pwuts). A self-hosted frontend that set it by hand gets no client IP from `X-Forwarded-For` for the sign-in IP log, IP blocks and per-visitor store search until `TRUSTED_PROXIES` lists the proxy in front of it. The single-container image and Vercel need nothing.

**What to do:** if your frontend sets `TRUST_X_FORWARDED_FOR`, remove it and set `TRUSTED_PROXIES` to a comma-separated list of the addresses or CIDR ranges of the proxies in front of it. Until you do, the frontend logs a warning at start that the old setting is ignored. The same `TRUSTED_PROXIES` setting now also names the proxies for the backend and the External API's per-address limits, replacing `FORWARDED_ALLOW_IPS` and `TRUSTED_PROXY_COUNT`, which keep working but are deprecated; behind your own reverse proxy, the single-container image takes it too. See [Client IP Addresses](https://github.com/Significant-Gravitas/AutoGPT/blob/master/docs/platform/client-ip.md).

---

## ✨ Highlights

- **Get started faster.** Signing up takes fewer steps (no more typing your password twice), the sign-up and login pages show up right away, and setup no longer gets stuck on "Loading your setup…". Sign up with Google and you can connect Gmail, Drive and Calendar in the same step. (#16829, #16831, #16968, #16845, #16877)
- **Safer sign-ins.** Adding a new way to sign in to your account (Google, Microsoft, GitHub or Discord) now ta
```
</details>

---
### 📦 [rockbenben/ChatGPT-Shortcut](https://github.com/rockbenben/ChatGPT-Shortcut)
`⭐ Stars: 8,976` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v4.5.2](https://github.com/rockbenben/ChatGPT-Shortcut/releases/tag/v4.5.2) (2026-11-04)`

> **简介**：Stop writing prompts from scratch — a searchable prompt library for ChatGPT, Claude, Gemini and Cursor · Русский 한국어 العربية हिन्दी ไทย ｜ 别再从头写提示词：现成的拿来就用，好用的收进自己的库

**💡 核心亮点更新 (中文)**：
**完整变更日志**：https://github.com/rockbenben/ChatGPT-Shortcut/compare/v4.5.1...v4.5.2

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
This release distinguishes network failures from genuinely empty states, enforces strict polling session isolation, and delivers noticeable performance gains across interactions.

### Fixed

- **Failure states separated from empty results**: Previously, network errors in comments, search, and collection feeds rendered misleading empty states ("No comments yet", "Prompt not found"). This update properly separates errors from empty data:
  - Network errors now surface a dedicated "Retry" action that bypasses the 60-minute cache suppression window.
  - Temporary network blips no longer falsely report prompts as deleted or inject incorrect `noindex` directives.
- **Session-scoped polling guards**: Switches between prompts immediately invalidate stale polling workers, preventing out-of-order responses from writing into newly opened cards.
- **Auth flow consistency**: Visiting community details or performing protected actions while logged out now opens the login modal directly rather than showing transient toasts.

### Added & Improved

- **Visibility badges & placeholder highlights**: Public prompts now feature a globe icon and clear visibility tooltips; bracketed `[placeholders]` are visually highlighted with replacement tips below the Copy button.
- **Performance optimizations (INP & LCP)**: Modals are preloaded during browser idle intervals and pointer events to eliminate chunk-loading delays (improved INP); offscreen community cards apply `content-visibility: auto
```
</details>

---
### 📦 [pionxzh/chatgpt-exporter](https://github.com/pionxzh/chatgpt-exporter)
`⭐ Stars: 2,902` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [userscript-v2.39.0](https://github.com/pionxzh/chatgpt-exporter/releases/tag/userscript-v2.39.0) (2026-11-20)`

> **简介**：导出并分享您的 ChatGPT 对话历史记录

**💡 核心亮点更新 (中文)**：
* 添加提示标题到 Markdown 导出 ([5879a14](https://github.com/pionxzh/chatgpt-exporter/commit/5879a142d3f5208a7f8e4b1e374012e568fe1ac4))，关闭[#370](https://github.com/pionxzh/chatgpt-exporter/issues/370)
* 导入跨多个文件的官方导出拆分 ([023cf2b](https://github.com/pionxzh/chatgpt-exporter/commit/023cf2b1ece2d41d9be326c026f7ae6ae10c9ae5))

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## [2.39.0](https://github.com/pionxzh/chatgpt-exporter/compare/userscript-v2.38.3...userscript-v2.39.0) (2026-11-20)


### Features

* add prompt headings to Markdown exports ([5879a14](https://github.com/pionxzh/chatgpt-exporter/commit/5879a142d3f5208a7f8e4b1e374012e568fe1ac4)), closes [#370](https://github.com/pionxzh/chatgpt-exporter/issues/370)
* import an official export split across several files ([023cf2b](https://github.com/pionxzh/chatgpt-exporter/commit/023cf2b1ece2d41d9be326c026f7ae6ae10c9ae5))
* use # prompt headings and title code-first prompts by their text ([e2eb460](https://github.com/pionxzh/chatgpt-exporter/commit/e2eb460b56b81b765bed0c3d6570a081a9a68958))


### Bug Fixes

* hide thinking preambles in official data exports ([8e5bd2a](https://github.com/pionxzh/chatgpt-exporter/commit/8e5bd2a4ad8e3f87a64f0abb7dd4090f86828145))
* keep prompt and thinking headings under the prompt heading ([ac320be](https://github.com/pionxzh/chatgpt-exporter/commit/ac320be62538d9dbbdb03886d1f3b06adf782815))
* keep scheduled task runs as separate replies ([8b924f5](https://github.com/pionxzh/chatgpt-exporter/commit/8b924f57f4e2ce0b5bffb55661f8b48ede3bc0b6))
* retain official JSON messages with missing recipient ([44affd4](https://github.com/pionxzh/chatgpt-exporter/commit/44affd4d68c88f73be59f8adda521da08ba95ba0))
```
</details>

---
### 📦 [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent)
`⭐ Stars: 48,046` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [2.2.2](https://github.com/zhayujie/CowAgent/releases/tag/2.2.2) (2026-10-30)`

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
`⭐ Stars: 2,539` &nbsp;|&nbsp; `💻 语言: Shell` &nbsp;|&nbsp; `🏷️ 最新版本: [20261108](https://github.com/lxhao61/integrated-examples/releases/tag/20261108) (2026-11-08)`

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
`⭐ Stars: 22,481` &nbsp;|&nbsp; `💻 语言: Shell` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.5.42](https://github.com/mack-a/v2ray-agent/releases/tag/v3.5.42) (2026-11-23)`

> **简介**：Xray、Tuic、hysteria2、sing-box 八合一一键脚本

**💡 核心亮点更新 (中文)**：
- 修复 Hysteria2 端口跳跃链接和二维码，使用单一连接端口，并通过 mport 传递跳跃范围
- Hysteria2 上下行带宽可分别填 0，订阅和二维码省略对应字段
- 修复 sing-box 未设置默认出站时误用 SOCKS5 节点的问题，保留原有默认出站，无原有出站时回退直连

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
fix(脚本): 修复 Hysteria2 订阅、SOCKS5 默认出站及 REALITY 目标残留问题

- 修复 Hysteria2 端口跳跃链接和二维码，使用单一连接端口，并通过 mport 传递跳跃范围
- Hysteria2 上下行带宽可分别填 0，订阅和二维码省略对应字段
- 修复 sing-box 未设置默认出站时误用 SOCKS5 节点的问题，保留原有默认出站，无原有出站时回退直连
- 新增 SOCKS5 节点后提示添加分流规则，并将所选入站和账号作为规则的默认选项
- 卸载订阅时清理订阅状态及指向该监听地址的 REALITY 目标，删除配置失败时中止当前流程
```
</details>

---
### 📦 [electerm/electerm](https://github.com/electerm/electerm)
`⭐ Stars: 15,688` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v5.12.6](https://github.com/electerm/electerm/releases/tag/v5.12.6) (2026-11-22)`

> **简介**：📻免费开源终端/ssh/sftp/ftp/telnet/串口/RDP/VNC/Spice客户端(Linux, Mac, Windows, Android, HarmonyOS, iOS)

**💡 核心亮点更新 (中文)**：
- 使用 Enter 重新加载停止的终端 (#4773)
- 添加直接书签编辑到选项卡上下文菜单 (#4755)
- 将 Cmd+ 绑定到 macOS 上的设置项 (#4760)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
### Major updates

- RDP: open RDP bookmarks with the local Windows client (mstsc.exe) via a per-bookmark switch, for old or non-standard servers the built-in client cannot reach (#4420) (#4761) by @H-TWINKLE

### New features/UI/Updates

- Reload a stopped terminal with Enter (#4773)
- Add direct bookmark edit to the tab context menu (#4755)
- Bind Cmd+, to the settings item on macOS (#4760) by @pcbeingused333
- Localize widget metadata from the widget's own repo (#4745)
- Clarify the widget install warning (#4749)

### Bug fixes

- Security: keep Markdown links out of the app window (#4763)
- Security: keep the main window on the app origin (#4762)
- Security: harden built-in FTP server widget defaults
- Harden static file server widget against DNS rebinding
- Propagate ZMODEM disk backpressure to terminal transports (#4772)
- Fix trzsz transfer framing, file handling and cancellation (#4771)
- Fix ZMODEM download completion, backpressure and split detection (#4770)
- Keep the extension for duplicate ZMODEM downloads (#4750)
- Stop a right click electerm handles from also reaching the program
- Report an empty OpenAI chat message as an error (#4754) by @pcbeingused333
- Fix MCP SFTP upload destinations and conflict handling (#4753) by @cccy0

-----

### 重大更新

- RDP：支持通过书签设置使用 Windows 本地远程桌面客户端 (mstsc.exe) 打开 RDP 书签，可连接内置客户端无法访问的旧版或非标准服务器 (#4420) (#4761)（由 @H-TWINKLE 提供）

### 新功能/界面/更新

- 按回车键重新加载已停止的终端 (#4773)
- 标签页右键菜单支持直接编辑书签 (#4755)
-
```
</details>

---
### 📦 [pbatard/rufus](https://github.com/pbatard/rufus)
`⭐ Stars: 38,466` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [v4.16](https://github.com/pbatard/rufus/releases/tag/v4.16) (2026-11-17)`

> **简介**：可靠的 USB 格式化实用程序

**💡 核心亮点更新 (中文)**：
* 最终解决[愚蠢的 AMI NTFS 驱动程序错误](https://github.com/pbatard/AmiNtfsBug)，以便运行时 UEFI 媒体验证可以在 AMI 搞砸的数百万台 PC 上运行
* 最后报告 USB 3.2+ 设备（USB 3.2 = 20 Gbps、USB 4.0 = 40 Gpbs、USB 4.1 = 80 Gbps — 看，USB 论坛，这真的没那么难！）
* 修复运行时 UEFI 媒体验证期间不考虑 CA 2023 更新的文件

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
* Finally work around that [stupid AMI NTFS driver bug](https://github.com/pbatard/AmiNtfsBug), so that runtime UEFI media validation can work on the millions of PCs that AMI screwed up
* Finally report USB 3.2+ devices (USB 3.2 = 20 Gbps, USB 4.0 = 40 Gpbs, USB 4.1 = 80 Gbps &mdash; See, USB Forum, it's really NOT that hard!)
* Fix the CA 2023 updated files not being taken into account during runtime UEFI media validation
* Fix the "Silent" installation option being potentially applied even when all dependencies aren't met (#3008)
* Fix a regression where "Write as ESP" used the whole drive, instead of the expected 1 GB partition
* Fix WUE timezone duplication for non English locales (#3070, #2499) and reinstate the use of dots in local usernames (#3057)
* Add classic right click context menu restoration to the QoL improvements option (courtesy of @Fredolx , #3007)
* Drop the ever problematic use of Group Policies when disabling the _"Do you want to format this drive?"_ prompt (#3042)
* Improve raw image partition (re)mount (courtesy of @jaredhagel2, #3002)
* Update embedded [GRUB](https://gitlab.com/gnu_grub/grub) to version 2.16
* Update [libcdio](https://github.com/libcdio/libcdio-C) to latest
* Update the official UEFI DBX URLs, since they were changed by Microsoft
* Address multiple vulnerabilities, courtesy of @indep-arg, @andife, Adam Korczynski, @SilentSobs and @kasparovabi: 
  - GHSA-hhx4-pjqh-499x, GHSA-hrxr-p5wv-qxm2, GHSA-6xgr-6q48-jwxr, GHSA-xh22-8p
```
</details>

---
### 📦 [pymumu/smartdns](https://github.com/pymumu/smartdns)
`⭐ Stars: 11,447` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [Release48.5](https://github.com/pymumu/smartdns/releases/tag/Release48.5) (2026-11-20)`

> **简介**：A local DNS server to obtain the fastest website IP for the best Internet experience, support DoT, DoH, DoQ. 一个本地DNS服务器，获取最快的网站IP，获得最佳上网体验，支持DoH，DoT，DoQ。

**💡 核心亮点更新 (中文)**：
* 修复（conf）：在 https://github.com/pymumu/smartdns/pull/2497 中使用 https:// URL 为 server-http3 保留 HTTP/3

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

**Full Changelog**: https://github.com/pymumu/smartdns/compare/Release48.4...Release48.5
```
</details>

---
### 📦 [XTLS/Xray-core](https://github.com/XTLS/Xray-core)
`⭐ Stars: 43,102` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v26.11.9](https://github.com/XTLS/Xray-core/releases/tag/v26.11.9) (2026-11-09)`

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

## <span id="-影音媒体与下载">🎬 影音媒体与下载</span>

### 📦 [mikf/gallery-dl](https://github.com/mikf/gallery-dl)
`⭐ Stars: 20,621` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.32.21](https://github.com/mikf/gallery-dl/releases/tag/v1.32.21) (2026-11-21)`

> **简介**：用于从多个图像托管站点下载图像库和集合的命令行程序

**💡 核心亮点更新 (中文)**：
- **补充**
- [fastpic] 添加 `image` 提取器 ([`gh#9886`](https://github.com/mikf/gallery-dl/issues/9886))
- [topfaps] 添加支持 ([`cb#281`](https://codeberg.org/mikf/gallery-dl/issues/281) [`pr#595`](https://codeberg.org/mikf/gallery-dl/pulls/595))

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Active development has moved to [Codeberg](https://codeberg.org/mikf/gallery-dl)\
(see [[Announcement] Moving to Codeberg](https://github.com/mikf/gallery-dl/issues/9374) for details)

https://codeberg.org/mikf/gallery-dl/releases/tag/v1.32.21

-------------------

### Extractors
- **Additions**
  - [fastpic] add `image` extractor ([`gh#9886`](https://github.com/mikf/gallery-dl/issues/9886))
  - [topfaps] add support ([`cb#281`](https://codeberg.org/mikf/gallery-dl/issues/281) [`pr#595`](https://codeberg.org/mikf/gallery-dl/pulls/595))
- **Removals**
  - [E621] remove `e6ai.net`
- **aryion**
  - extract `date_uploaded` metadata ([`cb#632`](https://codeberg.org/mikf/gallery-dl/issues/632))
- **celebforum**
  - fix `KeyError: 'articleSection'` ([`cb#635`](https://codeberg.org/mikf/gallery-dl/issues/635))
  - support `/thread/` URLs, fix `forum` extractor ([`cb#635`](https://codeberg.org/mikf/gallery-dl/issues/635))
- **Danbooru**
  - don't send session cookies with API keys ([`cb#638`](https://codeberg.org/mikf/gallery-dl/issues/638) [`gh#9902`](https://github.com/mikf/gallery-dl/issues/9902))
- **e621**
  - update to new API response layout ([`cb#645`](https://codeberg.org/mikf/gallery-dl/issues/645) [`cb#649`](https://codeberg.org/mikf/gallery-dl/issues/649) [`gh#9895`](https://github.com/mikf/gallery-dl/issues/9895))
  - normalize `v2` API responses & request `mode=extended` ([`pr#647`](https://codeberg.org/mikf/gallery-dl/pulls/647) [`gh#9898`](https:/
```
</details>

---
### 📦 [anefzaoui/misterdownloadmanager](https://github.com/anefzaoui/misterdownloadmanager)
`⭐ Stars: 16,945` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.5.2](https://github.com/anefzaoui/misterdownloadmanager/releases/tag/v0.5.2) (2026-11-09)`

> **简介**：isterdownloadmanager：终极开源、无尘室下载管理器，使用纯 Rust 从头编写，适用于 Windows、Mac 和 Linux

**💡 核心亮点更新 (中文)**：
- **Torrent → 文件…**：任何 torrent 的 torrent 文件列表（正在运行、已停止或已完成），带有一个用于选择每个文件的框（也是文件属性中的文件…按钮）。
- **下载列表中的 torrent 两列** ([#357](https://github.com/anefzaoui/misterdownloadmanager/issues/357))：**对等点**（Torrent 在运行时已连接的那些人，播种者和吸血者）和 **分享率**（在 **传输率** 之后，它发送的内容与它占用的内容）。在他们到达那里之前保存的布局。
- 扩展的**此页面上的媒体**可以在其页面之后命名文件：**使用页面标题作为媒体文件名前缀**将页面标题放在文件自己的名称之前。安装时关闭。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
**On a Mac?** The `-experimental` files are fresh builds for Mac (Apple Silicon and Intel) that we haven't tried ourselves yet. Want to be among the first? Give them a go and tell us how it went in an [issue](https://github.com/anefzaoui/misterdownloadmanager/issues).

A big fixes release: YouTube and video downloads, crashes and freezes, downloads on slow disks, the Mac helper, plus a Safari extension, far more file types and a few new columns and options.

### Added

- **Torrent → Files…**: the list of a torrent's files for any torrent, running, stopped or finished, with a box to choose each (also a Files… button in File Properties).
- **Two columns for torrents in the download list** ([#357](https://github.com/anefzaoui/misterdownloadmanager/issues/357)): **Peers** (those a torrent has connected while it runs, seeders and leechers alike) and **Share ratio** (what it has sent against what it took), after **Transfer rate**. A layout saved before them gets them there.
- The extension's **Media on this page** can name a file after its page: **Prefix media file names with the page title** puts the page's title before the file's own name. Off as installed.
- **Far more file types taken from the browser by default** ([#382](https://github.com/anefzaoui/misterdownloadmanager/issues/382)): AI models and datasets (GGUF, SAFETENSORS, CKPT, PT, ONNX, PARQUET...), 3D and CAD (GLB, FBX, OBJ, STL, BLEND, STEP...), design and camera RAW files, ebooks, Office files, DAT, disk images and sp
```
</details>

---
### 📦 [Kianuni/Erosion-CN](https://github.com/Kianuni/Erosion-CN)
`⭐ Stars: 2,730` &nbsp;|&nbsp; `💻 语言: Swift` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.0.6](https://github.com/Kianuni/Erosion-CN/releases/tag/v1.0.6) (2026-11-19)`

> **简介**：iOS / iPadOS 国行 Apple 智能、eSIM 与 MobileGestalt 系统配置工具箱（中英双语 · 防白苹果安全加固版） | Bootloop-Safe iOS / iPadOS MobileGestalt, Apple Intelligence & eSIM Toolbox (EN/ZH)

**💡 核心亮点更新 (中文)**：
- **Dedicated Whitelist Manager (`白名单`)**：Added top-bar & Overview card entry points supporting **manual `Bundle ID` / `AppGroup ID` entry**, **quick-picking from installed third-party containers**, **manual container subpath entry**, and one-tap deletion of rules.
- **Per-App, Per-Path & File Browser Controls**：Whitelist an entire app + its matching `group.<bundleID>` AppGroups from the container `⋯` menu, exempt a specific folder/config via the row **Ignore (`加白`)** button, or long-press any file/folder in **File Browser** → **Add to Ad Whitelist**.
- **Auto-Skip & Auto-Restore**：Whitelisted apps and paths automatically skip global **Lock All** (`一键全锁`) and immediately restore `0755`/`0644` writable permissions (cleaning `.erosion_adlock`) when added. Includes a removable default crash-guard entry for **SMZDM (`什么值得买` · `com.smzdm.client.ios`)**.

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Erosion-CN v1.0.6 (Build 31)

> [!IMPORTANT]
> **System Compatibility / 系统兼容性提示**  
> - **Supported / 完整支持**：`iOS / iPadOS 27.0 – 27.2.1` and `27.3 beta 1` (`24C503*`).  
> - **Patched / 已封堵**：Apple patched `worse_query` starting in **`iOS 27.3 beta 2` (`24C5049d+`)**. Do **NOT** update past `27.3 beta 1` if you rely on Erosion-CN.

---

### What's New / 更新内容

1. **General Splash Ad Blocker Whitelist & Manual Manager (`AdWhitelistStore` / `AdWhitelistManagerSheet`) / 去广告应用与路径通用白名单及手动管理面板** *(Thanks to [@appleoner](https://github.com/appleoner) for suggesting [#56](https://github.com/Kianuni/Erosion-CN/issues/56) / 感谢 [@appleoner](https://github.com/appleoner) 在 [#56](https://github.com/Kianuni/Erosion-CN/issues/56) 提出建议)*
   - **Dedicated Whitelist Manager (`白名单`)**：Added top-bar & Overview card entry points supporting **manual `Bundle ID` / `AppGroup ID` entry**, **quick-picking from installed third-party containers**, **manual container subpath entry**, and one-tap deletion of rules.
   - **Per-App, Per-Path & File Browser Controls**：Whitelist an entire app + its matching `group.<bundleID>` AppGroups from the container `⋯` menu, exempt a specific folder/config via the row **Ignore (`加白`)** button, or long-press any file/folder in **File Browser** → **Add to Ad Whitelist**.
   - **Auto-Skip & Auto-Restore**：Whitelisted apps and paths automatically skip global **Lock All** (`一键全锁`) and immediately restore `0755`/`0644` writable permissions (cleaning `.erosion_adlock`) when
```
</details>

---
### 📦 [ziyuanhuishequ/release-downloader](https://github.com/ziyuanhuishequ/release-downloader)
`⭐ Stars: 64` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.6.3](https://github.com/ziyuanhuishequ/release-downloader/releases/tag/v1.6.3) (2026-11-08)`

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
`⭐ Stars: 1,282` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.1.0](https://github.com/threerocks/sweety-handdraw-video/releases/tag/v3.1.0) (2026-11-11)`

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
`⭐ Stars: 30,078` &nbsp;|&nbsp; `💻 语言: C#` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.5.0](https://github.com/KnifeLemon/Filee/releases/tag/v2.5.0) (2026-11-16)`

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
### 📦 [paulrosen/abcjs](https://github.com/paulrosen/abcjs)
`⭐ Stars: 2,376` &nbsp;|&nbsp; `💻 语言: HTML` &nbsp;|&nbsp; `🏷️ 最新版本: [v6.7.3](https://github.com/paulrosen/abcjs/releases/tag/v6.7.3) (2026-11-18)`

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
### 📦 [LibreSpark/LibreTV](https://github.com/LibreSpark/LibreTV)
`⭐ Stars: 25,622` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.24.0](https://github.com/LibreSpark/LibreTV/releases/tag/v2.24.0) (2026-11-18)`

> **简介**：一分钟搭建影视站，支持Docker等部署方式

**💡 核心亮点更新 (中文)**：
获取方式

Docker（多架构 linux/amd64 / linux/arm64）

```bash
docker pull docker.io/bestzwei/libretv:2.24.0
docker pull ghcr.io/librespark/libretv:2.24.0
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
docker pull docker.io/bestzwei/libretv:2.24.0
docker pull ghcr.io/librespark/libretv:2.24.0
```

两个 registry 的镜像内容一致（同一组 digest），`latest` 也指向本版本。

### 免 Docker（下方附件，Node 18+）

```bash
sha256sum -c SHA256SUMS
tar -xzf libretv-2.24.0-standalone.tar.gz -C libretv
cd libretv && PASSWORD=your-password PORT=8080 node server.js
```

预构建包与 CPU 架构无关（x86_64 / arm64 / armv7），环境变量与 Docker 部署一致。

> 镜像由 docker-publish 工作流在同一 tag 上构建，刚发布时可能还要 5–10 分钟才可拉取。

## 变更

完整对比：https://github.com/LibreSpark/LibreTV/compare/v2.23.2...v2.24.0
```
</details>

---
### 📦 [dyang886/Game-Cheats-Manager](https://github.com/dyang886/Game-Cheats-Manager)
`⭐ Stars: 16,906` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.5.5](https://github.com/dyang886/Game-Cheats-Manager/releases/tag/v2.5.5) (2026-11-14)`

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
`⭐ Stars: 47,166` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2026.11.23-8728.g61f4512](https://github.com/DIYgod/RSSHub/releases/tag/v2026.11.23-8728.g61f4512) (2026-11-23)`

> **简介**：🧡 一切都是RSSible

**💡 核心亮点更新 (中文)**：
-ghcr.io/diygod/rsshub:61f451228e0420f7b44184d231fd7e98bfef26ea
- ghcr.io/diygod/rsshub:chromium-bundled-61f451228e0420f7b44184d231fd7e98bfef26ea
- diygod/rsshub:61f451228e0420f7b44184d231fd7e98bfef26ea

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Source commit: 61f451228e0420f7b44184d231fd7e98bfef26ea

Published multi-platform images:
- ghcr.io/diygod/rsshub:61f451228e0420f7b44184d231fd7e98bfef26ea
- ghcr.io/diygod/rsshub:chromium-bundled-61f451228e0420f7b44184d231fd7e98bfef26ea
- diygod/rsshub:61f451228e0420f7b44184d231fd7e98bfef26ea
- diygod/rsshub:chromium-bundled-61f451228e0420f7b44184d231fd7e98bfef26ea

Use these commit-specific image tags to reproduce this release. Daily Docker tags may be updated by subsequent builds.
```
</details>

---
### 📦 [amir1376/ab-download-manager](https://github.com/amir1376/ab-download-manager)
`⭐ Stars: 19,478` &nbsp;|&nbsp; `💻 语言: Kotlin` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.11.4](https://github.com/amir1376/ab-download-manager/releases/tag/v1.11.4) (2026-11-03)`

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
`⭐ Stars: 9,758` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.7.1](https://github.com/gyroflow/gyroflow/releases/tag/v1.7.1) (2026-11-20)`

> **简介**：使用陀螺仪数据进行视频稳定

**💡 核心亮点更新 (中文)**：
- **Canon Cinema RAW Light (.crm) 播放** - CRM 剪辑现在可以直接在 Gyroflow 中打开和播放，不再需要可播放的副本。第一次打开（Win​​dows x64、macOS、Linux x64）时会下载 Canon RAW SDK。与 BRAW 一样，无法在应用程序中渲染它们：导出项目文件并使用视频编辑器插件之一
- 在“高级”中添加了“默认 CLI 行为”：Gyroflow 对其启动的文件执行的操作，例如从“打开方式”菜单或将它们拖放到其图标上时。它可以渲染它们（像以前一样），在应用程序中打开它们，或将它们添加到渲染队列中。带有任何选项（例如“-f”）的命令行不受影响
- GoPro HERO4 Black/Silver：现在会从剪辑的视野（宽或中）中自动选择镜头配置文件，以与外部运动数据一起使用。 HERO3 文件现在被识别为 GoPro（通过

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
### ✨ Improvements
- **Canon Cinema RAW Light (.crm) playback** - CRM clips now open and play directly in Gyroflow, a playable copy is no longer needed. The Canon RAW SDK is downloaded the first time you open one (Windows x64, macOS, Linux x64). As with BRAW, rendering them in the app isn't available: export a project file and use one of the video editor plugins
- Added "Default CLI behavior" in `Advanced`: what Gyroflow does with the files it's started with, e.g. from the "Open with" menu or when they're dropped on its icon. It can render them (as before), open them in the app, or add them to the render queue. A command line with any option (e.g. `-f`) isn't affected
- GoPro HERO4 Black/Silver: the lens profile is now selected automatically from the clip's field of view (Wide or Medium), for use with external motion data. HERO3 files are now recognized as GoPro (by @anton-belkin)
- GMFlow (AI): stability fixes on some GPUs, and less time spent tuning for the GPU

### 🐛 Bug fixes
- Fixed the horizon drifting with horizon lock in clips with a lot of motion, e.g. aerobatic flights, FPV and skiing (regression in 1.7.0) (#1287)
- Fixed a tilted horizon with horizon lock on cameras with a large gyro bias, e.g. some Sony a7 IV (#1298)
- Fixed the picture jumping a few frames before the end of a trim range (or after its start), also in the rendered video
- Fixed rendering to a network drive (SMB) on macOS (#1291)
- Fixed the preview being very pixelated (stuck at 32x32 px
```
</details>

---
### 📦 [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp)
`⭐ Stars: 210,084` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [2026.10.26](https://github.com/yt-dlp/yt-dlp/releases/tag/2026.10.26) (2026-10-26)`

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
`⭐ Stars: 80,067` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [33.0.3](https://github.com/obsproject/obs-studio/releases/tag/33.0.3) (2026-11-22)`

> **简介**：OBS Studio - 用于直播和屏幕录制的免费开源软件

**💡 核心亮点更新 (中文)**：
- 修复了 Windows 33.0.2 中某些较旧 CPU 的崩溃问题 [R1CH/Warchamp7]
* 修复了 macOS 屏幕捕获在基于 Intel 的系统上不工作的问题 [jcm93]
* 修复了混合 MP4 不按时间分割的问题 [Johnsoac671]

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
33.0.3 Hotfix Changes
---------------------

- Fixed a crash on Windows in 33.0.2 with certain older CPUs [R1CH/Warchamp7]


33.0.2 Hotfix Changes
---------------------

* Fixed macOS Screen Capture not working on Intel-based systems [jcm93]
* Fixed Hybrid MP4 not splitting by time [Johnsoac671]
* Fixed frequent audio dropouts on Decklink output [CyBeRoni]
* Fixed a potential crash when right-clicking a spinbox in certain places [Warchamp7]
* Fixed a crash during shutdown when a native device dialog is still open [prgmitchell]
* Fixed YouTube AutoStop being mistakenly set to the AutoStart value [fcolona]
* Fixed a crash when source properties change while a subdialog such as Font selection is open [prgmitchell]
* Fixed a crash related to browser source memory allocation on Linux [tytan652/WizardCM]
* Fixed a bug where controller inputs in browser sources no longer worked when OBS lost focus on Windows & macOS [WizardCM]
* Fixed a crash on macOS when a browser source would request Bluetooth access [tytan652/WizardCM]
* Fixed a potential crash when a browser source would request a Passkey [tytan652/WizardCM]
* Enable WebGPU support on Windows for browser sources [WizardCM]
* Fixed a potential crash when initializing the virtual cam [notr1ch]
* Fixed a potential crash when unloading the virtual cam [notr1ch]
* Fixed a potential crash related to vertex buffers [notr1ch]
* Fixed repeated log entries sometimes not being truncated [exeldro]
* Fixed a browser
```
</details>

---
### 📦 [jerrykuku/luci-theme-argon](https://github.com/jerrykuku/luci-theme-argon)
`⭐ Stars: 5,647` &nbsp;|&nbsp; `💻 语言: CSS` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.1.4](https://github.com/jerrykuku/luci-theme-argon/releases/tag/v3.1.4) (2026-11-13)`

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
### 📦 [LibreELEC/LibreELEC.tv](https://github.com/LibreELEC/LibreELEC.tv)
`⭐ Stars: 2,863` &nbsp;|&nbsp; `💻 语言: Makefile` &nbsp;|&nbsp; `🏷️ 最新版本: [12.95.1](https://github.com/LibreELEC/LibreELEC.tv/releases/tag/12.95.1) (2026-11-14)`

> **简介**：刚好够 KODI 运行的操作系统

**💡 核心亮点更新 (中文)**：
该版本未提供详细更新说明。

---
### 📦 [agalwood/Motrix](https://github.com/agalwood/Motrix)
`⭐ Stars: 58,707` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.4.5](https://github.com/agalwood/Motrix/releases/tag/v2.4.5) (2026-11-20)`

> **简介**：功能齐全的下载管理器。

**💡 核心亮点更新 (中文)**：
* feat(release)：在 2.4.5 中默认启用配对桌面切换，位于 https://github.com/agalwood/Motrix/pull/2539

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# Motrix 2.4.5

English | [简体中文](https://github.com/agalwood/Motrix/blob/main/docs/release-notes/2.4.5.zh-CN.md)

## Changes since 2.4.4

- Desktop now accepts recoverable handoffs from paired browser extensions by default. Browser Extension **0.1.25** negotiates this capability for eligible paused downloads. If the connection drops after submission, the extension can recover the existing task ID.
- Existing extensions and older hosts continue to support the original download submission method. To stop accepting new handoffs on Desktop, launch with `MOTRIX_DOWNLOAD_HANDOFF=0`; previously prepared operations can still finish.

## Upgrade compatibility

**Back up your profile and download files before upgrading.** The bundled engine
uses SQLite **schema 6**. When upgrading an older engine database, retain its
complete pre-upgrade backup; older engines cannot open schema 6. Stop all engines
before restoring a verified backup to a separate path for a downgrade. Do not
reset or delete the upgraded database as a substitute for recovery.

Users migrating from Motrix v1 should follow the
[migration guide](https://github.com/agalwood/Motrix/blob/v2.4.5/docs/legacy-migration.md)
and retain the original profile and engine database backups.

## Downloads and updates

Desktop packages support macOS 13 or later, Windows 10 or later, and Linux, with
native x64 and ARM64 builds. No 32-bit desktop packages are provided. Official
macOS packages require signing and notarization. Windows NSIS in
```
</details>

---
### 📦 [subhra74/xdm](https://github.com/subhra74/xdm)
`⭐ Stars: 8,777` &nbsp;|&nbsp; `💻 语言: Kotlin` &nbsp;|&nbsp; `🏷️ 最新版本: [9.0.12](https://github.com/subhra74/xdm/releases/tag/9.0.12) (2026-11-22)`

> **简介**：自 2013 年以来，快速、可靠的下载加速器和视频下载器

**💡 核心亮点更新 (中文)**：
下载

|安装人员 |笔记|
|---|---|
| [xdm-9.0.12-x64.msi](https://github.com/subhra74/xdm/releases/download/9.0.12/xdm-9.0.12-x64.msi) |对于 Windows x64 (Windows 10/11) |
| [xdm-9.0.12-arm64.msi](https://github.com/subhra74/xdm/releases/downl

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Downloads

| Installer | Notes |
|---|---|
| [xdm-9.0.12-x64.msi](https://github.com/subhra74/xdm/releases/download/9.0.12/xdm-9.0.12-x64.msi) | For Windows x64 (Windows 10/11) |
| [xdm-9.0.12-arm64.msi](https://github.com/subhra74/xdm/releases/download/9.0.12/xdm-9.0.12-arm64.msi) | For Windows ARM (Windows 10/11) |
| [xdmsetup-9.0.12.msi](https://github.com/subhra74/xdm/releases/download/9.0.12/xdmsetup-9.0.12.msi) | Same as the x64 MSI; for XDM 8 (Microsoft Store) update notices |
| [xdm-app-9.0.12-linux-x64.flatpak](https://github.com/subhra74/xdm/releases/download/9.0.12/xdm-app-9.0.12-linux-x64.flatpak) | For any Linux x64 (Flatpak bundle; runtime installs from Flathub) |
| [xdm-app-9.0.12-linux-arm64.flatpak](https://github.com/subhra74/xdm/releases/download/9.0.12/xdm-app-9.0.12-linux-arm64.flatpak) | For any Linux ARM (Flatpak bundle; runtime installs from Flathub) |
| [xdm-app_9.0.12_amd64.deb](https://github.com/subhra74/xdm/releases/download/9.0.12/xdm-app_9.0.12_amd64.deb) | For Debian / Ubuntu / Linux Mint x64 |
| [xdm-app_9.0.12_arm64.deb](https://github.com/subhra74/xdm/releases/download/9.0.12/xdm-app_9.0.12_arm64.deb) | For Debian / Ubuntu / Linux Mint ARM |
| [xdm-app-9.0.12-1.x86_64.rpm](https://github.com/subhra74/xdm/releases/download/9.0.12/xdm-app-9.0.12-1.x86_64.rpm) | For Fedora / RHEL / openSUSE x64 |
| [xdm-app-9.0.12-1.aarch64.rpm](https://github.com/subhra74/xdm/releases/download/9.0.12/xdm-app-9.0.12-1.aarch64.rpm) | For Fedora / RHEL / openS
```
</details>

---

## <span id="-效率办公与创作">📝 效率办公与创作</span>

### 📦 [s1dashu/quiet-md](https://github.com/s1dashu/quiet-md)
`⭐ Stars: 2,655` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.1.14](https://github.com/s1dashu/quiet-md/releases/tag/v0.1.14) (2026-11-22)`

> **简介**：适用于 macOS、Windows 和 Linux 的超快本机笔记应用程序和富文本编辑器。使用 Rust + GPUI 构建。本地优先且设计精美。

**💡 核心亮点更新 (中文)**：
- **正则查找**：查找替换栏里点 `.*` 就按正则表达式匹配（不区分大小写，在一行内匹配），替换时可以用 `$1`、`${name}` 引用分组，替换后保留原来的文字样式；写错的表达式会提示「正则有误」。
- **Obsidian 双链**：导入的 Obsidian 库里，`[[笔记]]`、`[[文件夹/笔记]]`、`[[笔记#标题]]` 这样的双链点一下就打开对应的笔记，规则和 Obsidian 一致（不区分大小写、路径可省、同一文件夹优先）。
- **新语言和从右往左排版**：新增土耳其语界面，界面语言一共 9 种。阿拉伯语正确连写；从右往左的段落靠右排，光标、选区和方向键都按从右往左走，列表符号在右侧。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# Quiet.md 0.1.14

## 中文

这次更新带来正则查找、Obsidian 双链跳转、可下载的文档字体、土耳其语界面和从右往左的阿拉伯语排版，也让大文档库里的搜索和删除快了很多。

- **正则查找**：查找替换栏里点 `.*` 就按正则表达式匹配（不区分大小写，在一行内匹配），替换时可以用 `$1`、`${name}` 引用分组，替换后保留原来的文字样式；写错的表达式会提示「正则有误」。
- **Obsidian 双链**：导入的 Obsidian 库里，`[[笔记]]`、`[[文件夹/笔记]]`、`[[笔记#标题]]` 这样的双链点一下就打开对应的笔记，规则和 Obsidian 一致（不区分大小写、路径可省、同一文件夹优先）。
- **新语言和从右往左排版**：新增土耳其语界面，界面语言一共 9 种。阿拉伯语正确连写；从右往左的段落靠右排，光标、选区和方向键都按从右往左走，列表符号在右侧。
- **字体**：设置 › 外观里可以分别选择界面字体和文档字体，代码块仍用主题的等宽字体。字体列表按黑体、宋体、楷体·手写、等宽、西文等分组，每行用自己的字体显示示例，悬停或用方向键移到某一行就预览整页效果，可以收藏，也会记住最近用过的。
- **按需下载字体**：文档字体可以选霞鹜文楷、朱雀仿宋和小赖手写体，选中时才从 download.quiet.md 下载，列表里显示大小和下载进度，下载的字体可以删除。画板的中日韩手写字体（Xiaolai，14 MB）不再打包进安装包，第一次需要时才下载，下载期间画板先用系统字体。字体文件按哈希校验，除了请求这个文件不发送任何信息。
- **清理未使用资源**：设置 › 文档库可以找出没有任何笔记（包括回收站、版本历史和本机文件）用到的图片和文件，确认后移到文档库的 `.quiet/removed-assets`，30 天后自动删除，期间可以拖回来。
- **退格键回到标题**：设置 › 通用里新增这个开关，默认开（和以前一样，在正文开头按退格会把第一段并入标题）；关掉后光标留在正文里。
- **快捷键变化**：Windows 和 Linux 上「复制为 Markdown」的默认快捷键改为 **Ctrl+Shift+M**（原来的 Ctrl+Alt+Shift+C 在不少键盘布局上会被当成 AltGr 打出字母）。macOS 仍是 ⌘⇧C。自己改过键位的不受影响。
- **更快**：两千篇文档的库里，搜索框每输入一个字从最慢 5 秒多降到 45 毫秒以内；删除 190 篇的文件夹从最慢 1.5 秒降到约 0.1 秒，全选删除 822 项从约 1.1 秒降到约 0.23 秒，清空回收站从约 1 秒降到约 0.08 秒。切换文档时不再每次都同步写盘。
- **窗口和画板**：窗口变窄时自动收起的侧栏，放宽后会自动展开（手动收起的不会）。画板支持触控板双指缩放。笔记和侧栏之间的阴影更淡了。
- **文档菜单**：「…」菜单去掉了「更多」子菜单，「复制为 Markdown」直接放在「下载为」后面；「阅读模式」和「显示引用列表」变成菜单里的开关。
- **修复**：切换文档卡顿；代码块的折叠状态随文档保存；画板选背景色时可能崩溃；深色模式下查找替换和设置弹窗里的按钮看不清；Windows 上的设置说明和首次启动引导不再写 ⌘N 和「访达」；繁体中文界面用词统一（文件庫、垃圾桶）。

数据表这个版本还不开放：新建不了数据表，已有的数据表文件只显示只读占位，文件保持原样。

## English

This up
```
</details>

---
### 📦 [Trulsaa/obsidian-icloud-contacts](https://github.com/Trulsaa/obsidian-icloud-contacts)
`⭐ Stars: 35` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [0.4.22](https://github.com/Trulsaa/obsidian-icloud-contacts/releases/tag/0.4.22) (2026-11-01)`

> **简介**：Obsidian 插件，可从 iCloud 导入联系人并管理每个联系人的注释。

**💡 核心亮点更新 (中文)**：
该版本未提供详细更新说明。

---
### 📦 [ufebri/ray-vault-sync](https://github.com/ufebri/ray-vault-sync)
`⭐ Stars: 4` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [1.4.0](https://github.com/ufebri/ray-vault-sync/releases/tag/1.4.0) (2026-11-08)`

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
### 📦 [huami1314/GestaltX](https://github.com/huami1314/GestaltX)
`⭐ Stars: 8,829` &nbsp;|&nbsp; `💻 语言: Swift` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.1.1](https://github.com/huami1314/GestaltX/releases/tag/v1.1.1) (2026-11-13)`

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
`⭐ Stars: 77` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.1.5](https://github.com/RongleCat/grok-bot-anywhere/releases/tag/v0.1.5) (2026-11-13)`

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
`⭐ Stars: 2,000` &nbsp;|&nbsp; `💻 语言: Swift` &nbsp;|&nbsp; `🏷️ 最新版本: [spektralab-v2.4.2](https://github.com/JamesQiu2005/SpektraLab/releases/tag/spektralab-v2.4.2) (2026-11-18)`

> **简介**：SpektraLab — macOS 电影和打印模拟器。 SwiftUI 应用程序 + Metal/C++ 渲染引擎，链接进来，运行时没有 Python。 andreavolpato/spektrafilm 的一个分支。

**💡 核心亮点更新 (中文)**：
- **macOS 14 Sonoma 或更高版本**：SpektraLab 现在可以在 macOS 14 以及 15 及更高版本上运行。在 macOS 14 上，有一些小问题不存在：库存条不会将选定的胶片或纸张滚动到视图中，并且单击文本字段不会结束其编辑（Return、Esc 或 Tab 会结束）。
- **LibRaw 作为可选的 RAW 解码器**：**设置 › 开发 › RAW 解码器** 提供 **Apple (macOS)**（默认值和每个早期版本所使用的），或 **LibRaw**（开源解码器）。 LibRaw 可以读取 macOS 无法读取的某些相机，并且它的颜色和高光与 Apple 的不同，因此同一张照片在大约相同的曝光度下会产生不同的效果。它在自己的进程中运行，因此触发它的文件无法使应用程序崩溃；它无法读取的文件由 Apple 解码。使用 LibRaw，macOS 自己的镜头校正不可用（镜头数据库和文件自己的配置文件仍然可用）。切换对打开的画面重新进行冲洗；使用 Apple 解码器开发的内容会被保留，并在您切换回来时恢复。
- **许可证**：LibRaw 在 LGPL-2.1 下未经修改地在应用程序内的单独帮助程序中使用。它的通知位于磁盘映像的 **Licenses** 文件夹中，自述文件说明了如何从源代码重建帮助程序。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
SpektraLab 2.4.2 for the Mac: compatibility and stability.

- **macOS 14 Sonoma or later**: SpektraLab now runs on macOS 14 as well as 15 and later. On macOS 14 a few small things are not there: the stock strip does not scroll a chosen film or paper into view, and a click away from a text field does not end its editing (Return, Esc or Tab does).
- **LibRaw as an optional RAW decoder**: **Settings › Develop › RAW decoder** offers **Apple (macOS)**, the default and what every earlier version used, or **LibRaw**, an open-source decoder. LibRaw reads some cameras macOS does not, and its colour and highlights differ from Apple's, so the same photograph develops differently, at about the same exposure. It runs in a process of its own, so a file that trips it cannot take the app down; a file it cannot read is decoded by Apple's. With LibRaw, macOS's own lens correction is not available (the lens database's and a file's own profiles still are). Switching develops the open pictures again; what was developed with Apple's decoder is kept and comes back when you switch back.
- **Licences**: LibRaw is used, unmodified, under the LGPL-2.1, in a separate helper inside the app. Its notices are in the disk image's **Licenses** folder, and the README says how to rebuild the helper from source.

**Download:** `SpektraLab-2.4.2-universal.dmg`, one download for Apple silicon and Intel Macs (macOS 14 or later). Signed with Developer ID and notarised by Apple.
SHA-256 `02f0e258177ae43c158d93b82a2ba
```
</details>

---
### 📦 [robbietilton/Compositor](https://github.com/robbietilton/Compositor)
`⭐ Stars: 18,784` &nbsp;|&nbsp; `💻 语言: Swift` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.7.0](https://github.com/robbietilton/Compositor/releases/tag/v1.7.0) (2026-11-21)`

> **简介**：适用于 Mac 的 Photoshop 替代品

**💡 核心亮点更新 (中文)**：
- 向上和向下箭头现在可以步进调整和过滤面板中的数字

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
- Up and Down arrows now step the numbers in adjustment and filter panels
```
</details>

---
### 📦 [jgraph/drawio-desktop](https://github.com/jgraph/drawio-desktop)
`⭐ Stars: 64,110` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v32.7.4](https://github.com/jgraph/drawio-desktop/releases/tag/v32.7.4) (2026-11-17)`

> **简介**：Draw.io 的官方电子版本

**💡 核心亮点更新 (中文)**：
- 使用电子44.11.3
- 修复了从命令行导出 HTML 失败或挂在非常大的图表上的问题
- 一旦 PNG 或 PDF 文件中嵌入的图表长于应用程序可以容纳的最长文本，就停止读取该图表，而不是先解压缩所有内容

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Release Notes for 32.7.4

[Windows Installer](https://github.com/jgraph/drawio-desktop/releases/download/v32.7.4/draw.io-32.7.4-windows-installer.exe)
[Windows No Installer (zip)](https://github.com/jgraph/drawio-desktop/releases/download/v32.7.4/draw.io-32.7.4-windows.zip)
[macOS - Universal](https://github.com/jgraph/drawio-desktop/releases/download/v32.7.4/draw.io-universal-32.7.4.dmg)
Linux - [deb](https://github.com/jgraph/drawio-desktop/releases/download/v32.7.4/drawio-amd64-32.7.4.deb), [AppImage](https://github.com/jgraph/drawio-desktop/releases/download/v32.7.4/drawio-x86_64-32.7.4.AppImage) or [rpm](https://github.com/jgraph/drawio-desktop/releases/download/v32.7.4/drawio-x86_64-32.7.4.rpm)

**ChangeLog:**

- Uses electron 44.11.3
- Fixes HTML export from the command line failing or hanging on very large diagrams
- Stops reading a diagram embedded in a PNG or PDF file once it is longer than the longest text the app can hold, instead of decompressing all of it first
- Command line PDF exports with --width or --height now contain the diagram, fitted to that size, instead of an empty page [jgraph/drawio-desktop#2162]
- Command line PDF and SVG exports fill in %pagecount% [jgraph/drawio-desktop#2601]
- Command line exports no longer wait forever for an image whose server never answers: an image that makes no progress for 15 seconds is left out and the export completes
- Links in exported SVG and PDF files keep only safe link types, and PDF exports no l
```
</details>

---
### 📦 [Stirling-Tools/Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF)
`⭐ Stars: 97,266` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.5.0](https://github.com/Stirling-Tools/Stirling-PDF/releases/tag/v3.5.0) (2026-11-22)`

> **简介**：GitHub 上排名第一的 PDF 应用程序，可让您在任何地方的任何设备上编辑 PDF

**💡 核心亮点更新 (中文)**：
Stirling Office Convert 现已取代我们 docker 容器中的 Libreoffice！ 
随着速度的提高和更好的质量转换，这也意味着我们的码头工人的尺寸将减半！  感谢所有向我们发送示例文件的人，请k

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Stirling Office Convert has now replaced Libreoffice in our docker containers! 
Along with speed increases and better quality conversions it also means our docker going forward in 3.5.1 will be half the size!  Thank you to everyone who sent us example files, and please keep reporting any conversions that don't look right! We are hoping to get this perfect!

We have also made a big fix for desktop users whose documents were reloading a few seconds after upload, Thank you to everyone who reported this and great to see people using the new feedback button! (In bottom right) 

With the Office Convert change (outside of the tools getting the toggle removed)
- Compress now uses Office Convert
- HTML to PDF supports zoom again
- New admin setting to cap how many Office conversions run at once and queue
- Damaged Office, ebook and HTML files now give a clear "could not be read" message instead of an error

Other changes are:
- Faster desktop PDF operations, with the PDF engine now pre-installed in the app
- Performance improvements across the viewer, file list etc
- JPDFium and other dependency updates causing various bug fixes and improvements 

We also fixed some bugs including:
- Desktop documents reloading themselves and losing progress shortly after being opened
- Filled form fields showing their value twice in the viewer
- Form values being invisible in dark mode
- Thumbnail sidebar getting stuck on "Loading..." after applying changes

Note (breaking chang
```
</details>

---
### 📦 [halo-dev/halo](https://github.com/halo-dev/halo)
`⭐ Stars: 40,377` &nbsp;|&nbsp; `💻 语言: Java` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.27.3](https://github.com/halo-dev/halo/releases/tag/v2.27.3) (2026-11-13)`

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
### 📦 [emoacht/Monitorian](https://github.com/emoacht/Monitorian)
`⭐ Stars: 4,825` &nbsp;|&nbsp; `💻 语言: C#` &nbsp;|&nbsp; `🏷️ 最新版本: [4.16.14-Installer](https://github.com/emoacht/Monitorian/releases/tag/4.16.14-Installer) (2026-11-19)`

> **简介**：轻松调节多台显示器亮度的 Windows 桌面工具

**💡 核心亮点更新 (中文)**：
- 修复扫描时间过长时出现的异常

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
- Fix exception when scanning takes too long
```
</details>

---
### 📦 [YerongAI/Office-Tool](https://github.com/YerongAI/Office-Tool)
`⭐ Stars: 14,791` &nbsp;|&nbsp; `💻 语言: PowerShell` &nbsp;|&nbsp; `🏷️ 最新版本: [v11.9.15.0](https://github.com/YerongAI/Office-Tool/releases/tag/v11.9.15.0) (2026-11-11)`

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
`⭐ Stars: 3,026` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.2.13](https://github.com/TDesktop-x64/tdesktop/releases/tag/v1.2.13) (2026-11-14)`

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
`⭐ Stars: 195,792` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [1.147.0](https://github.com/microsoft/vscode/releases/tag/1.147.0) (2026-11-18)`

> **简介**：视觉工作室代码

**💡 核心亮点更新 (中文)**：
https://code.visualstudio.com/updates/v1_147

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
https://code.visualstudio.com/updates/v1_147
```
</details>

---

## <span id="-网络与代理技术">🌐 网络与代理技术</span>

### 📦 [AdguardTeam/AdGuardHome](https://github.com/AdguardTeam/AdGuardHome)
`⭐ Stars: 38,746` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.0.0](https://github.com/AdguardTeam/AdGuardHome/releases/tag/v1.0.0) (2026-11-19)`

> **简介**：网络范围内的广告和跟踪器阻止 DNS 服务器

**💡 核心亮点更新 (中文)**：
自9月下旬发布AdGuard Home v1.0测试版以来，我们收集了反馈并采取了相应行动。该产品在测试版本中在内部和外观方面都进行了重大修改。稳定版增加了鳍

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Since the beta of AdGuard Home v1.0 was released in late September, we collected feedback and acted accordingly. The product has gone through major overhaul both under the hood and appearance-wise in the beta versions. The stable release adds the fine-tuning that users asked for. Today, we are releasing AdGuard Home v1.0.

## A redesign you don’t have to relearn

The web interface for AdGuard Home has been completely updated to look cleaner, more modern, and fully aligned with the rest of the AdGuard ecosystem. Avoiding overall layout changes was intentional — we didn’t wish for you to stress out while relearning where every button is. We refreshed the visual style while preserving the familiar logic. We wrote extensively about it in our [article on the beta version](https://adguard-dns.io/en/blog/adguard-home-v1-0-beta.html), it is worth a look if you need more information. 

![New dashboard](https://cdn.adtidy.org/content/release_notes/dns/home-v1-0-beta/dashboard.png)

But this overhaul goes deeper than looks. The new frontend shares the backend’s strict optimization philosophy. Rebuilt with fine-grained reactivity, it is now significantly lighter and faster. This update also resolves memory consumption issues linked to the old interface, making AdGuard Home run smoothly on low-power devices, and introduces a fully responsive mobile UI.

![Before and after](https://cdn.adtidy.org/content/release_notes/dns/home-v1-0-beta/adguard_home_before_after.png)

## New re
```
</details>

---
### 📦 [SagerNet/sing-box](https://github.com/SagerNet/sing-box)
`⭐ Stars: 40,213` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.14.4](https://github.com/SagerNet/sing-box/releases/tag/v1.14.4) (2026-10-24)`

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
`⭐ Stars: 10,972` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [2.44.26](https://github.com/sub-store-org/Sub-Store/releases/tag/2.44.26) (2026-11-22)`

> **简介**：QX、Loon、Surge、Stash、Egern 和 Shadowrocket 的高级订阅管理器！

**💡 核心亮点更新 (中文)**：
* feat: 支持 Shadowrocket 非标 mieru URI(部分字段) ([b711e33](https://github.com/sub-store-org/Sub-Store/commit/b711e33))

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## <small>2.44.26 (2026-11-22)</small>

* feat: 支持 Shadowrocket 非标 mieru URI(部分字段) ([b711e33](https://github.com/sub-store-org/Sub-Store/commit/b711e33))
```
</details>

---
### 📦 [233boy/Xray](https://github.com/233boy/Xray)
`⭐ Stars: 2,846` &nbsp;|&nbsp; `💻 语言: Shell` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.37](https://github.com/233boy/Xray/releases/tag/v1.37) (2026-11-02)`

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
`⭐ Stars: 2,723` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.39.0](https://github.com/enfein/mieru/releases/tag/v3.39.0) (2026-10-23)`

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
`⭐ Stars: 15,889` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.5.16](https://github.com/v2rayA/v2rayA/releases/tag/v2.5.16) (2026-11-18)`

> **简介**：一个基于 Xray 的核心的 Web 客户端，在 Linux、Windows 和 macOS 上具有全局透明代理。

**💡 核心亮点更新 (中文)**：
* build(docker)：通过 https://github.com/v2rayA/v2rayA/pull/2124 在镜像中安装发行版的 Alpine 包
* 壮举：在 https://github.com/v2rayA/v2rayA/pull/2058 中添加按订阅更新策略和恢复
* 修复：通过 https://github.com/v2rayA/v2rayA/pull/2140 到达 Docker 内部环回的核心代理端口

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## What's Changed
* chore(deps): bump axios to 0.34.0 and set request headers in place by @Zakkaus in https://github.com/v2rayA/v2rayA/pull/2122
* ci: link the loong64 binaries statically against musl by @Zakkaus in https://github.com/v2rayA/v2rayA/pull/2125
* ci: install the Linux packages before uploading them by @Zakkaus in https://github.com/v2rayA/v2rayA/pull/2123
* ci: give development builds a package version dpkg and pacman accept by @Zakkaus in https://github.com/v2rayA/v2rayA/pull/2126
* build(docker): install the release's Alpine package in the image by @Zakkaus in https://github.com/v2rayA/v2rayA/pull/2124
* feat: add per-subscription update policies and recovery by @wywywywycloud in https://github.com/v2rayA/v2rayA/pull/2058
* fix: reach the core's proxy ports on loopback inside Docker by @Zakkaus in https://github.com/v2rayA/v2rayA/pull/2140
* feat(gui): add an Iran rule set to the RoutingA templates by @Zakkaus in https://github.com/v2rayA/v2rayA/pull/2142
* feat: sort nodes by latency and select the ones that failed the test by @Zakkaus in https://github.com/v2rayA/v2rayA/pull/2141
* feat: expose native proxy-group balancing strategies by @wywywywycloud in https://github.com/v2rayA/v2rayA/pull/2071
* feat(subscription): 为每个订阅增加节点解析 DNS by @nan0in in https://github.com/v2rayA/v2rayA/pull/2111
* feat: add global node check mode and custom target URL by @wywywywycloud in https://github.com/v2rayA/v2rayA/pull/2130

## New Contributors
* @nan0in made their first co
```
</details>

---
### 📦 [HyNetworks/hysteria](https://github.com/HyNetworks/hysteria)
`⭐ Stars: 22,981` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [app/v2.14.0](https://github.com/HyNetworks/hysteria/releases/tag/app/v2.14.0) (2026-11-15)`

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
### 📦 [Loyalsoldier/v2ray-rules-dat](https://github.com/Loyalsoldier/v2ray-rules-dat)
`⭐ Stars: 21,100` &nbsp;|&nbsp; `💻 语言: Other` &nbsp;|&nbsp; `🏷️ 最新版本: [202611222203](https://github.com/Loyalsoldier/v2ray-rules-dat/releases/tag/202611222203) (2026-11-22)`

> **简介**：🦄 🎃 👻 V2Ray 路由规则文件加强版，可代替 V2Ray 官方 geoip.dat 和 geosite.dat，适用于 V2Ray、Xray-core、mihomo(Clash-Meta)、hysteria、Trojan-Go 和 leaf。Enhanced edition of V2Ray rules dat files, applicable to V2Ray, Xray-core, mihomo(Clash-Meta), hysteria, Trojan-Go and leaf.

**💡 核心亮点更新 (中文)**：
该版本未提供详细更新说明。

---
### 📦 [Openwrt-Passwall/openwrt-passwall](https://github.com/Openwrt-Passwall/openwrt-passwall)
`⭐ Stars: 10,020` &nbsp;|&nbsp; `💻 语言: Lua` &nbsp;|&nbsp; `🏷️ 最新版本: [26.11.11-1](https://github.com/Openwrt-Passwall/openwrt-passwall/releases/tag/26.11.11-1) (2026-11-10)`

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

## <span id="-实用开源精选">📦 实用开源精选</span>

### 📦 [a3974892-cmd/wakeloom](https://github.com/a3974892-cmd/wakeloom)
`⭐ Stars: 62` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.21.5](https://github.com/a3974892-cmd/wakeloom/releases/tag/v1.21.5) (2026-11-09)`

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
`⭐ Stars: 41,599` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.6.1](https://github.com/storytold/craft-anything/releases/tag/v0.6.1) (2026-11-12)`

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
`⭐ Stars: 4,964` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.1.1](https://github.com/JustAResearcher/gpu-unlock-ada/releases/tag/v1.1.1) (2026-10-24)`

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
`⭐ Stars: 165` &nbsp;|&nbsp; `💻 语言: Shell` &nbsp;|&nbsp; `🏷️ 最新版本: [2026.11.22-21/50_arm_cortex-a9](https://github.com/kenzok8/compile-package/releases/tag/2026.11.22-21/50_arm_cortex-a9) (2026-11-22)`

> **简介**：small-package仓库，每日更新插件编译

**💡 核心亮点更新 (中文)**：
定时更新插件，推送发布 💤:

[下载链接] (https://dllkids.xyz/packages/arm_cortex-a9/)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
定时更新插件，推送发布 💤:

[下载链接] (https://dllkids.xyz/packages/arm_cortex-a9/)
```
</details>

---
### 📦 [jxxghp/MoviePilot](https://github.com/jxxghp/MoviePilot)
`⭐ Stars: 12,134` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.2.11](https://github.com/jxxghp/MoviePilot/releases/tag/v3.2.11) (2026-11-23)`

> **简介**：NAS媒体库自动化管理工具

**💡 核心亮点更新 (中文)**：
- **智能助手 / WebAgent 放开普通用户并绑定实时权限（后端 + 前端）**：
- 放开 WebAgent 与网页消息接口（`POST /api/v1/message/web`）给普通激活用户使用，取消默认的管理员上下文；智能助手按当前登录用户的实时权限（`discovery`、`search`、`subscribe`、`manage` 及各功能级 `features` 开关）校验白名单业务 API、工具与子代理调用，账号停用或权限调整后即时生效。
- 非管理员会话自动隐藏管理员工具、插件工具、后台 `Jobs` 任务与宿主机路径/命令信息，并在系统提示词中注入当前账号真实权限边界；禁止普通用户读写 `agent/jobs` 及修改 Agent 公共文件，同时放行只读读取本人会话上传的临时附件。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 本次更新内容

- **智能助手 / WebAgent 放开普通用户并绑定实时权限（后端 + 前端）**：
  - 放开 WebAgent 与网页消息接口（`POST /api/v1/message/web`）给普通激活用户使用，取消默认的管理员上下文；智能助手按当前登录用户的实时权限（`discovery`、`search`、`subscribe`、`manage` 及各功能级 `features` 开关）校验白名单业务 API、工具与子代理调用，账号停用或权限调整后即时生效。
  - 非管理员会话自动隐藏管理员工具、插件工具、后台 `Jobs` 任务与宿主机路径/命令信息，并在系统提示词中注入当前账号真实权限边界；禁止普通用户读写 `agent/jobs` 及修改 Agent 公共文件，同时放行只读读取本人会话上传的临时附件。
  - 前端智能助手面板仅对超级管理员加载并展示斜杠命令补全，避免普通用户输入 `/` 时触发管理员权限报错，并在切换账号或角色时自动清空缓存。
- **下载任务与下载历史按用户隔离（后端）**：
  - 具备搜索或订阅权限的普通网页用户可查看本人发起的正在下载任务与下载历史记录，并严格按当前登录用户隔离；管理员及具备「正在下载」管理权限的用户保持全局视图。
- **前端界面视觉与对比度优化（前端）**：
  - 优化运营卡片、媒体卡片、横向导航及浅色玻璃主题的自适应语义色板与主色对比度，提升亮暗主题下的一致性与可读性。
- **其他优化（后端）**：
  - 补齐接口错误提示多语言翻译，并完成 Fanart 图片语言记录辅助方法拆分与架构门禁对齐。

## 完整变更记录

- refactor(fanart): extract image language recording helper to satisfy complexity ratchet by @jxxghp ([e435fea](https://github.com/jxxghp/MoviePilot/commit/e435fea7abdbb06fcf7c994bac9982e478911094))
- feat(agent): enforce real-time per-user permissions for WebAgent and Web chat by @jxxghp ([cc0ebd9](https://github.com/jxxghp/MoviePilot/commit/cc0ebd9252c98037ac02f686ec8859bcd45d3f3e))
- fix(agent): align locale, evaluation harness, complexity, and dependency baseline by @jxxghp ([63e9ee7](https://github.com/jxxghp/MoviePilot/commit/63e9ee796f4a3297db8cbda08083ad2f404ad82c))
- chore(release): publish v3.2.11 by @jxxghp ([e13da2b](https://github.com/jxxghp/MoviePilot/commit/e13da2b8a873ae097fca7af897dc7ef17a179868))
- fix(architecture): satisfy concurrency, ruff, and architec
```
</details>

---
### 📦 [sandboxie-plus/Sandboxie](https://github.com/sandboxie-plus/Sandboxie)
`⭐ Stars: 20,058` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.19.1](https://github.com/sandboxie-plus/Sandboxie/releases/tag/v1.19.1) (2026-11-21)`

> **简介**：Sandboxie Plus 和 Classic

**💡 核心亮点更新 (中文)**：
![0 5 5](https://user-images.githubusercontent.com/3890945/105014988-575cb680-5a41-11eb-90d5-d942d28184b2.png)

发行说明

Sandboxie-Plus 1.19.1 在 SandMan 中引入了人工智能辅助故障排除。新的“使用 AI 代理进行故障排除”工具库

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
![0 5 5](https://user-images.githubusercontent.com/3890945/105014988-575cb680-5a41-11eb-90d5-d942d28184b2.png)

### Release Notes

Sandboxie-Plus 1.19.1 introduces AI-assisted troubleshooting in SandMan. The new “Troubleshoot with an AI Agent” toolbar button lets you connect an MCP-compatible AI client to investigate a sandbox issue. The feature is off by default and uses a local named pipe with a one-time pairing code. SandMan shows you the exact configuration changes or commands the agent proposes and asks for approval each time. You can review the session history and choose whether to submit an issue report with the agent’s findings and a log of the actions taken.

This release fixes two performance problems. Sandboxed applications that frequently look up localized strings or resources could suffer severe slowdowns, including frame rate drops in games. Those lookups now benefit from Windows’ cached language settings again. Sandboxie also removes a configuration locking bottleneck that forced concurrent process launches to wait on one another.

Sandbox border labels can now appear on any of the four window edges. A dedicated Box Border tab lets you choose the font, position and text orientation. The built-in INI editors gain optional line numbers and Ctrl+G navigation, and the new CustomProcessCommandLine setting lets you conditionally add, remove or replace arguments when launching a sandboxed process.

Version 1.19.1 also restores Windows 7 compatibility after a
```
</details>

---

## <span id="-系统与开发者工具">🛠️ 系统与开发者工具</span>

### 📦 [physicsdolphin/nv-uefi-unlocker](https://github.com/physicsdolphin/nv-uefi-unlocker)
`⭐ Stars: 2,871` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.1.11](https://github.com/physicsdolphin/nv-uefi-unlocker/releases/tag/v2.1.11) (2026-11-08)`

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
### 📦 [Atlas-OS/Atlas](https://github.com/Atlas-OS/Atlas)
`⭐ Stars: 22,177` &nbsp;|&nbsp; `💻 语言: PowerShell` &nbsp;|&nbsp; `🏷️ 最新版本: [0.6.1](https://github.com/Atlas-OS/Atlas/releases/tag/0.6.1) (2026-11-22)`

> **简介**：对 Windows 的开放式轻量级修改，旨在优化性能、隐私和可用性。

**💡 核心亮点更新 (中文)**：
- **Process Explorer。** Atlas 下载最新的 Microsoft 签名版本，因此更新的下载不再停止安装。
- **Atlas 安装。** 无法访问的 Windows 遥测日志文件夹不再停止安装。安装程序还处理较新的 Visual C++ Redistributable，并让 Windows 在需要时启动地图服务。
- **功能更新。** Atlas 在应用功能更新设置时可识别法语系统上的 Windows 11。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Download **AtlasManager.exe** to install Atlas 0.6.1, update an existing installation or create a Windows ISO.
This hotfix fixes several install and update failures reported after 0.6.0. Atlas still supports Windows 11 **25H2 and 26H2**.

## Updating from 0.6.0, 0.5.0 or 0.4.1

Back up your important files, open Atlas Manager and choose **Update to Atlas**.
Select **Keep my choices** to carry over your Atlas settings or **Choose again** to review them.
Atlas 0.4.0 and earlier need a fresh Windows installation. [Update guide](https://atlasos.net/docs/upgrade/upgrade/)

If Atlas Manager asks you to finish an earlier installation of 0.6.0, resume it with its 0.6.0 package before updating.

## Installing for the first time

Choose **Create an Atlas ISO**, then write it to a USB drive. [Installation guide](https://atlasos.net/docs/install/)

## Fixes

- **Process Explorer.** Atlas downloads the latest Microsoft-signed version, so an updated download no longer stops setup.
- **Atlas setup.** An inaccessible Windows telemetry log folder no longer stops installation. Setup also handles a newer Visual C++ Redistributable and lets Windows start the Maps service when it needs it.
- **Feature updates.** Atlas recognises Windows 11 on French systems when applying feature-update settings.
- **Microsoft Store.** Atlas gives stuck app updates a chance to clear and checks the Store again before starting repairs. Repair can use the newer App Installer already on the PC. If repair still fails,
```
</details>

---
### 📦 [Icalingua-plus-plus/Icalingua-plus-plus](https://github.com/Icalingua-plus-plus/Icalingua-plus-plus)
`⭐ Stars: 3,381` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.26.10](https://github.com/Icalingua-plus-plus/Icalingua-plus-plus/releases/tag/v2.26.10) (2026-11-15)`

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
`⭐ Stars: 13,337` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [v6.0.6](https://github.com/assimp/assimp/releases/tag/v6.0.6) (2026-11-09)`

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

## 🛑 建议清理 / 放弃维护项目

<details>
<summary>⚠️ 点击展开已放弃维护或超过 1 年停更的仓库清单 (140 个)</summary>

| 仓库名称 | Stars | 状态说明 | 操作建议 |
| :--- | :---: | :--- | :---: |
| [remotely-save/remotely-save](https://github.com/remotely-save/remotely-save) | 8,345 | 超过 742 天无代码提交 | [进入取消 Star](https://github.com/remotely-save/remotely-save) |
| [nexu-io/nexu](https://github.com/nexu-io/nexu) | 3,301 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/nexu-io/nexu) |
| [cityflow-project/CityFlow](https://github.com/cityflow-project/CityFlow) | 1,033 | 超过 460 天无代码提交 | [进入取消 Star](https://github.com/cityflow-project/CityFlow) |
| [facebookresearch/demucs](https://github.com/facebookresearch/demucs) | 10,423 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/facebookresearch/demucs) |
| [fufankeji/DeepSeek-OCR-Web](https://github.com/fufankeji/DeepSeek-OCR-Web) | 570 | 超过 391 天无代码提交 | [进入取消 Star](https://github.com/fufankeji/DeepSeek-OCR-Web) |
| [JimmyLv/awesome-nano-banana](https://github.com/JimmyLv/awesome-nano-banana) | 8,788 | 超过 440 天无代码提交 | [进入取消 Star](https://github.com/JimmyLv/awesome-nano-banana) |
| [btjawa/BiliTools](https://github.com/btjawa/BiliTools) | 4,981 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/btjawa/BiliTools) |
| [ehang-io/nps](https://github.com/ehang-io/nps) | 34,256 | 超过 907 天无代码提交 | [进入取消 Star](https://github.com/ehang-io/nps) |
| [ReturnFI/Blitz](https://github.com/ReturnFI/Blitz) | 1,086 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/ReturnFI/Blitz) |
| [kkangert/kspider](https://github.com/kkangert/kspider) | 1,260 | 超过 826 天无代码提交 | [进入取消 Star](https://github.com/kkangert/kspider) |
| [xenova/whisper-web](https://github.com/xenova/whisper-web) | 3,344 | 超过 782 天无代码提交 | [进入取消 Star](https://github.com/xenova/whisper-web) |
| [shadowsocks/luci-app-shadowsocks](https://github.com/shadowsocks/luci-app-shadowsocks) | 1,149 | 超过 1274 天无代码提交 | [进入取消 Star](https://github.com/shadowsocks/luci-app-shadowsocks) |
| [sinaptik-ai/pandas-ai](https://github.com/sinaptik-ai/pandas-ai) | 23,962 | 超过 390 天无代码提交 | [进入取消 Star](https://github.com/sinaptik-ai/pandas-ai) |
| [adithya-s-k/marker-api](https://github.com/adithya-s-k/marker-api) | 979 | 超过 768 天无代码提交 | [进入取消 Star](https://github.com/adithya-s-k/marker-api) |
| [yuchannslv5/warpflare](https://github.com/yuchannslv5/warpflare) | 334 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/yuchannslv5/warpflare) |
| [vvbbnn00/WARP-Clash-API](https://github.com/vvbbnn00/WARP-Clash-API) | 8,793 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/vvbbnn00/WARP-Clash-API) |
| [chika0801/hysteria-install](https://github.com/chika0801/hysteria-install) | 177 | 超过 871 天无代码提交 | [进入取消 Star](https://github.com/chika0801/hysteria-install) |
| [yeahwu/InstallOS](https://github.com/yeahwu/InstallOS) | 86 | 超过 1628 天无代码提交 | [进入取消 Star](https://github.com/yeahwu/InstallOS) |
| [bulianglin/psub](https://github.com/bulianglin/psub) | 1,757 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/bulianglin/psub) |
| [chatchat-space/Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat) | 38,712 | 超过 377 天无代码提交 | [进入取消 Star](https://github.com/chatchat-space/Langchain-Chatchat) |
| [lizongying/my-tv](https://github.com/lizongying/my-tv) | 31,942 | 超过 886 天无代码提交 | [进入取消 Star](https://github.com/lizongying/my-tv) |
| [joevess/IPTV](https://github.com/joevess/IPTV) | 10,271 | 超过 691 天无代码提交 | [进入取消 Star](https://github.com/joevess/IPTV) |
| [lecepin/WeChatVideoDownloader](https://github.com/lecepin/WeChatVideoDownloader) | 4,657 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/lecepin/WeChatVideoDownloader) |
| [hiroi-sora/Umi-OCR](https://github.com/hiroi-sora/Umi-OCR) | 48,884 | 超过 367 天无代码提交 | [进入取消 Star](https://github.com/hiroi-sora/Umi-OCR) |
| [linexjlin/GPTs](https://github.com/linexjlin/GPTs) | 32,018 | 超过 787 天无代码提交 | [进入取消 Star](https://github.com/linexjlin/GPTs) |
| [imDazui/Tvlist-awesome-m3u-m3u8](https://github.com/imDazui/Tvlist-awesome-m3u-m3u8) | 30,423 | 超过 373 天无代码提交 | [进入取消 Star](https://github.com/imDazui/Tvlist-awesome-m3u-m3u8) |
| [lxfater/Awesome-GPTs](https://github.com/lxfater/Awesome-GPTs) | 1,153 | 超过 1097 天无代码提交 | [进入取消 Star](https://github.com/lxfater/Awesome-GPTs) |
| [ClashDotNetFramework/experimental-clash](https://github.com/ClashDotNetFramework/experimental-clash) | 241 | 超过 1812 天无代码提交 | [进入取消 Star](https://github.com/ClashDotNetFramework/experimental-clash) |
| [zzzgydi/clash-verge](https://github.com/zzzgydi/clash-verge) | 21,835 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/zzzgydi/clash-verge) |
| [ddgth/cf2dns](https://github.com/ddgth/cf2dns) | 5,215 | 超过 686 天无代码提交 | [进入取消 Star](https://github.com/ddgth/cf2dns) |
| [zizifn/edgetunnel](https://github.com/zizifn/edgetunnel) | 9,348 | 超过 725 天无代码提交 | [进入取消 Star](https://github.com/zizifn/edgetunnel) |
| [missuo/Hysteria2](https://github.com/missuo/Hysteria2) | 204 | 超过 816 天无代码提交 | [进入取消 Star](https://github.com/missuo/Hysteria2) |
| [Misaka-blog/hysteria-install](https://github.com/Misaka-blog/hysteria-install) | 631 | 超过 948 天无代码提交 | [进入取消 Star](https://github.com/Misaka-blog/hysteria-install) |
| [MatsuriDayo/nekoray](https://github.com/MatsuriDayo/nekoray) | 15,222 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/MatsuriDayo/nekoray) |
| [FranzKafkaYu/x-ui](https://github.com/FranzKafkaYu/x-ui) | 8,422 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/FranzKafkaYu/x-ui) |
| [rwv/chinese-dos-games](https://github.com/rwv/chinese-dos-games) | 10,361 | 超过 837 天无代码提交 | [进入取消 Star](https://github.com/rwv/chinese-dos-games) |
| [getumbrel/llama-gpt](https://github.com/getumbrel/llama-gpt) | 10,922 | 超过 943 天无代码提交 | [进入取消 Star](https://github.com/getumbrel/llama-gpt) |
| [WangWenBin2017/OpenWrt-SSRPLUS](https://github.com/WangWenBin2017/OpenWrt-SSRPLUS) | 560 | 超过 630 天无代码提交 | [进入取消 Star](https://github.com/WangWenBin2017/OpenWrt-SSRPLUS) |
| [prompt-engineering/click-prompt](https://github.com/prompt-engineering/click-prompt) | 2,385 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/prompt-engineering/click-prompt) |
| [AutodeskAILab/Building-GAN](https://github.com/AutodeskAILab/Building-GAN) | 100 | 超过 1633 天无代码提交 | [进入取消 Star](https://github.com/AutodeskAILab/Building-GAN) |
| [novicezk/midjourney-proxy](https://github.com/novicezk/midjourney-proxy) | 5,378 | 超过 477 天无代码提交 | [进入取消 Star](https://github.com/novicezk/midjourney-proxy) |
| [adams549659584/go-proxy-bingai](https://github.com/adams549659584/go-proxy-bingai) | 8,385 | 超过 978 天无代码提交 | [进入取消 Star](https://github.com/adams549659584/go-proxy-bingai) |
| [tryptech/obs-zoom-and-follow](https://github.com/tryptech/obs-zoom-and-follow) | 440 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/tryptech/obs-zoom-and-follow) |
| [XingangPan/DragGAN](https://github.com/XingangPan/DragGAN) | 35,831 | 超过 918 天无代码提交 | [进入取消 Star](https://github.com/XingangPan/DragGAN) |
| [lewangdev/faster-whisper-youtube](https://github.com/lewangdev/faster-whisper-youtube) | 557 | 超过 1191 天无代码提交 | [进入取消 Star](https://github.com/lewangdev/faster-whisper-youtube) |
| [artidoro/qlora](https://github.com/artidoro/qlora) | 11,071 | 超过 895 天无代码提交 | [进入取消 Star](https://github.com/artidoro/qlora) |
| [langgenius/webapp-conversation](https://github.com/langgenius/webapp-conversation) | 1,097 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/langgenius/webapp-conversation) |
| [3andne/restls](https://github.com/3andne/restls) | 379 | 超过 1113 天无代码提交 | [进入取消 Star](https://github.com/3andne/restls) |
| [jtsang4/claude-to-chatgpt](https://github.com/jtsang4/claude-to-chatgpt) | 1,299 | 超过 827 天无代码提交 | [进入取消 Star](https://github.com/jtsang4/claude-to-chatgpt) |
| [yorunning/clash-conf](https://github.com/yorunning/clash-conf) | 104 | 超过 859 天无代码提交 | [进入取消 Star](https://github.com/yorunning/clash-conf) |
| [svc-develop-team/so-vits-svc](https://github.com/svc-develop-team/so-vits-svc) | 28,025 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/svc-develop-team/so-vits-svc) |
| [xiaye13579/BBLL](https://github.com/xiaye13579/BBLL) | 17,506 | 超过 633 天无代码提交 | [进入取消 Star](https://github.com/xiaye13579/BBLL) |
| [camenduru/MiniGPT-4-colab](https://github.com/camenduru/MiniGPT-4-colab) | 120 | 超过 1211 天无代码提交 | [进入取消 Star](https://github.com/camenduru/MiniGPT-4-colab) |
| [Vision-CAIR/MiniGPT-4](https://github.com/Vision-CAIR/MiniGPT-4) | 25,553 | 超过 811 天无代码提交 | [进入取消 Star](https://github.com/Vision-CAIR/MiniGPT-4) |
| [imfuxiao/Hamster](https://github.com/imfuxiao/Hamster) | 1,646 | 超过 559 天无代码提交 | [进入取消 Star](https://github.com/imfuxiao/Hamster) |
| [acheong08/ChatGPT](https://github.com/acheong08/ChatGPT) | 28,010 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/acheong08/ChatGPT) |
| [microsoft/JARVIS](https://github.com/microsoft/JARVIS) | 25,754 | 超过 481 天无代码提交 | [进入取消 Star](https://github.com/microsoft/JARVIS) |
| [choephix/auto-gpt-webui](https://github.com/choephix/auto-gpt-webui) | 116 | 超过 979 天无代码提交 | [进入取消 Star](https://github.com/choephix/auto-gpt-webui) |
| [facebookresearch/segment-anything](https://github.com/facebookresearch/segment-anything) | 55,174 | 超过 795 天无代码提交 | [进入取消 Star](https://github.com/facebookresearch/segment-anything) |
| [zai-org/ChatGLM-6B](https://github.com/zai-org/ChatGLM-6B) | 40,843 | 超过 879 天无代码提交 | [进入取消 Star](https://github.com/zai-org/ChatGLM-6B) |
| [ihciah/shadow-tls](https://github.com/ihciah/shadow-tls) | 2,681 | 超过 576 天无代码提交 | [进入取消 Star](https://github.com/ihciah/shadow-tls) |
| [jxbbb/ADAPT](https://github.com/jxbbb/ADAPT) | 421 | 超过 894 天无代码提交 | [进入取消 Star](https://github.com/jxbbb/ADAPT) |
| [mayooear/ai-pdf-chatbot-langchain](https://github.com/mayooear/ai-pdf-chatbot-langchain) | 16,578 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/mayooear/ai-pdf-chatbot-langchain) |
| [lencx/ChatGPT](https://github.com/lencx/ChatGPT) | 54,677 | 超过 815 天无代码提交 | [进入取消 Star](https://github.com/lencx/ChatGPT) |
| [nekohasekai/SagerNet](https://github.com/nekohasekai/SagerNet) | 56 | 超过 1778 天无代码提交 | [进入取消 Star](https://github.com/nekohasekai/SagerNet) |
| [P3TERX/Actions-OpenWrt](https://github.com/P3TERX/Actions-OpenWrt) | 7,604 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/P3TERX/Actions-OpenWrt) |
| [R86S/R86S-QuickInstaller](https://github.com/R86S/R86S-QuickInstaller) | 64 | 超过 1199 天无代码提交 | [进入取消 Star](https://github.com/R86S/R86S-QuickInstaller) |
| [WeNeedHome/SummaryOfLoanSuspension](https://github.com/WeNeedHome/SummaryOfLoanSuspension) | 20,313 | 超过 863 天无代码提交 | [进入取消 Star](https://github.com/WeNeedHome/SummaryOfLoanSuspension) |
| [zanzhz1101/LingMaxDNS](https://github.com/zanzhz1101/LingMaxDNS) | 23 | 超过 1594 天无代码提交 | [进入取消 Star](https://github.com/zanzhz1101/LingMaxDNS) |
| [IrineSistiana/mosdns-cn](https://github.com/IrineSistiana/mosdns-cn) | 324 | 超过 1635 天无代码提交 | [进入取消 Star](https://github.com/IrineSistiana/mosdns-cn) |
| [chika0801/Xray-install](https://github.com/chika0801/Xray-install) | 271 | 超过 1087 天无代码提交 | [进入取消 Star](https://github.com/chika0801/Xray-install) |
| [scutan90/DeepLearning-500-questions](https://github.com/scutan90/DeepLearning-500-questions) | 57,730 | 超过 879 天无代码提交 | [进入取消 Star](https://github.com/scutan90/DeepLearning-500-questions) |
| [Chikage0o0/Linux-NetSpeed](https://github.com/Chikage0o0/Linux-NetSpeed) | 3,733 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/Chikage0o0/Linux-NetSpeed) |
| [KFERMercer/OpenWrt-CI](https://github.com/KFERMercer/OpenWrt-CI) | 1,406 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/KFERMercer/OpenWrt-CI) |
| [qTox/qTox](https://github.com/qTox/qTox) | 4,970 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/qTox/qTox) |
| [quericy/one-key-ikev2-vpn](https://github.com/quericy/one-key-ikev2-vpn) | 2,105 | 超过 2198 天无代码提交 | [进入取消 Star](https://github.com/quericy/one-key-ikev2-vpn) |
| [riverscn/openwrt-iptvhelper](https://github.com/riverscn/openwrt-iptvhelper) | 371 | 超过 1914 天无代码提交 | [进入取消 Star](https://github.com/riverscn/openwrt-iptvhelper) |
| [frainzy1477/luci-app-clash](https://github.com/frainzy1477/luci-app-clash) | 1,621 | 超过 1704 天无代码提交 | [进入取消 Star](https://github.com/frainzy1477/luci-app-clash) |
| [Sanster/IOPaint](https://github.com/Sanster/IOPaint) | 23,283 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/Sanster/IOPaint) |
| [LANDrop/LANDrop](https://github.com/LANDrop/LANDrop) | 6,002 | 超过 831 天无代码提交 | [进入取消 Star](https://github.com/LANDrop/LANDrop) |
| [saveweb/review-2021](https://github.com/saveweb/review-2021) | 756 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/saveweb/review-2021) |
| [iranee/qnap-aliyunpan-webdav](https://github.com/iranee/qnap-aliyunpan-webdav) | 273 | 超过 1506 天无代码提交 | [进入取消 Star](https://github.com/iranee/qnap-aliyunpan-webdav) |
| [haoel/haoel.github.io](https://github.com/haoel/haoel.github.io) | 13,083 | 超过 1291 天无代码提交 | [进入取消 Star](https://github.com/haoel/haoel.github.io) |
| [tindy2013/stairspeedtest-reborn](https://github.com/tindy2013/stairspeedtest-reborn) | 3,820 | 超过 1263 天无代码提交 | [进入取消 Star](https://github.com/tindy2013/stairspeedtest-reborn) |
| [P3TERX/warp.sh](https://github.com/P3TERX/warp.sh) | 3,915 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/P3TERX/warp.sh) |
| [TheMRLL/WinXray](https://github.com/TheMRLL/WinXray) | 2,783 | 超过 1000 天无代码提交 | [进入取消 Star](https://github.com/TheMRLL/WinXray) |
| [Mikubill/cowtransfer-uploader](https://github.com/Mikubill/cowtransfer-uploader) | 447 | 超过 1747 天无代码提交 | [进入取消 Star](https://github.com/Mikubill/cowtransfer-uploader) |
| [281677160/build-actions](https://github.com/281677160/build-actions) | 388 | 超过 482 天无代码提交 | [进入取消 Star](https://github.com/281677160/build-actions) |
| [vaxilu/x-ui](https://github.com/vaxilu/x-ui) | 19,073 | 超过 825 天无代码提交 | [进入取消 Star](https://github.com/vaxilu/x-ui) |
| [xinntao/Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) | 37,617 | 超过 838 天无代码提交 | [进入取消 Star](https://github.com/xinntao/Real-ESRGAN) |
| [zu1k/proxypool](https://github.com/zu1k/proxypool) | 4,040 | 超过 1322 天无代码提交 | [进入取消 Star](https://github.com/zu1k/proxypool) |
| [TachibanaYoshino/AnimeGAN](https://github.com/TachibanaYoshino/AnimeGAN) | 4,610 | 超过 1572 天无代码提交 | [进入取消 Star](https://github.com/TachibanaYoshino/AnimeGAN) |
| [yuanzhoulvpi2017/tiny_python](https://github.com/yuanzhoulvpi2017/tiny_python) | 173 | 超过 1387 天无代码提交 | [进入取消 Star](https://github.com/yuanzhoulvpi2017/tiny_python) |
| [haiibo/OpenWrt](https://github.com/haiibo/OpenWrt) | 3,161 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/haiibo/OpenWrt) |
| [VergilGao/openwrt-packages](https://github.com/VergilGao/openwrt-packages) | 11 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/VergilGao/openwrt-packages) |
| [VergilGao/openwrt-compiler](https://github.com/VergilGao/openwrt-compiler) | 13 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/VergilGao/openwrt-compiler) |
| [OpenELEC/OpenELEC.tv](https://github.com/OpenELEC/OpenELEC.tv) | 1,620 | 超过 3368 天无代码提交 | [进入取消 Star](https://github.com/OpenELEC/OpenELEC.tv) |
| [github/copilot-docs](https://github.com/github/copilot-docs) | 23,151 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/github/copilot-docs) |
| [Kiougar/luci-wrtbwmon](https://github.com/Kiougar/luci-wrtbwmon) | 355 | 超过 1886 天无代码提交 | [进入取消 Star](https://github.com/Kiougar/luci-wrtbwmon) |
| [EtherDream/jsproxy](https://github.com/EtherDream/jsproxy) | 9,317 | 超过 966 天无代码提交 | [进入取消 Star](https://github.com/EtherDream/jsproxy) |
| [cheat-engine/cheat-engine](https://github.com/cheat-engine/cheat-engine) | 19,503 | 超过 583 天无代码提交 | [进入取消 Star](https://github.com/cheat-engine/cheat-engine) |
| [ffffffff0x/Dork-Admin](https://github.com/ffffffff0x/Dork-Admin) | 1,913 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/ffffffff0x/Dork-Admin) |
| [ffffffff0x/Digital-Privacy](https://github.com/ffffffff0x/Digital-Privacy) | 4,935 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/ffffffff0x/Digital-Privacy) |
| [Autodesk/civilconnection](https://github.com/Autodesk/civilconnection) | 122 | 超过 1452 天无代码提交 | [进入取消 Star](https://github.com/Autodesk/civilconnection) |
| [0xHJK/CleanApps](https://github.com/0xHJK/CleanApps) | 165 | 超过 1918 天无代码提交 | [进入取消 Star](https://github.com/0xHJK/CleanApps) |
| [KANIKIG/Multi-EasyGost](https://github.com/KANIKIG/Multi-EasyGost) | 1,942 | 超过 966 天无代码提交 | [进入取消 Star](https://github.com/KANIKIG/Multi-EasyGost) |
| [Kurokosama/AutoBuild-OpenWRT](https://github.com/Kurokosama/AutoBuild-OpenWRT) | 88 | 超过 1605 天无代码提交 | [进入取消 Star](https://github.com/Kurokosama/AutoBuild-OpenWRT) |
| [differentrain/DeletionTool](https://github.com/differentrain/DeletionTool) | 94 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/differentrain/DeletionTool) |
| [hideuvpn/android-google-play-store](https://github.com/hideuvpn/android-google-play-store) | 3,695 | 超过 1587 天无代码提交 | [进入取消 Star](https://github.com/hideuvpn/android-google-play-store) |
| [XJP-GIT/AntiZhaPian](https://github.com/XJP-GIT/AntiZhaPian) | 3,162 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/XJP-GIT/AntiZhaPian) |
| [jerrykuku/luci-app-ttnode](https://github.com/jerrykuku/luci-app-ttnode) | 89 | 超过 1763 天无代码提交 | [进入取消 Star](https://github.com/jerrykuku/luci-app-ttnode) |
| [KevinSHIT/NaiveSharp](https://github.com/KevinSHIT/NaiveSharp) | 97 | 超过 2208 天无代码提交 | [进入取消 Star](https://github.com/KevinSHIT/NaiveSharp) |
| [prasmussen/gdrive](https://github.com/prasmussen/gdrive) | 8,937 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/prasmussen/gdrive) |
| [tostercx/GTAO_Booster_PoC](https://github.com/tostercx/GTAO_Booster_PoC) | 2,861 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/tostercx/GTAO_Booster_PoC) |
| [ilxp/luci-app-ikoolproxy](https://github.com/ilxp/luci-app-ikoolproxy) | 502 | 超过 618 天无代码提交 | [进入取消 Star](https://github.com/ilxp/luci-app-ikoolproxy) |
| [kiddin9/luci-app-dnsfilter](https://github.com/kiddin9/luci-app-dnsfilter) | 124 | 超过 652 天无代码提交 | [进入取消 Star](https://github.com/kiddin9/luci-app-dnsfilter) |
| [h31105/deployX.sh](https://github.com/h31105/deployX.sh) | 416 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/h31105/deployX.sh) |
| [jerrykuku/openwrt-package](https://github.com/jerrykuku/openwrt-package) | 147 | 超过 1115 天无代码提交 | [进入取消 Star](https://github.com/jerrykuku/openwrt-package) |
| [frainzy1477/luci-app-trojan](https://github.com/frainzy1477/luci-app-trojan) | 120 | 超过 2022 天无代码提交 | [进入取消 Star](https://github.com/frainzy1477/luci-app-trojan) |
| [atrandys/xray](https://github.com/atrandys/xray) | 89 | 超过 1730 天无代码提交 | [进入取消 Star](https://github.com/atrandys/xray) |
| [v2board/v2board](https://github.com/v2board/v2board) | 5,064 | 超过 979 天无代码提交 | [进入取消 Star](https://github.com/v2board/v2board) |
| [ShadowsocksR-Live/iShadowsocksR](https://github.com/ShadowsocksR-Live/iShadowsocksR) | 601 | 超过 937 天无代码提交 | [进入取消 Star](https://github.com/ShadowsocksR-Live/iShadowsocksR) |
| [SuperNG6/Aria2-Trackers](https://github.com/SuperNG6/Aria2-Trackers) | 308 | 超过 2129 天无代码提交 | [进入取消 Star](https://github.com/SuperNG6/Aria2-Trackers) |
| [kakaruoterl/vless_install](https://github.com/kakaruoterl/vless_install) | 29 | 超过 2286 天无代码提交 | [进入取消 Star](https://github.com/kakaruoterl/vless_install) |
| [stupidloud/nanopi-openwrt](https://github.com/stupidloud/nanopi-openwrt) | 5,502 | 超过 950 天无代码提交 | [进入取消 Star](https://github.com/stupidloud/nanopi-openwrt) |
| [atrandys/trojan](https://github.com/atrandys/trojan) | 1,055 | 超过 1319 天无代码提交 | [进入取消 Star](https://github.com/atrandys/trojan) |
| [programthink/zhao](https://github.com/programthink/zhao) | 14,177 | 超过 1939 天无代码提交 | [进入取消 Star](https://github.com/programthink/zhao) |
| [RPRX/v2ray-vless](https://github.com/RPRX/v2ray-vless) | 390 | 超过 1365 天无代码提交 | [进入取消 Star](https://github.com/RPRX/v2ray-vless) |
| [h2y/Shadowrocket-ADBlock-Rules](https://github.com/h2y/Shadowrocket-ADBlock-Rules) | 16,739 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/h2y/Shadowrocket-ADBlock-Rules) |
| [p4gefau1t/trojan-go](https://github.com/p4gefau1t/trojan-go) | 8,385 | 超过 861 天无代码提交 | [进入取消 Star](https://github.com/p4gefau1t/trojan-go) |
| [Jrohy/trojan](https://github.com/Jrohy/trojan) | 5,622 | 超过 952 天无代码提交 | [进入取消 Star](https://github.com/Jrohy/trojan) |
| [mellow-io/mellow](https://github.com/mellow-io/mellow) | 3,535 | 超过 1443 天无代码提交 | [进入取消 Star](https://github.com/mellow-io/mellow) |
| [Dawneng/luci-theme-atmaterial](https://github.com/Dawneng/luci-theme-atmaterial) | 11 | 超过 1495 天无代码提交 | [进入取消 Star](https://github.com/Dawneng/luci-theme-atmaterial) |
| [trojan-gfw/igniter](https://github.com/trojan-gfw/igniter) | 3,274 | 超过 1092 天无代码提交 | [进入取消 Star](https://github.com/trojan-gfw/igniter) |
| [openwrt-develop/luci-theme-atmaterial](https://github.com/openwrt-develop/luci-theme-atmaterial) | 68 | 超过 2440 天无代码提交 | [进入取消 Star](https://github.com/openwrt-develop/luci-theme-atmaterial) |
| [trojan-gfw/trojan-quickstart](https://github.com/trojan-gfw/trojan-quickstart) | 244 | 超过 2041 天无代码提交 | [进入取消 Star](https://github.com/trojan-gfw/trojan-quickstart) |
| [FunctionClub/ZBench](https://github.com/FunctionClub/ZBench) | 1,172 | 超过 2072 天无代码提交 | [进入取消 Star](https://github.com/FunctionClub/ZBench) |
| [veekxt/v2ray-template](https://github.com/veekxt/v2ray-template) | 748 | 超过 2284 天无代码提交 | [进入取消 Star](https://github.com/veekxt/v2ray-template) |
| [HMBSbige/ShadowsocksR-Windows](https://github.com/HMBSbige/ShadowsocksR-Windows) | 6,891 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/HMBSbige/ShadowsocksR-Windows) |
| [trojan-gfw/trojan](https://github.com/trojan-gfw/trojan) | 19,747 | 超过 823 天无代码提交 | [进入取消 Star](https://github.com/trojan-gfw/trojan) |
</details>
