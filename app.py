import streamlit as st
from chatbot_engine import get_groq_response

st.set_page_config(page_title="Groq AI Chatbot", layout="centered")
st.title("⚡ Groq AI Chatbot")
st.caption("Internship Task 1: AI & Automation")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Render chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
if prompt := st.chat_input("Type your message here..."):
    # 1. Save & display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Get AI response with loading indicator
    with st.chat_message("assistant"):
        with st.spinner("Groq is thinking..."):
            response = get_groq_response(prompt)
        st.markdown(response)
    
    # 3. Save AI response to history
    st.session_state.messages.append({"role": "assistant", "content": response})