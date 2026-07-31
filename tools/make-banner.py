#!/usr/bin/env python3
"""
make-banner — 프로필 헤더 SVG 를 만든다. 라이트/다크 2벌.

왜 2벌인가: SVG 안에 `@media (prefers-color-scheme: dark)` 를 넣어도 <img> 로 참조하면
안 먹는다 — img 로 불린 SVG 는 부모 DOM 의 색 모드를 상속받지 않는다. GitHub 이 지원하는
방법은 <picture> + srcset 뿐이라 파일을 두 개 만든다.

<style> 도 안 쓴다. camo 프록시를 거치면 신뢰할 수 없어서 전부 presentation attribute
(fill=, stroke=)로 그린다.

배너에 그리는 건 장식이 아니라 실제 데이터다 — fixearly 코퍼스 74곳의 등급 분포와,
그 자를 자기 자신에게 댄 점수. 숫자가 바뀌면 이 스크립트를 다시 돌린다.

사용: python3 tools/make-banner.py
"""
import json
import os
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS = "https://raw.githubusercontent.com/m1kapp/fixearly/main/data/corpus.json"

# 자가채점은 코퍼스에 없다(fixearly 는 자기 보드에 안 올라간다). CLI 출력에서 옮겨 적는다.
SELF = {"grade": "B+", "score": 79}

THEME = {
    "light": dict(
        panel="#ffffff", border="#e4e9f0", rule="#eef2f7",
        ink="#0f1723", ink2="#4a5769", ink3="#7c8899", accent="#2563eb",
        grade={"S": "#0f7a63", "A": "#2f8f5b", "B": "#7d8a2c",
               "C": "#c0862e", "D": "#bf4a38", "E": "#8f2f24"},
    ),
    "dark": dict(
        panel="#0d1117", border="#30363d", rule="#21262d",
        ink="#e6edf3", ink2="#adbac7", ink3="#768390", accent="#58a6ff",
        grade={"S": "#2ea88a", "A": "#4fb87a", "B": "#a8b73a",
               "C": "#e0a53f", "D": "#e06c56", "E": "#c74a3c"},
    ),
}

SANS = "ui-sans-serif,-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,'SF Mono','JetBrains Mono',Menlo,Consolas,monospace"
# 한글은 mono 로 쓰면 폴백이 지저분해진다 — 본문은 sans, 숫자·핸들만 mono 로 남긴다.
KSANS = ("'Apple SD Gothic Neo','Noto Sans KR','Malgun Gothic',ui-sans-serif,"
         "-apple-system,'Segoe UI',sans-serif")

ORDER = ["S", "A", "B", "C", "D", "E"]

# 배너에 들어가는 문장. 언어별로 두 벌 × 테마 두 벌 = SVG 4개.
STR = {
    "en": dict(
        name="Minho Yoo", meta="· Seoul · @m1kapp", body=SANS, name_size=40,
        line1="I build small tools that measure the things",
        line2="people usually just argue about.",
        sub="JS/TS · static analysis · open-source performance",
        caption="{n} OPEN-SOURCE REPOS · GRADED BY FIXEARLY {v}",
        cap_font=MONO, cap_size=11.5, cap_track="0.08em",
        self="fixearly itself: {g} {s}",
    ),
    "ko": dict(
        name="유민호", meta="· 서울 · @m1kapp", body=KSANS, name_size=40,
        line1="사람들이 재지 않고 논쟁만 하는 것들을",
        line2="재는 작은 도구를 만듭니다.",
        sub="JS/TS · 정적 분석 · 오픈소스 성능 개선",
        caption="오픈소스 {n}곳 · fixearly {v} 로 채점",
        cap_font=KSANS, cap_size=12.5, cap_track="0.02em",
        self="fixearly 자가채점 {g} {s}",
    ),
}


