import pandas as pd

DATASET_PATH = "data/internships.csv"

def extract_role_skills(role_keyword: str):
    """
    Extract unique required skills for a given role
    from the internships dataset.
    """
    df = pd.read_csv(DATASET_PATH)

    # Normalize text
    df["internship_title"] = df["internship_title"].astype(str).str.lower()
    df["required_skills"] = df["required_skills"].fillna("").astype(str).str.lower()

    # Match role keyword in internship title
    matched_roles = df[df["internship_title"].str.contains(role_keyword.lower())]

    skill_set = set()

    for skills in matched_roles["required_skills"]:
        for skill in skills.split(","):
            clean_skill = skill.strip()
            if clean_skill:
                skill_set.add(clean_skill)

    return sorted(list(skill_set))
