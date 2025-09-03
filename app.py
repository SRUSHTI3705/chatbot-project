import streamlit as st

st.set_page_config(page_title="College Chatbot", page_icon="🤖")

st.title("🤖 College Chatbot")

st.write("Hi! I am your Chatbot. Ask me anything about college.")

# user input
user = st.text_input("You: ")

# chatbot logic
if user:
    if "hello" in user.lower():
        st.success("Bot: Hi, How are you?")
    elif "exam" in user.lower():
        st.success("Bot: Exams will start from 15th Nov.")
    elif "fees" in user.lower():
        st.success("Bot: You can pay fees on the online portal.")
    elif "library" in user.lower():
        st.success("Bot: Library is open from 9 AM to 7 PM.")
    elif "bye" in user.lower():
        st.success("Bot: Bye! Have a nice day 🙂")
    else:
        st.error("Bot: Sorry, I don’t understand.")
