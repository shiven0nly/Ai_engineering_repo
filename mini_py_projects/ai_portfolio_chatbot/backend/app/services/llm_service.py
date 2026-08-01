# Functions:
# -> Only communicate with Groq AI

import os
import sys
from pathlib import Path
import json

from groq import Groq

BACKEND_ROOT = Path(__file__).resolve().parents[2]
if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))

from app.services.memory import get_memory, store_memory
from app.services.prompt_builder import PROMPT
from app.services.candidate_loader import candidate_data
from app.services.jd_parser import parse_jd_to_json

try:
    from dotenv import load_dotenv
except ImportError: 
    def load_dotenv() -> bool:
        return False
    


load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=my_api_key) if my_api_key else None

model = "llama-3.3-70b-versatile"


def generate_response(user_message: str):
    if not client:
        return "GROQ API key is not configured."

    try:
        store_memory({"role": "user", "content": user_message})

        llm_messages = [{"role": "system", "content": PROMPT}]
        for entry in get_memory():
            if entry.get("role") in {"user", "assistant"} and entry.get("content"):
                llm_messages.append({"role": entry["role"], "content": entry["content"]})

        response = client.chat.completions.create(
            model=model,
            messages=llm_messages,
            temperature=0,
            stream=True,
        )

        assistant_parts = []
        for chunk in response:
            content = chunk.choices[0].delta.content or ""
            if content:
                assistant_parts.append(content)
                yield content

        full_response = "".join(assistant_parts).strip()
        if full_response:
            store_memory({"role": "assistant", "content": full_response})

    except Exception as exc:
        yield f"Unable to generate response: {exc}"


def generate_jd_match(jd: dict, user_message: str):
    # Analysis between candidate data and JD
    candidate_data_model = candidate_data()
    candidate_str = json.dumps(candidate_data_model.model_dump(), indent=2)
    jd_payload = json.dumps(jd, indent=2)

    prompt = f"""
    You are an Expert AI Technical Recruiter. Compare the candidate's resume with the Job Description provided below.
    
    <CANDIDATE_DATA>
    {candidate_str}
    </CANDIDATE_DATA>
    
    <JOB_DESCRIPTION>
    {jd_payload}
    </JOB_DESCRIPTION>
    
    # INSTRUCTIONS:
    Follow these instructions before returning the respone:
    1. Don't assume things from your side, or hallucinate, be honest. If candidate lacks in something and If some information is not clearly provided then mention it clearly.
    2. Provided the response 'Right-Aligned' instead of "Center-Aligned"
    3. Maintain proper spacing and tone.
    
    #TASK:
    Provide a detailed,structured match analysis formatted in Markdown:
    ### Match:
    - **Overall Match Score:**[X]%
    - **Short Summary:**[2-3 sentences on candidate fit]
    
    ### Key Matching Strengths & Skills:
    - Bullet points of direct skill matches, experience alignment, or hackathon/project alignments.
    
    ### Skill Gaps & Missing requirements:
    - Bullet points highlighting missing technical skills,domain knowledge gap, or unmet job requirements.
    
    ### Final Recommendation:
    - Clear hiring recommendation and potentional interview focus areas.
    
    """
    try:
        store_memory({"role": "user", "content": user_message})

        llm_messages = [{"role": "system", "content": PROMPT}]
        for entry in get_memory():
            if entry.get("role") in {"user", "assistant"} and entry.get("content"):
                llm_messages.append({"role": entry["role"], "content": entry["content"]})
                
        stream = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            stream=True,
        )
        
        assistant_parts = []
        for chunk in stream:
            content = chunk.choices[0].delta.content or ""
            if content:
                assistant_parts.append(content)
                yield content
            
        full_response = "".join(assistant_parts).strip()
        if full_response:
            store_memory({"role": "assistant", "content": full_response})
    
    except Exception as exc:
        yield f"Unable to analyze JD match: {exc}"
    
