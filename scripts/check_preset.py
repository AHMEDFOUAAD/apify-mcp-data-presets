"""List the tools an Apify MCP preset exposes.

Usage: APIFY_TOKEN=... python check_preset.py "https://mcp.apify.com/?tools=ahmed.fouaad82/rss-feed-reader"
The token is read from the environment and never printed.
"""
import json, os, sys, urllib.request


def post(url, body, sid=None):
    h = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}
    tok = os.environ.get("APIFY_TOKEN")
    if tok:
        h["Authorization"] = "Bearer " + tok
    if sid:
        h["Mcp-Session-Id"] = sid
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers=h, method="POST")
    with urllib.request.urlopen(req, timeout=60) as r:
        sid = r.headers.get("Mcp-Session-Id") or sid
        text = r.read().decode("utf-8")
        if "text/event-stream" in (r.headers.get("Content-Type") or ""):
            data = [l[5:].strip() for l in text.split("\n") if l.startswith("data:")]
            text = data[-1] if data else ""
        return sid, (json.loads(text) if text.strip() else None)


def main(url):
    sid, _ = post(url, {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {
        "protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "check-preset", "version": "1.0"}}})
    post(url, {"jsonrpc": "2.0", "method": "notifications/initialized"}, sid)
    _, res = post(url, {"jsonrpc": "2.0", "id": 2, "method": "tools/list"}, sid)
    for t in res["result"]["tools"]:
        print(t["name"])


if __name__ == "__main__":
    main(sys.argv[1])
