from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langserve import add_routes
import uvicorn
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
)

llm = Ollama(model="llama2")
prompt = ChatPromptTemplate.from_template("write me an essay about {subject} with 100 words")

add_routes(
    app,
    prompt|llm,
    path = "/essay"
)

if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8000)





