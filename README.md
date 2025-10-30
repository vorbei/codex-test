# codex-test

这个仓库包含PDF转DOCX的转换工具。

## 工具版本

### pdf_to_docx_v2.py (推荐)
改进版工具，使用PyMuPDF提取文本，更稳定可靠。

### pdf_to_docx.py
原始版本，使用pdf2docx库进行转换。

## 功能特性

- 单个PDF文件转换为DOCX格式
- 批量转换目录中的所有PDF文件
- 支持指定页面范围进行转换
- 提取并保留PDF文本内容

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

### 基本用法

转换单个PDF文件（推荐使用v2版本）：

```bash
python pdf_to_docx_v2.py input.pdf
```

或使用原始版本：

```bash
python pdf_to_docx.py input.pdf
```

### 指定输出文件名

```bash
python pdf_to_docx.py input.pdf -o output.docx
```

### 转换指定页面范围

只转换第1到第5页（页码从0开始）：

```bash
python pdf_to_docx.py input.pdf -s 0 -e 5
```

### 批量转换

转换目录中的所有PDF文件：

```bash
python pdf_to_docx.py --batch ./pdfs
```

批量转换并指定输出目录：

```bash
python pdf_to_docx.py --batch ./pdfs -o ./docx
```

## 命令行参数

- `input`: 输入的PDF文件路径或目录（批量模式）
- `-o, --output`: 输出的DOCX文件路径或目录（批量模式）
- `-s, --start-page`: 起始页码（从0开始，默认为0）
- `-e, --end-page`: 结束页码（默认为最后一页）
- `-b, --batch`: 批量转换模式

## 示例

```bash
# 查看帮助信息
python pdf_to_docx.py --help

# 转换单个文件
python pdf_to_docx.py document.pdf

# 转换并重命名
python pdf_to_docx.py report.pdf -o final_report.docx

# 只转换前10页
python pdf_to_docx.py large_file.pdf -s 0 -e 10

# 批量转换
python pdf_to_docx.py --batch ./pdf_folder -o ./docx_output
```

