import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATASET_PATH = os.path.join(BASE_DIR, "data", "internships.csv")

def evaluate_answer(role: str, answer: str):
    answer = answer.lower()

    df = pd.read_csv(DATASET_PATH)
    df["internship_title"] = df["internship_title"].str.lower()
    df["required_skills"] = df["required_skills"].fillna("").str.lower()

    role_rows = df[df["internship_title"].str.contains(role.lower(), na=False)]

    role_skills = set()
    for skills in role_rows["required_skills"]:
        for s in skills.split(","):
            s = s.strip()
            if s:
                role_skills.add(s)

    matched = [s for s in role_skills if s in answer]
    missing = [s for s in role_skills if s not in answer]

    score = int((len(matched) / len(role_skills)) * 100) if role_skills else 50

    feedback = []
    if matched:
        feedback.append("You mentioned relevant concepts.")
    if missing:
        feedback.append("Try mentioning tools and techniques related to the role.")

    return {
        "matched_keywords": matched,
        "missing_keywords": missing,
        "confidence_score": score,
        "feedback": feedback
    }
