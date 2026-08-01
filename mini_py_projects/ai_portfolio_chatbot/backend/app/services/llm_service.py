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
except ImportError: 
    def load_dotenv() -> bool:
        return False
    
from app.services.memory import get_memory, store_memory
from app.services.prompt_builder import PROMPT

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=my_api_key) if my_api_key else None

model = "llama-3.3-70b-versatile"


def generate_response(user_message: str):
    if not client:
        return "GROQ API key is not configured."

    try:
        store_memory({"role": "user", "content": user_message})

        llm_messages = [{"role": "system", "content": PROMPT}]
        for entry in get_memory():
            if entry.get("role") in {"user", "assistant"} and entry.get("content"):
                llm_messages.append({"role": entry["role"], "content": entry["content"]})

        response = client.chat.completions.create(
            model=model,
            messages=llm_messages,
            temperature=0,
            stream=True,
        )

        assistant_parts = []
        for chunk in response:
            content = chunk.choices[0].delta.content or ""
            if content:
                assistant_parts.append(content)
                yield content

        full_response = "".join(assistant_parts).strip()
        if full_response:
            store_memory({"role": "assistant", "content": full_response})

    except Exception as exc:
        yield f"Unable to generate response: {exc}"
    
