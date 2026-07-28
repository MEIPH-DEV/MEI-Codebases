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
    pdf_filename = "General_OB_Codebase.pdf"
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=A4,
        leftMargin=15 * mm,
        rightMargin=15 * mm,
        topMargin=15 * mm,
        bottomMargin=15 * mm,
    )

    styles = getSampleStyleSheet()

    # Obstetrics Color Palette
    primary_color = colors.HexColor("#831843")  # Deep Berry / Burgundy
    secondary_color = colors.HexColor("#be185d")  # Rose Red
    text_color = colors.HexColor("#1e293b")
    callout_bg = colors.HexColor("#fdf2f8")
    callout_border = colors.HexColor("#be185d")

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
        textColor=colors.HexColor("#fbcfe8"),
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
        textColor=colors.HexColor("#831843"),
    )

    story = []

    # 1. Header Banner
    header_data = [
        [
            Paragraph("GENERAL OB CODEBASE", title_style),
            Paragraph(
                "<b>Obstetrics & Maternal Health Formulary Manual</b>",
                subtitle_style,
            ),
        ]
    ]
    header_table = Table(header_data, colWidths=[105 * mm, 75 * mm])
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
    story.append(Paragraph("1. Obstetric Brand Formulary Reference", h2_style))
    story.append(
        HRFlowable(
            width="100%",
            thickness=1.5,
            color=secondary_color,
            spaceBefore=1,
            spaceAfter=6,
        )
    )

    # 3. Formulary Table Data
    table_data = [
        [
            Paragraph("Brand Name", th_style),
            Paragraph("Active Ingredient", th_style),
            Paragraph("Clinical Indications", th_style),
            Paragraph("Mechanism of Action", th_style),
            Paragraph("Dosing & Pearls", th_style),
        ],
        [
            Paragraph("Dydrogest", bold_body_style),
            Paragraph("Dydrogesterone", body_style),
            Paragraph(
                "Threatened miscarriage, recurrent loss, luteal support.",
                body_style,
            ),
            Paragraph(
                "Orally active progestogen; selective progesterone receptor affinity.",
                body_style,
            ),
            Paragraph(
                "10-40 mg daily. Non-androgenic pregnancy support.", body_style
            ),
        ],
        [
            Paragraph("Evamin", bold_body_style),
            Paragraph("Multivitamins", body_style),
            Paragraph(
                "Maternal vitamin support, preconception care.", body_style
            ),
            Paragraph(
                "Provides micronutrients essential for increased demands.",
                body_style,
            ),
            Paragraph("1 tablet daily post-meal with water.", body_style),
        ],
        [
            Paragraph("Medeprim", bold_body_style),
            Paragraph("Co-trimoxazole", body_style),
            Paragraph(
                "Susceptible urinary tract & pulmonary infections.", body_style
            ),
            Paragraph(
                "Sequential blockade of bacterial folate synthesis.",
                body_style,
            ),
            Paragraph(
                "1 DS tab BID. Avoid near delivery (kernicterus risk).",
                body_style,
            ),
        ],
        [
            Paragraph("Mum-2-B Plus", bold_body_style),
            Paragraph("Multivitamins & Minerals", body_style),
            Paragraph(
                "Prenatal support, neural tube defect prevention.", body_style
            ),
            Paragraph(
                "Delivers essential minerals & Folic Acid for development.",
                body_style,
            ),
            Paragraph(
                "1 capsule daily. Critical during early gestation.", body_style
            ),
        ],
        [
            Paragraph("Prevadopa", bold_body_style),
            Paragraph("Methyldopa", body_style),
            Paragraph(
                "Gestational hypertension, preeclampsia.", body_style
            ),
            Paragraph(
                "Central alpha-2 agonist; lowers vascular resistance.",
                body_style,
            ),
            Paragraph(
                "250-500 mg BID/TID. Preferred first-line agent.", body_style
            ),
        ],
        [
            Paragraph("Tranamic", bold_body_style),
            Paragraph("Tranexamic Acid", body_style),
            Paragraph(
                "Postpartum hemorrhage (PPH), bleeding control.", body_style
            ),
            Paragraph(
                "Antifibrinolytic; prevents plasmin degradation of fibrin.",
                body_style,
            ),
            Paragraph(
                "1 g IV over 10 mins within 3 hrs of PPH onset.", body_style
            ),
        ],
        [
            Paragraph("Erytose", bold_body_style),
            Paragraph("Erythromycin", body_style),
            Paragraph(
                "PPROM latency, gestational Chlamydia infection.", body_style
            ),
            Paragraph(
                "Macrolide; reversibly binds 50S ribosomal subunit.",
                body_style,
            ),
            Paragraph("250-500 mg QID. Standard in PPROM protocols.", body_style),
        ],
        [
            Paragraph("Evafer", bold_body_style),
            Paragraph("Iron Supplement", body_style),
            Paragraph("Iron deficiency anemia, blood loss recovery.", body_style),
            Paragraph(
                "Supplies elemental iron for hemoglobin production.", body_style
            ),
            Paragraph("60-120 mg elemental iron daily + Vitamin C.", body_style),
        ],
        [
            Paragraph("Evacarb 125", bold_body_style),
            Paragraph("Carbamazepine (125mg)", body_style),
            Paragraph("Maternal seizure management, neuralgia.", body_style),
            Paragraph("Blocks voltage-gated sodium channels.", body_style),
            Paragraph(
                "125 mg BID. Co-administer 5 mg/day Folic Acid.", body_style
            ),
        ],
        [
            Paragraph("Evacarb 250", bold_body_style),
            Paragraph("Carbamazepine (250mg)", body_style),
            Paragraph("Generalized tonic-clonic epilepsy in OB.", body_style),
            Paragraph("Suppresses repetitive firing in neuronal membranes.", body_style),
            Paragraph("250 mg BID/TID. Give maternal Vitamin K prior to birth.", body_style),
        ],
        [
            Paragraph("Contractocin", bold_body_style),
            Paragraph("Oxytocin", body_style),
            Paragraph(
                "Labor induction/augmentation, PPH management.", body_style
            ),
            Paragraph(
                "Binds oxytocin receptors; induces uterine contraction.",
                body_style,
            ),
            Paragraph(
                "Induction: 1-2 mU/min IV. PPH: 10 units IM/IV drip.",
                body_style,
            ),
        ],
    ]

    col_widths = [26 * mm, 36 * mm, 38 * mm, 42 * mm, 38 * mm]
    form_table = Table(table_data, colWidths=col_widths, repeatRows=1)

    table_style = [
        ("BACKGROUND", (0, 0), (-1, 0), primary_color),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ("PADDING", (0, 0), (-1, -1), 4),
    ]

    for i in range(1, len(table_data)):
        if i % 2 == 0:
            table_style.append(
                ("BACKGROUND", (0, i), (-1, i), colors.HexColor("#fdf2f8"))
            )

    form_table.setStyle(TableStyle(table_style))
    story.append(form_table)
    story.append(Spacer(1, 10))

    # 4. Clinical Callout Box
    callout_text = (
        "<b>Obstetric High-Alert Protocol: Postpartum Hemorrhage (PPH) Management</b><br/>"
        "When managing PPH, early treatment is crucial: administer <b>Tranamic</b> (Tranexamic Acid 1 g IV) "
        "alongside uterotonic therapies like <b>Contractocin</b> (Oxytocin) within 3 hours of birth. "
        "Delay beyond 3 hours significantly diminishes antifibrinolytic effectiveness."
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
    print("PDF output successfully generated as General_OB_Codebase.pdf")


if __name__ == "__main__":
    build_pdf()