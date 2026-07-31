# Functions:
# -> Read candidate JSON
# -> Return structured data

# Reading candidate json using pydantic

import json
from pathlib import Path
from typing import List, Optional
from pydantic import BaseModel

class PersonalInfo(BaseModel):
    full_name:str
    location:str
    email:str
    phone:str
    summary:str

class SocialLinks(BaseModel):
    linkedin:str
    github:str
    portfolio:str

class Education(BaseModel):
    institution:str
    degree:str
    duration:str
    cgpa:str
    
class TechnicalSkills(BaseModel):
    # technical skills are multiple that's why we store them in list
    languages: List[str]
    frontend: List[str]
    backend: List[str]
    databases: List[str]
    cloud_and_devops: List[str]
    ai_ml: List[str]
    tools: List[str]

class Skills(BaseModel):
    technical_skills:TechnicalSkills
    soft_skills: List[str] | None

class Experience(BaseModel):
    role:str | None
    organization:str | None
    location:str | None
    duration:str | None
    highlights:List[str] | None

class Projects(BaseModel):
    title: str
    year: str
    technologies: List[str]
    highlights: List[str]
    
# Summarizing everything here
class Candidate(BaseModel):
    personal_information: PersonalInfo
    social_links: SocialLinks
    education: List[Education]
    skills: Skills
    experience: List[Experience]
    projects: List[Projects]
    certifications: List[str]
    achievements: List[str]
    
# Loading and validating the JSON

def load_candidate_data(file_path: str) -> Candidate:
    with open(file_path, "r", encoding="utf-8") as file:
        json_content = file.read()
        return Candidate.model_validate_json(json_content)


def candidate_data():
    data_file = Path(__file__).resolve().parent.parent / "data" / "candidate.json"
    candidate = load_candidate_data(str(data_file))
    
    return candidate


if __name__ == "__main__":
    candidate_data()