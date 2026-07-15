import json
import os
import re
import time

try:
    from .models import Resume
    from .parser import extract_resume_text
except ImportError:  # pragma: no cover - allows running the module directly
    from models import Resume
    from parser import extract_resume_text

try:
    from dotenv import load_dotenv
except ImportError:  
    def load_dotenv():
        return False

try:
    from google import genai
    from google.genai import types
except ImportError:  # pragma: no cover - handled at runtime
    genai = None
    types = None


def choose_file():
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()

    print("Opening file selector window...")

    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[("PDF file", "*.pdf"), ("DOCX file", "*.docx")],
    )
    root.destroy()

    if not file_path:
        raise ValueError("No file selected")

    return file_path


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


def extract_resume(file_path=None):
    if file_path is None:
        file_path = choose_file()

    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY is not available")

    if genai is None or types is None:
        raise ImportError("google-genai is not installed. Run: pip install google-genai")

    text = extract_resume_text(file_path)
    schema = Resume.model_json_schema()

    prompt = f"""
    You are a resume extraction assistant.
    Extract the resume into a JSON object that strictly matches this schema:
    {schema}

    Resume text:
    {text}
    """

    client = genai.Client(api_key=api_key)
    models_to_try = ["gemini-3.5-flash", "gemini-3.0-flash","gemini-3.1-flash-lite","gemini-2.5-flash"]

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
                payload = _extract_json_payload(response_text)
                return Resume.model_validate(payload)
            raise ValueError("Gemini returned an empty response")
        except Exception as exc:  # broad catch to allow fallback on temporary service issues
            last_error = exc
            time.sleep(1)

    raise RuntimeError(f"Gemini request failed after retries: {last_error}")

