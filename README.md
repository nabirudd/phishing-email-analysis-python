<!-- HEADER WITH TOOL LOGOS (GitHub-safe version) -->
<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python" width="60" height="60"/>
  &nbsp;&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/virustotal.svg" alt="VirusTotal" width="60" height="60"/>
  &nbsp;&nbsp;
  <img src="https://cdn.worldvectorlogo.com/logos/urlscanio.svg" alt="urlscan.io" width="60" height="60"/>
  &nbsp;&nbsp;
  <img src="https://cdn.worldvectorlogo.com/logos/pandas.svg" alt="Pandas" width="60" height="60"/>
  &nbsp;&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" alt="VS Code" width="60" height="60"/>
  &nbsp;&nbsp;
  <img src="https://cdn-icons-png.flaticon.com/512/906/906324.png" alt="ReportLab" width="60" height="60"/>
</p>

<h1 align="left">📧 Phishing Email Analysis using Python, VirusTotal & urlscan.io</h1>

<p align="left">
  <em>A practical cybersecurity project demonstrating phishing detection, URL intelligence enrichment, and reporting automation — using free and trusted tools.</em>
</p>

---

## 🚀 **Project Overview**

This project simulates a **Security Operations Center (SOC)** workflow for analyzing phishing emails safely using **Python automation** and **cybersecurity intelligence APIs**.

It extracts URLs from phishing email samples, enriches them using **VirusTotal** and **urlscan.io**, classifies attack techniques, and produces a polished PDF report with findings and prevention tips.

---

## 🧰 **Tools & Libraries Used**

| Tool / Library | Purpose |
|----------------|----------|
| 🐍 **Python** | Core programming language |
| 🧹 **pandas** | Data analysis and cleaning |
| 🌐 **requests** | API integration for VirusTotal & urlscan.io |
| 🔍 **VirusTotal API** | URL reputation and malware checks |
| 🧪 **urlscan.io API** | Sandbox and page behavior analysis |
| 🧠 **tldextract** | Domain parsing and normalization |
| 📊 **openpyxl** | Excel report formatting |
| 🧾 **reportlab** | Automated PDF generation |
| 🧰 **VS Code** | Development environment |

---

## 🧩 **Project Architecture**

```

Phishing-Analysis/
│
├── scripts/
│   ├── enrich_dataset.py       # Extract URLs from dataset
│   ├── clean_urls.py           # Clean & normalize URLs
│   ├── vt_lookup.py            # VirusTotal analysis
│   ├── urlscan_lookup.py       # urlscan.io sandbox lookup
│   ├── combine_all.py          # Merge findings
│   ├── report_builder.py       # Classify techniques + add tips
│   ├── format_excel.py         # Beautify Excel report
│   └── export_pdf_report.py    # Generate final PDF
│
├── outputs/
│   ├── extracted_urls.csv
│   ├── cleaned_urls.csv
│   ├── domains.csv
│   ├── url_reputation.csv
│   ├── urlscan_results.csv
│   ├── final_report.csv
│   ├── findings.xlsx
│   ├── findings_formatted.xlsx
│   └── phishing_analysis_report.pdf
│
├── sampledataset.csv           # Email dataset (from Kaggle)
└── README.md

````

---

## 🔬 **Workflow Summary**

1. **Extract URLs** from emails → `enrich_dataset.py`  
2. **Clean and deduplicate** URLs → `clean_urls.py`  
3. **Check reputation** on VirusTotal → `vt_lookup.py`  
4. **Scan suspicious URLs** in sandbox → `urlscan_lookup.py`  
5. **Combine all results** → `combine_all.py`  
6. **Classify phishing techniques** & add prevention advice → `report_builder.py`  
7. **Generate formatted Excel & PDF reports** → `format_excel.py` + `export_pdf_report.py`

---

## 📈 **Key Features**

✅ Safe static phishing analysis (no live execution)  
✅ Automates VirusTotal & urlscan.io queries  
✅ Generates clean CSV, Excel, and PDF reports  
✅ Detects social engineering patterns  
✅ Provides actionable prevention tips  
✅ Uses 100% free, industry-trusted tools  
✅ Ideal for **SOC analyst** and **cybersecurity portfolio** projects  

---

## 🧠 **What I Learned**

- How to safely analyze phishing samples and extract URLs  
- How to use VirusTotal and urlscan.io APIs for reputation and sandboxing  
- How to clean large datasets and extract IOCs using pandas  
- How to generate analyst-level reports with automation  
- How to recognize **social engineering patterns** in phishing  
- How to communicate technical findings clearly and visually  

---

## 📄 **Example Outputs**

### 🧾 Excel Report (`findings_formatted.xlsx`)
| URL | Domain | Malicious | Technique | Prevention Tip |
|------|----------|------------|-------------|----------------|
| brightmade.com | brightmade.com | 9 | Credential Harvest | Verify sender, block domain |
| cnn.com | cnn.com | 0 | Benign | No action needed |

### 📊 PDF Report (`phishing_analysis_report.pdf`)
Includes:
- Title page with date and author  
- Top phishing URL table  
- Summary of findings   

---

## 🛡️ **Common Techniques Identified**

- 🎣 **Credential Harvesting** (fake login pages)  
- ⚠️ **Urgency/Threat** (“Verify Account Immediately”)  
- 🔗 **URL Shorteners** (bit.ly, t.co)  
- 🔁 **Redirect Chains** (obfuscation)

---

## 🧾 **Prevention Recommendations**

| Category | Mitigation |
|-----------|-------------|
| **Technical** | Implement SPF/DKIM/DMARC; block known malicious domains |
| **Human** | Train employees to identify fake urgency and suspicious links |
| **Process** | Enforce MFA, perform sandbox scans (urlscan.io), use PhishTool for triage |

---

---

## 📚 **Dataset Source**

🗂️ Kaggle — *Phishing Email Dataset (Safe & Sanitized)*  
🔗 [https://www.kaggle.com/](https://www.kaggle.com/)  

*(Used only for metadata extraction — no live phishing execution.)*

---

## 🏁 **How to Run the Project**

```bash
# 1. Clone this repository
git clone https://github.com/<your-username>/phishing-analysis.git
cd phishing-analysis

