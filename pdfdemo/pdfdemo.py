from PyPDF4 import PdfFileReader
from PIL import Image

# 画像抽出用PDFを取得
pdf = open("etude1-4.pdf", "rb")
reader = PdfFileReader(pdf)

# ページ数を取得
page_count = reader.getNumPages()
print(page_count)