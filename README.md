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

- **Aramco 完成入股 HUMAIN：取得 49% 股权，2026 年投入约 26 亿美元现金**  
  沙特公共投资基金（PIF）与沙特阿美（Aramco）于 2026 年 11 月 1 日宣布完成 HUMAIN 交易：Aramco 通过全资子公司取得这家沙特 AI 公司 49% 的股权，PIF 保留 51%。Aramco 除转入自有 AI…  
  原始来源 Source: <https://www.aramco.com/en/news-media/news/2026/pif-and-aramco-close-humain-transaction-to-accelerate-humains-global-growth> · Shift: <https://shift.kai-nex.com/event/evt-64c67f684ecd28f4/>
- **ChatGPT 将合并 Chat 与 Work：12 月起 ChatGPT 和 Codex 共用 Token 额度，付费账户按设备与支付卡限量**  
  据 The Decoder 11 月 1 日引述 OpenAI 更新的帮助中心页面，ChatGPT 正把 Chat 与 Work 两种模式并到同一界面；从 12 月起，Plus、Pro 和 Business 套餐在 ChatGPT 与 Co…  
  原始来源 Source: <https://the-decoder.com/openais-upcoming-chat-and-work-merger-in-chatgpt-signals-the-end-of-all-you-can-prompt-pricing/> · Shift: <https://shift.kai-nex.com/event/evt-146790c19d15ac71/>
- **Axios：OpenAI 中期选举后将推动 AI「限速」相关提案，并把数据中心改称「AI 计算园区」**  
  据 Axios 11 月 1 日独家报道（经 Silicon Report 转述），OpenAI 计划在美国周二中期选举后发起一轮政策和公关攻势：提案包括推动制定 AI「限速」、鼓励美国参与制定全球标准、展示 AI 如何赋能日常生活，以及把…  
  原始来源 Source: <https://www.siliconreport.com/openai-plans-post-midterm-push-for-ai-speed-limits-axios-reports> · Shift: <https://shift.kai-nex.com/event/evt-892cb64d23d3640c/>
- **DeepSeek 公开 Super-agent 架构并开源原型：常驻 Router 调度多个并行 Worker**  
  DeepSeek Harness 团队于 2026 年 10 月 31 日发布《Super-agent 设计探索》，提出让编程智能体脱离单一会话、常驻在线并行推进多项工作的架构：Router 层统一对接人和分派任务，Worker 层在隔离会…  
  原始来源 Source: <https://github.com/deepseek-ai/dsh-superagent-prototype> · Shift: <https://shift.kai-nex.com/event/evt-cba0961d50a52122/>
- **Anthropic 给四款旧 Claude 模型补加文本水印，Opus 4.6 与 Sonnet 4.6 改采样参数即失效**  
  据 The Decoder 2026 年 10 月 31 日报道，Anthropic 在给 API 客户的邮件中表示，将为 Claude Mythos 5、Opus 4.7、Opus 4.6 和 Sonnet 4.6 加上文本水印，以赶上欧…  
  原始来源 Source: <https://the-decoder.com/anthropics-watermark-rollout-leaves-a-loophole-on-two-older-claude-models/> · Shift: <https://shift.kai-nex.com/event/evt-5e540095393d705c/>
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

[查看本周全部 25 条 See all →](weekly/2026-W44.md)
<!-- THIS_WEEK:END -->

<!-- ARCHIVE:START -->
## 归档 Archive
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
