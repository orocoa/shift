<div align="center">

# ？｜Shift · Awesome 每周 AI 新闻精选 · Weekly AI News & LLM Index

**每周 AI 新闻 / 大模型（LLM）动态精选：一句话摘要 + 官方原始来源，不搬运全文。**  
**A curated, source-first weekly index of AI news and LLM releases — one-line summaries with original sources.**

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Website](https://img.shields.io/badge/site-kai--nex.com%2Fshift-blue)](https://kai-nex.com/shift/)
[![Feed](https://img.shields.io/badge/feed-JSON-orange)](https://kai-nex.com/shift/feed.json)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/orocoa/shift?style=social)](https://github.com/orocoa/shift/stargazers)

### 🌐 [打开 Shift 网站 Open Shift →](https://kai-nex.com/shift/) · 📡 [订阅源 feed.json](https://kai-nex.com/shift/feed.json)

</div>

## 目录 Contents
- [如何关注 How to follow](#如何关注-how-to-follow)
- [本周 This week（2026-W43）](#本周-this-week2026-w43)
- [归档 Archive](#归档-archive)
- [使用与自建 Use it / Build your own](#使用与自建-use-it--build-your-own)
- [贡献 Contributing](#贡献-contributing)
- [许可 License](#许可-license)

## 如何关注 How to follow
- ⭐ **Star** 本仓库，⭐ Star this repo to bookmark it.
- 👀 **Watch → Custom → Releases / All activity**，每周更新提醒 for weekly update notifications.
- 📡 数据源（Shift 自有 JSON 格式，适合程序读取）Data feed (Shift's own JSON, for scripts): `https://kai-nex.com/shift/feed.json`，见 see [docs/REUSE.md](docs/REUSE.md)
- 🌐 每日浏览 Browse daily: https://kai-nex.com/shift/

<!-- THIS_WEEK:START -->
## 本周 This week（2026-W43）

- **Meta 详解 Prometheus：俄亥俄吉瓦级超算，目标约百万 GPU**  
  Meta 工程博客介绍位于俄亥俄州 New Albany 的吉瓦级超算集群 Prometheus：一期已完成并用于训练 Muse 系列基础模型（含 Muse Wonder），现正继续扩容，目标规模约 100 万 GPU，并采用闭式液冷等效率…  
  原始来源 Source: <https://engineering.fb.com/2026/10/19/data-center-engineering/inside-prometheus-meta-gigawatt-scale-supercluster/> · Shift: <https://kai-nex.com/shift/#/event/evt-1317a947cf89ccb5>
- **Inception 发布 Mercury 3：称对标 Luna/Haiku，约 1068 tok/s**  
  Inception Labs 发布扩散式大模型 Mercury 3，官方称在多项基准上优于或持平 GPT-6 Luna 与 Claude Haiku 5.5，NVIDIA GPU 上输出约 1068 token/秒（相对上述速度优化模型约快…  
  原始来源 Source: <https://www.inceptionlabs.ai/blog/introducing-mercury-3> · Shift: <https://kai-nex.com/shift/#/event/evt-bbee36b90875094a>
- **Cloudflare 预览抽取模型 Clairic：Workers AI 上线，输入价 $0.10/百万 token**  
  Cloudflare 宣布在 Workers AI 以预览形式托管 System One 抽取模型 Clairic（@cf/cloudflare/clairic），可从非结构化输入一次前向返回类型化抽取、计算、估计与预测值，Changelo…  
  原始来源 Source: <https://blog.cloudflare.com/clairic-extraction-model/> · Shift: <https://kai-nex.com/shift/#/event/evt-8a224c2d8b379d21>
- **MiniMax 发布 M3.1 Flash：Agent 向降价，输入 $0.15/百万 token**  
  MiniMax 正式推出 MiniMax M3.1 Flash，称其为曾匿名处理逾 200 万亿 token 的 Space Bunny 的后续版本，在 Agent、编码与 Computer Use 等基准上接近领先模型，在线推理近三倍加速…  
  原始来源 Source: <https://www.minimax.io/blog/minimax-m31f> · Shift: <https://kai-nex.com/shift/#/event/evt-bf46fbebf5b2b673>
- **DeepSeek 开源生产推理框架 DeepInfer：首发支持 V4.1-Flash，可跑 NVIDIA SM100 与昇腾 950**  
  DeepSeek 在 GitHub 以 Apache-2.0 许可开源 DeepInfer，称其为支撑自家大规模生产服务的推理框架；本次版本提供离线推理，首发支持 DeepSeek-V4.1-Flash，硬件覆盖 NVIDIA SM100…  
  原始来源 Source: <https://github.com/deepseek-ai/DeepInfer> · Shift: <https://kai-nex.com/shift/#/event/evt-8bfb9e856bb621b7>
- **美国国土安全部下令联邦民事机构排除并移除 DeepSeek 产品，涵盖基于其实现的第三方服务**  
  美国国土安全部依 2018 年《联邦采购供应链安全法》（FASCSA）发布命令：联邦民事机构采购中排除 DeepSeek 及其关联实体的 IT 产品与服务，并从机构系统中移除 DeepSeek 产品以及基于 DeepSeek 实现开发的第三…  
  原始来源 Source: <https://public-inspection.federalregister.gov/2026-21447.pdf> · Shift: <https://kai-nex.com/shift/#/event/evt-7c4427f03ee376c9>
- **Mistral 发布 Voxtral 3 语音智能体栈：50+ 语言转写、情绪化 TTS 与实时 SDK，可自部署**  
  Mistral 推出 Voxtral 3 系列：转写模型 Voxtral Small/Mini Transcribe 3 覆盖 50 余种语言，Mini 版 4B 参数、每分钟 0.0035 美元；实时转写延迟低于 500 毫秒；Voxtr…  
  原始来源 Source: <https://mistral.ai/news/voxtral-3/> · Shift: <https://kai-nex.com/shift/#/event/evt-abad49b4a1952898>
<!-- THIS_WEEK:END -->

<!-- ARCHIVE:START -->
## 归档 Archive
- [2026-W43](weekly/2026-W43.md) · 7 条
- [2026-W42](weekly/2026-W42.md) · 32 条
- [2026-W41](weekly/2026-W41.md) · 39 条
- [2026-W40](weekly/2026-W40.md) · 54 条
- [2026-W39](weekly/2026-W39.md) · 6 条
- [2026-W38](weekly/2026-W38.md) · 2 条
- [2026-W17](weekly/2026-W17.md) · 1 条
<!-- ARCHIVE:END -->

## 使用与自建 Use it / Build your own

- 读取数据源、字段说明、用任意 jsonfeed.org 源生成自己的周报：[docs/REUSE.md](docs/REUSE.md)
- Read the feed, see the fields, or build your own weekly from any jsonfeed.org feed: [docs/REUSE.md](docs/REUSE.md)

```bash
python3 scripts/build_weekly.py --all --update-readme   # 或 or: --latest --update-readme
```
模板 Template: [weekly/TEMPLATE.md](weekly/TEMPLATE.md)

## 贡献 Contributing
> 🙌 **欢迎参与 Contributions welcome!** [推荐新闻 Submit a news item](https://github.com/orocoa/shift/issues/new?template=submit-news.yml) · [good first issues](https://github.com/orocoa/shift/labels/good%20first%20issue) · [讨论区 Discussions](https://github.com/orocoa/shift/discussions)

详见 See [CONTRIBUTING.md](CONTRIBUTING.md).

## 许可 License
- 内容 Content: [CC BY 4.0](LICENSE)
- 代码 Code (`scripts/`): [MIT](LICENSE-CODE)

<sub>关键词 Keywords: AI news, LLM, 大模型, 每周 AI 新闻, AI 周报, awesome list, newsletter, model releases</sub>
