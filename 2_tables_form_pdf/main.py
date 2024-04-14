import camelot


pages = camelot.read_pdf("./28_tasks/MO1F-16CJ-2-28JG-40-1-WA-2_01-APR-2011_9_01-JUL-2022_COMP.PDF", pages="1-100")
print(pages)