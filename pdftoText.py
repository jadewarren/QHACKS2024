# importing required modules 
from PyPDF2 import PdfReader 

# creating a pdf reader object 
reader = PdfReader('/Users/jadewarren/Desktop/JadeWarren_Resume.pdf') 

# printing number of pages in pdf file 
print(len(reader.pages)) 

def clean_text(text):
    text = text.replace('\n', ' ')
    text = text.replace('\t', ' ')
    text = text.replace('\r', ' ')
    return text

# getting a specific page from the pdf file 
#page = reader.pages[0] 

# get all pages
for i in range(len(reader.pages)):
    page = reader.pages[i]
    text = page.extract_text()
    text = clean_text(text)
    print(text)

# extracting text from page 
# text = page.extract_text() 
# print(text) 
