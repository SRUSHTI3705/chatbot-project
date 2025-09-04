import streamlit as st
import sqlite3
import os

# Page config
st.set_page_config(page_title="🎓 College Chatbot", page_icon="🎓", layout="centered")

st.markdown("<h1 style='text-align: center; color: darkblue;'>🎓 College Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Search student info easily</p>", unsafe_allow_html=True)
st.write("---")

# Input box
roll = st.text_input("Enter Roll Number", placeholder="Type Roll Number here")
search_btn = st.button("🔍 Search")

# Database path
DB_FILE = os.path.join(os.path.dirname(__file__), "college.db")

# Function to get student info
def get_student(roll_no):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE roll_no=?", (roll_no,))
    student = cur.fetchone()
    conn.close()
    return student

# Display search result
if search_btn:
    student = get_student(roll)
    if student:
        st.success(f"✅ Student Found!")
        st.markdown(f"**Name:** {student[1]}")
        st.markdown(f"**Roll No:** {student[0]}")
        st.markdown(f"**Course:** {student[2]}")
        st.markdown(f"**Year:** {student[3]}")
    else:
        st.error("❌ No record found")
