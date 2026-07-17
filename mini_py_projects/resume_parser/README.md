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