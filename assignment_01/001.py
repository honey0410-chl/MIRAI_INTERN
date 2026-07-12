import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GGEMINI_API_KEY")
client = genai.Client(api_key=api_key)
response = client.model.generate_content(
    model="gemini-2.3-flash",
    contents="Explain to me how does a gemini api works in one sentence"

)
print(response)