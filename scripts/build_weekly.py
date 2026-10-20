#!/usr/bin/env python3
"""Build weekly Markdown archives from the public Shift feed (https://kai-nex.com/shift/feed.json).

Also accepts any jsonfeed.org (v1.x) feed via --feed. Items are grouped by ISO week of `published_date`. One-line summaries only (no full text).

Usage:
  python3 scripts/build_weekly.py --all [--update-readme]      # backfill every week
  python3 scripts/build_weekly.py --latest [--update-readme]   # only the newest week
  python3 scripts/build_weekly.py --week 2026-W43 [--ids evt-a,evt-b] [-o FILE]
"""
import argparse, datetime as dt, json, os, re, sys, urllib.request
from collections import defaultdict

FEED = "https://kai-nex.com/shift/feed.json"
SITE = "https://kai-nex.com/shift/#/event/"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTE = "> 摘要基于官方发布，厂商数据为厂商自述。Summaries rely on official sources; vendor figures are vendor claims."

def load(src):
    if src.startswith("http"):
        req = urllib.request.Request(src, headers={"User-Agent": "shift-weekly"})
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)
    return json.load(open(src, encoding="utf-8"))

def normalize(feed):
    """Return Shift-style events from either the Shift feed or a jsonfeed.org feed (version 1.x)."""
    if "events" in feed:
        return feed["events"]
    out = []
    for it in feed.get("items", []):
        src = it.get("external_url") or it.get("url") or ""
        out.append({"id": it.get("id", src), "title": it.get("title") or "", "summary": it.get("summary") or it.get("content_text") or "",
                    "published_date": (it.get("date_published") or "")[:10], "reference_numbers": {src: 1} if src else {},
                    "link": it.get("url") or src})
    return out

def one_line(text, n=120):
    t = " ".join((text or "").split())
    return t if len(t) <= n else t[:n].rstrip() + "…"

def week_of(date):
    y, w, _ = dt.date.fromisoformat(date[:10]).isocalendar()
    return f"{y}-W{w:02d}"

def week_range(week):
    y, w = int(week[:4]), int(week[-2:])
    mon = dt.date.fromisocalendar(y, w, 1)
    return mon, mon + dt.timedelta(days=6)

def items_md(events):
    out = []
    for e in events:
        src = next(iter(e.get("reference_numbers") or {}), "")
        out += [f"- **{e['title']}**  ", f"  {one_line(e.get('summary'))}  ",
                (f"  原始来源 Source: <{src}> · Link: <{e['link']}>" if "link" in e else f"  原始来源 Source: <{src}> · Shift: <{SITE}{e['id']}>")]
    return "\n".join(out)

def sort_events(evs):
    return sorted(evs, key=lambda e: (e.get("published_date", ""), e.get("importance") or 0), reverse=True)

def week_md(week, events):
    a, b = week_range(week)
    return f"# {week}（{a:%m-%d} ~ {b:%m-%d}）\n\n共 {len(events)} 条 · {len(events)} items\n\n{items_md(events)}\n\n{NOTE}\n"

def write(path, text):
    old = open(path, encoding="utf-8").read() if os.path.exists(path) else None
    if old != text:
        open(path, "w", encoding="utf-8").write(text)
        print("updated", os.path.relpath(path, ROOT))

def update_readme(groups):
    path = os.path.join(ROOT, "README.md")
    r = open(path, encoding="utf-8").read()
    latest = max(groups)
    top = sort_events(groups[latest])[:15]
    more = f"\n\n[查看本周全部 {len(groups[latest])} 条 See all →](weekly/{latest}.md)" if len(groups[latest]) > len(top) else ""
    this_week = f"<!-- THIS_WEEK:START -->\n## 本周 This week（{latest}）\n\n{items_md(top)}{more}\n<!-- THIS_WEEK:END -->"
    archive = "<!-- ARCHIVE:START -->\n## 归档 Archive\n" + "\n".join(
        f"- [{w}](weekly/{w}.md) · {len(groups[w])} 条" for w in sorted(groups, reverse=True)) + "\n<!-- ARCHIVE:END -->"
    r = re.sub(r"<!-- THIS_WEEK:START -->.*?<!-- THIS_WEEK:END -->", lambda m: this_week, r, flags=re.S)
    r = re.sub(r"<!-- ARCHIVE:START -->.*?<!-- ARCHIVE:END -->", lambda m: archive, r, flags=re.S)
    r = re.sub(r"\(#本周-this-week[^)]*\)", "(#本周-this-week" + latest.lower().replace("-", "-") + ")", r)
    r = re.sub(r"\[本周 This week（[^）]*）\]", f"[本周 This week（{latest}）]", r)
    write(path, r)

def main():
    p = argparse.ArgumentParser()
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--all", action="store_true")
    g.add_argument("--latest", action="store_true")
    g.add_argument("--week")
    p.add_argument("--ids", default="")
    p.add_argument("--feed", default=FEED)
    p.add_argument("-o", "--out")
    p.add_argument("--update-readme", action="store_true")
    a = p.parse_args()
    events = [e for e in normalize(load(a.feed)) if e.get("published_date") and e.get("title")]
    groups = defaultdict(list)
    for e in events:
        groups[week_of(e["published_date"])].append(e)
    if a.week:
        evs = groups.get(a.week, [])
        if a.ids:
            by = {e["id"]: e for e in events}
            want = [i for i in a.ids.split(",") if i]
            missing = [i for i in want if i not in by]
            if missing:
                sys.exit(f"not in feed: {missing}")
            evs = [by[i] for i in want]
        text = week_md(a.week, sort_events(evs) if not a.ids else evs)
        if a.out:
            write(a.out, text)
        else:
            print(text)
        return
    weeks = sorted(groups) if a.all else [max(groups)]
    os.makedirs(os.path.join(ROOT, "weekly"), exist_ok=True)
    for w in weeks:
        write(os.path.join(ROOT, "weekly", f"{w}.md"), week_md(w, sort_events(groups[w])))
        print(f"{w}: {len(groups[w])} items")
    if a.update_readme:
        update_readme(groups)

if __name__ == "__main__":
    main()
