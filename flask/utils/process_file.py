# checks the incoming file's extension and preps the data for pinecone
import os
import pytesseract
from pdf2image import convert_from_bytes
import textract
from PyPDF2 import PdfReader


def pdf(file):
    page_images = convert_from_bytes(file.read())
    # path, fileName = os.path.split(fileName)
    # fileBaseName, fileExtension = os.path.splitext(fileName)
    extracted_text_list = []
    for page_image in page_images:
        extracted_text = pytesseract.image_to_string(page_image).encode('utf-8')
        extracted_text_list.append(str(extracted_text))  # Add the text to the list

    # Concatenate all the extracted text into a single string
    full_text = ' '.join(extracted_text_list)
    print(full_text)

    return full_text


def docxlsx(fileName):
    text = textract.process(fileName)
    print(text)


def main(file):
    if file.filename.lower().endswith('.pdf'):
        print('it is pdf!')
        return pdf(file)     
    elif file.filename.lower().endswith(('.docx', '.xlsx')):
        print('it is docx or xlsx!')
        return docxlsx(file)
    elif file.filename.lower().endswith(('.png', '.jpg')):
        print('it is png or jpg!')
        return file
    else:
        return 0