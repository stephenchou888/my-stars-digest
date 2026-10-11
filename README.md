# 📡 Starred 项目雷达看板
> **生成时间**：`2026-10-11` ｜ **关注项目总数**：`353` ｜ **本期更新**：`58` ｜ **弃坑预警**：`136`

| 统计指标 | 数量 | 状态提示 |
| :--- | :---: | :--- |
| 🌟 总关注库 | **353** | 监控运行中 |
| 🚀 近期有更新 | **58** | 涵盖 6 个分类 |
| 🛑 建议清理/弃坑 | **136** | 建议取消 Star 保持关注列表整洁 |

---
## 🧭 领域分类速览导航

- [🤖 AI 与智能体生态 (29)](#-AI-与智能体生态)
- [📝 效率办公与创作 (6)](#-效率办公与创作)
- [🎬 影音媒体与下载 (7)](#-影音媒体与下载)
- [🌐 网络与代理技术 (10)](#-网络与代理技术)
- [📦 实用开源精选 (4)](#-实用开源精选)
- [🛠️ 系统与开发者工具 (2)](#-系统与开发者工具)

---

## <span id="-AI-与智能体生态">🤖 AI 与智能体生态</span>

### 📦 [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)
`⭐ Stars: 9,317` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.11.564](https://github.com/genspark-ai/genoffice/releases/tag/v0.11.564) (2026-10-11)`

> **简介**：Free, open-source AI Office suite: Docs, Sheets, Slides, PDF, Markdown and HTML editors with a built-in AI agent, plus a `genoffice` CLI and agent skill so Claude Code, Codex and Cursor can create and edit real .docx/.xlsx/.pptx files locally. Bring your own key. macOS, Windows & Linux.

**💡 核心亮点更新 (中文)**：
- **PDF:** sign PDFs with a digital certificate (.p12/.pfx or the Windows certificate store) and verify existing signatures ; Form Design saves as soon as you press Done, keeps CJK field values, validates field names and hides generated ones; Fill Form date fields accept common layouts, explain rejections and offer a calendar picker (requested by .
- **Sheets:** large streamed workbooks past the Full Load budget can now be filtered on the columns you use (reported by ; fast scrolling through many hidden rows no longer loads the whole sheet; the AutoFilter header button is drawn like Excel's; Ctrl+arrow moves word by word in the cell editor; streamed workbooks preload before print and PDF export ; the CSV guard digest follows file identity .
- **Slides:** canvas gestures match PowerPoint: one undo step per drag, Shift+marquee adds to the selection, modifier keys and guides while resizing, Escape cancels, a 3 px snap pull, and rubber-band selection survives releasing outside the canvas and drags connectors with the group.

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
GenOffice v0.11.564 stable desktop installers.

## What's New

- **PDF:** sign PDFs with a digital certificate (.p12/.pfx or the Windows certificate store) and verify existing signatures (@carloscn); Form Design saves as soon as you press Done, keeps CJK field values, validates field names and hides generated ones; Fill Form date fields accept common layouts, explain rejections and offer a calendar picker (requested by @alberk8).
- **Sheets:** large streamed workbooks past the Full Load budget can now be filtered on the columns you use (reported by @miaomiao-wzs); fast scrolling through many hidden rows no longer loads the whole sheet; the AutoFilter header button is drawn like Excel's; Ctrl+arrow moves word by word in the cell editor; streamed workbooks preload before print and PDF export (@HThanh-how); the CSV guard digest follows file identity (@tokg-venv).
- **Slides:** canvas gestures match PowerPoint: one undo step per drag, Shift+marquee adds to the selection, modifier keys and guides while resizing, Escape cancels, a 3 px snap pull, and rubber-band selection survives releasing outside the canvas and drags connectors with the group.
- **Docs:** Track Changes no longer duplicates a split or merged paragraph; a page break inside a table cell turns the page (@tokg-venv); a style template can set East Asian and Latin fonts separately (@tokg-venv, reported by @theonegis); Russian table ribbon strings and a Table Layout tab that no longer clips its third row (@FrI3nd7).
- **
```
</details>

---
### 📦 [ruvnet/RuView](https://github.com/ruvnet/RuView)
`⭐ Stars: 97,345` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v3122](https://github.com/ruvnet/RuView/releases/tag/v3122) (2026-10-10)`

> **简介**：π RuView turns commodity WiFi signals into real-time spatial intelligence, vital sign monitoring, and presence detection — all without a single pixel of video.

**💡 核心亮点更新 (中文)**：
Automated release from CI pipeline

**Changes:**
Merge pull request 2192 from clonea1/contrib/pin-led-strip-idf54

fix(firmware): pin led_strip to 3.0.x; 3.1.0 breaks ESP-IDF 5.4 builds

**Docker Image:**
`ghcr.io/ruvnet/RuView:a71634ae8a606bba546348

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Automated release from CI pipeline

**Changes:**
Merge pull request #2192 from clonea1/contrib/pin-led-strip-idf54

fix(firmware): pin led_strip to 3.0.x; 3.1.0 breaks ESP-IDF 5.4 builds

**Docker Image:**
`ghcr.io/ruvnet/RuView:a71634ae8a606bba5463489450c69e8b42de114e`
```
</details>

---
### 📦 [pascalorg/editor](https://github.com/pascalorg/editor)
`⭐ Stars: 24,802` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.0.3](https://github.com/pascalorg/editor/releases/tag/v1.0.3) (2026-09-24)`

> **简介**：开源 3D 建筑编辑器，具有本地 CLI、MCP 工具以及适用于人类和 AI 代理的实用工作流程。

**💡 核心亮点更新 (中文)**：
- GLB 和 USDZ 导出现在完成或返回可操作的超时，而不是无限期地保持进行（[#888](https://github.com/pascalorg/editor/pull/888)）。
- 隐藏站点不再清空 GLB 导出、PDF 导出或 2D 计划；子级可见性保持独立（[#907](https://github.com/pascalorg/editor/pull/907)）。
- 容器节点可见性现在在 3D 查看器中一致应用（[#908](https://github.com/pascalorg/editor/pull/908)）。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
1.0.3 brings all seven `@pascal-app/*` packages to the same version on npm `latest` and carries the export and visibility fixes into one coordinated release.

### 🐛 Fixes

- GLB and USDZ exports now finish or return an actionable timeout instead of remaining in progress indefinitely ([#888](https://github.com/pascalorg/editor/pull/888)).
- A hidden Site no longer empties GLB exports, PDF exports or the 2D plan; child visibility remains independent ([#907](https://github.com/pascalorg/editor/pull/907)).
- Container node visibility now applies consistently in the 3D viewer ([#908](https://github.com/pascalorg/editor/pull/908)).
- The CLI starts the runtime belonging to its own published version ([#893](https://github.com/pascalorg/editor/pull/893)).

### 🧰 Release

- The release workflow now aligns all seven package versions and internal ranges ([#909](https://github.com/pascalorg/editor/pull/909)).
- Package repository URLs and the MCP executable path were corrected ([#911](https://github.com/pascalorg/editor/pull/911)).

### 📦 Packages

| Package | Version |
|---|---|
| `@pascal-app/core` | `1.0.3` |
| `@pascal-app/viewer` | `1.0.3` |
| `@pascal-app/editor` | `1.0.3` |
| `@pascal-app/nodes` | `1.0.3` |
| `@pascal-app/mcp` | `1.0.3` |
| `@pascal-app/ifc-converter` | `1.0.3` |
| `@pascal-app/cli` | `1.0.3` |

The CLI downloads its checksummed portable runtime from the [`@pascal-app/cli@1.0.3`](https://github.com/pascalorg/editor/releases/tag/%40pascal-app%2Fcli%401.0.3) release
```
</details>

---
### 📦 [librepods-org/librepods](https://github.com/librepods-org/librepods)
`⭐ Stars: 30,240` &nbsp;|&nbsp; `💻 语言: Kotlin` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.0.1-rc1](https://github.com/librepods-org/librepods/releases/tag/v1.0.1-rc1) (2026-10-06)`

> **简介**：AirPods 从苹果的生态系统中解放出来。

**💡 核心亮点更新 (中文)**：
- AirPods 5 支持（[99d6d73](https://github.com/kavishdevar/librepods/commit/99d6d73add011b50b8e780fde136d8b576d77a53))
- 修复服务启动时不需要的 AirPods 自动连接 ([e81e4dd](https://github.com/kavishdevar/librepods/commit/e81e4dde16a563eb8003e16371e51f762eb1c4d8))
- 将“demo”添加到演示 AirPods 名称中以获得清晰指示（[cf6d226](https://github.com/kavishdevar/librepods/commit/cf6d226fca4570e02997a9678af3bcdf284887a2)）

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
> [!NOTE]
> Install the `.zip` files in your root manager app if you want to grant the app `BLUETOOTH_PRIVILEGED` and `MODIFY_PHONE_STATE` permissions to allow the app to 
> - Disable audio output when no AirPods are worn
> - Set Metadata like icon and battery status to make it available in system settings/widget

<a href="https://play.google.com/store/apps/details?id=me.kavishdevar.librepods"><img width="170" alt="GetItOnGooglePlay_Badge_Web_color_English" src="https://github.com/user-attachments/assets/2948308f-af92-443f-94d9-ee381c3a6ccc"/></a>

## What's changed
- AirPods 5 support ([99d6d73](https://github.com/kavishdevar/librepods/commit/99d6d73add011b50b8e780fde136d8b576d77a53))
- Fix unwanted automatic connections to AirPods on service start ([e81e4dd](https://github.com/kavishdevar/librepods/commit/e81e4dde16a563eb8003e16371e51f762eb1c4d8))
- Add `demo` to demo AirPods name for clear indication ([cf6d226](https://github.com/kavishdevar/librepods/commit/cf6d226fca4570e02997a9678af3bcdf284887a2))
- Show `bypassed` message on settings page before first AACP connection ([95ecc0e](https://github.com/kavishdevar/librepods/commit/95ecc0eb3d665eef4ea1d607551210b8c8a6beca))
- Hide reconnect button in m3e before first AACP connection ([21babd8](https://github.com/kavishdevar/librepods/commit/21babd819fc41876be4e7f3312ea31c066fb211d))
- Fix non-round icon ([c3f537b](https://github.com/kavishdevar/librepods/commit/c3f537b0e96a86dda2e2759e32f892f5040caa8e))
- Fix le
```
</details>

---
### 📦 [linshenkx/prompt-optimizer](https://github.com/linshenkx/prompt-optimizer)
`⭐ Stars: 37,562` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.11.11](https://github.com/linshenkx/prompt-optimizer/releases/tag/v2.11.11) (2026-10-09)`

> **简介**：An AI prompt optimizer for writing better prompts and getting better AI results.

**💡 核心亮点更新 (中文)**：
- Clear the evaluation model setting to restore automatic selection. The UI explains the default order and warns about deleted or disabled function models.
- Earlier evaluation responses no longer interfere with restarted evaluations, and rapid function-model changes are saved in user-action order.
- Image uploads are prepared for compatibility. Material resizing requires confirmation, and cancelling preparation leaves the existing input unchanged.

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## English

### Summary
- Corrects model selection for prompt analysis, result evaluation, and variable generation: an explicit evaluation model takes priority, followed by the global optimization model, the caller's fallback model, and the first enabled model.
- Improves reliability when models are deleted or disabled, lists are refreshed, and settings are saved, preventing stale requests from overwriting current state or using unavailable models.
- Includes persisted evaluation, image-recognition, and other known UI settings in backup and restore.
- Includes oversized-image preparation and first-time setup documentation improvements made since the previous release.

### Highlights
- Clear the evaluation model setting to restore automatic selection. The UI explains the default order and warns about deleted or disabled function models.
- Earlier evaluation responses no longer interfere with restarted evaluations, and rapid function-model changes are saved in user-action order.
- Image uploads are prepared for compatibility. Material resizing requires confirmation, and cancelling preparation leaves the existing input unchanged.

### Product Updates
#### Desktop
- Receive the shared model-selection, evaluation, and backup fixes.
- Fix repeated quit-time storage saves preventing the desktop process from exiting normally.
- Preserve compatible JPEG inputs and their format while preparing oversized model inputs; PNG conversion uses the PNG output path.

#### Web
- Improve image up
```
</details>

---
### 📦 [RSSNext/Folo](https://github.com/RSSNext/Folo)
`⭐ Stars: 39,087` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [desktop/v1.15.0](https://github.com/RSSNext/Folo/releases/tag/desktop/v1.15.0) (2026-10-02)`

> **简介**：🧡 Folo 是人工智能 RSS 阅读器

**💡 核心亮点更新 (中文)**：
- 升级至 Electron 44
- 设置同步再次涵盖所有外观、常规和AI设置；每个设备上仅保留特定于设备的内容，例如界面语言、字体和登录时启动
- 动作语言和 AI 个性化提示现已同步，因此 AI 聊天会以您选择的动作语言进行回答

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# What's new in v1.15.0

## Improvements

- Upgraded to Electron 44
- Settings sync covers every appearance, general and AI setting again; only device-specific ones such as the interface language, fonts and launch at login stay on each device
- The action language and the AI personalization prompt now sync, so AI chat answers in the action language you picked
- Finished the Simplified Chinese, Traditional Chinese, Japanese and French translations, including text that was previously hard-coded in English
- In-app bug reports and feature requests now open the matching GitHub issue form with the details filled in
- Regex conditions in Actions now show an example pattern and how to escape special characters

## No longer broken

- Fixed only device-specific settings syncing between devices since 1.6.0
- Fixed the AI settings and chat panel staying in English in Simplified and Traditional Chinese
- Fixed English title case being applied to non-English entry titles and settings labels
- Fixed names containing "&" or quotes showing HTML entities
- Fixed unread counts that stayed behind after reading new entries
- Fixed an invisible strip next to the scrollbar that blocked hovering and clicking the right edge of timeline entries
- Fixed lists missing from the All view
- Fixed social media posts showing the feed title instead of your custom subscription title
- Fixed Folo not starting hidden in the tray when launched at login on macOS
- Fixed the Dock icon ignoring the macOS dark and
```
</details>

---
### 📦 [roboflow/supervision](https://github.com/roboflow/supervision)
`⭐ Stars: 51,180` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [0.30.9](https://github.com/roboflow/supervision/releases/tag/0.30.9) (2026-10-08)`

> **简介**：我们为您编写可重复使用的计算机视觉工具。 💜

**💡 核心亮点更新 (中文)**：
- **`BoxAnnotator`** 边框在安装或未安装 OpenCV 的情况下绘制相同的像素。
- **`get_video_frames_generator`** 读取浏览器录制的 WebM 和可变帧率 MKV 到底。
- **`from_coco`**、`from_pascal_voc` 和 `from_createml` 不再使用超过 `x_max` 的 `x_min` 构建盒子。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# v0.30.9 — Closer to OpenCV without OpenCV

Installs without OpenCV now draw and resize like OpenCV, and the COCO and CreateML loaders stop accepting reversed boxes.

- **`BoxAnnotator`** borders paint the same pixels with or without OpenCV installed.
- **`get_video_frames_generator`** reads browser-recorded WebM and variable frame rate MKV to the end.
- **`from_coco`**, `from_pascal_voc` and `from_createml` no longer build boxes with `x_min` past `x_max`.
- **`get_top_k`** rejects a negative `k` instead of dropping one classification.
- **`DetectionsSmoother`** forgets expired tracks on frames without `tracker_id`.

Drop-in upgrade. Without OpenCV, borders and resized regions shift toward OpenCV's output. Negative `k`, negative COCO/CreateML box sizes and an `epsilon` that is `NaN`, infinite or `1e30` and larger are now rejected; without OpenCV, so is rectangle `thickness` above 32767.

## ✨ Spotlights / highlights

### NumPy fallback matches OpenCV

Without `opencv-python`, thick rectangle borders were drawn entirely inside the rectangle. They now extend `(thickness + 1) // 2` pixels outside it, like OpenCV. The same release fixes `cv2.resize` with `fx`/`fy` sampling the wrong source pixels (it hit `PixelateAnnotator`) and `approxPolyDP` dropping vertices that sit beyond a segment endpoint. For polygons, the fallback now follows OpenCV 4.13 and later; older OpenCV keeps the infinite-line rule, so results differ by installed backend. (#2675, #2690, #2673)
```
</details>

---
### 📦 [MetaCubeX/mihomo](https://github.com/MetaCubeX/mihomo)
`⭐ Stars: 34,802` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.19.32](https://github.com/MetaCubeX/mihomo/releases/tag/v1.19.32) (2026-09-30)`

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
`⭐ Stars: 36,289` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.3.0](https://github.com/microsoft/graphrag/releases/tag/v3.3.0) (2026-10-08)`

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
`⭐ Stars: 150,597` &nbsp;|&nbsp; `💻 语言: Rust` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.5.8](https://github.com/clash-verge-rev/clash-verge-rev/releases/tag/v2.5.8) (2026-10-09)`

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
`⭐ Stars: 77,797` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.1.905-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.905-beta) (2026-10-08)`

> **简介**：用于运行和训练法学硕士和扩散模型的本地 UI。支持 GGUF、MLX、Qwen3.8、DeepSeek-V4、MiniMax-H3、Gemma 4、FLUX 等。

**💡 核心亮点更新 (中文)**：
- **10 月 8 日修复** - 更好的浏览器 + 100 多个错误修复 + 性能修复
- **沙箱**，适用于 Linux 的 Bwrap、适用于 Mac 的 Seatbelt 和适用于 Windows 的 MXC
- **将任何模型转变为 Jev 式决策模型。** 准确度从 30% 提高到 80%

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
We're introducing Windows, Mac and Linux sandboxing in Unsloth! [Read our guide](https://unsloth.ai/docs/new/studio/sandboxing-in-unsloth). Turn any text or vision LLM into a Jev-style decision model in Unsloth, with decision accuracy going from 30% to 80%. Train, test, export and serve decision models directly from Unsloth. Also included: native ComfyUI models, diffusion improvements and a better Browser in Desktop.

## Highlights

- **8th Oct Fixes** - Better Browser + 100+ bug fixes + perf fixes
- **Sandboxing** with Bwrap for Linux, Seatbelt for Mac and MXC for Windows
- **Turn any model into a Jev-style decision model.** Accuracy went from 30% to 80%
- **Load ComfyUI diffusion models** natively in Unsloth
- **Faster + more accurate diffusion** with INT8 ConvRot and more

https://github.com/user-attachments/assets/92959172-d2a2-450b-a5bf-6369a1e5ae16

## Decision models

- Train any text or vision LLM as a Jev-style decision model using QLoRA.
- Test trained models directly from the Decision API settings.
- Make decisions with confidence scores for every option.
- Export Clef models with Qwen3.5 backbones and Laya models to GGUF.
- Serve supported decision models through llama.cpp, including models that understand images.
- Save and resume smaller adapter and decision-head checkpoints.
- Guide at https://unsloth.ai/docs/basics/train-your-own-decision-model-with-unsloth
<img width="600" height="773" alt="image" src="https://github.com/user-attachments/
```
</details>

---
### 📦 [arc53/DocsGPT](https://github.com/arc53/DocsGPT)
`⭐ Stars: 18,318` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [1.0.0](https://github.com/arc53/DocsGPT/releases/tag/1.0.0) (2026-10-08)`

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
`⭐ Stars: 83,149` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.2.19](https://github.com/lobehub/lobehub/releases/tag/v2.2.19) (2026-10-07)`

> **简介**：🤯 LobeHub 是您的首席代理运营商，通过招聘、调度和报告整个 AI 团队，将您的代理组织为 7×24 小时运营。

**💡 核心亮点更新 (中文)**：
- **桌面 OTA 核心** — 桌面被分为签名外壳和可 OTA 的核心，因此更新、重新加载和回滚以基于范围的包形式提供，而不是完全重新安装。 （#19501、#20191、#20214）
- **GitHub 应用程序闭环** — 从 Integrations 目录连接 GitHub，安装应用程序，然后让拉取请求路由回打开它们的代理； CI 失败和审查反馈现在唤醒该代理。 （＃19721，＃19728，＃19888，＃19726）
- **目标交付** — 已完成的目标会获得一个带有总结故事情节的“交付”选项卡，在工作开始之前澄清不明确的目标，并且目标的主要代理默认运行 50 回合。 （#20189、#20143、#20178）

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 📦 Release v2.2.19

This release was automatically published from PR #20476.

### Changes
See PR description: https://github.com/lobehub/lobehub/pull/20476

### Commit Message
# 🚀 LobeHub Release (20261007)

**Release Date:** October 7, 2026\
**Since v2.2.18:** 546 commits · 547 merged PRs · 15 contributors

> This release turns Desktop into an over-the-air updatable shell, closes the GitHub loop from install to merge, and gives Goals, tasks, devices and tunneled ports first-class surfaces, starts moving lists onto a local-first replica — on top of a broad performance pass over the agent runtime and tool payloads.

---

## ✨ Highlights

- **Desktop OTA Core** — Desktop is split into a signed shell plus an OTA-able core, so updates, reloads and rollbacks ship as range-based packs instead of a full reinstall. (#19501, #20191, #20214)
- **GitHub App Closed Loop** — Connect GitHub from the Integrations directory, install the App, and let pull requests route back to the agent that opened them; CI failures and review feedback now wake that agent. (#19721, #19728, #19888, #19726)
- **Goal Delivery** — Finished Goals get a Delivery tab with a wrap-up storyline, ambiguous goals are clarified before work starts, and a Goal's main Agent runs 50 turns by default. (#20189, #20143, #20178)
- **Device Ports & Tunnels** — Detect listening ports on a device, expose them in one click, browse folders at the current directory, and relay HTTP/WebSocket traffic through registered tunnel links. (
```
</details>

---
### 📦 [Dooy/chatgpt-web-midjourney-proxy](https://github.com/Dooy/chatgpt-web-midjourney-proxy)
`⭐ Stars: 6,795` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.26.8](https://github.com/Dooy/chatgpt-web-midjourney-proxy/releases/tag/v2.26.8) (2026-09-29)`

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
`⭐ Stars: 29,794` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v4.17.2](https://github.com/labring/FastGPT/releases/tag/v4.17.2) (2026-10-09)`

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
`⭐ Stars: 9,870` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.3.1](https://github.com/yihong0618/bilingual_book_maker/releases/tag/v1.3.1) (2026-09-30)`

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
`⭐ Stars: 37,150` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.3.2](https://github.com/1Panel-dev/1Panel/releases/tag/v2.3.2) (2026-09-24)`

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
`⭐ Stars: 28,563` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v6.14.2](https://github.com/invoke-ai/InvokeAI/releases/tag/v6.14.2) (2026-09-27)`

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
`⭐ Stars: 147,635` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [langchain-core==1.6.9](https://github.com/langchain-ai/langchain/releases/tag/langchain-core%3D%3D1.6.9) (2026-10-08)`

> **简介**：代理工程平台。

**💡 核心亮点更新 (中文)**：
自 langchain-core==1.6.8 以来的变化

版本（核心）：1.6.9 (41160)
feat(core)：接受 with_retry 中的可调用（41158）

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Changes since langchain-core==1.6.8

release(core): 1.6.9 (#41160)
feat(core): accept a callable in with_retry (#41158)
```
</details>

---
### 📦 [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)
`⭐ Stars: 187,526` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [autogpt-platform-beta-v0.8.3](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.8.3) (2026-10-08)`

> **简介**：AutoGPT 的愿景是为每个人提供易于使用和构建的人工智能。我们的使命是提供工具，以便您可以专注于重要的事情。

**💡 核心亮点更新 (中文)**：
- **#14990** - 向 PostHog 报告 OAuth 启动和交换失败（通过
- **#15052** - 让用户编辑并组合问题卡中的建议答案（通过
- **#15069** - 从链接的 Discord、Slack、Teams 或 Telegram 服务器驱动的聊天在频道中作为本机按钮获取批准卡（通过

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
# 🚀 Release `autogpt-platform-beta-v0.8.3`

**Date:** October 2026

---

## 🔥 What's New?

### New Features
- **#14990** - Report OAuth starts and exchange failures to PostHog (by @kcze)
- **#15052** - Let users edit and combine suggested answers in question cards (by @0ubbe)
- **#15069** - A chat driven from a linked Discord, Slack, Teams or Telegram server gets its approval cards in the channel as native buttons (by @Pwuts)
- **#15138** - `ENABLE_USER_NOTIFICATIONS` switch so prod can send auth emails only (by @Bentlybro)
- **#15145** - Add Clip's avatar and roster pins for the 33rd roster expert (by @ntindle)
- **#15146** - Add Clip's avatar and roster pins for the 33rd roster expert (hotfix) (by @ntindle)
- **#14951** - Add official PayPal MCP Server to MCP catalog (by @ntindle)
- **#15070** - Add GPT-6.1 Sol to the LLM catalog (by @ntindle)
- **#14836** - Send signup, onboarding, checkout and churn events to PostHog (by @kcze)
- **#15134** - Add official Canva MCP Server to MCP catalog (by @ntindle)
- **#15053** - Ordinary sandbox work never asks; outward commands and unrequested deletes of the user's files still do (by @Pwuts)
- **#15203** - Add Mistral Large 4 (by @ntindle)
- **#15210** - Add Mistral Medium 3.5, Small 4 and Ministral 3, and retire Medium 3.1 and Small 3.2 (by @Pwuts)
- **#15188** - Add GitHub repository traffic block (views, clones, referrers, popular content) (by @ntindle)
- **#15191** - Add Hacker News search, stories, item and
```
</details>

---
### 📦 [rockbenben/ChatGPT-Shortcut](https://github.com/rockbenben/ChatGPT-Shortcut)
`⭐ Stars: 8,815` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v4.5.1](https://github.com/rockbenben/ChatGPT-Shortcut/releases/tag/v4.5.1) (2026-10-09)`

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
`⭐ Stars: 2,801` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [userscript-v2.37.0](https://github.com/pionxzh/chatgpt-exporter/releases/tag/userscript-v2.37.0) (2026-10-11)`

> **简介**：Export and Share your ChatGPT conversation history

**💡 核心亮点更新 (中文)**：
* choose how Markdown exports save images ([ec966c5](https://github.com/pionxzh/chatgpt-exporter/commit/ec966c51654c2726fec78b4b10f041be69999979)), closes [#405](https://github.com/pionxzh/chatgpt-exporter/issues/405)
* save JSON (ZIP) images as files too ([82ec4bc](https://github.com/pionxzh/chatgpt-exporter/commit/82ec4bcfea9f6c651393861dbdf7c8eae8330045)), closes [#295](https://github.com/pionxzh/chatgpt-exporter/issues/295)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## [2.37.0](https://github.com/pionxzh/chatgpt-exporter/compare/userscript-v2.36.3...userscript-v2.37.0) (2026-10-11)


### Features

* choose how Markdown exports save images ([ec966c5](https://github.com/pionxzh/chatgpt-exporter/commit/ec966c51654c2726fec78b4b10f041be69999979)), closes [#405](https://github.com/pionxzh/chatgpt-exporter/issues/405)
* save JSON (ZIP) images as files too ([82ec4bc](https://github.com/pionxzh/chatgpt-exporter/commit/82ec4bcfea9f6c651393861dbdf7c8eae8330045)), closes [#295](https://github.com/pionxzh/chatgpt-exporter/issues/295)


### Bug Fixes

* keep assistant text as written in markdown and text exports ([4c8fe6e](https://github.com/pionxzh/chatgpt-exporter/commit/4c8fe6ea01d58a59bc59aea9ba1421fee7d80969))


### Performance Improvements

* compile markdown to HTML with micromark directly ([f9d9e4c](https://github.com/pionxzh/chatgpt-exporter/commit/f9d9e4c1b0d59f38b7b83dd65bb5967bfbd34609))
```
</details>

---
### 📦 [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent)
`⭐ Stars: 47,347` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [2.2.0](https://github.com/zhayujie/CowAgent/releases/tag/2.2.0) (2026-09-30)`

> **简介**：开源个人人工智能助理和代理线束。计划任务，运行工具和技能，利用记忆和知识进行自我进化。多代理、多模式、多渠道。轻量级、可扩展、单行安装。

**💡 核心亮点更新 (中文)**：
- **技能安装**：从 Cow Skill Hub、GitHub 或 ClawHub 安装，或上传存档、`SKILL.md` 或文件夹。每个技能都会先预览，确认后才安装。
- **MCP 配置**：在 UI 中添加、编辑和删除 MCP 服务器，涵盖 stdio、SSE 和 Streamable HTTP 传输。表单和 JSON 编辑均可用，您可以直接粘贴一个或多个“mcpServers”条目。保存检查连接并列出服务器的工具；更改将在下一条消息时生效，无需重新启动。谢谢（#3155）
- **工具检索诊断**：查看 MCP 工具的排名以及检索在对话期间回落的原因，从而更容易找出工具未被选择的原因。谢谢（#3165）

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
🌐 [English](https://docs.cowagent.ai/releases/v2.2.0) | [中文](https://docs.cowagent.ai/zh/releases/v2.2.0)

## 🧩 Capabilities Center

The former **Skills** menu is now **Capabilities**, a single place in the Web console and desktop client to manage built-in tools, MCP tools, and skills:

- **Skill installation**: install from Cow Skill Hub, GitHub, or ClawHub, or upload an archive, a `SKILL.md`, or a folder. Every skill is previewed first and only installed after you confirm.
- **MCP configuration**: add, edit, and remove MCP servers in the UI, covering the stdio, SSE, and Streamable HTTP transports. Both form and JSON editing are available, and you can paste one or more `mcpServers` entries directly. Saving checks the connection and lists the server's tools; changes take effect on the next message without a restart. Thanks @tsumon (#3155)
- **Tool retrieval diagnostics**: see how MCP tools were ranked and why retrieval fell back during a conversation, making it easier to find out why a tool was not picked. Thanks @zhongjunqi7657 (#3165)

<img src="https://cdn.jsdelivr.net/gh/zhayujie/cowagent-assets@main/screenshots/en/capabilities-overview.png" alt="Capabilities" width="800" />

Related docs: [MCP Tools](https://docs.cowagent.ai/tools/mcp), [Installing Skills](https://docs.cowagent.ai/skills/install)

## 🤝 Multi-Agent Collaboration

- **Task handoff as separate messages**: when an Agent delegates a task to a team member, the member's reply streams as its own
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
### 📦 [mack-a/v2ray-agent](https://github.com/mack-a/v2ray-agent)
`⭐ Stars: 22,064` &nbsp;|&nbsp; `💻 语言: Shell` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.5.25](https://github.com/mack-a/v2ray-agent/releases/tag/v3.5.25) (2026-09-15)`

> **简介**：Xray、Tuic、hysteria2、sing-box 八合一一键脚本

**💡 核心亮点更新 (中文)**：
feat(脚本): 修复xray无法启动的问题

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
feat(脚本): 修复xray无法启动的问题
```
</details>

---
### 📦 [electerm/electerm](https://github.com/electerm/electerm)
`⭐ Stars: 15,337` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v5.5.76](https://github.com/electerm/electerm/releases/tag/v5.5.76) (2026-10-08)`

> **简介**：📻免费开源终端/ssh/sftp/ftp/telnet/串口/RDP/VNC/Spice客户端(Linux, Mac, Windows, Android, HarmonyOS, iOS)

**💡 核心亮点更新 (中文)**：
- 添加选择加入设置，以在切换到具有更多窗格的布局时将选项卡分布在窗格上（#4571）
- 支持复制书签数据
- 支持将 electterm 命令安装到 PATH，修复安装功能 (#4565)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
### New features/UI/Updates

- Add opt-in setting to spread tabs over panes when switching to a layout with more panes (#4571) by @swoogi
- Support copy bookmark data
- Support install electerm command to PATH, fix install function (#4565)
- Support table render in AI chat content
- Add AtomGit mirror for upgrade
- Show session stopped notice with reload / close shortcuts tip for error terminal (#4573)
- Improve data safety, avoid data damage in import/sync in some cases

### Bug fixes

- Fix Windows startup directories to use PowerShell syntax (#4572) by @curforever
- Fix scroll select in tmux (#4559) (#4566)
- Fix theme color related functions

-----

### 新功能/界面/更新

- 新增选项：切换到窗格更多的布局时将标签页分散到各个窗格 (#4571)（由 @swoogi 提供）
- 支持复制书签数据
- 支持将 electerm 命令安装到 PATH，并修复安装函数 (#4565)
- AI 对话内容支持表格渲染
- 新增 AtomGit 升级镜像
- 异常终端显示会话已停止提示及重新加载/关闭快捷键提示 (#4573)
- 提升数据安全性，避免导入/同步等场景下的数据损坏

### 问题修复

- 修复 Windows 启动目录使用 PowerShell 语法的问题 (#4572)（由 @curforever 提供）
- 修复 tmux 中滚动选择问题 (#4559) (#4566)
- 修复主题颜色相关函数

-------

Download下载: [https://electerm.org](https://electerm.org)
```
</details>

---
### 📦 [XX-net/XX-Net](https://github.com/XX-net/XX-Net)
`⭐ Stars: 33,445` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [5.16.7](https://github.com/XX-net/XX-Net/releases/tag/5.16.7) (2026-09-28)`

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
`⭐ Stars: 34,170` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [1.1.4](https://github.com/FreeCAD/FreeCAD/releases/tag/1.1.4) (2026-09-28)`

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
`⭐ Stars: 9,507` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [v154.0.8037.49-4](https://github.com/klzgrad/naiveproxy/releases/tag/v154.0.8037.49-4) (2026-10-07)`

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

## <span id="-效率办公与创作">📝 效率办公与创作</span>

### 📦 [robbietilton/Compositor](https://github.com/robbietilton/Compositor)
`⭐ Stars: 15,881` &nbsp;|&nbsp; `💻 语言: Swift` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.4.10](https://github.com/robbietilton/Compositor/releases/tag/v1.4.10) (2026-10-11)`

> **简介**：The Photoshop alternative for Mac

**💡 核心亮点更新 (中文)**：
- Spot Healing and Content-Aware Fill rebuilt: edges and texture carry on through what's removed
- Import a folder of images as layers, from Import Image or by dropping it on the canvas, a tab or the Dock
- Gaussian Blur: Preserve Transparency, and solid edges for a picture filling the canvas

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
- Spot Healing and Content-Aware Fill rebuilt: edges and texture carry on through what's removed
- Import a folder of images as layers, from Import Image or by dropping it on the canvas, a tab or the Dock
- Gaussian Blur: Preserve Transparency, and solid edges for a picture filling the canvas
- RAW develop adds Noise Reduction, Lens Correction and Highlight Recovery
- Opens HEIF photos from Canon, Sony and Fuji cameras (.hif, .heif)
- The Layers panel keeps everything inside it at its narrowest
- A new app icon
```
</details>

---
### 📦 [jgraph/drawio-desktop](https://github.com/jgraph/drawio-desktop)
`⭐ Stars: 63,465` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v32.4.1](https://github.com/jgraph/drawio-desktop/releases/tag/v32.4.1) (2026-10-09)`

> **简介**：Official electron build of draw.io

**💡 核心亮点更新 (中文)**：
- Uses electron 44.7.0
- Asks before reading a local file named in Extras > Configuration (libraries, templates or fonts) for the first time, and reads the configuration once when a window opens, so script in the page can no longer make other files on the computer readable by changing it. Files already configured before this update keep working without a prompt
- Reads urlParams.json from the installation folder or the draw.io user data folder only, no longer from the folder draw.io was started in, which on Windows is the folder of a diagram opened from Explorer. A urlParams.json kept elsewhere needs to move to the user data folder (~/Library/Application Support/draw.io on macOS, %APPDATA%\draw.io on Windows). The file can no longer override settings the app manages itself, such as Google Fonts and spell checking

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Release Notes for 32.4.1

[Windows Installer](https://github.com/jgraph/drawio-desktop/releases/download/v32.4.1/draw.io-32.4.1-windows-installer.exe)
[Windows No Installer (zip)](https://github.com/jgraph/drawio-desktop/releases/download/v32.4.1/draw.io-32.4.1-windows.zip)
[macOS - Universal](https://github.com/jgraph/drawio-desktop/releases/download/v32.4.1/draw.io-universal-32.4.1.dmg)
Linux - [deb](https://github.com/jgraph/drawio-desktop/releases/download/v32.4.1/drawio-amd64-32.4.1.deb), [AppImage](https://github.com/jgraph/drawio-desktop/releases/download/v32.4.1/drawio-x86_64-32.4.1.AppImage) or [rpm](https://github.com/jgraph/drawio-desktop/releases/download/v32.4.1/drawio-x86_64-32.4.1.rpm)

**ChangeLog:**

- Uses electron 44.7.0
- Asks before reading a local file named in Extras > Configuration (libraries, templates or fonts) for the first time, and reads the configuration once when a window opens, so script in the page can no longer make other files on the computer readable by changing it. Files already configured before this update keep working without a prompt
- Reads urlParams.json from the installation folder or the draw.io user data folder only, no longer from the folder draw.io was started in, which on Windows is the folder of a diagram opened from Explorer. A urlParams.json kept elsewhere needs to move to the user data folder (~/Library/Application Support/draw.io on macOS, %APPDATA%\draw.io on Windows). The file can no longer override setting
```
</details>

---
### 📦 [Stirling-Tools/Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF)
`⭐ Stars: 94,009` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.1.0](https://github.com/Stirling-Tools/Stirling-PDF/releases/tag/v3.1.0) (2026-10-05)`

> **简介**：GitHub 上排名第一的 PDF 应用程序，可让您在任何地方的任何设备上编辑 PDF

**💡 核心亮点更新 (中文)**：
此版本再次出现一些重大变化！
群组签名（称为 Stirling Sign）即将退出 Alpha 版，现在默认为新用户启用，使用它，您可以在整个组织中共享、跟踪和签署 PDF。它还配备了全新的

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Some big changes in this release yet again!
Group signing (Called Stirling Sign) is moving out of alpha and is now being enabled by default for new users, with it, you can share, track, and sign PDFs across your org. It also comes with a brand new sign UI, drastically improving the user experience of signing. Please let us know if you have any issues with it!

We are also shipping a new embedded conversion tool called "Stirling Office Convert" which we are trialing, It aims to give better conversion results faster and with less memory. This is a beta, so please compare and let us know! (Enable it by default under Advanced > Feature Flags)

We have a ton of other features in this release:

- Text editor supports editing tables directly in file!
- Text editor supports editing OCRed image PDFs! 
- Text editor UI and UX improvements
- Attachments Support improvements (Add, rename, extract, delete etc)
- Several Dependency updates

And to mention again: 
- Brand new Group signing UI 
- New PDF conversion tool, hopefully to replace the old tool in the future (and coming to native desktop soon!) 
- Sign tool improvements

We also fixed some bugs including
- Certain translations missing
- Account linking not working for certain versions
- Auto rotate not working on desktop
- Selfhost users shown invalid teams menu
- Desktop not correctly updating itself sometimes


## What's Changed
### Bug Fixes
* fix(viewer): carry view state across a reload on plugin ev
```
</details>

---
### 📦 [emoacht/Monitorian](https://github.com/emoacht/Monitorian)
`⭐ Stars: 4,749` &nbsp;|&nbsp; `💻 语言: C#` &nbsp;|&nbsp; `🏷️ 最新版本: [4.16.1-Installer](https://github.com/emoacht/Monitorian/releases/tag/4.16.1-Installer) (2026-09-25)`

> **简介**：轻松调节多台显示器亮度的 Windows 桌面工具

**💡 核心亮点更新 (中文)**：
- 添加和修改波兰语 (pl-PL) 语言。感谢！

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
- Add and modifty Polish (pl-PL) langauge. Thank to @Blizzeq!
```
</details>

---
### 📦 [TDesktop-x64/tdesktop](https://github.com/TDesktop-x64/tdesktop)
`⭐ Stars: 2,968` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.2.10](https://github.com/TDesktop-x64/tdesktop/releases/tag/v1.2.10) (2026-09-21)`

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
`⭐ Stars: 193,586` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [1.141.0](https://github.com/microsoft/vscode/releases/tag/1.141.0) (2026-10-07)`

> **简介**：视觉工作室代码

**💡 核心亮点更新 (中文)**：
https://code.visualstudio.com/updates/v1_141

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
https://code.visualstudio.com/updates/v1_141
```
</details>

---

## <span id="-影音媒体与下载">🎬 影音媒体与下载</span>

### 📦 [guohuiyuan/go-music-dl](https://github.com/guohuiyuan/go-music-dl)
`⭐ Stars: 5,291` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.1.1](https://github.com/guohuiyuan/go-music-dl/releases/tag/v1.1.1) (2026-09-17)`

> **简介**：一个基于 Go 语言的全网音乐搜索与下载工具。支持 CLI 命令行与 Web 服务双模式，内置网易云、QQ、酷狗、Bilibili、汽水音乐等 10+ 个主流平台，支持多源并发搜索与无损音质解析。music-dl交流群：755087923

**💡 核心亮点更新 (中文)**：
* d5e61b2d3500974ab627a4802216589aca5f8df0 修复：更新依赖项并移除go.sum中过时条目
* 114fccf0e2a897f5fc53241fa1d82e7e84cb5f8f 功能(咪咕)：新增咪咕音频流下载与播放支持
* 34b7efc20fd934a39d4e485b5e834e7b89558151 功能：优化下载去重与文件存在性校验

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## Changelog
* d5e61b2d3500974ab627a4802216589aca5f8df0 修复：更新依赖项并移除go.sum中过时条目
* 114fccf0e2a897f5fc53241fa1d82e7e84cb5f8f 功能(咪咕)：新增咪咕音频流下载与播放支持
* 34b7efc20fd934a39d4e485b5e834e7b89558151 功能：优化下载去重与文件存在性校验
* 15f799a7d2c76cc784b5dbb878a6930705f77e31 功能：优化设置弹窗与下载相关功能
* c1b188c366ece39cb19a61d108e4fbf7c29271e5 功能：新增详情页面路径检测与返回按钮功能
* 8d2b57561bfff8292b7cafa096d3c0fcc33d5c9b 功能：更新Android SDK设置以移除过时的"tools"包
```
</details>

---
### 📦 [dyang886/Game-Cheats-Manager](https://github.com/dyang886/Game-Cheats-Manager)
`⭐ Stars: 15,213` &nbsp;|&nbsp; `💻 语言: C++` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.5.4](https://github.com/dyang886/Game-Cheats-Manager/releases/tag/v2.5.4) (2026-10-11)`

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
`⭐ Stars: 46,497` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2026.10.11-8411.a7d4000](https://github.com/DIYgod/RSSHub/releases/tag/v2026.10.11-8411.a7d4000) (2026-10-11)`

> **简介**：🧡 Everything is RSSible

**💡 核心亮点更新 (中文)**：
- ghcr.io/diygod/rsshub:a7d400051d8dc73c0a0a60197920df9d3f80b75c
- ghcr.io/diygod/rsshub:chromium-bundled-a7d400051d8dc73c0a0a60197920df9d3f80b75c
- diygod/rsshub:a7d400051d8dc73c0a0a60197920df9d3f80b75c

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
Source commit: a7d400051d8dc73c0a0a60197920df9d3f80b75c

Published multi-platform images:
- ghcr.io/diygod/rsshub:a7d400051d8dc73c0a0a60197920df9d3f80b75c
- ghcr.io/diygod/rsshub:chromium-bundled-a7d400051d8dc73c0a0a60197920df9d3f80b75c
- diygod/rsshub:a7d400051d8dc73c0a0a60197920df9d3f80b75c
- diygod/rsshub:chromium-bundled-a7d400051d8dc73c0a0a60197920df9d3f80b75c

Use these commit-specific image tags to reproduce this release. Daily Docker tags may be updated by subsequent builds.
```
</details>

---
### 📦 [amir1376/ab-download-manager](https://github.com/amir1376/ab-download-manager)
`⭐ Stars: 18,418` &nbsp;|&nbsp; `💻 语言: Kotlin` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.11.0](https://github.com/amir1376/ab-download-manager/releases/tag/v1.11.0) (2026-10-11)`

> **简介**：A Download Manager that speeds up your downloads

**💡 核心亮点更新 (中文)**：
*  made their first contribution in https://github.com/amir1376/ab-download-manager/pull/1434

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 1.11.0

### Added

- Added a speed limiter toggle to the system tray (#1458)
- Added an option to limit download speed while using other apps (#1466)
- Added an option to configure the minimum download part size (#1467)
- Added an **Open With** option to the download item menu and Download Complete dialog (long-press the **Open** button) (#1465)
- Added start and finish dates to the desktop download list (#1447)
- Show the selected item count and total content size in the desktop download list (#1445)

### Fixed

- Fixed launching the app through browser integration on macOS (#1434)
- Set window titles when creating windows (#1432)
- Fixed flickering when the NSIS installer closes the app on Windows (#1471)

### Improved

- Updated translations
- UI/UX improvements

## New Contributors
* @MohammedSaud404 made their first contribution in https://github.com/amir1376/ab-download-manager/pull/1434
```
</details>

---
### 📦 [lyswhut/lx-music-desktop](https://github.com/lyswhut/lx-music-desktop)
`⭐ Stars: 54,362` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.12.6](https://github.com/lyswhut/lx-music-desktop/releases/tag/v2.12.6) (2026-09-19)`

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
`⭐ Stars: 5,518` &nbsp;|&nbsp; `💻 语言: Less` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.4.8](https://github.com/jerrykuku/luci-theme-argon/releases/tag/v2.4.8) (2026-10-08)`

> **简介**：Argon 是一个干净整洁的 OpenWrt LuCI 主题，允许用户使用图像或视频自定义其登录界面。   它还支持明暗模式自动和手动切换。

**💡 核心亮点更新 (中文)**：
* 修复（级联）：在 https://github.com/jerrykuku/luci-theme-argon/pull/709 中为 argon 配置表单添加底部间距
* feat(sysauth): 在登录页面上渲染身份验证登录插件 https://github.com/jerrykuku/luci-theme-argon/pull/710
* 修复（sysauth）：避免在 https://github.com/jerrykuku/luci-theme-argon/pull/712 中的集中登录输入上出现蓝色轮廓

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## v2.4.8 r2 · 2026-10-09

主题和配置插件已重新打包：APK 版本为 `2.4.8-r2`，IPK 版本为 `2.4.8-2`。

- 修复 APK 在 OpenWrt 25.12 稳定版上因 ucode 依赖无法安装的问题。#715
- 修复深色模式下升级弹窗的配色和长文本换行。
- 调整通知横幅的位置与间距，避免遮挡页面内容。

The theme and config packages have been rebuilt as `2.4.8-r2` (APK) and `2.4.8-2` (IPK).

- Fix the ucode dependency that prevented APK installation on stable OpenWrt 25.12. #715
- Fix colors and text wrapping in the dark-mode firmware upgrade dialog.
- Fix notification spacing and overlapping page content.

## 安装 / Installation

| 包管理器 / Package manager | 下载格式 / Package format |
| --- | --- |
| `opkg`（OpenWrt 23.05 / 24.10、基于这些版本的 GL.iNet 固件） | `.ipk` |
| `apk-tools 3.x`（OpenWrt 25.12 等原生 APK 固件） | `.apk` |

主题、配置插件和语言包请选择相同格式。APK 包不支持 `apk-tools 2.x`。

Download the theme, config plugin and language packs in the same format. APK packages require `apk-tools 3.x`.

## What's Changed

* fix(cascade): add bottom spacing for argon config form by @TuringTrail in https://github.com/jerrykuku/luci-theme-argon/pull/709
* feat(sysauth): render Authentication Login plugins on the login page by @FuSan21 in https://github.com/jerrykuku/luci-theme-argon/pull/710
* fix(sysauth): avoid blue outline on focused login inputs by @TuringTrail in https://github.com/jerrykuku/luci-theme-argon/pull/712

## New Contributors

* @TuringTrail made their first contribution in https://github.com/jerrykuku/luci-theme-argon/pull/709

**Full Changelog**: https://github.com/jerrykuku/luci-theme-argon/compare/v2.4.7...v2.4.8
```
</details>

---
### 📦 [qier222/YesPlayMusic](https://github.com/qier222/YesPlayMusic)
`⭐ Stars: 33,367` &nbsp;|&nbsp; `💻 语言: Vue` &nbsp;|&nbsp; `🏷️ 最新版本: [v0.4.11](https://github.com/qier222/YesPlayMusic/releases/tag/v0.4.11) (2026-10-10)`

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

## <span id="-网络与代理技术">🌐 网络与代理技术</span>

### 📦 [bestruirui/BestSub](https://github.com/bestruirui/BestSub)
`⭐ Stars: 2,140` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.0.6](https://github.com/bestruirui/BestSub/releases/tag/v2.0.6) (2026-10-07)`

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
`⭐ Stars: 38,768` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.14.3](https://github.com/SagerNet/sing-box/releases/tag/v1.14.3) (2026-10-09)`

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
### 📦 [LorenEteval/Furious](https://github.com/LorenEteval/Furious)
`⭐ Stars: 1,460` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [0.8.2](https://github.com/LorenEteval/Furious/releases/tag/0.8.2) (2026-09-19)`

> **简介**：基于 PySide6 的 GUI 客户端。支持 Xray-core 和 hysteria

**💡 核心亮点更新 (中文)**：
* 修复和改进
* [Xray-core v26.9.9](https://github.com/XTLS/Xray-core/releases/tag/v26.9.9)
* [hysteria2 v2.12.3](https://github.com/HyNetworks/hysteria/releases/tag/app%2Fv2.12.3)

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
* Fixes and improvements
* [Xray-core v26.9.9](https://github.com/XTLS/Xray-core/releases/tag/v26.9.9)
* [hysteria2 v2.12.3](https://github.com/HyNetworks/hysteria/releases/tag/app%2Fv2.12.3)
```
</details>

---
### 📦 [sub-store-org/Sub-Store](https://github.com/sub-store-org/Sub-Store)
`⭐ Stars: 10,652` &nbsp;|&nbsp; `💻 语言: JavaScript` &nbsp;|&nbsp; `🏷️ 最新版本: [2.42.3](https://github.com/sub-store-org/Sub-Store/releases/tag/2.42.3) (2026-10-06)`

> **简介**：QX、Loon、Surge、Stash、Egern 和 Shadowrocket 的高级订阅管理器！

**💡 核心亮点更新 (中文)**：
* feat: 调整 sing-box TLS certificate_sha256 相关逻辑 ([a3e6106](https://github.com/sub-store-org/Sub-Store/commit/a3e6106))

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## <small>2.42.3 (2026-10-06)</small>

* feat: 调整 sing-box TLS certificate_sha256 相关逻辑 ([a3e6106](https://github.com/sub-store-org/Sub-Store/commit/a3e6106))
```
</details>

---
### 📦 [enfein/mieru](https://github.com/enfein/mieru)
`⭐ Stars: 2,584` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.38.1](https://github.com/enfein/mieru/releases/tag/v3.38.1) (2026-10-11)`

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
`⭐ Stars: 15,680` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.5.10](https://github.com/v2rayA/v2rayA/releases/tag/v2.5.10) (2026-10-09)`

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
### 📦 [HyNetworks/hysteria](https://github.com/HyNetworks/hysteria)
`⭐ Stars: 22,645` &nbsp;|&nbsp; `💻 语言: Go` &nbsp;|&nbsp; `🏷️ 最新版本: [app/v2.13.0](https://github.com/HyNetworks/hysteria/releases/tag/app/v2.13.0) (2026-10-05)`

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
### 📦 [Loyalsoldier/v2ray-rules-dat](https://github.com/Loyalsoldier/v2ray-rules-dat)
`⭐ Stars: 20,853` &nbsp;|&nbsp; `💻 语言: Other` &nbsp;|&nbsp; `🏷️ 最新版本: [202610112207](https://github.com/Loyalsoldier/v2ray-rules-dat/releases/tag/202610112207) (2026-10-11)`

> **简介**：🦄 🎃 👻 V2Ray 路由规则文件加强版，可代替 V2Ray 官方 geoip.dat 和 geosite.dat，适用于 V2Ray、Xray-core、mihomo(Clash-Meta)、hysteria、Trojan-Go 和 leaf。Enhanced edition of V2Ray rules dat files, applicable to V2Ray, Xray-core, mihomo(Clash-Meta), hysteria, Trojan-Go and leaf.

**💡 核心亮点更新 (中文)**：
该版本未提供详细更新说明。

---
### 📦 [Openwrt-Passwall/openwrt-passwall](https://github.com/Openwrt-Passwall/openwrt-passwall)
`⭐ Stars: 9,948` &nbsp;|&nbsp; `💻 语言: Lua` &nbsp;|&nbsp; `🏷️ 最新版本: [26.10.4-1](https://github.com/Openwrt-Passwall/openwrt-passwall/releases/tag/26.10.4-1) (2026-10-04)`

> **简介**：暂无项目描述

**💡 核心亮点更新 (中文)**：
* 请按照 [openwrt-passwall-build](https://github.com/moetayuko/openwrt-passwall-build) 仓库的说明，将其提供的软件源添加到设备中，然后直接使用包管理器安装。
* 从 [SourceForge](https://sourceforge.net/projects/openwrt-passwall-build/files/) 下载预构建的软件包。
* 将文件上传到您的设备，使用 Shell 命令进行安装。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
![](https://img.shields.io/github/downloads/Openwrt-Passwall/openwrt-passwall/26.10.4-1/total?style=flat-square)
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
`⭐ Stars: 117,875` &nbsp;|&nbsp; `💻 语言: C#` &nbsp;|&nbsp; `🏷️ 最新版本: [7.25.4](https://github.com/2dust/v2rayN/releases/tag/7.25.4) (2026-09-30)`

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
* https://github.com/XTLS/Xray-core/releases/tag/v26.9.30



### [发布文件介绍，不知道下载哪个文件的请看](https://github.com/2dust/v2rayN/wiki/Release-files-introduction)
```
</details>

---

## <span id="-实用开源精选">📦 实用开源精选</span>

### 📦 [kenzok8/compile-package](https://github.com/kenzok8/compile-package)
`⭐ Stars: 164` &nbsp;|&nbsp; `💻 语言: Shell` &nbsp;|&nbsp; `🏷️ 最新版本: [2026.10.11-19/51_arm_cortex-a15_neon-vfpv4](https://github.com/kenzok8/compile-package/releases/tag/2026.10.11-19/51_arm_cortex-a15_neon-vfpv4) (2026-10-11)`

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
`⭐ Stars: 11,865` &nbsp;|&nbsp; `💻 语言: Python` &nbsp;|&nbsp; `🏷️ 最新版本: [v3.1.4](https://github.com/jxxghp/MoviePilot/releases/tag/v3.1.4) (2026-10-11)`

> **简介**：NAS媒体库自动化管理工具

**💡 核心亮点更新 (中文)**：
- 新增插件扩展的 AI 助手形象，支持在助手面板中预览和切换，管理员可设置默认形象。
- 优化悬浮助手的贴边收起、位置记忆和形象加载，刷新后恢复已选形象，并改善气泡定位与减少动态效果的适配。
- 优化下载卡片、整理历史和文件列表的布局、长路径显示与排序；改善移动端悬浮按钮交互，修复版本历史列表标记。

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
## 本次更新内容

**🚀 v3.1.4 更新内容**

- 新增插件扩展的 AI 助手形象，支持在助手面板中预览和切换，管理员可设置默认形象。
- 优化悬浮助手的贴边收起、位置记忆和形象加载，刷新后恢复已选形象，并改善气泡定位与减少动态效果的适配。
- 优化下载卡片、整理历史和文件列表的布局、长路径显示与排序；改善移动端悬浮按钮交互，修复版本历史列表标记。
- 优化订阅补全搜索：限制单个来源最多翻查 20 页，减少持续不匹配的 IMDb 查询；整季缺失时完整收集资源，让后页整季包参与择优。
- 提升下载可靠性：缺少站点凭据时按匹配配置补齐，空白保存路径使用默认目录，并遵守站点限流与配额冷却。
- 修复工作流中种子上下文在持久化、过滤和添加下载节点之间传递的问题，恢复节点输出供后续步骤使用。
- 修复插件依赖恢复与启停状态刷新，避免停用插件的依赖约束干扰已启用插件。
- 改善 Agent 与工具兼容性：兼容媒体类型参数，Python 执行环境继承部署配置，修复 CLI 对 MCP/REST 工具结果的解析。
- 加强整理任务异常处理：未被处理的执行异常转入人工复核，避免任务无限自动重放。

## 完整变更记录

- ci: preserve manual release summaries and raw changelog by @jxxghp ([63e30e4](https://github.com/jxxghp/MoviePilot/commit/63e30e453bc52790f722031d896bc9e1dbc9ae66))
- test: align release contract and isolate search media mocks by @jxxghp ([4f3424d](https://github.com/jxxghp/MoviePilot/commit/4f3424dcdb5a198d07db4a648dbf8373736240df))
- test: mock media singleton instance at search boundary by @jxxghp ([736b668](https://github.com/jxxghp/MoviePilot/commit/736b6686c3eb559187945e2172fcf3d1756a9ba6))
- fix(api): accept agent media type values by @pyss56 ([0d62815](https://github.com/jxxghp/MoviePilot/commit/0d62815a0fa997d6034f8ea842b1f092a03f6e79))
- fix: isolate unhandled durable transfer failures by @jxxghp ([bb29451](https://github.com/jxxghp/MoviePilot/commit/bb2945122280701f81d4a4252ce4b2e87d556c45))
- fix(plugin): recover dependencies without disabled constraints by @jxxghp ([b663825](https://github.com/jxxghp/MoviePilot/commit/b663825fe704408f77747c41693eb902e386c4
```
</details>

---
### 📦 [sandboxie-plus/Sandboxie](https://github.com/sandboxie-plus/Sandboxie)
`⭐ Stars: 19,674` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.18.6](https://github.com/sandboxie-plus/Sandboxie/releases/tag/v1.18.6) (2026-10-11)`

> **简介**：Sandboxie Plus & Classic

**💡 核心亮点更新 (中文)**：
![0 5 5](https://user-images.githubusercontent.com/3890945/105014988-575cb680-5a41-11eb-90d5-d942d28184b2.png)

Release Notes

Sandboxie Plus 1.18.6 brings several fixes that improve stability and reliability, alongside expanded language support.

<details>
<summary>🔍 点击展开查看官方原版 Release 说明 (Raw Notes)</summary>

```markdown
![0 5 5](https://user-images.githubusercontent.com/3890945/105014988-575cb680-5a41-11eb-90d5-d942d28184b2.png)

### Release Notes

Sandboxie Plus 1.18.6 brings several fixes that improve stability and reliability, alongside expanded language support. This release adds Persian (Farsi) translations for SandMan, the Troubleshooting Wizard, and the installer, thanks to imalyzer’s contribution, making Sandboxie Plus more accessible to Persian-speaking users.

This update fixes an issue in SandMan where URL-encoded characters were incorrectly interpreted as message placeholders, resulting in corrupted SBIE message links. It also resolves updater issues to make the update process more reliable.

Further corrections address transient exemption handling and path handling, improving reliability in these areas. A potential null pointer exception when unloading the driver has also been fixed, preventing a possible crash during driver shutdown.

For a full list of changes please review the [change log](https://github.com/sandboxie-plus/Sandboxie/blob/master/CHANGELOG.md#1186--5736---2026-10-11).


#### You can support the project through donations, any help will be greatly appreciated.

[<img src="https://www.paypalobjects.com/en_US/AT/i/btn/btn_donateCC_LG.gif">](https://xanasoft.com/go.php?to=donate)

#### If you have issues with an update installation, just uninstall the previous version keeping the sandboxie.ini and reinstall the new build.
```
</details>

---
### 📦 [HMBSbige/NatTypeTester](https://github.com/HMBSbige/NatTypeTester)
`⭐ Stars: 4,880` &nbsp;|&nbsp; `💻 语言: C#` &nbsp;|&nbsp; `🏷️ 最新版本: [10.0.10](https://github.com/HMBSbige/NatTypeTester/releases/tag/10.0.10) (2026-10-08)`

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
`⭐ Stars: 3,380` &nbsp;|&nbsp; `💻 语言: TypeScript` &nbsp;|&nbsp; `🏷️ 最新版本: [v2.26.8](https://github.com/Icalingua-plus-plus/Icalingua-plus-plus/releases/tag/v2.26.8) (2026-09-23)`

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
`⭐ Stars: 79,922` &nbsp;|&nbsp; `💻 语言: C` &nbsp;|&nbsp; `🏷️ 最新版本: [v1.1.18](https://github.com/ventoy/Ventoy/releases/tag/v1.1.18) (2026-10-09)`

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
| [cityflow-project/CityFlow](https://github.com/cityflow-project/CityFlow) | 1,026 | 超过 418 天无代码提交 | [进入取消 Star](https://github.com/cityflow-project/CityFlow) |
| [facebookresearch/demucs](https://github.com/facebookresearch/demucs) | 10,370 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/facebookresearch/demucs) |
| [JimmyLv/awesome-nano-banana](https://github.com/JimmyLv/awesome-nano-banana) | 8,807 | 超过 398 天无代码提交 | [进入取消 Star](https://github.com/JimmyLv/awesome-nano-banana) |
| [btjawa/BiliTools](https://github.com/btjawa/BiliTools) | 5,067 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/btjawa/BiliTools) |
| [ehang-io/nps](https://github.com/ehang-io/nps) | 34,248 | 超过 864 天无代码提交 | [进入取消 Star](https://github.com/ehang-io/nps) |
| [ReturnFI/Blitz](https://github.com/ReturnFI/Blitz) | 1,092 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/ReturnFI/Blitz) |
| [kkangert/kspider](https://github.com/kkangert/kspider) | 1,267 | 超过 783 天无代码提交 | [进入取消 Star](https://github.com/kkangert/kspider) |
| [xenova/whisper-web](https://github.com/xenova/whisper-web) | 3,347 | 超过 740 天无代码提交 | [进入取消 Star](https://github.com/xenova/whisper-web) |
| [shadowsocks/luci-app-shadowsocks](https://github.com/shadowsocks/luci-app-shadowsocks) | 1,151 | 超过 1232 天无代码提交 | [进入取消 Star](https://github.com/shadowsocks/luci-app-shadowsocks) |
| [adithya-s-k/marker-api](https://github.com/adithya-s-k/marker-api) | 984 | 超过 726 天无代码提交 | [进入取消 Star](https://github.com/adithya-s-k/marker-api) |
| [yuchannslv5/warpflare](https://github.com/yuchannslv5/warpflare) | 334 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/yuchannslv5/warpflare) |
| [vvbbnn00/WARP-Clash-API](https://github.com/vvbbnn00/WARP-Clash-API) | 8,821 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/vvbbnn00/WARP-Clash-API) |
| [ca110us/epeius](https://github.com/ca110us/epeius) | 1,226 | 超过 783 天无代码提交 | [进入取消 Star](https://github.com/ca110us/epeius) |
| [chika0801/hysteria-install](https://github.com/chika0801/hysteria-install) | 178 | 超过 828 天无代码提交 | [进入取消 Star](https://github.com/chika0801/hysteria-install) |
| [yeahwu/InstallOS](https://github.com/yeahwu/InstallOS) | 86 | 超过 1586 天无代码提交 | [进入取消 Star](https://github.com/yeahwu/InstallOS) |
| [bulianglin/psub](https://github.com/bulianglin/psub) | 1,768 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/bulianglin/psub) |
| [lizongying/my-tv](https://github.com/lizongying/my-tv) | 31,963 | 超过 843 天无代码提交 | [进入取消 Star](https://github.com/lizongying/my-tv) |
| [joevess/IPTV](https://github.com/joevess/IPTV) | 10,279 | 超过 649 天无代码提交 | [进入取消 Star](https://github.com/joevess/IPTV) |
| [lecepin/WeChatVideoDownloader](https://github.com/lecepin/WeChatVideoDownloader) | 4,670 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/lecepin/WeChatVideoDownloader) |
| [linexjlin/GPTs](https://github.com/linexjlin/GPTs) | 32,043 | 超过 744 天无代码提交 | [进入取消 Star](https://github.com/linexjlin/GPTs) |
| [lxfater/Awesome-GPTs](https://github.com/lxfater/Awesome-GPTs) | 1,150 | 超过 1055 天无代码提交 | [进入取消 Star](https://github.com/lxfater/Awesome-GPTs) |
| [ClashDotNetFramework/experimental-clash](https://github.com/ClashDotNetFramework/experimental-clash) | 242 | 超过 1770 天无代码提交 | [进入取消 Star](https://github.com/ClashDotNetFramework/experimental-clash) |
| [zzzgydi/clash-verge](https://github.com/zzzgydi/clash-verge) | 21,895 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/zzzgydi/clash-verge) |
| [ddgth/cf2dns](https://github.com/ddgth/cf2dns) | 5,206 | 超过 643 天无代码提交 | [进入取消 Star](https://github.com/ddgth/cf2dns) |
| [zizifn/edgetunnel](https://github.com/zizifn/edgetunnel) | 9,231 | 超过 683 天无代码提交 | [进入取消 Star](https://github.com/zizifn/edgetunnel) |
| [missuo/Hysteria2](https://github.com/missuo/Hysteria2) | 203 | 超过 774 天无代码提交 | [进入取消 Star](https://github.com/missuo/Hysteria2) |
| [Misaka-blog/hysteria-install](https://github.com/Misaka-blog/hysteria-install) | 628 | 超过 906 天无代码提交 | [进入取消 Star](https://github.com/Misaka-blog/hysteria-install) |
| [MatsuriDayo/nekoray](https://github.com/MatsuriDayo/nekoray) | 15,315 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/MatsuriDayo/nekoray) |
| [FranzKafkaYu/x-ui](https://github.com/FranzKafkaYu/x-ui) | 8,475 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/FranzKafkaYu/x-ui) |
| [rwv/chinese-dos-games](https://github.com/rwv/chinese-dos-games) | 10,330 | 超过 795 天无代码提交 | [进入取消 Star](https://github.com/rwv/chinese-dos-games) |
| [getumbrel/llama-gpt](https://github.com/getumbrel/llama-gpt) | 10,928 | 超过 901 天无代码提交 | [进入取消 Star](https://github.com/getumbrel/llama-gpt) |
| [WangWenBin2017/OpenWrt-SSRPLUS](https://github.com/WangWenBin2017/OpenWrt-SSRPLUS) | 563 | 超过 588 天无代码提交 | [进入取消 Star](https://github.com/WangWenBin2017/OpenWrt-SSRPLUS) |
| [prompt-engineering/click-prompt](https://github.com/prompt-engineering/click-prompt) | 2,389 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/prompt-engineering/click-prompt) |
| [AutodeskAILab/Building-GAN](https://github.com/AutodeskAILab/Building-GAN) | 101 | 超过 1591 天无代码提交 | [进入取消 Star](https://github.com/AutodeskAILab/Building-GAN) |
| [novicezk/midjourney-proxy](https://github.com/novicezk/midjourney-proxy) | 5,366 | 超过 434 天无代码提交 | [进入取消 Star](https://github.com/novicezk/midjourney-proxy) |
| [adams549659584/go-proxy-bingai](https://github.com/adams549659584/go-proxy-bingai) | 8,422 | 超过 935 天无代码提交 | [进入取消 Star](https://github.com/adams549659584/go-proxy-bingai) |
| [tryptech/obs-zoom-and-follow](https://github.com/tryptech/obs-zoom-and-follow) | 440 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/tryptech/obs-zoom-and-follow) |
| [XingangPan/DragGAN](https://github.com/XingangPan/DragGAN) | 35,743 | 超过 876 天无代码提交 | [进入取消 Star](https://github.com/XingangPan/DragGAN) |
| [lewangdev/faster-whisper-youtube](https://github.com/lewangdev/faster-whisper-youtube) | 560 | 超过 1148 天无代码提交 | [进入取消 Star](https://github.com/lewangdev/faster-whisper-youtube) |
| [artidoro/qlora](https://github.com/artidoro/qlora) | 11,043 | 超过 853 天无代码提交 | [进入取消 Star](https://github.com/artidoro/qlora) |
| [langgenius/webapp-conversation](https://github.com/langgenius/webapp-conversation) | 1,101 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/langgenius/webapp-conversation) |
| [3andne/restls](https://github.com/3andne/restls) | 374 | 超过 1071 天无代码提交 | [进入取消 Star](https://github.com/3andne/restls) |
| [jtsang4/claude-to-chatgpt](https://github.com/jtsang4/claude-to-chatgpt) | 1,298 | 超过 784 天无代码提交 | [进入取消 Star](https://github.com/jtsang4/claude-to-chatgpt) |
| [yorunning/clash-conf](https://github.com/yorunning/clash-conf) | 102 | 超过 816 天无代码提交 | [进入取消 Star](https://github.com/yorunning/clash-conf) |
| [svc-develop-team/so-vits-svc](https://github.com/svc-develop-team/so-vits-svc) | 28,084 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/svc-develop-team/so-vits-svc) |
| [xiaye13579/BBLL](https://github.com/xiaye13579/BBLL) | 17,493 | 超过 590 天无代码提交 | [进入取消 Star](https://github.com/xiaye13579/BBLL) |
| [camenduru/MiniGPT-4-colab](https://github.com/camenduru/MiniGPT-4-colab) | 120 | 超过 1169 天无代码提交 | [进入取消 Star](https://github.com/camenduru/MiniGPT-4-colab) |
| [Vision-CAIR/MiniGPT-4](https://github.com/Vision-CAIR/MiniGPT-4) | 25,600 | 超过 769 天无代码提交 | [进入取消 Star](https://github.com/Vision-CAIR/MiniGPT-4) |
| [imfuxiao/Hamster](https://github.com/imfuxiao/Hamster) | 1,637 | 超过 516 天无代码提交 | [进入取消 Star](https://github.com/imfuxiao/Hamster) |
| [acheong08/ChatGPT](https://github.com/acheong08/ChatGPT) | 27,896 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/acheong08/ChatGPT) |
| [microsoft/JARVIS](https://github.com/microsoft/JARVIS) | 25,423 | 超过 439 天无代码提交 | [进入取消 Star](https://github.com/microsoft/JARVIS) |
| [choephix/auto-gpt-webui](https://github.com/choephix/auto-gpt-webui) | 116 | 超过 937 天无代码提交 | [进入取消 Star](https://github.com/choephix/auto-gpt-webui) |
| [Moonvy/OpenPromptStudio](https://github.com/Moonvy/OpenPromptStudio) | 6,691 | 超过 896 天无代码提交 | [进入取消 Star](https://github.com/Moonvy/OpenPromptStudio) |
| [facebookresearch/segment-anything](https://github.com/facebookresearch/segment-anything) | 54,986 | 超过 753 天无代码提交 | [进入取消 Star](https://github.com/facebookresearch/segment-anything) |
| [zai-org/ChatGLM-6B](https://github.com/zai-org/ChatGLM-6B) | 40,919 | 超过 836 天无代码提交 | [进入取消 Star](https://github.com/zai-org/ChatGLM-6B) |
| [ihciah/shadow-tls](https://github.com/ihciah/shadow-tls) | 2,678 | 超过 534 天无代码提交 | [进入取消 Star](https://github.com/ihciah/shadow-tls) |
| [jxbbb/ADAPT](https://github.com/jxbbb/ADAPT) | 421 | 超过 852 天无代码提交 | [进入取消 Star](https://github.com/jxbbb/ADAPT) |
| [mayooear/ai-pdf-chatbot-langchain](https://github.com/mayooear/ai-pdf-chatbot-langchain) | 16,583 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/mayooear/ai-pdf-chatbot-langchain) |
| [lencx/ChatGPT](https://github.com/lencx/ChatGPT) | 54,599 | 超过 773 天无代码提交 | [进入取消 Star](https://github.com/lencx/ChatGPT) |
| [nekohasekai/SagerNet](https://github.com/nekohasekai/SagerNet) | 54 | 超过 1735 天无代码提交 | [进入取消 Star](https://github.com/nekohasekai/SagerNet) |
| [P3TERX/Actions-OpenWrt](https://github.com/P3TERX/Actions-OpenWrt) | 7,627 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/P3TERX/Actions-OpenWrt) |
| [R86S/R86S-QuickInstaller](https://github.com/R86S/R86S-QuickInstaller) | 65 | 超过 1157 天无代码提交 | [进入取消 Star](https://github.com/R86S/R86S-QuickInstaller) |
| [WeNeedHome/SummaryOfLoanSuspension](https://github.com/WeNeedHome/SummaryOfLoanSuspension) | 20,346 | 超过 820 天无代码提交 | [进入取消 Star](https://github.com/WeNeedHome/SummaryOfLoanSuspension) |
| [zanzhz1101/LingMaxDNS](https://github.com/zanzhz1101/LingMaxDNS) | 23 | 超过 1551 天无代码提交 | [进入取消 Star](https://github.com/zanzhz1101/LingMaxDNS) |
| [IrineSistiana/mosdns-cn](https://github.com/IrineSistiana/mosdns-cn) | 325 | 超过 1593 天无代码提交 | [进入取消 Star](https://github.com/IrineSistiana/mosdns-cn) |
| [chika0801/Xray-install](https://github.com/chika0801/Xray-install) | 273 | 超过 1045 天无代码提交 | [进入取消 Star](https://github.com/chika0801/Xray-install) |
| [alesimula/wsa_pacman](https://github.com/alesimula/wsa_pacman) | 4,190 | 超过 1024 天无代码提交 | [进入取消 Star](https://github.com/alesimula/wsa_pacman) |
| [scutan90/DeepLearning-500-questions](https://github.com/scutan90/DeepLearning-500-questions) | 57,657 | 超过 837 天无代码提交 | [进入取消 Star](https://github.com/scutan90/DeepLearning-500-questions) |
| [Chikage0o0/Linux-NetSpeed](https://github.com/Chikage0o0/Linux-NetSpeed) | 3,745 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/Chikage0o0/Linux-NetSpeed) |
| [KFERMercer/OpenWrt-CI](https://github.com/KFERMercer/OpenWrt-CI) | 1,410 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/KFERMercer/OpenWrt-CI) |
| [qTox/qTox](https://github.com/qTox/qTox) | 4,974 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/qTox/qTox) |
| [quericy/one-key-ikev2-vpn](https://github.com/quericy/one-key-ikev2-vpn) | 2,104 | 超过 2155 天无代码提交 | [进入取消 Star](https://github.com/quericy/one-key-ikev2-vpn) |
| [riverscn/openwrt-iptvhelper](https://github.com/riverscn/openwrt-iptvhelper) | 371 | 超过 1871 天无代码提交 | [进入取消 Star](https://github.com/riverscn/openwrt-iptvhelper) |
| [frainzy1477/luci-app-clash](https://github.com/frainzy1477/luci-app-clash) | 1,624 | 超过 1661 天无代码提交 | [进入取消 Star](https://github.com/frainzy1477/luci-app-clash) |
| [Sanster/IOPaint](https://github.com/Sanster/IOPaint) | 23,302 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/Sanster/IOPaint) |
| [LANDrop/LANDrop](https://github.com/LANDrop/LANDrop) | 5,982 | 超过 788 天无代码提交 | [进入取消 Star](https://github.com/LANDrop/LANDrop) |
| [saveweb/review-2021](https://github.com/saveweb/review-2021) | 759 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/saveweb/review-2021) |
| [iranee/qnap-aliyunpan-webdav](https://github.com/iranee/qnap-aliyunpan-webdav) | 274 | 超过 1464 天无代码提交 | [进入取消 Star](https://github.com/iranee/qnap-aliyunpan-webdav) |
| [haoel/haoel.github.io](https://github.com/haoel/haoel.github.io) | 13,072 | 超过 1249 天无代码提交 | [进入取消 Star](https://github.com/haoel/haoel.github.io) |
| [tindy2013/stairspeedtest-reborn](https://github.com/tindy2013/stairspeedtest-reborn) | 3,841 | 超过 1221 天无代码提交 | [进入取消 Star](https://github.com/tindy2013/stairspeedtest-reborn) |
| [P3TERX/warp.sh](https://github.com/P3TERX/warp.sh) | 3,932 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/P3TERX/warp.sh) |
| [TheMRLL/WinXray](https://github.com/TheMRLL/WinXray) | 2,791 | 超过 957 天无代码提交 | [进入取消 Star](https://github.com/TheMRLL/WinXray) |
| [Mikubill/cowtransfer-uploader](https://github.com/Mikubill/cowtransfer-uploader) | 447 | 超过 1704 天无代码提交 | [进入取消 Star](https://github.com/Mikubill/cowtransfer-uploader) |
| [281677160/build-actions](https://github.com/281677160/build-actions) | 390 | 超过 439 天无代码提交 | [进入取消 Star](https://github.com/281677160/build-actions) |
| [vaxilu/x-ui](https://github.com/vaxilu/x-ui) | 19,097 | 超过 783 天无代码提交 | [进入取消 Star](https://github.com/vaxilu/x-ui) |
| [xinntao/Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) | 37,057 | 超过 796 天无代码提交 | [进入取消 Star](https://github.com/xinntao/Real-ESRGAN) |
| [zu1k/proxypool](https://github.com/zu1k/proxypool) | 4,037 | 超过 1280 天无代码提交 | [进入取消 Star](https://github.com/zu1k/proxypool) |
| [TachibanaYoshino/AnimeGAN](https://github.com/TachibanaYoshino/AnimeGAN) | 4,611 | 超过 1530 天无代码提交 | [进入取消 Star](https://github.com/TachibanaYoshino/AnimeGAN) |
| [yuanzhoulvpi2017/tiny_python](https://github.com/yuanzhoulvpi2017/tiny_python) | 173 | 超过 1344 天无代码提交 | [进入取消 Star](https://github.com/yuanzhoulvpi2017/tiny_python) |
| [haiibo/OpenWrt](https://github.com/haiibo/OpenWrt) | 3,165 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/haiibo/OpenWrt) |
| [VergilGao/openwrt-packages](https://github.com/VergilGao/openwrt-packages) | 11 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/VergilGao/openwrt-packages) |
| [VergilGao/openwrt-compiler](https://github.com/VergilGao/openwrt-compiler) | 13 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/VergilGao/openwrt-compiler) |
| [OpenELEC/OpenELEC.tv](https://github.com/OpenELEC/OpenELEC.tv) | 1,618 | 超过 3326 天无代码提交 | [进入取消 Star](https://github.com/OpenELEC/OpenELEC.tv) |
| [github/copilot-docs](https://github.com/github/copilot-docs) | 23,180 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/github/copilot-docs) |
| [Kiougar/luci-wrtbwmon](https://github.com/Kiougar/luci-wrtbwmon) | 357 | 超过 1844 天无代码提交 | [进入取消 Star](https://github.com/Kiougar/luci-wrtbwmon) |
| [EtherDream/jsproxy](https://github.com/EtherDream/jsproxy) | 9,324 | 超过 924 天无代码提交 | [进入取消 Star](https://github.com/EtherDream/jsproxy) |
| [cheat-engine/cheat-engine](https://github.com/cheat-engine/cheat-engine) | 19,304 | 超过 540 天无代码提交 | [进入取消 Star](https://github.com/cheat-engine/cheat-engine) |
| [ffffffff0x/Dork-Admin](https://github.com/ffffffff0x/Dork-Admin) | 1,918 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/ffffffff0x/Dork-Admin) |
| [ffffffff0x/Digital-Privacy](https://github.com/ffffffff0x/Digital-Privacy) | 4,944 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/ffffffff0x/Digital-Privacy) |
| [Autodesk/civilconnection](https://github.com/Autodesk/civilconnection) | 117 | 超过 1410 天无代码提交 | [进入取消 Star](https://github.com/Autodesk/civilconnection) |
| [0xHJK/CleanApps](https://github.com/0xHJK/CleanApps) | 165 | 超过 1876 天无代码提交 | [进入取消 Star](https://github.com/0xHJK/CleanApps) |
| [KANIKIG/Multi-EasyGost](https://github.com/KANIKIG/Multi-EasyGost) | 1,947 | 超过 924 天无代码提交 | [进入取消 Star](https://github.com/KANIKIG/Multi-EasyGost) |
| [Kurokosama/AutoBuild-OpenWRT](https://github.com/Kurokosama/AutoBuild-OpenWRT) | 89 | 超过 1563 天无代码提交 | [进入取消 Star](https://github.com/Kurokosama/AutoBuild-OpenWRT) |
| [differentrain/DeletionTool](https://github.com/differentrain/DeletionTool) | 94 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/differentrain/DeletionTool) |
| [hideuvpn/android-google-play-store](https://github.com/hideuvpn/android-google-play-store) | 3,614 | 超过 1544 天无代码提交 | [进入取消 Star](https://github.com/hideuvpn/android-google-play-store) |
| [XJP-GIT/AntiZhaPian](https://github.com/XJP-GIT/AntiZhaPian) | 3,162 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/XJP-GIT/AntiZhaPian) |
| [jerrykuku/luci-app-ttnode](https://github.com/jerrykuku/luci-app-ttnode) | 89 | 超过 1721 天无代码提交 | [进入取消 Star](https://github.com/jerrykuku/luci-app-ttnode) |
| [KevinSHIT/NaiveSharp](https://github.com/KevinSHIT/NaiveSharp) | 96 | 超过 2165 天无代码提交 | [进入取消 Star](https://github.com/KevinSHIT/NaiveSharp) |
| [prasmussen/gdrive](https://github.com/prasmussen/gdrive) | 8,946 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/prasmussen/gdrive) |
| [tostercx/GTAO_Booster_PoC](https://github.com/tostercx/GTAO_Booster_PoC) | 2,867 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/tostercx/GTAO_Booster_PoC) |
| [ilxp/luci-app-ikoolproxy](https://github.com/ilxp/luci-app-ikoolproxy) | 507 | 超过 576 天无代码提交 | [进入取消 Star](https://github.com/ilxp/luci-app-ikoolproxy) |
| [kiddin9/luci-app-dnsfilter](https://github.com/kiddin9/luci-app-dnsfilter) | 123 | 超过 609 天无代码提交 | [进入取消 Star](https://github.com/kiddin9/luci-app-dnsfilter) |
| [h31105/deployX.sh](https://github.com/h31105/deployX.sh) | 416 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/h31105/deployX.sh) |
| [jerrykuku/openwrt-package](https://github.com/jerrykuku/openwrt-package) | 147 | 超过 1073 天无代码提交 | [进入取消 Star](https://github.com/jerrykuku/openwrt-package) |
| [frainzy1477/luci-app-trojan](https://github.com/frainzy1477/luci-app-trojan) | 120 | 超过 1980 天无代码提交 | [进入取消 Star](https://github.com/frainzy1477/luci-app-trojan) |
| [atrandys/xray](https://github.com/atrandys/xray) | 89 | 超过 1687 天无代码提交 | [进入取消 Star](https://github.com/atrandys/xray) |
| [v2board/v2board](https://github.com/v2board/v2board) | 5,058 | 超过 936 天无代码提交 | [进入取消 Star](https://github.com/v2board/v2board) |
| [ShadowsocksR-Live/iShadowsocksR](https://github.com/ShadowsocksR-Live/iShadowsocksR) | 600 | 超过 895 天无代码提交 | [进入取消 Star](https://github.com/ShadowsocksR-Live/iShadowsocksR) |
| [SuperNG6/Aria2-Trackers](https://github.com/SuperNG6/Aria2-Trackers) | 310 | 超过 2086 天无代码提交 | [进入取消 Star](https://github.com/SuperNG6/Aria2-Trackers) |
| [kakaruoterl/vless_install](https://github.com/kakaruoterl/vless_install) | 29 | 超过 2244 天无代码提交 | [进入取消 Star](https://github.com/kakaruoterl/vless_install) |
| [stupidloud/nanopi-openwrt](https://github.com/stupidloud/nanopi-openwrt) | 5,517 | 超过 907 天无代码提交 | [进入取消 Star](https://github.com/stupidloud/nanopi-openwrt) |
| [atrandys/trojan](https://github.com/atrandys/trojan) | 1,054 | 超过 1276 天无代码提交 | [进入取消 Star](https://github.com/atrandys/trojan) |
| [programthink/zhao](https://github.com/programthink/zhao) | 14,070 | 超过 1897 天无代码提交 | [进入取消 Star](https://github.com/programthink/zhao) |
| [RPRX/v2ray-vless](https://github.com/RPRX/v2ray-vless) | 390 | 超过 1322 天无代码提交 | [进入取消 Star](https://github.com/RPRX/v2ray-vless) |
| [h2y/Shadowrocket-ADBlock-Rules](https://github.com/h2y/Shadowrocket-ADBlock-Rules) | 16,715 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/h2y/Shadowrocket-ADBlock-Rules) |
| [p4gefau1t/trojan-go](https://github.com/p4gefau1t/trojan-go) | 8,385 | 超过 819 天无代码提交 | [进入取消 Star](https://github.com/p4gefau1t/trojan-go) |
| [Jrohy/trojan](https://github.com/Jrohy/trojan) | 5,638 | 超过 910 天无代码提交 | [进入取消 Star](https://github.com/Jrohy/trojan) |
| [mellow-io/mellow](https://github.com/mellow-io/mellow) | 3,539 | 超过 1401 天无代码提交 | [进入取消 Star](https://github.com/mellow-io/mellow) |
| [Dawneng/luci-theme-atmaterial](https://github.com/Dawneng/luci-theme-atmaterial) | 11 | 超过 1453 天无代码提交 | [进入取消 Star](https://github.com/Dawneng/luci-theme-atmaterial) |
| [trojan-gfw/igniter](https://github.com/trojan-gfw/igniter) | 3,277 | 超过 1049 天无代码提交 | [进入取消 Star](https://github.com/trojan-gfw/igniter) |
| [openwrt-develop/luci-theme-atmaterial](https://github.com/openwrt-develop/luci-theme-atmaterial) | 68 | 超过 2397 天无代码提交 | [进入取消 Star](https://github.com/openwrt-develop/luci-theme-atmaterial) |
| [trojan-gfw/trojan-quickstart](https://github.com/trojan-gfw/trojan-quickstart) | 244 | 超过 1999 天无代码提交 | [进入取消 Star](https://github.com/trojan-gfw/trojan-quickstart) |
| [FunctionClub/ZBench](https://github.com/FunctionClub/ZBench) | 1,178 | 超过 2030 天无代码提交 | [进入取消 Star](https://github.com/FunctionClub/ZBench) |
| [veekxt/v2ray-template](https://github.com/veekxt/v2ray-template) | 750 | 超过 2242 天无代码提交 | [进入取消 Star](https://github.com/veekxt/v2ray-template) |
| [HMBSbige/ShadowsocksR-Windows](https://github.com/HMBSbige/ShadowsocksR-Windows) | 6,925 | 作者已正式归档 (Archived) | [进入取消 Star](https://github.com/HMBSbige/ShadowsocksR-Windows) |
| [trojan-gfw/trojan](https://github.com/trojan-gfw/trojan) | 19,760 | 超过 781 天无代码提交 | [进入取消 Star](https://github.com/trojan-gfw/trojan) |
</details>
