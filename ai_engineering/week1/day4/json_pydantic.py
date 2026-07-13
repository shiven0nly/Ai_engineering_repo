import json
import os
import re
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel


class customerTicket(BaseModel):
    name: str
    email: str
    issue: str


def extract_json_payload(content: str) -> dict:
    if not content:
        raise ValueError("The model returned an empty response.")

    cleaned = content.strip()

    if cleaned.startswith("```"):
        match = re.search(r"```(?:json)?\s*(\{.*\})\s*```", cleaned, re.S | re.I)
        if match:
            cleaned = match.group(1)

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", cleaned, re.S)
        if match:
            try:
                return json.loads(match.group(0))
            except json.JSONDecodeError as exc:
                raise ValueError("The model did not return valid JSON.") from exc
        raise


load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API Key not available")

client = Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"
role="user"
text="Hello, My name is Shiven Sharma and I have an iphone is not working at all. My addresh is delhi. My email is 'shiv@gmail.com' and my contact number is '978221233'."
prompt=f"""This is a customer ticket. Please extract personal information from this.{text}"""

# message: role and content
message={
    "role":role,
    "content":prompt
}

# Schema for json_object
schema = customerTicket.model_json_schema()
response_format = {"type": "json_object"}

# System prompt for LLM
system_prompt = f"""Extract the personal information from the ticket strictly based on this schema and return ONLY a JSON object matching it. Schema: {schema}"""

# System role for LLM
message_system={
    "role":"system",
    "content": system_prompt
}

messages=[message_system,message]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    response_format=response_format,
    temperature=0,
)

answer = response.choices[0].message.content
print(answer)

raw_json = answer
# we have to write extract_json_payload to get json_data from string
data_file = extract_json_payload(raw_json)
ticket = customerTicket(**data_file)
print(ticket.name)
print(ticket.email)
print(ticket.issue)

# homework on this:
# take resume in pdf or word
# have hr give you a list of things like skill, experience, projects
# extract these from resume
# match against the hr list
# generate a percentage of matching or not