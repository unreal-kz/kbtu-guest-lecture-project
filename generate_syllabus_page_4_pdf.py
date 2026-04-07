from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


OUTPUT_PATH = "syllabus-page-4.pdf"


def make_styles():
    styles = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "Title",
            parent=styles["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=14,
            leading=18,
            alignment=TA_CENTER,
            spaceAfter=6,
        ),
        "subtitle": ParagraphStyle(
            "Subtitle",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=10,
            leading=12,
            alignment=TA_LEFT,
            spaceBefore=4,
            spaceAfter=4,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=8.3,
            leading=10.2,
            alignment=TA_LEFT,
        ),
        "body_bold": ParagraphStyle(
            "BodyBold",
            parent=styles["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=8.3,
            leading=10.2,
            alignment=TA_LEFT,
        ),
        "small": ParagraphStyle(
            "Small",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=7.6,
            leading=9.0,
            alignment=TA_LEFT,
        ),
        "small_center": ParagraphStyle(
            "SmallCenter",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=7.2,
            leading=8.6,
            alignment=TA_CENTER,
        ),
    }


def p(text, style):
    return Paragraph(text, style)


def build_calendar_table(styles):
    rows = [
        [
            p("No", styles["small_center"]),
            p("Topic", styles["body_bold"]),
            p("Lecture", styles["small_center"]),
            p("Practice", styles["small_center"]),
            p("SIS (students independent study)", styles["small_center"]),
            p("TSIS (teacher supervised independent study)", styles["small_center"]),
        ],
        [
            "1",
            p("Introduction to Field Methods in IS", styles["body"]),
            "3",
            "0",
            "",
            "",
        ],
        [
            "2",
            p("Organizations, Stakeholders, Ethics in Field Work", styles["body"]),
            "3",
            "0",
            "",
            "",
        ],
        [
            "3",
            p("Interpretive User Research &amp; Interviewing", styles["body"]),
            "3",
            "0",
            "",
            "",
        ],
        [
            "4",
            p("Qualitative Analysis: Open &amp; Axial Coding", styles["body"]),
            "3",
            "0",
            "",
            p("TSIS 1 defense: Interpretive User Research", styles["body"]),
        ],
        [
            "5",
            p(
                "Problem Framing theories in Information Systems: Variance, "
                "Covariation in the system, Process (sequence of events), "
                "Systems (overall system)",
                styles["body"],
            ),
            "3",
            "0",
            "",
            p("TSIS 2 defense: QCA Requirements Quality Analysis", styles["body"]),
        ],
        [
            "6",
            p("Survey Research Design for IS", styles["body"]),
            "3",
            "0",
            "",
            "",
        ],
        [
            "7",
            p("Descriptive &amp; Inferential Statistics for IS", styles["body"]),
            "3",
            "0",
            "",
            p("TSIS 3 defense: Survey &amp; Statistical Analysis", styles["body"]),
        ],
        [
            "8",
            p("Qualitative Comparative Analysis (QCA): Logic &amp; Sets", styles["body"]),
            "3",
            "0",
            p("Midterm test", styles["body"]),
            "",
        ],
        [
            "9",
            p("QCA in Practice: Truth Tables &amp; Configurations", styles["body"]),
            "3",
            "0",
            "",
            p("TSIS 4 defense: ML Metrics Evaluation", styles["body"]),
        ],
        [
            "10",
            p("IS Requirements &amp; Solution Design", styles["body"]),
            "3",
            "0",
            "",
            "",
        ],
        [
            "11",
            p("ML-enabled IS &amp; Evaluation Metrics", styles["body"]),
            "3",
            "0",
            p("SIS consultations", styles["body"]),
            "",
        ],
        [
            "12",
            p("Integrating Field Data for IS Decisions", styles["body"]),
            "3",
            "0",
            p("SIS submission and defense", styles["body"]),
            "",
        ],
        [
            "13",
            p("Field Project Consultation &amp; Improvement", styles["body"]),
            "3",
            "0",
            "",
            "",
        ],
        [
            "14",
            p("Professional Reporting &amp; Stakeholder Presentation", styles["body"]),
            "3",
            "0",
            "",
            "",
        ],
        [
            "15",
            p("Final Exam Review &amp; Integration", styles["body"]),
            "3",
            "0",
            p("Endterm test", styles["body"]),
            "",
        ],
        [
            "16-17",
            p("Final Exam", styles["body"]),
            "",
            "",
            "",
            "",
        ],
    ]

    table = Table(
        rows,
        colWidths=[10 * mm, 66 * mm, 12 * mm, 12 * mm, 33 * mm, 45 * mm],
        repeatRows=1,
    )
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e9ecef")),
                ("GRID", (0, 0), (-1, -1), 0.4, colors.black),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ALIGN", (0, 0), (0, -1), "CENTER"),
                ("ALIGN", (2, 0), (3, -1), "CENTER"),
                ("ALIGN", (4, 0), (5, 0), "CENTER"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ]
        )
    )
    return table


