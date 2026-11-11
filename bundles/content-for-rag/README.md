# Bundle: Content for RAG (RSS, podcast transcripts, PDF text)

> **Disclosure:** I (GitHub @AHMEDFOUAAD, Apify user `ahmed.fouaad82`) built and sell these Actors on Apify Store. They are **paid per result** (pay-per-event). The first results of every run are free (25 for most of these Actors; see each Store page's Pricing tab), then the listed price applies. You need **your own Apify account** (OAuth sign-in or your own API token); runs bill to your account, and Apify's free plan includes $5/month of usage. This repo only contains client configs: it is not affiliated with or endorsed by Apify.

**Who it is for:** RAG pipelines, research assistants, newsletter/monitoring agents.

**MCP endpoint (Apify hosted server, preselected Actors):**

```text
https://mcp.apify.com/?tools=ahmed.fouaad82/rss-feed-reader,ahmed.fouaad82/podcast-published-transcripts,ahmed.fouaad82/public-pdf-text
```

| Actor (Store page) | MCP tool name | What it returns | Price after the free first results* |
|---|---|---|---|
| [RSS Feed Reader - RSS and Atom to JSON](https://apify.com/ahmed.fouaad82/rss-feed-reader) | `ahmed-dot-fouaad82--rss-feed-reader` | RSS/Atom items as clean JSON (title, url, dates, summary), with keyword and since filters. | $1.00 per 1,000 items |
| [Podcast Transcript Scraper - Published RSS Transcripts](https://apify.com/ahmed.fouaad82/podcast-published-transcripts) | `ahmed-dot-fouaad82--podcast-published-transcripts` | Transcripts that podcasts already publish in their RSS feed (podcast:transcript), as text/segments. No speech-to-text. | $2.00 per 1,000 transcripts |
| [PDF to Text Extractor - Public PDF URLs](https://apify.com/ahmed.fouaad82/public-pdf-text) | `ahmed-dot-fouaad82--public-pdf-text` | Page-by-page text from public PDF URLs, ready for chunking. | $20.00 per 1,000 pages |

\* Prices read from the public Apify Store API on 2026-11-11; the Store page Pricing tab is authoritative.

The server also adds `get-actor-run`, `get-dataset-items`, `get-key-value-store-record` and `abort-actor-run`, so the agent can read results and stop runs.

## Install

### Claude Desktop / Claude.ai (recommended: connector with OAuth)
Settings → Connectors → **Add custom connector** → name `apify-rag-content`, URL = the endpoint above → sign in to Apify when asked.

No connector support? Use the stdio bridge in [`claude_desktop_config.json`](claude_desktop_config.json) (needs Node.js; replace `YOUR_APIFY_TOKEN` locally, never commit it).

### Cursor
Copy [`cursor.mcp.json`](cursor.mcp.json) into `~/.cursor/mcp.json` (global) or `.cursor/mcp.json` (project). Cursor opens the Apify OAuth sign-in on first use.
Token instead of OAuth: [`cursor.mcp.token.json`](cursor.mcp.token.json) reads `APIFY_TOKEN` from your environment.

### VS Code (GitHub Copilot agent mode)
Copy [`vscode.mcp.json`](vscode.mcp.json) into `.vscode/mcp.json`. Token instead of OAuth: [`vscode.mcp.token.json`](vscode.mcp.token.json) prompts for the token and stores it securely.

### Claude Code
```bash
claude mcp add apify-rag-content "https://mcp.apify.com/?tools=ahmed.fouaad82/rss-feed-reader,ahmed.fouaad82/podcast-published-transcripts,ahmed.fouaad82/public-pdf-text" -t http
```

## Try it
- Read the 5 newest items from https://hnrss.org/frontpage and summarize them.
- Get the published transcript of the latest episode of this podcast feed: <RSS feed URL>. Max 1 episode.
- Extract the text of pages 1-3 of <public PDF URL> and give me a 5-bullet summary.

## Keep cost under control
- Ask for small `maxResults` first; the first results of each run are free.
- Set a monthly usage limit in Apify Console → Billing → Limits.
- Each paid result is charged once; failed runs are not charged per result.
