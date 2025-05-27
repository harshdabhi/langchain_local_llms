from fastapi import FastAPI
from langserve import add_routes
from langchain_community.llms import Ollama, OpenAI
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langchain.chains import LLMChain
from langchain.schema.runnable import RunnablePassthrough
import uvicorn
import os
import json
from pathlib import Path
from typing import Dict, Any

with open(Path.cwd().parent / "key.json", "r") as f:
    langchain_api_key = json.load(f)["langchain_api"]

#os.environ['OPEN_API_KEY']=os.getenv('open_api_key')
# for tracing using langsmith
os.environ['LANGCHAIN_TRACING_V2']='true'
os.environ['LANGCHAIN_API_KEY']=langchain_api_key

LANGSMITH_TRACING='true'
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
LANGSMITH_API_KEY=os.getenv('langchain_api_key')
LANGSMITH_PROJECT="pr-enchanted-almond-17"
#OPENAI_API_KEY="<your-openai-api-key>"

app = FastAPI(
    title="Ollama API",
    description="API for Ollama",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

llm1 = ChatOllama(model="Gemma3:1b", base_url="http://host.docker.internal:11434", temperature=0.2)

prompt1 = ChatPromptTemplate.from_template(
    "Answer the following question: {question}"
)

# Create a more explicit chain structure
def create_chain() -> Dict[str, Any]:
    chain = (
        {"question": RunnablePassthrough()}
        | prompt1
        | llm1
        | StrOutputParser()
    )
    return chain

chain = create_chain()

add_routes(
    app,
    chain,
    path="/ollama1",  # this define the path for the api
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080) 