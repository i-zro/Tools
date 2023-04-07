from pdf2docx import Converter
import sys
import re


if len(sys.argv)== 1:
    print ("USAGE: %s file.pdf", sys.argv[0])
print (sys.argv)

pdf_file = sys.argv[1]
docx_file = re.sub(".pdf", ".docx", pdf_file, flags=re.I)

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file, start=0, end=None)
cv.close()
