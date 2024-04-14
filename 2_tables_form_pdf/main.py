import camelot


pages = camelot.read_pdf("file.pdf", pages="1-100")
print(pages)