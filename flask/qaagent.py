from langchain.chat_models import ChatOpenAI

chat = ChatOpenAI(model="gpt-4")

from langchain.pydantic_v1 import BaseModel, Field, validator
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser, OutputFixingParser

class DocsResponse(BaseModel):
    explanation: str = Field(description="The explanation answering the user's question")
    example: str = Field(description="A code example to support the explanation")

parser = PydanticOutputParser(pydantic_object=DocsResponse)
fixing_parser = OutputFixingParser.from_llm(parser=parser, llm=chat)

prompt_template = """You are an AI assistant helping a user with a question about writing code with Manim. Answer the user's question using the documentation below and provide a code example to support your explanation.

FORMAT: {format_instructions}

DOCUMENTATION:
{context}

REQUEST: 
{question}

Answer the user's question according to the FORMAT above:"""

PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"], partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain_type_kwargs = {"prompt": PROMPT}

from langchain.chains import RetrievalQA

qa_chain = RetrievalQA.from_chain_type(llm=ChatOpenAI(model="gpt-4"), chain_type="stuff", retriever=db.as_retriever(), chain_type_kwargs=chain_type_kwargs, return_source_documents=True)

answer = qa_chain({"query": "How can I animate a circle in Manim?"})

parsed_answer = fixing_parser.parse(answer['result'])

print(parsed_answer.explanation)
pprint(parsed_answer.example)
print(answer['source_documents'])