## Functional Requirements

### Chat System
- The system shall accept a user's question.
- The system shall send the question to the LLM.
- The system shall stream the response.
- The system shall preserve conversation history.

### Candidate Profile
- The system shall load candidate information.
- The system shall answer only from candidate data.
- The system shall refuse to invent information.

### Job Description Matching
- The system shall accept a job description.
- The system shall compare required skills with candidate skills.
- The system shall identify strengths.
- The system shall identify missing skills.
- The system shall provide a recommendation.

### Conversation Memory
- The system shall maintain previous messages.
- The system shall use previous context in future answers.

### Error Handling
- The system shall return friendly error messages.
- The system shall handle API failures gracefully.

## Non-Functional Requirements

- Fast response time
- Mobile responsive UI
- Streaming responses
- Secure API key handling
- Modular codebase
- Easy deployment
- Maintainable architecture