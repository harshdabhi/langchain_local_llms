## Importing libraries

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain import chains

## for running models locally 
from langchain_community.llms import Ollama

#import streamlit as st
import os


## for running models locally 
from langchain_community.llms import Ollama

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are helpful assistant and good at giving career advise"),
        ("user","Question:{question}")
    ]
)

llm=Ollama(model="Gemma3"
           ,base_url="http://host.docker.internal:11434")

output_parser=StrOutputParser()

chains=prompt|llm|output_parser 

chains.invoke({'question':'Enter the career question you want to ask? '})
