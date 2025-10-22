# scripts/enrich_dataset.py
# ------------------------------------------------------------
# This script extracts URLs from an email dataset (CSV format)
# and prepares them for external analysis (urlscan, VirusTotal)
# ------------------------------------------------------------

import pandas as pd
import re
import os

# Input and output paths
DATA_PATH = "C:/Users/mnudd/Downloads/Phishing/samples/sampledataset.csv"      # your dataset name
OUTPUT_PATH = "outputs/extracted_urls.csv"

# URL pattern
url_re = re.compile(r'https?://[^\s\'"<>]+', re.IGNORECASE)

def extract_urls(text):
    """Find all URLs in the given text."""
    if not isinstance(text, str):
        return []
    return url_re.findall(text)

def main():
    print("📂 Loading dataset...")
    df = pd.read_csv(DATA_PATH, encoding="utf-8", dtype=str)
    print(f"✅ Loaded {len(df)} rows")

    # Make sure a 'body' column exists
    if 'body' not in df.columns:
        raise KeyError("Column 'body' not found in your dataset — check your CSV headers.")

    # Extract URLs from the 'body' column
    df["extracted_urls"] = df["body"].apply(extract_urls)

    # Flatten all URLs into one simple list
    all_urls = []
    for idx, urls in enumerate(df["extracted_urls"]):
        for u in urls:
            all_urls.append({"row": idx, "url": u})

    out_df = pd.DataFrame(all_urls)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    out_df.to_csv(OUTPUT_PATH, index=False)

    print(f"🔍 Found {len(out_df)} URLs total")
    print(f"💾 Saved to {OUTPUT_PATH}")
    print("\nNext: analyze these URLs safely on urlscan.io or VirusTotal.")

if __name__ == "__main__":
    main()
