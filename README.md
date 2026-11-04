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

- **OpenAI：GPT-6 Astra 不到一周从零设计出一台硬件设备，未公开内部模型 CAD 基准成绩大幅领先**  
  OpenAI 11 月 3 日发文介绍 ChatGPT 和 Codex 在 CAD、PCB 设计和仿真等实体工程中的使用。据 The Decoder 转述，OpenAI 硬件团队用 GPT-6 Astra 在不到一周内设计出一台可与 Cod…  
  原始来源 Source: <https://the-decoder.com/openai-says-gpt-6-astra-designed-a-hardware-device-from-scratch-in-under-a-week/> · Shift: <https://shift.kai-nex.com/event/evt-da5ea8e479c06775/>
- **Anthropic 推出 Message Threads 公测：长对话 Agent 每轮只发增量，首 token 延迟降约 35%**  
  Anthropic 在 Claude Platform 上线 Message Threads 公测。过去 Messages API 每次请求都要重发完整对话历史；开启线程后，Agent 只需发送上一轮之后的新消息。Anthropic 称，多…  
  原始来源 Source: <https://claude.com/resources/articles/message-threads> · Shift: <https://shift.kai-nex.com/event/evt-697a999f1ade6db2/>
- **Revolut 把自托管 GLM 设为默认 AI 编程模型，称推理成本降约九成，替代 Claude Code 等商用工具**  
  据 The Register 11 月 3 日报道，英国金融科技公司 Revolut 运维与基础设施负责人 David Abitbol 在上月纽约 AI Engineer 大会上表示，公司在不到一年内把自托管的智谱 GLM 模型设为 AI…  
  原始来源 Source: <https://www.theregister.com/ai-and-ml/2026/11/03/british-fintech-revolut-slashes-ai-coding-costs-10x-by-cutting-out-claude-and-going-self-hosted/5307345> · Shift: <https://shift.kai-nex.com/event/evt-149329eb526a0dac/>
- **Anthropic 提交招股书修订稿：前三季度营收 332 亿美元，并称未来模型可能“很快”触及 AI 加速研发门槛**  
  Anthropic 于 11 月 2 日向美国 SEC 提交 S-1 第一号修订稿，补入截至 9 月 30 日的财务：前九个月营收 332.4 亿美元，第三季度营收 169.6 亿美元、净亏损 232.9 亿美元，亏损主要来自可转债等金融工…  
  原始来源 Source: <https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm> · Shift: <https://shift.kai-nex.com/event/evt-c6d2cbc0bf820046/>
- **OpenAI 公布自研 Git 后端 Pando：为应对 Codex 带来的并行开发量，推送延迟降近 5 倍**  
  OpenAI 11 月 2 日发布工程博客，介绍为内部单一代码仓库重建的 Git 兼容后端 Pando。按 CellCog 对原文的转述，Codex 让工程师可以同时推进多项改动，旧系统一度可靠性低于 90%；Pando 上线后推送中位延迟…  
  原始来源 Source: <https://cellcog.ai/blog/openai-pando-git/> · Shift: <https://shift.kai-nex.com/event/evt-d8e688b97199f71f/>
- **OpenAI 提高漏洞赏金：例外级发现含奖金最高 17.2 万美元，并与 Cathedral 开展下一轮 AI 攻防冲刺**  
  OpenAI 11 月 2 日宣布，将严重级漏洞的赏金区间提高四倍以上，核心产品的严重漏洞最高 3 万美元，例外级发现加上奖金最高可达 17.2 万美元。同日 OpenAI 还宣布，安全公司 Cathedral 的研究人员将加入其下一轮内部…  
  原始来源 Source: <https://alphasignal.ai/news/openai-raises-bug-bounty-to-172-000-to-hunt-its-own-flaws> · Shift: <https://shift.kai-nex.com/event/evt-cf1707b3c10b33ca/>
- **高盛收回交易员与银行家的 AI 编程工具，Claude Code、Copilot 改为仅限工程师使用**  
  据 The Decoder 11 月 2 日引述 Bloomberg 报道，高盛依据 10 月的内部规定，停止大多数员工使用 Anthropic 的 Claude Code、GitHub Copilot 等高级 AI 编程工具，只有工程师仍…  
  原始来源 Source: <https://the-decoder.com/goldman-sachs-pulls-ai-coding-tools-from-traders-and-bankers/> · Shift: <https://shift.kai-nex.com/event/evt-5d1b9e55879b5bf7/>
<!-- THIS_WEEK:END -->

<!-- ARCHIVE:START -->
## 归档 Archive
- [2026-W45](weekly/2026-W45.md) · 7 条
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
