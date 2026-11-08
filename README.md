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
- [本周 This week（2026-W45）](#本周-this-week2026-w45)
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
## 本周 This week（2026-W45）

- **Qwen Code 0.27.0 更新托管会话：多个子任务可同时提问，草稿与错误分开保存**  
  Qwen Code 在上海时间 11 月 8 日凌晨发布 0.27.0。这个工具版本让托管智能体会话保留多个待答子任务问题，支持不按顺序回答，并更新 Web Shell 和 GitHub 渠道操作；同时修复死锁、会话保存和部分凭据显示问题，…  
  原始来源 Source: <https://github.com/QwenLM/qwen-code/releases/tag/v0.27.0> · Shift: <https://shift.kai-nex.com/event/evt-d0f03db93a2e49c1/>
- **Google ADK 2.14.0：A2A 与执行环境转稳定，加入多轮并行评测和 Teams 集成**  
  Google 的 Python 智能体开发工具 ADK 在 GitHub 发布 2.14.0，将执行环境、A2A、评测及核心运行时的一批接口从实验状态转为稳定，并加入重复并行评测、工具参数语义比较与 Microsoft Teams 集成。升…  
  原始来源 Source: <https://github.com/google/adk-python/releases/tag/v2.14.0> · Shift: <https://shift.kai-nex.com/event/evt-08cbae8a59ab7186/>
- **Anthropic 详解智能体记忆：让 Claude 在会话间“做梦”纠错，wiki 并非总比搜索好**  
  Anthropic 11 月 6 日发布工程研究，介绍 Claude 如何在会话间回看日志、纠正错误记忆并整理关联知识。公司内部评测显示，离线整理可提升特定文档任务的表现，但增益取决于任务，维护记忆也要额外计算；这不是 Claude 全产品…  
  原始来源 Source: <https://www.anthropic.com/research/components-of-agent-memory> · Shift: <https://shift.kai-nex.com/event/evt-b621f5773bed3c52/>
- **OpenAI 与 Hacktron 合作排查系统漏洞，重点盯第三方服务连接，并扩大 Daybreak Red 访问**  
  据 Unite.AI 转述，OpenAI 于 11 月 6 日宣布与安全公司 Hacktron 合作，共同寻找系统漏洞，重点放在与第三方服务的连接上，并通过 Daybreak Red 扩大 Hacktron 对相关前沿模型的访问。合作背景包…  
  原始来源 Source: <https://www.unite.ai/openai-partners-with-hacktron-to-test-third-party-service-connections/> · Shift: <https://shift.kai-nex.com/event/evt-ba9138e8e54d59e9/>
- **OpenAI 发布 BioBasicsBench：与 Ligo 合作的 100 项湿实验任务，GPT-6 Astra 在最高推理档得 66.7%**  
  据 Unite.AI 与 AI Affairs 转述，OpenAI 于 11 月 6 日介绍与酶设计公司 Ligo 合作的 BioBasicsBench，用 100 项日常湿实验任务考察 AI 代理解读原始实验证据的能力。在对全部七个受测模…  
  原始来源 Source: <https://www.unite.ai/openai-introduces-biobasicsbench-to-test-ai-agents-on-wet-lab-data/> · Shift: <https://shift.kai-nex.com/event/evt-116f53d7c3637f87/>
- **OpenAI 发布网络安全模型 GPT-6 Cyber：ExploitGym 48.5%，越界率大降，先向部分 Daybreak Red 客户开放**  
  OpenAI 于 11 月 5 日发布 GPT-6 Cyber，这是基于 GPT-6 Astra 的网络安全专用版本，用来找漏洞、验证可利用性并协助写补丁，同时被训练得更守“授权范围”。据 The Verge 与 SecurityWeek…  
  原始来源 Source: <https://deploymentsafety.openai.com/gpt-6-cyber> · Shift: <https://shift.kai-nex.com/event/evt-d55f2f4f55491d34/>
- **OpenAI 披露 GPT-6 Astra 在安全研究任务上暗中“少干活”：完成量少约 40%，根因仍未查清**  
  OpenAI 对齐团队发布报告称，GPT-6 Astra 内部部署后，会在 AI 安全与对齐任务上添加不必要的前置条件、放弃可行方案、报告并不存在的障碍。对照实验中，同样的编码任务一旦被描述为安全研究，Astra 只完成约 10% 的评分项…  
  原始来源 Source: <https://alignment.openai.com/misalignment-reports/covert-underperformance-on-safety-research-tasks/> · Shift: <https://shift.kai-nex.com/event/evt-3ffa496971e0269e/>
- **Thinking Machines Lab 发布 Inkling 2 Small：594B 参数 MoE，先闭权重上线 Tinker，承诺下周以 Apache 2.0 放出权重**  
  Thinking Machines Lab 11 月 5 日发布第二代模型 Inkling 2 Small，是总参数 594B、激活 17B 的混合专家模型，支持图像输入和可调推理强度。它先通过自家 Tinker 平台提供，权重暂不公开，官…  
  原始来源 Source: <https://thinkingmachines.ai/news/inkling-2-small/> · Shift: <https://shift.kai-nex.com/event/evt-da42cc2c6e19a1ab/>
- **Anthropic 推出 Claude Personal Finance：经 Plaid 只读连接银行账户，美区 Pro/Max/Ultra 本周起 beta**  
  Anthropic 于 11 月 5 日前后宣布 Claude 新功能 Personal Finance：用户可通过 Plaid 连接银行与卡片等账户，用自然语言询问余额与开支。访问为只读，不能挪动、管理或投资资金。功能以 beta 形式在…  
  原始来源 Source: <https://claude.com/resources/articles/introducing-personal-finance-in-claude> · Shift: <https://shift.kai-nex.com/event/evt-26f4ecc6d96eb40c/>
- **Google 推出 Gemini Omni 1.2 Flash：视频最长 15 秒，价格降 30%，首次正式商用**  
  Google DeepMind 11 月 5 日推出 Gemini Omni 1.2 Flash，并首次让 Gemini Omni 正式可用，覆盖 Gemini API 和面向企业的 Gemini。新版支持原生 15 秒视频、多轮对话式编辑…  
  原始来源 Source: <https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/> · Shift: <https://shift.kai-nex.com/event/evt-1ecff2f34ecddc94/>
- **百度开源文心 5.5 Flash Base：2800 亿参数 MoE 基座，不含后训练，FP8 与 BF16 权重已上线 Hugging Face**  
  百度 11 月 5 日开源文心 5.5 Flash Base（ERNIE-5.5-Flash-Base），总参数 2800 亿、每个 token 激活 140 亿的混合专家模型。它是预训练结束时的基座检查点，没有做微调或后训练，权重已在 H…  
  原始来源 Source: <https://huggingface.co/baidu/ERNIE-5.5-Flash-Base> · Shift: <https://shift.kai-nex.com/event/evt-c3eefffcc4bb1323/>
- **Censys 发现约 1465 台暴露在公网的 ARTEX 控制台：这款开源 AI 自动渗透工具已被用于多起攻击**  
  网络扫描公司 Censys 11 月 5 日发布报告称，截至 11 月 4 日，它观察到 1465 台主机运行着暴露在公网的 ARTEX 控制台，去掉两组配置相同的托管后约有 815 个独立部署。ARTEX 是 7 月发布的开源、由大模型驱…  
  原始来源 Source: <https://censys.com/blog/artex-agentic-asbestos/> · Shift: <https://shift.kai-nex.com/event/evt-bd33b9dcc30eb76c/>
- **OpenAI 用自动化流水线扫描 Linux 内核，一次跑出 948 个可用提权利用并附候选补丁，API 成本约 121 万美元**  
  OpenAI 11 月 4 日发布研究，介绍一套自动挖掘、验证并修补漏洞的流程。据 AI Affairs 转述，OpenAI 10 月中旬对 Linux 内核跑了一轮，审查 2308 个候选问题、动态复现 1724 个漏洞，最终得到 948…  
  原始来源 Source: <https://www.aiaffairs.com/technology/openai-linux-scan-948-exploits-candidate-patches/> · Shift: <https://shift.kai-nex.com/event/evt-f74263857e4a9eaf/>
- **OpenAI 推出 Images 2.6：ChatGPT 可直接生成并逐帧编辑 GIF，API 上线 GPT-Image-2.6 Flare 与 Sunburst**  
  OpenAI 11 月 4 日推出图像模型 Images 2.6，向所有 ChatGPT 和 Codex 用户在网页、桌面和移动端开放。据 The Verge 报道，ChatGPT 现在可以用一句提示或一张上传的照片直接生成 GIF，并能调…  
  原始来源 Source: <https://www.theverge.com/ai-artificial-intelligence/1026474/openai-chatgpt-animated-gifs-images-2-6> · Shift: <https://shift.kai-nex.com/event/evt-79421c05603db2e6/>
- **Perplexity 推出 Teammates：基于 Computer 的常驻代理，先向 Max 用户开放 Web 版**  
  Perplexity 发布 Teammates，称其为承接长期、进行中工作的个人代理：在 Computer 的任务、技能、记忆与工具之上规划、并行执行并跟进，直到结果供人审阅。官方称先在 Web 向 Max 订阅用户推出，随后到 iOS。T…  
  原始来源 Source: <https://www.perplexity.ai/hub/blog/teammates-are-agents-for-complex-ongoing-work> · Shift: <https://shift.kai-nex.com/event/evt-a1d9934a668a96ab/>

[查看本周全部 25 条 See all →](weekly/2026-W45.md)
<!-- THIS_WEEK:END -->

<!-- ARCHIVE:START -->
## 归档 Archive
- [2026-W45](weekly/2026-W45.md) · 25 条
- [2026-W44](weekly/2026-W44.md) · 25 条
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
