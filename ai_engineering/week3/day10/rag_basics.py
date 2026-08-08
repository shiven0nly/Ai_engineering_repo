import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Api key not found..")

client = Groq(api_key=my_api_key)
model='llama-3.3-70b-versatile'

# Step 1: knowledge base
knowledge_base={
    "age":"The age of shiven is 19 years",
    "Net_worth":"The network of shiven is 25lpa"
}

# Step 2: Retrieval
def retreive_info(ques):
    ques=ques.lower()
    if 'age' in ques:
        return knowledge_base['age']
    elif "net worth" in ques:
        return knowledge_base['Net_worth']
    else:
        return None

def ask_llm(ques) ->str:
    context=retreive_info(ques)
    sys_prompt=f"""
    answer in one line strictly.Answer according on the context donot hallucinate {context}
    """
    sys_msg={
        "role":"system",
        "content":sys_prompt
    }
    
    user_msg={
        "role":"user",
        "content":ques
    }
    messages=[user_msg,sys_msg]
    response=client.chat.completions.create(model=model,messages=messages)
    answer=response.choices[0].message.content
    return answer

quest="""How old is shiven?"""
# it throws the error that its not his database, the thing is because we have specified a very specific keyword 'age' but what is the age of shiven? and how old shiven is? are same questions but llm wont able to decide that, that's why only retrieval is very rigid system, we need something that solves this problem, so that llm will able to understand that 'networth' and 'how rich he is?' are the same questions.
print(ask_llm(quest))
# to solve the above problem, vector database and embeddings come into the picture.
     