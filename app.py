import requests
import streamlit as st
from hf_assistant import query_hf_assistant

# Directory structure:
# Streamlit-Assistant/
# ├── app.py
# ├── requirements.txt
# └── hf_assistant.py

# 1. requirements.txt
# -------------------
# streamlit
# requests

# 2. hf_assistant.py

HF_CHAT_URL = "https://hf.co/chat/assistant/68455d278815bdbc636ee500"

def query_hf_assistant(message, history=None):
    # This is a placeholder. Replace with actual API endpoint and payload if available.
    # For demonstration, we simulate a response.
    # If HuggingFace provides an API endpoint, use requests.post with the correct headers and payload.
    # Example:
    # response = requests.post(HF_CHAT_API_URL, json={"inputs": message, "history": history or []})
    # return response.json()["generated_text"]
    return f"Echo: {message}"

# 3. app.py

st.set_page_config(page_title="HuggingFace Assistant", page_icon="🤖")

st.title("🤖 HuggingFace Assistant via Streamlit")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("You:", key="input")

if st.button("Send") and user_input:
    st.session_state.history.append({"role": "user", "content": user_input})
    response = query_hf_assistant(user_input, st.session_state.history)
    st.session_state.history.append({"role": "assistant", "content": response})

for chat in st.session_state.history:
    if chat["role"] == "user":
        st.markdown(f"**You:** {chat['content']}")
    else:
        st.markdown(f"**Assistant:** {chat['content']}")

# 4. To run:
# $ pip install -r requirements.txt
# $ streamlit run app.py