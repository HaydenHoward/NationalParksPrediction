import requests 
import pandas as pd
from bs4 import BeautifulSoup as bs
import io
from PyPDF2 import PdfReader
import tabula as tb
import pdfquery
import pandas as pd
import re
import camelot

file = "DataGathering/NPS_2016_Visitor_Spending_Effects.pdf"

tables = camelot.read_pdf(file)
tables[0].df[1:3]


# data = tb.read_pdf(file, pages = [26,27,28,29,30,31,32,33,34,35,36,37,38,39])
# data = tb.read_pdf(file, pages = 26)

# pdf = pdfquery.PDFQuery(file)
# pdf.load()
# pdf.tree.write('pdfXML.txt', pretty_print = True)




































# url = "https://irma.nps.gov/DataStore/DownloadFile/575389"

# # read = requests.get(url)
# # html_content = read.content

# # soup = bs(html_content, "html.parser")

# def info(pdf_path):
 
#     # used get method to get the pdf file
#     response = requests.get(pdf_path)
 
#     # response.content generate binary code for
#     # string function
#     with io.BytesIO(response.content) as f:
 
#         # initialized the pdf
#         pdf = PdfReader(f)
 
#         # all info about pdf
#         information = pdf.metadata()
#         number_of_pages = pdf.getNumPages()
 
#     txt = f"""
#     Information about {pdf_path}:
     
#     Author: {information.author}
#     Creator: {information.creator}
#     Producer: {information.producer}
#     Subject: {information.subject}
#     Title: {information.title}
#     Number of pages: {number_of_pages}
#     """
#     print(txt)
     
#     return information

# info(url)