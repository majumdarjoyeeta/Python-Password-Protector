#write ----- pip install PyPDF2-- in the terminal
from PyPDF2 import PdfWriter, PdfReader
import getpass  #it allows us for password typing..it makes hidden of whatever we are typing

reader = PdfReader("cv_JM.pdf")  #reader is an object , Pdfreader make the pdf compatible for reading
writer = PdfWriter()  #creating writer object
#encrypting the pdf and writing using writer object

for page in reader.pages:  #to access all the pages
    writer.add_page(page)  #if the pdf has 5 pages we will read it one by one
    
password = getpass.getpass(prompt="Enter the password for the pdf-------->>")  #asking the password using getpass
writer.encrypt(password)
with open('new.pdf', 'wb') as f : #creating new pdf
    writer.write(f)  #creating encrypted pdf
    

