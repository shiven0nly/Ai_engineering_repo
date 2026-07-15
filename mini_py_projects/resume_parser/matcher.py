
required_skills = ["python", "React", "MERN", "Git", "Linux", "Docker"]
required_education = {
    "degrees": ["B.Tech", "Bachelor's of Technology"],
    "cgpa": 7.5,
    "percentage_12": 0.6,
}
required_experience = {"total_years": 2.0}
required_projects = ["LLM Wrapper", "E-commerce", "API Handling", "System Design"]

required_resume = {
    "skills": required_skills,
    "education": required_education,
    "experience": required_experience,
    "projects": required_projects,
}


def _get_value(resume, field_name, default=None):
    if isinstance(resume, dict):
        return resume.get(field_name, default)
    return getattr(resume, field_name, default)


def match_skills(resume, required_skills):
    resume_skills = _get_value(resume, "skills", []) or []
    resume_skills = [str(skill).lower() for skill in resume_skills]

    matched = []
    missing = []

    for skill in required_skills or []:
        if str(skill).lower() in resume_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    score = round((len(matched) / len(required_skills)) * 100, 2) if required_skills else 100.0
    return {"matched": matched, "missing": missing, "score": score, "matches": score >= 50}


def match_education(resume, required_education):
    education_list = _get_value(resume, "education", []) or []

    degrees = required_education.get("degrees", [])
    required_cgpa = required_education.get("cgpa")
    required_percentage = required_education.get("percentage_12")

    degree_match = False
    cgpa_match = False
    percentage_match = False

    for entry in education_list:
        if isinstance(entry, dict):
            degree = entry.get("degree")
            cgpa = entry.get("cgpa")
            percentage = entry.get("percentage_12")
        else:
            degree = getattr(entry, "degree", None)
            cgpa = getattr(entry, "cgpa", None)
            percentage = getattr(entry, "percentage_12", None)

        if degree and any(str(degree_value).lower() == str(degree).lower() for degree_value in degrees):
            degree_match = True
        if required_cgpa is not None and cgpa is not None and cgpa >= required_cgpa:
            cgpa_match = True
        if required_percentage is not None and percentage is not None and percentage >= required_percentage:
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
    experience_list = _get_value(resume, "experience", []) or []
    required_years = required_experience.get("total_years") if isinstance(required_experience, dict) else required_experience

    matched = False
    for entry in experience_list:
        if isinstance(entry, dict):
            years = entry.get("total_years")
        else:
            years = getattr(entry, "total_years", None)

        if years is not None and required_years is not None and years >= required_years:
            matched = True
            break

    return {"matches": matched, "score": 100.0 if matched else 0.0}


def match_projects(resume, required_projects):
    resume_projects = _get_value(resume, "projects", []) or []
    resume_project_titles = []

    for project in resume_projects:
        if isinstance(project, dict):
            title = project.get("title")
        else:
            title = getattr(project, "title", None)
        if title is not None:
            resume_project_titles.append(str(title).lower())

    matched = []
    missing = []

    for project in required_projects or []:
        if str(project).lower() in resume_project_titles:
            matched.append(project)
        else:
            missing.append(project)

    score = round((len(matched) / len(required_projects)) * 100, 2) if required_projects else 100.0
    return {"matched": matched, "missing": missing, "score": score, "matches": score >= 50}


def matched_resume(resume):
    skills = match_skills(resume, required_skills)
    projects = match_projects(resume, required_projects)
    experience = match_experience(resume, required_experience)
    education = match_education(resume, required_education)

    print(skills)
    print(projects)
    print(experience)
    print(education)
    return {"skills": skills, "projects": projects, "experience": experience, "education": education}
    