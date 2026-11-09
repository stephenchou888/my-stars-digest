# 📡 Starred 项目雷达看板
> 🖥️ **交互式管理看板 (shadcn/ui)**：[👉 点击进入在线雷达看板 (https://stephenchou888.github.io/my-stars-digest/)](https://stephenchou888.github.io/my-stars-digest/)

> **生成时间**：`2026-11-09` ｜ **关注项目总数**：`409` ｜ **本期更新**：`98` ｜ **弃坑预警**：`135`

| 统计指标 | 数量 | 状态提示 |
| :--- | :---: | :--- |
| 🌟 总关注库 | **409** | [进入 shadcn 在线看板管理](https://stephenchou888.github.io/my-stars-digest/) |
| 🚀 近期有更新 | **98** | 涵盖 6 个分类 |
| 🛑 建议清理/弃坑 | **135** | 建议取消 Star 保持关注列表整洁 |

---
## 🧭 领域分类速览导航

- [🤖 AI 与智能体生态 (53)](#-AI-与智能体生态)
- [📝 效率办公与创作 (11)](#-效率办公与创作)
- [📦 实用开源精选 (7)](#-实用开源精选)
- [🎬 影音媒体与下载 (15)](#-影音媒体与下载)
- [🛠️ 系统与开发者工具 (2)](#-系统与开发者工具)
- [🌐 网络与代理技术 (10)](#-网络与代理技术)

---

## <span id="-AI-与智能体生态">🤖 AI 与智能体生态</span>

### 📦 [duyunzhoudyz/dyz-gongwen-skills](https://github.com/duyunzhoudyz/dyz-gongwen-skills)
`⭐ Stars: 565` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.1.0](https://github.com/duyunzhoudyz/dyz-gongwen-skills/releases/tag/v1.1.0) (2026-11-04)`

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
`⭐ Stars: 19,870` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.2.0](https://github.com/vercel-labs/agent-desktop/releases/tag/v1.2.0) (2026-11-05)`

> **简介**：计算机使用 CLI 进行 AI 代理

**💡 核心亮点更新 (中文)**：
* feat(macos)：在 https://github.com/vercel-labs/agent-desktop/pull/503 中选择只有其容器可以选择的列表行
* 修复（macos）：通过 https://github.com/vercel-labs/agent-desktop/pull/511 在菜单和系统面板上方绘制光标覆盖层
* 文档：通过 https://github.com/vercel-labs/agent-desktop/pull/481 简化自述文件和存储库文档

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## What's Changed
* feat(macos): select list rows that only their container can select by @lahfir in https://github.com/vercel-labs/agent-desktop/pull/503
* fix(macos): draw the cursor overlay above menus and system panels by @lahfir in https://github.com/vercel-labs/agent-desktop/pull/511
* docs: simplify the README and repo docs by @lahfir in https://github.com/vercel-labs/agent-desktop/pull/481
* docs: document the homebrew-core install by @lahfir in https://github.com/vercel-labs/agent-desktop/pull/524
* feat: agent-desktop mcp by @lahfir in https://github.com/vercel-labs/agent-desktop/pull/519
* fix(macos): ignore exited apps in the workspace inventory by @lahfir in https://github.com/vercel-labs/agent-desktop/pull/371
* fix: preserve partial snapshots after observation expires by @lahfir in https://github.com/vercel-labs/agent-desktop/pull/372
* feat: accept stdin for text commands by @lahfir in https://github.com/vercel-labs/agent-desktop/pull/373
* fix: start the macos cursor overlay outside the caller's directory by @lahfir in https://github.com/vercel-labs/agent-desktop/pull/381
* chore: release 1.2.0 with mcp support by @lahfir in https://github.com/vercel-labs/agent-desktop/pull/568


**Full Changelog**: https://github.com/vercel-labs/agent-desktop/compare/v1.1.0...v1.2.0
```
</details>

---
### 📦 [JimLiu/baocut](https://github.com/JimLiu/baocut)
`⭐ Stars: 1,707` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [baocut-v3.16.4-build.92](https://github.com/JimLiu/baocut/releases/tag/baocut-v3.16.4-build.92) (2026-11-07)`

> **简介**：BaoCut：具有可编辑时间线的人工智能视频代理。转录、字幕、翻译、配音、剪辑和动画。

**💡 核心亮点更新 (中文)**：
- **等待问题和批准不再超时。** 等待您的问题或批准不再因“操作超时”而失败。大约四到五分钟后。当工具调用等待时，BaoCut 现在将保持活动进度发送到接受流式响应的 MCP 客户端，因此 2.1.274 之前的 Claude Code 版本和 Claude Code 的工具空闲看门狗不再丢弃它。快速调用和纯 JSON 客户端保持不变。 2.1.142之前的Claude Code版本仍然可以在60秒后结束此类调用；如果发生这种情况，请更新克劳德代码。参考文献 [#131](https://github.com/jimliu/baocut/issues/131)。 [详情](https://github.com/jimliu/baocut/commit/8371871a67acbc8b9ec40d4e2353c271e8da2748)
- **问题历史记录保留选择。** 当您在对话历史记录中展开时，停止、跳过或回答的问题会保留其标题、选项和选项说明，以便您可以查看所问的内容。 [详情](https://github.com/jimliu/baocut/pull/132)
- 内部：模型 API 服务测试现在使用仍然可用的图像模型。 [详情](https://github.com/jimliu/baocut/pull/130)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
BaoCut 3.16.4 (Build 92) for Apple Silicon, macOS 14+.

Bundle ID: com.baocut.app. Developer ID signed, hardened runtime and Apple notarization accepted for both App and DMG.

Runtime and native Worker startup, signer fingerprint, staple and Gatekeeper checks passed. UI/export, real model inference and paid Agent calls were not exercised by this workflow. ffmpeg/ffprobe and an agent engine are external dependencies.

Source: 4c8b479313b2daefc54df8a317ec8b1e526bd268
Actions: https://github.com/JimLiu/baocut/actions/runs/42404385219


## What's changed

- **Waiting questions and approvals no longer time out.** A question or approval that waits on you no longer fails with "The operation timed out." after about four to five minutes. While a tool call waits, BaoCut now sends keep-alive progress to MCP clients that accept streamed responses, so Claude Code versions before 2.1.274 and Claude Code's tool idle watchdog no longer drop it. Quick calls and JSON-only clients are unchanged. Claude Code versions before 2.1.142 can still end such calls after 60 seconds; update Claude Code if that happens. Refs [#131](https://github.com/jimliu/baocut/issues/131). [Details](https://github.com/jimliu/baocut/commit/8371871a67acbc8b9ec40d4e2353c271e8da2748)
- **Question history keeps the choices.** Questions that were stopped, skipped or answered keep their headers, choices and choice descriptions when you expand them in the conversation history, so you can review what was asked. [Details](https:
```
</details>

---
### 📦 [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)
`⭐ Stars: 18,850` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.1.150](https://github.com/milind-soni/OpenMausBot/releases/tag/v0.1.150) (2026-11-09)`

> **简介**：开源 Grok Bot 替代品，带有机器人可以使用的虚拟机

**💡 核心亮点更新 (中文)**：
- **My Cloud 上的恢复自行完成。** 恢复备份或将此计算机的工作区移至 My Cloud，通常需要等待“完全退出 MausBot...”，而 Cloud 无法做到这一点。现在，我的云会在恢复后立即重新启动自己的服务器，并在恢复时显示进度。
- **当许多机器人等待时，轮流队列会保持很快。** 检查下一个轮到谁所花费的时间与等待的数量成正比，而不是其平方，因此繁忙的云会不断应答。
- **一旦其模型调用之一得到应答，克劳德回合就不会发送两次**。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## What's new in 0.1.150

### Clouds finish restores and stay responsive
- **A restore on My Cloud finishes by itself.** Restoring a backup, or moving this computer's workspace to My Cloud, used to wait on "Fully quit MausBot…", which a Cloud can't do. My Cloud now restarts its own server right after the restore and shows progress while it comes back.
- **The turn queue stays fast when many bots wait.** Checking who goes next takes time in proportion to the number waiting, not its square, so a busy Cloud keeps answering.
- **A Claude turn is never sent twice** once one of its model calls has answered.
- **Routines save a run's progress once per window,** not after every step, so long runs write far less.
- **Paired phones and desktops get large bot lists** without stalling.

### A calmer, clearer app
- **Polish pass.** One corner-radius scale, clearer headings and lighter icons. A reply with a table or code is now one bubble instead of three boxes of different widths.
- **Pages open beside the chat.** A bot's page shows as a small card with **Open page**. The large view keeps the message box usable, so you can talk about the page while looking at it. You can also save a page as a file.
- **Simple mode does more.** The everyday settings that needed Advanced are now in Simple: what a bot may do without asking, reply style, per-bot notifications, who can see a bot, the cloud computer picker and Android.
- **Rules for every bot.** One field next to About me holds instructions eve
```
</details>

---
### 📦 [yuchen-ya/reelterminal](https://github.com/yuchen-ya/reelterminal)
`⭐ Stars: 24` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.3.12](https://github.com/yuchen-ya/reelterminal/releases/tag/v1.3.12) (2026-11-02)`

> **简介**：ReelTerminal — 您的 AI 视频的最后一站。具有共享人类/代理控制的代理本机视频整理编辑器。

**💡 核心亮点更新 (中文)**：
- 修复安装包中混入多余文件的问题。
- 修复切换指令窗口时，编辑窗口意外关闭的问题。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
- 修复安装包中混入多余文件的问题。
- 修复切换指令窗口时，编辑窗口意外关闭的问题。
```
</details>

---
### 📦 [KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)
`⭐ Stars: 4,184` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.7.0](https://github.com/KKKKhazix/agent-autoloop/releases/tag/v1.7.0) (2026-11-09)`

> **简介**：让你的命令行 Agent 在后台自己接活、自己跟进到底；平时不烦你，遇到拿不准的事才发卡片找你拍板。

**💡 核心亮点更新 (中文)**：
- **回答带上所选的文字。** 资料文件里 `answers` 的每一项多了 `chosen`：选了选项时是那一项的文字，只写了话时就是那句话。`choice` 仍是从 0 起的序号、原样保留。之前只有序号，Agent 会把 `choice: 1` 当成第一项，把人的决定读反（试跑里选“绿色”被报成“蓝色”）。`try` 的提示词也改成直接读 `chosen`。
- **Windows：npm 装的 Claude Code 能启动。** `npm i -g /claude-code` 生成的 `claude.cmd` 直接指向 `claude.exe`，以前会报“不能直接运行”、每一轮以退出码 127 失败，`check` 里的登录检查也一样。现在包装指向 `.exe` 时直接运行它，参数照原样传。
- **Answers carry the chosen text.** Each entry in the run file's `answers` now has `chosen`: the text of the picked option, or the person's own words when they wrote instead. `choice` is still the zero-based index, unchanged. With only the index, agents read `choice: 1` as the first option and reported the opposite of the decision (picking "green" in a trial came back as "blue"). The `try` prompt now reads `chosen` directly.

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
卡片回答带上所选的文字，Agent 不会再把人的选择读错；Windows 上用 npm 装的 Claude Code 能直接启动。旧规则、旧插件不用改。

- **回答带上所选的文字。** 资料文件里 `answers` 的每一项多了 `chosen`：选了选项时是那一项的文字，只写了话时就是那句话。`choice` 仍是从 0 起的序号、原样保留。之前只有序号，Agent 会把 `choice: 1` 当成第一项，把人的决定读反（试跑里选“绿色”被报成“蓝色”）。`try` 的提示词也改成直接读 `chosen`。
- **Windows：npm 装的 Claude Code 能启动。** `npm i -g @anthropic-ai/claude-code` 生成的 `claude.cmd` 直接指向 `claude.exe`，以前会报“不能直接运行”、每一轮以退出码 127 失败，`check` 里的登录检查也一样。现在包装指向 `.exe` 时直接运行它，参数照原样传。

感谢 lanfeng123456、Bortlesboat 的修复，qianqian2024 的报告。

---

Card answers now carry the chosen text, so agents no longer misread a person's choice; on Windows, Claude Code installed with npm starts. Existing rules and plugins work unchanged.

- **Answers carry the chosen text.** Each entry in the run file's `answers` now has `chosen`: the text of the picked option, or the person's own words when they wrote instead. `choice` is still the zero-based index, unchanged. With only the index, agents read `choice: 1` as the first option and reported the opposite of the decision (picking "green" in a trial came back as "blue"). The `try` prompt now reads `chosen` directly.
- **Windows: Claude Code installed with npm starts.** The `claude.cmd` that `npm i -g @anthropic-ai/claude-code` writes points straight at `claude.exe`; it used to be refused as not directly runnable, failing every run with exit code 127, and the login check in `check` failed the same way. A wrapper that points at an `.exe` now runs it directly, passing the arguments through as th
```
</details>

---
### 📦 [alchaincyf/huashu-motion](https://github.com/alchaincyf/huashu-motion)
`⭐ Stars: 2,538` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.3.1](https://github.com/alchaincyf/huashu-motion/releases/tag/v0.3.1) (2026-10-22)`

> **简介**：让你的agent一键直出商业级产品宣传片：会作曲，能指着画面改。Commercial-grade launch films by your coding agent — point at the frame to change it.

**💡 核心亮点更新 (中文)**：
- 三个方向卡上不再列配乐。大多数人没法凭一个曲风名字判断好坏，这个选择交给导演：方向选定后，按产品的使用者、场景、节奏、使用感受和出身来选音乐世界、速度和编制，写进分镜。
- 用户主动想参与配乐，才给选项；用户点名了风格或曲子，就用用户的。
- 速度跟着产品和剪辑走，不再默认 120。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 这一版改了什么

**配乐由导演按产品特点自己定，不再让用户挑**
- 三个方向卡上不再列配乐。大多数人没法凭一个曲风名字判断好坏，这个选择交给导演：方向选定后，按产品的使用者、场景、节奏、使用感受和出身来选音乐世界、速度和编制，写进分镜。
- 用户主动想参与配乐，才给选项；用户点名了风格或曲子，就用用户的。
- 速度跟着产品和剪辑走，不再默认 120。

## 怎么更新

```bash
git pull --ff-only
```

---

**Music is the director's call**: the direction cards no longer list music. Once a direction is chosen, the director picks the music world, tempo and band from the product's character and writes it into the treatment; options only when the user asks, and a style or track the user names wins. Tempo follows the product and the cut, not a default 120.

Update with `git pull --ff-only`.
```
</details>

---
### 📦 [wquguru/cicada](https://github.com/wquguru/cicada)
`⭐ Stars: 2,017` &nbsp;|&nbsp; `💻 语言: Swift` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.7.0](https://github.com/wquguru/cicada/releases/tag/v1.7.0) (2026-11-09)`

> **简介**：知了 Cicada · 任何会议和直播的实时字幕、同声传译、AI 会议纪要，Mac、Windows、Linux、Android 免费开源。Live subtitles, interpreting and meeting notes for any call or stream, on Mac, Windows, Linux and Android.

**💡 核心亮点更新 (中文)**：
- Cicada 在运行时停留在 Dock 中，录制时有一个橙色点和右键菜单 ([308f00c](https://github.com/wquguru/cicada/commit/308f00c27dfe008f3ccea3dbb22a58e482b5026e))
- 共享...以应用程序语言将链接和密码一起复制为一条消息 ([64b9471](https://github.com/wquguru/cicada/commit/64b94712a1ef3d9b9049e062db0a4952e45b6974))

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
### Mac

#### New

- Cicada stays in the Dock while it runs, with an orange dot while recording and a right-click menu ([308f00c](https://github.com/wquguru/cicada/commit/308f00c27dfe008f3ccea3dbb22a58e482b5026e))
- Share… copies the link and password together as one message in the app's language ([64b9471](https://github.com/wquguru/cicada/commit/64b94712a1ef3d9b9049e062db0a4952e45b6974))

#### Fixed

- A fresh 7-day share link no longer says it lasts 8 days ([a67e9c7](https://github.com/wquguru/cicada/commit/a67e9c72ba1a20e18c81b7ce291c03b04aa4f5ce))
- Fast speech without pauses comes out one sentence or clause per line instead of one growing block (#20) ([93dfb07](https://github.com/wquguru/cicada/commit/93dfb075e933fa3903378fb8b3caafd0a462ecd4))
- The live notes transcript starts a new paragraph every two or three sentences when someone talks fast ([7c40e6b](https://github.com/wquguru/cicada/commit/7c40e6b11301246680e85f22016033945cdd1e3e))
- The meeting record no longer splits a Chinese word like 所以 across two lines ([ac4d8e0](https://github.com/wquguru/cicada/commit/ac4d8e0929f153c68fae78435ddcfd8de073475a))
- In the live notes window, fast Chinese lines end at a clause more often instead of between two words ([79af264](https://github.com/wquguru/cicada/commit/79af264913a67bb50123788d92eaac4fb24d7ba4))

### Windows

#### New

- Share… copies the link and password together as one message in the app's language ([b01fe7f](https://github.com/wquguru/cicada/commit/b01fe7fc5
```
</details>

---
### 📦 [SourceWeft/SourceWeft](https://github.com/SourceWeft/SourceWeft)
`⭐ Stars: 429` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.3.0-rc.8](https://github.com/SourceWeft/SourceWeft/releases/tag/v0.3.0-rc.8) (2026-10-11)`

> **简介**：ChatGPT 和 NotebookLM 的开源、自托管替代方案 — 一个 AI 工作站中的代理、技能、MCP 和引用知识。您的模型，您的基础设施。免费使用 GPT 6：https://SourceWeft.com/

**💡 核心亮点更新 (中文)**：
* 修复（发布）：通过 https://github.com/SourceWeft/SourceWeft/pull/278 恢复验证的桌面发布
* 修复（发布）：通过 https://github.com/SourceWeft/SourceWeft/pull/279 中的发布 ID 验证草稿资产
* feat(web)：通过 https://github.com/SourceWeft/SourceWeft/pull/281 澄清共享设置导航

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Self-hosting files for Web/Docker, macOS and Windows installers, and Linux x64 AppImage packages.

These installers have no Apple Developer ID or Windows publisher certificate; macOS is not notarized. Operating systems may warn or block installation. Historical clients without an update key need one manual overwrite upgrade.
All application update packages have verified Tauri updater signatures. Local device execution currently requires macOS.
See docker/README.md in the self-hosting archive for installation and upgrade instructions. Translations are provided in separate README files.


## What's Changed
* fix(release): resume verified desktop publication by @QThans in https://github.com/SourceWeft/SourceWeft/pull/278
* fix(release): verify draft assets by release ID by @QThans in https://github.com/SourceWeft/SourceWeft/pull/279
* feat(web): clarify shared settings navigation by @QThans in https://github.com/SourceWeft/SourceWeft/pull/281
* fix(web): publish support email in public footer by @QThans in https://github.com/SourceWeft/SourceWeft/pull/284
* fix(desktop): recover transient update network failures by @QThans in https://github.com/SourceWeft/SourceWeft/pull/285
* chore(release): prepare v0.3.0-rc.8 by @QThans in https://github.com/SourceWeft/SourceWeft/pull/287


**Full Changelog**: https://github.com/SourceWeft/SourceWeft/compare/v0.3.0-rc.7...v0.3.0-rc.8
```
</details>

---
### 📦 [openai/codex](https://github.com/openai/codex)
`⭐ Stars: 134,025` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [rust-v0.167.0](https://github.com/openai/codex/releases/tag/rust-v0.167.0) (2026-11-06)`

> **简介**：在您的终端中运行的轻量级编码代理

**💡 核心亮点更新 (中文)**：
- 使用“codex Agents --no-daemon”打开代理命令中心。命令中心和会话选择器现在标记未读结果（#58238、#58239、#58263、#58264）。
- 从终端会话选择器在连接的后端之间切换，并在切换时保留草稿（#58280、#58457）。
- 在支持的终端上撰写时预览本地图像附件，并从可单击的脚本路径打开查看的本地图像（#58261、#58446）。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## New Features

- Open the agent command center with `codex agents --no-daemon`. The command center and session picker now mark unread results (#58238, #58239, #58263, #58264).
- Switch between connected backends from the terminal session picker and keep your drafts when switching (#58280, #58457).
- Preview local image attachments while composing on supported terminals, and open viewed local images from clickable transcript paths (#58261, #58446).
- Find API key and cloud provider options under “Sign in another way.” Enable `gcp_setup_wizard` to set up Google Cloud Vertex AI with Application Default Credentials or a credential file (#57857, #58427).
- Opt into macOS or Windows system proxy settings from `/experimental` (#58157).
- Expand patch details directly in the transcript while an approval prompt is open (#58281).

## Bug Fixes

- Saved chats stay visible after you switch model providers. If a chat can’t resume, you can read its transcript and prepare an editable prompt to continue in a new chat (#58202).
- `Ctrl+L` clears the terminal display while keeping earlier messages available through `Ctrl+T` (#58266).
- Deleting text that exposes a leading `!` keeps an ordinary draft in chat mode (#58412).
- Network approval prompts close when their requests end. Concurrent requests to the same endpoint prompt one at a time (#58350, #58351).
- Long realtime V3 conversations save completed speech to chat history as the transcript grows (#58221).
- Automatic context compaction
```
</details>

---
### 📦 [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)
`⭐ Stars: 15,430` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.4.4](https://github.com/akitaonrails/ai-memory/releases/tag/v3.4.4) (2026-11-08)`

> **简介**：用于代理编码 CLI 的长期记忆解决方案，并促进不同代理供应商之间的切换

**💡 核心亮点更新 (中文)**：
校验和 (SHA256)
````
333928cbc642ad7e649260a1ec1731a8cc182fb5a4cb109cfd5cede5f9cda651 ai内存-3.4.4-1.aarch64.rpm
3c4a2a546ff959aa89897223bfd830b12c6542e261b4ddf9825fa9a20a53a108 ai-内存-3.4.4-1.x86_64.rpm
5a3f1142b9c6c642d9fd4b7035ac46e5a652

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Checksums (SHA256)
```
333928cbc642ad7e649260a1ec1731a8cc182fb5a4cb109cfd5cede5f9cda651  ai-memory-3.4.4-1.aarch64.rpm
3c4a2a546ff959aa89897223bfd830b12c6542e261b4ddf9825fa9a20a53a108  ai-memory-3.4.4-1.x86_64.rpm
5a3f1142b9c6c642d9fd4b7035ac46e5a6526a26b6da3c24649aa8470d58088c  ai-memory-claude-plugin.zip
00877f637c01853c95db033e3f75944df96b04fa2586ce5738e0218884903f3f  ai-memory-hooks.tar.gz
5b8b9030c247b091ac2bacbf181f52f8fdba9d4ed47cdef23faab874d4c94d9f  ai-memory-install-hooks
034c290de7e78b1c969a02135e054bc7a661bb8654c77939123bf0a6b5aa58fb  ai-memory-linux-aarch64.tar.gz
2d69626c3f2ca7498b43da7fe733162ac798bffa7d088319bde1808c5d62ab59  ai-memory-linux-x86_64.tar.gz
498f07cd5581516f2987fe65b9e266d6f5a30066ec99a2e91a897e18f8507e64  ai-memory-macos-aarch64.tar.gz
6ec4661e298434e3c321e0d6c42da97fad5b6b6b03237ee42633c34ca40d3893  ai-memory-macos-x86_64.tar.gz
75844776d9250fd00daa6dd8d5852868163569d3e767daa991bc6e36b2706cce  ai-memory-windows-x86_64.zip
6a91c44ffa2e85d3b5a6ce26a4ccff0286b91d08d276d2bb4d47c346b036ee8b  ai-memory-wrapper.cmd
5e405aa237a2399f13084f71ae89545cbca77683c8251b4c4572cb51aedc8de4  ai-memory-wrapper.ps1
982cfeb1515a062fdb348e4622d130682660d30a1ce104d8ff0a11d997d409a7  ai-memory-wrapper
c05aedd9a572d5807986910d5099adac132ae558d677bc2d0f64a6d53eaf0d3b  install.ps1
c4eed9675ebeadda0f68fa952236c31a6f42ddce03a26aa9756539ccb22b83d5  install.sh
```

## Install
```bash
# Linux/macOS, no root: checksum-verified release binary under ~/.local, then one-step set
```
</details>

---
### 📦 [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)
`⭐ Stars: 57,248` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.7.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.7.2) (2026-11-06)`

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
`⭐ Stars: 110,402` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.6.1](https://github.com/Panniantong/Agent-Reach/releases/tag/v1.6.1) (2026-11-01)`

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
`⭐ Stars: 5,720` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.8.0](https://github.com/microsoft/skill-recorder/releases/tag/v0.8.0) (2026-11-02)`

> **简介**：桌面应用程序，记录您的屏幕上工作会话，并使用 GitHub Copilot SDK 将其重建为意图 + 有序步骤，然后为 Microsoft Autopilot（例如 Scout、Microsoft Copilot Cowork 或 Copilot Studio）构建可重用的技能或自动化。

**💡 核心亮点更新 (中文)**：
- **导入现有录制文件：** 使用录制旁边的较小文件夹按钮选择本地 MP4 或 WebM，例如下载的 Teams 演示。
- 在继续之前检查实际的视频和音频解码。不支持的编解码器和无效媒体将被拒绝并给出解释；不需要转换器、独立 FFmpeg 安装或新的应用程序依赖项。
- 添加可选详细信息来解释任务、补充演示或建议其出现位置。支持将详细信息留空。时间戳指导人工智能；他们不会修剪录音。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Source-only release

Skill Recorder 0.8.0 is published from commit [`505c97ae47be5642c0e1b44ebb8d1c1530c298fa`](https://github.com/microsoft/skill-recorder/commit/505c97ae47be5642c0e1b44ebb8d1c1530c298fa).

This release is **source-only**. No installers or portable binaries are attached. GitHub's generated archives contain the tagged repository source only.

## Changes

- **Import an existing recording:** use the smaller folder button beside Record to select a local MP4 or WebM, such as a downloaded Teams demonstration.
- Check actual video and audio decoding before proceeding. Unsupported codecs and invalid media are rejected with an explanation; no converter, standalone FFmpeg installation, or new application dependency is required.
- Add optional details to explain the task, supplement the demonstration, or suggest where it appears. Leaving details empty is supported. Timestamps guide the AI; they do not trim the recording.
- Transcribe audio locally with the existing Whisper model, then reconstruct activities from the video, speech, and user details. Silent videos and videos without audio are supported; transcription failures stop analysis so they can be retried.
- Reuse the existing activity-review and skill-building flow: edit, reorder, add or remove activities, then create, review, and install/export a skill.
- Preserve live screen recording, its settings, and its event-first analysis behavior.
- Keep the original recording untouched. Store a local ses
```
</details>

---
### 📦 [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model)
`⭐ Stars: 66,630` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.8.3](https://github.com/Ebony-Vinyl/dsh-our-free-model/releases/tag/v2.8.3) (2026-11-08)`

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
`⭐ Stars: 28,677` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.3.1](https://github.com/hypit-ai/hypit/releases/tag/v0.3.1) (2026-10-09)`

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
`⭐ Stars: 21,148` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.0.10](https://github.com/HBAI-Ltd/Toonflow-app/releases/tag/v2.0.10) (2026-11-05)`

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
`⭐ Stars: 444,765` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [rea-agents-6.8.0](https://github.com/morluto/rea/releases/tag/rea-agents-6.8.0) (2026-10-25)`

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
`⭐ Stars: 17,163` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v4.0.11](https://github.com/chatfire-AI/huobao-drama/releases/tag/v4.0.11) (2026-11-05)`

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
`⭐ Stars: 32,680` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.1.3373](https://github.com/yetone/magpie/releases/tag/v0.1.3373) (2026-11-09)`

> **简介**：每个代理的模型。一处。来自菜单栏的 DeepSeek 上的 Codex、Kimi 上的 Claude Code。

**💡 核心亮点更新 (中文)**：
- 更新了视频生成设置以使用 Magpie Image 模型创建视频。
- **macOS（Apple Silicon）：** `magpie-darwin-arm64.dmg`
- **macOS（英特尔）：** `magpie-darwin-amd64.dmg`

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Improvements
- Updated video generation settings to use the Magpie Image model for creating videos.

### Install

Download from [usemagpie.ai](https://usemagpie.ai), or `curl -fsSL https://usemagpie.ai/install.sh | sh`. An installed magpie updates itself.

- **macOS (Apple Silicon):** `magpie-darwin-arm64.dmg`
- **macOS (Intel):** `magpie-darwin-amd64.dmg`
- **Windows:** `magpie-windows-amd64.exe` (ARM: `magpie-windows-arm64.exe`)
- **Linux:** `magpie-linux-amd64` / `magpie-linux-arm64` (needs GTK 3 and WebKitGTK 4.1)
- **Terminal only:** `magpie-cli-<os>-<arch>`

<!-- lang:zh -->

## 改进
- 更新了视频生成设置，以使用 Magpie Image 模型来创建视频。

### 安装

从 [usemagpie.ai](https://usemagpie.ai) 下载，或运行 `curl -fsSL https://usemagpie.ai/install.sh | sh`。已安装的 magpie 会自动更新。



---
The same release, and the feed magpie updates from: https://github.com/yetone/magpie-releases/releases/tag/v0.1.3373
```
</details>

---
### 📦 [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
`⭐ Stars: 261,857` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.23.0](https://github.com/NousResearch/hermes-agent/releases/tag/v0.23.0) (2026-11-05)`

> **简介**：与您共同成长的代理商

**💡 核心亮点更新 (中文)**：
- **浏览器选项卡中的桌面工作区** — 新的 Web 应用程序从您自己的网关提供完整的桌面工作区：相同的聊天、群聊、插件和设置，在网络上的任何浏览器中或通过登录的公共 URL 后面。 Docker 镜像和 Nix 包提供了它。默认关闭；使用“webapp.enabled”或“设置”中的“Web 访问”将其打开。 （[#141864]（https://github.com/NousResearch/hermes-agent/pull/141864），[#145598]（https://github.com/NousResearch/hermes-agent/pull/145598），[#145536]（https://github.com/NousResearch/hermes-agent/pull/145536）， [#145072](https://github.com/NousResearch/hermes-agent/pull/145072), [#145153](https://github.com/NousResearch/hermes-agent/pull/145153) — , , ,
- **一个网关拥有每一次对话** — 之前，CLI、TUI、桌面、编辑器 (ACP)、消息传递机器人和 cron 都可以针对同一个聊天运行自己的代理副本，这就是消息被写入两次或在表面之间丢失的原因。现在，每台计算机都运行一个拥有每个会话的网关，并且每个表面都作为客户端附加到它：您在任何地方打开的聊天都是同一个聊天，具有一个队列和一个历史记录。您甚至可以从桌面引导或编辑排队的提示，而无需它运行两次。 ([#106742](https://github.com/NousResearch/hermes-agent/pull/106742), [#140334](https://github.com/NousResearch/hermes-agent/pull/140334) — ,
- **终端中的图片** - 当您粘贴图像或工具截取屏幕截图时，CLI 和 TUI 现在会在聊天中直接绘制它，而不是打印文件路径：kitty 和 Ghostty（CLI 和 TUI）以及 iTerm2、WezTerm 和 Konsole (CLI) 中的真实像素，其他地方的彩色块，以及打开图像支持时 VS Code 终端中的全分辨率。 （[#147293]（https://github.com/NousResearch/hermes-agent/pull/147293），[#148874]（https://github.com/NousResearch/hermes-agent/pull/148874）-

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# Hermes Agent v0.23.0

**Release Date:** November 5, 2026
**Since v0.22.0:** ~10,080 commits · ~1,950 merged PRs · ~8,720 files changed · ~725,200 insertions · ~201,400 deletions · **~850 issues closed** · 666 contributors

> **The Hearth Release.** In the old hymns Hermes kept the threshold and Hestia kept the hearth, and the two were honored side by side. v0.22.0 got newcomers through the door; v0.23.0 builds the fire they gather around. The headline: your whole Desktop workspace now opens in a browser tab, served by your own gateway. Underneath it, every conversation lives in one place: a single gateway owns each session, and the CLI, TUI, Desktop, editors, bots and cron all sit down at the same table instead of each running its own agent. From that one hearth, Desktop keeps every machine you run Hermes on connected at once, Group Chats route their own conversations, and the terminal finally draws your images inline and lets you rewind a conversation. Around it: plugins that keep themselves updated, price tags and spend limits on paid MCP tools, pluggable delegation, a plugin catalog that grew from about 600 to over 1,050 entries, a leaner built-in skill set, and a long run of memory and latency work for long-lived gateways. This release rolls up and fully documents the v0.22.1–v0.22.7 patch releases.

<!-- HERMES_BUILDS_TABLE -->

---

## ✨ Highlights

- **Your Desktop workspace in a browser tab** — The new Webapp serves the full Desktop workspace from your own gateway:
```
</details>

---
### 📦 [Makememo/MemoAI](https://github.com/Makememo/MemoAI)
`⭐ Stars: 1,081` &nbsp;|&nbsp; `💻 语言: Other` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.8.10](https://github.com/Makememo/MemoAI/releases/tag/v1.8.10) (2026-11-03)`

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
`⭐ Stars: 11,994` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.12.852](https://github.com/genspark-ai/genoffice/releases/tag/v0.12.852) (2026-11-04)`

> **简介**：免费的开源 AI Office 套件：带有内置 AI 代理的文档、表格、幻灯片、PDF、Markdown 和 HTML 编辑器，以及“genoffice”CLI 和代理技能，以便 Claude Code、Codex 和 Cursor 可以在本地创建和编辑真正的 .docx/.xlsx/.pptx 文件。带上你自己的钥匙。 macOS、Windows 和 Linux。

**💡 核心亮点更新 (中文)**：
- **文档：** 旧版 .doc 导入更加完善 - 嵌套和浮动表格、文本列、页码和边框、单元格阴影、图片裁剪、字体和 Bidi 文本；格式标记显示分页符、换行符和分节符（由 报告；可以单击文本后面的封面图片并保留在其页面上，并且锚定在表格单元格中的图片保留在其中（由 报告；Word 样式按钮和样式窗格；双击选择 Word 之类的单词；嵌套的 PAGE 字段保留其父级 ，由 报告；未更改的表格在保存时保持字节相同；邮件合并获得标签和信封；泰语、韩语、希伯来语和阿拉伯语面孔、表格在 100 个文档的比较中，边框、锚定图片和 CJK 间距的布局更接近 Word。
- **工作表：**旧版 .xls 工作簿保留单元格格式（由 报告）；保存刷新每个公式缓存，由 报告；排序的公式保持指向自己的行；外部链接面板和查询刷新；冻结窗格在流式滚动中幸存。
- **幻灯片：** 旧版 .ppt 导入，第 1 阶段，带有可编辑文本； MathType 方程预览正确渲染（由 报告；绘图选项卡上的 Word 样式笔库；打印对话框提供打印机、副本和双面打印。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
GenOffice v0.12.852 stable desktop installers.

## What's New

- **Docs:** legacy .doc import rounds out — nested and floating tables, text columns, page numbering and borders, cell shading, picture crops, fonts and bidi text; formatting marks show page, wrap and section breaks (reported by @soulmate543748); cover pictures behind text can be clicked and stay on their page, and pictures anchored in a table cell stay inside it (reported by @hwang824); Word-style Styles button and Styles pane; double-click selects the word like Word; nested PAGE fields keep their parent (@tokg-venv, reported by @lkopenec); untouched tables stay byte-identical on save (@tokg-venv); mail merge gains labels and envelopes (@tokg-venv); Thai, Korean, Hebrew and Arabic faces, table borders, anchored pictures and CJK spacing lay out closer to Word across a 100-document comparison.
- **Sheets:** legacy .xls workbooks keep cell formatting (reported by @emrahoksak); saving refreshes every formula cache (@tokg-venv, reported by @NoeFaucher); sorted formulas keep pointing at their own row (@NoeFaucher); external links panel and query refresh (@tokg-venv); freeze panes survive streamed scrolling.
- **Slides:** legacy .ppt import, stage 1 with editable text (@tokg-venv); MathType equation previews render correctly (reported by @soulmate543748); Word-style pen gallery on the Draw tab; print dialog offers printer, copies and duplex (@tokg-venv).
- **PDF:** PNG/JPG export moves into the PDF Converter menu; annot
```
</details>

---
### 📦 [ruvnet/RuView](https://github.com/ruvnet/RuView)
`⭐ Stars: 103,116` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [ruview-harness-v0.9.2](https://github.com/ruvnet/RuView/releases/tag/ruview-harness-v0.9.2) (2026-10-12)`

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
`⭐ Stars: 25,403` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [@pascal-app/cli@1.0.7](https://github.com/pascalorg/editor/releases/tag/%40pascal-app/cli%401.0.7) (2026-11-08)`

> **简介**：适用于 AECO、扫描到 BIM 的开源 3D 建筑软件。代理友好、浏览器优先、MCP、CLI。

**💡 核心亮点更新 (中文)**：
`@pascal-app/cli@1.0.7` 的 Pascal Web 编辑器运行时。当命令第一次启动编辑器时，CLI 会下载“pascal-web-runtime-1.0.7.ta​​r.gz”，并根据 npm 包内发布的摘要进行验证。离线安装可以通过t

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
The Pascal web editor runtime for `@pascal-app/cli@1.0.7`. The CLI downloads `pascal-web-runtime-1.0.7.tar.gz` the first time a command starts the editor and verifies it against the digest published inside the npm package. Offline installs can pass the archive directly: `pascal editor --runtime pascal-web-runtime-1.0.7.tar.gz`.
```
</details>

---
### 📦 [librepods-org/librepods](https://github.com/librepods-org/librepods)
`⭐ Stars: 30,667` &nbsp;|&nbsp; `💻 语言: Kotlin` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.0.4](https://github.com/librepods-org/librepods/releases/tag/v1.0.4) (2026-10-16)`

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
`⭐ Stars: 40,956` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.15.1](https://github.com/linshenkx/prompt-optimizer/releases/tag/v2.15.1) (2026-11-03)`

> **简介**：人工智能提示优化器，用于编写更好的提示并获得更好的人工智能结果。

**💡 核心亮点更新 (中文)**：
- 恢复桌面和窄屏幕上可读的功能模型选择器。
- 在全屏和表面预览执行错误中展开单个 HTML/SVG 预览。
- 直接在 Arena 中从 Prompt Garden 打开常见模型评估提示。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## English

### Summary

This patch fixes Function Models selectors collapsing into vertically wrapped text. It also includes the shared HTML/SVG preview fixes and Prompt Garden evaluation-prompt integration already merged after v2.15.0.

### Highlights

- Restore readable Function Models selectors on desktop and narrow screens.
- Expand a single HTML/SVG preview in fullscreen and surface preview execution errors.
- Open common model-evaluation prompts from Prompt Garden directly in Arena.

### Product Updates

#### Desktop

- Apply the shared selector layout and HTML/SVG preview improvements.

#### Web

- Add the evaluation-prompt entry in Arena and support imports from Prompt Garden, including selected example variables and reference images.
- Preserve test columns and previous results when importing; imports do not automatically start model requests.

#### Extension

- Apply the shared selector and preview improvements, including error reporting from the packaged preview sandbox.

#### Core/Infra

- Reuse existing session and preview components for Garden imports and result rendering.

### Fixes

- Give Function Models selectors a stable layout wrapper so scoped width rules reach the intended element; keep placeholder text on one line.
- Recognize standalone SVG and SVG code fences, and fit fixed-size SVG graphics to the preview viewport.
- Let a single HTML/SVG artifact use the available fullscreen area.
- Display errors reported by preview scripts, modules, resources and
```
</details>

---
### 📦 [RSSNext/Folo](https://github.com/RSSNext/Folo)
`⭐ Stars: 39,250` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [desktop/v1.17.0](https://github.com/RSSNext/Folo/releases/tag/desktop/v1.17.0) (2026-11-02)`

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
`⭐ Stars: 51,563` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [0.31.5](https://github.com/roboflow/supervision/releases/tag/0.31.5) (2026-11-05)`

> **简介**：我们为您编写可重复使用的计算机视觉工具。 💜

**💡 核心亮点更新 (中文)**：
- **LineZone** 对穿过线时隐藏几帧的对象进行计数。
- 阿拉伯语和希伯来语标签使用新的“rtl”额外功能正确呈现。
- Oriented-box IoU、NMS 和指标现在在 OpenCV 安装上使用精确的 Clipper。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# v0.31.5: Line counts through occlusion, the exact clipper for oriented boxes, and right-to-left labels

Right-to-left labels, line counting that survives occlusion, and a batch of edge-case fixes across annotators, exports and the NumPy fallback.

- **LineZone** counts objects that are hidden for a few frames while they cross the line.
- Arabic and Hebrew labels render correctly with the new `rtl` extra.
- Oriented-box IoU, NMS and metrics now use the exact clipper on OpenCV installs.
- Annotating a Pillow image keeps its transparency and untouched pixels.
- Heat maps and ellipse halos now work on grayscale scenes.

It's a drop-in upgrade, but check the Migration guide if you count line crossings, score-oriented boxes on OpenCV, or compare stored outputs.

## ✨ Spotlights / highlights

### Right-to-left labels with the new `rtl` extra

`sv.RichLabelAnnotator` now draws Arabic and Hebrew labels correctly on RGB and RGBA images when the new `rtl` extra is installed. Pillow only joins Arabic letters and orders right-to-left text when it's built with Raqm, and most Windows installs and many containers lack it. There, `"سيارة 0.92"` came out as isolated letters in reverse order. Lines with Arabic or Hebrew are now shaped in the label's font, using fallback Arabic and Hebrew fonts from `khatt` for missing glyphs, and right-aligned in the background box. Other image modes fall back to Pillow, with a warning that suggests RGB or RGBA when Raqm is missing. Without th
```
</details>

---
### 📦 [MetaCubeX/mihomo](https://github.com/MetaCubeX/mihomo)
`⭐ Stars: 35,620` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.19.33](https://github.com/MetaCubeX/mihomo/releases/tag/v1.19.33) (2026-10-21)`

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
### 📦 [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev)
`⭐ Stars: 157,268` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.5.10](https://github.com/clash-verge-rev/clash-verge-rev/releases/tag/v2.5.10) (2026-11-03)`

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
`⭐ Stars: 79,226` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.1.916-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.916-beta) (2026-11-06)`

> **简介**：用于运行和训练法学硕士和扩散模型的本地 UI。支持 GGUF、MLX、Qwen3.8、DeepSeek-V4.1、MiniMax-H3、Gemma 4、FLUX 等。

**💡 核心亮点更新 (中文)**：
- **大量性能修复**，下周将推出更多 Glass 主题优化
- **玻璃主题修复**不再模糊，更好的渲染，更多选项
- **统一内存卸载**现在可以正确地适用于大型模型

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
This release brings large performance fixes across Unsloth: faster typing and search in long chats, faster image/video loads, two-GPU image/video gen. It also adds separate browsers for each chat, floating browser window.

## Highlights

- **Large performance fixes** with more Glass theme optimizations coming next week
- **Glass theme fixes** no more blur, better rendering, more options
- **Unified memory offloading** now properly works for big models
- **Separate browsers for each chat** - Multiple chats can now run their own browser individually
- **Floating browser** you can move and resize over the chat & let the model do it's thing
- **Dynamic V3.1 Qwen3.8-Flash** - 50% less token use, 15% more accurate
- **Two-GPU image and video** up to 2x faster on matching NVIDIA cards
- **Faster chat search and deleting** - search and delete chats much faster
- **Stable diffusion image/video models loads** up to 40% faster
- **LTX-2.5 video** much faster for new prompts on 16 to 24 GB GPUs

## Chat performance

- Typing in a long chat no longer lags when a Glass theme or chat background is on.
- Chat search stays fast on very long histories instead of failing to load.
- Clearing and deleting chats is much faster on large histories.
- The first use of voice or audio features after launch no longer freezes a streaming reply for seconds.
- Read aloud with the **Unsloth model** engine no longer waits seconds on a model lookup before speaking.
- Glass themes over a
```
</details>

---
### 📦 [arc53/DocsGPT](https://github.com/arc53/DocsGPT)
`⭐ Stars: 18,366` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [1.1.0](https://github.com/arc53/DocsGPT/releases/tag/1.1.0) (2026-10-25)`

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
`⭐ Stars: 84,495` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.3.2](https://github.com/lobehub/lobehub/releases/tag/v2.3.2) (2026-11-06)`

> **简介**：🤯 LobeHub - 您团队中的超级代理。将超级代理添加到您的团队已使用的聊天中。他们自己承担工作，并且每周都会变得更好。

**💡 核心亮点更新 (中文)**：
- **任务标签** — 通过 Web UI、代理工具或 CLI 为任务添加标签、按标签过滤并按标签对视图进行分组。 （＃22176，＃22175）
- **撤消批量任务操作** — 批量操作通过撤消立即应用，删除的任务将进入回收站。 (#22167)
- **对话中的 MCP 应用程序** — 来自 MCP 应用程序的交互式视图在对话内呈现。 (#21231)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Release v2.3.2

From PR #22430: https://github.com/lobehub/lobehub/pull/22430

### Summary

Contribution source: AI-assisted

# 🚀 LobeHub Release (20261106)

**Release Date:** November 6, 2026  
**Since v2.3.1:** 127 merged PRs · 11 contributors

> Everyday work gets easier to organize and easier to undo: tasks gain labels and a recycle bin, channels behave like real conversations, and interactive MCP views open right inside the chat.

---

## ✨ Highlights

- **Task labels** — Label tasks, filter by label and group views by label, from the Web UI, Agent tools or the CLI. (#22176, #22175)
- **Undo for batch task actions** — Batch actions apply instantly with an undo, and deleted tasks go to a recycle bin. (#22167)
- **MCP Apps in conversations** — Interactive views from MCP Apps render inside the conversation. (#21231)
- **Channels in the message list** — Conversations open as channels, messages appear as soon as you send them, mentioned members get notified, and @mentioning someone outside a channel invites them. (#22205, #22325, #22222, #22294)
- **GitHub Copilot CLI as a heterogeneous Agent** — Run Copilot CLI alongside the existing local Agents. Codex also gains native questions and Speed selection based on what the machine supports. (#22195, #22287, #22264)
- **Managed cloud devices** — Connect one with `lh connect --managed`, follow its phases in the device list, and let it wake before work is dispatched. (#22269, #22275, #22274, #22276)
- **Richer chat input** — Drag
```
</details>

---
### 📦 [hiddify/hiddify-app](https://github.com/hiddify/hiddify-app)
`⭐ Stars: 33,824` &nbsp;|&nbsp; `💻 语言: Dart` &nbsp;|&nbsp; `🏷️ 最新版本: [v5.5.5](https://github.com/hiddify/hiddify-app/releases/tag/v5.5.5) (2026-11-04)`

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
`⭐ Stars: 30,005` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v4.17.4](https://github.com/labring/FastGPT/releases/tag/v4.17.4) (2026-11-05)`

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
`⭐ Stars: 9,934` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.3.2](https://github.com/yihong0618/bilingual_book_maker/releases/tag/v1.3.2) (2026-10-30)`

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
`⭐ Stars: 37,406` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.4.2](https://github.com/1Panel-dev/1Panel/releases/tag/v2.4.2) (2026-10-30)`

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
`⭐ Stars: 29,036` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v6.14.4](https://github.com/invoke-ai/InvokeAI/releases/tag/v6.14.4) (2026-11-03)`

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
`⭐ Stars: 39,637` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.0.2](https://github.com/The-Vibe-Company/quivr/releases/tag/v2.0.2) (2026-10-30)`

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
`⭐ Stars: 160,723` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [1.19.0](https://github.com/langgenius/dify/releases/tag/1.19.0) (2026-11-04)`

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
`⭐ Stars: 25,026` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.6.55](https://github.com/nextai-translator/nextai-translator/releases/tag/v0.6.55) (2026-11-02)`

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
`⭐ Stars: 149,241` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [langchain-core==1.7.6](https://github.com/langchain-ai/langchain/releases/tag/langchain-core%3D%3D1.7.6) (2026-11-05)`

> **简介**：代理工程平台。

**💡 核心亮点更新 (中文)**：
自 langchain-core==1.7.5 以来的变化

版本（核心）：1.7.6 (41698)
perf(core)：累积可运行流时合并流式“AIMessageChunk”一次（41697）
perf(core): 阻止 `parse_partial_json` 一次重试一个字符 (41467)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Changes since langchain-core==1.7.5

release(core): 1.7.6 (#41698)
perf(core): merge streamed `AIMessageChunk`s once when accumulating runnable streams (#41697)
perf(core): stop `parse_partial_json` from retrying one character at a time (#41467)
```
</details>

---
### 📦 [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)
`⭐ Stars: 187,956` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [autogpt-platform-beta-v0.11.1](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.11.1) (2026-11-06)`

> **简介**：AutoGPT 的愿景是为每个人提供易于使用和构建的人工智能。我们的使命是提供工具，以便您可以专注于重要的事情。

**💡 核心亮点更新 (中文)**：
- **#11220** - 支持输入节点和触发节点（通过
- **#14991** - 在副驾驶聊天中将技能作为 /commands 运行并带有参数（通过
- **#16582** - 使后台子任务真正起作用并返回聊天（通过

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 🔥 What's New?

### ⚠️ Breaking Changes

- **#16416** - Self-hosted installs: `.env.default` no longer ships a Web Push (VAPID) key pair, and the backend no longer sends push notifications with the old shipped pair. Run `make init-env` to generate a pair for your install; the single-container image generates its own on first boot. Replacing the pair invalidates existing push subscriptions. `NEXT_PUBLIC_VAPID_PUBLIC_KEY` can stay blank, and the frontend then uses the backend's key (by @ntindle)

### New Features

- **#11220** - Support input nodes alongside trigger nodes (by @Pwuts)
- **#14991** - Run skills as /commands with arguments in the copilot chat (by @ntindle)
- **#16582** - Make background subtasks real work that returns to the chat (by @ntindle)
- **#16506** - Warn canceled trials 3 days and 1 day before access ends (by @Torantulino)
- **#16622** - Make the email-change approval email clear about both addresses (by @Torantulino)
- **#15488** - Redesign the k6 load tests around real user workloads (by @ntindle)
- **#16605** - Add Tencent Hy4 to the LLM catalog (by @ntindle)

### New Blocks

- **#16561** - Add Firecrawl Alexandria data tool blocks (by @Torantulino)
- **#16395** - Bring the Exa integration up to date with Exa's current API (by @Torantulino)
- **#16393** - Add Treg blocks for people, company and web data (by @Torantulino)

### Enhancements

- **#16446** - Creating a GitHub repository asks first in Auto mode (by @Pwuts)
- **#14377** - Drop redundant sc
```
</details>

---
### 📦 [rockbenben/ChatGPT-Shortcut](https://github.com/rockbenben/ChatGPT-Shortcut)
`⭐ Stars: 8,924` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v4.5.2](https://github.com/rockbenben/ChatGPT-Shortcut/releases/tag/v4.5.2) (2026-11-04)`

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
`⭐ Stars: 2,869` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [userscript-v2.38.3](https://github.com/pionxzh/chatgpt-exporter/releases/tag/userscript-v2.38.3) (2026-11-04)`

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
`⭐ Stars: 47,848` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [2.2.2](https://github.com/zhayujie/CowAgent/releases/tag/2.2.2) (2026-10-30)`

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
`⭐ Stars: 22,314` &nbsp;|&nbsp; `💻 语言: Shell` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.5.40](https://github.com/mack-a/v2ray-agent/releases/tag/v3.5.40) (2026-11-07)`

> **简介**：Xray、Tuic、hysteria2、sing-box 八合一一键脚本

**💡 核心亮点更新 (中文)**：
fix(xray): 修复 Xray 安装 Hysteria2 无法查看账号
fix(脚本):修复 Hysteria2 订阅缺少上下行速率

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
fix(xray): 修复 Xray 安装 Hysteria2 无法查看账号
fix(脚本):修复 Hysteria2 订阅缺少上下行速率
```
</details>

---
### 📦 [electerm/electerm](https://github.com/electerm/electerm)
`⭐ Stars: 15,577` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v5.9.0](https://github.com/electerm/electerm/releases/tag/v5.9.0) (2026-11-07)`

> **简介**：📻免费开源终端/ssh/sftp/ftp/telnet/串口/RDP/VNC/Spice客户端(Linux, Mac, Windows, Android, HarmonyOS, iOS)

**💡 核心亮点更新 (中文)**：
- SSH：支持 PKCS#8、PPK v3 和 FIDO2 密钥 (ssh2 1.23.0)，改进 MFA 支持 (#4554)
- MCP：添加只读命令规则工具，被拒绝的命令现在指向它（#4699）
- 当 GitHub 无法访问时，从 GitHub 安装的小部件现在会回退到mirror.electterm.org 和 jsDelivr；应用内更新程序使用相同的镜像

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
### Major updates

- Fix terminal rendering after WebGL context loss: fall back to the DOM renderer and keep sessions alive (#4702) by @forever765
- Widget: Support password manager: an installed widget can supply passwords for SSH/ftp/VNC/Spice/Telnet/RDP bookmarks (KeePassXC ready), with a per-bookmark opt-in (#4705) by @mkneppe
- UX: Support set icon for custom bookmark/bookmark group by @xinxingi
- Widget: Widgets can offer bookmarks to import, with an import result report and a warning about embedded secrets (#4703) by @mkneppe
- Support create a private key in the SSH bookmark form (#4554)
- Editor: support markdown preview in the built-in editor (#4666)

### New features/UI/Updates

- SSH: support PKCS#8, PPK v3 and FIDO2 keys (ssh2 1.23.0), improve MFA support (#4554)
- MCP: add a read-only command rules tool, and a rejected command now points at it (#4699) by @ifyh-W
- Widget install from GitHub now falls back to mirror.electerm.org and jsDelivr when GitHub is unreachable; the in-app updater uses the same mirror
- RDP: can check host reachability before connecting, show readable connect errors (#4685) by @mkneppe
- SSH: a stale or blank private key path no longer blocks a password login (#4684) by @mkneppe
- Use static default local bookmarks, so app start faster (#4672)
- Bookmark import: bookmarks without a category are collected into a standalone category
- VNC: show why a connection failed, with a hint for RealVNC's RA2 security type that no ope
```
</details>

---
### 📦 [XTLS/Xray-core](https://github.com/XTLS/Xray-core)
`⭐ Stars: 42,744` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v26.11.9](https://github.com/XTLS/Xray-core/releases/tag/v26.11.9) (2026-11-09)`

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
`⭐ Stars: 9,619` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [v154.0.8037.49-5](https://github.com/klzgrad/naiveproxy/releases/tag/v154.0.8037.49-5) (2026-10-22)`

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

### 📦 [RongleCat/grok-bot-anywhere](https://github.com/RongleCat/grok-bot-anywhere)
`⭐ Stars: 48` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.1.4](https://github.com/RongleCat/grok-bot-anywhere/releases/tag/v0.1.4) (2026-11-06)`

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
`⭐ Stars: 1,576` &nbsp;|&nbsp; `💻 语言: Swift` &nbsp;|&nbsp; `🏷️ 最新版本: [spektralab-v2.2.2](https://github.com/JamesQiu2005/SpektraLab/releases/tag/spektralab-v2.2.2) (2026-11-09)`

> **简介**：SpektraLab — macOS 电影和打印模拟器。 SwiftUI 应用程序 + Metal/C++ 渲染引擎，链接进来，运行时没有 Python。 andreavolpato/spektrafilm 的一个分支。

**💡 核心亮点更新 (中文)**：
- **Canvas Color Space (Canvas Color Space) 位于 Develop 的···菜单中。** 2.2.1 有该功能，但 Mac 的菜单没有显示。
- **用户指南**，中英文：[docs/USER-GUIDE.md](https://github.com/JamesQiu2005/SpektraLab/blob/main/docs/USER-GUIDE.md) · [文档/USER-GUIDE.zh-CN.md](https://github.com/JamesQiu2005/SpektraLab/blob/main/docs/USER-GUIDE.zh-CN.md)。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
SpektraLab 2.2.2 for the Mac.

- **Canvas Colour Space (画布色域) is in Develop's ··· menu.** 2.2.1 had the feature but the Mac's menu did not show it.
- **The user guide**, in English and Chinese: [docs/USER-GUIDE.md](https://github.com/JamesQiu2005/SpektraLab/blob/main/docs/USER-GUIDE.md) · [docs/USER-GUIDE.zh-CN.md](https://github.com/JamesQiu2005/SpektraLab/blob/main/docs/USER-GUIDE.zh-CN.md).

Everything in [2.2.1](https://github.com/JamesQiu2005/SpektraLab/releases/tag/spektralab-v2.2.1): the Digital Intermediate (数字中间片), the Export preview in the recipe's colour space, agents through `SpektraLab cli` and MCP, Check for Updates.

**Download:** `SpektraLab-2.2.2-universal.dmg` (Apple silicon, macOS 15 or later; the DMG is universal, but Intel Macs are untested). Signed with Developer ID and notarised by Apple.
SHA-256 `b6a5356f8faaec922b425172f3506e18b21c8c9488cdad29e9671f6ac4ee2c0a`
```
</details>

---
### 📦 [robbietilton/Compositor](https://github.com/robbietilton/Compositor)
`⭐ Stars: 18,541` &nbsp;|&nbsp; `💻 语言: Swift` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.6.6](https://github.com/robbietilton/Compositor/releases/tag/v1.6.6) (2026-11-08)`

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
`⭐ Stars: 63,902` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v32.6.10](https://github.com/jgraph/drawio-desktop/releases/tag/v32.6.10) (2026-11-04)`

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
`⭐ Stars: 96,085` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.3.0](https://github.com/Stirling-Tools/Stirling-PDF/releases/tag/v3.3.0) (2026-11-05)`

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
`⭐ Stars: 40,181` &nbsp;|&nbsp; `💻 语言: Java` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.27.2](https://github.com/halo-dev/halo/releases/tag/v2.27.2) (2026-11-02)`

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
`⭐ Stars: 4,059` &nbsp;|&nbsp; `💻 语言: PHP` &nbsp;|&nbsp; `🏷️ 最新版本: [2.4.2](https://github.com/zyx0814/dzzoffice/releases/tag/2.4.2) (2026-10-22)`

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
`⭐ Stars: 4,806` &nbsp;|&nbsp; `💻 语言: C#` &nbsp;|&nbsp; `🏷️ 最新版本: [4.16.11-Installer](https://github.com/emoacht/Monitorian/releases/tag/4.16.11-Installer) (2026-11-08)`

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
`⭐ Stars: 14,690` &nbsp;|&nbsp; `💻 语言: PowerShell` &nbsp;|&nbsp; `🏷️ 最新版本: [v11.8.50.0](https://github.com/YerongAI/Office-Tool/releases/tag/v11.8.50.0) (2026-10-18)`

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
`⭐ Stars: 3,007` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.2.12](https://github.com/TDesktop-x64/tdesktop/releases/tag/v1.2.12) (2026-11-07)`

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
`⭐ Stars: 195,214` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [1.145.2](https://github.com/microsoft/vscode/releases/tag/1.145.2) (2026-11-06)`

> **简介**：视觉工作室代码

**💡 核心亮点更新 (中文)**：
https://code.visualstudio.com/updates/v1_145

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
https://code.visualstudio.com/updates/v1_145
```
</details>

---

## <span id="-实用开源精选">📦 实用开源精选</span>

### 📦 [a3974892-cmd/wakeloom](https://github.com/a3974892-cmd/wakeloom)
`⭐ Stars: 60` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.21.4](https://github.com/a3974892-cmd/wakeloom/releases/tag/v1.21.4) (2026-11-08)`

> **简介**：暂无项目描述

**💡 核心亮点更新 (中文)**：
- 本次仅发布 Windows 版本。Linux 等待用户测试，暂不提供安装包或自动更新清单。
- 优化字体、圆角、留白和浅深色外观，新增原创 W 标志，将导航编号改为图标。
- 修正大模型 API 设置区域的字体、边距及窄窗口横向溢出。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
- 本次仅发布 Windows 版本。Linux 等待用户测试，暂不提供安装包或自动更新清单。
- 优化字体、圆角、留白和浅深色外观，新增原创 W 标志，将导航编号改为图标。
- 修正大模型 API 设置区域的字体、边距及窄窗口横向溢出。
- 新增诊断日志：自动保存运行过程和异常，支持搜索、筛选、预览、复制与文件导出，重启后保留。
- 日志过滤常见凭据，不附带配置、聊天或附件；分享前可预览检查。
- 本地启动增加分步骤日志、有限重试、超时及下载校验；持续网络故障仍可能导致失败。
- 将源码和测试集中到 app 目录，精简仓库首页，保留用户数据兼容性。
- 关闭旧程序后运行新版即可；遇到异常可从左侧「日志」复制诊断信息。

历史版本说明见 [GitHub Releases](https://github.com/a3974892-cmd/wakeloom/releases)。
```
</details>

---
### 📦 [storytold/craft-anything](https://github.com/storytold/craft-anything)
`⭐ Stars: 23,349` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.5.0](https://github.com/storytold/craft-anything/releases/tag/v0.5.0) (2026-11-06)`

> **简介**：制作任何东西：了解任何软件的工作原理，并制作自己的软件。

**💡 核心亮点更新 (中文)**：
* 让原生 OpenCode 运行 Craft Anything 工具并通过 https://github.com/storytold/craft-anything/pull/800 显示其工具调用
* 通过 https://github.com/storytold/craft-anything/pull/767 稳定环回请求和取消装置 (R3.11)
* 保持模型发现测试不依赖于 https://github.com/storytold/craft-anything/pull/980 中安装的 OpenCode (R5.2)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## What's Changed
* Give native OpenCode runs the Craft Anything tools and show their tool calls by @advokat11 in https://github.com/storytold/craft-anything/pull/800
* Stabilize loopback request and cancellation fixtures (R3.11) by @Afloat16 in https://github.com/storytold/craft-anything/pull/767
* Keep the model discovery test from depending on OpenCode being installed (R5.2) by @justinjohn0306 in https://github.com/storytold/craft-anything/pull/980
* Start the Advanced console's prompt box at three lines (#942, R2.9) by @justinjohn0306 in https://github.com/storytold/craft-anything/pull/979
* Stop counting a video or music player as a game (#953, R2.7) by @justinjohn0306 in https://github.com/storytold/craft-anything/pull/970
* Add Georgian (ka) UI catalog by @devius in https://github.com/storytold/craft-anything/pull/775
* List MaterialCraft with the other Craft apps by @zitann2020 in https://github.com/storytold/craft-anything/pull/836
* List MaterialCraft in the Japanese Craft apps table by @zitann2020 in https://github.com/storytold/craft-anything/pull/837
* List MaterialCraft in the Korean Craft apps table by @zitann2020 in https://github.com/storytold/craft-anything/pull/838
* List MaterialCraft in the Chinese Craft apps table by @zitann2020 in https://github.com/storytold/craft-anything/pull/839
* Name the two modes plainly in Japanese: 外から観察 and 中まで解析 by @zitann2020 in https://github.com/storytold/craft-anything/pull/679
* Compare remote query test paths canonicall
```
</details>

---
### 📦 [JustAResearcher/gpu-unlock-ada](https://github.com/JustAResearcher/gpu-unlock-ada)
`⭐ Stars: 4,850` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.1.1](https://github.com/JustAResearcher/gpu-unlock-ada/releases/tag/v1.1.1) (2026-10-24)`

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
`⭐ Stars: 2,853` &nbsp;|&nbsp; `💻 语言: Other` &nbsp;|&nbsp; `🏷️ 最新版本: [0.10.4a](https://github.com/NeverSinkDev/NeverSink-Filter-for-PoE2/releases/tag/0.10.4a) (2026-10-15)`

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
`⭐ Stars: 165` &nbsp;|&nbsp; `💻 语言: Shell` &nbsp;|&nbsp; `🏷️ 最新版本: [2026.11.09-10/55_mips_24kc](https://github.com/kenzok8/compile-package/releases/tag/2026.11.09-10/55_mips_24kc) (2026-11-09)`

> **简介**：small-package仓库，每日更新插件编译

**💡 核心亮点更新 (中文)**：
定时更新插件，推送发布 💤:

[下载链接] (https://dllkids.xyz/packages/mips_24kc/)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
定时更新插件，推送发布 💤:

[下载链接] (https://dllkids.xyz/packages/mips_24kc/)
```
</details>

---
### 📦 [jxxghp/MoviePilot](https://github.com/jxxghp/MoviePilot)
`⭐ Stars: 12,048` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.2.5](https://github.com/jxxghp/MoviePilot/releases/tag/v3.2.5) (2026-11-06)`

> **简介**：NAS媒体库自动化管理工具

**💡 核心亮点更新 (中文)**：
- 下载与订阅：保留合集中的真实集号，修复缺集被误记为已下载、订阅提前完成的问题；Transmission 临时通信故障支持自动重连重试。
- 整理与网盘：完善远程存储覆盖整理时的临时文件命名，修复 115 等存储的重命名兼容问题。
- 媒体库：限制 Emby/Jellyfin 异常剧集范围的展开，避免媒体库同步时内存暴涨。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 本次更新内容

以下汇总主项目 v3.2.4 发布后（北京时间 2026 年 11 月 4 日 07:54 起）的前后端及 App 变化；iOS App 采用独立版本号，目前为 v1.2.1。

- 下载与订阅：保留合集中的真实集号，修复缺集被误记为已下载、订阅提前完成的问题；Transmission 临时通信故障支持自动重连重试。
- 整理与网盘：完善远程存储覆盖整理时的临时文件命名，修复 115 等存储的重命名兼容问题。
- 媒体库：限制 Emby/Jellyfin 异常剧集范围的展开，避免媒体库同步时内存暴涨。
- 站点兼容：适配 HDChina 新站 RSS，修复 CSPT 流量统计解析，以及站点从 HTTP 跳转 HTTPS 时丢失登录 Cookie 的问题。
- AI 助手：补齐模型请求的超时限制，避免请求长时间挂起；修复历史会话选择记录的时间与兼容加载。
- 运行稳定性：主动回收闲置浏览器会话；持久事件按处理器独立投递和重试，避免已完成的处理器随其它处理器失败而重复执行。
- 插件管理：修复启动时插件恢复异常；更新已安装插件时保留当前文件夹、筛选、排序和滚动位置。
- 界面提示：修复浅色玻璃主题下提示文字不清晰的问题；AppPush 通知渠道改用 MoviePilot 图标。
- App 兼容与导航：主 App 支持 iOS 16+（小组件仍需 iOS 17+），完善 iPad、iPhone 和 iPhone Duo 的导航、横竖屏与窗口适配，修复底栏滑块切换时回弹。
- App 消息通知：默认使用生产 APNs；授权前检查 AppPush 配置，修复错误登录提示及后台点击通知崩溃。原生推送仍需具备推送权限的签名。
- App 连接恢复：网络切换后服务地址不可达时，启动检查最多等待 15 秒便返回服务地址列表，并保留已保存的服务和登录状态。
- App 弹窗：修复插件设置保存后误入“App 导航连接已中断”恢复页的问题，保存失败后可继续编辑和重试。

## 完整变更记录

- docs(site): add site API integration requirements by @jxxghp ([90d469c](https://github.com/jxxghp/MoviePilot/commit/90d469c510c19e8ae03f6881becd36958e957ff5))
- fix(indexer): parse cspt dashboard traffic metrics by @jxxghp ([a87c005](https://github.com/jxxghp/MoviePilot/commit/a87c005322a99de7e374d574a830ba407951af21))
- fix(mediaserver): cap Emby episode range expansion by @MiCat-S ([dd43022](https://github.com/jxxghp/MoviePilot/commit/dd43022cd3cdb066a81d14f40d39c291e1abbf9c))
- fix(event): isolate durable broadcast handler delivery by @jxxghp ([054119e](https://github.com/jxxghp/MoviePilot/commit/054119e885e71e3b240986e35892d6
```
</details>

---
### 📦 [sandboxie-plus/Sandboxie](https://github.com/sandboxie-plus/Sandboxie)
`⭐ Stars: 19,903` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.18.8](https://github.com/sandboxie-plus/Sandboxie/releases/tag/v1.18.8) (2026-10-17)`

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
`⭐ Stars: 22` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.6.3](https://github.com/ziyuanhuishequ/release-downloader/releases/tag/v1.6.3) (2026-11-08)`

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
`⭐ Stars: 1,136` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.0.2](https://github.com/threerocks/sweety-handdraw-video/releases/tag/v3.0.2) (2026-11-03)`

> **简介**：从主题或文章制作完整手绘讲解视频：按部位描线、逐字书写、VoiceStudio 配音、五项内置制作依赖。

**💡 核心亮点更新 (中文)**：
- 规划尺寸 400、放大 3.2 倍时，3 个像素超出 0.36 px；
- 放大 2.4 倍时，2 个像素超出 0.14 px。
- 整张拉伸；

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# v3.0.2

用 3.0 的制作工具包做宣传片时，遇到三个小问题，都临时绕过去了。这一版从引擎里修掉它们，以后不用再绕。

## 1. 近景重绘的笔尖路径对齐像素中心（[#31](https://github.com/threerocks/sweety-handdraw-video/issues/31)）

**现象**：带推近镜头的页面，插画按放大倍数 s 重绘，渲染检查偶尔报 `color outside the active brush`。宣传片里长椅那张图：
- 规划尺寸 400、放大 3.2 倍时，3 个像素超出 0.36 px；
- 放大 2.4 倍时，2 个像素超出 0.14 px。

当时只能把规划尺寸改成 360 绕过去。

**原因**：笔尖路径按 `point × s` 放大，可规划图第 p 个像素放大后的中心在 `p × s + (s − 1) / 2`。所以近景里每条笔尖路径都比画面偏左上 (s − 1) / 2 像素，3.2 倍时是 1.1 px。笔划另一侧的颜色于是显得在笔头外面。墨线压感（落笔收笔变细）的中心线用的是同一种放大，也一样偏。

**现在**：笔尖路径和压感中心线都按像素中心对齐放大（`stroke_assets.to_render`）。同一张图、同一规划尺寸重建后，越界像素 2 → 0，最差的离容差还有 0.83 px。

## 2. 近方形线稿不再被压扁（[#32](https://github.com/threerocks/sweety-handdraw-video/issues/32)）

**现象**：1199 × 1312 的线稿（比例 0.91）上色后配准失败：线条只保留 68.6%，新增 27.9%。当时只能先手动把线稿补成正方形再上色。

**原因**：出图时这类线稿按“方图”处理，补边成方形画布再做上色编辑，生图工具返回整张方图。`line_first.py` 再把它直接拉伸回 0.91，所有线条横向压扁约 9%。

**现在**：上色图和线稿比例不同时，`line_first.py` 两种都试：
- 整张拉伸；
- 从正中裁回线稿那一块。

取保留线条多的一种，报告里的 `colour_fit` 写明用了哪种。同一对原图修复后：线条保留 100%，偏移 0，新增 3.6%，配准通过。比例一致的上色图照旧拉伸。

## 3. `gen --edit 名字` 可以用了（[#33](https://github.com/threerocks/sweety-handdraw-video/issues/33)）

**现象**：文档写的是 `art_pipeline.py JOB gen --edit 名字`，实际报 `unrecognized arguments`，只有 `gen 名字 --edit` 能用。

**现在**：`--edit`、`--force`、`--parallel` 写在名字前后都行。

## 验证

- 新增 `test_v302_fixes.py`（6 项）。拿到 v3.0.1 的代码上跑，6 项全部不通过：2 项失败，4 项报错。
- 全套测试与离线冒烟短片通过；`validate_package` 与 `tools/release.py check` 通过。
- 两个真实复现都用宣传片的原始素材：近方形那对线稿和上色图，以及长椅那张图在规划尺寸 400 的重建。

以上是工程检查。近景页面笔尖位置的变化最多约 1 px，观感需要人工观看确认。
```
</details>

---
### 📦 [KnifeLemon/Filee](https://github.com/KnifeLemon/Filee)
`⭐ Stars: 24,364` &nbsp;|&nbsp; `💻 语言: C#` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.3.0](https://github.com/KnifeLemon/Filee/releases/tag/v2.3.0) (2026-11-03)`

> **简介**：免费的开源文件转换器。通过拖放功能离线转换 263 格式 — 图像、PDF、Word、Excel、PowerPoint、HWP/HWPX、视频、音频、电子书和档案。无需上传，无需 Office。

**💡 核心亮点更新 (中文)**：
发生了什么变化

<!--更新
级别：推荐
zh: 注释：向照片添加箭头、框、突出显示、字母和数字。
zh: 裁剪视频：删除黑色空间或剪切到所需的比例
ko：合并：将 PDF 的第 2、4、6、8 和 9 页收集到一张纸上
zh: 设置 → 字段：从列表和圆形工具栏中隐藏未使用字段的格式（CAD、3D、字体等）。
ko：文档、电子书、字幕（SRT、WebVTT）

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## What's Changed

<!-- update
level: recommended
ko: 주석 달기: 사진에 화살표, 상자, 강조, 글자, 번호를 넣어요
ko: 동영상 자르기: 검은 여백을 없애거나 원하는 비율로 잘라요
ko: 모아찍기: PDF 2·4·6·8·9쪽을 한 장에 모아요
ko: 설정 → 분야: 쓰지 않는 분야(CAD, 3D, 글꼴 등)의 형식을 목록과 원형 툴바에서 숨겨요
ko: 문서·전자책·자막(SRT, WebVTT)을 내 PC의 AI로 번역하고, 동영상·음성에서 자막(SRT)을 만들어요
ko: 인쇄용 CMYK 파일: PSD·TIFF·JPG → PDF, AI·PDF → JPG·TIFF가 CMYK 그대로 나와요
ko: 폴더로 복사·이동, 이미지·동영상 크기 제한, 원근 보정 자르기, 합치기 전에 순서 정렬, 접히는 사이드바
ko: 새 형식: Krita, 마인크래프트 팩, Modrinth 모드팩, Dart·HiveQL, 음성 메모(.qta), Bink, 사진 → 3D 부조, 이탈리아어·인도네시아어·베트남어
ko: Ubuntu 22.04에서 OCR → PDF가 실패하던 문제, DOCX → PDF가 멈추던 문제, 움직이는 GIF → JXL이 한 장만 나오던 문제 등을 고쳤어요
en: Annotate: arrows, boxes, highlights, text and numbers on a picture
en: Crop video: remove black bars, or crop to a ratio
en: Pages per sheet: 2, 4, 6, 8 or 9 PDF pages on each sheet
en: Settings → Fields: hide the formats of fields you don't work in (CAD, 3D, fonts …)
en: Translate documents, e-books and SRT / WebVTT subtitles with a local AI, and make captions (SRT) from video and audio
en: CMYK print files stay CMYK: PSD, TIFF, JPG → PDF, and AI, PDF → JPG, TIFF
en: Copy or move to a folder, size limits for pictures and videos, perspective crop, sort files before merging, a collapsible sidebar
en: New formats: Krita, Minecraft packs, Modrinth modpacks, Dart and HiveQL, Voice Memos (.qta), Bink, pictures → 3D relief; Italian, Indonesian and Vietnamese
en: Fixed OCR to PDF on Ubuntu 22.04, DOCX → PDF hanging, animated GIF → JPEG XL keeping one fra
```
</details>

---
### 📦 [guohuiyuan/go-music-dl](https://github.com/guohuiyuan/go-music-dl)
`⭐ Stars: 6,104` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.1.5](https://github.com/guohuiyuan/go-music-dl/releases/tag/v1.1.5) (2026-11-09)`

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
`⭐ Stars: 23,965` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.22.0](https://github.com/LibreSpark/LibreTV/releases/tag/v2.22.0) (2026-11-08)`

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
### 📦 [dyang886/Game-Cheats-Manager](https://github.com/dyang886/Game-Cheats-Manager)
`⭐ Stars: 16,053` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.5.4](https://github.com/dyang886/Game-Cheats-Manager/releases/tag/v2.5.4) (2026-10-11)`

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
`⭐ Stars: 46,878` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2026.11.09-8610.f813abe](https://github.com/DIYgod/RSSHub/releases/tag/v2026.11.09-8610.f813abe) (2026-11-09)`

> **简介**：🧡 一切都是RSSible

**💡 核心亮点更新 (中文)**：
-ghcr.io/diygod/rsshub:f813abebdbca64733452000f73c79e5b8f8b4716
-ghcr.io/diygod/rsshub:chromium-bundled-f813abebdbca64733452000f73c79e5b8f8b4716
-diygod/rsshub:f813abebdbca64733452000f73c79e5b8f8b4716

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Source commit: f813abebdbca64733452000f73c79e5b8f8b4716

Published multi-platform images:
- ghcr.io/diygod/rsshub:f813abebdbca64733452000f73c79e5b8f8b4716
- ghcr.io/diygod/rsshub:chromium-bundled-f813abebdbca64733452000f73c79e5b8f8b4716
- diygod/rsshub:f813abebdbca64733452000f73c79e5b8f8b4716
- diygod/rsshub:chromium-bundled-f813abebdbca64733452000f73c79e5b8f8b4716

Use these commit-specific image tags to reproduce this release. Daily Docker tags may be updated by subsequent builds.
```
</details>

---
### 📦 [amir1376/ab-download-manager](https://github.com/amir1376/ab-download-manager)
`⭐ Stars: 19,118` &nbsp;|&nbsp; `💻 语言: Kotlin` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.11.4](https://github.com/amir1376/ab-download-manager/releases/tag/v1.11.4) (2026-11-03)`

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
`⭐ Stars: 9,701` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.7.0](https://github.com/gyroflow/gyroflow/releases/tag/v1.7.0) (2026-11-07)`

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
`⭐ Stars: 206,322` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [2026.10.26](https://github.com/yt-dlp/yt-dlp/releases/tag/2026.10.26) (2026-10-26)`

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
`⭐ Stars: 79,196` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [33.0.1](https://github.com/obsproject/obs-studio/releases/tag/33.0.1) (2026-10-29)`

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
`⭐ Stars: 5,598` &nbsp;|&nbsp; `💻 语言: CSS` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.1.3](https://github.com/jerrykuku/luci-theme-argon/releases/tag/v3.1.3) (2026-11-06)`

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
### 📦 [qier222/YesPlayMusic](https://github.com/qier222/YesPlayMusic)
`⭐ Stars: 33,598` &nbsp;|&nbsp; `💻 语言: Vue` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.4.11](https://github.com/qier222/YesPlayMusic/releases/tag/v0.4.11) (2026-10-10)`

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
`⭐ Stars: 58,019` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.4.0](https://github.com/agalwood/Motrix/releases/tag/v2.4.0) (2026-11-08)`

> **简介**：功能齐全的下载管理器。

**💡 核心亮点更新 (中文)**：
* ci(fnos)：通过 https://github.com/agalwood/Motrix/pull/2507 发布经过验证的本机包以实现稳定版本
* 修复（最终确定）：稳定 Windows 后缀重命名并通过 https://github.com/agalwood/Motrix/pull/2512 恢复隔离
* 文档：通过 https://github.com/agalwood/Motrix/pull/2510 修改问题模板中的预检清单项目 [skip ci]

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# Motrix 2.4.0

English | [简体中文](https://github.com/agalwood/Motrix/blob/main/docs/release-notes/2.4.0.zh-CN.md)

## Changes since 2.3.0

- Choose **File → Create Torrent File** to create a BitTorrent v1 `.torrent` from a file or folder. Desktop users can select local files. In the Server Web UI, select a source within your account’s readable download roots and save the torrent to your browser. Enable seeding after saving to verify and seed the original files.
- Install the experimental native Synology SPK through Package Center on supported x86_64 and ARM64 models running DSM 7.2.2-72806 or later. Local administrators share the same tasks and settings. See the [Synology installation guide](https://github.com/agalwood/Motrix/blob/v2.4.0/packaging/synology/README.md) for model coverage.
- Fix Windows downloads failing to remove a temporary filename suffix when file timestamps change during finalization. A verified retry can recover a quarantined file while preserving conflicting files.
- Separate release workflows verify and publish fnOS FPKs and Synology SPKs. Download the package for your NAS architecture from the Release and check the accompanying SHA-256.
- Update the desktop Electron runtime to **45.2.3**.

## Upgrade compatibility

**Back up your profile and download files before upgrading.** The bundled engine
uses SQLite **schema 6**. When upgrading an older engine database, retain its
complete pre-upgrade backup; older engines cannot open schema 6. Stop all engines
be
```
</details>

---
### 📦 [subhra74/xdm](https://github.com/subhra74/xdm)
`⭐ Stars: 8,375` &nbsp;|&nbsp; `💻 语言: Kotlin` &nbsp;|&nbsp; `🏷️ 最新版本: [v9.0.9](https://github.com/subhra74/xdm/releases/tag/v9.0.9) (2026-11-01)`

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

## <span id="-系统与开发者工具">🛠️ 系统与开发者工具</span>

### 📦 [physicsdolphin/nv-uefi-unlocker](https://github.com/physicsdolphin/nv-uefi-unlocker)
`⭐ Stars: 2,134` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.1.11](https://github.com/physicsdolphin/nv-uefi-unlocker/releases/tag/v2.1.11) (2026-11-08)`

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
### 📦 [openwrt/openwrt](https://github.com/openwrt/openwrt)
`⭐ Stars: 29,146` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [v25.12.6](https://github.com/openwrt/openwrt/releases/tag/v25.12.6) (2026-10-18)`

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
`⭐ Stars: 39,784` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.14.4](https://github.com/SagerNet/sing-box/releases/tag/v1.14.4) (2026-10-24)`

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
`⭐ Stars: 10,863` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [2.44.6](https://github.com/sub-store-org/Sub-Store/releases/tag/2.44.6) (2026-11-08)`

> **简介**：QX、Loon、Surge、Stash、Egern 和 Shadowrocket 的高级订阅管理器！

**💡 核心亮点更新 (中文)**：
* feat: YAML 逻辑优化 #667 ([2888806](https://github.com/sub-store-org/Sub-Store/commit/2888806)), closes [#667](https://github.com/sub-store-org/Sub-Store/issues/667)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## <small>2.44.6 (2026-11-08)</small>

* feat: YAML 逻辑优化 #667 ([2888806](https://github.com/sub-store-org/Sub-Store/commit/2888806)), closes [#667](https://github.com/sub-store-org/Sub-Store/issues/667)
```
</details>

---
### 📦 [233boy/Xray](https://github.com/233boy/Xray)
`⭐ Stars: 2,800` &nbsp;|&nbsp; `💻 语言: Shell` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.37](https://github.com/233boy/Xray/releases/tag/v1.37) (2026-11-02)`

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
`⭐ Stars: 2,683` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.39.0](https://github.com/enfein/mieru/releases/tag/v3.39.0) (2026-10-23)`

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
`⭐ Stars: 15,832` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.5.13](https://github.com/v2rayA/v2rayA/releases/tag/v2.5.13) (2026-11-02)`

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
`⭐ Stars: 28,106` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.48.002](https://github.com/vernesong/OpenClash/releases/tag/v0.48.002) (2026-10-12)`

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
### 📦 [QiuSimons/YAOF](https://github.com/QiuSimons/YAOF)
`⭐ Stars: 2,782` &nbsp;|&nbsp; `💻 语言: Shell` &nbsp;|&nbsp; `🏷️ 最新版本: [25.12.6](https://github.com/QiuSimons/YAOF/releases/tag/25.12.6) (2026-10-18)`

> **简介**：适用于 Nanopi R2C/R2S/R4S/X86 的 OpenWrt

**💡 核心亮点更新 (中文)**：
该版本未提供详细更新说明。

---
### 📦 [Loyalsoldier/v2ray-rules-dat](https://github.com/Loyalsoldier/v2ray-rules-dat)
`⭐ Stars: 21,015` &nbsp;|&nbsp; `💻 语言: Other` &nbsp;|&nbsp; `🏷️ 最新版本: [202611082203](https://github.com/Loyalsoldier/v2ray-rules-dat/releases/tag/202611082203) (2026-11-08)`

> **简介**：🦄 🎃 👻 V2Ray 路由规则文件加强版，可代替 V2Ray 官方 geoip.dat 和 geosite.dat，适用于 V2Ray、Xray-core、mihomo(Clash-Meta)、hysteria、Trojan-Go 和 leaf。Enhanced edition of V2Ray rules dat files, applicable to V2Ray, Xray-core, mihomo(Clash-Meta), hysteria, Trojan-Go and leaf.

**💡 核心亮点更新 (中文)**：
该版本未提供详细更新说明。

---
### 📦 [Openwrt-Passwall/openwrt-passwall](https://github.com/Openwrt-Passwall/openwrt-passwall)
`⭐ Stars: 9,996` &nbsp;|&nbsp; `💻 语言: Lua` &nbsp;|&nbsp; `🏷️ 最新版本: [26.11.3-1](https://github.com/Openwrt-Passwall/openwrt-passwall/releases/tag/26.11.3-1) (2026-11-03)`

> **简介**：暂无项目描述

**💡 核心亮点更新 (中文)**：
* 请按照 [openwrt-passwall-build](https://github.com/moetayuko/openwrt-passwall-build) 仓库的说明，将其提供的软件源添加到设备中，然后直接使用包管理器安装。
* 从 [SourceForge](https://sourceforge.net/projects/openwrt-passwall-build/files/) 下载预构建的软件包。
* 将文件上传到您的设备，使用 Shell 命令进行安装。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
![](https://img.shields.io/github/downloads/Openwrt-Passwall/openwrt-passwall/26.11.3-1/total?style=flat-square)
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
  Firmware built on official OpenWrt 25.12, ImmortalWrt 25.12 a
```
</details>

---
### 📦 [2dust/v2rayN](https://github.com/2dust/v2rayN)
`⭐ Stars: 120,230` &nbsp;|&nbsp; `💻 语言: C#` &nbsp;|&nbsp; `🏷️ 最新版本: [7.25.6](https://github.com/2dust/v2rayN/releases/tag/7.25.6) (2026-10-11)`

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

## 🛑 建议清理 / 放弃维护项目

<details>
<summary>⚠️ 点击展开已放弃维护或超过 1 年停更的仓库清单 (135 个)</summary>

| 仓库名称 | Stars | 状态说明 | 操作建议 |
| :--- | :---: | :--- | :---: |
| [cityflow-project/CityFlow](https://github.com/cityflow-project/CityFlow) | 1,032 | 超过 446 天无代码提交 | [进入取消 Star](https://github.com/cityflow-project/CityFlow) |
| [facebookresearch/demucs](https://github.com/facebookresearch/demucs) | 10,404 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/facebookresearch/demucs) |
| [fufankeji/DeepSeek-OCR-Web](https://github.com/fufankeji/DeepSeek-OCR-Web) | 569 | 超过 377 天无代码提交 | [进入取消 Star](https://github.com/fufankeji/DeepSeek-OCR-Web) |
| [JimmyLv/awesome-nano-banana](https://github.com/JimmyLv/awesome-nano-banana) | 8,799 | 超过 426 天无代码提交 | [进入取消 Star](https://github.com/JimmyLv/awesome-nano-banana) |
| [btjawa/BiliTools](https://github.com/btjawa/BiliTools) | 5,010 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/btjawa/BiliTools) |
| [ehang-io/nps](https://github.com/ehang-io/nps) | 34,252 | 超过 893 天无代码提交 | [进入取消 Star](https://github.com/ehang-io/nps) |
| [ReturnFI/Blitz](https://github.com/ReturnFI/Blitz) | 1,089 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/ReturnFI/Blitz) |
| [kkangert/kspider](https://github.com/kkangert/kspider) | 1,264 | 超过 812 天无代码提交 | [进入取消 Star](https://github.com/kkangert/kspider) |
| [xenova/whisper-web](https://github.com/xenova/whisper-web) | 3,344 | 超过 768 天无代码提交 | [进入取消 Star](https://github.com/xenova/whisper-web) |
| [shadowsocks/luci-app-shadowsocks](https://github.com/shadowsocks/luci-app-shadowsocks) | 1,149 | 超过 1260 天无代码提交 | [进入取消 Star](https://github.com/shadowsocks/luci-app-shadowsocks) |
| [sinaptik-ai/pandas-ai](https://github.com/sinaptik-ai/pandas-ai) | 23,943 | 超过 376 天无代码提交 | [进入取消 Star](https://github.com/sinaptik-ai/pandas-ai) |
| [adithya-s-k/marker-api](https://github.com/adithya-s-k/marker-api) | 982 | 超过 754 天无代码提交 | [进入取消 Star](https://github.com/adithya-s-k/marker-api) |
| [yuchannslv5/warpflare](https://github.com/yuchannslv5/warpflare) | 334 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/yuchannslv5/warpflare) |
| [vvbbnn00/WARP-Clash-API](https://github.com/vvbbnn00/WARP-Clash-API) | 8,801 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/vvbbnn00/WARP-Clash-API) |
| [chika0801/hysteria-install](https://github.com/chika0801/hysteria-install) | 177 | 超过 857 天无代码提交 | [进入取消 Star](https://github.com/chika0801/hysteria-install) |
| [yeahwu/InstallOS](https://github.com/yeahwu/InstallOS) | 86 | 超过 1614 天无代码提交 | [进入取消 Star](https://github.com/yeahwu/InstallOS) |
| [bulianglin/psub](https://github.com/bulianglin/psub) | 1,757 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/bulianglin/psub) |
| [lizongying/my-tv](https://github.com/lizongying/my-tv) | 31,966 | 超过 872 天无代码提交 | [进入取消 Star](https://github.com/lizongying/my-tv) |
| [joevess/IPTV](https://github.com/joevess/IPTV) | 10,276 | 超过 677 天无代码提交 | [进入取消 Star](https://github.com/joevess/IPTV) |
| [lecepin/WeChatVideoDownloader](https://github.com/lecepin/WeChatVideoDownloader) | 4,661 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/lecepin/WeChatVideoDownloader) |
| [linexjlin/GPTs](https://github.com/linexjlin/GPTs) | 32,016 | 超过 773 天无代码提交 | [进入取消 Star](https://github.com/linexjlin/GPTs) |
| [lxfater/Awesome-GPTs](https://github.com/lxfater/Awesome-GPTs) | 1,155 | 超过 1083 天无代码提交 | [进入取消 Star](https://github.com/lxfater/Awesome-GPTs) |
| [ClashDotNetFramework/experimental-clash](https://github.com/ClashDotNetFramework/experimental-clash) | 241 | 超过 1798 天无代码提交 | [进入取消 Star](https://github.com/ClashDotNetFramework/experimental-clash) |
| [zzzgydi/clash-verge](https://github.com/zzzgydi/clash-verge) | 21,856 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/zzzgydi/clash-verge) |
| [ddgth/cf2dns](https://github.com/ddgth/cf2dns) | 5,216 | 超过 672 天无代码提交 | [进入取消 Star](https://github.com/ddgth/cf2dns) |
| [zizifn/edgetunnel](https://github.com/zizifn/edgetunnel) | 9,324 | 超过 711 天无代码提交 | [进入取消 Star](https://github.com/zizifn/edgetunnel) |
| [missuo/Hysteria2](https://github.com/missuo/Hysteria2) | 204 | 超过 802 天无代码提交 | [进入取消 Star](https://github.com/missuo/Hysteria2) |
| [Misaka-blog/hysteria-install](https://github.com/Misaka-blog/hysteria-install) | 629 | 超过 934 天无代码提交 | [进入取消 Star](https://github.com/Misaka-blog/hysteria-install) |
| [MatsuriDayo/nekoray](https://github.com/MatsuriDayo/nekoray) | 15,247 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/MatsuriDayo/nekoray) |
| [FranzKafkaYu/x-ui](https://github.com/FranzKafkaYu/x-ui) | 8,434 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/FranzKafkaYu/x-ui) |
| [rwv/chinese-dos-games](https://github.com/rwv/chinese-dos-games) | 10,351 | 超过 823 天无代码提交 | [进入取消 Star](https://github.com/rwv/chinese-dos-games) |
| [getumbrel/llama-gpt](https://github.com/getumbrel/llama-gpt) | 10,924 | 超过 929 天无代码提交 | [进入取消 Star](https://github.com/getumbrel/llama-gpt) |
| [WangWenBin2017/OpenWrt-SSRPLUS](https://github.com/WangWenBin2017/OpenWrt-SSRPLUS) | 560 | 超过 616 天无代码提交 | [进入取消 Star](https://github.com/WangWenBin2017/OpenWrt-SSRPLUS) |
| [prompt-engineering/click-prompt](https://github.com/prompt-engineering/click-prompt) | 2,387 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/prompt-engineering/click-prompt) |
| [AutodeskAILab/Building-GAN](https://github.com/AutodeskAILab/Building-GAN) | 100 | 超过 1619 天无代码提交 | [进入取消 Star](https://github.com/AutodeskAILab/Building-GAN) |
| [novicezk/midjourney-proxy](https://github.com/novicezk/midjourney-proxy) | 5,375 | 超过 463 天无代码提交 | [进入取消 Star](https://github.com/novicezk/midjourney-proxy) |
| [adams549659584/go-proxy-bingai](https://github.com/adams549659584/go-proxy-bingai) | 8,396 | 超过 964 天无代码提交 | [进入取消 Star](https://github.com/adams549659584/go-proxy-bingai) |
| [tryptech/obs-zoom-and-follow](https://github.com/tryptech/obs-zoom-and-follow) | 440 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/tryptech/obs-zoom-and-follow) |
| [XingangPan/DragGAN](https://github.com/XingangPan/DragGAN) | 35,700 | 超过 904 天无代码提交 | [进入取消 Star](https://github.com/XingangPan/DragGAN) |
| [lewangdev/faster-whisper-youtube](https://github.com/lewangdev/faster-whisper-youtube) | 558 | 超过 1177 天无代码提交 | [进入取消 Star](https://github.com/lewangdev/faster-whisper-youtube) |
| [artidoro/qlora](https://github.com/artidoro/qlora) | 11,068 | 超过 881 天无代码提交 | [进入取消 Star](https://github.com/artidoro/qlora) |
| [langgenius/webapp-conversation](https://github.com/langgenius/webapp-conversation) | 1,101 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/langgenius/webapp-conversation) |
| [3andne/restls](https://github.com/3andne/restls) | 377 | 超过 1099 天无代码提交 | [进入取消 Star](https://github.com/3andne/restls) |
| [jtsang4/claude-to-chatgpt](https://github.com/jtsang4/claude-to-chatgpt) | 1,298 | 超过 812 天无代码提交 | [进入取消 Star](https://github.com/jtsang4/claude-to-chatgpt) |
| [yorunning/clash-conf](https://github.com/yorunning/clash-conf) | 103 | 超过 845 天无代码提交 | [进入取消 Star](https://github.com/yorunning/clash-conf) |
| [svc-develop-team/so-vits-svc](https://github.com/svc-develop-team/so-vits-svc) | 28,050 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/svc-develop-team/so-vits-svc) |
| [xiaye13579/BBLL](https://github.com/xiaye13579/BBLL) | 17,520 | 超过 619 天无代码提交 | [进入取消 Star](https://github.com/xiaye13579/BBLL) |
| [camenduru/MiniGPT-4-colab](https://github.com/camenduru/MiniGPT-4-colab) | 119 | 超过 1197 天无代码提交 | [进入取消 Star](https://github.com/camenduru/MiniGPT-4-colab) |
| [Vision-CAIR/MiniGPT-4](https://github.com/Vision-CAIR/MiniGPT-4) | 25,563 | 超过 797 天无代码提交 | [进入取消 Star](https://github.com/Vision-CAIR/MiniGPT-4) |
| [imfuxiao/Hamster](https://github.com/imfuxiao/Hamster) | 1,643 | 超过 544 天无代码提交 | [进入取消 Star](https://github.com/imfuxiao/Hamster) |
| [acheong08/ChatGPT](https://github.com/acheong08/ChatGPT) | 27,986 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/acheong08/ChatGPT) |
| [microsoft/JARVIS](https://github.com/microsoft/JARVIS) | 25,597 | 超过 467 天无代码提交 | [进入取消 Star](https://github.com/microsoft/JARVIS) |
| [choephix/auto-gpt-webui](https://github.com/choephix/auto-gpt-webui) | 116 | 超过 965 天无代码提交 | [进入取消 Star](https://github.com/choephix/auto-gpt-webui) |
| [facebookresearch/segment-anything](https://github.com/facebookresearch/segment-anything) | 55,112 | 超过 781 天无代码提交 | [进入取消 Star](https://github.com/facebookresearch/segment-anything) |
| [zai-org/ChatGLM-6B](https://github.com/zai-org/ChatGLM-6B) | 40,862 | 超过 865 天无代码提交 | [进入取消 Star](https://github.com/zai-org/ChatGLM-6B) |
| [ihciah/shadow-tls](https://github.com/ihciah/shadow-tls) | 2,680 | 超过 562 天无代码提交 | [进入取消 Star](https://github.com/ihciah/shadow-tls) |
| [jxbbb/ADAPT](https://github.com/jxbbb/ADAPT) | 421 | 超过 880 天无代码提交 | [进入取消 Star](https://github.com/jxbbb/ADAPT) |
| [mayooear/ai-pdf-chatbot-langchain](https://github.com/mayooear/ai-pdf-chatbot-langchain) | 16,586 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/mayooear/ai-pdf-chatbot-langchain) |
| [lencx/ChatGPT](https://github.com/lencx/ChatGPT) | 54,662 | 超过 801 天无代码提交 | [进入取消 Star](https://github.com/lencx/ChatGPT) |
| [nekohasekai/SagerNet](https://github.com/nekohasekai/SagerNet) | 56 | 超过 1764 天无代码提交 | [进入取消 Star](https://github.com/nekohasekai/SagerNet) |
| [P3TERX/Actions-OpenWrt](https://github.com/P3TERX/Actions-OpenWrt) | 7,617 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/P3TERX/Actions-OpenWrt) |
| [R86S/R86S-QuickInstaller](https://github.com/R86S/R86S-QuickInstaller) | 64 | 超过 1185 天无代码提交 | [进入取消 Star](https://github.com/R86S/R86S-QuickInstaller) |
| [WeNeedHome/SummaryOfLoanSuspension](https://github.com/WeNeedHome/SummaryOfLoanSuspension) | 20,322 | 超过 849 天无代码提交 | [进入取消 Star](https://github.com/WeNeedHome/SummaryOfLoanSuspension) |
| [zanzhz1101/LingMaxDNS](https://github.com/zanzhz1101/LingMaxDNS) | 23 | 超过 1580 天无代码提交 | [进入取消 Star](https://github.com/zanzhz1101/LingMaxDNS) |
| [IrineSistiana/mosdns-cn](https://github.com/IrineSistiana/mosdns-cn) | 324 | 超过 1621 天无代码提交 | [进入取消 Star](https://github.com/IrineSistiana/mosdns-cn) |
| [chika0801/Xray-install](https://github.com/chika0801/Xray-install) | 272 | 超过 1073 天无代码提交 | [进入取消 Star](https://github.com/chika0801/Xray-install) |
| [scutan90/DeepLearning-500-questions](https://github.com/scutan90/DeepLearning-500-questions) | 57,715 | 超过 865 天无代码提交 | [进入取消 Star](https://github.com/scutan90/DeepLearning-500-questions) |
| [Chikage0o0/Linux-NetSpeed](https://github.com/Chikage0o0/Linux-NetSpeed) | 3,739 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/Chikage0o0/Linux-NetSpeed) |
| [KFERMercer/OpenWrt-CI](https://github.com/KFERMercer/OpenWrt-CI) | 1,408 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/KFERMercer/OpenWrt-CI) |
| [qTox/qTox](https://github.com/qTox/qTox) | 4,970 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/qTox/qTox) |
| [quericy/one-key-ikev2-vpn](https://github.com/quericy/one-key-ikev2-vpn) | 2,105 | 超过 2184 天无代码提交 | [进入取消 Star](https://github.com/quericy/one-key-ikev2-vpn) |
| [riverscn/openwrt-iptvhelper](https://github.com/riverscn/openwrt-iptvhelper) | 371 | 超过 1900 天无代码提交 | [进入取消 Star](https://github.com/riverscn/openwrt-iptvhelper) |
| [frainzy1477/luci-app-clash](https://github.com/frainzy1477/luci-app-clash) | 1,622 | 超过 1690 天无代码提交 | [进入取消 Star](https://github.com/frainzy1477/luci-app-clash) |
| [Sanster/IOPaint](https://github.com/Sanster/IOPaint) | 23,284 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/Sanster/IOPaint) |
| [LANDrop/LANDrop](https://github.com/LANDrop/LANDrop) | 5,999 | 超过 817 天无代码提交 | [进入取消 Star](https://github.com/LANDrop/LANDrop) |
| [saveweb/review-2021](https://github.com/saveweb/review-2021) | 756 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/saveweb/review-2021) |
| [iranee/qnap-aliyunpan-webdav](https://github.com/iranee/qnap-aliyunpan-webdav) | 273 | 超过 1492 天无代码提交 | [进入取消 Star](https://github.com/iranee/qnap-aliyunpan-webdav) |
| [haoel/haoel.github.io](https://github.com/haoel/haoel.github.io) | 13,082 | 超过 1277 天无代码提交 | [进入取消 Star](https://github.com/haoel/haoel.github.io) |
| [tindy2013/stairspeedtest-reborn](https://github.com/tindy2013/stairspeedtest-reborn) | 3,823 | 超过 1249 天无代码提交 | [进入取消 Star](https://github.com/tindy2013/stairspeedtest-reborn) |
| [P3TERX/warp.sh](https://github.com/P3TERX/warp.sh) | 3,921 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/P3TERX/warp.sh) |
| [TheMRLL/WinXray](https://github.com/TheMRLL/WinXray) | 2,789 | 超过 986 天无代码提交 | [进入取消 Star](https://github.com/TheMRLL/WinXray) |
| [Mikubill/cowtransfer-uploader](https://github.com/Mikubill/cowtransfer-uploader) | 447 | 超过 1733 天无代码提交 | [进入取消 Star](https://github.com/Mikubill/cowtransfer-uploader) |
| [281677160/build-actions](https://github.com/281677160/build-actions) | 387 | 超过 468 天无代码提交 | [进入取消 Star](https://github.com/281677160/build-actions) |
| [vaxilu/x-ui](https://github.com/vaxilu/x-ui) | 19,084 | 超过 811 天无代码提交 | [进入取消 Star](https://github.com/vaxilu/x-ui) |
| [xinntao/Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) | 37,413 | 超过 824 天无代码提交 | [进入取消 Star](https://github.com/xinntao/Real-ESRGAN) |
| [zu1k/proxypool](https://github.com/zu1k/proxypool) | 4,039 | 超过 1308 天无代码提交 | [进入取消 Star](https://github.com/zu1k/proxypool) |
| [TachibanaYoshino/AnimeGAN](https://github.com/TachibanaYoshino/AnimeGAN) | 4,610 | 超过 1558 天无代码提交 | [进入取消 Star](https://github.com/TachibanaYoshino/AnimeGAN) |
| [yuanzhoulvpi2017/tiny_python](https://github.com/yuanzhoulvpi2017/tiny_python) | 173 | 超过 1372 天无代码提交 | [进入取消 Star](https://github.com/yuanzhoulvpi2017/tiny_python) |
| [haiibo/OpenWrt](https://github.com/haiibo/OpenWrt) | 3,160 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/haiibo/OpenWrt) |
| [VergilGao/openwrt-packages](https://github.com/VergilGao/openwrt-packages) | 11 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/VergilGao/openwrt-packages) |
| [VergilGao/openwrt-compiler](https://github.com/VergilGao/openwrt-compiler) | 13 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/VergilGao/openwrt-compiler) |
| [OpenELEC/OpenELEC.tv](https://github.com/OpenELEC/OpenELEC.tv) | 1,619 | 超过 3354 天无代码提交 | [进入取消 Star](https://github.com/OpenELEC/OpenELEC.tv) |
| [github/copilot-docs](https://github.com/github/copilot-docs) | 23,163 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/github/copilot-docs) |
| [Kiougar/luci-wrtbwmon](https://github.com/Kiougar/luci-wrtbwmon) | 355 | 超过 1872 天无代码提交 | [进入取消 Star](https://github.com/Kiougar/luci-wrtbwmon) |
| [EtherDream/jsproxy](https://github.com/EtherDream/jsproxy) | 9,312 | 超过 952 天无代码提交 | [进入取消 Star](https://github.com/EtherDream/jsproxy) |
| [cheat-engine/cheat-engine](https://github.com/cheat-engine/cheat-engine) | 19,445 | 超过 569 天无代码提交 | [进入取消 Star](https://github.com/cheat-engine/cheat-engine) |
| [ffffffff0x/Dork-Admin](https://github.com/ffffffff0x/Dork-Admin) | 1,913 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/ffffffff0x/Dork-Admin) |
| [ffffffff0x/Digital-Privacy](https://github.com/ffffffff0x/Digital-Privacy) | 4,934 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/ffffffff0x/Digital-Privacy) |
| [Autodesk/civilconnection](https://github.com/Autodesk/civilconnection) | 121 | 超过 1438 天无代码提交 | [进入取消 Star](https://github.com/Autodesk/civilconnection) |
| [0xHJK/CleanApps](https://github.com/0xHJK/CleanApps) | 165 | 超过 1904 天无代码提交 | [进入取消 Star](https://github.com/0xHJK/CleanApps) |
| [KANIKIG/Multi-EasyGost](https://github.com/KANIKIG/Multi-EasyGost) | 1,943 | 超过 952 天无代码提交 | [进入取消 Star](https://github.com/KANIKIG/Multi-EasyGost) |
| [Kurokosama/AutoBuild-OpenWRT](https://github.com/Kurokosama/AutoBuild-OpenWRT) | 88 | 超过 1591 天无代码提交 | [进入取消 Star](https://github.com/Kurokosama/AutoBuild-OpenWRT) |
| [differentrain/DeletionTool](https://github.com/differentrain/DeletionTool) | 94 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/differentrain/DeletionTool) |
| [hideuvpn/android-google-play-store](https://github.com/hideuvpn/android-google-play-store) | 3,677 | 超过 1573 天无代码提交 | [进入取消 Star](https://github.com/hideuvpn/android-google-play-store) |
| [XJP-GIT/AntiZhaPian](https://github.com/XJP-GIT/AntiZhaPian) | 3,162 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/XJP-GIT/AntiZhaPian) |
| [jerrykuku/luci-app-ttnode](https://github.com/jerrykuku/luci-app-ttnode) | 89 | 超过 1749 天无代码提交 | [进入取消 Star](https://github.com/jerrykuku/luci-app-ttnode) |
| [KevinSHIT/NaiveSharp](https://github.com/KevinSHIT/NaiveSharp) | 97 | 超过 2194 天无代码提交 | [进入取消 Star](https://github.com/KevinSHIT/NaiveSharp) |
| [prasmussen/gdrive](https://github.com/prasmussen/gdrive) | 8,940 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/prasmussen/gdrive) |
| [tostercx/GTAO_Booster_PoC](https://github.com/tostercx/GTAO_Booster_PoC) | 2,862 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/tostercx/GTAO_Booster_PoC) |
| [ilxp/luci-app-ikoolproxy](https://github.com/ilxp/luci-app-ikoolproxy) | 505 | 超过 604 天无代码提交 | [进入取消 Star](https://github.com/ilxp/luci-app-ikoolproxy) |
| [kiddin9/luci-app-dnsfilter](https://github.com/kiddin9/luci-app-dnsfilter) | 124 | 超过 637 天无代码提交 | [进入取消 Star](https://github.com/kiddin9/luci-app-dnsfilter) |
| [h31105/deployX.sh](https://github.com/h31105/deployX.sh) | 417 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/h31105/deployX.sh) |
| [jerrykuku/openwrt-package](https://github.com/jerrykuku/openwrt-package) | 147 | 超过 1101 天无代码提交 | [进入取消 Star](https://github.com/jerrykuku/openwrt-package) |
| [frainzy1477/luci-app-trojan](https://github.com/frainzy1477/luci-app-trojan) | 120 | 超过 2008 天无代码提交 | [进入取消 Star](https://github.com/frainzy1477/luci-app-trojan) |
| [atrandys/xray](https://github.com/atrandys/xray) | 89 | 超过 1716 天无代码提交 | [进入取消 Star](https://github.com/atrandys/xray) |
| [v2board/v2board](https://github.com/v2board/v2board) | 5,066 | 超过 965 天无代码提交 | [进入取消 Star](https://github.com/v2board/v2board) |
| [ShadowsocksR-Live/iShadowsocksR](https://github.com/ShadowsocksR-Live/iShadowsocksR) | 602 | 超过 923 天无代码提交 | [进入取消 Star](https://github.com/ShadowsocksR-Live/iShadowsocksR) |
| [SuperNG6/Aria2-Trackers](https://github.com/SuperNG6/Aria2-Trackers) | 309 | 超过 2115 天无代码提交 | [进入取消 Star](https://github.com/SuperNG6/Aria2-Trackers) |
| [kakaruoterl/vless_install](https://github.com/kakaruoterl/vless_install) | 29 | 超过 2272 天无代码提交 | [进入取消 Star](https://github.com/kakaruoterl/vless_install) |
| [stupidloud/nanopi-openwrt](https://github.com/stupidloud/nanopi-openwrt) | 5,510 | 超过 936 天无代码提交 | [进入取消 Star](https://github.com/stupidloud/nanopi-openwrt) |
| [atrandys/trojan](https://github.com/atrandys/trojan) | 1,055 | 超过 1305 天无代码提交 | [进入取消 Star](https://github.com/atrandys/trojan) |
| [programthink/zhao](https://github.com/programthink/zhao) | 14,166 | 超过 1925 天无代码提交 | [进入取消 Star](https://github.com/programthink/zhao) |
| [RPRX/v2ray-vless](https://github.com/RPRX/v2ray-vless) | 390 | 超过 1351 天无代码提交 | [进入取消 Star](https://github.com/RPRX/v2ray-vless) |
| [h2y/Shadowrocket-ADBlock-Rules](https://github.com/h2y/Shadowrocket-ADBlock-Rules) | 16,731 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/h2y/Shadowrocket-ADBlock-Rules) |
| [p4gefau1t/trojan-go](https://github.com/p4gefau1t/trojan-go) | 8,384 | 超过 847 天无代码提交 | [进入取消 Star](https://github.com/p4gefau1t/trojan-go) |
| [Jrohy/trojan](https://github.com/Jrohy/trojan) | 5,630 | 超过 938 天无代码提交 | [进入取消 Star](https://github.com/Jrohy/trojan) |
| [mellow-io/mellow](https://github.com/mellow-io/mellow) | 3,535 | 超过 1429 天无代码提交 | [进入取消 Star](https://github.com/mellow-io/mellow) |
| [Dawneng/luci-theme-atmaterial](https://github.com/Dawneng/luci-theme-atmaterial) | 11 | 超过 1481 天无代码提交 | [进入取消 Star](https://github.com/Dawneng/luci-theme-atmaterial) |
| [trojan-gfw/igniter](https://github.com/trojan-gfw/igniter) | 3,273 | 超过 1078 天无代码提交 | [进入取消 Star](https://github.com/trojan-gfw/igniter) |
| [openwrt-develop/luci-theme-atmaterial](https://github.com/openwrt-develop/luci-theme-atmaterial) | 68 | 超过 2426 天无代码提交 | [进入取消 Star](https://github.com/openwrt-develop/luci-theme-atmaterial) |
| [trojan-gfw/trojan-quickstart](https://github.com/trojan-gfw/trojan-quickstart) | 244 | 超过 2027 天无代码提交 | [进入取消 Star](https://github.com/trojan-gfw/trojan-quickstart) |
| [FunctionClub/ZBench](https://github.com/FunctionClub/ZBench) | 1,173 | 超过 2058 天无代码提交 | [进入取消 Star](https://github.com/FunctionClub/ZBench) |
| [veekxt/v2ray-template](https://github.com/veekxt/v2ray-template) | 749 | 超过 2270 天无代码提交 | [进入取消 Star](https://github.com/veekxt/v2ray-template) |
| [HMBSbige/ShadowsocksR-Windows](https://github.com/HMBSbige/ShadowsocksR-Windows) | 6,900 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/HMBSbige/ShadowsocksR-Windows) |
| [trojan-gfw/trojan](https://github.com/trojan-gfw/trojan) | 19,744 | 超过 809 天无代码提交 | [进入取消 Star](https://github.com/trojan-gfw/trojan) |
</details>
