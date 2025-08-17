code = """\
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm

# Output file PDF
file_path = "Slip_Gaji_Geren_Mario_Balia.pdf"

doc = SimpleDocTemplate(file_path, pagesize=A4,
                        rightMargin=2*cm, leftMargin=2*cm,
                        topMargin=2*cm, bottomMargin=2*cm)

story = []
styles = getSampleStyleSheet()

# --- Header dengan Logo ---
logo = "logo.png"  # pastikan ada file logo.png di folder
im = Image(logo, 3*cm, 3*cm)

company_text = \"\"\"<b>PT ARIGHT MARKETING INDONESIA</b><br/>
Graha Boulevard Kelapa Gading Blok KGC No. C09, Jakarta Utara 14240\"\"\"

style_company = ParagraphStyle(
    name="Company",
    fontSize=11,
    leading=13,
    spaceAfter=6,
    alignment=0
)

header_table = Table([
    [im, Paragraph(company_text, style_company)]
], colWidths=[3.5*cm, 12*cm])

header_table.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE")
]))

story.append(header_table)
story.append(Spacer(1, 12))
story.append(Paragraph("<b>SLIP GAJI</b>", ParagraphStyle(name="Title", alignment=1, fontSize=14)))
story.append(Paragraph("Periode: 01 – 30 Juli 2025", styles["Normal"]))
story.append(Spacer(1, 12))

# --- Data Karyawan ---
story.append(Paragraph("<b>Data Karyawan</b>", styles["Heading3"]))
data_karyawan = [
    ["Nama", "Geren Mario Balia"],
    ["Jabatan", "Assistant Marketing Manager"],
    ["NIK", "00589"]
]
table1 = Table(data_karyawan, colWidths=[5*cm, 10*cm])
table1.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
    ("FONTSIZE", (0, 0), (-1, -1), 10)
]))
story.append(table1)
story.append(Spacer(1, 12))

# --- Rincian Gaji ---
story.append(Paragraph("<b>Rincian Gaji</b>", styles["Heading3"]))
data_gaji = [
    ["Gaji Pokok", "11.550.000"],
    ["Bonus", "500.000"],
    ["Special Allowance", "600.000"],
    ["<b>Total Pendapatan</b>", "<b>12.650.000</b>"]
]
table2 = Table(data_gaji, colWidths=[8*cm, 7*cm])
table2.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
    ("FONTSIZE", (0, 0), (-1, -1), 10),
    ("ALIGN", (1, 0), (1, -1), "RIGHT")
]))
story.append(table2)
story.append(Spacer(1, 12))

# --- Potongan ---
story.append(Paragraph("<b>Potongan</b>", styles["Heading3"]))
data_potongan = [
    ["BPJS Ketenagakerjaan", "350.000"],
    ["PPh 21", "200.000"],
    ["<b>Total Potongan</b>", "<b>550.000</b>"]
]
table3 = Table(data_potongan, colWidths=[8*cm, 7*cm])
table3.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
    ("FONTSIZE", (0, 0), (-1, -1), 10),
    ("ALIGN", (1, 0), (1, -1), "RIGHT")
]))
story.append(table3)
story.append(Spacer(1, 12))

# --- Take Home Pay ---
style_takehome = ParagraphStyle(
    name="TakeHome",
    alignment=1,
    fontSize=12,
    leading=14,
    textColor=colors.green,
    spaceAfter=12
)
story.append(Paragraph("<b>Gaji Bersih (Take Home Pay): Rp 12.100.000</b>", style_takehome))

# --- Footer ---
style_footer = ParagraphStyle(
    name="Footer",
    alignment=1,
    fontSize=8,
    textColor=colors.grey
)
story.append(Paragraph("*Slip gaji ini bersifat rahasia, dicetak otomatis oleh sistem, tidak memerlukan tanda tangan atau stempel.*", style_footer))

# Build PDF
doc.build(story)

print("Slip gaji berhasil dibuat:", file_path)
"""

with open("/mnt/data/buat_slip_gaji.py", "w") as f:
    f.write(code)

		
	
		
	
		
