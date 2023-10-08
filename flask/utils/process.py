# checks the incoming file's extension and preps the data for pinecone
import os
import pytesseract
from pdf2image import convert_from_path
import textract


def pdf(fileName):
    doc = convert_from_path(fileName)
    path, fileName = os.path.split(fileName)
    fileBaseName, fileExtension = os.path.splitext(fileName)

    for page_data in doc:
        txt = pytesseract.image_to_string(page_data).encode("utf-8")
        print(txt)


def docxlsx(fileName):
    text = textract.process(fileName)
    print(text)


def main(fileName):
    if fileName.lower().endswith('.pdf'):
        pdf(fileName)     
    elif fileName.lower().endswith(('.docx', '.xlsx')):
        docxlsx(fileName)
    elif fileName.lower().endswith(('.png', '.jpg')):
        return fileName
    else:
        return 0

main('../data/sample.xlsx')



























# import pickle

# # takes pdf file
# # pass to ocr
# # process the selectable pdf
# # return it in text format
# def process():
#     print('Hello Process')
#     # ocr()
#     # pickler() ??

# ## takes pdf file, ocr it, return it in selectable pdf format
# def ocr():
#     print('Hello OCR')


# ## functions for pickle library
# def pickler(unpickled):
#     # process the data into pickle format
#     with open("./data/case_docs.pkl", "wb") as f:
#         pickle.dump(unpickled, f)
# def unpickler():
#     with open("./data/case_docs.pkl", "rb") as f:
#         docs = pickle.load(f)
#         from pprint import pprint
#     print(f"{len(docs)} documents loaded")
#     pprint(docs[8].page_content)