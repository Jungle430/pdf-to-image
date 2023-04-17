import shutil
import fitz
import sys
import os

assert len(sys.argv) == 2

pdf_file = sys.argv[1]
pdf = fitz.open(pdf_file)
out_path = f"{pdf_file[:-4]}-image"

if os.path.exists(out_path):
    shutil.rmtree(out_path)
os.mkdir(out_path)

for page in range(pdf.page_count):
    curr_page = pdf.load_page(page)
    pix = curr_page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0))
    pix.save(f"{out_path}/{pdf_file[:-4]}-{page}.png")

pdf.close()
