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
- [本周 This week（2026-W46）](#本周-this-week2026-w46)
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
## 本周 This week（2026-W46）

- **Gemini 4 Carbon 全面开放：API 每百万 Token 2/10 美元，Google 称多项评测第一且每任务成本低一半以上**  
  Google DeepMind 于 11 月 10 日（美国时间）宣布 Gemini 4 Carbon 向开发者、企业、科学家和消费者开放。两周前它只经 Fairwind 计划提供给部分网络防御者。API 沿用与 Gemini 4 Argo…  
  原始来源 Source: <https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/> · Shift: <https://shift.kai-nex.com/event/evt-aab95d37d6d1bf91/>
- **Anthropic 给 Claude 加上表格、白板和数据看板，Adobe、Atlassian 等应用可直接嵌进 Claude**  
  Anthropic 于 11 月 10 日（美国时间）宣布，Claude 即日起可与团队一起搭建表格（Claude Sheets）、白板（Claude Whiteboards）和数据看板（Claude Data，原 Dashboards）。…  
  原始来源 Source: <https://claude.com/resources/articles/more-ways-to-work-with-claude-sheets-whiteboards-and-interactive-connectors> · Shift: <https://shift.kai-nex.com/event/evt-959d4e983278fe82/>
- **OpenAI 推出 Businesses in ChatGPT：商家可注册主页、上传商品，并用 Business Agents 在对话里接待顾客**  
  据 The Decoder 报道，OpenAI 于 11 月 10 日推出 beta 功能 Businesses in ChatGPT。商家可在 Business Hub 注册和管理自家资料、上传带价格和库存的商品数据，并查看自己在对话中被…  
  原始来源 Source: <https://the-decoder.com/openai-turns-chatgpt-into-a-business-directory-with-ai-agents-that-handle-customer-questions/> · Shift: <https://shift.kai-nex.com/event/evt-5b9d63dab965ad44/>
- **DeepMind 发布 AlphaProof Code：AI 代理四周写出超 600 万行 Lean 证明，形式化验证了 Signal 协议的实际代码**  
  Google DeepMind 于 11 月 10 日发布 AlphaProof Code，一个由多个模型协作的代理式形式化验证框架。研究人员用它证明了 Signal 协议实际运行代码的关键安全性质，Signal 协议也用于 Google…  
  原始来源 Source: <https://deepmind.google/blog/introducing-alphaproof-code/> · Shift: <https://shift.kai-nex.com/event/evt-465a67aced68a144/>
- **Anthropic 发布 Claude Fable 5.2 与 Mythos 5.2：输出最多快 30%，每百万 Token 8/40 美元**  
  Anthropic 于 11 月 9 日（美国时间）发布 Claude Fable 5.2 和 Claude Mythos 5.2。两者是同一底层模型：Fable 5.2 带网络安全与生物安全防护、即日向所有用户开放；Mythos 5.2…  
  原始来源 Source: <https://www.anthropic.com/claude-fable-and-mythos-5-2> · Shift: <https://shift.kai-nex.com/event/evt-861fefc5853e2217/>
- **Meta 发布最小最省钱的 Muse Ember：每百万输入 Token 0.10 美元，主打 Agent 的大量重复步骤**  
  Meta 于 11 月 9 日（美国时间）发布 Muse Ember，称其是最小、最高效的 Muse 模型，专门处理 Agent 反复执行的工具调用、编码子任务、路由、信息抽取和长文档解析。模型以 muse-ember-1.0 上线 Mus…  
  原始来源 Source: <https://research.meta.ai/blog/muse-ember> · Shift: <https://shift.kai-nex.com/event/evt-87a2cca8c1f6e264/>
- **Fireworks 更新安全事件：账单信息及部分客户的数据集、不完整模型权重被访问**  
  AI 推理平台 Fireworks 于 11 月 9 日更新 10 月的安全公告，称入侵范围比最初披露的大：账户与账单信息受影响，少数账户的密钥、数据集和不完整模型权重也被访问。公司称支付卡号未存储、未受影响，推理、Training SDK…  
  原始来源 Source: <https://fireworks.ai/security/bulletins/october-2026-security-incident-update> · Shift: <https://shift.kai-nex.com/event/evt-3ca33fc4c7adf515/>
<!-- THIS_WEEK:END -->

<!-- ARCHIVE:START -->
## 归档 Archive
- [2026-W46](weekly/2026-W46.md) · 7 条
- [2026-W45](weekly/2026-W45.md) · 28 条
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
