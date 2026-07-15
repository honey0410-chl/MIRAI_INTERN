import streamlit as st
import requests
import random
from PIL import Image
from io import BytesIO
from urllib.parse import quote

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Image Studio",
    page_icon="🎨",
    layout="wide"
)

st.title("🎨 AI Image Studio")
st.caption("Create stunning AI-generated images using Pollinations AI")

# -----------------------------
# Sidebar Settings
# -----------------------------
st.sidebar.header("⚙️ Image Settings")

art_style = st.sidebar.selectbox(
    "Choose Art Style",
    [
        "Realistic",
        "Anime",
        "Cyberpunk",
        "Watercolor",
        "Pixel Art",
        "Fantasy",
        "Oil Painting"
    ]
)

width = st.sidebar.slider(
    "Image Width",
    min_value=256,
    max_value=1024,
    value=512,
    step=64
)

height = st.sidebar.slider(
    "Image Height",
    min_value=256,
    max_value=1024,
    value=512,
    step=64
)

# -----------------------------
# Task 3
# Magic Enhance Checkbox
# -----------------------------
magic = st.sidebar.checkbox(" Enable Magic Enhance")

# -----------------------------
# Prompt
# -----------------------------
user_prompt = st.text_area(
    "Enter your image prompt",
    placeholder="Example: Iron Man flying through the clouds..."
)

# -----------------------------
# Surprise Prompts
# -----------------------------
surprise_prompts = [
    "An astronaut riding a horse on Mars",
    "A cyberpunk street food vendor in Tokyo",
    "A dragon drinking coffee in a café",
    "A giant whale floating in the sky",
    "A futuristic underwater city with glowing fish"
]

col1, col2 = st.columns(2)

generate = col1.button("Generate Image")
surprise = col2.button(" Surprise Me!")

# -----------------------------
# Surprise Button Logic
# -----------------------------
if surprise:
    user_prompt = random.choice(surprise_prompts)
    st.success(f"Surprise Prompt: {user_prompt}")
    generate = True

# -----------------------------
# Generate Image
# -----------------------------
if generate:

    if user_prompt.strip() == "":
        st.warning("Please enter a prompt.")
        st.stop()

    # Combine prompt with style
    full_prompt = f"{user_prompt}, {art_style} style"

    # -----------------------------
    # Task 3
    # Magic Enhance
    # -----------------------------
    if magic:
        full_prompt += ", masterpiece, 8k resolution, highly detailed, trending on artstation, unreal engine 5 render"

    # Encode spaces properly
    encoded_prompt = quote(full_prompt)

    # -----------------------------
    # Task 1
    # Width & Height
    # -----------------------------
    url = (
        f"https://image.pollinations.ai/prompt/{encoded_prompt}"
        f"?width={width}&height={height}"
    )

    with st.spinner("Generating image..."):

        response = requests.get(url)

    if response.status_code == 200:

        image = Image.open(BytesIO(response.content))

        st.image(
            image,
            caption="Generated Image",
            use_container_width=True
        )

        # -----------------------------
        # Task 2
        # Dynamic File Name
        # -----------------------------
        filename = f"{art_style.lower().replace(' ','_')}_image.png"

        st.download_button(
            "⬇️ Download Image",
            data=response.content,
            file_name=filename,
            mime="image/png"
        )

    else:
        st.error("Image generation failed. Please try again.")