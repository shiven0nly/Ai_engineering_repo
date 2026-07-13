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
text="Hello, My name is Shiven Sharma and I have an iphone is not working at all. My addresh is delhi. My email is 'shiv@gmail.com' and my contact number is '978221233'."
prompt=f"""This is a customer ticket. Please extract personal information from this.{text}"""
# SYSTEM
message_system={
    "role":"system",
    "content":"You are my college female classmate, who is alo my bench-partner"
}

# message: role and content
message={
    "role":role,
    "content":prompt
}

messages=[message_system,message]

# Temperature by default is 0 meaning safe
# groq temp go from 0 to 2 ,like 0 , 1 , 2

response=client.chat.completions.create(model=model, messages=messages, temperature=2)

print(response) # Here we get answer + usages

print("###########################")

answer=response.choices[0].message.content #this is how we only get the answer
print(answer)
