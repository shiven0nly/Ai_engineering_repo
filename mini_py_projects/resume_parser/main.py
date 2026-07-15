import tempfile
from pathlib import Path

import streamlit as st

try:
    from .extractor import extract_resume
    from .parser import extract_resume_text
    from .matcher import matched_resume
except ImportError:  # pragma: no cover - allows running the module directly
    from extractor import extract_resume
    from parser import extract_resume_text
    from matcher import matched_resume


def _save_uploaded_file(uploaded_file):
    if uploaded_file is None:
        return None

    suffix = Path(uploaded_file.name).suffix or ".pdf"
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
        temp_file.write(uploaded_file.getbuffer())
        return temp_file.name


def main():
    st.set_page_config(page_title="Resume Evaluator", layout="wide")
    st.title("Resume Evaluator")
    st.caption("Upload a candidate resume and a requirements document to get a Gemini-based evaluation.")

    resume_file = st.file_uploader("Upload resume (PDF or DOCX)", type=["pdf", "docx"])
    requirements_file = st.file_uploader("Upload requirements (PDF or DOCX)", type=["pdf", "docx"])

    if st.button("Evaluate candidate", type="primary"):
        if resume_file is None or requirements_file is None:
            st.error("Please upload both a resume and a requirements file.")
            return

        with st.spinner("Parsing and evaluating the resume..."):
            resume_path = _save_uploaded_file(resume_file)
            requirements_path = _save_uploaded_file(requirements_file)

            resume_data = extract_resume(resume_path)
            requirements_text = extract_resume_text(requirements_path)
            result = matched_resume(resume_data, requirements_text)

        st.success("Evaluation complete")

        st.subheader("Candidate Information")
        info = result.get("personal_info", {})
        col1, col2, col3 = st.columns(3)
        col1.metric("Name", info.get("name") or "-")
        col2.metric("Email", info.get("email") or "-")
        col3.metric("Phone", info.get("phone") or "-")

        st.subheader("Overall Result")
        st.metric("Score", f"{result.get('score', 0)}/100")
        st.write(result.get("summary", ""))

        st.subheader("Strengths")
        for item in result.get("strengths", []):
            st.write(f"- {item}")

        st.subheader("Weaknesses")
        for item in result.get("weaknesses", []):
            st.write(f"- {item}")

        st.subheader("Missing Fields")
        for item in result.get("missing_fields", []):
            st.write(f"- {item}")

        st.subheader("Feedback")
        st.write(result.get("feedback", ""))


if __name__ == "__main__":
    main()
