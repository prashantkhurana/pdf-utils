from pypdf import PdfReader, PdfWriter, PdfMerger
import os

# read file
filesDir = '/Users/prashantkhurana/Downloads/reports/'
pdfFileMerger = PdfMerger()
writer = PdfWriter()

for filename in os.listdir(filesDir):
    if filename.endswith('.pdf'):
        pdfReader = PdfReader(filesDir + filename)
        pdfFileMerger.append(pdfReader)

pdfFileMerger.write("merged.pdf")