import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from time import sleep

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API KEy not available")

client = Groq(api_key=my_api_key)
model='llama-3.3-70b-versatile'

JD="""
We are hiring a Backend python Developer.

Requirements:
- Strong python
- FastAPI or Django
- PostgresSQL
- Docker
- AWS
- REST APIs
- 2+ years of experience

"""
RESUME="""
Name: Shiven Sharma

Experience:
3 years as a software Developer.

Skills:
Python,FastAPI,MySQL,Docker,REST APIs, Git

Projects:
Built a food delivery backend using FASTAPI and MySQL

Deployed applications using Docker.

"""
def ask_llm(system_prompt,user_prompt):
    sys_msg={
        "role":"system",
        "content":system_prompt
    }
    user_msg={
        "role":"user",
        "content":user_prompt
    }
    messages=[sys_msg,user_msg]
    response=client.chat.completions.create(model=model,messages=messages)
    answer=response.choices[0].message.content
    return answer

def step1_res_extract():
    # extract skills from resume
    system_prompt="""
    You are a professional HR assistant. Extract the skills from the candidates resume provided. Only return the skills no other informations. DO not invest any skilss by yourself.
    """
    user_prompt=f"""
    Extract the skills from this resume{RESUME}
    """
    return ask_llm(system_prompt,user_prompt)

def step2_res_extract():
    # extract skills from JD
    system_prompt="""
    You are a professional HR assistant. Extract the skills from the Job description provided. Only return the skills no other informations. DO not invest any skilss by yourself.
    # OUTPUT FORMAT:
    Skills should be seperated by comas. Just return comma seperated skills donot return any other filler information.
    """
    user_prompt=f"""
    Extract the skills from this resume{JD}
    """
    return ask_llm(system_prompt,user_prompt)

def step3_match(candidate,jd):
    system_prompt="""
    You are a professional HR assistant. Compare the skills of candidate and the skills required in the JD and produce a final board between 1 and 100, also produce a short verdict whether the candidate is a good fit for the role.
    """
    user_prompt=f"""
    Compare and match the skills:
    jd: {JD}
    Candidate Resume: {RESUME}
    """
    return ask_llm(system_prompt,user_prompt)    
    
candidate=step1_res_extract()
print(candidate)
sleep(2)
jd=step2_res_extract()
print(jd)
sleep(2)
score=step3_match(candidate,jd)
print(score)
# whenever calls is greater than one then always put the sleep, otherwise LLM will rate limit you