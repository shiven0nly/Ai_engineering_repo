# This is the file to brainstorm about the resume-parser project before writing the code

**So, Before starting we structure the project essentials**
`It is an LLM + NLP pipeline`

**FLOW:** Resume pdf -> Extract Text -> LLM -> Structured JSON -> Compare with JD -> Generate Score -> Show result

* LLM is only used for extraction.. Everything else is done by python.

---

* *Instead of writing one huge file we divide it into several multiple files*

**Resume-parser/**
- main.py
- parser.py
- extractor.py
- matcher.py
- scorer.py
- models.py
- utils.py

**resumes/**
- 
**outputs/**
-
- requirement.txt

---

#### Step 1: Resume input
* **Input:** resume.pdf or resume.docx
* **Functions:**
    1. load_pdf()  # pdfplumber / pymupdf 
    2. load_docx() # python-docx
    3. extract_text()
    4. output = resume_text

---

#### Step 2: LLM Extraction
* **We will ask GPT only to return:**
    1. Name
    2. Email
    3. Phone
    4. Skills
    5. Projects
    6. Experience
    7. Education
* *Return strictly the JSON only of the schema*

---

#### Step 3: Pydantic
* **We create a schema for resume extraction using pydantic like:**
```
    class Resume(BaseModel):
        name: str
        email: str
        phone: int
        skills: list[str]
        projects: list[str]
        experience: int
        education: list[str] # like class 12th, college cgpa

```
---

#### Step 4: HR Requirements
* **We create a json file for HR Requirement like:**
```
{
    "skills":["python","react","docker","git","linux"],
    "experience":2,
    "projects":["REST API", "MERN APPS" , "CRUD OPERATIONS", "PYTHON FLASK" , "FASTAPI"]
    "education": 7.5  #minimum cgpa

}
```
---

#### Step 5: Matching Engine
**Here, we do matching of keyword like:**
* *Candidate:*
    * Python
    * React
    * MongoDB

* *HR Requirements:*
    * Python
    * React
    * Docker
    * Git
    * Linux

* *Matching:*
    * Python : ok
    * React : ok
    * Docker : no
    * Git : no
    * Linux : Linux

* *Skill score:*
    2/5 = 40%

---

#### Step 6: Experience Matching

* *Candidate:*
    * 3 years

* *HR Requirements:*
    * 2 years

* *Score:*
    * 100% (cap at 100%)

---

#### Step 7: Project Matching
* *Candidate:*
    * Bank Management
    * News App
    * Portfolio

* *HR Requirements:*
    * Authentication
    * FastAPI

* Here LLM can help us as because , bank management app contains authentication, news app can use django fastapi based backend, even if its not written exactly.

---

#### Step 8: Final Score
*For Example:*
* **Skills:** 40%
* **Experience:** 100%
* **Projects:** 80%

**Weighted:**
    * Skills = 0.5
    * Experience = 0.2
    * Projects = 0.3

**FINAL SCORE:** 77%

---

#### STEP 9: Final Output
*Its json of the candidate:*
```
{
    "candidate_name":"Shiv",
    "email:"abc@gmail.com",
    "phone:0123456789,
    "experience":3,
    "match_score":77,
    "matched_skills":[
        ...
    ],
    "missing_skills":[
        ...
    ],
    "recommendation":"Shortlist"
}
```
---
### How to Run this locally
```
git clone https://github.com/shiven0nly/Ai_engineering_repo.git

code Ai_engineering_repo

cd mini_py_projects

cd resume_parser

.\.venv\Scripts\activate.ps1

streamlit run main.py

# to deactivate the server

deactivate
```

---

### Additional Features:
**We can add additional features to make this project more feature-rich:**
- [ ] Rank multiple resumes and show the Top 10 candidates.
- [ ] Highlight missing skills with suggestions.
- [ ] Export results to CSV/JSON.
- [ ] Add a small Streamlit UI for HR to upload resumes.
- [ ] Visualize scores with a bar chart (Matplotlib).
- [ ] Support multiple job descriptions.

### Author
**SHIVEN SHARMA**