# 2. Create virtual environment
python -m venv .venv
.venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the scripts in order
python scripts/enrich_dataset.py
python scripts/clean_urls.py
python scripts/vt_lookup.py
python scripts/urlscan_lookup.py
python scripts/combine_all.py
python scripts/report_builder.py
python scripts/format_excel.py
python scripts/export_pdf_report.py
````

## 📸 **Project Screenshots**

> Below are key stages of the **Phishing Email Analysis Workflow** — from data extraction and enrichment to final reporting.  
> Each screenshot is neatly displayed with a title and description for better readability.

---

## 🧠 **Python Script Execution**

### ⚙️ **1. enrich_dataset.py — Extract URLs from Phishing Emails**
<p align="center">
  <img src="https://github.com/nabirudd/phishing-email-analysis-python/blob/main/screenshots/enrich_dataset.png?raw=true" alt="enrich_dataset script output" width="750" style="border:2px solid #555; border-radius:10px; padding:5px;">
</p>
<p align="center"><em>Extracts all URLs from the email dataset for further analysis.</em></p>

---

### 🧹 **2. clean_urls.py — Clean & Normalize URLs**
<p align="center">
  <img src="https://github.com/nabirudd/phishing-email-analysis-python/blob/main/screenshots/clean_urls.png?raw=true" alt="clean_urls script output" width="750" style="border:2px solid #555; border-radius:10px; padding:5px;">
</p>
<p align="center"><em>Removes duplicates and invalid URLs, producing a clean dataset.</em></p>

---

### 🔍 **3. vt_lookup.py — VirusTotal Reputation Analysis**
<p align="center">
  <img src="https://github.com/nabirudd/phishing-email-analysis-python/blob/main/screenshots/Virus%20Total%20Lookup.png?raw=true" alt="VirusTotal lookup" width="750" style="border:2px solid #555; border-radius:10px; padding:5px;">
</p>
<p align="center"><em>Checks each URL’s reputation via the VirusTotal API.</em></p>

---

### 🧪 **4. urlscan_lookup.py — Sandbox URL Analysis**
<p align="center">
  <img src="https://github.com/nabirudd/phishing-email-analysis-python/blob/main/screenshots/urlscan_lookup.png?raw=true" alt="urlscan lookup" width="750" style="border:2px solid #555; border-radius:10px; padding:5px;">
</p>
<p align="center"><em>Submits suspicious URLs to urlscan.io for sandbox scanning.</em></p>

---

### 🔗 **5. combine_all.py — Merge Intelligence Results**
<p align="center">
  <img src="https://github.com/nabirudd/phishing-email-analysis-python/blob/main/screenshots/combine_all.png?raw=true" alt="combine_all script output" width="750" style="border:2px solid #555; border-radius:10px; padding:5px;">
</p>
<p align="center"><em>Combines VirusTotal and urlscan.io data into a unified intelligence table.</em></p>

---

### 🧠 **6. report_builder.py — Classify Techniques & Add Tips**
<p align="center">
  <img src="https://github.com/nabirudd/phishing-email-analysis-python/blob/main/screenshots/report_builder.png?raw=true" alt="report_builder script output" width="750" style="border:2px solid #555; border-radius:10px; padding:5px;">
