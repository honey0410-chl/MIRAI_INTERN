import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
import json
import requests
from PIL import Image
from io import BytesIO
from urllib.parse import quote
from gtts import gTTS

load_dotenv()

def parse_json(text):
    text = text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "")

    if text.endswith("```"):
        text = text[:-3]

    return json.loads(text.strip())

# Cache Gemini Client

@st.cache_resource
def get_gemini_client():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        st.error("GEMINI_API_KEY not found.")
        st.stop()

    return genai.Client(api_key=api_key)

client = get_gemini_client()


# Page Configuration

st.set_page_config(
    page_title="AI Visual Novel",
    page_icon="📖",
    layout="wide"
)

st.title("Multi-Modal Visual Novel")
st.caption("An AI-powered Choose Your Own Adventure Story")


# Sidebar

st.sidebar.header("Story Settings")

genre = st.sidebar.selectbox(
    "Story Genre",
    [
        "Fantasy",
        "Sci-Fi",
        "Horror",
        "Mystery",
        "Adventure"
    ]
)

art_style = st.sidebar.selectbox(
    "Art Style",
    [
        "Realistic",
        "Anime",
        "Fantasy Art",
        "Pixel Art",
        "Watercolor",
        "Cyberpunk"
    ]
)

if "history" not in st.session_state:
    st.session_state.history = []

if "chat" not in st.session_state:
    st.session_state.chat = None

if "started" not in st.session_state:
    st.session_state.started = False

if "story" not in st.session_state:
    st.session_state.story = None

if st.sidebar.button("🚀 Start New Story"):
    st.session_state.chat = None
    st.session_state.story = None
    st.session_state.history = []
    st.session_state.started = True
    st.rerun()

if st.sidebar.button("🔄 Restart Story"):
    st.session_state.chat = None
    st.session_state.story = None
    st.session_state.history = []
    st.session_state.started = True
    st.rerun()

if not st.session_state.started:

    st.info(
        """
###  Welcome!

Choose:

-  Story Genre
-  Art Style

Then click **Start New Story**.

Your adventure is waiting!
"""
    )

    st.stop()


SYSTEM_PROMPT = """
You are an AI Visual Novel Director.

Your job is to create an interactive story.

Always reply ONLY in valid JSON.

Do NOT wrap the JSON inside markdown code fences.

Do NOT use ```json.

Return raw JSON only.

Return exactly this format:

{
    "story_text":"...",
    "image_prompt":"...",
    "options":[
        "...",
        "...",
        "..."
    ]
}

Rules:

1. story_text should be around 80-120 words.

2. image_prompt should describe a beautiful cinematic scene suitable for AI image generation.

3. options must contain exactly 3 different choices.

4. Never include markdown.

5. Never include explanations.

6. Output ONLY JSON.
"""


# -----------------------------
# Start Story (Only Once)
# -----------------------------
if st.session_state.chat is None:

    st.session_state.chat = client.chats.create(
        model="gemini-2.5-flash"
    )

    opening_prompt = f"""
{SYSTEM_PROMPT}

Start a brand new {genre} adventure.

Use {art_style} for all visual descriptions.
"""

    response = st.session_state.chat.send_message(opening_prompt)

    try:
        story_data = parse_json(response.text)

        st.session_state.story = story_data
        st.session_state.history.append(story_data)

    except Exception:
        st.error("❌ Gemini returned invalid JSON.")
        st.stop()

# -----------------------------
# Display Story
# -----------------------------
left, right = st.columns([2, 1])

with left:
    st.subheader("📖 Story")
    st.markdown(st.session_state.story["story_text"])

with right:

    image_prompt = st.session_state.story["image_prompt"]

    encoded_prompt = quote(image_prompt)

    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"

    try:

        response = requests.get(url, timeout=20)

        if response.status_code == 200:

            image = Image.open(BytesIO(response.content))

            st.image(
                image,
                caption="Scene Illustration",
                use_container_width=True
            )

        else:

            st.toast("Image server is busy...")

    except Exception:

        st.toast("Image server is busy...")



# -----------------------------
# Narration (TTS)
# -----------------------------
story = st.session_state.story["story_text"]

try:

    audio_file = f"story_{len(st.session_state.history)}.mp3"

    tts = gTTS(text=story)

    tts.save(audio_file)

    st.subheader("🔊 Narration")

    st.audio(audio_file)

except Exception:
    st.toast("Audio generation failed.")

# -----------------------------
# Dynamic Choices
# -----------------------------
st.subheader("Choose Your Next Move")

col1, col2, col3 = st.columns(3)

options = st.session_state.story["options"]

for col, option in zip([col1, col2, col3], options):

    with col:

        if st.button(option, use_container_width=True):

            with st.spinner("Creating the next chapter..."):

                try:

                    response = st.session_state.chat.send_message(option)

                    story_data = parse_json(response.text)

                    st.session_state.story = story_data
                    st.session_state.history.append(story_data)

                    st.rerun()

                except Exception:

                    st.error("Couldn't continue the story.")





    