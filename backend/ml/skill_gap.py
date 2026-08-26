import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATASET_PATH = os.path.join(BASE_DIR, "data", "internships.csv")


def calculate_skill_gap(role: str, user_skills: list):
    df = pd.read_csv(DATASET_PATH)

    df["internship_title"] = df["internship_title"].astype(str).str.lower()
    df["required_skills"] = df["required_skills"].fillna("").astype(str).str.lower()

    role = role.lower()
    user_skills = [s.lower() for s in user_skills]

    matched_rows = df[
    df["internship_title"]
    .str.lower()
    .str.contains(role.lower(), na=False)
    ]


    role_skills = set()
    for skills in matched_rows["required_skills"]:
        for s in skills.split(","):
            s = s.strip()
            if s:
                role_skills.add(s)

    skills_you_have = [s for s in role_skills if s in user_skills]
    skills_to_learn = [s for s in role_skills if s not in user_skills]

    gap_percentage = (
        int((len(skills_to_learn) / len(role_skills)) * 100)
        if role_skills else 0
    )

    return {
        "skills_you_have": skills_you_have,
        "skills_to_learn": skills_to_learn,
        "gap_percentage": gap_percentage
    }
