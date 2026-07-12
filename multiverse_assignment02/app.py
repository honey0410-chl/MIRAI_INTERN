import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# ----------------------------
# Load API Key
# ----------------------------
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="The Multiverse of Chatbots",
    page_icon="🌌",
    layout="wide"
)

st.title("🌌 THE MULTIVERSE OF CHATBOTS")
st.caption("Talk to your favourite personalities.")

# ----------------------------
# Characters
# ----------------------------

characters = {
    "😡 Angry Ravi Shastri":
    "You are Ravi Shastri. Extremely loud, aggressive, passionate and always defending Indian cricket.",

    "🦸 Iron Man":
    "You are Tony Stark. Funny, sarcastic and genius.",

    "🦇 Batman":
    "You are Batman. Serious and mysterious.",

    "😂 Stand-up Comedian":
    "Answer every question like a stand-up comedian.",

    "👨‍🏫 Teacher":
    "Explain everything simply like a teacher."
}

selected = st.sidebar.selectbox(
    "Who do you want to talk to?",
    characters.keys()
)

# ----------------------------
# Memory
# ----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ----------------------------
# Display History
# ----------------------------

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ----------------------------
# Chat Input
# ----------------------------

if prompt := st.chat_input("Type your message..."):

    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    history = ""

    for msg in st.session_state.messages:

        if msg["role"] == "user":
            history += f"User: {msg['content']}\n"

        else:
            history += f"Assistant: {msg['content']}\n"

    final_prompt = f"""
You are roleplaying as:

{characters[selected]}

Conversation:

{history}

Reply as the assistant.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=final_prompt
    )

    reply = response.text

    with st.chat_message("assistant"):
        st.markdown(reply)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":reply
        }
    )