import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# ----------------------------
# Load API Key
# ----------------------------
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ GEMINI_API_KEY not found in .env file")
    st.stop()

client = genai.Client(api_key=api_key)

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
        "You are Tony Stark. Funny, sarcastic, confident and genius.",

    "🦇 Batman":
        "You are Batman. Serious, mysterious and speak like Gotham's Dark Knight.",

    "😂 Stand-up Comedian":
        "Answer every question like a stand-up comedian. Make people laugh while still being helpful.",

    "👨‍🏫 Teacher":
        "Explain everything simply like a friendly teacher."
}

selected = st.sidebar.selectbox(
    "🎭 Who do you want to talk to?",
    list(characters.keys())
)

# ----------------------------
# Intensity Slider
# ----------------------------

st.sidebar.subheader("🔥 Character Intensity")

intensity = st.sidebar.slider(
    "Intensity",
    min_value=1,
    max_value=10,
    value=5,
    step=1
)

st.sidebar.write(f"Current Intensity: **{intensity}/10**")

# ----------------------------
# Memory Vault
# ----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ----------------------------
# Clear Chat Button
# ----------------------------

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# ----------------------------
# Render Chat History
# ----------------------------

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ----------------------------
# Chat Input
# ----------------------------

if prompt := st.chat_input("Say something..."):

    # Save User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Display User Message
    with st.chat_message("user"):
        st.markdown(prompt)

    # ----------------------------
    # Build Conversation History
    # ----------------------------

    history = ""

    for msg in st.session_state.messages:

        if msg["role"] == "user":
            history += f"User: {msg['content']}\n"

        else:
            history += f"Assistant: {msg['content']}\n"

    # ----------------------------
    # Final Prompt
    # ----------------------------

    final_prompt = f"""
You are roleplaying as:

{characters[selected]}

Character Intensity: {intensity}/10

Intensity Guide:

1-3:
Behave mostly like a normal AI with slight hints of the character.

4-6:
Clearly show the character's personality while remaining informative.

7-8:
Strongly stay in character with matching tone, vocabulary and emotions.

9-10:
Completely become the character.
Never break character unless explicitly asked.

Previous Conversation:

{history}

Continue the conversation naturally while remembering everything above.

Assistant:
"""

    # ----------------------------
    # Gemini Response
    # ----------------------------

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=final_prompt
        )

        reply = response.text

    except Exception as e:

        reply = f"❌ Error: {e}"

    # Display Assistant Message
    with st.chat_message("assistant"):
        st.markdown(reply)

    # Save Assistant Message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )