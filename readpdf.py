import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import BytesIO

def pdf_to_text(path):
    encoding = 'utf-8'
    manager = PDFResourceManager()
    #b = bytes()
    #retstr = BytesIO(b)
    retstr = open("C:/Users/backe/temp/temp.txt", 'w', encoding=encoding)
    layout = LAParams()
    device = TextConverter(manager, retstr, laparams=layout)
    filepath = open(path, 'rb')
    interpreter = PDFPageInterpreter(manager, device)

    for page in PDFPage.get_pages(filepath, check_extractable=True):
        interpreter.process_page(page)

    text = retstr

    filepath.close()
    device.close()
    retstr.close()
    #return text


#if __name__ == "__main__":
#    text = pdf_to_text("/home/jonas/git/parsermonitor/Webshop/Bekraftelser/checkup/elektroskandia/0203618.pdf")
#    print(text)
