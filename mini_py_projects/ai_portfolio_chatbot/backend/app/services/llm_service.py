# Functions:
# -> Only communicate with Groq AI

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq


try:
    from prompt_builder import PROMPT
except ImportError:
    from prompt_builder import PROMPT


load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API Key not available")

client = Groq(api_key=my_api_key)

model="openai/gpt-oss-120b"
user_prompt="""
Tell me about the user?
"""

msg_user={
    "role":"user",
    "content":user_prompt,
}
msg_sys={
        "role":"system",
        "content":PROMPT
}
def call_llm():
    messages=[msg_user,msg_sys]
    response=client.chat.completions.create(model=model, messages=messages,temperature=0)
    answer=response.choices[0].message.content 
    return answer

if __name__ == "__main__":
    call_llm()