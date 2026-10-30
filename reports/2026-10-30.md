# 📡 Starred 项目雷达看板
> 🖥️ **交互式管理看板 (shadcn/ui)**：[👉 点击进入在线雷达看板 (https://stephenchou888.github.io/my-stars-digest/)](https://stephenchou888.github.io/my-stars-digest/)

> **生成时间**：`2026-10-30` ｜ **关注项目总数**：`374` ｜ **本期更新**：`81` ｜ **弃坑预警**：`136`

| 统计指标 | 数量 | 状态提示 |
| :--- | :---: | :--- |
| 🌟 总关注库 | **374** | [进入 shadcn 在线看板管理](https://stephenchou888.github.io/my-stars-digest/) |
| 🚀 近期有更新 | **81** | 涵盖 6 个分类 |
| 🛑 建议清理/弃坑 | **136** | 建议取消 Star 保持关注列表整洁 |

---
## 🧭 领域分类速览导航

- [🤖 AI 与智能体生态 (42)](#-AI-与智能体生态)
- [📦 实用开源精选 (6)](#-实用开源精选)
- [🎬 影音媒体与下载 (12)](#-影音媒体与下载)
- [📝 效率办公与创作 (8)](#-效率办公与创作)
- [🌐 网络与代理技术 (11)](#-网络与代理技术)
- [🛠️ 系统与开发者工具 (2)](#-系统与开发者工具)

---

## <span id="-AI-与智能体生态">🤖 AI 与智能体生态</span>

### 📦 [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)
`⭐ Stars: 14,492` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.3.0](https://github.com/akitaonrails/ai-memory/releases/tag/v3.3.0) (2026-10-30)`

> **简介**：用于代理编码 CLI 的长期记忆解决方案，并促进不同代理供应商之间的切换

**💡 核心亮点更新 (中文)**：
校验和 (SHA256)
````
efc5b8910cd5ad910b698a0ed6c07592342d6ca284c906ab187cf9b45888a029 ai-内存-3.3.0-1.aarch64.rpm
e1c912ab528839a4c7652a9199ecf2d26695482c9e0c8570bc8aff07209fd09f ai-memory-3.3.0-1.x86_64.rpm
56225762a682bd330c4e24406f2dbe0b1407

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Checksums (SHA256)
```
efc5b8910cd5ad910b698a0ed6c07592342d6ca284c906ab187cf9b45888a029  ai-memory-3.3.0-1.aarch64.rpm
e1c912ab528839a4c7652a9199ecf2d26695482c9e0c8570bc8aff07209fd09f  ai-memory-3.3.0-1.x86_64.rpm
56225762a682bd330c4e24406f2dbe0b140793e4ca5519581f627dd7effa2edc  ai-memory-claude-plugin.zip
84465e90e30cc1681a6cdb8fd562799214fc4c426b5dc8ef2b5ec1cdbd11ff4a  ai-memory-hooks.tar.gz
5b8b9030c247b091ac2bacbf181f52f8fdba9d4ed47cdef23faab874d4c94d9f  ai-memory-install-hooks
1d59924fe8d9ad0bd408b91e9e63de351d3b1beb7a427388cb81fdff991c2e2b  ai-memory-linux-aarch64.tar.gz
21855e931e010779b0dd15b9670cca5aa98fe1891eb312d96bfbb2227bfabf97  ai-memory-linux-x86_64.tar.gz
c583bb79691c97fb6df3feb775a9a4d677be1bd0b671208d41e0b03699c1e0b6  ai-memory-macos-aarch64.tar.gz
aaf601c42ed0d54ac3a6e9b63046c3cb69d78344930ff09ce9d829751185d255  ai-memory-macos-x86_64.tar.gz
5780c4c4873f765bcf5542a9cc16a77c720d56878947bb4232d7ed7aab110354  ai-memory-windows-x86_64.zip
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
`⭐ Stars: 50,961` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.7.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.7.0) (2026-10-28)`

> **简介**：DeepTutor：终身个性化辅导。 https://deeptutor.info/。

**💡 核心亮点更新 (中文)**：
- **完整应用程序：** 停止 DeepTutor 并备份运行时主目录，然后运行 ​​`python -m pip install --upgrade "deeptutor[full]==1.7.0"`。在使用相同的“DEEPTUTOR_HOME”重新启动之前运行“python -m pip check”和“deeptutor module list”。裸露的“deeptutor”现在仅选择核心。
- **旧版 CLI 软件包：** 首先运行 `python -m pip uninstall deeptutor-cli`，然后安装新的核心或完整配置文件。 （可选）重新安装 `deeptutor-cli==1.7.0` 作为兼容性别名。旧的 CLI 拥有共享的 Python 文件，因此在同一事务中升级它可以删除新核心所需的文件。包删除使运行时主目录数据保持不变。
- **源安装：**安装 `requirements/full.txt`，然后安装 `python -m pip install -e 。 --无部门`。使用“python scripts/install_extras.py <extra>”作为可选的源依赖项。源检查支持模块启用/禁用；软件包安装/卸载需要wheel环境。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# DeepTutor v1.7.0 Release Notes

**Release Date:** 2026.10.28

Building on [v1.6.15](past_releases/ver1-6-15.md), v1.7.0 brings modular installation, a refreshed learning workspace, block-based notebooks with Dito, and narrated video lessons. Full-app upgrades now use `deeptutor[full]`; existing runtime data remains separate from the installed packages.

## What's New

### Install the parts you use

`deeptutor` now provides core chat, CLI, and SDK; `deeptutor[full]` selects the Web app and standard feature modules. The `deeptutor-cli` package becomes a compatibility alias. Inspect installed, enabled, and ready states with `deeptutor module list`, then enable, disable, install, or remove modules while the app is stopped. Dependency checks protect required modules, and removal preserves user data.

### A workspace organized around learning

Modern and Classic layouts offer different navigation arrangements. Home brings together Chat, the Task Board, Learning notebook, and Calendar; Learning and Resources keep study activities and materials accessible. Customize Chat modes, controls, and starting prompts, or choose which learning methods appear on the New learning page. Conversation and resource navigation retain their workspace boundaries.

### Notebook pages with Dito beside them

The Learning notebook replaces the former Co-Writer editor with pages, subpages, and blocks. Import Word documents, insert source records from Favorites, discuss a passage with Dito, and review prop
```
</details>

---
### 📦 [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)
`⭐ Stars: 106,489` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.6.0](https://github.com/Panniantong/Agent-Reach/releases/tag/v1.6.0) (2026-10-23)`

> **简介**：让您的人工智能代理有一双能够看到整个互联网的眼睛。阅读和搜索 Twitter、Reddit、YouTube、GitHub、Bilibili、小红书 — 一个 CLI，零 API 费用。

**💡 核心亮点更新 (中文)**：
- 从旧版升级：把"帮我更新 Agent Reach"那句话发给你的 AI 就行。你的密钥和设置都保留，旧版程序会自动删掉。
- 加一个平台只要说一句，需要的软件都会自动装好，不需要管理员密码；你只需要登录或者填一个 Key。
- 小红书、推特这类要登录的平台，改用 Agent Reach 自己的专用浏览器，不弹窗、不占用你的浏览器；多个 AI 可以同时查。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
中文：

- 从旧版升级：把"帮我更新 Agent Reach"那句话发给你的 AI 就行。你的密钥和设置都保留，旧版程序会自动删掉。
- 加一个平台只要说一句，需要的软件都会自动装好，不需要管理员密码；你只需要登录或者填一个 Key。
- 小红书、推特这类要登录的平台，改用 Agent Reach 自己的专用浏览器，不弹窗、不占用你的浏览器；多个 AI 可以同时查。
- RSS 订阅和 Exa 全网搜索合并进了"网页"。以后有新版本，AI 会用大白话告诉你改了什么，你同意了才更新。

English:

- Upgrading from an older version: just send your AI the "update Agent Reach" sentence. Your keys and settings are kept, and the old program is removed for you.
- Adding a platform takes one sentence. Everything it needs is installed for you, with no admin password; you only log in or enter a key.
- Platforms that need a login, such as Xiaohongshu and X, now use Agent Reach's own browser in the background, never yours, and several AIs can search at once.
- RSS and Exa search are now part of "web". When a new version is out, your AI tells you in plain words what changed and updates only if you say yes.

1.6 is a rebuild. Agents call one command, `agent-reach`; everything Agent Reach installs or stores lives under `~/.agent-reach/`.
1.6 是重构版本：Agent 只调一个命令 `agent-reach`，Agent Reach 装的、存的东西全部在 `~/.agent-reach/` 下。

中文（技术细节）：
- 本版发布前已真实测通 28/40 个动作；以下未在发布机上测通，经维护者批准随本版发布：Reddit（测试网络被拦）、Instagram（限流）、B站字幕、LinkedIn、雪球热帖热股（未登录）、小宇宙（未配 Key）。
- 修复未登录 gh 阻断公开 API、公开行情触发浏览器、错误认证提示和未登记缓存清理；临时音频/字幕保存在 Reach 内。BOSS 站内搜索优先官方 OpenCLI，JD 上游适配故障单列；PR 与发版均检查真实验收和待验状态。
- CLI 对已声明的公开搜索/阅读先复用网页工具，成功后不准备浏览器；结果标注来源和内容范围，站内路径明确要求认证时才提示登录。可指定后端保留原有站内能力。
- 浏览器渠道共用一份登录，闲置十分钟自动关闭，下次使用自动打开。
- 添加渠道自动准备工具；删除时只清理该网站的登录。默认平台也能去掉，去掉后更新不会再加回来。
- 更新时，有已测版本的工具保持在
```
</details>

---
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
`⭐ Stars: 51,690` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.7.3](https://github.com/Ebony-Vinyl/dsh-our-free-model/releases/tag/v2.7.3) (2026-10-30)`

> **简介**：在 dsh 里装上这个插件即可，无需登录、注册或填 API Key，就能使用包括 DeepSeek V4.1 Flash、Kimi K3 在内的前沿模型——完全免费，不限量。 All you do is install this plugin in dsh: no login, no sign-up, no API key — the frontier models are just there, DeepSeek V4.1 Flash and Kimi K3 among them. Completely free, with no usage cap.

**💡 核心亮点更新 (中文)**：
- 官方 OpenCode 推理路径接入原生 Bun 传输，补全缺失的环境信息，并一次性迁移旧的哈希派生会话映射；同一会话继续稳定复用 ID。
- 针对已复现的真实 DSH 工具集拒绝，为 `subagent_fork`、`working_directory` 使用可逆出站别名。工具描述、参数及宿主实际执行能力保留；响应恢复原名，别名碰撞会自动避让。
- 修复 Chat 历史消息同时带有 `content: []` 和 `tool_calls` 时漏改工具名的问题。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# v2.7.3 插件发布

本次发布 DSH 插件，基于当前主线并包含 #709 的真实工具集兼容修复。桌面应用版本及官方桌面安装包保持原状。

## 免费车道兼容

- 官方 OpenCode 推理路径接入原生 Bun 传输，补全缺失的环境信息，并一次性迁移旧的哈希派生会话映射；同一会话继续稳定复用 ID。
- 针对已复现的真实 DSH 工具集拒绝，为 `subagent_fork`、`working_directory` 使用可逆出站别名。工具描述、参数及宿主实际执行能力保留；响应恢复原名，别名碰撞会自动避让。
- 修复 Chat 历史消息同时带有 `content: []` 和 `tool_calls` 时漏改工具名的问题。
- 取消 HTTP/HTTPS/SOCKS5 代理握手或关闭中继时立即清理出口连接，避免继续等待独立握手超时。

## 账号渠道与连接稳定性

- EAC router 对各渠道可明确识别的排队响应提供同渠道、同模型的账号轮换，保留已启用账号、余额及模型限制策略。
- 修复排队与额度换号后的实际账号归属、认证续期预算，以及 OpenCode 匿名槽与账号槽的轮换；已经向下游输出后不重放请求。
- 客户端断开或取消时及时关闭上游响应并释放并发槽，减少残留连接及无效占用。

## 安全升级与维护

- 宿主无法安全热重载时，验证并安装新版本后明确提示重启生效；待重启期间阻止再次安装，保留回滚备份。
- 识别由包管理器管理的安装，继续通过宿主的安装与更新流程维护程序。
- 渠道包构建增加功能标记检查，避免重新构建时退回旧能力。
- 中英文 README 同步交流群12、群号 `1130235133` 及新二维码。

## 安装前提

**默认 OpenCode 免费推理需要自行安装原生 Bun。插件不会自动下载或安装 Bun。** 可以用 `OUR_FREE_MODEL_BUN` 指定可执行文件；查找路径和传输设置见 [免费车道传输说明](https://github.com/Ebony-Vinyl/dsh-our-free-model/blob/v2.7.3/docs/oc-free-transport.md)。

`OUR_FREE_MODEL_FREE_TRANSPORT=node` 可切回此前的 Node 传输用于诊断，但不保证上游接受。上述兼容修复不解除真实额度、地区或账号限制，也不承诺所有 429 均可恢复。

自行安装的旧版用户可在插件升级页检查更新；宿主管理的安装请通过原安装方式更新可信 tarball。手工安装使用本次完整插件包，保留原有用户数据目录，不要仅替换入口文件。

## 回退

升级器继续执行原有签名、文件大小、SHA-256、备份与回滚校验。手工回退使用上一版可信插件包，并保留配置、账号及统计数据。


## 本次发布验证

- 完整 `npm test` 108/108 套件通过，包含生产签名发布检查、原版 1.3.1 与 2.5.9 升级回归；根目录及独立端类型检查、生成产物一致性检查通过。
- 发布 PR 四项 CI 全部通过，合并后的 main 检查与签名工作流通过。
- tarball 从固定提交的 LF 字节构建，全部 80 个运行时文件逐字节匹配正式签名清单，解包后入口加载通过。
- 使用原版 2.5.9 升级器从公开固定提交地址完成下载、生产验签和安装，80 个运行时文件摘要一致，测试用户数据保留；新入口在全新进程中加载成功。此项不代表真实 DSH 宿主中的热重载已验收。
-
```
</details>

---
### 📦 [hypit-ai/hypit](https://github.com/hypit-ai/hypit)
`⭐ Stars: 26,672` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.3.1](https://github.com/hypit-ai/hypit/releases/tag/v0.3.1) (2026-10-09)`

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
`⭐ Stars: 19,937` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.0.8](https://github.com/HBAI-Ltd/Toonflow-app/releases/tag/v2.0.8) (2026-10-27)`

> **简介**：短剧、漫剧制作工具 Toonflow：开源 AI 视频创作平台，集成剧本创作、智能分镜、角色与场景资产管理、图像生成和视频生成。融合无限画布、AI Agent 与可视化工作流，支持本地部署、自选模型、跨平台客户端、MCP 与插件扩展。Open-source AI short drama and motion comic creation tool with an infinite canvas, AI agents, storyboarding, image and video generation. Self-hosted and extensible, with a canvas-based approach similar to LibTV and TapNow.

**💡 核心亮点更新 (中文)**：
* fix(agent): 未打开画布时允许空 canvas.id by  in https://github.com/HBAI-Ltd/Toonflow-app/pull/358

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 📦 下载指南

选择你的设备对应的安装包，点击即可下载：

| 你的设备 | 下载 |
| --- | --- |
| 💻 Windows（64 位） | [⬇️ 下载 Windows 安装包](https://github.com/HBAI-Ltd/Toonflow-app/releases/download/v2.0.8/toonflow-2.0.8-Setup.exe) |
| 🍎 Mac（M 系列芯片） | [⬇️ 下载 M 系列 Mac 安装包](https://github.com/HBAI-Ltd/Toonflow-app/releases/download/v2.0.8/macos-arm64-toonflow.dmg) |
| 🍎 Mac（Intel 芯片） | [⬇️ 下载 Intel Mac 安装包](https://github.com/HBAI-Ltd/Toonflow-app/releases/download/v2.0.8/stable-macos-x64-toonflow.dmg) |
| 📱 Android（ARM64，Android 8 及以上） | [⬇️ 下载 Android APK](https://github.com/HBAI-Ltd/Toonflow-app/releases/download/v2.0.8/toonflow-2.0.8-android-arm64.apk) |

> 💡 手动安装请选择上表中的链接。下方其他文件供软件自动更新使用。

## 🚀 安装说明

- 💻 **Windows**：双击下载的安装包，按提示完成安装。
- 🍎 **Mac**：打开下载的安装包，将 `toonflow.app` 拖入“应用程序”，再从“应用程序”打开。
- 📱 **Android**：在手机上打开 APK，按系统提示允许此来源安装应用。后续版本可直接覆盖安装。

M 系列 Mac 安装包已完成 Developer ID 签名与 Apple 公证。首次打开时，macOS 仍可能提示确认打开从互联网下载的应用。

---


## What's Changed
* fix(agent): 未打开画布时允许空 canvas.id by @Delusion-Create in https://github.com/HBAI-Ltd/Toonflow-app/pull/358

## New Contributors
* @Delusion-Create made their first contribution in https://github.com/HBAI-Ltd/Toonflow-app/pull/358

**Full Changelog**: https://github.com/HBAI-Ltd/Toonflow-app/compare/v2.0.7...v2.0.8
```
</details>

---
### 📦 [morluto/rea](https://github.com/morluto/rea)
`⭐ Stars: 409,462` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [rea-agents-6.8.0](https://github.com/morluto/rea/releases/tag/rea-agents-6.8.0) (2026-10-25)`

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
`⭐ Stars: 16,744` &nbsp;|&nbsp; `💻 语言: Vue` &nbsp;|&nbsp; `🏷️ 最新版本: [v4.0.9](https://github.com/chatfire-AI/huobao-drama/releases/tag/v4.0.9) (2026-10-25)`

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
`⭐ Stars: 25,794` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.1.2181](https://github.com/yetone/magpie/releases/tag/v0.1.2181) (2026-10-30)`

> **简介**：每个代理的模型。一处。来自菜单栏的 DeepSeek 上的 Codex、Kimi 上的 Claude Code。

**💡 核心亮点更新 (中文)**：
- 插件安装现在要求在使用相同包替换现有插件之前进行确认。
- 插件托盘面板中的 **更多** 按钮现在可打开“发现”页面。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Features
- Plugin installation now asks for confirmation before replacing an existing plugin with the same package.
- The **More** button in the Plugins tray panel now opens the Discover page.

## Bug Fixes
- Fixed plugin cards showing **Installed** for the wrong repository.
- Fixed a repository’s package name hiding the actual npm package name.
- Fixed the automatic update status so it no longer says it is checking while downloading.
- Fixed image configuration requests going to the wrong Gemini API endpoint and not reaching all Gemini services.
- Fixed a `.git` folder being treated as a repository unless Git actually recognizes it.
- Fixed Discover so gateway-only repositories are listed as request hooks, and fixed their labels.

## Improvements
- Improved error reporting for failed plugin and settings operations.
- Improved Claude Code proxy communication: writes now wait for proxy confirmation, and unnecessary checks on Claude Code’s own endpoint were removed.

### Install

Download from [usemagpie.ai](https://usemagpie.ai), or `curl -fsSL https://usemagpie.ai/install.sh | sh`. An installed magpie updates itself.

- **macOS (Apple Silicon):** `magpie-darwin-arm64.dmg`
- **macOS (Intel):** `magpie-darwin-amd64.dmg`
- **Windows:** `magpie-windows-amd64.exe` (ARM: `magpie-windows-arm64.exe`)
- **Linux:** `magpie-linux-amd64` / `magpie-linux-arm64` (needs GTK 3 and WebKitGTK 4.1)
- **Terminal only:** `magpie-cli-<os>-<arch>`

<!-- lang:zh -->

## 功能
- 现在，插件安装在用相同包替换现有插件之前会
```
</details>

---
### 📦 [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
`⭐ Stars: 258,629` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.22.5](https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.5) (2026-10-23)`

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
`⭐ Stars: 11,340` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.12.115](https://github.com/genspark-ai/genoffice/releases/tag/v0.12.115) (2026-10-26)`

> **简介**：免费的开源 AI Office 套件：带有内置 AI 代理的文档、表格、幻灯片、PDF、Markdown 和 HTML 编辑器，以及“genoffice”CLI 和代理技能，以便 Claude Code、Codex 和 Cursor 可以在本地创建和编辑真正的 .docx/.xlsx/.pptx 文件。带上你自己的钥匙。 macOS、Windows 和 Linux。

**💡 核心亮点更新 (中文)**：
- **文档：** 邮件选项卡将本地数据源合并到信件、信封和标签中，由 要求；将两个文档比较为跟踪更改红线和读/写块级内容控件；接受或拒绝对插入文本或段落标记的格式更改不再留下残留物（由 报告）；粘贴的 Zotero 引文保留其字段代码并且从不锁定段落（由 报告）；内联方程不再继承首行缩进，由 报告；文本框和形状编辑器内的项目符号、编号和缩进、折叠轮廓手柄、在保存过程中保持其位置的浮动图片以及在文档中保留的标题，没有标题样式；合并跨页面的组将其行保持在内容高度；标题标签在 SEQ 匹配器中转义；切换到替换时焦点保留在查找字段中。
- **工作表：**加密工作簿打开、保存和更改密码；据报道，从主页画廊重新设计现有表格不再与其重叠；上标和下标实际上升高和降低了文本，由 报告；从模型中隐藏单元格并使它们远离跟踪工具；枢轴总结中的 stdDev/var 系列，注释中的图片； .xls 公式列返回到正确的位置； Univer 所缺乏的 Excel 选择和编辑和弦（Shift+Home、Ctrl+Shift+*、Ctrl+2/3/4、Ctrl+Shift+Enter、Ctrl+'、Alt+↓、Ctrl+Backspace 等）；数字在变成 #### 之前会溢出到单元格边缘，列默认边框会阻止样式单元格的渗漏，并缩小合并范围的预算。
- **幻灯片：** A4/A3 纸张尺寸、纵向和自定义幻灯片尺寸，询问者；幻灯片母版的编辑功能区，要求；报道称，中途终止的保存会使前一副牌完好无损。图表数据表绘制在水平条形图下；表格样式的十六进制颜色在验证之前被修剪。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
GenOffice v0.12.115 stable desktop installers.

## What's New

- **Docs:** a Mailings tab merges a local data source into letters, envelopes and labels (@tokg-venv, asked by @hou0); compare two documents into a tracked-changes redline and read/write block-level content controls (@tokg-venv); accepting or rejecting a formatting change on inserted text or a paragraph mark no longer leaves residue (reported by @ZLGBoss); a pasted Zotero citation keeps its field code and never locks the paragraph (reported by @Keeptg); inline equations no longer inherit the first-line indent (@widechaos, reported by @Keeptg); bullets, numbering and indent inside textbox and shape editors, folding outline handles, floating pictures that keep their position across a save and a heading that survives in a document without heading styles (@tokg-venv); a merged group crossing a page keeps its rows at content height (@tokg-venv); caption labels are escaped in the SEQ matcher (@aniruddhaadak80); focus stays in the find field when switching to Replace.
- **Sheets:** encrypted workbooks open, save and change their password (@barathrajd); restyling an existing table from the Home gallery no longer overlaps it (@widechaos, reported by @putude); superscript and subscript actually raise and lower the text (@tokg-venv, reported by @putude); hide cells from the model and keep them out of the trace tools (@tokg-venv); stdDev/var family in pivot Summarize By, pictures in notes (@tokg-venv); .xls formula columns co
```
</details>

---
### 📦 [ruvnet/RuView](https://github.com/ruvnet/RuView)
`⭐ Stars: 101,655` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [ruview-harness-v0.9.2](https://github.com/ruvnet/RuView/releases/tag/ruview-harness-v0.9.2) (2026-10-12)`

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
`⭐ Stars: 25,225` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [@pascal-app/cli@1.0.6](https://github.com/pascalorg/editor/releases/tag/%40pascal-app/cli%401.0.6) (2026-10-23)`

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
`⭐ Stars: 30,524` &nbsp;|&nbsp; `💻 语言: Kotlin` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.0.4](https://github.com/librepods-org/librepods/releases/tag/v1.0.4) (2026-10-16)`

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
`⭐ Stars: 39,869` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.13.0](https://github.com/linshenkx/prompt-optimizer/releases/tag/v2.13.0) (2026-10-28)`

> **简介**：人工智能提示优化器，用于编写更好的提示并获得更好的人工智能结果。

**💡 核心亮点更新 (中文)**：
- **就地交互式输出：** 使用预览或源来检查结果。显式 HTML 代码块和支持的 HTML 内容与周围的 Markdown 一起呈现为独立的网页。多个块可以同时保持交互。
- **交互式扩展预览：**修复测试版的扩展脚本限制，以便生成的按钮、表单和画布可以在结果内工作，而无需打开另一个选项卡。
- **有界流和渲染：**生成使用专用输出文档、虚拟化源视图和后台 Markdown 解析。过大或昂贵的内容会回溯到源。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## English

### Summary

This stable release brings interactive HTML inside Markdown results to Web, Desktop and the browser extension, with a redesigned output pipeline for concurrent generation and large responses. It also improves backup integrity, adds import codes for selected cloud backups, preserves model selections and saved parameters, and refines image-editing and structured-input templates.

### Highlights

- **Interactive output in place:** use Preview or Source to inspect results. Explicit HTML code blocks and supported HTML content render as isolated web pages alongside the surrounding Markdown. Multiple blocks can remain interactive at the same time.
- **Interactive extension previews:** fix the beta's extension script restriction so generated buttons, forms and canvases work inside results without opening another tab.
- **Bounded streaming and rendering:** generation uses a dedicated output document, virtualized source views and background Markdown parsing. Oversized or expensive content falls back to source.
- **More reliable backups:** validate data and image resources before restoration, protect existing images from eviction, and restore workspace snapshots only after preceding import steps succeed.
- **Cloud backup import codes:** transfer a selected WebDAV, S3-compatible or Cloudflare R2 snapshot using a code, link or QR code when its size permits.

### Product Updates

#### Desktop

- Propagate cancellation from the interface through desktop IPC to model
```
</details>

---
### 📦 [RSSNext/Folo](https://github.com/RSSNext/Folo)
`⭐ Stars: 39,196` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [desktop/v1.16.0](https://github.com/RSSNext/Folo/releases/tag/desktop/v1.16.0) (2026-10-16)`

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
`⭐ Stars: 51,434` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [0.31.3](https://github.com/roboflow/supervision/releases/tag/0.31.3) (2026-10-28)`

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
`⭐ Stars: 35,349` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.19.33](https://github.com/MetaCubeX/mihomo/releases/tag/v1.19.33) (2026-10-21)`

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
`⭐ Stars: 36,496` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.3.0](https://github.com/microsoft/graphrag/releases/tag/v3.3.0) (2026-10-08)`

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
`⭐ Stars: 155,021` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.5.8](https://github.com/clash-verge-rev/clash-verge-rev/releases/tag/v2.5.8) (2026-10-09)`

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
`⭐ Stars: 78,781` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.1.912-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.912-beta) (2026-10-28)`

> **简介**：用于运行和训练法学硕士和扩散模型的本地 UI。支持 GGUF、MLX、Qwen3.8、DeepSeek-V4.1、MiniMax-H3、Gemma 4、FLUX 等。

**💡 核心亮点更新 (中文)**：
- **Trick or treat**：🎃 新万圣节主题 - 截止 11 月 1 日
- **更快的 Unsloth**：首次启动速度提高 2 倍，工具调用、模型列表、数据集准备和 MiniMax-H3 加载速度也加快
- **多 LoRA 批处理**：最多 4 个兼容的排队微调作业一起训练

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Halloween 👻 is here. Through October, a **Trick or treat** row in the sidebar opens eleven Halloween themes, spooky greetings and a few spiders and bats.

This release also speeds up the first launch, Linux tool calls and model loading, and trains compatible fine-tuning jobs together with multi-LoRA.

<p align="center">
<img width="500" alt="Unsloth app" src="https://github.com/user-attachments/assets/36f5a627-e30c-461a-bf55-508aa3f30fb4" />
</p>



## Highlights

- **Trick or treat**: 🎃 new Halloween themes - until Nov 1
- **Faster Unsloth**: 2x faster first launch, plus speedups for tool calls, model lists, dataset prep and MiniMax-H3 loads
- **Multi-LoRA batching**: up to 4 compatible queued fine-tuning jobs train together
- **SGLang thinking + auto-compact**: Resume and JSON output now work on vLLM and SGLang too
- **Browser use switch**: let models control the built-in browser from its new tab page

## Optimizations

- Setup now precompiles Python files, so the first launch is about 2x faster.
- On Linux, tool calls start in 1 to 2 ms instead of 84 to 174 ms with a 2 GB server process.
- With 497 cached models, the model list uses about a third of the CPU time it did.
- Preparing a 1,000-row chat dataset for Gemma 3 4B took 1.75 s instead of 6.6 s in our test.
- MiniMax-H3 loaded in 49 s instead of 61 s on a Linux A100.

## Multi-LoRA + API

When several compatible jobs wait in the fine-tuning queue, Unsloth now trains them together, each with
```
</details>

---
### 📦 [arc53/DocsGPT](https://github.com/arc53/DocsGPT)
`⭐ Stars: 18,350` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [1.1.0](https://github.com/arc53/DocsGPT/releases/tag/1.1.0) (2026-10-25)`

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
`⭐ Stars: 83,600` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.2.21](https://github.com/lobehub/lobehub/releases/tag/v2.2.21) (2026-10-29)`

> **简介**：🤯 LobeHub 是您的首席代理运营商，通过招聘、调度和报告整个 AI 团队，将您的代理组织为 7×24 小时运营。

**💡 核心亮点更新 (中文)**：
- **项目作为工作区** — 在项目内运行对话和任务，包括项目主编辑器、成员和库设置、可交换的主代理、按代理分组并按状态和设备过滤的主题、拖放重新排序项目以及在项目内分组的频道。 （#21370、#21345、#21344、#21483、#21382、#21398、#21490、#21752）
- **多代理通道** — 代理在通道中协作，每个通道继承其代理的设备和目录，并且重新设计的通道设置保留每个通道的回复样式和表情符号。 （＃21545，＃21782，＃21658，＃21757）
- **机器人唤醒** — 机器人根据自己的职责决定何时回复，可以首先确认并在线程中回答，在编辑时唤醒它们，不参与多方线程，并且选择不回复会呈现为自己的状态。可在 Discord、Slack 和飞书/Lark 上使用。 （＃21585，＃21726，＃21719，＃21756，＃21728，＃21727，＃21825）

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 📦 Release v2.2.21

This release was automatically published from PR #21872.

### Changes
See PR description: https://github.com/lobehub/lobehub/pull/21872

### Commit Message
# 🚀 LobeHub Release (20261029)

**Release Date:** October 29, 2026  
**Since v2.2.20:** 616 merged PRs · 16 contributors

> Projects become the place where work happens — conversations, channels, tasks and acceptance live inside them — while bots learn when to speak up, goals gain a full review loop, and Resources become Docs.

---

## ✨ Highlights

- **Projects as workspaces** — Run conversations and tasks inside a project, with a project home composer, members and libraries settings, a swappable main agent, topics grouped by agent and filtered by status and device, drag-to-reorder projects, and channels grouped inside projects. (#21370, #21345, #21344, #21483, #21382, #21398, #21490, #21752)
- **Multi-agent channels** — Agents collaborate in channels, each channel inherits its Agent's device and directory, and the redesigned channel settings keep reply style and emoji per channel. (#21545, #21782, #21658, #21757)
- **Bot wake** — Bots decide when to reply based on their duties, can acknowledge first and answer in a thread, wake on edits that @-mention them, stay out of multi-party threads, and the choice not to reply renders as its own state. Available on Discord, Slack and Feishu / Lark. (#21585, #21726, #21719, #21756, #21728, #21727, #21825)
- **Goals workspace** — A cross-agent goals page, decis
```
</details>

---
### 📦 [Dooy/chatgpt-web-midjourney-proxy](https://github.com/Dooy/chatgpt-web-midjourney-proxy)
`⭐ Stars: 6,804` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.26.8](https://github.com/Dooy/chatgpt-web-midjourney-proxy/releases/tag/v2.26.8) (2026-09-29)`

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
`⭐ Stars: 29,947` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v4.17.2](https://github.com/labring/FastGPT/releases/tag/v4.17.2) (2026-10-09)`

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
`⭐ Stars: 9,913` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.3.2](https://github.com/yihong0618/bilingual_book_maker/releases/tag/v1.3.2) (2026-10-30)`

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
`⭐ Stars: 37,314` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.4.1](https://github.com/1Panel-dev/1Panel/releases/tag/v2.4.1) (2026-10-22)`

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
### 📦 [The-Vibe-Company/quivr](https://github.com/The-Vibe-Company/quivr)
`⭐ Stars: 39,618` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.0.0](https://github.com/The-Vibe-Company/quivr/releases/tag/v2.0.0) (2026-10-29)`

> **简介**：一个开源引擎，可将连续的内容流转化为搜索和监控。持久摄取、混合搜索、警报以及格式、模型和业务规则的插件。

**💡 核心亮点更新 (中文)**：
* **docs-site:** 将 PostHog 分析添加到文档站点 ([#3954](https://github.com/The-Vibe-Company/quivr/issues/3954)) ([1f72133](https://github.com/The-Vibe-Company/quivr/commit/1f72133e27e1cc0a7a05fb35a93df0f9e33136c4))

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Quivr 2.0.0

Quivr is an open-source engine for content that keeps arriving. Your application, or Quivr's sources (RSS, Microsoft 365 mailboxes, X lists), send it documents. Quivr keeps every version of each document and makes it searchable within seconds, by keywords, by meaning, or both. It also checks every new document against your saved alerts. Quivr has no user interface: your application talks to it over an HTTP API, and AI agents use it through `quivr mcp`.

2.0.0 is the first stable release of the rewritten Quivr. The alphas were for evaluation. From this release on, Quivr makes promises you can build on.

### What 2.0 promises

- **A stable API.** The HTTP API keeps the `/v0` path for every 2.x release. A 2.x release only adds to it: new endpoints, optional fields, response fields and enum values. A change that could break a working client waits for the next major release.
- **Upgrades that keep your data.** An upgrade from one 2.x release to another runs `quivr migrate`, then rolls the worker and the API, with your data in place.
- **Plugins that check their compatibility.** A plugin declares the Plugin API versions it supports, and Quivr refuses to activate one it cannot run.
- **Clear status for each feature.** Everything in the documentation is stable within 2.x except a short list of experimental features, each marked on its page: search measurement tooling, Jev re-ranking and Jev-judged alerts, the dedicated vector host, and the `quivr-autoscaler` binary.
```
</details>

---
### 📦 [langgenius/dify](https://github.com/langgenius/dify)
`⭐ Stars: 159,968` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [1.18.0](https://github.com/langgenius/dify/releases/tag/1.18.0) (2026-10-23)`

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
`⭐ Stars: 25,024` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.6.45](https://github.com/nextai-translator/nextai-translator/releases/tag/v0.6.45) (2026-10-24)`

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
`⭐ Stars: 148,702` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [langchain-core==1.7.3](https://github.com/langchain-ai/langchain/releases/tag/langchain-core%3D%3D1.7.3) (2026-10-29)`

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
`⭐ Stars: 187,826` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [autogpt-platform-beta-v0.10.0](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.10.0) (2026-10-27)`

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
`⭐ Stars: 8,887` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v4.5.1](https://github.com/rockbenben/ChatGPT-Shortcut/releases/tag/v4.5.1) (2026-10-09)`

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
`⭐ Stars: 2,842` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [userscript-v2.38.1](https://github.com/pionxzh/chatgpt-exporter/releases/tag/userscript-v2.38.1) (2026-10-30)`

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
`⭐ Stars: 47,686` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [2.2.2](https://github.com/zhayujie/CowAgent/releases/tag/2.2.2) (2026-10-30)`

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
`⭐ Stars: 22,239` &nbsp;|&nbsp; `💻 语言: Shell` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.5.32](https://github.com/mack-a/v2ray-agent/releases/tag/v3.5.32) (2026-10-29)`

> **简介**：Xray、Tuic、hysteria2、sing-box 八合一一键脚本

**💡 核心亮点更新 (中文)**：
feat(脚本): 修复xray-core 正式版回退版本问题

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
feat(脚本): 修复xray-core 正式版回退版本问题
```
</details>

---
### 📦 [electerm/electerm](https://github.com/electerm/electerm)
`⭐ Stars: 15,505` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v5.8.0](https://github.com/electerm/electerm/releases/tag/v5.8.0) (2026-10-30)`

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
`⭐ Stars: 42,468` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v26.10.29](https://github.com/XTLS/Xray-core/releases/tag/v26.10.29) (2026-10-29)`

> **简介**：X射线，穿透一切。也是最好的 v2ray 核心。魔法发生的地方。适合多种用途的开放平台。

**💡 核心亮点更新 (中文)**：
- **TRX(Tron)/USDT/USDC: `TNrDh5VSfwd4RPrwsohr6poyNTfFefNYan`**
- **TON：`UQApeV-u2gm43aC1uP76xAC1m6vCylstaN1gpfBmre_5IyTH`**
- **BTC：`1JpqcziZZuqv3QQJhZGNGBVdCBrGgkL6cT`**

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
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
- **SOL/USDT/USDC: `3x5NuXHzB5APG6vRinPZcsUv5ukWUY1tBGRSJiEJWtZa`**
- **ETH/USDT/USDC: `0xDc3Fe44F0f25D13CACb1C4896CD0D321df3146Ee`**
- **Project X NFT: https://opensea.io/item/ethereum/0x5ee362866001613093361eb8569d59c4141b76d1/1**
- **VLESS NFT: https://opensea.io/collection/vless**
- **REALITY NFT: https://opensea
```
</details>

---
### 📦 [klzgrad/naiveproxy](https://github.com/klzgrad/naiveproxy)
`⭐ Stars: 9,582` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [v154.0.8037.49-5](https://github.com/klzgrad/naiveproxy/releases/tag/v154.0.8037.49-5) (2026-10-22)`

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
`⭐ Stars: 4,543` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.1.1](https://github.com/JustAResearcher/gpu-unlock-ada/releases/tag/v1.1.1) (2026-10-24)`

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
`⭐ Stars: 2,854` &nbsp;|&nbsp; `💻 语言: Other` &nbsp;|&nbsp; `🏷️ 最新版本: [0.10.4a](https://github.com/NeverSinkDev/NeverSink-Filter-for-PoE2/releases/tag/0.10.4a) (2026-10-15)`

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
`⭐ Stars: 165` &nbsp;|&nbsp; `💻 语言: Shell` &nbsp;|&nbsp; `🏷️ 最新版本: [2026.10.29-20/01_arm_cortex-a9](https://github.com/kenzok8/compile-package/releases/tag/2026.10.29-20/01_arm_cortex-a9) (2026-10-29)`

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
`⭐ Stars: 11,984` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.2.2](https://github.com/jxxghp/MoviePilot/releases/tag/v3.2.2) (2026-10-29)`

> **简介**：NAS媒体库自动化管理工具

**💡 核心亮点更新 (中文)**：
- 插件市场支持安装前查看使用说明，完善文档入口和作者头像展示。
- 搜索字幕筛选支持“中字”和“特效”，兼容已有筛选设置。
- 新增 Obscurify.ai 大模型服务商。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 本次更新内容

- 插件市场支持安装前查看使用说明，完善文档入口和作者头像展示。
- 搜索字幕筛选支持“中字”和“特效”，兼容已有筛选设置。
- 新增 Obscurify.ai 大模型服务商。
- 优化 Agent 在兼容 Responses 接口下的缓存复用，修复 Telegram 等渠道的命令回执投递。
- 修复历史整理任务恢复、结果结算及缺少元数据导致的异常，避免重复创建待处理任务。
- 插件 Release 安装支持 GitHub 镜像下载，完善下载超时、异常回退和安装方式偏好处理。
- 修复站点重定向异常中断 CookieCloud 同步等批量操作的问题。
- 改善浅色主题下媒体卡片文字与信息的对比度。
- 升级 LangGraph 依赖，修复已知安全问题。
- 修复升级弹窗在禁用和加载状态下按钮文字不可见的问题。
- 修复 App 通知在重启或认证失效后重新登录时误解绑的问题，保留已配对的网页通知。

## 完整变更记录

- fix(plugin): support mirrors for Release asset downloads (#7224) by @jxxghp ([be65e04](https://github.com/jxxghp/MoviePilot/commit/be65e047b0e64b216420ba38bec7a087409552ff))
- fix(site): keep redirect failures from aborting site requests (#7227) by @MiCat-S ([252b702](https://github.com/jxxghp/MoviePilot/commit/252b702875cba0fa2d4428376ef2829cc4c997b9))
- fix(agent): route agent command receipts to the signed channel user (#7228) by @MiCat-S ([87561a9](https://github.com/jxxghp/MoviePilot/commit/87561a90d16e9bc087225c72bbfebe16865b3baa))
- feat(llm): 新增 Obscurify.ai provider (#7229) by @tonydavis629 ([421dd2c](https://github.com/jxxghp/MoviePilot/commit/421dd2c055198eaa54a7b57f50c902c6ea5e37c8))
- fix(transfer): recover legacy results and retain pending sources (#7232) by @paysenyu ([b55d9bd](https://github.com/jxxghp/MoviePilot/commit/b55d9bd167bf612305658b3e61106f6b4eff912c))
- fix(agent): preserve cache keys for compatible Responses endpoints (#7236) by @jxxghp ([8fe8ea4](https://github.com/jxxghp/MoviePilot/commit/8fe8ea477e2bf74f3525b5864831969c34e26
```
</details>

---
### 📦 [sandboxie-plus/Sandboxie](https://github.com/sandboxie-plus/Sandboxie)
`⭐ Stars: 19,828` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.18.8](https://github.com/sandboxie-plus/Sandboxie/releases/tag/v1.18.8) (2026-10-17)`

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
`⭐ Stars: 4,896` &nbsp;|&nbsp; `💻 语言: C#` &nbsp;|&nbsp; `🏷️ 最新版本: [10.0.10](https://github.com/HMBSbige/NatTypeTester/releases/tag/10.0.10) (2026-10-08)`

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
`⭐ Stars: 17,806` &nbsp;|&nbsp; `💻 语言: C#` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.2.0](https://github.com/KnifeLemon/Filee/releases/tag/v2.2.0) (2026-10-28)`

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
`⭐ Stars: 5,720` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.1.3](https://github.com/guohuiyuan/go-music-dl/releases/tag/v1.1.3) (2026-10-19)`

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
`⭐ Stars: 22,764` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.21.1](https://github.com/LibreSpark/LibreTV/releases/tag/v2.21.1) (2026-10-26)`

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
`⭐ Stars: 15,812` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.5.4](https://github.com/dyang886/Game-Cheats-Manager/releases/tag/v2.5.4) (2026-10-11)`

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
`⭐ Stars: 46,727` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2026.10.29-8494.9dae470](https://github.com/DIYgod/RSSHub/releases/tag/v2026.10.29-8494.9dae470) (2026-10-29)`

> **简介**：🧡 一切都是RSSible

**💡 核心亮点更新 (中文)**：
-ghcr.io/diygod/rsshub:9dae4709c8fc2bbd4a0012e2412de609eb0c6872
- ghcr.io/diygod/rsshub:chromium-bundled-9dae4709c8fc2bbd4a0012e2412de609eb0c6872
-diygod/rsshub:9dae4709c8fc2bbd4a0012e2412de609eb0c6872

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Source commit: 9dae4709c8fc2bbd4a0012e2412de609eb0c6872

Published multi-platform images:
- ghcr.io/diygod/rsshub:9dae4709c8fc2bbd4a0012e2412de609eb0c6872
- ghcr.io/diygod/rsshub:chromium-bundled-9dae4709c8fc2bbd4a0012e2412de609eb0c6872
- diygod/rsshub:9dae4709c8fc2bbd4a0012e2412de609eb0c6872
- diygod/rsshub:chromium-bundled-9dae4709c8fc2bbd4a0012e2412de609eb0c6872

Use these commit-specific image tags to reproduce this release. Daily Docker tags may be updated by subsequent builds.
```
</details>

---
### 📦 [amir1376/ab-download-manager](https://github.com/amir1376/ab-download-manager)
`⭐ Stars: 18,831` &nbsp;|&nbsp; `💻 语言: Kotlin` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.11.1](https://github.com/amir1376/ab-download-manager/releases/tag/v1.11.1) (2026-10-14)`

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
`⭐ Stars: 203,792` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [2026.10.26](https://github.com/yt-dlp/yt-dlp/releases/tag/2026.10.26) (2026-10-26)`

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
`⭐ Stars: 78,598` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [33.0.1](https://github.com/obsproject/obs-studio/releases/tag/33.0.1) (2026-10-29)`

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
`⭐ Stars: 5,572` &nbsp;|&nbsp; `💻 语言: CSS` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.1.1](https://github.com/jerrykuku/luci-theme-argon/releases/tag/v3.1.1) (2026-10-28)`

> **简介**：Argon 是一个干净整洁的 OpenWrt LuCI 主题，允许用户使用图像或视频自定义其登录界面。   它还支持明暗模式自动和手动切换。

**💡 核心亮点更新 (中文)**：
* 修复（wol）：通过 https://github.com/jerrykuku/luci-theme-argon/pull/722 正确设置和输出间距
* 修复（openclash）：通过 https://github.com/jerrykuku/luci-theme-argon/pull/723 对齐布局并恢复主题重音
* 修复（页面）：通过 https://github.com/jerrykuku/luci-theme-argon/pull/727 纠正原生 LuCI 卡布局

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Fixed / 修复

- Fix mobile sidebar controls that could fail to open, including in Chrome.
- Keep overview port counters and Wi-Fi signal/noise readings readable in narrow layouts and with larger text.
- Prevent wireless client Disconnect menu buttons from wrapping vertically; improve the layout of network names, MAC addresses and host details.
- Refresh stylesheet cache keys when CSS changes, including source rebuilds using the same package version.
- Correct card layouts and spacing on system logs, processes, package management, cron, SSH access, public keys, diagnostics and reboot pages.
- Improve OpenClash update/log pages, Wake on LAN settings/output and Tailscale status/device tables, including both Services and VPN menu paths.

- 修复手机侧栏菜单可能无法打开的问题，包括 Chrome 浏览器下的点击响应。
- 改善概览端口收发计数与 Wi-Fi 信号／噪声显示，兼顾窄屏和大字号。
- 修复无线客户端 Disconnect 菜单按钮文字竖排，优化网络名称、MAC 地址与主机信息布局。
- CSS 更新时自动变更缓存标识，覆盖使用相同包版本号重新编译的情况。
- 修正系统日志、进程、软件包管理、计划任务、SSH 管理、公钥、网络诊断及重启页面的卡片布局和间距。
- 改善 OpenClash 更新／日志、网络唤醒设置／输出及 Tailscale 状态／设备表格，兼容 Services 与 VPN 两种菜单路径。

## Upgrade notes / 升级说明

Users on v3.1.0 can upgrade through **System → Argon Config → Theme updates**. Users on v3.0.0 or earlier must install v3.1.1 manually once. Online installation updates the theme package and preserves settings; install separate translation packages in the usual way.

v3.1.0 用户可通过**系统 → Argon 配置 → 主题更新**升级。v3.0.0 及更早版本用户需先手动安装一次 v3.1.1。在线安装更新主题主包并保留设置；独立语言包仍按原方式安装。

## Installation / 安装说明

| Firmware / 固件 | Package / 安装包 |
| --- |
```
</details>

---
### 📦 [qier222/YesPlayMusic](https://github.com/qier222/YesPlayMusic)
`⭐ Stars: 33,493` &nbsp;|&nbsp; `💻 语言: Vue` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.4.11](https://github.com/qier222/YesPlayMusic/releases/tag/v0.4.11) (2026-10-10)`

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
`⭐ Stars: 57,577` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.1.1](https://github.com/agalwood/Motrix/releases/tag/v2.1.1) (2026-10-29)`

> **简介**：功能齐全的下载管理器。

**💡 核心亮点更新 (中文)**：
* 修复（迁移）：避免在 https://github.com/agalwood/Motrix/pull/2458 中保留未解析的磁力路径提示
* 修复（设置）：通过 https://github.com/agalwood/Motrix/pull/2460 将并发下载限制提高到 200
* 杂务（发布）：在 https://github.com/agalwood/Motrix/pull/2461 中准备 2.1.1

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# Motrix 2.1.1

English | [简体中文](https://github.com/agalwood/Motrix/blob/v2.1.1/docs/release-notes/2.1.1.zh-CN.md)

Motrix 2.1.1 increases the configurable download concurrency and fixes false
path conflicts during legacy task migration.

## Changes since 2.1.0

- Raise the simultaneous-download setting from 1–100 to **1–200**, keeping
  the default at **10**. Values above 100 remain intact after saving other
  settings and restarting the application. Addresses the requested limit
  increase in [#2439](https://github.com/agalwood/Motrix/issues/2439).
- Stop treating display names and output hints from unresolved legacy magnet
  tasks as owned file paths. Multiple magnet tasks can be imported without
  false path conflicts, and those hints no longer block unrelated HTTP or
  BitTorrent task activation. Existing-file protections for tasks with actual
  output ownership remain in place. Fixes
  [#2437](https://github.com/agalwood/Motrix/issues/2437).
- Update form resolvers, virtual lists, layout and icon dependencies, along with
  Biome and pnpm. Update electron-builder to **26.18.1** and electron-updater to
  **6.8.12**, including fixes for differential-download redirects and cached
  block maps. `vscode-jsonrpc` remains at **9.0.3**, Electron at **45.1.0**, and
  the bundled engine at **aria2 1.37.0-motrix.21**.

## Downloads and updates

Desktop packages support macOS 13 or later, Windows 10 or later, and Linux,
with native x64 and ARM64 builds. No 32-bit desktop packages ar
```
</details>

---
### 📦 [subhra74/xdm](https://github.com/subhra74/xdm)
`⭐ Stars: 8,167` &nbsp;|&nbsp; `💻 语言: Kotlin` &nbsp;|&nbsp; `🏷️ 最新版本: [9.0.8](https://github.com/subhra74/xdm/releases/tag/9.0.8) (2026-10-25)`

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
`⭐ Stars: 18,194` &nbsp;|&nbsp; `💻 语言: Swift` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.5.12](https://github.com/robbietilton/Compositor/releases/tag/v1.5.12) (2026-10-27)`

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
`⭐ Stars: 63,721` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v32.6.1](https://github.com/jgraph/drawio-desktop/releases/tag/v32.6.1) (2026-10-23)`

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
`⭐ Stars: 95,386` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.2.2](https://github.com/Stirling-Tools/Stirling-PDF/releases/tag/v3.2.2) (2026-10-24)`

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
`⭐ Stars: 40,085` &nbsp;|&nbsp; `💻 语言: Java` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.27.1](https://github.com/halo-dev/halo/releases/tag/v2.27.1) (2026-10-23)`

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
`⭐ Stars: 4,784` &nbsp;|&nbsp; `💻 语言: C#` &nbsp;|&nbsp; `🏷️ 最新版本: [4.16.2-Installer](https://github.com/emoacht/Monitorian/releases/tag/4.16.2-Installer) (2026-10-12)`

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
`⭐ Stars: 14,622` &nbsp;|&nbsp; `💻 语言: PowerShell` &nbsp;|&nbsp; `🏷️ 最新版本: [v11.8.50.0](https://github.com/YerongAI/Office-Tool/releases/tag/v11.8.50.0) (2026-10-18)`

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
`⭐ Stars: 194,364` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [1.144.0](https://github.com/microsoft/vscode/releases/tag/1.144.0) (2026-10-28)`

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
`⭐ Stars: 2,137` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.0.6](https://github.com/bestruirui/BestSub/releases/tag/v2.0.6) (2026-10-07)`

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
`⭐ Stars: 39,422` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.14.4](https://github.com/SagerNet/sing-box/releases/tag/v1.14.4) (2026-10-24)`

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
`⭐ Stars: 10,798` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [2.44.2](https://github.com/sub-store-org/Sub-Store/releases/tag/2.44.2) (2026-10-25)`

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
`⭐ Stars: 2,649` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.39.0](https://github.com/enfein/mieru/releases/tag/v3.39.0) (2026-10-23)`

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
`⭐ Stars: 15,767` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.5.10](https://github.com/v2rayA/v2rayA/releases/tag/v2.5.10) (2026-10-09)`

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
`⭐ Stars: 27,997` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.48.002](https://github.com/vernesong/OpenClash/releases/tag/v0.48.002) (2026-10-12)`

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
`⭐ Stars: 22,796` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [app/v2.13.0](https://github.com/HyNetworks/hysteria/releases/tag/app/v2.13.0) (2026-10-05)`

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
`⭐ Stars: 2,775` &nbsp;|&nbsp; `💻 语言: Shell` &nbsp;|&nbsp; `🏷️ 最新版本: [25.12.6](https://github.com/QiuSimons/YAOF/releases/tag/25.12.6) (2026-10-18)`

> **简介**：适用于 Nanopi R2C/R2S/R4S/X86 的 OpenWrt

**💡 核心亮点更新 (中文)**：
该版本未提供详细更新说明。

---
### 📦 [Loyalsoldier/v2ray-rules-dat](https://github.com/Loyalsoldier/v2ray-rules-dat)
`⭐ Stars: 20,975` &nbsp;|&nbsp; `💻 语言: Other` &nbsp;|&nbsp; `🏷️ 最新版本: [202610292204](https://github.com/Loyalsoldier/v2ray-rules-dat/releases/tag/202610292204) (2026-10-29)`

> **简介**：🦄 🎃 👻 V2Ray 路由规则文件加强版，可代替 V2Ray 官方 geoip.dat 和 geosite.dat，适用于 V2Ray、Xray-core、mihomo(Clash-Meta)、hysteria、Trojan-Go 和 leaf。Enhanced edition of V2Ray rules dat files, applicable to V2Ray, Xray-core, mihomo(Clash-Meta), hysteria, Trojan-Go and leaf.

**💡 核心亮点更新 (中文)**：
该版本未提供详细更新说明。

---
### 📦 [Openwrt-Passwall/openwrt-passwall](https://github.com/Openwrt-Passwall/openwrt-passwall)
`⭐ Stars: 9,984` &nbsp;|&nbsp; `💻 语言: Lua` &nbsp;|&nbsp; `🏷️ 最新版本: [26.10.29-1](https://github.com/Openwrt-Passwall/openwrt-passwall/releases/tag/26.10.29-1) (2026-10-29)`

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
`⭐ Stars: 119,510` &nbsp;|&nbsp; `💻 语言: C#` &nbsp;|&nbsp; `🏷️ 最新版本: [7.25.6](https://github.com/2dust/v2rayN/releases/tag/7.25.6) (2026-10-11)`

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
`⭐ Stars: 28,975` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [v25.12.6](https://github.com/openwrt/openwrt/releases/tag/v25.12.6) (2026-10-18)`

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
`⭐ Stars: 80,460` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.1.18](https://github.com/ventoy/Ventoy/releases/tag/v1.1.18) (2026-10-09)`

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
| [cityflow-project/CityFlow](https://github.com/cityflow-project/CityFlow) | 1,029 | 超过 436 天无代码提交 | [进入取消 Star](https://github.com/cityflow-project/CityFlow) |
| [facebookresearch/demucs](https://github.com/facebookresearch/demucs) | 10,403 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/facebookresearch/demucs) |
| [fufankeji/DeepSeek-OCR-Web](https://github.com/fufankeji/DeepSeek-OCR-Web) | 568 | 超过 367 天无代码提交 | [进入取消 Star](https://github.com/fufankeji/DeepSeek-OCR-Web) |
| [JimmyLv/awesome-nano-banana](https://github.com/JimmyLv/awesome-nano-banana) | 8,805 | 超过 416 天无代码提交 | [进入取消 Star](https://github.com/JimmyLv/awesome-nano-banana) |
| [btjawa/BiliTools](https://github.com/btjawa/BiliTools) | 5,034 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/btjawa/BiliTools) |
| [ehang-io/nps](https://github.com/ehang-io/nps) | 34,263 | 超过 883 天无代码提交 | [进入取消 Star](https://github.com/ehang-io/nps) |
| [ReturnFI/Blitz](https://github.com/ReturnFI/Blitz) | 1,091 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/ReturnFI/Blitz) |
| [kkangert/kspider](https://github.com/kkangert/kspider) | 1,265 | 超过 802 天无代码提交 | [进入取消 Star](https://github.com/kkangert/kspider) |
| [xenova/whisper-web](https://github.com/xenova/whisper-web) | 3,345 | 超过 758 天无代码提交 | [进入取消 Star](https://github.com/xenova/whisper-web) |
| [shadowsocks/luci-app-shadowsocks](https://github.com/shadowsocks/luci-app-shadowsocks) | 1,151 | 超过 1250 天无代码提交 | [进入取消 Star](https://github.com/shadowsocks/luci-app-shadowsocks) |
| [sinaptik-ai/pandas-ai](https://github.com/sinaptik-ai/pandas-ai) | 23,913 | 超过 366 天无代码提交 | [进入取消 Star](https://github.com/sinaptik-ai/pandas-ai) |
| [adithya-s-k/marker-api](https://github.com/adithya-s-k/marker-api) | 984 | 超过 744 天无代码提交 | [进入取消 Star](https://github.com/adithya-s-k/marker-api) |
| [yuchannslv5/warpflare](https://github.com/yuchannslv5/warpflare) | 334 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/yuchannslv5/warpflare) |
| [vvbbnn00/WARP-Clash-API](https://github.com/vvbbnn00/WARP-Clash-API) | 8,812 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/vvbbnn00/WARP-Clash-API) |
| [ca110us/epeius](https://github.com/ca110us/epeius) | 1,223 | 超过 802 天无代码提交 | [进入取消 Star](https://github.com/ca110us/epeius) |
| [chika0801/hysteria-install](https://github.com/chika0801/hysteria-install) | 177 | 超过 847 天无代码提交 | [进入取消 Star](https://github.com/chika0801/hysteria-install) |
| [yeahwu/InstallOS](https://github.com/yeahwu/InstallOS) | 86 | 超过 1604 天无代码提交 | [进入取消 Star](https://github.com/yeahwu/InstallOS) |
| [bulianglin/psub](https://github.com/bulianglin/psub) | 1,762 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/bulianglin/psub) |
| [lizongying/my-tv](https://github.com/lizongying/my-tv) | 31,964 | 超过 862 天无代码提交 | [进入取消 Star](https://github.com/lizongying/my-tv) |
| [joevess/IPTV](https://github.com/joevess/IPTV) | 10,280 | 超过 667 天无代码提交 | [进入取消 Star](https://github.com/joevess/IPTV) |
| [lecepin/WeChatVideoDownloader](https://github.com/lecepin/WeChatVideoDownloader) | 4,667 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/lecepin/WeChatVideoDownloader) |
| [linexjlin/GPTs](https://github.com/linexjlin/GPTs) | 32,030 | 超过 763 天无代码提交 | [进入取消 Star](https://github.com/linexjlin/GPTs) |
| [lxfater/Awesome-GPTs](https://github.com/lxfater/Awesome-GPTs) | 1,152 | 超过 1073 天无代码提交 | [进入取消 Star](https://github.com/lxfater/Awesome-GPTs) |
| [ClashDotNetFramework/experimental-clash](https://github.com/ClashDotNetFramework/experimental-clash) | 241 | 超过 1788 天无代码提交 | [进入取消 Star](https://github.com/ClashDotNetFramework/experimental-clash) |
| [zzzgydi/clash-verge](https://github.com/zzzgydi/clash-verge) | 21,864 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/zzzgydi/clash-verge) |
| [ddgth/cf2dns](https://github.com/ddgth/cf2dns) | 5,213 | 超过 662 天无代码提交 | [进入取消 Star](https://github.com/ddgth/cf2dns) |
| [zizifn/edgetunnel](https://github.com/zizifn/edgetunnel) | 9,297 | 超过 701 天无代码提交 | [进入取消 Star](https://github.com/zizifn/edgetunnel) |
| [missuo/Hysteria2](https://github.com/missuo/Hysteria2) | 204 | 超过 792 天无代码提交 | [进入取消 Star](https://github.com/missuo/Hysteria2) |
| [Misaka-blog/hysteria-install](https://github.com/Misaka-blog/hysteria-install) | 629 | 超过 924 天无代码提交 | [进入取消 Star](https://github.com/Misaka-blog/hysteria-install) |
| [MatsuriDayo/nekoray](https://github.com/MatsuriDayo/nekoray) | 15,272 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/MatsuriDayo/nekoray) |
| [FranzKafkaYu/x-ui](https://github.com/FranzKafkaYu/x-ui) | 8,451 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/FranzKafkaYu/x-ui) |
| [rwv/chinese-dos-games](https://github.com/rwv/chinese-dos-games) | 10,347 | 超过 813 天无代码提交 | [进入取消 Star](https://github.com/rwv/chinese-dos-games) |
| [getumbrel/llama-gpt](https://github.com/getumbrel/llama-gpt) | 10,924 | 超过 919 天无代码提交 | [进入取消 Star](https://github.com/getumbrel/llama-gpt) |
| [WangWenBin2017/OpenWrt-SSRPLUS](https://github.com/WangWenBin2017/OpenWrt-SSRPLUS) | 560 | 超过 606 天无代码提交 | [进入取消 Star](https://github.com/WangWenBin2017/OpenWrt-SSRPLUS) |
| [prompt-engineering/click-prompt](https://github.com/prompt-engineering/click-prompt) | 2,389 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/prompt-engineering/click-prompt) |
| [AutodeskAILab/Building-GAN](https://github.com/AutodeskAILab/Building-GAN) | 101 | 超过 1609 天无代码提交 | [进入取消 Star](https://github.com/AutodeskAILab/Building-GAN) |
| [novicezk/midjourney-proxy](https://github.com/novicezk/midjourney-proxy) | 5,374 | 超过 453 天无代码提交 | [进入取消 Star](https://github.com/novicezk/midjourney-proxy) |
| [adams549659584/go-proxy-bingai](https://github.com/adams549659584/go-proxy-bingai) | 8,406 | 超过 954 天无代码提交 | [进入取消 Star](https://github.com/adams549659584/go-proxy-bingai) |
| [tryptech/obs-zoom-and-follow](https://github.com/tryptech/obs-zoom-and-follow) | 440 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/tryptech/obs-zoom-and-follow) |
| [XingangPan/DragGAN](https://github.com/XingangPan/DragGAN) | 35,711 | 超过 894 天无代码提交 | [进入取消 Star](https://github.com/XingangPan/DragGAN) |
| [lewangdev/faster-whisper-youtube](https://github.com/lewangdev/faster-whisper-youtube) | 559 | 超过 1167 天无代码提交 | [进入取消 Star](https://github.com/lewangdev/faster-whisper-youtube) |
| [artidoro/qlora](https://github.com/artidoro/qlora) | 11,061 | 超过 871 天无代码提交 | [进入取消 Star](https://github.com/artidoro/qlora) |
| [langgenius/webapp-conversation](https://github.com/langgenius/webapp-conversation) | 1,102 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/langgenius/webapp-conversation) |
| [3andne/restls](https://github.com/3andne/restls) | 377 | 超过 1089 天无代码提交 | [进入取消 Star](https://github.com/3andne/restls) |
| [jtsang4/claude-to-chatgpt](https://github.com/jtsang4/claude-to-chatgpt) | 1,300 | 超过 802 天无代码提交 | [进入取消 Star](https://github.com/jtsang4/claude-to-chatgpt) |
| [yorunning/clash-conf](https://github.com/yorunning/clash-conf) | 102 | 超过 835 天无代码提交 | [进入取消 Star](https://github.com/yorunning/clash-conf) |
| [svc-develop-team/so-vits-svc](https://github.com/svc-develop-team/so-vits-svc) | 28,064 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/svc-develop-team/so-vits-svc) |
| [xiaye13579/BBLL](https://github.com/xiaye13579/BBLL) | 17,515 | 超过 609 天无代码提交 | [进入取消 Star](https://github.com/xiaye13579/BBLL) |
| [camenduru/MiniGPT-4-colab](https://github.com/camenduru/MiniGPT-4-colab) | 119 | 超过 1187 天无代码提交 | [进入取消 Star](https://github.com/camenduru/MiniGPT-4-colab) |
| [Vision-CAIR/MiniGPT-4](https://github.com/Vision-CAIR/MiniGPT-4) | 25,575 | 超过 787 天无代码提交 | [进入取消 Star](https://github.com/Vision-CAIR/MiniGPT-4) |
| [imfuxiao/Hamster](https://github.com/imfuxiao/Hamster) | 1,640 | 超过 535 天无代码提交 | [进入取消 Star](https://github.com/imfuxiao/Hamster) |
| [acheong08/ChatGPT](https://github.com/acheong08/ChatGPT) | 27,982 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/acheong08/ChatGPT) |
| [microsoft/JARVIS](https://github.com/microsoft/JARVIS) | 25,524 | 超过 457 天无代码提交 | [进入取消 Star](https://github.com/microsoft/JARVIS) |
| [choephix/auto-gpt-webui](https://github.com/choephix/auto-gpt-webui) | 116 | 超过 955 天无代码提交 | [进入取消 Star](https://github.com/choephix/auto-gpt-webui) |
| [facebookresearch/segment-anything](https://github.com/facebookresearch/segment-anything) | 55,074 | 超过 771 天无代码提交 | [进入取消 Star](https://github.com/facebookresearch/segment-anything) |
| [zai-org/ChatGLM-6B](https://github.com/zai-org/ChatGLM-6B) | 40,897 | 超过 855 天无代码提交 | [进入取消 Star](https://github.com/zai-org/ChatGLM-6B) |
| [ihciah/shadow-tls](https://github.com/ihciah/shadow-tls) | 2,681 | 超过 552 天无代码提交 | [进入取消 Star](https://github.com/ihciah/shadow-tls) |
| [jxbbb/ADAPT](https://github.com/jxbbb/ADAPT) | 421 | 超过 870 天无代码提交 | [进入取消 Star](https://github.com/jxbbb/ADAPT) |
| [mayooear/ai-pdf-chatbot-langchain](https://github.com/mayooear/ai-pdf-chatbot-langchain) | 16,582 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/mayooear/ai-pdf-chatbot-langchain) |
| [lencx/ChatGPT](https://github.com/lencx/ChatGPT) | 54,667 | 超过 791 天无代码提交 | [进入取消 Star](https://github.com/lencx/ChatGPT) |
| [nekohasekai/SagerNet](https://github.com/nekohasekai/SagerNet) | 56 | 超过 1754 天无代码提交 | [进入取消 Star](https://github.com/nekohasekai/SagerNet) |
| [P3TERX/Actions-OpenWrt](https://github.com/P3TERX/Actions-OpenWrt) | 7,621 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/P3TERX/Actions-OpenWrt) |
| [R86S/R86S-QuickInstaller](https://github.com/R86S/R86S-QuickInstaller) | 64 | 超过 1175 天无代码提交 | [进入取消 Star](https://github.com/R86S/R86S-QuickInstaller) |
| [WeNeedHome/SummaryOfLoanSuspension](https://github.com/WeNeedHome/SummaryOfLoanSuspension) | 20,332 | 超过 839 天无代码提交 | [进入取消 Star](https://github.com/WeNeedHome/SummaryOfLoanSuspension) |
| [zanzhz1101/LingMaxDNS](https://github.com/zanzhz1101/LingMaxDNS) | 23 | 超过 1570 天无代码提交 | [进入取消 Star](https://github.com/zanzhz1101/LingMaxDNS) |
| [IrineSistiana/mosdns-cn](https://github.com/IrineSistiana/mosdns-cn) | 325 | 超过 1611 天无代码提交 | [进入取消 Star](https://github.com/IrineSistiana/mosdns-cn) |
| [chika0801/Xray-install](https://github.com/chika0801/Xray-install) | 273 | 超过 1063 天无代码提交 | [进入取消 Star](https://github.com/chika0801/Xray-install) |
| [scutan90/DeepLearning-500-questions](https://github.com/scutan90/DeepLearning-500-questions) | 57,696 | 超过 855 天无代码提交 | [进入取消 Star](https://github.com/scutan90/DeepLearning-500-questions) |
| [Chikage0o0/Linux-NetSpeed](https://github.com/Chikage0o0/Linux-NetSpeed) | 3,743 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/Chikage0o0/Linux-NetSpeed) |
| [KFERMercer/OpenWrt-CI](https://github.com/KFERMercer/OpenWrt-CI) | 1,409 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/KFERMercer/OpenWrt-CI) |
| [qTox/qTox](https://github.com/qTox/qTox) | 4,969 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/qTox/qTox) |
| [quericy/one-key-ikev2-vpn](https://github.com/quericy/one-key-ikev2-vpn) | 2,105 | 超过 2174 天无代码提交 | [进入取消 Star](https://github.com/quericy/one-key-ikev2-vpn) |
| [riverscn/openwrt-iptvhelper](https://github.com/riverscn/openwrt-iptvhelper) | 371 | 超过 1890 天无代码提交 | [进入取消 Star](https://github.com/riverscn/openwrt-iptvhelper) |
| [frainzy1477/luci-app-clash](https://github.com/frainzy1477/luci-app-clash) | 1,623 | 超过 1680 天无代码提交 | [进入取消 Star](https://github.com/frainzy1477/luci-app-clash) |
| [Sanster/IOPaint](https://github.com/Sanster/IOPaint) | 23,295 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/Sanster/IOPaint) |
| [LANDrop/LANDrop](https://github.com/LANDrop/LANDrop) | 5,995 | 超过 807 天无代码提交 | [进入取消 Star](https://github.com/LANDrop/LANDrop) |
| [saveweb/review-2021](https://github.com/saveweb/review-2021) | 758 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/saveweb/review-2021) |
| [iranee/qnap-aliyunpan-webdav](https://github.com/iranee/qnap-aliyunpan-webdav) | 274 | 超过 1482 天无代码提交 | [进入取消 Star](https://github.com/iranee/qnap-aliyunpan-webdav) |
| [haoel/haoel.github.io](https://github.com/haoel/haoel.github.io) | 13,078 | 超过 1267 天无代码提交 | [进入取消 Star](https://github.com/haoel/haoel.github.io) |
| [tindy2013/stairspeedtest-reborn](https://github.com/tindy2013/stairspeedtest-reborn) | 3,831 | 超过 1239 天无代码提交 | [进入取消 Star](https://github.com/tindy2013/stairspeedtest-reborn) |
| [P3TERX/warp.sh](https://github.com/P3TERX/warp.sh) | 3,926 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/P3TERX/warp.sh) |
| [TheMRLL/WinXray](https://github.com/TheMRLL/WinXray) | 2,792 | 超过 976 天无代码提交 | [进入取消 Star](https://github.com/TheMRLL/WinXray) |
| [Mikubill/cowtransfer-uploader](https://github.com/Mikubill/cowtransfer-uploader) | 447 | 超过 1723 天无代码提交 | [进入取消 Star](https://github.com/Mikubill/cowtransfer-uploader) |
| [281677160/build-actions](https://github.com/281677160/build-actions) | 388 | 超过 458 天无代码提交 | [进入取消 Star](https://github.com/281677160/build-actions) |
| [vaxilu/x-ui](https://github.com/vaxilu/x-ui) | 19,097 | 超过 801 天无代码提交 | [进入取消 Star](https://github.com/vaxilu/x-ui) |
| [xinntao/Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) | 37,277 | 超过 814 天无代码提交 | [进入取消 Star](https://github.com/xinntao/Real-ESRGAN) |
| [zu1k/proxypool](https://github.com/zu1k/proxypool) | 4,039 | 超过 1298 天无代码提交 | [进入取消 Star](https://github.com/zu1k/proxypool) |
| [TachibanaYoshino/AnimeGAN](https://github.com/TachibanaYoshino/AnimeGAN) | 4,611 | 超过 1548 天无代码提交 | [进入取消 Star](https://github.com/TachibanaYoshino/AnimeGAN) |
| [yuanzhoulvpi2017/tiny_python](https://github.com/yuanzhoulvpi2017/tiny_python) | 173 | 超过 1362 天无代码提交 | [进入取消 Star](https://github.com/yuanzhoulvpi2017/tiny_python) |
| [haiibo/OpenWrt](https://github.com/haiibo/OpenWrt) | 3,161 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/haiibo/OpenWrt) |
| [VergilGao/openwrt-packages](https://github.com/VergilGao/openwrt-packages) | 11 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/VergilGao/openwrt-packages) |
| [VergilGao/openwrt-compiler](https://github.com/VergilGao/openwrt-compiler) | 13 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/VergilGao/openwrt-compiler) |
| [OpenELEC/OpenELEC.tv](https://github.com/OpenELEC/OpenELEC.tv) | 1,620 | 超过 3344 天无代码提交 | [进入取消 Star](https://github.com/OpenELEC/OpenELEC.tv) |
| [github/copilot-docs](https://github.com/github/copilot-docs) | 23,169 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/github/copilot-docs) |
| [Kiougar/luci-wrtbwmon](https://github.com/Kiougar/luci-wrtbwmon) | 356 | 超过 1862 天无代码提交 | [进入取消 Star](https://github.com/Kiougar/luci-wrtbwmon) |
| [EtherDream/jsproxy](https://github.com/EtherDream/jsproxy) | 9,318 | 超过 942 天无代码提交 | [进入取消 Star](https://github.com/EtherDream/jsproxy) |
| [cheat-engine/cheat-engine](https://github.com/cheat-engine/cheat-engine) | 19,405 | 超过 559 天无代码提交 | [进入取消 Star](https://github.com/cheat-engine/cheat-engine) |
| [ffffffff0x/Dork-Admin](https://github.com/ffffffff0x/Dork-Admin) | 1,914 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/ffffffff0x/Dork-Admin) |
| [ffffffff0x/Digital-Privacy](https://github.com/ffffffff0x/Digital-Privacy) | 4,937 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/ffffffff0x/Digital-Privacy) |
| [Autodesk/civilconnection](https://github.com/Autodesk/civilconnection) | 118 | 超过 1428 天无代码提交 | [进入取消 Star](https://github.com/Autodesk/civilconnection) |
| [0xHJK/CleanApps](https://github.com/0xHJK/CleanApps) | 165 | 超过 1894 天无代码提交 | [进入取消 Star](https://github.com/0xHJK/CleanApps) |
| [KANIKIG/Multi-EasyGost](https://github.com/KANIKIG/Multi-EasyGost) | 1,944 | 超过 942 天无代码提交 | [进入取消 Star](https://github.com/KANIKIG/Multi-EasyGost) |
| [Kurokosama/AutoBuild-OpenWRT](https://github.com/Kurokosama/AutoBuild-OpenWRT) | 88 | 超过 1581 天无代码提交 | [进入取消 Star](https://github.com/Kurokosama/AutoBuild-OpenWRT) |
| [differentrain/DeletionTool](https://github.com/differentrain/DeletionTool) | 94 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/differentrain/DeletionTool) |
| [hideuvpn/android-google-play-store](https://github.com/hideuvpn/android-google-play-store) | 3,652 | 超过 1563 天无代码提交 | [进入取消 Star](https://github.com/hideuvpn/android-google-play-store) |
| [XJP-GIT/AntiZhaPian](https://github.com/XJP-GIT/AntiZhaPian) | 3,160 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/XJP-GIT/AntiZhaPian) |
| [jerrykuku/luci-app-ttnode](https://github.com/jerrykuku/luci-app-ttnode) | 89 | 超过 1739 天无代码提交 | [进入取消 Star](https://github.com/jerrykuku/luci-app-ttnode) |
| [KevinSHIT/NaiveSharp](https://github.com/KevinSHIT/NaiveSharp) | 96 | 超过 2184 天无代码提交 | [进入取消 Star](https://github.com/KevinSHIT/NaiveSharp) |
| [prasmussen/gdrive](https://github.com/prasmussen/gdrive) | 8,943 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/prasmussen/gdrive) |
| [tostercx/GTAO_Booster_PoC](https://github.com/tostercx/GTAO_Booster_PoC) | 2,864 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/tostercx/GTAO_Booster_PoC) |
| [ilxp/luci-app-ikoolproxy](https://github.com/ilxp/luci-app-ikoolproxy) | 507 | 超过 594 天无代码提交 | [进入取消 Star](https://github.com/ilxp/luci-app-ikoolproxy) |
| [kiddin9/luci-app-dnsfilter](https://github.com/kiddin9/luci-app-dnsfilter) | 123 | 超过 628 天无代码提交 | [进入取消 Star](https://github.com/kiddin9/luci-app-dnsfilter) |
| [h31105/deployX.sh](https://github.com/h31105/deployX.sh) | 416 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/h31105/deployX.sh) |
| [jerrykuku/openwrt-package](https://github.com/jerrykuku/openwrt-package) | 147 | 超过 1091 天无代码提交 | [进入取消 Star](https://github.com/jerrykuku/openwrt-package) |
| [frainzy1477/luci-app-trojan](https://github.com/frainzy1477/luci-app-trojan) | 120 | 超过 1998 天无代码提交 | [进入取消 Star](https://github.com/frainzy1477/luci-app-trojan) |
| [atrandys/xray](https://github.com/atrandys/xray) | 89 | 超过 1706 天无代码提交 | [进入取消 Star](https://github.com/atrandys/xray) |
| [v2board/v2board](https://github.com/v2board/v2board) | 5,064 | 超过 955 天无代码提交 | [进入取消 Star](https://github.com/v2board/v2board) |
| [ShadowsocksR-Live/iShadowsocksR](https://github.com/ShadowsocksR-Live/iShadowsocksR) | 601 | 超过 913 天无代码提交 | [进入取消 Star](https://github.com/ShadowsocksR-Live/iShadowsocksR) |
| [SuperNG6/Aria2-Trackers](https://github.com/SuperNG6/Aria2-Trackers) | 309 | 超过 2105 天无代码提交 | [进入取消 Star](https://github.com/SuperNG6/Aria2-Trackers) |
| [kakaruoterl/vless_install](https://github.com/kakaruoterl/vless_install) | 29 | 超过 2262 天无代码提交 | [进入取消 Star](https://github.com/kakaruoterl/vless_install) |
| [stupidloud/nanopi-openwrt](https://github.com/stupidloud/nanopi-openwrt) | 5,514 | 超过 926 天无代码提交 | [进入取消 Star](https://github.com/stupidloud/nanopi-openwrt) |
| [atrandys/trojan](https://github.com/atrandys/trojan) | 1,055 | 超过 1295 天无代码提交 | [进入取消 Star](https://github.com/atrandys/trojan) |
| [programthink/zhao](https://github.com/programthink/zhao) | 14,078 | 超过 1915 天无代码提交 | [进入取消 Star](https://github.com/programthink/zhao) |
| [RPRX/v2ray-vless](https://github.com/RPRX/v2ray-vless) | 389 | 超过 1341 天无代码提交 | [进入取消 Star](https://github.com/RPRX/v2ray-vless) |
| [h2y/Shadowrocket-ADBlock-Rules](https://github.com/h2y/Shadowrocket-ADBlock-Rules) | 16,722 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/h2y/Shadowrocket-ADBlock-Rules) |
| [p4gefau1t/trojan-go](https://github.com/p4gefau1t/trojan-go) | 8,389 | 超过 837 天无代码提交 | [进入取消 Star](https://github.com/p4gefau1t/trojan-go) |
| [Jrohy/trojan](https://github.com/Jrohy/trojan) | 5,635 | 超过 928 天无代码提交 | [进入取消 Star](https://github.com/Jrohy/trojan) |
| [mellow-io/mellow](https://github.com/mellow-io/mellow) | 3,535 | 超过 1419 天无代码提交 | [进入取消 Star](https://github.com/mellow-io/mellow) |
| [Dawneng/luci-theme-atmaterial](https://github.com/Dawneng/luci-theme-atmaterial) | 11 | 超过 1471 天无代码提交 | [进入取消 Star](https://github.com/Dawneng/luci-theme-atmaterial) |
| [trojan-gfw/igniter](https://github.com/trojan-gfw/igniter) | 3,274 | 超过 1068 天无代码提交 | [进入取消 Star](https://github.com/trojan-gfw/igniter) |
| [openwrt-develop/luci-theme-atmaterial](https://github.com/openwrt-develop/luci-theme-atmaterial) | 68 | 超过 2416 天无代码提交 | [进入取消 Star](https://github.com/openwrt-develop/luci-theme-atmaterial) |
| [trojan-gfw/trojan-quickstart](https://github.com/trojan-gfw/trojan-quickstart) | 244 | 超过 2017 天无代码提交 | [进入取消 Star](https://github.com/trojan-gfw/trojan-quickstart) |
| [FunctionClub/ZBench](https://github.com/FunctionClub/ZBench) | 1,175 | 超过 2048 天无代码提交 | [进入取消 Star](https://github.com/FunctionClub/ZBench) |
| [veekxt/v2ray-template](https://github.com/veekxt/v2ray-template) | 749 | 超过 2260 天无代码提交 | [进入取消 Star](https://github.com/veekxt/v2ray-template) |
| [HMBSbige/ShadowsocksR-Windows](https://github.com/HMBSbige/ShadowsocksR-Windows) | 6,910 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/HMBSbige/ShadowsocksR-Windows) |
| [trojan-gfw/trojan](https://github.com/trojan-gfw/trojan) | 19,750 | 超过 799 天无代码提交 | [进入取消 Star](https://github.com/trojan-gfw/trojan) |
</details>
