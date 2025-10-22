# scripts/combine_all.py
# ------------------------------------------------------------
# Combines VirusTotal + urlscan.io results into a single file
# Handles missing columns gracefully.
# ------------------------------------------------------------

import pandas as pd
import os

# Input files
VT_RESULTS = "outputs/url_reputation.csv"
URLSCAN_RESULTS = "outputs/urlscan_results.csv"
CLEANED = "outputs/cleaned_urls.csv"

# Output file
FINAL_OUTPUT = "outputs/final_report.csv"

def main():
    print("📂 Loading data...")

    # Load CSVs
    vt_df = pd.read_csv(VT_RESULTS, dtype=str)
    urlscan_df = pd.read_csv(URLSCAN_RESULTS, dtype=str)
    cleaned_df = pd.read_csv(CLEANED, dtype=str)

    print(f"✅ VirusTotal results: {len(vt_df)} rows")
    print(f"✅ urlscan.io results: {len(urlscan_df)} rows")

    # Merge cleaned URLs with VirusTotal
    merged = cleaned_df.merge(vt_df, left_on="url_norm", right_on="url", how="left", suffixes=("", "_vt"))
    # Merge again with urlscan (some URLs might not have results)
    merged = merged.merge(urlscan_df, on="url", how="left", suffixes=("", "_us"))

    # Ensure all expected columns exist
    for col in [
        "urlscan_permalink", "screenshot", "page_title",
        "final_url", "malicious_us"
    ]:
        if col not in merged.columns:
            merged[col] = ""

    # Select & reorder
    cols = [
        "url", "domain",
        "malicious", "suspicious", "harmless", "undetected", "permalink",
        "urlscan_permalink", "screenshot", "page_title", "final_url", "malicious_us"
    ]
    merged = merged[[c for c in cols if c in merged.columns]]

    # Save final report
    os.makedirs(os.path.dirname(FINAL_OUTPUT), exist_ok=True)
    merged.to_csv(FINAL_OUTPUT, index=False)
    print(f"💾 Saved final combined report to {FINAL_OUTPUT}")
    print("✅ Combined report ready!")

if __name__ == "__main__":
    main()
