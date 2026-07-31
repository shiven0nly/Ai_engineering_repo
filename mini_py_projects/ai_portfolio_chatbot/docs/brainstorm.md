# Objective:
An AI-powered portfolio where recruiters can chat with an AI version of me instead of reading my resume.

### Before creating folders, we will answer questions like:

1. What exactly are we building?
    - Ans: We are building an AI chatbot for resume, that anyone can ask about me from the AI chatbot, and AI will answer it by seeing the resume I uploaded.

2. Who will use it?
    - Ans: Mostly, HR assitants.

3. What are its core features?
    - Ans: HR / User can ask anyone question about me, and the chatbot will answer it throughly and honestly. HR can also also upload JD as pdf/docx to match the skills with the candidate and with memory management, HR / User can ask follow up questions easily.


### System Architecture:
1. Recruiter
2. Frontend
3. Backend
4. Prompt Builder
5. Groq API
6. Streaming
7. Frontend

### Data design:
What information AI needs?
- Candidate name
- Education
- Project
- Skills
- Experience
- Certification
- Achievements
- Social Link/Reference

### Backend design:
We have to think on?
1. What endpoints are needed?
2. WHat should each endpoint return?
3. Should responses stream?
4. How should errors be handled?

### Prompt Engineering:
- System prompt
- Context injection
- Candidate Profile
- Conversion history
- Safety rules
- Hallucination prevention

### Candidate Resume?
We need structed candidate data for it.
- What fields belong?
- Which fields are optional?
- How should projects be represented?
- How should skills be categorized?

*We can do them, by taking reference from our ['resume_parser project'](/mini_py_projects/resume_parser/)*


### Implementation:
1. Candidate data
2. Prompt builder
3. LLM Service
4. CLI Prototype
5. FASTAPI
6. Streaming
7. React Frontend
8. Memory
9. JD Matching
10. Deployment

### Repo structure:
- docs
- frontend/
- backend/
- README.md

### Design Order:
1. Architecture ->
2. System Flow ->
3. Data Model ->
4. Prompt Design ->
5. API Design ->
6. Folder Structure

#### Architecture Design:
**FLow:** React Frontend -> FastAPI Backend -> Prompt Builder -> Candidate Data ->Groq LLM API -> Conversation Memory (assistant)

#### Coding workflow:
**Flow:** Candidate JSON -> Candidate Loader -> Prompt Builder -> LLM Service -> CLI Prototype -> FastAPI -> Streaming -> React -> Memory -> JD Matching