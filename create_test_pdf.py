#!/usr/bin/env python3
"""创建一个测试用的PDF文件"""

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def create_test_pdf(filename="test.pdf"):
    """创建一个包含文本和简单内容的测试PDF"""
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # 第一页
    c.setFont("Helvetica-Bold", 24)
    c.drawString(1*inch, height - 1*inch, "PDF to DOCX Conversion Test")

    c.setFont("Helvetica", 12)
    c.drawString(1*inch, height - 1.5*inch, "This is a test PDF file created for testing the PDF to DOCX converter.")

    c.setFont("Helvetica-Bold", 16)
    c.drawString(1*inch, height - 2.5*inch, "Features to test:")

    c.setFont("Helvetica", 12)
    features = [
        "1. Text extraction and formatting",
        "2. Multiple paragraphs",
        "3. Different font sizes",
        "4. Bullet points and lists",
        "5. Multiple pages"
    ]

    y_position = height - 3*inch
    for feature in features:
        c.drawString(1.5*inch, y_position, feature)
        y_position -= 0.3*inch

    # 添加一些段落
    c.setFont("Helvetica", 11)
    paragraph = (
        "This paragraph contains some regular text to test how well the converter "
        "handles normal paragraph formatting. The text should be properly extracted "
        "and formatted in the resulting DOCX file."
    )

    y_position -= 0.5*inch
    c.drawString(1*inch, y_position, "Sample paragraph:")
    y_position -= 0.3*inch

    # 分行显示段落
    words = paragraph.split()
    line = ""
    for word in words:
        if len(line + word) < 70:
            line += word + " "
        else:
            c.drawString(1*inch, y_position, line)
            y_position -= 0.2*inch
            line = word + " "
    if line:
        c.drawString(1*inch, y_position, line)

    # 添加第二页
    c.showPage()
    c.setFont("Helvetica-Bold", 20)
    c.drawString(1*inch, height - 1*inch, "Page 2")

    c.setFont("Helvetica", 12)
    c.drawString(1*inch, height - 1.5*inch, "This is the second page of the test PDF.")
    c.drawString(1*inch, height - 2*inch, "It helps test multi-page conversion capability.")

    # 添加一些数字列表
    c.setFont("Helvetica-Bold", 14)
    c.drawString(1*inch, height - 3*inch, "Important Notes:")

    c.setFont("Helvetica", 11)
    notes = [
        "- The converter should preserve text content",
        "- Layout may vary slightly from the original",
        "- Complex formatting might need adjustment",
        "- Images and special elements may require special handling"
    ]

    y_position = height - 3.5*inch
    for note in notes:
        c.drawString(1.5*inch, y_position, note)
        y_position -= 0.3*inch

    # 保存PDF
    c.save()
    print(f"Test PDF created: {filename}")

if __name__ == "__main__":
    create_test_pdf("test.pdf")
