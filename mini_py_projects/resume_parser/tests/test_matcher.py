import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mini_py_projects.resume_parser.matcher import (
    match_education,
    match_experience,
    match_projects,
    match_skills,
    required_resume,
)
from mini_py_projects.resume_parser.models import (
    Education,
    Experience,
    Projects,
    Resume,
)


class MatcherTests(unittest.TestCase):
    def setUp(self):
        self.resume = Resume(
            job_title="Software Engineer",
            name="Jane Doe",
            email="jane@example.com",
            phone="1234567890",
            skills=["python", "react", "git", "docker"],
            projects=[
                Projects(title="LLM Wrapper", technologies_used=["python", "fastapi"]),
                Projects(title="E-commerce", technologies_used=["react", "node"]),
            ],
            education=[
                Education(college="ABC University", degree="B.Tech", cgpa=8.2, percentage_12=78.0),
            ],
            experience=[
                Experience(total_years=2.5, company="OpenAI", role="Software Engineer"),
            ],
            certifications=["AWS Certified"],
            languages=["English", "Hindi"],
            summary="Experienced engineer",
        )

    def test_match_skills(self):
        result = match_skills(self.resume, required_resume["skills"])
        self.assertGreaterEqual(result["score"], 50)
        self.assertIn("python", result["matched"])

    def test_match_education(self):
        result = match_education(self.resume, required_resume["education"])
        self.assertTrue(result["matches"])
        self.assertGreaterEqual(result["score"], 50)

    def test_match_experience(self):
        result = match_experience(self.resume, required_resume["experience"])
        self.assertTrue(result["matches"])

    def test_match_projects(self):
        result = match_projects(self.resume, required_resume["projects"])
        self.assertGreaterEqual(result["score"], 50)
        self.assertIn("LLM Wrapper", result["matched"])


if __name__ == "__main__":
    unittest.main()
