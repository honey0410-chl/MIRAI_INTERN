# 📖 Multi-Modal Visual Novel

An AI-powered **Choose Your Own Adventure** application built with **Streamlit**, **Google Gemini 2.5 Flash**, **Pollinations AI**, and **Google Text-to-Speech (gTTS)**.

The application generates an interactive story where every decision changes the narrative. Each scene includes AI-generated text, an AI-generated illustration, and narrated audio, creating an immersive visual novel experience.

---

## ✨ Features

- 📖 AI-generated interactive storytelling using Gemini 2.5 Flash
- 🎭 Multiple story genres
- 🎨 Multiple art styles
- 🖼️ AI-generated scene illustrations using Pollinations AI
- 🔊 Text-to-Speech narration using gTTS
- 🎮 Dynamic choice buttons generated from structured JSON
- 💾 Stateful storytelling using Streamlit Session State
- ⚡ Cached Gemini client using `@st.cache_resource`
- 🛡️ Graceful error handling with `try...except`

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini API
- Pollinations AI
- gTTS (Google Text-to-Speech)
- Requests
- Pillow
- JSON

---

## 📂 Project Structure

```
Multi-Modal-Visual-Novel/
│
├── app.py
├── .env
└── requirements.txt
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd Multi-Modal-Visual-Novel
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

### 4. Run the application

```bash
streamlit run app.py
```

---

## 🎮 How to Use

1. Select a **Story Genre** from the sidebar.
2. Choose an **Art Style**.
3. Click **Start New Story**.
4. Read the generated story.
5. View the AI-generated illustration.
6. Listen to the narrated story.
7. Select one of the available choices.
8. Continue exploring your adventure.

---

## 🧠 How It Works

1. The user selects a genre and art style.
2. Gemini generates a structured JSON response containing:
   - `story_text`
   - `image_prompt`
   - `options`
3. The JSON is parsed into a Python dictionary.
4. The `image_prompt` is sent to Pollinations AI to generate a scene illustration.
5. The `story_text` is converted into speech using gTTS.
6. Dynamic buttons are created from the `options` list.
7. The selected option is sent back to Gemini to continue the story.

---

## 📸 Demo

The application demonstrates:

- Interactive storytelling
- AI-generated illustrations
- Dynamic UI generation
- JSON parsing
- Text-to-Speech narration
- Stateful conversation

---

## 📦 Requirements

```
streamlit
google-genai
python-dotenv
requests
Pillow
gTTS
```

---

## 🚀 Future Improvements

- Save generated images locally
- Story history panel
- Background music
- Character avatars
- Download complete story as PDF
- Multiple save slots

---

## 👨‍💻 Author

**Honey Chilhate**

B.Tech Information Technology Student

---

## 🙏 Acknowledgements

This project was developed as part of the **Virtual Summer Internship 2026 – AI Builder Track** by **MirAI School of Technology**.

Special thanks to the mentors and instructors for providing guidance throughout the internship.
