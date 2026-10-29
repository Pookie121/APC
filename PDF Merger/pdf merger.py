
from pypdf import PdfMerger

m = PdfMerger()

m.append("1.pdf")
m.append("2.pdf")

m.write("merged.pdf")
m.close()

print("PDFs merged successfully!")
