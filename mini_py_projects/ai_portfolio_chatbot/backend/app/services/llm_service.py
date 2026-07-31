# Functions:
# -> Only communicate with Groq AI

import os
import sys
from pathlib import Path

from groq import Groq

BACKEND_ROOT = Path(__file__).resolve().parents[2]
if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))

try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover
    def load_dotenv() -> bool:
        return False

from app.services.prompt_builder import PROMPT

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=my_api_key) if my_api_key else None

model = "openai/gpt-oss-120b"


def generate_response(user_message: str):
    if not client:
        return "GROQ API key is not configured. Please set GROQ_API_KEY in the backend .env file."

    try:
        messages = [
            {"role": "user", "content": user_message},
            {"role": "system", "content": PROMPT},
        ]
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0,
            stream=True
        )
# 2. Yield text tokens incrementally
        for chunk in response:
            content = chunk.choices[0].delta.content or ""
            if content:
                yield content

    except Exception as exc:
        yield f"Unable to generate response: {exc}"
