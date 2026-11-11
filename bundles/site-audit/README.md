# Bundle: Site audit (sitemap URLs, link/status checks, dedup)

> **Disclosure:** I (GitHub @AHMEDFOUAAD, Apify user `ahmed.fouaad82`) built and sell these Actors on Apify Store. They are **paid per result** (pay-per-event). The first results of every run are free (25 for most of these Actors; see each Store page's Pricing tab), then the listed price applies. You need **your own Apify account** (OAuth sign-in or your own API token); runs bill to your account, and Apify's free plan includes $5/month of usage. This repo only contains client configs: it is not affiliated with or endorsed by Apify.

**Who it is for:** SEO/site-migration checks, docs-site link audits, crawl-list preparation.

**MCP endpoint (Apify hosted server, preselected Actors):**

```text
https://mcp.apify.com/?tools=ahmed.fouaad82/sitemap-extractor,ahmed.fouaad82/url-status-checker,ahmed.fouaad82/dataset-dedup-merge
```

| Actor (Store page) | MCP tool name | What it returns | Price after the free first results* |
|---|---|---|---|
| [Sitemap Extractor - XML & Gzip](https://apify.com/ahmed.fouaad82/sitemap-extractor) | `ahmed-dot-fouaad82--sitemap-extractor` | All URLs from sitemap indexes and gzip sitemaps, with include/exclude regex and lastmod filters. | $0.50 per 1,000 URLs |
| [Broken Link Checker & Bulk URL Status Checker](https://apify.com/ahmed.fouaad82/url-status-checker) | `ahmed-dot-fouaad82--url-status-checker` | HTTP status, redirects and broken links for a URL list or a page's links (shallow crawl). | $2.00 per 1,000 checks |
| [Dataset Deduplication & Merge](https://apify.com/ahmed.fouaad82/dataset-dedup-merge) | `ahmed-dot-fouaad82--dataset-dedup-merge` | Merge Apify datasets/runs and drop duplicates by key fields. | $0.02 per 1,000 rows |

\* Prices read from the public Apify Store API on 2026-11-11; the Store page Pricing tab is authoritative.

The server also adds `get-actor-run`, `get-dataset-items`, `get-key-value-store-record` and `abort-actor-run`, so the agent can read results and stop runs.

## Install

### Claude Desktop / Claude.ai (recommended: connector with OAuth)
Settings → Connectors → **Add custom connector** → name `apify-site-audit`, URL = the endpoint above → sign in to Apify when asked.

No connector support? Use the stdio bridge in [`claude_desktop_config.json`](claude_desktop_config.json) (needs Node.js; replace `YOUR_APIFY_TOKEN` locally, never commit it).

### Cursor
Copy [`cursor.mcp.json`](cursor.mcp.json) into `~/.cursor/mcp.json` (global) or `.cursor/mcp.json` (project). Cursor opens the Apify OAuth sign-in on first use.
Token instead of OAuth: [`cursor.mcp.token.json`](cursor.mcp.token.json) reads `APIFY_TOKEN` from your environment.

### VS Code (GitHub Copilot agent mode)
Copy [`vscode.mcp.json`](vscode.mcp.json) into `.vscode/mcp.json`. Token instead of OAuth: [`vscode.mcp.token.json`](vscode.mcp.token.json) prompts for the token and stores it securely.

### Claude Code
```bash
claude mcp add apify-site-audit "https://mcp.apify.com/?tools=ahmed.fouaad82/sitemap-extractor,ahmed.fouaad82/url-status-checker,ahmed.fouaad82/dataset-dedup-merge" -t http
```

## Try it
- Extract up to 50 URLs containing /blog/ from https://<your-site>/sitemap.xml.
- Check these URLs and report any that are not HTTP 200: <url1>, <url2>, <url3>.
- Find broken links on https://example.com (crawl depth 0, max 25 results).

## Keep cost under control
- Ask for small `maxResults` first; the first results of each run are free.
- Set a monthly usage limit in Apify Console → Billing → Limits.
- Each paid result is charged once; failed runs are not charged per result.
