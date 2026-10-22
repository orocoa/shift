# 复用指南 Reuse guide

## 1. 读取 Shift 数据源 Consume the Shift feed

`https://shift.kai-nex.com/feed.json` 是 Shift 自己的 JSON 格式（**不是** jsonfeed.org 标准，普通 RSS 阅读器无法直接订阅）。It is Shift's own JSON schema (**not** jsonfeed.org), so regular RSS readers can't subscribe to it directly.

```bash
curl -s https://shift.kai-nex.com/feed.json | python3 -c "import json,sys; d=json.load(sys.stdin); [print(e['published_date'], e['title']) for e in d['events'][:5]]"
```

### 顶层字段 Top-level fields
| Field | Type | Notes |
|---|---|---|
| `schema_version` | int | Feed schema version |
| `date` / `created_at` | str | Feed date and build time (ISO 8601, UTC) |
| `events` | list | All published items (see below) |
| `days` | list | `{date, events}` grouped by day |
| `editorial_update` | object | Latest editorial changes |

### 条目字段 Event fields (`events[]`)
| Field | Type | Notes |
|---|---|---|
| `id` | str | e.g. `evt-1317a947cf89ccb5`; page: `https://shift.kai-nex.com/#/event/<id>` |
| `title`, `summary` | str | Chinese title and summary |
| `translations.en` | object | English title/summary when available |
| `published_date` | str | `YYYY-MM-DD` |
| `date_basis` | object | How the date was determined |
| `reference_numbers` | object | `{source_url: citation_number}` |
| `sources` | list | `{url, label, ...}` primary sources |
| `category`, `importance` | str, int | Category and editorial importance |
| `detail`, `report` | str, object | Full article: **please link, don't republish** |
| `media` | list | Media referenced by sources |

## 2. 生成你自己的周报 Build your own weekly

`scripts/build_weekly.py` 只依赖 Python 3 标准库。It accepts the Shift feed **or any jsonfeed.org v1.x feed** (`items[]` with `title`, `summary`/`content_text`, `date_published`, `url`/`external_url`).

```bash
python3 scripts/build_weekly.py --all                         # Shift feed, every week → weekly/
python3 scripts/build_weekly.py --week 2026-W43 --feed https://example.com/feed.json
python3 scripts/build_weekly.py --latest --update-readme      # refresh README (needs the marker comments)
```

## 许可 License
- 内容 Content (README, weekly/, docs/): CC BY 4.0, see [LICENSE](../LICENSE). Please credit "Shift (https://shift.kai-nex.com/)".
- 代码 Code (scripts/): MIT, see [LICENSE-CODE](../LICENSE-CODE).
