<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <img alt="Minho Yoo — I build small tools that measure the things people usually just argue about. 74 open-source repos graded by fixearly: S 16, A 21, B 16, C 14, D 6, E 1." src="assets/banner-light.svg" width="100%">
</picture>

<p align="center">
  <b>English</b> · <a href="README.ko.md">한국어</a>
</p>

<p align="center">
  <a href="https://fixearly.m1k.app"><img alt="fixearly" src="https://img.shields.io/badge/npx-fixearly-2563eb?style=flat-square&logo=npm&logoColor=white"></a>
  <a href="https://m1k.app"><img alt="m1k.app" src="https://img.shields.io/badge/m1k.app-workshop-0f1723?style=flat-square"></a>
  <a href="https://github.com/m1kapp"><img alt="@m1kapp" src="https://img.shields.io/badge/org-%40m1kapp-7c8899?style=flat-square&logo=github"></a>
</p>

---

## 🔬 fixearly

**[m1kapp/fixearly](https://github.com/m1kapp/fixearly)** · **[fixearly.m1k.app](https://fixearly.m1k.app)**

A JS/TS analyzer that scores **the cost of changing this code later** — not style, not coverage.
Fully local, no upload, no config:

```bash
npx fixearly
```

The point isn't the grade. It's that the grade has to be **falsifiable**. So the ruler gets tested
against real code — the **74 open-source repos** in the banner are the baseline — and a scoring axis
only gets in if it clears one bar:

> [!NOTE]
> An axis has to **move the score** *and* **produce a pull request a maintainer actually merges**.
> Four candidate axes passed the statistics and were cut anyway, because nothing shippable came out of them.

### Merged

Found by the tool, verified by hand, benchmarked before sending.

| PR | Repo | What |
|---|---|---|
| [nocodb#14309](https://github.com/nocodb/nocodb/pull/14309) | [nocodb](https://github.com/nocodb/nocodb) · 64.4k★ | O(1) workspace-user lookup in field validation |
| [outline#13117](https://github.com/outline/outline/pull/13117) | [outline](https://github.com/outline/outline) · 39.9k★ | O(n²) merge in markdown import |

Three more approved and waiting to merge — [vite](https://github.com/vitejs/vite/pull/23114),
[medusa](https://github.com/medusajs/medusa/pull/16188), [novu](https://github.com/novuhq/novu/pull/12074).
**Four were closed.**

The full log — wins and losses — is [IMPACT.md](https://github.com/m1kapp/fixearly/blob/main/IMPACT.md).
It's generated from the GitHub API, so the ones that didn't land can't be quietly dropped.

> Checkable, not claimed — the contributor graphs of
> [nocodb](https://github.com/nocodb/nocodb/graphs/contributors) and
> [outline](https://github.com/outline/outline/graphs/contributors) list me.

---

## 🧰 [@m1kapp](https://github.com/m1kapp) — the workshop

Everything I ship lives in one org, mapped at **[m1k.app](https://m1k.app)**. Small tools, each one
built because I wanted it to exist. All of these are live right now.

| | Live | What it does |
|---|---|---|
| **[fixearly](https://github.com/m1kapp/fixearly)** | [fixearly.m1k.app](https://fixearly.m1k.app) | Scores JS/TS by *change cost*, benchmarked on 74 OSS repos |
| **핫컷 / ytcc** <sub>(private)</sub> | [ytcc-next.vercel.app](https://ytcc-next.vercel.app) | Finds a video's best moment from its own comments |
| **[Claude Run](https://github.com/m1kapp/claude-rank)** | [claude-rank](https://claude-rank-theta.vercel.app) | Claude subscription value leaderboard, from submitted usage reports |
| **[PromptWing](https://github.com/m1kapp/promptwing)** | [promptwing.vercel.app](https://promptwing.vercel.app) | AI image prompt studio |
| **[logodown](https://github.com/m1kapp/logodown)** | [logodown.vercel.app](https://logodown.vercel.app) | Make logos the way you write markdown |
| **[kit](https://github.com/m1kapp/kit)** | [kit-inky.vercel.app](https://kit-inky.vercel.app) | The shared UI kit the rest of these are built from |
| **[m1kskills](https://github.com/m1kapp/m1kskills)** | — | Markdown prompt-skills, portable to any AI tool |

<sub>Also: [중위소득 계산기](https://median-income-calc.vercel.app) (Korean income calculator) ·
formychildren (private) — a birthday game for my kid, and the only thing here with a
real user.</sub>

---

## Elsewhere

Contributor to **[nuxt-seo](https://github.com/harlan-zw/nuxt-seo)**.
Earlier and now retired: [teamlog](https://github.com/yoo-minho/teamlog-front) (team blogging) ·
[cutin](https://github.com/yoo-minho/cutin) (basketball video editing).
I write at [uminoh.tistory.com](https://uminoh.tistory.com/).

<p>
  <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-black?style=flat-square&logo=typescript&logoColor=3178C6">
  <img alt="Nuxt" src="https://img.shields.io/badge/Nuxt-black?style=flat-square&logo=nuxt.js&logoColor=00DC82">
  <img alt="Vue" src="https://img.shields.io/badge/Vue-black?style=flat-square&logo=vue.js&logoColor=4FC08D">
  <img alt="NestJS" src="https://img.shields.io/badge/NestJS-black?style=flat-square&logo=nestjs&logoColor=E0234E">
  <img alt="Prisma" src="https://img.shields.io/badge/Prisma-black?style=flat-square&logo=prisma&logoColor=2D3748">
  <img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-black?style=flat-square&logo=postgresql&logoColor=4169E1">
</p>

<sub>The banner isn't decoration — it's the live grade distribution of the fixearly corpus, regenerated
by <a href="tools/make-banner.py"><code>tools/make-banner.py</code></a>. The ▲ marks where fixearly
scores itself.</sub>
