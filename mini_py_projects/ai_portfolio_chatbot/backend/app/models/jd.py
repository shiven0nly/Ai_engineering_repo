from typing import List, Optional
from pydantic import BaseModel

class JobDescriptionSchema(BaseModel):
    job_title:Optional[str]="Not Specified"
    experience_level: Optional[str]="Not Specified"
    required_skills: List[str]=[]
    preferred_skills:List[str]=[]
    key_responsibilities:List[str]=[]
    education_requirements:Optional[str]="Not Specified"