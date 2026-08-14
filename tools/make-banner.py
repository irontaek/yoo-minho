#!/usr/bin/env python3
"""
make-banner — 프로필 헤더 SVG 를 만든다. 라이트/다크 2벌.

왜 2벌인가: SVG 안에 `@media (prefers-color-scheme: dark)` 를 넣어도 <img> 로 참조하면
안 먹는다 — img 로 불린 SVG 는 부모 DOM 의 색 모드를 상속받지 않는다. GitHub 이 지원하는
방법은 <picture> + srcset 뿐이라 파일을 두 개 만든다.

<style> 도 안 쓴다. camo 프록시를 거치면 신뢰할 수 없어서 전부 presentation attribute
(fill=, stroke=)로 그린다.

미니멀 텍스트 배너 — 이름과 한 줄 소개만. 특정 프로젝트(fixearly) 데이터로 첫인상을
정하지 않는다. 등급 분포·머지 실적 같은 fixearly 자체 증거는 README 의 fixearly 박스에 있다.

사용: python3 tools/make-banner.py
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

THEME = {
    "light": dict(panel="#ffffff", border="#e4e9f0",
                   ink="#0f1723", ink2="#4a5769", ink3="#7c8899", accent="#2563eb"),
    "dark": dict(panel="#0d1117", border="#30363d",
                  ink="#e6edf3", ink2="#adbac7", ink3="#768390", accent="#58a6ff"),
}

MONO = "ui-monospace,'SF Mono','JetBrains Mono',Menlo,Consolas,monospace"
# 한글은 mono 로 쓰면 폴백이 지저분해진다 — 본문은 sans, 핸들만 mono 로 남긴다.
KSANS = ("'Apple SD Gothic Neo','Noto Sans KR','Malgun Gothic',ui-sans-serif,"
         "-apple-system,'Segoe UI',sans-serif")

STR = dict(
    name="유민호", handle="@irontaek", meta="· 서울 · @m1kapp",
    line1="사람들이 재지 않고 논쟁만 하는 것들을",
    line2="재는 작은 도구를 만듭니다.",
    sub="JS/TS · 정적 분석 · 오픈소스 성능 개선",
)

# m1k.app 의 아이콘(www.m1k.app/icon.svg) 원본 그대로 가져온 것 — 로켓 + K.
# 512x512 좌표계라 <g transform="translate(x,y) scale(s)"> 로 축소해 박는다.
ICON_INNER = '''<rect width="512" height="512" rx="77" fill="url(#mk-lg)"/>
<rect x="2.048" y="2.048" width="507.904" height="507.904" rx="74.952" fill="none" stroke="#f6f6f4" stroke-width="4.096" stroke-opacity="0.25"/>
<g transform="translate(87.0,179.2) scale(6.4000)"><path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></g>
<path d="M280.24 331.42L319.83 331.42L319.83 292.04L333.79 274.13L368.58 331.42L416.08 331.42L363.37 247.88L415.04 180.58L368.58 180.58L321.91 242.25L319.83 242.25L319.83 180.58L280.24 180.58Z" fill="#ffffff"/>'''


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build(t):
    c, S = THEME[t], STR
    W, H = 1000, 176
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}" role="img" aria-label="{S["name"]}">']

    o.append(f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" '
             f'fill="{c["panel"]}" stroke="{c["border"]}" stroke-width="1.5"/>')
    # 왼쪽 강조 띠
    o.append(f'<rect x="1.5" y="15" width="4" height="{H-30}" rx="2" fill="{c["accent"]}"/>')

    # 로고 — m1k.app 아이콘, 오른쪽 위에 56x56 로 축소해 박음
    icon, iy = 56, 32
    ix = W - 44 - icon
    o.append(f'<defs><linearGradient id="mk-lg" x1="0" y1="0" x2="1" y2="1">'
             f'<stop offset="0%" stop-color="#09090b"/><stop offset="100%" stop-color="#433946"/>'
             f'</linearGradient></defs>')
    o.append(f'<g transform="translate({ix},{iy}) scale({icon/512:.6f})">{ICON_INNER}</g>')

    o.append(f'<text x="44" y="60" font-family="{KSANS}" font-size="40" '
             f'font-weight="750" letter-spacing="-0.8" fill="{c["ink"]}">{esc(S["name"])}</text>')
    o.append(f'<text x="46" y="86" font-family="{MONO}" font-size="13" '
             f'fill="{c["accent"]}">{esc(S["handle"])}</text>')
    o.append(f'<text x="152" y="86" font-family="{KSANS}" font-size="13" '
             f'fill="{c["ink3"]}">{esc(S["meta"])}</text>')
    o.append(f'<text x="44" y="118" font-family="{KSANS}" font-size="17" '
             f'fill="{c["ink2"]}">{esc(S["line1"])}</text>')
    o.append(f'<text x="44" y="141" font-family="{KSANS}" font-size="17" '
             f'fill="{c["ink2"]}">{esc(S["line2"])}</text>')
    o.append(f'<text x="{W-44}" y="{H-24}" text-anchor="end" font-family="{MONO}" font-size="12" '
             f'fill="{c["ink3"]}">{esc(S["sub"])}</text>')

    o.append("</svg>")
    return "\n".join(o) + "\n"


os.makedirs(f"{ROOT}/assets", exist_ok=True)
for t in THEME:
    p = f"{ROOT}/assets/banner-{t}.svg"
    open(p, "w", encoding="utf-8").write(build(t))
    print(f"  assets/banner-{t}.svg  {os.path.getsize(p)}B")
