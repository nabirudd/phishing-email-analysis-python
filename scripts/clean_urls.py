# scripts/clean_urls.py
# ------------------------------------------------------------
# Cleans and deduplicates extracted URLs from your dataset.
# Removes invalid, duplicate, and non-web URLs.
# Saves clean list and domain counts for prioritization.
# ------------------------------------------------------------

import pandas as pd
import re
import os
from urllib.parse import urlsplit, urlunsplit
import tldextract

# Input and output paths
SRC = "outputs/extracted_urls.csv"
OUT_CLEAN = "outputs/cleaned_urls.csv"
OUT_DOMAINS = "outputs/domains.csv"

# Regex to strip unwanted punctuation
punct_strip_re = re.compile(r'^[\[\("\'<>]+|[\]\)"\'\.,;:!?\-]+$')

def normalize_url(url):
    if not isinstance(url, str) or not url.strip():
        return None
    url = url.strip()
    # Ignore mailto, javascript, etc.
    if url.lower().startswith(("mailto:", "javascript:", "data:")):
        return None
    # Remove leading/trailing punctuation
    url = punct_strip_re.sub("", url)
    try:
        parts = urlsplit(url)
    except Exception:
        return None
    # If scheme missing, add http
    if parts.scheme == "" and url.startswith("//"):
        url = "http:" + url
        parts = urlsplit(url)
    if parts.scheme not in ("http", "https"):
        return None
    # Rebuild without fragment
    url = urlunsplit((parts.scheme, parts.netloc, parts.path or "/", parts.query, ""))
    return url

def domain_from_url(url):
    if not url:
        return None
    t = tldextract.extract(url)
    if not t.suffix:
        return None
    return f"{t.domain}.{t.suffix}"

def main():
    print("📂 Loading extracted URLs...")
    if not os.path.exists(SRC):
        raise FileNotFoundError(f"Cannot find file: {SRC}")
    df = pd.read_csv(SRC, dtype=str)
    print(f"✅ Loaded {len(df)} URLs")

    print("🧹 Cleaning and normalizing URLs...")
    df["url_norm"] = df["url"].apply(normalize_url)
    df = df[df["url_norm"].notnull()].copy()
    df["domain"] = df["url_norm"].apply(domain_from_url)

    before = len(df)
    df = df.drop_duplicates(subset=["url_norm"])
    after = len(df)
    print(f"🗑️ Removed {before - after} duplicates; {after} unique URLs remain.")

    os.makedirs(os.path.dirname(OUT_CLEAN), exist_ok=True)
    df[["row", "url", "url_norm", "domain"]].to_csv(OUT_CLEAN, index=False)
    print(f"💾 Saved cleaned URLs to {OUT_CLEAN}")

    domain_counts = df["domain"].value_counts().reset_index()
    domain_counts.columns = ["domain", "count"]
    domain_counts.to_csv(OUT_DOMAINS, index=False)
    print(f"💾 Saved domain list to {OUT_DOMAINS}")
    print("✅ Cleaning complete.")

if __name__ == "__main__":
    main()
