import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
import numpy as np
from sentence_transformers import SentenceTransformer

def cosine_similarity(a,b):
    return np.dot(a,b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )
    
model = SentenceTransformer
("all-MiniLM-6-V2") # 384
load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")
groq_model="llama-3.3-70b-versatile"

# knowledge base:
documents = [
    "Employees receive 24 days of paid leave per year.",
   
    "Employees work from the office on Tuesday, Wednesday and Thursday. "
    "Monday and Friday are optional work-from-home days.",
   
    "Employees receive Rs 3000 per month for gym reimbursement.",
   
    "Employees can claim Rs 2000 per month for home internet.",
   
    "Employees have a 90 day notice period."
]

document_embeddings = model.encode(documents)

query = "How much vacation do I get?"
qembedding = model.encode(query)

def retrieval(qembedding):
    scores = []

    for i,document in document_embeddings:
        score = cosine_similarity(qembedding,document_embeddings)
        scores.append(score,document)
    scores.sort(reverse=True) # score and line return krega
    return scores[0]

score,context=retrieve(qembedding)
print(score)
print(context)
