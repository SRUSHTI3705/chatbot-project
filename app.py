import streamlit as st
from transformers import pipeline

# HuggingFace pipeline (question-answering model)
qa = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

st.set_page_config(page_title="Smart AI Chatbot", page_icon="🤖")
st.title("🤖 Smart AI Chatbot")

st.write("Hi! I am your AI chatbot. Ask me anything...")

# Context (you can expand this for college info or general knowledge)
context = """
Our college is located in Mumbai. The library is open from 9 AM to 7 PM.
Exams will start from 15th November. Fees can be paid online.
Placements are available for IT and Computer Engineering students.
"""

# user input
user = st.text_input("You: ")

if user:
    answer = qa(question=user, context=context)
    st.success(f"Bot: {answer['answer']}")

