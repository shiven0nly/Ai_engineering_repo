# AI Portfolio Assistant

An AI-powered portfolio website that allows recruiters to interact with a virtual version of the candidate through natural conversation.

Instead of reading a static resume, recruiters can ask questions, analyze job descriptions, and receive AI-generated insights about the candidate.

## Project Overview:
Traditional resumes are static and require recruiters to manually search for relevant information. This project transforms a candidate portfolio into an AI-powered assistant capable of answering questions, maintaining conversational context, and evaluating job descriptions against the candidate's profile.

## Features:
- AI-powered portfolio chat
- Streaming responses
- Conversation memory
- Job Description matching
- Suitability score
- Voice-to-text input
- Structured candidate profile
- Modern Responsive UI
- Auto-Scroll while streaming

## Features remain:
- [] Copy AI response
- [] Clear chat
- [] Save chat history after refresh.

## Architecture:
React Frontend
  |
FastAPI Backend
  |
  | - Candidate loader
  | - Prompt Builder
  | - Memory Manager
  | - Chat Service
  | _ JD Matching Service
        |
      Groq API

## Tech Stack:
- **Frontend:** React, JavaScript, CSS
- **Backend:** FastAPI, Python
- **AI Models:** Llama-3.3-70b-versatile, openai/gpt-oss-120b
- **LLM Provider:** Groq API
- **Validation:** Pydantic (BaseModel)
- **Speech Recognition:** window.SpeechRecognition
- **Deployment:** Vercel

## Data Flow:

Recruiter -> React UI -> POST /chat -> FastAPI -> Prompt Builder -> Memory -> Groq -> Streaming Response -> React

## Installation:
```
git clone https://github.com/shiven0nly/Ai_engineering_repo

# for backend
cd mini_py_project
cd ai_portfolio_chatbot
cd backend
uvicorn app.main:app --reload

# open new terminal for frontend
cd mini_py_project
cd ai_portfolio_chatbot
cd frontend
npm run dev

# now it will start both backend and frontend servers.
```

### Environment vairiables
GROQ_API_KEY=your_groq_api_key_here
CHAT_MODEL=llama-3.3-70b-versatile
JD_MODEL=openai/gpt-oss-120b

### Future Improvements:

- [] Resume upload for dynamic candidate profiles
- [] Authentication
- [] Persistent chat history
- [] Multi-language support
- [] Text-to-Speech
- [] PDF export
---

### What I learned:
1. Desigining a modular FastAPI backend.
2. Building streaming AI responses.
3. Managing conversation memory.
4. Integrating multiple LLMs for different tasks.
5. Creating responsive React interface.
6. Using browser Speech Recognition APIs.
7. Structuring prompts for reliable AI responses.

---
### Author:
**Name:** *Shiven Sharma*
