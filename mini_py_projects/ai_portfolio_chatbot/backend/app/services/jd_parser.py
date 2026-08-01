import io
import json
import os
import sys
from pathlib import Path

import fitz
from docx import Document
from groq import Groq

BACKEND_ROOT = Path(__file__).resolve().parents[2]
if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))

from app.models.jd import JobDescriptionSchema

try:
    from dotenv import load_dotenv
except ImportError:
    def load_dotenv() -> bool:
        return False

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_text_from_file(file_bytes:bytes,filename:str)->str:
    # checking the file-extension
    extract = filename.split(".")[-1].lower()
    
    # extracting text from pdf file
    if extract == "pdf":
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        text = "\n".join([page.get_text() for page in doc])
        return text.strip()
    
    elif extract in ["docx","doc"]:
        doc = Document(io.BytesIO(file_bytes))
        text="\n".join([para.text for para in doc.paragraphs if para.text.strip()])
        return text.strip()
    
    else:
        raise ValueError("Unsupported file format. Please upload PDF or DOCX")
    
def parse_jd_to_json(raw_text:str)->JobDescriptionSchema:
        #COnverts raw JD text into validated JSON via Groq and Pydantic.
        prompt=f"""
        Extract key information from the following Job Description into a clean JSON structure.
        JSON Structure required:
        {{
            "job_title":"...",
            "experience_level":"...",
            "required_skills":["skill1","skill2",..],
            "preferred_skills":["skill1","skill2",..],
            "key_responsibilities":["resp1","resp2",..],
            "education_requirements":"..."
        }}
        
        JOB DESCRIPTION CONTENT:
        {raw_text}
        
        Return Strictly raw JSON format without markdown code fences or conversational text.
        """
        
        response=client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[{"role":"user","content":prompt}],
            temperature=0
        )
        
        cleaned_json = response.choices[0].message.content.strip()

        if cleaned_json.startswith("```"):
            cleaned_json = cleaned_json.strip("`")
            if cleaned_json.lower().startswith("json"):
                cleaned_json = cleaned_json[4:].strip()

        raw_dict = json.loads(cleaned_json)

        # Validate with pydantic:
        return JobDescriptionSchema(**raw_dict)