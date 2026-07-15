required_resume = {
    "skills": ["python", "React", "MERN", "Git", "Linux", "Docker"],
    "education": {
        "degrees": ["B.Tech", "Bachelor's of Technology"],
        "cgpa": 7.5,
        "percentage_12": 0.6,
    },
    "experience": {"total_years": 2.0},
    "projects": ["LLM Wrapper", "E-commerce", "API Handling", "System Design"],
}


def match_skills(resume, required_skills):
    resume_skills = [skill.lower() for skill in getattr(resume, "skills", []) or []]
    matched = []
    missing = []

    for skill in required_skills or []:
        if skill.lower() in resume_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    score = round((len(matched) / len(required_skills)) * 100, 2) if required_skills else 100.0
    return {"matched": matched, "missing": missing, "score": score, "matches": score >= 50}


def match_education(resume, required_education):
    education_list = getattr(resume, "education", []) or []

    degrees = required_education.get("degrees", [])
    required_cgpa = required_education.get("cgpa")
    required_percentage = required_education.get("percentage_12")

    degree_match = False
    cgpa_match = False
    percentage_match = False

    for entry in education_list:
        if entry.degree and any(degree.lower() == entry.degree.lower() for degree in degrees):
            degree_match = True
        if required_cgpa is not None and entry.cgpa is not None and entry.cgpa >= required_cgpa:
            cgpa_match = True
        if required_percentage is not None and entry.percentage_12 is not None and entry.percentage_12 >= required_percentage:
            percentage_match = True

    score = 0
    if degree_match:
        score += 50
    if cgpa_match:
        score += 25
    if percentage_match:
        score += 25

    return {"matches": score >= 50, "score": score, "degree_matched": degree_match}


def match_experience(resume, required_experience):
    experience_list = getattr(resume, "experience", []) or []
    required_years = required_experience.get("total_years") if isinstance(required_experience, dict) else required_experience

    matched = False
    for entry in experience_list:
        if entry.total_years is not None and required_years is not None and entry.total_years >= required_years:
            matched = True
            break

    return {"matches": matched, "score": 100.0 if matched else 0.0}


def match_projects(resume, required_projects):
    resume_projects = [project.title.lower() for project in getattr(resume, "projects", []) or []]
    matched = []
    missing = []

    for project in required_projects or []:
        if project.lower() in resume_projects:
            matched.append(project)
        else:
            missing.append(project)

    score = round((len(matched) / len            (required_projects)) * 100, 2) if required_projects else 100.0

    return {"matched": matched, "missing": missing, "score": score, "matches": score >= 50}