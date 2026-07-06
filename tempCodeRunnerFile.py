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
prompt="Do you know Virat Kohli ?"
message={
    "role":role,
    "content":prompt
}

messages=[message]

response=client.chat.completions.create(model=model, messages=messages)

print(response) # Here we get answer + usages

print("###########################")

answer=response.choices[0].message.content #this is how we only get the answer
print(answer)
