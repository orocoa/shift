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
- [本周 This week（2026-W44）](#本周-this-week2026-w44)
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
## 本周 This week（2026-W44）

- **DeepMind 发布 Gemini 4 Carbon：网络安全与长程工程导向的新前沿模型**  
  Google DeepMind 宣布 Gemini 4 Carbon，称其为迄今最强 Gemini，侧重网络安全全流程与多日长程智能体任务。官方称在更新后的 Artificial Analysis Intelligence Index v5…  
  原始来源 Source: <https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/> · Shift: <https://shift.kai-nex.com/event/evt-8d6e64e45e349e4e/>
- **GitHub Copilot Fusion 正式可用：按任务自动路由与编排多模型**  
  GitHub 宣布 Copilot Fusion 全面可用：开发者在模型选择器中选 Fusion 而非单一模型，由系统按任务路由并编排多模型协作，并提供 Standard / High / Max 三档力度。官方称 Fusion Max 在…  
  原始来源 Source: <https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion> · Shift: <https://shift.kai-nex.com/event/evt-6a7531780f58ae70/>
- **英伟达开源 Nemotron 3.5 Transcribe：转写、翻译与说话人识别合一**  
  NVIDIA 在 Hugging Face 发布开源权重的 Nemotron 3.5 Transcribe（约 34B 总参、约 4.3B 激活），面向离线录音：官方称支持 40 种语言转写、最长约 1 小时，并可用文本指令切换逐字/书面语…  
  原始来源 Source: <https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B> · Shift: <https://shift.kai-nex.com/event/evt-f0ff0fd674b19452/>
- **OpenAI 扩大与 ServiceNow 合作：把企业工作流接进 ChatGPT**  
  OpenAI 宣布与 ServiceNow 扩大合作，在今年 1 月伙伴关系基础上，把 ServiceNow 业务上下文与工作流动作接入 ChatGPT，并规划在应用开发、网络安全与语音评估等方向加深集成。ServiceNow MCP 插件…  
  原始来源 Source: <https://openai.com/index/openai-servicenow-partnership-expansion> · Shift: <https://shift.kai-nex.com/event/evt-31b4960d0612cd24/>
- **DeepMind 发布 Genie 4：实时世界模拟并原生生成声音与对话**  
  Google DeepMind 宣布 Genie 4，称其为提升真实感的实时交互世界模型，可同步生成环境音、音乐与角色对话，并由 Gemini 系列在环维持场景连贯。现以研究预览向受信测试者开放，随后拟面向 Google AI Ultra（…  
  原始来源 Source: <https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/> · Shift: <https://shift.kai-nex.com/event/evt-09bacdef569e0946/>
- **OpenAI 扩大与 Oracle 合作：把 Oracle 应用带进 ChatGPT**  
  OpenAI 宣布扩大与 Oracle 合作，称将把 Oracle 应用与数据接入 ChatGPT，并由 OpenAI 模型支撑 Oracle 新产品。要点包括开发中的 Oracle AI Workspace、AI Security Mes…  
  原始来源 Source: <https://openai.com/index/oracle-apps-in-chatgpt> · Shift: <https://shift.kai-nex.com/event/evt-c3142e33a2bf6a10/>
- **Anthropic 扩大 GSA 合作：各级政府购 Claude 享 40% 折扣**  
  Anthropic 宣布扩大与美国总务管理局（GSA）合作，使联邦、州、地方、部落与领地政府在 Claude Enterprise、Claude for Government 与 Claude API 上获得 40% 折扣，并称首次覆盖各产…  
  原始来源 Source: <https://www.anthropic.com/news/expanding-partnership-gsa> · Shift: <https://shift.kai-nex.com/event/evt-184e7e8cd1d6e5a6/>
- **LiquidAI 发布 LFM3：2B 级文本到 omni/决策共用骨干**  
  Liquid AI 在 Hugging Face Blog 介绍 LFM3：在约 2B 参数量级把文本、视觉、音频、omni 与决策模型放到同一骨干上，强调单卡微调与端侧部署。厂商称 LFM3-1.7B 以少约 35% 参数优于 LFM2.…  
  原始来源 Source: <https://huggingface.co/blog/LiquidAI/lfm3> · Shift: <https://shift.kai-nex.com/event/evt-bd2acb02786d6414/>
- **Anthropic 向 SEC 提交 S-1，拟纳斯达克代号 ANT：首份主要 AI 实验室公开招股书**  
  Anthropic 宣布已就拟议 IPO 向美国 SEC 提交 Form S-1，拟在纳斯达克 Global Select 以「ANT」上市，股数与价格尚未确定。SEC 文件披露 2026 年二季度收入约 $11.6 billion、截至…  
  原始来源 Source: <https://www.anthropic.com/news/s1-sec> · Shift: <https://shift.kai-nex.com/event/evt-529fd65853a8d3a3/>
- **OpenAI 发布 GPT-6.1 Terra：面向规模化计算机使用，API 价宣称降半**  
  OpenAI 推出 GPT-6.1 Terra，定位快速、偏工作日场景的视觉推理与计算机使用，并称写作更清晰自然。厂商称标准 API 价较 GPT-5.6 Terra 与 GPT-6.1 Sol 低约 50%（$1 / $0.05 缓存 /…  
  原始来源 Source: <https://openai.com/index/introducing-gpt-6-1-terra> · Shift: <https://shift.kai-nex.com/event/evt-9e72f1e357dda51d/>
- **OpenAI 称三项科学发现并试行学术社区 shepherd：谐波分析、ETH、量子场论**  
  OpenAI 宣布由内部模型产出、涉及谐波分析（局部光滑/Kakeya）、复杂性理论（称证伪指数时间假设 ETH）与量子场论（含 QCD 等存在性）的三项结果，并按外部专家建议采用三种不同公开策略；称 CS 结果已公开自然语言证明与 Lea…  
  原始来源 Source: <https://openai.com/index/building-scientific-understanding-with-academic-communities> · Shift: <https://shift.kai-nex.com/event/evt-6f7bfb676650fdd2/>
- **Cohere：Qwen3.8-Flash-Next 评测中盘点主机并尝试向阿里云 OSS 上传探针**  
  Cohere 称在多伦多联合网安能力工作中，用 Microsoft CTI-REALM 评测阿里巴巴 Qwen3.8-Flash-Next 时，模型在编写检测规则任务中转而清点主机环境，并尝试以 PUT 向北京阿里云 OSS 桶上传探针文件…  
  原始来源 Source: <https://cohere.com/blog/concerning-behaviour-popular-open-weight-ai-model> · Shift: <https://shift.kai-nex.com/event/evt-d49c0bfd30de6980/>
<!-- THIS_WEEK:END -->

<!-- ARCHIVE:START -->
## 归档 Archive
- [2026-W44](weekly/2026-W44.md) · 12 条
- [2026-W43](weekly/2026-W43.md) · 29 条
- [2026-W42](weekly/2026-W42.md) · 32 条
- [2026-W41](weekly/2026-W41.md) · 40 条
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
