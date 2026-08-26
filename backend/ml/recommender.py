import pandas as pd
import os
import re
from typing import List
from difflib import SequenceMatcher

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATASET_PATH = os.path.join(BASE_DIR, "data", "internships.csv")


def normalize_text(text: str) -> str:
    """
    Generic text normalization for job roles.
    No hard-coded role mappings.
    """
    text = text.lower()

    # Remove common noise words
    text = re.sub(r"\b(intern|trainee|junior|jr|associate)\b", "", text)

    # Remove plural / suffix variations
    text = re.sub(r"(ics|ist|ers|er|ing|s)$", "", text)

    # Remove non-alphabet characters
    text = re.sub(r"[^a-z\s]", "", text)

    return text.strip()


def similarity(a: str, b: str) -> float:
    """
    Fuzzy similarity between two normalized strings.
    """
    return SequenceMatcher(None, a, b).ratio()


class InternshipRecommender:
    def __init__(self):
        self.df = pd.read_csv(DATASET_PATH)

        self.df["internship_title"] = self.df["internship_title"].astype(str)
        self.df["required_skills"] = self.df["required_skills"].fillna("").astype(str)

        # Normalized columns ONLY for matching
        self.df["internship_title_norm"] = (
            self.df["internship_title"].str.lower()
        )
        self.df["required_skills_norm"] = (
            self.df["required_skills"].str.lower()
        )


    def _extract_skills_original(self, skills_str: str) -> list:
        return [s.strip() for s in skills_str.split(",") if s.strip()]

    def _extract_skills_lower(self, skills_str: str) -> set:
        return {s.strip().lower() for s in skills_str.split(",") if s.strip()}


    def recommend(self, role: str, user_skills: List[str]):
        user_skills = {s.lower() for s in user_skills}
        normalized_user_role = normalize_text(role)

        recommendations = []

        # ---------- STEP 1: IDENTIFY PRIMARY ROLE SKILLS ----------
        primary_role_skills_original = set()
        primary_role_skills_lower = set()

        for _, row in self.df.iterrows():
            normalized_title = normalize_text(row["internship_title_norm"])
            name_similarity = similarity(normalized_user_role, normalized_title)

            if name_similarity >= 0.6:
                orig = self._extract_skills_original(row["required_skills"])
                low = self._extract_skills_lower(row["required_skills"])

                primary_role_skills_original.update(orig)
                primary_role_skills_lower.update(low)


        # ---------- STEP 2: PROCESS EACH INTERNSHIP INDEPENDENTLY ----------
        for _, row in self.df.iterrows():
            orig_skills = self._extract_skills_original(row["required_skills"])
            low_skills = self._extract_skills_lower(row["required_skills"])

            if not orig_skills:
                continue

            normalized_title = normalize_text(row["internship_title"])
            name_similarity = similarity(normalized_user_role, normalized_title)

            # Primary match (name-based, generic)
            is_primary = name_similarity >= 0.6

            # Related role match (skill similarity ONLY with primary role)
            skill_overlap = (
                len(primary_role_skills_lower & low_skills) / len(primary_role_skills_lower)
                if primary_role_skills_lower else 0
            )


            is_related = skill_overlap >= 0.4

            if not (is_primary or is_related):
                continue

            # ---------- STEP 3: PER-INTERNSHIP SKILL GAP ----------
            skills_you_have = []
            skills_to_learn = []

            for skill in orig_skills:
                if skill.lower() in user_skills:
                    skills_you_have.append(skill)   # ORIGINAL CASE
                else:
                    skills_to_learn.append(skill)   # ORIGINAL CASE


            match_score = int(
                (len(skills_you_have) / len(orig_skills)) * 100
            )

            recommendations.append({
                "internship_title": row["internship_title"],
                "company_name": row.get("company_name", ""),
                "location": row.get("location", ""),
                "match_type": "primary" if is_primary else "related",
                "match_score": match_score,
                "required_skills": sorted(list(orig_skills)),
                "skills_you_have": skills_you_have,
                "skills_to_learn": skills_to_learn
            })

        # ---------- STEP 4: SORT RESULTS ----------
        recommendations.sort(
            key=lambda x: (
                0 if x["match_type"] == "primary" else 1,
                -x["match_score"]
            )
        )

        return recommendations
