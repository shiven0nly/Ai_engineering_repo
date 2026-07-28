import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq


load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API Key not available")

client = Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"
role="user"
prompt="Explain how internet works?"
message={
    "role":role,
    "content":prompt
}

messages=[message]

# streaming the answer
stream=client.chat.completions.create(model=model,messages=messages,stream=True)

for chunk in stream:
    content=chunk.choices[0].delta.content
    if content:
        print(content,end="",flush=True)
        # flush=True (turant print, jese jese aate jaye usko print kro)