def load():
    with urllib.request.urlopen(CORPUS, timeout=20) as r:
        c = json.load(r)
    dist = {k: 0 for k in ORDER}
    for repo in c["repos"]:
        g = (repo.get("gradeF") or repo.get("grade") or "?")[0]
        if g in dist:
            dist[g] += 1
    return c, dist


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def build(t, lang, corpus, dist):
    c, S = THEME[t], STR[lang]
    W, H = 1000, 228
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}" role="img" aria-label="Minho Yoo">']

    # 판
    o.append(f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" '
             f'fill="{c["panel"]}" stroke="{c["border"]}" stroke-width="1.5"/>')
    # 왼쪽 강조 띠 — 등급색을 순서대로 쌓아 자(ruler)를 암시한다
    seg = (H - 30) / len(ORDER)
    for i, g in enumerate(ORDER):
        o.append(f'<rect x="1.5" y="{15 + i*seg:.1f}" width="4" height="{seg:.1f}" '
                 f'fill="{c["grade"][g]}"/>')

    # ── 왼쪽: 이름 ──────────────────────────────────────────────
    o.append(f'<text x="44" y="72" font-family="{S["body"]}" font-size="{S["name_size"]}" '
             f'font-weight="750" letter-spacing="-0.8" fill="{c["ink"]}">{esc(S["name"])}</text>')
    o.append(f'<text x="46" y="98" font-family="{MONO}" font-size="13" '
             f'fill="{c["accent"]}">@yoo-minho</text>')
    o.append(f'<text x="152" y="98" font-family="{S["body"]}" font-size="13" '
             f'fill="{c["ink3"]}">{esc(S["meta"])}</text>')
    o.append(f'<text x="44" y="135" font-family="{S["body"]}" font-size="16" '
             f'fill="{c["ink2"]}">{esc(S["line1"])}</text>')
    o.append(f'<text x="44" y="157" font-family="{S["body"]}" font-size="16" '
             f'fill="{c["ink2"]}">{esc(S["line2"])}</text>')
    o.append(f'<text x="44" y="184" font-family="{S["body"]}" font-size="12" '
             f'fill="{c["ink3"]}">{esc(S["sub"])}</text>')

    # ── 오른쪽: 코퍼스 등급 분포 ───────────────────────────────
    x0, base, bw, gap = 566, 152, 46, 22
    top, mx = 62, max(dist.values())
    o.append(f'<text x="{x0}" y="42" font-family="{S["cap_font"]}" font-size="{S["cap_size"]}" '
             f'letter-spacing="{S["cap_track"]}" fill="{c["ink3"]}">'
             f'{esc(S["caption"].format(n=corpus["n"], v=corpus["version"]))}</text>')
    o.append(f'<line x1="{x0}" y1="{base+.5}" x2="{x0+6*bw+5*gap}" y2="{base+.5}" '
             f'stroke="{c["border"]}" stroke-width="1"/>')

    for i, g in enumerate(ORDER):
        n = dist[g]
        h = max(3, (base - top) * n / mx)
        x = x0 + i * (bw + gap)
        o.append(f'<rect x="{x}" y="{base-h:.1f}" width="{bw}" height="{h:.1f}" rx="3" '
                 f'fill="{c["grade"][g]}"/>')
        o.append(f'<text x="{x+bw/2}" y="{base-h-8:.1f}" text-anchor="middle" '
                 f'font-family="{MONO}" font-size="12.5" font-weight="700" '
                 f'fill="{c["ink2"]}">{n}</text>')
        o.append(f'<text x="{x+bw/2}" y="{base+19}" text-anchor="middle" '
                 f'font-family="{MONO}" font-size="13" font-weight="700" '
                 f'fill="{c["grade"][g]}">{g}</text>')

    # 자기 자신도 잰다 — B 칸 아래에 표시. 중간이라는 게 요점이다.
    bx = x0 + ORDER.index(SELF["grade"][0]) * (bw + gap) + bw / 2
    o.append(f'<text x="{bx}" y="{base+36}" text-anchor="middle" font-family="{MONO}" '
             f'font-size="11" fill="{c["ink3"]}">▲</text>')
    o.append(f'<text x="{bx}" y="{base+49}" text-anchor="middle" font-family="{S["body"]}" '
             f'font-size="11" fill="{c["ink3"]}">'
             f'{esc(S["self"].format(g=SELF["grade"], s=SELF["score"]))}</text>')

    o.append("</svg>")
    return "\n".join(o) + "\n"


corpus, dist = load()
os.makedirs(f"{ROOT}/assets", exist_ok=True)
for lang in STR:
    for t in THEME:
        tag = "" if lang == "en" else f"-{lang}"
        p = f"{ROOT}/assets/banner{tag}-{t}.svg"
        open(p, "w", encoding="utf-8").write(build(t, lang, corpus, dist))
        print(f"  assets/banner{tag}-{t}.svg  {os.path.getsize(p)}B")
print(f"  코퍼스 {corpus['n']}곳 {corpus['version']} · "
      + " ".join(f"{k}{dist[k]}" for k in ORDER))
