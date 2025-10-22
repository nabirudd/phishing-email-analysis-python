# scripts/urlscan_lookup.py
# ------------------------------------------------------------
# Automatically submit URLs to urlscan.io for sandbox analysis
# and collect summary results (verdicts, redirects, screenshots)
# ------------------------------------------------------------

import os
import time
import requests
import pandas as pd
from pathlib import Path

INPUT_FILE = "outputs/final_findings.csv"      # cleaned + VT merged
OUTPUT_FILE = "outputs/urlscan_results.csv"
CACHE_DIR = "outputs/urlscan_cache"
SLEEP_TIME = 20   # seconds between scans (free tier limit)

URLSCAN_API_KEY = os.getenv("URLSCAN_API_KEY")

def submit_to_urlscan(url):
    """Submit a URL to urlscan.io for scanning."""
    headers = {"API-Key": URLSCAN_API_KEY, "Content-Type": "application/json"}
    payload = {"url": url, "visibility": "public"}
    resp = requests.post("https://urlscan.io/api/v1/scan/", json=payload, headers=headers)
    if resp.status_code == 200:
        data = resp.json()
        return data.get("api", None)  # api result endpoint
    else:
        print(f"⚠️  Failed to submit {url} - {resp.status_code}")
        return None

def fetch_scan_result(api_url):
    """Fetch the finished scan result."""
    if not api_url:
        return None
    for _ in range(15):  # check for up to ~3 minutes
        r = requests.get(api_url)
        if r.status_code == 200:
            j = r.json()
            if j.get("page"):
                return j
        time.sleep(10)
    return None

def main():
    if not URLSCAN_API_KEY:
        raise SystemExit("❌ No URLSCAN_API_KEY set. Run `$env:URLSCAN_API_KEY='your_key'` first.")

    Path(CACHE_DIR).mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(INPUT_FILE, dtype=str)
    print(f"📂 Loaded {len(df)} URLs from {INPUT_FILE}")

    # For safety, start with only 5 URLs (you can increase later)
    df = df.head(5)

    results = []
    for _, row in df.iterrows():
        url = row["url_norm"]
        cache_file = Path(CACHE_DIR) / f"{hash(url)}.json"

        if cache_file.exists():
            data = eval(cache_file.read_text(encoding="utf-8"))
        else:
            print(f"🚀 Submitting: {url}")
            api_url = submit_to_urlscan(url)
            if not api_url:
                continue
            time.sleep(SLEEP_TIME)
            data = fetch_scan_result(api_url)
            if data:
                cache_file.write_text(str(data), encoding="utf-8")
 
        if data and "page" in data:
            page = data["page"]
            task = data.get("task", {})
            results.append({
                "url": url,
                "page_title": page.get("title"),
                "domain": page.get("domain"),
                "country": page.get("country"),
                "asnname": page.get("asnname"),
                "verdict": page.get("verdict"),
                "final_url": task.get("url"),
                "screenshot": data.get("screenshotURL"),
                "task_link": data.get("task", {}).get("reportURL")
            })

    pd.DataFrame(results).to_csv(OUTPUT_FILE, index=False)
    print(f"💾 Saved urlscan results to {OUTPUT_FILE}")
    print("✅ Done! You can now open screenshots and verdicts in your browser.")

if __name__ == "__main__":
    main()
