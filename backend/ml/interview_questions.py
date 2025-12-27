import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATASET_PATH = os.path.join(BASE_DIR, "data", "internships.csv")

def get_questions_for_role(role: str, limit: int = 5):
    df = pd.read_csv(DATASET_PATH)

    df["internship_title"] = df["internship_title"].astype(str).str.lower()
    df["required_skills"] = df["required_skills"].fillna("").astype(str).str.lower()

    role = role.lower()

    matched_rows = df[
        df["internship_title"].str.contains(role, na=False) |
        df["required_skills"].str.contains(role, na=False)
    ]


    skill_set = set()
    for skills in matched_rows["required_skills"]:
        for s in skills.split(","):
            s = s.strip()
            if s:
                skill_set.add(s)

    if not skill_set:
        return [
            "Tell me about yourself.",
            "What skills are you currently learning?",
            "Why are you interested in this role?"
        ]

    questions = []
    for skill in list(skill_set)[:limit]:
        questions.append(f"Explain your experience with {skill}.")

    return questions
