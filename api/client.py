import requests
import streamlit as st

def get_ollama_response(input_text):
    response = requests.post(
        "http://localhost:8000/essay/invoke",
        json={'input': {'subject': input_text}}  # Add 'input' key
    )
    # Print full response to check its structure
    print(response.json())
    return response.json().get('output', 'No output found in response')

# Streamlit framework
st.title("🤗 LLM-Pretice")
input_text = st.text_input("Enter your question")   

if input_text:
    st.write(get_ollama_response(input_text))
