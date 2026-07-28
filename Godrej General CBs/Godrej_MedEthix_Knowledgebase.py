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
    pdf_filename = "Godrej_MedEthix_Knowledgebase.pdf"
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=A4,
        leftMargin=15 * mm,
        rightMargin=15 * mm,
        topMargin=15 * mm,
        bottomMargin=15 * mm,
    )

    styles = getSampleStyleSheet()

    # Green Theme for Godrej & MedEthix FMCG Portfolio
    primary_color = colors.HexColor("#15803d")  # Forest Green
    secondary_color = colors.HexColor("#16a34a")  # Emerald Green
    text_color = colors.HexColor("#0f172a")
    callout_bg = colors.HexColor("#f0fdf4")
    callout_border = colors.HexColor("#16a34a")

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
        textColor=colors.HexColor("#dcfce7"),
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
        textColor=colors.HexColor("#15803d"),
    )

    story = []

    # 1. Header Banner
    header_data = [
        [
            Paragraph("GODREJ FMCG PORTFOLIO", title_style),
            Paragraph(
                "<b>Consumer, Baby & Home Care (MedEthix Channel)</b>",
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

    # 2. Section Heading - Operational Framework
    story.append(
        Paragraph("1. Strategic Distribution Overview", h2_style)
    )
    story.append(
        HRFlowable(
            width="100%",
            thickness=1.5,
            color=secondary_color,
            spaceBefore=1,
            spaceAfter=6,
        )
    )

    corp_data = [
        [
            Paragraph("Portfolio Dimension", th_style),
            Paragraph("Details & Strategic Value", th_style),
        ],
        [
            Paragraph("Principal Manufacturer", bold_body_style),
            Paragraph(
                "Godrej Consumer Products Limited (GCPL) — global leader in personal care, hair care, and home insecticides.",
                body_style,
            ),
        ],
        [
            Paragraph("Channel Partner", bold_body_style),
            Paragraph(
                "MedEthix Incorporated — facilitating local distribution, healthcare channel access, and regulatory support.",
                body_style,
            ),
        ],
        [
            Paragraph("Target Market Segment", bold_body_style),
            Paragraph(
                "Filipino families seeking affordable, dermatologically safe baby wipes, gentle hair color, ambient scents, and disease vector control.",
                body_style,
            ),
        ],
    ]

    corp_table = Table(corp_data, colWidths=[50 * mm, 130 * mm], repeatRows=1)
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
                ("BACKGROUND", (0, i), (-1, i), colors.HexColor("#f0fdf4"))
            )
    corp_table.setStyle(TableStyle(corp_style))
    story.append(corp_table)
    story.append(Spacer(1, 10))

    # 3. Section Heading - Product Portfolio
    story.append(Paragraph("2. Godrej Brands Breakdown", h2_style))
    story.append(
        HRFlowable(
            width="100%",
            thickness=1.5,
            color=secondary_color,
            spaceBefore=1,
            spaceAfter=6,
        )
    )

    prod_data = [
        [
            Paragraph("Brand Name", th_style),
            Paragraph("Category", th_style),
            Paragraph("Flagship Items", th_style),
            Paragraph("Key Value Proposition", th_style),
        ],
        [
            Paragraph("Mitu Baby®", bold_body_style),
            Paragraph("Baby Hygiene", body_style),
            Paragraph("Hypoallergenic Wipes, Powder, Shampoo", body_style),
            Paragraph(
                "Alcohol-free, dermatologically tested wipes enriched with soothing Chamomile and Aloe Vera.",
                body_style,
            ),
        ],
        [
            Paragraph("NYU®", bold_body_style),
            Paragraph("Hair Care", body_style),
            Paragraph("NYU Crème Color, Henna Shampoo", body_style),
            Paragraph(
                "100% ammonia-free hair color formula with super-fruit oil extracts and pleasant fruity aroma.",
                body_style,
            ),
        ],
        [
            Paragraph("Stella®", bold_body_style),
            Paragraph("Air Care", body_style),
            Paragraph("Stella Matic, Pocket, Reed Diffuser", body_style),
            Paragraph(
                "Long-lasting ambient fresheners engineered with natural essential oils for homes & cars.",
                body_style,
            ),
        ],
        [
            Paragraph("HIT®", bold_body_style),
            Paragraph("Insect Control", body_style),
            Paragraph("HIT Aerosol, Goodknight Electric", body_style),
            Paragraph(
                "Fast knock-down vector protection against dengue mosquitoes, flies, and crawling pests.",
                body_style,
            ),
        ],
    ]

    prod_table = Table(
        prod_data, colWidths=[35 * mm, 32 * mm, 45 * mm, 68 * mm], repeatRows=1
    )
    prod_table.setStyle(TableStyle(corp_style))
    story.append(prod_table)
    story.append(Spacer(1, 10))

    # 4. Callout Box
    callout_text = (
        "<b>Summary Note:</b><br/>"
        "By integrating Godrej's household care innovations (<b>Mitu Baby</b>, <b>NYU</b>, <b>Stella</b>, and <b>HIT</b>), "
        "MedEthix expands beyond prescription pharmaceuticals into holistic family healthcare, hygiene, and wellness."
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
        "PDF output successfully generated as Godrej_MedEthix_Knowledgebase.pdf"
    )


if __name__ == "__main__":
    build_pdf()