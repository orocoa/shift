#!/usr/bin/env python3
"""Generate a weekly Markdown index from the public Shift feed.

Usage:
  python3 scripts/build_weekly.py --week 2026-W43 [--ids evt-a,evt-b] [--feed URL_OR_PATH] [-o weekly/2026-W43.md]
Without --ids, includes every event in the feed. One-line summary only (no full text).
"""
import argparse, json, sys, urllib.request

FEED = "https://kai-nex.com/shift/feed.json"
SITE = "https://kai-nex.com/shift/#/event/"

def load(src):
    if src.startswith("http"):
        with urllib.request.urlopen(src, timeout=30) as r:
            return json.load(r)
    return json.load(open(src, encoding="utf-8"))

def one_line(text, n=120):
    t = " ".join((text or "").split())
    return t if len(t) <= n else t[:n].rstrip() + "…"

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--week", required=True)
    p.add_argument("--ids", default="")
    p.add_argument("--feed", default=FEED)
    p.add_argument("-o", "--out")
    a = p.parse_args()
    events = load(a.feed).get("events", [])
    want = [i for i in a.ids.split(",") if i]
    if want:
        by = {e["id"]: e for e in events}
        missing = [i for i in want if i not in by]
        if missing:
            sys.exit(f"not in feed: {missing}")
        events = [by[i] for i in want]
    lines = [f"# {a.week}", ""]
    for e in events:
        src = next(iter(e.get("reference_numbers") or {}), "")
        lines += [f"- **{e['title']}**  ", f"  {one_line(e.get('summary'))}  ",
                  f"  原始来源 Source: <{src}> · Shift: <{SITE}{e['id']}>"]
    lines += ["", "> 摘要基于官方发布，厂商数据为厂商自述。Summaries rely on official sources; vendor figures are vendor claims.", ""]
    out = "\n".join(lines)
    if a.out:
        open(a.out, "w", encoding="utf-8").write(out)
    else:
        print(out)

if __name__ == "__main__":
    main()
