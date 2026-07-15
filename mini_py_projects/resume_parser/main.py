from pathlib import Path

try:
    from .extractor import extract_resume
except ImportError:  # pragma: no cover - allows running the module directly
    from extractor import extract_resume




def main():
    # extracting file
    resume_json=extract_resume()
    print(resume_json)
    


if __name__ == "__main__":
    main()
