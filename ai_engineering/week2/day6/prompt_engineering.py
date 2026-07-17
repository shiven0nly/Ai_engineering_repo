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

def llm_res(prompt):
    message={
        "role":"user",
        "content":prompt
    }
    messages=[message]
    response=client.chat.completions.create(model=model,messages=messages)
    result=response.choices[0].message.content
    return result

bad_prompt="""This is a user complaint: My girlfriend ghosted me!! , handles this"""

#print(llm_res(bad_prompt))

# adding role to bad_prompt

bad_prompt2="""#ROLE: You are a support assistant at a mobile/laptop company.
This is a user complaint: 
My laptop is not working
Classify this.
"""
#print(llm_res(bad_prompt2))

# adding the task
bad_prompt3="""#ROLE: You are a support assistant at a mobile/laptop company.
#TASK:
You have to classify the issue in a category
This is a user complaint: 
My laptop is not working
Classify this.
"""
#print(llm_res(bad_prompt3))

# adding constraints
bad_prompt4="""#ROLE: You are a support assistant at a mobile/laptop company.
#TASK:
You have to classify the issue in a category.
#CONSTRAINT:
You have to classify the issue in one of three categories namely- billing,technical and return.
This is a user complaint: 
My girlfriend ghosted me from two weeks.
Classify this.
"""
#print(llm_res(bad_prompt4))

# adding output format
bad_prompt5="""#ROLE: You are a support assistant at a mobile/laptop company.
#TASK:
You have to classify the issue in a category.
#CONSTRAINT:
You have to classify the issue in one of three categories namely- billing,technical and return.
#OUTPUT FORMAT:
Give the answer in one word according to the categories given in the constraints.
This is a user complaint: 
I am not happy with my girlfriend.
Classify this.
"""

#print(llm_res(bad_prompt5))

#example (zeroshot/oneshot/fewshot)
bad_prompt6="""#ROLE: You are a support assistant at a mobile/laptop company.
#TASK:
You have to classify the issue in a category.
#CONSTRAINT:
You have to classify the issue in one of three categories namely- billing,technical and return.
#OUTPUT FORMAT:
Give the answer in one word according to the categories given in the constraints.
#EXAMPLE:
For instance if a user complain says he wants a refun then category is 'Return'
This is a user complaint: 
I am not happy with my girlfriend.I want Refund.
Classify this.
"""
#print(llm_res(bad_prompt6))

#adding fallback
bad_prompt7="""#ROLE: You are a support assistant at a mobile/laptop company.
#TASK:
You have to classify the issue in a category.
#CONSTRAINT:
You have to classify the issue in one of three categories namely- billing,technical and return.
#OUTPUT FORMAT:
Give the answer in one word according to the categories given in the constraints.
#EXAMPLE:
For instance if a user complain says he wants a refun then category is 'Return', if laptop is not working properly then category is 'Technical' and if amount deducted is not same as mentioned then the category is 'Billing'.
#FALLBACK:
If user complaint doesnt matches with anyone of the categories then return 'Sorry, but I can't help you with this'.
This is a user complaint: 
My marriage is broke.
Classify this.
"""
print(llm_res(bad_prompt7))