from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    HRFlowable,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


def build_pdf():
    pdf_filename = "MedEthix_General_Info_Knowledgebase.pdf"
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=A4,
        leftMargin=15 * mm,
        rightMargin=15 * mm,
        topMargin=15 * mm,
        bottomMargin=15 * mm,
    )

    styles = getSampleStyleSheet()

    # Blue Theme for MedEthix Corporate Knowledgebase
    primary_color = colors.HexColor("#0369a1")  # Deep Ocean Blue
    secondary_color = colors.HexColor("#0284c7")  # Bright Sky Blue
    text_color = colors.HexColor("#0f172a")
    callout_bg = colors.HexColor("#f0f9ff")
    callout_border = colors.HexColor("#0284c7")

    # Typography Styles
    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=18,
        textColor=colors.white,
        spaceAfter=4,
    )

    subtitle_style = ParagraphStyle(
        "SubtitleStyle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9,
        textColor=colors.HexColor("#e0f2fe"),
    )

    h2_style = ParagraphStyle(
        "H2Style",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=11,
        textColor=primary_color,
        spaceBefore=10,
        spaceAfter=6,
    )

    body_style = ParagraphStyle(
        "BodyStyle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8,
        leading=10.5,
        textColor=text_color,
    )

    bold_body_style = ParagraphStyle(
        "BoldBodyStyle", parent=body_style, fontName="Helvetica-Bold"
    )

    th_style = ParagraphStyle(
        "THStyle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=7.5,
        textColor=colors.white,
    )

    callout_style = ParagraphStyle(
        "CalloutStyle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8,
        leading=11,
        textColor=colors.HexColor("#0369a1"),
    )

    story = []

    # 1. Header Banner
    header_data = [
        [
            Paragraph("MEDETHIX INCORPORATED", title_style),
            Paragraph(
                "<b>Corporate Overview & Knowledgebase</b>",
                subtitle_style,
            ),
        ]
    ]
    header_table = Table(header_data, colWidths=[110 * mm, 70 * mm])
    header_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), primary_color),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("PADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
            ]
        )
    )
    story.append(header_table)
    story.append(Spacer(1, 8))

    # 2. Section Heading
    story.append(Paragraph("1. Corporate Overview", h2_style))
    story.append(
        HRFlowable(
            width="100%",
            thickness=1.5,
            color=secondary_color,
            spaceBefore=1,
            spaceAfter=6,
        )
    )

    # Corporate Profile Table
    corp_data = [
        [
            Paragraph("Property", th_style),
            Paragraph("Details", th_style),
        ],
        [
            Paragraph("Established", bold_body_style),
            Paragraph(
                "2009 (Member of AC Health / Ayala Healthcare Holdings)",
                body_style,
            ),
        ],
        [
            Paragraph("Core Focus", bold_body_style),
            Paragraph(
                "Reproductive & Women's Health, First Aid Spray Therapeutics, Consumer Health, and Branded Generics",
                body_style,
            ),
        ],
        [
            Paragraph("Regulatory Footprint", bold_body_style),
            Paragraph(
                "Over 500 FDA product registrations; cGMP partners holding US-FDA and UK-MHRA accreditations",
                body_style,
            ),
        ],
    ]

    corp_table = Table(corp_data, colWidths=[45 * mm, 135 * mm], repeatRows=1)
    corp_style = [
        ("BACKGROUND", (0, 0), (-1, 0), primary_color),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ("PADDING", (0, 0), (-1, -1), 5),
    ]
    for i in range(1, len(corp_data)):
        if i % 2 == 0:
            corp_style.append(
                ("BACKGROUND", (0, i), (-1, i), colors.HexColor("#f0f9ff"))
            )
    corp_table.setStyle(TableStyle(corp_style))
    story.append(corp_table)
    story.append(Spacer(1, 10))

    # 3. Product Portfolio Heading
    story.append(Paragraph("2. Product Portfolio Reference", h2_style))
    story.append(
        HRFlowable(
            width="100%",
            thickness=1.5,
            color=secondary_color,
            spaceBefore=1,
            spaceAfter=6,
        )
    )

    # Product Table Data
    prod_data = [
        [
            Paragraph("Brand Name", th_style),
            Paragraph("Generic / Active Ingredient", th_style),
            Paragraph("Category", th_style),
            Paragraph("Clinical Indications", th_style),
        ],
        [
            Paragraph("Dydrogest", bold_body_style),
            Paragraph("Dydrogesterone", body_style),
            Paragraph("Reproductive", body_style),
            Paragraph(
                "Threatened miscarriage, recurrent loss, luteal support.",
                body_style,
            ),
        ],
        [
            Paragraph("Pubergen", bold_body_style),
            Paragraph("Human Chorionic Gonadotropin (hCG)", body_style),
            Paragraph("Fertility Care", body_style),
            Paragraph(
                "Infertility, hypogonadotropic hypogonadism.", body_style
            ),
        ],
        [
            Paragraph("Gynogen HP", bold_body_style),
            Paragraph("Human Menopausal Gonadotropin (hMG)", body_style),
            Paragraph("Reproductive", body_style),
            Paragraph("Controlled ovarian stimulation in ART.", body_style),
        ],
        [
            Paragraph("Endmet", bold_body_style),
            Paragraph("Leuprorelin Acetate (3.75/11.25mg)", body_style),
            Paragraph("Oncology/Endocrine", body_style),
            Paragraph("Prostate cancer, endometriosis, fibroids.", body_style),
        ],
        [
            Paragraph("Mum-2-B Gold", bold_body_style),
            Paragraph("Multivitamins + Minerals + DHA", body_style),
            Paragraph("Maternal Nutrition", body_style),
            Paragraph("Comprehensive prenatal & postnatal support.", body_style),
        ],
        [
            Paragraph("Tranamic", bold_body_style),
            Paragraph("Tranexamic Acid", body_style),
            Paragraph("Obstetrics/Surgery", body_style),
            Paragraph("Postpartum hemorrhage (PPH) management.", body_style),
        ],
        [
            Paragraph("Fast Aid Mist-Dress", bold_body_style),
            Paragraph("Lidocaine 1% + Cetrimide 0.1%", body_style),
            Paragraph("Wound Care", body_style),
            Paragraph("Liquid aerosol bandage for cuts and burns.", body_style),
        ],
        [
            Paragraph("RELISPRAY PLUS", bold_body_style),
            Paragraph("7 Essential Oils Complex", body_style),
            Paragraph("Topical Analgesic", body_style),
            Paragraph("Deep aerosol spray for muscle & joint pain.", body_style),
        ],
        [
            Paragraph("Fast Aid VINODINE", bold_body_style),
            Paragraph("Povidone-Iodine 5% Aerosol", body_style),
            Paragraph("Antiseptic Spray", body_style),
            Paragraph("Touch-free antiseptic for wound care.", body_style),
        ],
        [
            Paragraph("Medifilm Vit D3", bold_body_style),
            Paragraph("Cholecalciferol (OTF)", body_style),
            Paragraph("Consumer Health", body_style),
            Paragraph("Fast-dissolving oral strip for Vitamin D.", body_style),
        ],
    ]

    col_widths = [32 * mm, 50 * mm, 38 * mm, 60 * mm]
    prod_table = Table(prod_data, colWidths=col_widths, repeatRows=1)
    prod_table.setStyle(TableStyle(corp_style))
    story.append(prod_table)
    story.append(Spacer(1, 10))

    # 4. Callout Box
    callout_text = (
        "<b>Strategic Overview: MedEthix Incorporated</b><br/>"
        "MedEthix combines a robust regulatory platform with nationwide distribution under AC Health (Ayala Group). "
        "The company focuses on high-impact therapeutic areas including reproductive health, maternal care, "
        "and first-aid spray formulations across the Philippines."
    )
    callout_data = [[Paragraph(callout_text, callout_style)]]
    callout_table = Table(callout_data, colWidths=[180 * mm])
    callout_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), callout_bg),
                ("BOX", (0, 0), (-1, -1), 1, callout_border),
                ("PADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    story.append(callout_table)

    doc.build(story)
    print(
        "PDF output successfully generated as MedEthix_General_Info_Knowledgebase.pdf"
    )


if __name__ == "__main__":
    build_pdf()