</p>
<p align="center"><em>Classifies phishing techniques and generates prevention advice.</em></p>

---

### 📊 **7. format_excel.py — Beautify Excel Report**
<p align="center">
  <img src="https://github.com/nabirudd/phishing-email-analysis-python/blob/main/screenshots/format_excel.png?raw=true" alt="format_excel script output" width="750" style="border:2px solid #555; border-radius:10px; padding:5px;">
</p>
<p align="center"><em>Formats the Excel output for a professional report appearance.</em></p>

---

### 🧾 **8. export_pdf_report.py — Generate Final PDF Report**
<p align="center">
  <img src="https://github.com/nabirudd/phishing-email-analysis-python/blob/main/screenshots/export_pdf_report.png?raw=true" alt="export_pdf_report script output" width="750" style="border:2px solid #555; border-radius:10px; padding:5px;">
</p>
<p align="center"><em>Creates a SOC-style phishing intelligence report in PDF format.</em></p>

---

## 📂 **Output Results**

### 🧹 **1. Cleaned URLs**
<p align="center">
  <img src="https://github.com/nabirudd/phishing-email-analysis-python/blob/main/screenshots/Output_cleaned_urls.png?raw=true" alt="cleaned_urls output" width="750" style="border:2px solid #555; border-radius:10px; padding:5px;">
</p>
<p align="center"><em>Final cleaned list of URLs ready for reputation analysis.</em></p>

---

### 🌐 **2. Domains List**
<p align="center">
  <img src="https://github.com/nabirudd/phishing-email-analysis-python/blob/main/screenshots/Output_domains.png?raw=true" alt="domains output" width="750" style="border:2px solid #555; border-radius:10px; padding:5px;">
</p>
<p align="center"><em>Top domains extracted from phishing URLs, showing frequency and volume.</em></p>

---

### 🔎 **3. Extracted URLs**
<p align="center">
  <img src="https://github.com/nabirudd/phishing-email-analysis-python/blob/main/screenshots/output_extracted_urls.png?raw=true" alt="extracted_urls output" width="750" style="border:2px solid #555; border-radius:10px; padding:5px;">
</p>
<p align="center"><em>Raw URLs pulled directly from phishing emails.</em></p>

---

### 📈 **4. Final Findings (Excel Output)**
<p align="center">
  <img src="https://github.com/nabirudd/phishing-email-analysis-python/blob/main/screenshots/output_final_findings.png?raw=true" alt="final findings output" width="750" style="border:2px solid #555; border-radius:10px; padding:5px;">
</p>
<p align="center"><em>Consolidated phishing intelligence summary for analyst review.</em></p>

---

### 🧾 **5. Final Report**
<p align="center">
  <img src="https://github.com/nabirudd/phishing-email-analysis-python/blob/main/screenshots/output_final_report.png?raw=true" alt="final report output" width="750" style="border:2px solid #555; border-radius:10px; padding:5px;">
</p>
<p align="center"><em>Comprehensive PDF report with findings and prevention strategies.</em></p>

---

### 🧮 **6. Findings**
<p align="center">
  <img src="https://github.com/nabirudd/phishing-email-analysis-python/blob/main/screenshots/output_findings.png?raw=true" alt="findings output" width="750" style="border:2px solid #555; border-radius:10px; padding:5px;">
</p>
<p align="center"><em>Intermediate Excel summary showing raw and enriched phishing data.</em></p>

---

### 💼 **7. Findings Formatted**
<p align="center">
  <img src="https://github.com/nabirudd/phishing-email-analysis-python/blob/main/screenshots/output_findings_formatted.png?raw=true" alt="findings formatted output" width="750" style="border:2px solid #555; border-radius:10px; padding:5px;">
</p>
<p align="center"><em>Polished Excel output, styled for presentation or client reporting.</em></p>

---

### 🧠 **8. URL Reputation**
<p align="center">
  <img src="https://github.com/nabirudd/phishing-email-analysis-python/blob/main/screenshots/output_url_reputation.png?raw=true" alt="url reputation output" width="750" style="border:2px solid #555; border-radius:10px; padding:5px;">
</p>
<p align="center"><em>Shows malicious/suspicious ratings gathered from VirusTotal.</em></p>

---

### 🌍 **9. URLScan Results**
<p align="center">
  <img src="https://github.com/nabirudd/phishing-email-analysis-python/blob/main/screenshots/output_urlscan_results.png?raw=true" alt="urlscan results output" width="750" style="border:2px solid #555; border-radius:10px; padding:5px;">
</p>
<p align="center"><em>Sandbox snapshots and metadata from urlscan.io analysis.</em></p>

---

<p align="center">
  <em>“Security is not a product, but a process.” – Bruce Schneier</em>
</p>
