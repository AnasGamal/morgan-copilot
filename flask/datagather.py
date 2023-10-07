from bs4 import BeautifulSoup as Soup
from langchain.document_loaders.recursive_url_loader import RecursiveUrlLoader
import pickle
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from dotenv import load_dotenv

urls = ["https://docs.manim.community/en/stable/"]

# loader = RecursiveUrlLoader(url="https://docs.manim.community/en/stable/", max_depth=3, extractor=lambda x: Soup(x, "html.parser").text)
# docs = loader.load()

with open("manim_docs.pkl", "rb") as f:
    docs = pickle.load(f)
    from pprint import pprint
print(f"{len(docs)} documents loaded")
pprint(docs[8].page_content)


load_dotenv()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
split_docs = text_splitter.split_documents(docs)

db = Chroma.from_documents(split_docs, embedding=OpenAIEmbeddings())