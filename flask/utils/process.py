# checks the incoming file's extension and preps the data for pinecone
import os
import pytesseract
from pdf2image import convert_from_path
import textract
import pymongo


client = pymongo.MongoClient("mongodb+srv://dbUser:<dbUserPassword>@cluster0.lwvx13a.mongodb.net/?retryWrites=true&w=majority")
db = client['caseData']
collection = db['Case']


def pdf(fileName):
    output = ''
    doc = convert_from_path(fileName)
    path, fileName = os.path.split(fileName)
    fileBaseName, fileExtension = os.path.splitext(fileName)

    for page_data in doc:
        txt = pytesseract.image_to_string(page_data).encode("utf-8")
        print(txt)
        output += str(txt)
    return output


def docxlsx(fileName):
    text = textract.process(fileName)
    print(text)
    return text

def insert_into_array(case_id, new_data):
    try:
        existing_document = collection.find_one({"_id": case_id})

        if existing_document:
            existing_document["Data"].append(new_data)
            collection.update_one({"_id": case_id}, {"$set": {"data":existing_document["data"]}})
            print("Data entered successfully")
        else:
            print("Document not found")
    except pymongo.errors.OperationFailure as e:
        print("an error occured:", e)
        print("error code:", e.code)
        print("error message:", e.details)
        print("max wire version support by the server:", e._max_wire_version)


def main(case_id, fileName):
    if fileName.lower().endswith('.pdf'):
        data = pdf(fileName)
    elif fileName.lower().endswith(('.docx', '.xlsx')):
        data = docxlsx(fileName)
    elif fileName.lower().endswith(('.png', '.jpg')):
        return fileName
    
    data_to_insert = {
        "Case": "2",
        "Data": data
    }
    insert_into_array(case_id, data)

    client.close()
    return 0

main("6520eee2fdba0a4cb5bed93d",'../data/sample.pdf')







