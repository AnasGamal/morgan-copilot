import pymongo
import os

mongo_user = os.getenv("MONGO_USER") or "MONGO_USER"
mongo_password = os.getenv("MONGO_PASS") or "MONGO_PASS"

client = pymongo.MongoClient("mongodb+srv://{mongo_user}:{mongo_password}@cluster0.lwvx13a.mongodb.net/?retryWrites=true&w=majority")
db = client['caseData']
collection = db['Case']

data_to_insert = {
    "Case": "2",
    "Data": 'test'
}

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