
import json
import os
import re
import time

try:
    from dotenv import load_dotenv
except ImportError:
    def load_dotenv():
        return False

try:
    from google import genai
    from google.genai import types
except ImportError:
    genai = None
    types = None


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


def _extract_json_payload(text: str):
    text = text.strip()
    text = re.sub(r"```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```", "", text)

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group(0))
        raise ValueError("Gemini response was not valid JSON")


def personal_info(resume):
    if isinstance(resume, dict):
        return {
            "name": resume.get("name"),
            "email": resume.get("email"),
            "phone": resume.get("phone"),
        }

    return {
        "name": getattr(resume, "name", None),
        "email": getattr(resume, "email", None),
        "phone": getattr(resume, "phone", None),
    }


def _call_gemini(prompt: str):
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is not available")

    if genai is None or types is None:
        raise ImportError("google-genai is not installed. Run: pip install google-genai")

    client = genai.Client(api_key=api_key)
    models_to_try = ["gemini-3.5-flash", "gemini-3.0-flash", "gemini-3.1-flash-lite", "gemini-2.5-flash"]

    last_error = None
    for model_name in models_to_try:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0,
                    response_mime_type="application/json",
                ),
            )
            response_text = getattr(response, "text", "") or ""
            if response_text:
                return _extract_json_payload(response_text)
            raise ValueError("Gemini returned an empty response")
        except Exception as exc:
            last_error = exc
            time.sleep(1)

    raise RuntimeError(f"Gemini request failed after retries: {last_error}")


def match_resume_with_gemini(resume, requirements_text: str):
    info = personal_info(resume)

    resume_text = ""
    if isinstance(resume, dict):
        resume_text = json.dumps(resume, indent=2)
    else:
        resume_text = json.dumps(
            {
                "name": getattr(resume, "name", None),
                "email": getattr(resume, "email", None),
                "phone": getattr(resume, "phone", None),
                "job_title": getattr(resume, "job_title", None),
                "degree": getattr(resume, "degree", None),
                "skills": getattr(resume, "skills", None),
                "projects": getattr(resume, "projects", None),
                "education": getattr(resume, "education", None),
                "experience": getattr(resume, "experience", None),
                "summary": getattr(resume, "summary", None),
            },
            indent=2,
            default=str,
        )

    prompt = f"""
    You are an expert recruiter and technical evaluator.

    Evaluate this candidate resume against the job requirements below.
    Be thoughtful and semantic, not just keyword-based. If a project or skill is indirectly related, give credit.

    Requirements text:
    {requirements_text}

    Candidate resume:
    {resume_text}

    Return JSON with this exact structure:
    {{
      "score": 0-100,
      "summary": "short evaluation summary",
      "strengths": ["..."],
      "weaknesses": ["..."],
      "missing_fields": ["..."],
      "feedback": "detailed feedback"
    }}
    """

    result = _call_gemini(prompt)
    return {
        "personal_info": info,
        "score": result.get("score", 0),
        "summary": result.get("summary", ""),
        "strengths": result.get("strengths", []),
        "weaknesses": result.get("weaknesses", []),
        "missing_fields": result.get("missing_fields", []),
        "feedback": result.get("feedback", ""),
    }


def matched_resume(resume, requirements_text=None):
    if requirements_text is None:
        requirements_text = "".join(
            [
                "Evaluate the candidate for a software engineering role. Prefer candidates with strong Python, React, MERN, Git, Docker, system design, API development, and B.Tech or equivalent education.",
                "Experience of at least 2 years is preferred.",
            ]
        )

    return match_resume_with_gemini(resume, requirements_text)
    