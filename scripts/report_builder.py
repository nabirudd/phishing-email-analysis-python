# scripts/report_builder.py
# ------------------------------------------------------------
# Builds a polished Excel (findings.xlsx) from final_report.csv
# Adds simple technique classification + prevention tips.
# ------------------------------------------------------------

import pandas as pd
import os

FINAL_REPORT = "outputs/final_report.csv"
DOMAINS = "outputs/domains.csv"
OUT_XLSX = "outputs/findings.xlsx"

def classify_technique(row):
    url = str(row.get("url", "")).lower()
    title = str(row.get("page_title", "")).lower()
    vt_mal = int(row.get("malicious", 0) or 0)
    us_mal = str(row.get("urlscan_malicious", "")).lower() in ("true", "1", "yes")

    tech = []

    if any(k in title for k in ["login", "sign in", "verify", "password"]) or any(k in url for k in ["/login", "signin", "verify", "account"]):
        tech.append("Credential-harvest (fake login)")

    if any(k in title for k in ["urgent", "action required", "verify your account", "suspended", "final notice"]):
        tech.append("Urgency / scare tactic")

    if any(k in url for k in ["bit.ly", "tinyurl", "t.co", "goo.gl", "ow.ly"]):
        tech.append("URL shortener / redirect")

    if (vt_mal > 0 or us_mal) and not tech:
        tech.append("Suspicious / flagged by engines")

    if not tech:
        tech.append("Likely benign / informational")

    return "; ".join(sorted(set(tech)))

def prevention_tip(technique):
    t = technique.lower()
    if "credential-harvest" in t:
        return "Verify sender domains; use MFA; block phishing domains; inspect links via urlscan."
    if "urgency" in t:
        return "Train users to distrust urgent requests; add banners for external emails."
    if "shortener" in t:
        return "Expand shortened URLs safely in a sandbox; restrict public shortener use."
    if "flagged by engines" in t:
        return "Block via proxy/firewall; update threat feeds; educate users."
    return "No action needed; monitor and train users."

def main():
    # Load data
    if not os.path.exists(FINAL_REPORT):
        raise SystemExit(f"❌ Missing {FINAL_REPORT}. Run combine_all.py first.")

    df = pd.read_csv(FINAL_REPORT, dtype=str)

    # Convert numeric columns safely
    for c in ["malicious", "suspicious", "harmless", "undetected"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0).astype(int)

    # Add technique + prevention
    df["Technique"] = df.apply(classify_technique, axis=1)
    df["Prevention Tip"] = df["Technique"].apply(prevention_tip)

    # Copy for selection
    showcase = df.copy()

    # Flag malicious or suspicious
    if "urlscan_malicious" in showcase.columns:
        showcase["is_bad"] = (
            (showcase["malicious"] > 0)
            | (showcase["urlscan_malicious"].astype(str).str.lower().isin(["true", "1", "yes"]))
        )
    else:
        showcase["is_bad"] = showcase["malicious"] > 0

    showcase = showcase.sort_values(["is_bad", "malicious"], ascending=[False, False])

    # If fewer than 5 bad samples, add rare domains
    if os.path.exists(DOMAINS) and showcase["is_bad"].sum() < 5:
        dom = pd.read_csv(DOMAINS, dtype=str)
        dom["count"] = pd.to_numeric(dom["count"], errors="coerce").fillna(0).astype(int)
        rare = dom.sort_values("count").head(10)["domain"].tolist()
        extra = df[df["domain"].isin(rare)]
        showcase = pd.concat([showcase, extra]).drop_duplicates(subset=["url"])

    # Select top 15
    top = showcase.head(15)

    # Reorder columns neatly
    cols = [
        "url", "domain",
        "malicious", "suspicious", "harmless", "undetected",
        "permalink", "urlscan_permalink", "screenshot", "page_title", "final_url",
        "Technique", "Prevention Tip"
    ]
    top = top[[c for c in cols if c in top.columns]]

    # Save to Excel
    os.makedirs(os.path.dirname(OUT_XLSX), exist_ok=True)
    top.to_excel(OUT_XLSX, index=False)
    print(f"✅ Wrote polished findings to {OUT_XLSX}")
    print("Open that file and pick the 5–10 best examples for your final submission.")

if __name__ == "__main__":
    main()
