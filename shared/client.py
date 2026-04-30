import os
from dotenv import load_dotenv
from google import genai  # google-genai >= 0.8

load_dotenv()


def get_client() -> genai.Client:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise EnvironmentError("GEMINI_API_KEY not set. Copy .env.example to .env and fill in your key.")
    return genai.Client(api_key=api_key)
