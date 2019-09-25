import PyPDF2
pdf_file = open('../data/attendence.pdf', 'rb')
pdfreader = PyPDF2.PdfFileReader(pdf_file)

page = pdfreader.getPage(0).extractText() + "\n"
print(page)








