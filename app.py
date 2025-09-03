import streamlit as st
from transformers import pipeline

# QnA pipeline (for college related info)
qa = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# Text generation pipeline (for general questions)
generator = pipeline("text-generation", model="gpt2")

st.set_page_config(page_title="Hybrid AI Chatbot", page_icon="🤖")
st.title("🤖 Hybrid AI Chatbot")

st.write("Hi! I am your chatbot. Ask me anything about college or general questions.")

# College context
context = """
Our college is located in Mumbai.
The library is open from 9 AM to 7 PM.
Exams will start from 15th November.
Fees can be paid online through the student portal.
Placements are available for IT, Computer, and Electronics students.
Top recruiters include TCS, Infosys, and Wipro.
The principal of the college is Dr. Sharma.
The canteen serves food from 9 AM to 5 PM.
"""

# User input
user = st.text_input("You: ")

if user:
    # Simple rule: if question contains college keywords → use QnA
    college_keywords = ["exam", "fees", "library", "placement", "college", "canteen", "principal"]
    if any(word in user.lower() for word in college_keywords):
        answer = qa(question=user, context=context)
        st.success(f"Bot: {answer['answer']}")
    else:
        response = generator(user, max_length=50, num_return_sequences=1)
        st.success("Bot: " + response[0]['generated_text'])
