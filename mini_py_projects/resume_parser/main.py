from pathlib import Path

try:
    from .extractor import extract_resume
    from .parser import extract_resume_text
    from .matcher import matched_resume
except ImportError:  # pragma: no cover - allows running the module directly
    from extractor import extract_resume
    from parser import extract_resume_text
    from matcher import matched_resume

try:
    from .report_generator import report
except ImportError:
    from report_generator import report


def choose_requirements_file():
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select requirements file",
        filetypes=[("PDF file", "*.pdf"), ("DOCX file", "*.docx")],
    )
    root.destroy()
    if not file_path:
        raise ValueError("No requirements file selected")
    return file_path


def main():
    resume_json = extract_resume()
    requirements_path = choose_requirements_file()
    requirements_text = extract_resume_text(requirements_path)
    resume_matching = matched_resume(resume_json, requirements_text)
    report(resume_matching)


if __name__ == "__main__":
    main()
