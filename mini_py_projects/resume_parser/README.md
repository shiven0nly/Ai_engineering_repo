## Problem
Recruiters manually review hundreds of resumes...

## Solution

An AI-powered ATS that extracts structured resume data,
compares it against job requirements,
scores the candidate,
and generates actionable feedback.

### Architecture

**FLOW:**
```
Resume pdf -> Paser -> LLM + Pydantic -> Structured Resume JSON -> Matcher -> Candidate Score + FeedBack -> Streamlit Dashboard

```

### Tech Stack

- Python
- Gemini
- Pydantic
- PyMuPDF
- python-docx
- Streamlit

### Features

- PDF & DOCX Support
- Structured Resume Extraction
- Job Description Parsing
- Candidate Matching
- AI Feedback
- ATS Score
---

**You can learn more about the project by going to the below link:-**
[setting_up_project.md](https://github.com/shiven0nly/Ai_engineering_repo/blob/main/mini_py_projects/resume_parser/setting_up_project.md)
