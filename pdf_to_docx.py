#!/usr/bin/env python3
"""
PDF转DOCX工具
使用pdf2docx库将PDF文件转换为DOCX格式
"""

import argparse
import os
import sys
from pathlib import Path

try:
    from pdf2docx import Converter
except ImportError:
    print("错误: 未找到pdf2docx库。请运行: pip install pdf2docx")
    sys.exit(1)


def convert_pdf_to_docx(pdf_path, docx_path=None, start_page=0, end_page=None):
    """
    将PDF文件转换为DOCX格式

    参数:
        pdf_path: PDF文件路径
        docx_path: 输出的DOCX文件路径（可选，默认与PDF同名）
        start_page: 起始页码（从0开始）
        end_page: 结束页码（None表示到最后一页）

    返回:
        bool: 转换是否成功
    """
    # 检查输入文件是否存在
    if not os.path.exists(pdf_path):
        print(f"错误: PDF文件不存在: {pdf_path}")
        return False

    # 如果未指定输出路径，使用相同的文件名，只改变扩展名
    if docx_path is None:
        docx_path = str(Path(pdf_path).with_suffix('.docx'))

    try:
        print(f"开始转换: {pdf_path} -> {docx_path}")

        # 创建转换器对象
        cv = Converter(pdf_path)

        # 执行转换
        cv.convert(docx_path, start=start_page, end=end_page)

        # 关闭转换器
        cv.close()

        print(f"转换成功! 输出文件: {docx_path}")
        return True

    except Exception as e:
        print(f"转换失败: {str(e)}")
        return False


def batch_convert(input_dir, output_dir=None):
    """
    批量转换目录中的所有PDF文件

    参数:
        input_dir: 包含PDF文件的目录
        output_dir: 输出目录（可选，默认与输入目录相同）
    """
    if not os.path.isdir(input_dir):
        print(f"错误: 目录不存在: {input_dir}")
        return

    # 如果未指定输出目录，使用输入目录
    if output_dir is None:
        output_dir = input_dir
    else:
        # 确保输出目录存在
        os.makedirs(output_dir, exist_ok=True)

    # 查找所有PDF文件
    pdf_files = list(Path(input_dir).glob("*.pdf"))

    if not pdf_files:
        print(f"在目录 {input_dir} 中未找到PDF文件")
        return

    print(f"找到 {len(pdf_files)} 个PDF文件")

    success_count = 0
    for pdf_file in pdf_files:
        output_path = os.path.join(output_dir, pdf_file.stem + '.docx')
        if convert_pdf_to_docx(str(pdf_file), output_path):
            success_count += 1

    print(f"\n批量转换完成: {success_count}/{len(pdf_files)} 个文件成功转换")


def main():
    """命令行接口"""
    parser = argparse.ArgumentParser(
        description='将PDF文件转换为DOCX格式',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s input.pdf                    # 转换单个文件
  %(prog)s input.pdf -o output.docx     # 指定输出文件名
  %(prog)s input.pdf -s 0 -e 5          # 只转换第1到第5页
  %(prog)s --batch ./pdfs               # 批量转换目录中的所有PDF
  %(prog)s --batch ./pdfs -o ./docx     # 批量转换并指定输出目录
        """
    )

    parser.add_argument('input',
                       help='输入的PDF文件路径或目录（批量模式）')
    parser.add_argument('-o', '--output',
                       help='输出的DOCX文件路径或目录（批量模式）')
    parser.add_argument('-s', '--start-page',
                       type=int,
                       default=0,
                       help='起始页码（从0开始，默认为0）')
    parser.add_argument('-e', '--end-page',
                       type=int,
                       help='结束页码（默认为最后一页）')
    parser.add_argument('-b', '--batch',
                       action='store_true',
                       help='批量转换模式：转换目录中的所有PDF文件')

    args = parser.parse_args()

    # 批量转换模式
    if args.batch:
        batch_convert(args.input, args.output)
    else:
        # 单文件转换模式
        convert_pdf_to_docx(
            args.input,
            args.output,
            args.start_page,
            args.end_page
        )


if __name__ == "__main__":
    main()
