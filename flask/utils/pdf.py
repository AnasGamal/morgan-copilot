import pickle

# takes pdf file
# pass to ocr
# process the selectable pdf
# return it in text format
def process():
    print('Hello Process')
    # ocr()
    # pickler() ??

## takes pdf file, ocr it, return it in selectable pdf format
def ocr():
    print('Hello OCR')


## functions for pickle library
def pickler(unpickled):
    # process the data into pickle format
    with open("./data/case_docs.pkl", "wb") as f:
        pickle.dump(unpickled, f)
def unpickler():
    with open("./data/case_docs.pkl", "rb") as f:
        docs = pickle.load(f)
        from pprint import pprint
    print(f"{len(docs)} documents loaded")
    pprint(docs[8].page_content)