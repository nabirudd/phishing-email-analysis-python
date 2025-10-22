# scripts/combine_results.py
# ------------------------------------------------------------
# Combines cleaned URL data with VirusTotal reputation results
# to create a full findings table for reporting.
# ------------------------------------------------------------

import pandas as pd

CLEANED = "outputs/cleaned_urls.csv"
VT_RESULTS = "outputs/url_reputation.csv"
OUTPUT = "outputs/final_findings.csv"

def main():
    print("📂 Loading cleaned URLs and VirusTotal results...")
    urls_df = pd.read_csv(CLEANED, dtype=str)
    vt_df = pd.read_csv(VT_RESULTS, dtype=str)

    print(f"✅ Loaded {len(urls_df)} cleaned URLs, {len(vt_df)} VirusTotal records")

    # Merge on normalized URL
    merged = urls_df.merge(vt_df, left_on="url_norm", right_on="url", how="left")

    # Select relevant columns for clarity
    merged = merged[[
        "row", "url_norm", "domain",
        "malicious", "suspicious", "harmless", "undetected", "permalink"
    ]]

    merged.to_csv(OUTPUT, index=False)
    print(f"💾 Saved combined results to {OUTPUT}")
    print("✅ You can now open it in Excel for final analysis and reporting.")

if __name__ == "__main__":
    main()
