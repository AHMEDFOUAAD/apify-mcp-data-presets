# Bundle: Public job boards (Greenhouse, Lever, multi-ATS)

> **Disclosure:** I (GitHub @AHMEDFOUAAD, Apify user `ahmed.fouaad82`) built and sell these Actors on Apify Store. They are **paid per result** (pay-per-event). The first results of every run are free (25 for most of these Actors; see each Store page's Pricing tab), then the listed price applies. You need **your own Apify account** (OAuth sign-in or your own API token); runs bill to your account, and Apify's free plan includes $5/month of usage. This repo only contains client configs: it is not affiliated with or endorsed by Apify.

**Who it is for:** Recruiting/sourcing agents, job-market research, job-alert bots.

**MCP endpoint (Apify hosted server, preselected Actors):**

```text
https://mcp.apify.com/?tools=ahmed.fouaad82/greenhouse-public-jobs,ahmed.fouaad82/lever-salary-jobs,ahmed.fouaad82/ats-public-jobs
```

| Actor (Store page) | MCP tool name | What it returns | Price after the free first results* |
|---|---|---|---|
| [Greenhouse Jobs Scraper & API](https://apify.com/ahmed.fouaad82/greenhouse-public-jobs) | `ahmed-dot-fouaad82--greenhouse-public-jobs` | Public job posts from Greenhouse boards (by board token), with title/location/updated-since filters. | $1.00 per 1,000 jobs |
| [Lever Jobs Scraper - Salary Ranges & Remote Filters](https://apify.com/ahmed.fouaad82/lever-salary-jobs) | `ahmed-dot-fouaad82--lever-salary-jobs` | Public Lever postings with parsed salary ranges, minimum-salary and remote-only filters. | $2.00 per 1,000 jobs |
| [ATS Jobs Scraper - Lever, Greenhouse, Workable, Recruitee](https://apify.com/ahmed.fouaad82/ats-public-jobs) | `ahmed-dot-fouaad82--ats-public-jobs` | One normalized job schema across several ATS boards, with incremental (new-only) mode. | $2.00 per 1,000 jobs |

\* Prices read from the public Apify Store API on 2026-11-11; the Store page Pricing tab is authoritative.

The server also adds `get-actor-run`, `get-dataset-items`, `get-key-value-store-record` and `abort-actor-run`, so the agent can read results and stop runs.

## Install

### Claude Desktop / Claude.ai (recommended: connector with OAuth)
Settings → Connectors → **Add custom connector** → name `apify-public-jobs`, URL = the endpoint above → sign in to Apify when asked.

No connector support? Use the stdio bridge in [`claude_desktop_config.json`](claude_desktop_config.json) (needs Node.js; replace `YOUR_APIFY_TOKEN` locally, never commit it).

### Cursor
Copy [`cursor.mcp.json`](cursor.mcp.json) into `~/.cursor/mcp.json` (global) or `.cursor/mcp.json` (project). Cursor opens the Apify OAuth sign-in on first use.
Token instead of OAuth: [`cursor.mcp.token.json`](cursor.mcp.token.json) reads `APIFY_TOKEN` from your environment.

### VS Code (GitHub Copilot agent mode)
Copy [`vscode.mcp.json`](vscode.mcp.json) into `.vscode/mcp.json`. Token instead of OAuth: [`vscode.mcp.token.json`](vscode.mcp.token.json) prompts for the token and stores it securely.

### Claude Code
```bash
claude mcp add apify-public-jobs "https://mcp.apify.com/?tools=ahmed.fouaad82/greenhouse-public-jobs,ahmed.fouaad82/lever-salary-jobs,ahmed.fouaad82/ats-public-jobs" -t http
```

## Try it
- List open engineering roles on the Greenhouse board `stripe` updated in the last 7 days. Use maxResults 20.
- Find remote Lever jobs at `spotify` with a published salary range; return title, location and salary.
- Pull up to 20 jobs across these company job-board URLs into one schema: <Greenhouse/Lever/Workable/Recruitee board URLs>.

## Keep cost under control
- Ask for small `maxResults` first; the first results of each run are free.
- Set a monthly usage limit in Apify Console → Billing → Limits.
- Each paid result is charged once; failed runs are not charged per result.
