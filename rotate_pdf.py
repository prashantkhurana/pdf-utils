from pypdf import PdfReader, PdfWriter

# read file
reader = PdfReader("input.pdf")
writer = PdfWriter()

# rotate alternate pages.
for page_num in range(len(reader.pages)) :
    page = reader.pages[page_num]
    if page_num % 2 : 
        writer.add_page(page.rotate(90))
    else :
        writer.add_page(page.rotate(270))  

# write file          
with open("output.pdf", "wb") as fp:
    writer.write(fp)