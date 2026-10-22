<div align="center">

# ？｜Shift · Awesome 每周 AI 新闻精选 · Weekly AI News & LLM Index

**每周 AI 新闻 / 大模型（LLM）动态精选：一句话摘要 + 官方原始来源，不搬运全文。**  
**A curated, source-first weekly index of AI news and LLM releases — one-line summaries with original sources.**

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Website](https://img.shields.io/badge/site-shift.kai--nex.com-blue)](https://shift.kai-nex.com/)
[![Feed](https://img.shields.io/badge/feed-JSON-orange)](https://shift.kai-nex.com/feed.json)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/orocoa/shift?style=social)](https://github.com/orocoa/shift/stargazers)

### 🌐 [打开 Shift 网站 Open Shift →](https://shift.kai-nex.com/) · 📡 [订阅源 feed.json](https://shift.kai-nex.com/feed.json)

</div>

## 目录 Contents
- [如何关注 How to follow](#如何关注-how-to-follow)
- [本周 This week（2026-W43）](#本周-this-week2026-w43)
- [归档 Archive](#归档-archive)
- [使用与自建 Use it / Build your own](#使用与自建-use-it--build-your-own)
- [贡献 Contributing](#贡献-contributing)
- [许可 License](#许可-license)

## 如何关注 How to follow
- ⭐ **Star** 本仓库，⭐ Star this repository to bookmark Shift and easily come back to it.
- 👀 **Watch → Custom → Releases / All activity**，每周更新提醒 Set Watch to Custom and choose Releases or All activity to receive weekly update notifications.
- 📡 数据源（Shift 自有 JSON 格式，适合程序读取）Data feed in Shift's own JSON format (not RSS), suitable for scripts: `https://shift.kai-nex.com/feed.json`，见 see [docs/REUSE.md](docs/REUSE.md) for format details and reuse instructions.
- 🌐 每日浏览 Browse daily on the [Shift website](https://shift.kai-nex.com/).

<!-- THIS_WEEK:START -->
## 本周 This week（2026-W43）

- **Anthropic 发布 Claude Duet：主动式智能体研究预览面向美国 Pro/Max**  
  Anthropic 开放 Claude Duet 研究预览：独立 iOS/Android 应用与 claude.ai，基于 Claude Opus 5.5，提供晨间简报与后台任务，并在发送、付款、签署或删除前征求确认；预览期计入 Pro/M…  
  原始来源 Source: <https://claude.com/resources/articles/claude-duet> · Shift: <https://shift.kai-nex.com/event/evt-77d31ab543ad7fd2/>
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
- **ElevenLabs 发布 Eleven Realtime：面向实时对话的两款语音到语音模型**  
  ElevenLabs 推出完整语音智能体模型 Eleven Realtime v1 Mini 与 v1 Max，支持 90+ 语言与库内 17000+ 音色；官方援引 Artificial Analysis：Max 在 Big Bench…  
  原始来源 Source: <https://elevenlabs.io/blog/realtime> · Shift: <https://shift.kai-nex.com/event/evt-d0474c7083be9ee9/>
- **Cloudflare 预览抽取模型 Clairic：Workers AI 上线，输入价 $0.10/百万 token**  
  Cloudflare 宣布在 Workers AI 以预览形式托管 System One 抽取模型 Clairic（@cf/cloudflare/clairic），可从非结构化输入一次前向返回类型化抽取、计算、估计与预测值，Changelo…  
  原始来源 Source: <https://blog.cloudflare.com/clairic-extraction-model/> · Shift: <https://shift.kai-nex.com/event/evt-8a224c2d8b379d21/>
- **OpenAI 收购 Orchestra Bio：药物研发编排平台并入 Rosalind**  
  OpenAI 宣布收购药物研发协作平台 Orchestra Bio，将团队与技术并入面向生命科学的 Rosalind（含 GPT-Rosalind 与 Rosalind Workbench），目标用智能体协助研究到推进治疗的编排。  
  原始来源 Source: <https://openai.com/index/openai-to-acquire-orchestra-bio> · Shift: <https://shift.kai-nex.com/event/evt-6dec96fb6f683447/>
- **MiniMax 发布 M3.1 Flash：Agent 向降价，输入 $0.15/百万 token**  
  MiniMax 正式推出 MiniMax M3.1 Flash，称其为曾匿名处理逾 200 万亿 token 的 Space Bunny 的后续版本，在 Agent、编码与 Computer Use 等基准上接近领先模型，在线推理近三倍加速…  
  原始来源 Source: <https://www.minimax.io/blog/minimax-m31f> · Shift: <https://shift.kai-nex.com/event/evt-bf46fbebf5b2b673/>
- **DeepSeek 开源生产推理框架 DeepInfer：首发支持 V4.1-Flash，可跑 NVIDIA SM100 与昇腾 950**  
  DeepSeek 在 GitHub 以 Apache-2.0 许可开源 DeepInfer，称其为支撑自家大规模生产服务的推理框架；本次版本提供离线推理，首发支持 DeepSeek-V4.1-Flash，硬件覆盖 NVIDIA SM100…  
  原始来源 Source: <https://github.com/deepseek-ai/DeepInfer> · Shift: <https://shift.kai-nex.com/event/evt-8bfb9e856bb621b7/>
- **OpenAI 客户案例：Terminal X 称 GPT-6.1 Sol 评测与资深投资人判断一致率 88.6%**  
  OpenAI 介绍投行操作系统 Terminal X：用 GPT-6.1 Sol 与 GPT-6 Luna 编码各基金“Capital Memory”，其 Eval Agent 在 500 次打分中与资深人工审阅一致率 88.6%，并称对…  
  原始来源 Source: <https://openai.com/index/terminal-x> · Shift: <https://shift.kai-nex.com/event/evt-34003a6a4a87deea/>
- **美国国土安全部下令联邦民事机构排除并移除 DeepSeek 产品，涵盖基于其实现的第三方服务**  
  美国国土安全部依 2018 年《联邦采购供应链安全法》（FASCSA）发布命令：联邦民事机构采购中排除 DeepSeek 及其关联实体的 IT 产品与服务，并从机构系统中移除 DeepSeek 产品以及基于 DeepSeek 实现开发的第三…  
  原始来源 Source: <https://public-inspection.federalregister.gov/2026-21447.pdf> · Shift: <https://shift.kai-nex.com/event/evt-7c4427f03ee376c9/>
- **Mistral 发布 Voxtral 3 语音智能体栈：50+ 语言转写、情绪化 TTS 与实时 SDK，可自部署**  
  Mistral 推出 Voxtral 3 系列：转写模型 Voxtral Small/Mini Transcribe 3 覆盖 50 余种语言，Mini 版 4B 参数、每分钟 0.0035 美元；实时转写延迟低于 500 毫秒；Voxtr…  
  原始来源 Source: <https://mistral.ai/news/voxtral-3/> · Shift: <https://shift.kai-nex.com/event/evt-abad49b4a1952898/>
<!-- THIS_WEEK:END -->

<!-- ARCHIVE:START -->
## 归档 Archive
- [2026-W43](weekly/2026-W43.md) · 15 条
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

<sub>关键词 Keywords: AI news, LLM, 大模型, 每周 AI 新闻, AI 周报, awesome list, newsletter, model releases</sub>
