import fitz

file = fitz.open("docss\SQL Revision Notes.pdf")

docs = file.load_page()
print(docs)

