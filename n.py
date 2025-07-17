import fitz

file = fitz.open("docss\SQL Revision Notes.pdf")

docs = file.load_page(1)
text = docs.get_text()
print(text)

