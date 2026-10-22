import streamlit as st
import json
import time

st.title("Simple Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
prompt = st.chat_input("Type your message ...")

if prompt:
    # Save and display user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)

    # Exercise 2: Typing indicator
    with st.chat_message("assistant"):
        with st.spinner("Assistant is typing..."):
            time.sleep(1)

            # Rule-based reply
            if "python" in prompt.lower():
                reply = (
                    "Python is a popular language "
                    "for AI and data science."
                )
            elif "streamlit" in prompt.lower():
                reply = (
                    "Streamlit is a Python framework "
                    "for interactive web apps."
                )
            else:
                reply = (
                    f"You said: '{prompt}'. "
                    "I'm a demo chatbot!"
                )

        st.write(reply)

    # Save assistant reply
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })

# Exercise 1: Download chat history
st.divider()

if st.session_state.messages:
    chat_text = "\n".join(
        f"{m['role']}: {m['content']}"
        for m in st.session_state.messages
    )

    st.download_button(
        label="Download Chat History",
        data=chat_text,
        file_name="chat_history.txt",
        mime="text/plain"
    )

# Clear chat
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()
