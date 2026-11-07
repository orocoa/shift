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

- **OpenAI 与 Hacktron 合作排查系统漏洞，重点盯第三方服务连接，并扩大 Daybreak Red 访问**  
  据 Unite.AI 转述，OpenAI 于 11 月 6 日宣布与安全公司 Hacktron 合作，共同寻找系统漏洞，重点放在与第三方服务的连接上，并通过 Daybreak Red 扩大 Hacktron 对相关前沿模型的访问。合作背景包…  
  原始来源 Source: <https://www.unite.ai/openai-partners-with-hacktron-to-test-third-party-service-connections/> · Shift: <https://shift.kai-nex.com/event/evt-ba9138e8e54d59e9/>
- **OpenAI 发布 BioBasicsBench：与 Ligo 合作的 100 项湿实验任务，GPT-6 Astra 在最高推理档得 66.7%**  
  据 Unite.AI 与 AI Affairs 转述，OpenAI 于 11 月 6 日介绍与酶设计公司 Ligo 合作的 BioBasicsBench，用 100 项日常湿实验任务考察 AI 代理解读原始实验证据的能力。在对全部七个受测模…  
  原始来源 Source: <https://www.unite.ai/openai-introduces-biobasicsbench-to-test-ai-agents-on-wet-lab-data/> · Shift: <https://shift.kai-nex.com/event/evt-116f53d7c3637f87/>
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
- **OpenAI 用自动化流水线扫描 Linux 内核，一次跑出 948 个可用提权利用并附候选补丁，API 成本约 121 万美元**  
  OpenAI 11 月 4 日发布研究，介绍一套自动挖掘、验证并修补漏洞的流程。据 AI Affairs 转述，OpenAI 10 月中旬对 Linux 内核跑了一轮，审查 2308 个候选问题、动态复现 1724 个漏洞，最终得到 948…  
  原始来源 Source: <https://www.aiaffairs.com/technology/openai-linux-scan-948-exploits-candidate-patches/> · Shift: <https://shift.kai-nex.com/event/evt-f74263857e4a9eaf/>
- **OpenAI 推出 Images 2.6：ChatGPT 可直接生成并逐帧编辑 GIF，API 上线 GPT-Image-2.6 Flare 与 Sunburst**  
  OpenAI 11 月 4 日推出图像模型 Images 2.6，向所有 ChatGPT 和 Codex 用户在网页、桌面和移动端开放。据 The Verge 报道，ChatGPT 现在可以用一句提示或一张上传的照片直接生成 GIF，并能调…  
  原始来源 Source: <https://www.theverge.com/ai-artificial-intelligence/1026474/openai-chatgpt-animated-gifs-images-2-6> · Shift: <https://shift.kai-nex.com/event/evt-79421c05603db2e6/>
- **Perplexity 推出 Teammates：基于 Computer 的常驻代理，先向 Max 用户开放 Web 版**  
  Perplexity 发布 Teammates，称其为承接长期、进行中工作的个人代理：在 Computer 的任务、技能、记忆与工具之上规划、并行执行并跟进，直到结果供人审阅。官方称先在 Web 向 Max 订阅用户推出，随后到 iOS。T…  
  原始来源 Source: <https://www.perplexity.ai/hub/blog/teammates-are-agents-for-complex-ongoing-work> · Shift: <https://shift.kai-nex.com/event/evt-a1d9934a668a96ab/>
- **腾讯发布 Hy4：首次支持视觉理解和电脑操作，价格不变，权重承诺数日内放出**  
  腾讯 11 月 4 日正式发布新一代模型 Hy4，首次加入图像理解和电脑使用能力，价格与 8 月的 Hy4 Preview 相同，官方称数日内发布权重和系统卡。独立评测方面，Artificial Analysis 给出 35 分，在中国实验…  
  原始来源 Source: <https://www.tencent.com/tencent-launches-hy4-joining-the-ranks-of-the-worlds-leading-open-source-ai-models/> · Shift: <https://shift.kai-nex.com/event/evt-c70e7345188cb24b/>
- **OpenAI 宣布收购开发者工具公司 Pierre，将其代码存储服务并入 Codex**  
  OpenAI 11 月 4 日宣布将收购 Pierre Computer Company，以扩充 Codex 构建、理解和审查代码的工具，交易条款未披露。Pierre 提供面向 AI Agent 的代码存储云服务 Code Storage，…  
  原始来源 Source: <https://siliconangle.com/2026/11/04/openai-to-acquire-developer-tooling-startup-pierre-computer/> · Shift: <https://shift.kai-nex.com/event/evt-10049b983dbf08f5/>
- **Adweek：Anthropic 与美联社达成首笔内容授权协议，Claude 选举夜引用美联社实时数据**  
  据 Adweek 11 月 4 日援引两名知情人士报道，Anthropic 在美国中期选举前与美联社（AP）达成内容和数据授权协议，这是 Anthropic 首次付费授权数字新闻出版方的内容。选举夜在 Claude 上查询最新民调的用户，会…  
  原始来源 Source: <https://www.adweek.com/media/anthropic-licensing-deal-ap-election/> · Shift: <https://shift.kai-nex.com/event/evt-bb8dc1ee35572b7b/>
- **OpenAI：GPT-6 Astra 不到一周从零设计出一台硬件设备，未公开内部模型 CAD 基准成绩大幅领先**  
  OpenAI 11 月 3 日发文介绍 ChatGPT 和 Codex 在 CAD、PCB 设计和仿真等实体工程中的使用。据 The Decoder 转述，OpenAI 硬件团队用 GPT-6 Astra 在不到一周内设计出一台可与 Cod…  
  原始来源 Source: <https://the-decoder.com/openai-says-gpt-6-astra-designed-a-hardware-device-from-scratch-in-under-a-week/> · Shift: <https://shift.kai-nex.com/event/evt-da5ea8e479c06775/>
- **Anthropic 推出 Message Threads 公测：长对话 Agent 每轮只发增量，首 token 延迟降约 35%**  
  Anthropic 在 Claude Platform 上线 Message Threads 公测。过去 Messages API 每次请求都要重发完整对话历史；开启线程后，Agent 只需发送上一轮之后的新消息。Anthropic 称，多…  
  原始来源 Source: <https://claude.com/resources/articles/message-threads> · Shift: <https://shift.kai-nex.com/event/evt-697a999f1ade6db2/>
- **Revolut 把自托管 GLM 设为默认 AI 编程模型，称推理成本降约九成，替代 Claude Code 等商用工具**  
  据 The Register 11 月 3 日报道，英国金融科技公司 Revolut 运维与基础设施负责人 David Abitbol 在上月纽约 AI Engineer 大会上表示，公司在不到一年内把自托管的智谱 GLM 模型设为 AI…  
  原始来源 Source: <https://www.theregister.com/ai-and-ml/2026/11/03/british-fintech-revolut-slashes-ai-coding-costs-10x-by-cutting-out-claude-and-going-self-hosted/5307345> · Shift: <https://shift.kai-nex.com/event/evt-149329eb526a0dac/>

[查看本周全部 19 条 See all →](weekly/2026-W45.md)
<!-- THIS_WEEK:END -->

<!-- ARCHIVE:START -->
## 归档 Archive
- [2026-W45](weekly/2026-W45.md) · 19 条
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
