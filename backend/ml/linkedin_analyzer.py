import re

COMMON_SKILLS = [
    "python", "sql", "excel", "data analysis", "machine learning",
    "power bi", "tableau", "java", "c++", "javascript", "html", "css"
]

COMMON_ROLES = [
    "data analyst", "software engineer", "machine learning engineer",
    "web developer", "business analyst"
]


def analyze_linkedin(text: str, target_role: str):
    text = text.lower()

    found_skills = [s for s in COMMON_SKILLS if s in text]
    found_roles = [r for r in COMMON_ROLES if r in text]

    # Keywords missing for target role (simple heuristic)
    role_keywords = [k for k in COMMON_SKILLS if k not in found_skills]

    return {
        "detected_roles": found_roles,
        "detected_skills": found_skills,
        "missing_keywords": role_keywords[:5]  # keep it simple
    }