def build_assessment_table(styles):
    header = ["No", "Assessment criteria"] + [str(i) for i in range(1, 16)] + ["Weight"]
    rows = [
        header,
        ["1", p("Attendance / participation", styles["small"]), *["" for _ in range(15)], "0%"],
        ["2", "Practice", *["" for _ in range(15)], "0%"],
        ["3", "SIS", *["" for _ in range(11)], "*", "", "", "", "10%"],
        ["4", "TSIS", "", "", "", "*", "*", "", "*", "", "*", "", "", "", "", "", "10%"],
        ["5", "Mid-term", "", "", "", "", "", "", "*", "", "", "", "", "", "", "", "30%"],
        ["6", "End-term", "", "", "", "", "", "", "", "", "", "", "", "", "", "*", "10%"],
        ["7", p("Final examination", styles["small"]), *["" for _ in range(15)], "40%"],
        ["", "Total", *["" for _ in range(15)], "100%"],
    ]

    col_widths = [9 * mm, 28 * mm] + [8 * mm for _ in range(15)] + [13 * mm]
    table = Table(rows, colWidths=col_widths, repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e9ecef")),
                ("GRID", (0, 0), (-1, -1), 0.35, colors.black),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("ALIGN", (1, 1), (1, -1), "LEFT"),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                ("LEFTPADDING", (0, 0), (-1, -1), 3),
                ("RIGHTPADDING", (0, 0), (-1, -1), 3),
            ]
        )
    )
    return table


def build_pdf():
    styles = make_styles()
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=A4,
        leftMargin=12 * mm,
        rightMargin=12 * mm,
        topMargin=10 * mm,
        bottomMargin=10 * mm,
    )

    story = [
        p("Field Projects for IS", styles["title"]),
        p("Calendar (reconstructed from the provided page 4 scan)", styles["subtitle"]),
        build_calendar_table(styles),
        Spacer(1, 5 * mm),
        p("Course assessment schedule", styles["subtitle"]),
        build_assessment_table(styles),
        Spacer(1, 4 * mm),
        p(
            "<b>Class sessions</b> will be a mixture of information, discussion and practical "
            "application of skills.",
            styles["body"],
        ),
        p(
            "<b>Practice</b> will reinforce the students knowledge by practical appliance of "
            "lectured materials.",
            styles["body"],
        ),
        p(
            "<b>In-class assessment</b> will prepare students for their mid-term and final "
            "assessment and identify the competence level they have achieved on a related "
            "subject matter, the aim being to diagnose potential discrepancies in students "
            "understanding and performance in order to make specific adjustments to the "
            "course content and procedures.",
            styles["body"],
        ),
    ]

    doc.build(story)


if __name__ == "__main__":
    build_pdf()
    print(OUTPUT_PATH)
