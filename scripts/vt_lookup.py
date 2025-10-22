# scripts/vt_lookup.py
# ------------------------------------------------------------
# Uses VirusTotal API v3 to check the reputation of URLs
# and saves results (malicious/suspicious/harmless) in CSV form
# ------------------------------------------------------------

import os
import time
import base64
import requests
import pandas as pd
from pathlib import Path

# Input and output files
CLEANED_FILE = "outputs/cleaned_urls.csv"
OUTPUT_FILE = "outputs/url_reputation.csv"
CACHE_DIR = "outputs/vt_cache"

# Get your API key from environment variable
VT_API_KEY = os.getenv("VT_API_KEY")
SLEEP_TIME = 15  # seconds between requests (free API limit)

def vt_url_id(url):
    """Create VirusTotal URL-safe base64 ID."""
    return base64.urlsafe_b64encode(url.encode()).decode().strip("=")

def vt_lookup(url):
    """Query VirusTotal API for a given URL."""
    url_id = vt_url_id(url)
    endpoint = f"https://www.virustotal.com/api/v3/urls/{url_id}"
    headers = {"x-apikey": VT_API_KEY}
    response = requests.get(endpoint, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"HTTP {response.status_code}"}

def main():
    if not VT_API_KEY:
        raise SystemExit("❌ Error: No VirusTotal API key found. Set it before running.")

    Path(CACHE_DIR).mkdir(parents=True, exist_ok=True)

    # Load cleaned URLs
    df = pd.read_csv(CLEANED_FILE, dtype=str)
    print(f"📂 Loaded {len(df)} cleaned URLs")

    results = []

    # Limit for demo (you can remove this limit later)
    df = df.head(10)  # check only first 10 URLs for now

    for _, row in df.iterrows():
        url = row["url_norm"]
        cache_path = Path(CACHE_DIR) / f"{vt_url_id(url)}.json"

        # Use cached result if exists
        if cache_path.exists():
            data = cache_path.read_text(encoding="utf-8")
            jdata = eval(data)
        else:
            print(f"🔍 Checking: {url}")
            jdata = vt_lookup(url)
            cache_path.write_text(str(jdata), encoding="utf-8")
            time.sleep(SLEEP_TIME)

        if "data" in jdata:
            attrs = jdata["data"]["attributes"]
            stats = attrs.get("last_analysis_stats", {})
            results.append({
                "url": url,
                "malicious": stats.get("malicious", 0),
                "suspicious": stats.get("suspicious", 0),
                "harmless": stats.get("harmless", 0),
                "undetected": stats.get("undetected", 0),
                "permalink": f"https://www.virustotal.com/gui/url/{vt_url_id(url)}"
            })
        else:
            results.append({"url": url, "error": jdata.get("error", "No data")})

    out_df = pd.DataFrame(results)
    out_df.to_csv(OUTPUT_FILE, index=False)
    print(f"💾 Saved results to {OUTPUT_FILE}")
    print("✅ Done! You can safely open the CSV to review reputations.")

if __name__ == "__main__":
    main()
