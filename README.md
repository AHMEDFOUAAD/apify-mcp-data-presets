# Apify MCP data presets for AI agents

Copy-paste MCP configs that give Claude Desktop, Cursor, VS Code (Copilot) or Claude Code a **small, focused set of public-web-data tools** instead of the whole Apify Store. Each bundle points the official hosted [Apify MCP server](https://docs.apify.com/platform/integrations/mcp) at three specific Actors using its documented `?tools=` URL parameter, so the agent sees exactly three dedicated tools plus the run/dataset helpers.

> **Disclosure:** I (GitHub @AHMEDFOUAAD, Apify user `ahmed.fouaad82`) built and sell these Actors on Apify Store. They are **paid per result** (pay-per-event). The first results of every run are free (25 for most of these Actors; see each Store page's Pricing tab), then the listed price applies. You need **your own Apify account** (OAuth sign-in or your own API token); runs bill to your account, and Apify's free plan includes $5/month of usage. This repo only contains client configs: it is not affiliated with or endorsed by Apify.

| Bundle | Actors | Endpoint |
|---|---|---|
| [Public job boards (Greenhouse, Lever, multi-ATS)](bundles/jobs/) | [greenhouse-public-jobs](https://apify.com/ahmed.fouaad82/greenhouse-public-jobs), [lever-salary-jobs](https://apify.com/ahmed.fouaad82/lever-salary-jobs), [ats-public-jobs](https://apify.com/ahmed.fouaad82/ats-public-jobs) | `https://mcp.apify.com/?tools=ahmed.fouaad82/greenhouse-public-jobs,ahmed.fouaad82/lever-salary-jobs,ahmed.fouaad82/ats-public-jobs` |
| [Content for RAG (RSS, podcast transcripts, PDF text)](bundles/content-for-rag/) | [rss-feed-reader](https://apify.com/ahmed.fouaad82/rss-feed-reader), [podcast-published-transcripts](https://apify.com/ahmed.fouaad82/podcast-published-transcripts), [public-pdf-text](https://apify.com/ahmed.fouaad82/public-pdf-text) | `https://mcp.apify.com/?tools=ahmed.fouaad82/rss-feed-reader,ahmed.fouaad82/podcast-published-transcripts,ahmed.fouaad82/public-pdf-text` |
| [Site audit (sitemap URLs, link/status checks, dedup)](bundles/site-audit/) | [sitemap-extractor](https://apify.com/ahmed.fouaad82/sitemap-extractor), [url-status-checker](https://apify.com/ahmed.fouaad82/url-status-checker), [dataset-dedup-merge](https://apify.com/ahmed.fouaad82/dataset-dedup-merge) | `https://mcp.apify.com/?tools=ahmed.fouaad82/sitemap-extractor,ahmed.fouaad82/url-status-checker,ahmed.fouaad82/dataset-dedup-merge` |

Each bundle folder has: `cursor.mcp.json`, `vscode.mcp.json`, token variants, `claude_desktop_config.json` (stdio bridge via `mcp-remote`) and a `server.json` (official MCP Registry entry).

## Why presets?
- **Fewer, sharper tools.** A preselected endpoint exposes only the tools for one job, which keeps the agent's tool list short and its choices predictable (Apify recommends pinning tools in production).
- **Fresh public data.** Job boards, feeds, transcripts, PDFs, sitemaps and link status, fetched at run time, returned as structured JSON.
- **Pay per result.** No subscription for these Actors; the first results of every run are free.

## Verified
On 2026-11-11 the three endpoints were initialized against `https://mcp.apify.com` (server `apify-mcp-server` 0.21.5) and `tools/list` returned the expected tools, for example for the jobs bundle:

```text
ahmed-dot-fouaad82--greenhouse-public-jobs
ahmed-dot-fouaad82--lever-salary-jobs
ahmed-dot-fouaad82--ats-public-jobs
get-actor-run, get-dataset-items, get-key-value-store-record, abort-actor-run
```

The jobs bundle's `claude_desktop_config.json` was also run as-is through `npx mcp-remote@latest` (stdio bridge, Node 22): `initialize` and `tools/list` returned the same 7 tools.

A real tool call (`ahmed-dot-fouaad82--rss-feed-reader`, 3 items from the Hacker News RSS feed) returned `SUCCEEDED` with 3 dataset rows and 0 charged results (free slice). Re-run the check yourself with [`scripts/check_preset.py`](scripts/check_preset.py).

Notes from that test:
- Endpoints that preload an Actor **require authentication** (OAuth or token); without it the server answers HTTP 401. Only discovery tools (`search-actors`, `fetch-actor-details`, docs) work anonymously.
- OAuth sign-in was not exercised by the script (it used a token header); OAuth is the method Apify documents as recommended.

## Security
- Never commit your Apify token. The token variants read it from an environment variable or a secure prompt.
- The Actors only read public pages (no logins, no private data). Each Store page documents its sources and robots/ToS limits.

## Licence
MIT for the configs and script in this repo. The Actors are separate paid products on Apify Store.
