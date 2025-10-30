#!/usr/bin/env python3
"""创建一个简单的测试PDF文件"""

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_simple_pdf(filename="simple_test.pdf"):
    """创建一个非常简单的PDF"""
    c = canvas.Canvas(filename, pagesize=letter)

    # 只添加简单文本
    c.drawString(100, 750, "Hello World!")
    c.drawString(100, 730, "This is a simple test PDF.")
    c.drawString(100, 710, "Testing PDF to DOCX conversion.")

    c.save()
    print(f"Simple test PDF created: {filename}")

if __name__ == "__main__":
    create_simple_pdf()
