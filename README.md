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

- **OpenAI、Google、微软、Anthropic 支持 robots.txt 统一 AI 训练退出信号**  
  2026 年 10 月 30 日，四家 AI 公司宣布支持一个跨厂商的 robots.txt 训练偏好信号：网站写一组 User-Agent: __usage_ai-training 规则，就能一次性向参与厂商表达是否允许用于 AI 训练，…  
  原始来源 Source: <https://developers.google.com/search/blog/2026/10/ai-training-control> · Shift: <https://shift.kai-nex.com/event/evt-9c6158c4f66136b5/>
- **Claude Max 20x 更名 Ultra，已验证账户取消五小时会话限制**  
  Anthropic 于 2026 年 10 月 30 日调整 Claude 订阅档名称：100 美元/月的 Max 5x 改叫 Max，200 美元/月的 Max 20x 改叫 Ultra，价格不变、现有订阅自动迁移。Ultra 的已验证账…  
  原始来源 Source: <https://support.claude.com/en/articles/17728952-what-is-the-ultra-plan> · Shift: <https://shift.kai-nex.com/event/evt-7d8e705399da9201/>
- **Google Suncatcher 卫星传回首个在轨 AI 回答：星载 Gemma 4 写了一首俳句**  
  Google 于 2026 年 10 月 30 日宣布，Project Suncatcher 原型卫星完成调试，实现了数据中心级 TPU 在轨的首次 AI 回答：星载 Gemma 4 开放模型按地面指令写出一首关于太空的俳句。下一步将测试…  
  原始来源 Source: <https://blog.google/innovation-and-ai/models-and-research/google-research/project-suncatcher-satellite-response/> · Shift: <https://shift.kai-nex.com/event/evt-651cbaad0ced455d/>
- **Mistral 开源改进版 Large 4「Le Chonk」权重：编程开源侧领先、整体仍落后部分中国模型**  
  Mistral 在预览反馈与继续强化学习后，开源改进版旗舰模型 Mistral Large 4（绰号 Le Chonk）权重。官方称其为约 1 万亿参数的原生多模态模型，在 FrontierCode 2.0 与 Terminal-Bench…  
  原始来源 Source: <https://mistral.ai/news/mistral-large-4-oss> · Shift: <https://shift.kai-nex.com/event/evt-7642773f0e59e845/>
- **OpenAI 扩展前沿模型错位监测：从 HF 事故缺口到分层探针**  
  OpenAI 于 2026 年 10 月 29 日说明如何检测前沿模型错位行为：称 Hugging Face 相关事故暴露其在部分网络安全评测中未运行错位监测的缺口，随后大幅扩展训练、评测、内部使用与外部部署监测。官方称加强后的系统在事故回…  
  原始来源 Source: <https://openai.com/index/how-we-detect-frontier-model-misalignment> · Shift: <https://shift.kai-nex.com/event/evt-8f14f667833c2397/>
- **OpenAI 更新 Model Spec：以五价值观重组行为指引**  
  OpenAI 于 2026 年 10 月 29 日更新公开 Model Spec，围绕忠实人类意图、伤害最小化、诚实与透明、人类能动性与关怀五价值观重组指引，并补充情境、监督与能动性相关默认；同时退役大部分细粒度文风规定。官方称 Spec…  
  原始来源 Source: <https://openai.com/index/updated-model-spec> · Shift: <https://shift.kai-nex.com/event/evt-5e8307f3942f37f4/>
- **OpenAI 将多档 Pro 的 Work 与 Codex 用量上限翻倍**  
  据 The Decoder 2026 年 10 月 29 日报道，OpenAI 上调多档付费 Pro 计划的用量上限：Pro 100 与 Pro 500 的 Work 与 Codex 配额均翻倍；Pro 200 的较低档配额翻倍，并在用户反…  
  原始来源 Source: <https://the-decoder.com/openai-doubles-usage-limits-on-pro-plans-as-competition-with-anthropic-heats-up/> · Shift: <https://shift.kai-nex.com/event/evt-af2ff92ac12c1679/>
- **Epoch AI：开源模型 GLM 5.3 利用补丁空窗，自主攻破 6 个 Firefox 版本**  
  Epoch AI 于 2026 年 10 月 29 日发布报告：智谱 Z.ai 8 月发布的开源权重模型 GLM 5.3，在无人指导下利用“已公开修复、但尚未推送给用户”的补丁空窗，攻破 9 月 17 日至 10 月 26 日间发布的全部…  
  原始来源 Source: <https://epoch.ai/publications/open-weight-models-patch-gap> · Shift: <https://shift.kai-nex.com/event/evt-8bf96691f581897b/>
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

[查看本周全部 20 条 See all →](weekly/2026-W44.md)
<!-- THIS_WEEK:END -->

<!-- ARCHIVE:START -->
## 归档 Archive
- [2026-W44](weekly/2026-W44.md) · 20 条
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
