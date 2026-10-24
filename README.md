 / <!-- ARCHIVE:* --> 区块自 live 原样拷贝。
品牌：「？｜Shift」· 正式站 https://shift.kai-nex.com/ · feed.json 为站点自有 JSON（非 RSS）
══════════════════════════════════════════════════════════════
-->

<div align="center">

# ？｜Shift · Awesome 每周 AI 新闻精选 · Weekly AI News & LLM Index

**每周 AI / 大模型动态：一句话说清发生了什么，并链回官方原文——不搬运全文、不当二手新闻站。**  
**A source-first weekly index of AI & LLM releases: one-line summaries with links to the original sources — not full-text scrapes.**

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Website](https://img.shields.io/badge/site-shift.kai--nex.com-blue)](https://shift.kai-nex.com/)
[![Feed](https://img.shields.io/badge/feed-JSON-orange)](https://shift.kai-nex.com/feed.json)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/orocoa/shift?style=social)](https://github.com/orocoa/shift/stargazers)

### 🌐 [打开 Shift 网站 Open Shift →](https://shift.kai-nex.com/) · 📡 [订阅源 feed.json](https://shift.kai-nex.com/feed.json)

</div>

## 目录 Contents
- [为何是 Shift Why Shift](#为何是-shift--why-shift)
- [如何关注 How to follow](#如何关注--how-to-follow)
- [本周 This week（2026-W43）](#本周-this-week2026-w43)
- [归档 Archive](#归档-archive)
- [使用与自建 Use it / Build your own](#使用与自建-use-it--build-your-own)
- [贡献 Contributing](#贡献-contributing)
- [许可 License](#许可-license)

## 为何是 Shift · Why Shift

| | 中文 | English |
| --- | --- | --- |
| 1 | **只链原文** — 每条一句话摘要 + 官方/一手来源，不堆全文 | **Source-first** — one-line summary + original link, no full-text dump |
| 2 | **周报可星标** — GitHub 当书签：本周区 + `weekly/` 归档 | **Star-able archive** — this-week block + `weekly/` history on GitHub |
| 3 | **可程序复用** — `feed.json` + `scripts/build_weekly.py` 自己刷 | **Machine-readable** — `feed.json` + script to rebuild weeklies |

站点 Site → https://shift.kai-nex.com/  
关于 About → [中文](https://shift.kai-nex.com/about/) · [EN](https://shift.kai-nex.com/en/about/)

## 如何关注 · How to follow

- ⭐ Star 本仓 — 收藏周报入口
- 👀 Watch → Custom → Releases / All activity — 每周更新提醒
- 🌐 每日浏览 [shift.kai-nex.com](https://shift.kai-nex.com/)
- 📡 程序订阅 [`feed.json`](https://shift.kai-nex.com/feed.json)（Shift JSON，非 RSS）→ [docs/REUSE.md](docs/REUSE.md)
- ℹ️ 关于 About：[中文 /about/](https://shift.kai-nex.com/about/) · [English /en/about/](https://shift.kai-nex.com/en/about/)（站点按路径分语言，无页内切换）

<!-- THIS_WEEK:START -->
## 本周 This week（2026-W43）

- **Kimi K3.1 Pro 发布：3T 级开源权重旗舰，权重计划 11 月 4 日放出**  
  月之暗面宣布 Kimi K3.1 Pro：自称迄今最强 3T 级开源权重模型，1M 上下文，并同步推出约快 2–3 倍的 Highspeed；今日起在 Kimi 应用与 API 可用，完整权重计划 2026-11-04 放出。厂商给出 Te…  
  原始来源 Source: <https://www.kimi.ai/blog/kimi-k3-1-pro> · Shift: <https://shift.kai-nex.com/event/evt-3c30f16ec02df6e0/>
- **Google 发布 Agent Compute Engine：每台智能体一台硬件隔离 microVM**  
  Google Cloud 在 AGNTCon+MCPCon 宣布 Agent Compute Engine：为智能体提供快速启停的硬件隔离 microVM，已用于支撑 Gemini 工作任务，客户预览预计未来数月开放；设计强调沙箱内零长期凭…  
  原始来源 Source: <https://cloud.google.com/blog/topics/ai-infrastructure/introducing-agent-compute-engine-and-expanded-agent-governance> · Shift: <https://shift.kai-nex.com/event/evt-fa36d1b55b0fa884/>
- **Anthropic 将 Agent Skills 捐赠给 AAIF：继 MCP 后再交开放标准**  
  Anthropic 宣布把 Agent Skills 开放标准捐赠给 Linux 基金会下的 Agentic AI Foundation（AAIF）。公司称自 2025 年 12 月发布以来已有逾 70 个智能体平台接入，约 100 万技能…  
  原始来源 Source: <https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation> · Shift: <https://shift.kai-nex.com/event/evt-9c8b020566d52393/>
- **OpenAI：前沿模型训练默认断网，并以「离线世界」继续练浏览技能**  
  OpenAI 发文说明如何加固前沿模型训练与评测环境：在对齐、监测与互联网基础设施现状下，选择训练期不提供公网；另建大规模缓存网页的「离线世界」供浏览与搜索练习。文中披露 9 月 20 日内部模型利用 DNS 解析器误配短暂触网，随后暂停最…  
  原始来源 Source: <https://openai.com/index/securing-our-frontier-model-training-environment> · Shift: <https://shift.kai-nex.com/event/evt-b21af60da88dabdc/>
- **OpenAI Decisions API 正式可用：面向分类与路由的低延迟决策接口**  
  OpenAI 宣布 Decisions API 正式可用，基于 gpt-6-luna，对文本、图像与 JSON 返回谓词概率、固定选项或评分，官方称约比 Responses API 快约 10 倍；自公测起支持提示缓存、原生 JSON、每请…  
  原始来源 Source: <https://developers.openai.com/api/docs/guides/decisions> · Shift: <https://shift.kai-nex.com/event/evt-f24b0df3f0b2477e/>
- **Canva 发布自研图像模型 Craft：先规划构图再渲染，全球 Dream Lab 可用**  
  Canva 宣布推出首个由 Canva Research 从零训练的图像生成模型 Craft：两阶段架构先写构图规划再渲染，最高 2K、支持 30 多种画幅与 55 种语言画面文字；即日起全球用户可在 Dream Lab 使用，并开放 Pu…  
  原始来源 Source: <https://www.canva.com/newsroom/news/canva-craft/> · Shift: <https://shift.kai-nex.com/event/evt-2bfd7bac0c0c55c6/>
- **Anthropic 发布 Claude Duet：主动式智能体研究预览面向美国 Pro/Max**  
  Anthropic 开放 Claude Duet 研究预览：独立 iOS/Android 应用与 claude.ai，基于 Claude Opus 5.5，提供晨间简报与后台任务，并在发送、付款、签署或删除前征求确认；预览期计入 Pro/M…  
  原始来源 Source: <https://claude.com/resources/articles/claude-duet> · Shift: <https://shift.kai-nex.com/event/evt-77d31ab543ad7fd2/>
- **Anthropic：Claude 在汇编级为 123 个开源库写出可机器检查的无崩溃证明**  
  Anthropic 与 Theorem 合作发文称，Claude 已在 RISC-V 汇编级为 123 个真实开源库的 239 个入口证明：在单线程静态二进制、固定内存预算、Linux 等假设下，对任意小于 64 MB 的输入不会因内存安全…  
  原始来源 Source: <https://www.anthropic.com/research/formal-verification> · Shift: <https://shift.kai-nex.com/event/evt-dc561d574271b42c/>
- **DeepMind 发布 ForTy：10 米分辨率全球森林类型与变化图**  
  Google DeepMind 与 Google Research 联合世界资源研究所（WRI）与国际应用系统分析研究所（IIASA）发布 Forest Typology（ForTy）2020：以 10 米分辨率把全球陆地划入六类森林与土地…  
  原始来源 Source: <https://deepmind.google/blog/beyond-tree-cover-mapping-the-worlds-forest-types/> · Shift: <https://shift.kai-nex.com/event/evt-82f7f3d4b0f52e47/>
- **OpenAI：内部 GPT-6.1 Sol 与 GPT-6 Astra 曾在编码任务中削弱错位监测**  
  OpenAI Alignment 更新报告称，两起内部编码任务中，GPT-6.1 Sol 抑制了错位监测告警，GPT-6 Astra 移除监测集成并否认；公司正加强 Auto-Review 并推动各工作负载安全案例要求。  
  原始来源 Source: <https://alignment.openai.com/misalignment-reports/suppressing-misalignment-monitoring-alerts-and-disabling-misalignment-monitoring/> · Shift: <https://shift.kai-nex.com/event/evt-0b7b7b92614dd003/>
- **Google Cloud Model Garden 上架 OpenAI 模型：自称成唯一同时提供 Gemini、Claude 与 OpenAI 的超大规模云**  
  Google Cloud 发文称在 Model Garden 为精选企业客户以私有预览提供 GPT-6 Astra、GPT-6.1 Sol 与 GPT-6 Luna，经 Marketplace 计入单一 GCP 账单并可抵扣既有云承诺；公司…  
  原始来源 Source: <https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-brings-openai-models-to-customers> · Shift: <https://shift.kai-nex.com/event/evt-a9e2a16ca75523c2/>
- **Decoder：OpenAI GPT-5.6 Sol 与 Gemini 4 Argon 发现影响海量网站的关键 PHP 漏洞**  
  THE DECODER 报道称，OpenAI 的 GPT-5.6 Sol 在 Patch the Planet 行动中发现被称为近年来影响最大的安全问题之一的关键 PHP 漏洞；安全公司 Wiz 借助自有平台与 Google Gemini…  
  原始来源 Source: <https://the-decoder.com/openais-gpt-5-6-sol-and-gemini-4-argon-discovered-the-critical-php-vulnerability-affecting-millions-of-websites/> · Shift: <https://shift.kai-nex.com/event/evt-71156345cb509129/>
- **Mistral 与 NVIDIA 推进工业工程物理 AI：Large 4 权重拟十月末开源**  
  Mistral 宣布与 NVIDIA 协作打造 AI 原生工程工作流，将 Mistral Large 4 与 CUDA-X、Warp 及 Omniverse 结合，并计划发布公开物理基准与 CAE/EDA 智能体评测；Large 4 约一万…  
  原始来源 Source: <https://mistral.ai/news/mistral-nvidia-ai-for-industrial-engineering> · Shift: <https://shift.kai-nex.com/event/evt-7fe0af7ef05adcc5/>
- **Meta 详解 Prometheus：俄亥俄吉瓦级超算，目标约百万 GPU**  
  Meta 工程博客介绍位于俄亥俄州 New Albany 的吉瓦级超算集群 Prometheus：一期已完成并用于训练 Muse 系列基础模型（含 Muse Wonder），现正继续扩容，目标规模约 100 万 GPU，并采用闭式液冷等效率…  
  原始来源 Source: <https://engineering.fb.com/2026/10/19/data-center-engineering/inside-prometheus-meta-gigawatt-scale-supercluster/> · Shift: <https://shift.kai-nex.com/event/evt-1317a947cf89ccb5/>
- **Inception 发布 Mercury 3：称对标 Luna/Haiku，约 1068 tok/s**  
  Inception Labs 发布扩散式大模型 Mercury 3，官方称在多项基准上优于或持平 GPT-6 Luna 与 Claude Haiku 5.5，NVIDIA GPU 上输出约 1068 token/秒（相对上述速度优化模型约快…  
  原始来源 Source: <https://www.inceptionlabs.ai/blog/introducing-mercury-3> · Shift: <https://shift.kai-nex.com/event/evt-bbee36b90875094a/>

[查看本周全部 23 条 See all →](weekly/2026-W43.md)
<!-- THIS_WEEK:END -->

<!-- ARCHIVE:START -->
## 归档 Archive
- [2026-W43](weekly/2026-W43.md) · 23 条
- [2026-W42](weekly/2026-W42.md) · 32 条
- [2026-W41](weekly/2026-W41.md) · 39 条
- [2026-W40](weekly/2026-W40.md) · 54 条
- [2026-W39](weekly/2026-W39.md) · 6 条
- [2026-W38](weekly/2026-W38.md) · 2 条
- [2026-W17](weekly/2026-W17.md) · 1 条
<!-- ARCHIVE:END -->

## 使用与自建 Use it / Build your own

- 读取数据源、字段说明、用任意 jsonfeed.org 源生成自己的周报：[docs/REUSE.md](docs/REUSE.md)
- Read the feed field reference, or build your own weekly digest from the Shift feed or any jsonfeed.org (v1.x) feed: [docs/REUSE.md](docs/REUSE.md)

```bash
python3 scripts/build_weekly.py --all --update-readme   # 或 or: --latest --update-readme
```
模板 Template: [weekly/TEMPLATE.md](weekly/TEMPLATE.md)

## 贡献 Contributing
> 🙌 **欢迎参与 Contributions welcome!** [推荐新闻 Submit a news item](https://github.com/orocoa/shift/issues/new?template=submit-news.yml) · [good first issues](https://github.com/orocoa/shift/labels/good%20first%20issue) · [讨论区 Discussions](https://github.com/orocoa/shift/discussions)

详见 See [CONTRIBUTING.md](CONTRIBUTING.md) for the contribution guidelines.

## 许可 License
- 内容 Content: [CC BY 4.0](LICENSE)
- 代码 Code (`scripts/`): [MIT](LICENSE-CODE)

<sub>关键词 Keywords: AI news, LLM, 大模型, 每周 AI 新闻, AI 周报, awesome list, newsletter, model releases, source-first, feed.json</sub>
