# so it takes resume.pdf / resume.docx -> python process -> extract text -> return text

# to pass a pdf or docx file in python we use pathlib

from pathlib import Path

def extract_resume_text(file_path: str):
    path = Path(file_path)
    # suffix gets the extension(.pdf, .docx)
    extension = path.suffix.lower()
    
    if extension == ".pdf":
        return extract_pdf(file_path)
        
    elif extension == ".docx":
        return extract_docx(file_path)
    else:
        raise SystemError
    
# to extract the text from pdf
import pymupdf
def extract_pdf(file_path):
    with pymupdf.open(file_path) as doc:
        text = "".join(page.get_text() for page in doc)
    return text
    

# to extract the text from docx
from docx import Document
def extract_docx(file_path):
    doc = Document(file_path)
    text = [para.text for para in doc.paragraphs]
    return "\n".join(text)
    
