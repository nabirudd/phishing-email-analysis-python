# scripts/export_pdf_report.py
# ------------------------------------------------------------
# Converts your phishing findings Excel into a professional PDF report.
# Requires: reportlab, pandas, openpyxl
# ------------------------------------------------------------

import os
import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from datetime import datetime

EXCEL_FILE = "outputs/findings_formatted.xlsx"
PDF_FILE = "outputs/phishing_analysis_report.pdf"

def generate_pdf():
    if not os.path.exists(EXCEL_FILE):
        raise SystemExit(f"❌ Missing {EXCEL_FILE}. Run format_excel.py first.")

    df = pd.read_excel(EXCEL_FILE)

    # Basic layout
    doc = SimpleDocTemplate(PDF_FILE, pagesize=landscape(A4), title="Phishing Analysis Report")
    styles = getSampleStyleSheet()
    story = []

    # Title page
    story.append(Paragraph("<b>Phishing Email Analysis Report</b>", styles["Title"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph(f"<b>Date:</b> {datetime.now().strftime('%d %B %Y')}", styles["Normal"]))
    story.append(Paragraph("<b>Author:</b> Your Name", styles["Normal"]))
    story.append(Spacer(1, 24))

    intro = """<b>Objective:</b> This report presents an automated analysis of email URLs using 
    Python, VirusTotal, and urlscan.io. The goal is to detect, classify, and understand phishing 
    techniques, demonstrating a practical understanding of social engineering detection."""
    story.append(Paragraph(intro, styles["BodyText"]))
    story.append(Spacer(1, 24))

    # Table Title
    story.append(Paragraph("<b>Top Phishing URL Findings</b>", styles["Heading2"]))
    story.append(Spacer(1, 12))

    # Limit to 10 rows for readability
    display_df = df.head(10).fillna("")
    table_data = [list(display_df.columns)] + display_df.values.tolist()

    # Create styled table
    table = Table(table_data, repeatRows=1)
    table_style = TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.darkblue),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,0), 8),
        ('BACKGROUND', (0,1), (-1,-1), colors.beige),
        ('GRID', (0,0), (-1,-1), 0.25, colors.grey)
    ])
    table.setStyle(table_style)
    story.append(table)
    story.append(Spacer(1, 24))

    # Summary section
    summary_text = """
    <b>Summary & Recommendations:</b><br/>
    • Most phishing attempts used credential harvesting and urgency tactics.<br/>
    • Common red flags included fake login forms and shortened URLs.<br/>
    • Recommend implementing SPF/DKIM/DMARC, blocking suspicious domains, and user awareness training.<br/>
    • Use sandbox tools (urlscan.io) and VirusTotal APIs for triage before opening unknown URLs.<br/>
    """
    story.append(Paragraph(summary_text, ParagraphStyle("Summary", fontSize=10, leading=14)))
    story.append(Spacer(1, 24))
    story.append(Paragraph("✅ <b>End of Report</b>", styles["Normal"]))

    # Build the PDF
    doc.build(story)
    print(f"✅ PDF report successfully created at: {PDF_FILE}")

if __name__ == "__main__":
    generate_pdf()
