import os
import shutil
from fpdf import FPDF

Ruta = 'C:/Users/exgciud/Desktop/Python'
Filename = 'test.pdf'

if not os.path.exists(Ruta):
    os.makedirs(Ruta)

os.chdir(Ruta)

pdf = FPDF()
pdf.add_page()
pdf.set_xy(0, 0)
pdf.set_font('arial', 'B', 13.0)
pdf.cell(ln=0, h=5.0, align='L', w=0, txt="Archivo Dummy para que proceso de control M no se cancele", border=0)
pdf.output(Filename, 'F')


aaaaaaaaaaaaaaaa