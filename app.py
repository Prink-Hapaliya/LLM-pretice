from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# os. environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that translates {input_language} to {output_language}."),
        ("user", "Question: {question}")
    ]
)

# streamlit framework
st.title("🤗 LLM-Pretice")
input_text = st.text_input("Enter your question")

# LLM
llm = Ollama(model="llama2")
output_parser = StrOutputParser()

# Chain
chain = prompt|llm|output_parser

if input_text:
    input_language = "English"  # or get this value from user input
    output_language = "English"  # or get this value from user input
    st.write(chain.invoke({"question": input_text, "input_language": input_language, "output_language": output_language}))
