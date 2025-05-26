import streamlit as st
import requests 

def get_llm1(input_text1):
    response = requests.post("http://localhost:8000/ollama1/invoke", json={"input": {"question": input_text1}})
    return response.json()['output']

def get_llm2(input_text2):
    response=requests.post("http://localhost:8000/ollama2/invoke", json={"input": {"question": input_text2}})
    return response.json()['output']


input_text1 = st.text_input("Question 1")
input_text2 = st.text_input("Question 2")

if input_text1:
    st.write(get_llm1(input_text1))

if input_text2:
    st.write(get_llm2(input_text2))
