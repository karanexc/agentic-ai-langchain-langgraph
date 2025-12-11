from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from langserve import add_routes
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

model = ChatGroq(model="llama-3.1-8b-instant",groq_api_key=groq_api_key)

### Prompt Templates
from langchain_core.prompts import ChatPromptTemplate

generic_template = "Translate the following into {language}:"

prompt = ChatPromptTemplate.from_messages([
    ("system", generic_template),
    ("user", "{text}")
])

parser = StrOutputParser()

## Create chain
chain = prompt | model | parser

## App definition

app = FastAPI(title = "LangChain Server", 
              version="1.0",
              description="Simple API server using LangChain runnable interfaces")

## Adding chain routes
add_routes(
    app,
    chain,
    path="/chain"
)

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1",port=8000)