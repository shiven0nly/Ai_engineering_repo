import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
import numpy as np
from sentence_transformers import SentenceTransformer

def cosine_similarity(a,b):
    return np.dot(a,b)/(
        np.linalg.norm(a) * np.linalg.norm(b)
    )
        
model = SentenceTransformer("all-MiniLM-L6-V2") # 384 features vector
text = "Machine learning is fun."
res=model.encode(text)
print(res[:10])

v1="There are 25 paid leaves"
v2="There are 25 vacation days"
print(cosine_similarity(v1,v2))