<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <img alt="유민호 — 사람들이 재지 않고 논쟁만 하는 것들을 재는 작은 도구를 만듭니다. JS/TS · 정적 분석 · 오픈소스 성능 개선." src="assets/banner-light.svg" width="100%">
</picture>

<p align="center">
  <a href="https://fixearly.m1k.app"><img alt="fixearly" src="https://img.shields.io/badge/npx-fixearly-2563eb?style=flat-square&logo=npm&logoColor=white"></a>
  <a href="https://m1k.app"><img alt="m1k.app" src="https://img.shields.io/badge/m1k.app-workshop-0f1723?style=flat-square"></a>
  <a href="https://github.com/m1kapp"><img alt="@m1kapp" src="https://img.shields.io/badge/org-%40m1kapp-7c8899?style=flat-square&logo=github"></a>
</p>

---

## 🧰 [M1K Projects](https://github.com/m1kapp)

만드는 것은 전부 한 org 에 모아두고, 지도는 **[m1k.app](https://m1k.app)** 에 있습니다.
있었으면 해서 만든 작은 도구들이고, 아래는 전부 지금 돌아갑니다.

| | 주소 | 하는 일 |
|---|---|---|
| **[fixearly](https://github.com/m1kapp/fixearly)** | [fixearly.m1k.app](https://fixearly.m1k.app) | JS/TS 를 *변경 비용*으로 채점 · 오픈소스 74곳 기준선 |
| **핫컷 / ytcc** <sub>(비공개)</sub> | [ytcc-next.vercel.app](https://ytcc-next.vercel.app) | 영상의 최고 순간을 댓글이 찾아줍니다 |
| **[Claude Run](https://github.com/m1kapp/claude-rank)** | [claude-rank](https://claude-rank-theta.vercel.app) | 제출된 usage-report 로 만드는 Claude 구독 가성비 랭킹 |
| **[PromptWing](https://github.com/m1kapp/promptwing)** | [promptwing.vercel.app](https://promptwing.vercel.app) | AI 이미지 프롬프트 스튜디오 |
| **[logodown](https://github.com/m1kapp/logodown)** | [logodown.vercel.app](https://logodown.vercel.app) | 마크다운 쓰듯 로고 만들기 |
| **[kit](https://github.com/m1kapp/kit)** | [kit-inky.vercel.app](https://kit-inky.vercel.app) | 위 것들이 공유하는 UI 킷 |
| **[m1kskills](https://github.com/m1kapp/m1kskills)** | — | 어느 AI 도구에나 붙여 쓰는 마크다운 스킬 |

<sub>그 외: [중위소득 계산기](https://median-income-calc.vercel.app) ·
formychildren(비공개) — 아이 생일 선물로 만든 게임이고, 여기서 유일하게 진짜 사용자가 있습니다.</sub>

<details>
<summary><b>fixearly 자세히</b> — 나중에 이 코드를 고칠 때 드는 비용을 재는 JS/TS 분석기</summary>

<br>

스타일도, 커버리지도 아닙니다. 100% 로컬, 업로드 없음, 설정 없음:

```bash
npx fixearly
```

요점은 등급이 아니라 그 등급이 **반증 가능해야 한다**는 겁니다. 그래서 자를 실제 코드에 댑니다 —
배너에 있는 **오픈소스 74곳**이 그 기준선이고, 채점축은 하나의 바를 넘어야만 들어옵니다.

> [!NOTE]
> 축은 **점수를 움직여야 하고**, 동시에 **메인테이너가 실제로 머지하는 PR 이 나와야** 합니다.
> 통계는 통과했는데 들고 갈 게 안 나와서 잘라낸 후보 축이 네 개 있습니다.

**머지된 것** — 도구가 찾고, 손으로 검증하고, 벤치마크를 붙여 보냈습니다.

<!-- auto:impact -->
| 머지 | 내용 |
|---|---|
| [openstatus#2583](https://github.com/openstatusHQ/openstatus/pull/2583) · 9.1k★ | 페이지 monitor 검증 뒤 중복 조회 |
| [mongoose#16474](https://github.com/Automattic/mongoose/pull/16474) · 27.5k★ | bulkSave 오류 문서 반복 매칭 |
| [pnpm#14032](https://github.com/pnpm/pnpm/pull/14032) · 36.4k★ | 의존성 분할 안 미사용 Set |
| [rollup#6482](https://github.com/rollup/rollup/pull/6482) · 26.3k★ | 청크 렌더 안 미사용 Map |
| [typebot#2572](https://github.com/baptisteArno/typebot.io/pull/2572) · 10.3k★ | in-depth analytics 순차 await |
| [ghost#29831](https://github.com/TryGhost/Ghost/pull/29831) · 55.1k★ | member 통계 안 미사용 Map |
| [medusa#16233](https://github.com/medusajs/medusa/pull/16233) · 36.1k★ | cart variant lookup O(n²) |
| [medusa#16188](https://github.com/medusajs/medusa/pull/16188) · 36.1k★ | translations batch match O(n²) |
| [ghost#29704](https://github.com/TryGhost/Ghost/pull/29704) · 55.1k★ | growth stats 집계 3회 직렬 |
| [vite#23114](https://github.com/vitejs/vite/pull/23114) · 82.7k★ | pure CSS 청크 선형 조회 |
| [n8n#34899](https://github.com/n8n-io/n8n/pull/34899) · 203.2k★ | resource-mapper schema validation O(n²) |
| [nocodb#14309](https://github.com/nocodb/nocodb/pull/14309) · 64.8k★ | user field validation O(n²) |
| [outline#13117](https://github.com/outline/outline/pull/13117) · 40.4k★ | markdown import merge O(n²) |

**닫힌 것 10건.**
<!-- /auto:impact -->

이긴 것과 진 것 전부는 [IMPACT.md](https://github.com/m1kapp/fixearly/blob/main/IMPACT.md) 에 있습니다.
GitHub API 로 생성되기 때문에 안 된 것만 조용히 빼는 게 불가능합니다.

> 주장이 아니라 확인 가능합니다 —
> [nocodb](https://github.com/nocodb/nocodb/graphs/contributors) 와
> [outline](https://github.com/outline/outline/graphs/contributors) 의 컨트리뷰터 목록에 있습니다.

</details>

---

## 📊 활동

스트릭과 1년치 잔디.

<p align="center">
  <img height="165" src="https://streak-stats.demolab.com?user=irontaek&hide_border=true&background=0D1117&ring=2563EB&fire=2563EB&currStreakLabel=2563EB&sideNums=E6EDF3&sideLabels=8B949E&dates=8B949E&stroke=30363D" alt="streak stats" />
</p>

<img width="100%" src="https://github-readme-activity-graph.vercel.app/graph?username=irontaek&bg_color=0D1117&color=8B949E&line=2563EB&point=58A6FF&area=true&area_color=2563EB&hide_border=true&radius=8" alt="contribution activity graph" />

---

## 그 밖에

**[nuxt-seo](https://github.com/harlan-zw/nuxt-seo)** 기여자.
예전에 만들었고 지금은 접은 것: [teamlog](https://github.com/irontaek/teamlog-front)(팀 블로그) ·
[cutin](https://github.com/irontaek/cutin)(농구 영상 편집).
글은 [uminoh.tistory.com](https://uminoh.tistory.com/) 에 씁니다.

<p>
  <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-black?style=flat-square&logo=typescript&logoColor=3178C6">
  <img alt="Nuxt" src="https://img.shields.io/badge/Nuxt-black?style=flat-square&logo=nuxt.js&logoColor=00DC82">
  <img alt="Vue" src="https://img.shields.io/badge/Vue-black?style=flat-square&logo=vue.js&logoColor=4FC08D">
  <img alt="NestJS" src="https://img.shields.io/badge/NestJS-black?style=flat-square&logo=nestjs&logoColor=E0234E">
  <img alt="Prisma" src="https://img.shields.io/badge/Prisma-black?style=flat-square&logo=prisma&logoColor=2D3748">
  <img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-black?style=flat-square&logo=postgresql&logoColor=4169E1">
</p>
