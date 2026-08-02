#!/usr/bin/env python3
"""
update-impact — README 의 임팩트 구역을 fixearly 의 impact.json 에서 다시 만든다.

프로필에 적힌 "머지 2건"은 세 번째가 머지되는 순간 거짓이 된다. 손으로 고치는 값은
반드시 어긋나므로(랜딩에서 '오픈소스 70개'가 8곳 남아 있던 것과 같은 병) 마커 사이만
생성하고, GitHub Actions 가 하루 한 번 돌린다.

바깥의 글(서사·판단)은 건드리지 않는다.

출처: m1kapp/fixearly 의 impact.json — impact.mjs 가 GitHub API 로 갱신해 커밋한다.
사용: python3 tools/update-impact.py [--check]
"""
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = "https://raw.githubusercontent.com/m1kapp/fixearly/main"
CHECK = "--check" in sys.argv

BEGIN = "<!-- auto:impact -->"
END = "<!-- /auto:impact -->"


def fetch(path):
    with urllib.request.urlopen(f"{RAW}/{path}", timeout=25) as r:
        return json.load(r)


def repo_short(f):
    """'nocodb · 64.4k★' → ('nocodb', '64.4k')"""
    m = re.match(r"^(.*?)\s*·\s*([\d.,]+k?)\s*★?\s*$", str(f.get("repoLabel", "")))
    return (m.group(1).strip(), m.group(2)) if m else (f["repo"].split("/")[-1], None)


def link(f):
    return f"https://github.com/{f['repo']}/pull/{f['pr']}"


def block(findings):
    merged = [f for f in findings if f.get("status") == "merged"]
    # 최근 머지가 위로. 세 번째가 붙어도 순서가 유지된다.
    merged.sort(key=lambda f: f.get("mergedAt") or "", reverse=True)
    approved = [f for f in findings if f.get("status") == "approved"]
    closed = [f for f in findings if f.get("status") == "closed"]

    out = []
    # 저장소 이름을 따로 열로 두면 PR 열과 겹친다. 별 수만 붙여 한 열로.
    out += ["| 머지 | 내용 |", "|---|---|"]
    for f in merged:
        name, stars = repo_short(f)
        star = f" · {stars}★" if stars else ""
        out.append(f"| [{name}#{f['pr']}]({link(f)}){star} | {f['title']} |")
    out.append("")

    names = ", ".join(f"[{repo_short(f)[0]}]({link(f)})" for f in approved)
    parts = []
    if approved:
        parts.append(f"승인 후 머지 대기 {len(approved)}건 — {names}.")
    if closed:
        parts.append(f"**닫힌 것 {len(closed)}건.**")
    out.append(" ".join(parts))
    return BEGIN + "\n" + "\n".join(out) + "\n" + END


findings = fetch("impact.json")["findings"]
changed, problems = [], []

for fname in ("README.md",):
    p = f"{ROOT}/{fname}"
    if not os.path.exists(p):
        problems.append(f"{fname} 없음")
        continue
    doc = open(p, encoding="utf-8").read()
    m = re.search(re.escape(BEGIN) + r".*?" + re.escape(END), doc, re.S)
    if not m:
        problems.append(f"{fname} 에 {BEGIN} 마커가 없다")
        continue
    want = block(findings)
    if m.group(0) != want:
        changed.append(fname)
        if not CHECK:
            open(p, "w", encoding="utf-8").write(doc[: m.start()] + want + doc[m.end():])

for p in problems:
    print(f"  ✗ {p}")

state = {}
for f in findings:
    state[f.get("status", "?")] = state.get(f.get("status", "?"), 0) + 1
summary = " · ".join(f"{k} {v}" for k, v in sorted(state.items()))

if CHECK:
    print(f"{'갱신 필요: ' + ', '.join(changed) if changed else '임팩트 구역이 최신이다'}  ({summary})")
    sys.exit(1 if (changed or problems) else 0)
print(f"{'갱신 ' + ', '.join(changed) if changed else '변경 없음'}  ({summary})")
sys.exit(1 if problems else 0)
