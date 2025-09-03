import streamlit as st
from transformers import pipeline

# QnA pipeline
qa = pipeline("question-answering", model="deepset/roberta-base-squad2")

# Text generation pipeline
generator = pipeline("text-generation", model="gpt2")

# Chat history
if "history" not in st.session_state:
    st.session_state.history = []

st.set_page_config(page_title="Advanced AI Chatbot", page_icon="🤖")
st.title("🤖 Advanced AI Chatbot")

st.write("Ask me anything in English or Marathi about college or general topics!")

# Context
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
    st.session_state.history.append(("You", user))
    college_keywords = ["exam", "fees", "library", "placement", "college", "canteen", "principal"]

    if any(word in user.lower() for word in college_keywords):
        answer = qa(question=user, context=context)
        bot_reply = answer["answer"]
    else:
        response = generator(user, max_length=60, num_return_sequences=1)
        bot_reply = response[0]["generated_text"]

    st.session_state.history.append(("Bot", bot_reply))

# Display chat history
for sender, msg in st.session_state.history:
    if sender == "You":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 Bot:** {msg}")
