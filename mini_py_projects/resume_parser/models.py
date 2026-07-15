from pydantic import BaseModel
from typing import List

class Education(BaseModel):
    college: str
    degree: str
    cgpa: float | None = None
    percentage_12: float | None = None
    
class Experience(BaseModel):
    total_years: float | None = None
    company: str | None = None
    role: str | None = None
    
class Projects(BaseModel):
    title: str
    technologies_used: List[str] | None = None
    
class Resume(BaseModel):
    job_title: str | None = None
    name: str
    email: str
    phone: str
    degree:str
    skills: List[str]
    projects: List[Projects]
    education: List[Education]
    experience: List[Experience]
    certifications: List[str]
    languages: List[str] | None = None
    summary: str

