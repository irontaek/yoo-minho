### Minho Yoo

I build small tools that measure the things people usually just argue about.
Most of my current work lives under [**@m1kapp**](https://github.com/m1kapp).

---

### 🔬 [fixearly](https://github.com/m1kapp/fixearly) · [fixearly.m1k.app](https://fixearly.m1k.app)

A JS/TS analyzer that scores **the cost of changing this code later** — not style, not coverage.
Fully local, no upload, no config: `npx fixearly`

The point isn't the grade, it's that the grade has to be **falsifiable**. So I test the ruler
against real code: **74 open-source repos** form the baseline, and a scoring axis only gets in
if it clears one bar — it has to move the score **and** produce a pull request a maintainer
actually merges.

**Merged so far** — found by the tool, verified by hand, benchmarked before sending:

| PR | Repo | What |
|---|---|---|
| [nocodb#14309](https://github.com/nocodb/nocodb/pull/14309) | [nocodb](https://github.com/nocodb/nocodb) · 64.4k★ | O(1) workspace-user lookup in field validation |
| [outline#13117](https://github.com/outline/outline/pull/13117) | [outline](https://github.com/outline/outline) · 39.9k★ | O(n²) merge in markdown import |

Three more approved and waiting to merge — [vite](https://github.com/vitejs/vite/pull/23114),
[medusa](https://github.com/medusajs/medusa/pull/16188),
[novu](https://github.com/novuhq/novu/pull/12074). Four were closed.

The full log — wins and losses — is
[IMPACT.md](https://github.com/m1kapp/fixearly/blob/main/IMPACT.md). It's generated from the
GitHub API, so I can't quietly drop the ones that didn't land.

> Checkable, not claimed: the contributor graphs of
> [nocodb](https://github.com/nocodb/nocodb/graphs/contributors) and
> [outline](https://github.com/outline/outline/graphs/contributors) list me.

---

### Also

- [**m1kskills**](https://github.com/m1kapp/m1kskills) — markdown prompt-skills, portable to any AI tool
- [**claude-rank**](https://github.com/m1kapp/claude-rank) — Claude subscription value leaderboard
- Contributor to [nuxt-seo](https://github.com/harlan-zw/nuxt-seo)
- Earlier: [teamlog](https://github.com/yoo-minho/teamlog-front) (team blogging) ·
  [cutin](https://github.com/yoo-minho/cutin) (basketball video editing) — both retired

---

<img src="https://img.shields.io/badge/typescript-black?style=flat-square&logo=typescript&logoColor=3178C6" />&nbsp;
<img src="https://img.shields.io/badge/nuxt.js-black?style=flat-square&logo=nuxt.js&logoColor=00DC82" />&nbsp;
<img src="https://img.shields.io/badge/vue.js-black?style=flat-square&logo=vue.js&logoColor=4FC08D" />&nbsp;
<img src="https://img.shields.io/badge/nestjs-black?style=flat-square&logo=nestjs&logoColor=E0234E" />&nbsp;
<img src="https://img.shields.io/badge/prisma-black?style=flat-square&logo=prisma&logoColor=2D3748" />&nbsp;
<img src="https://img.shields.io/badge/postgresql-black?style=flat-square&logo=PostgreSQL&logoColor=4169E1" />
