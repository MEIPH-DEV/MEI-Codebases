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
    pdf_filename = "RM_Codebase.pdf"
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=A4,
        leftMargin=15 * mm,
        rightMargin=15 * mm,
        topMargin=15 * mm,
        bottomMargin=15 * mm,
    )

    styles = getSampleStyleSheet()

    # Color Palette
    primary_color = colors.HexColor("#1e3a8a")  # Deep Blue
    secondary_color = colors.HexColor("#2563eb")  # Royal Blue
    accent_color = colors.HexColor("#3b82f6")
    text_color = colors.HexColor("#1e293b")
    callout_bg = colors.HexColor("#eff6ff")
    callout_border = colors.HexColor("#1d4ed8")

    # Typography Styles
    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=20,
        textColor=colors.white,
        spaceAfter=4,
    )

    subtitle_style = ParagraphStyle(
        "SubtitleStyle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9,
        textColor=colors.HexColor("#bfdbfe"),
    )

    h2_style = ParagraphStyle(
        "H2Style",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=12,
        textColor=primary_color,
        spaceBefore=12,
        spaceAfter=8,
    )

    body_style = ParagraphStyle(
        "BodyStyle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.5,
        leading=11,
        textColor=text_color,
    )

    bold_body_style = ParagraphStyle(
        "BoldBodyStyle", parent=body_style, fontName="Helvetica-Bold"
    )

    th_style = ParagraphStyle(
        "THStyle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=8,
        textColor=colors.white,
    )

    callout_style = ParagraphStyle(
        "CalloutStyle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8,
        leading=11,
        textColor=colors.HexColor("#1e40af"),
    )

    story = []

    # 1. Header Banner
    header_data = [
        [
            Paragraph("RM CODEBASE", title_style),
            Paragraph(
                "<b>Reproductive & Men's Health Clinical Formulary</b>",
                subtitle_style,
            ),
        ]
    ]
    header_table = Table(header_data, colWidths=[100 * mm, 80 * mm])
    header_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), primary_color),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("PADDING", (0, 0), (-1, -1), 10),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
            ]
        )
    )
    story.append(header_table)
    story.append(Spacer(1, 10))

    # 2. Section Heading
    story.append(Paragraph("1. Product Formulary & Clinical Reference", h2_style))
    story.append(
        HRFlowable(
            width="100%",
            thickness=1.5,
            color=secondary_color,
            spaceBefore=1,
            spaceAfter=8,
        )
    )

    # 3. Formulary Table Data
    table_data = [
        [
            Paragraph("Brand Name", th_style),
            Paragraph("Active Ingredient", th_style),
            Paragraph("Clinical Indications", th_style),
            Paragraph("Mechanism of Action", th_style),
            Paragraph("Dosing & Clinical Pearls", th_style),
        ],
        [
            Paragraph("Mamazol", bold_body_style),
            Paragraph("Miconazole", body_style),
            Paragraph(
                "Candidal balanitis, cutaneous fungal infections, intertrigo.",
                body_style,
            ),
            Paragraph(
                "Inhibits ergosterol synthesis, disrupting fungal cell membrane integrity.",
                body_style,
            ),
            Paragraph(
                "Apply thin layer to affected area BID for 2-4 weeks. Keep area dry.",
                body_style,
            ),
        ],
        [
            Paragraph("Pubergen", bold_body_style),
            Paragraph("Human Chorionic Gonadotropin (hCG)", body_style),
            Paragraph(
                "Hypogonadotropic hypogonadism, male infertility, cryptorchidism.",
                body_style,
            ),
            Paragraph(
                "LH analogue; stimulates Leydig cells to produce endogenous testosterone.",
                body_style,
            ),
            Paragraph(
                "1500–5000 IU IM/SC 2–3 times weekly. Preserves intratesticular T during TRT.",
                body_style,
            ),
        ],
        [
            Paragraph("Gynogen", bold_body_style),
            Paragraph("Estradiol", body_style),
            Paragraph(
                "Estrogen deficiency, endocrine therapy, hormone replacement protocols.",
                body_style,
            ),
            Paragraph(
                "Binds estrogen receptors; modulates gonadotropin release and metabolic target tissues.",
                body_style,
            ),
            Paragraph(
                "Individualized dosing based on serum levels. Monitor cardiovascular & hepatic markers.",
                body_style,
            ),
        ],
        [
            Paragraph("Endogen", bold_body_style),
            Paragraph("Dienogest", body_style),
            Paragraph(
                "Progestogenic management, pelvic pain suppression, hormone-dependent tissue control.",
                body_style,
            ),
            Paragraph(
                "Selective progestin; suppresses endogenous estradiol secretion and induces tissue atrophy.",
                body_style,
            ),
            Paragraph(
                "2 mg daily continuously. Consistent daily dosing prevents breakthrough bleeding.",
                body_style,
            ),
        ],
        [
            Paragraph("Evaban", bold_body_style),
            Paragraph("Apixaban", body_style),
            Paragraph(
                "DVT/PE prophylaxis, thromboprophylaxis in high-risk vascular/pelvic procedures.",
                body_style,
            ),
            Paragraph(
                "Direct FXa inhibitor; blocks prothrombinase activity and clot formation.",
                body_style,
            ),
            Paragraph(
                "2.5 mg to 5 mg BID depending on indication and renal function.",
                body_style,
            ),
        ],
        [
            Paragraph("Endmet 11.25", bold_body_style),
            Paragraph("Leuprorelin Acetate (11.25mg)", body_style),
            Paragraph(
                "Advanced prostate cancer, long-term androgen deprivation therapy (ADT).",
                body_style,
            ),
            Paragraph(
                "3-month GnRH depot; desensitizes receptors to lower serum testosterone to castrate levels.",
                body_style,
            ),
            Paragraph(
                "11.25 mg SC/IM every 12 weeks. Monitor PSA and serum testosterone levels.",
                body_style,
            ),
        ],
        [
            Paragraph("Endmet 3.75", bold_body_style),
            Paragraph("Leuprorelin Acetate (3.75mg)", body_style),
            Paragraph(
                "Prostate cancer (monthly ADT), hormone-sensitive neoplasm management.",
                body_style,
            ),
            Paragraph(
                "Continuous GnRH receptor stimulation inducing LH/FSH suppression.",
                body_style,
            ),
            Paragraph(
                "3.75 mg SC/IM monthly. Co-administer anti-androgen initially to prevent flare.",
                body_style,
            ),
        ],
    ]

    col_widths = [30 * mm, 38 * mm, 38 * mm, 40 * mm, 34 * mm]
    form_table = Table(table_data, colWidths=col_widths, repeatRows=1)

    table_style = [
        ("BACKGROUND", (0, 0), (-1, 0), primary_color),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ("PADDING", (0, 0), (-1, -1), 5),
    ]

    for i in range(1, len(table_data)):
        if i % 2 == 0:
            table_style.append(
                ("BACKGROUND", (0, i), (-1, i), colors.HexColor("#eff6ff"))
            )

    form_table.setStyle(TableStyle(table_style))
    story.append(form_table)
    story.append(Spacer(1, 12))

    # 4. Clinical Callout Box
    callout_text = (
        "<b>RM Clinical Guidance: Androgen Deprivation Therapy (ADT) Flare Prevention</b><br/>"
        "Initiating GnRH agonists such as <b>Endmet 3.75</b> or <b>Endmet 11.25</b> causes an initial "
        "transient surge in serum testosterone. To prevent symptomatic disease flare (e.g., bone pain, acute urinary obstruction), "
        "co-administer an anti-androgen starting prior to or concurrently with the first depot injection."
    )
    callout_data = [[Paragraph(callout_text, callout_style)]]
    callout_table = Table(callout_data, colWidths=[180 * mm])
    callout_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), callout_bg),
                ("BOX", (0, 0), (-1, -1), 1, callout_border),
                ("PADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )
    story.append(callout_table)

    doc.build(story)
    print("PDF output successfully generated as RM_Codebase.pdf")


if __name__ == "__main__":
    build_pdf()