from fastapi import APIRouter
from pydantic import BaseModel

from backend.ml.recommender import InternshipRecommender
from backend.ml.experience_scorer import calculate_experience_score
from backend.ml.skill_gap import calculate_skill_gap

router = APIRouter(prefix="/recommend-advanced")

recommender = InternshipRecommender()


class AdvancedRequest(BaseModel):
    user_skills: list[str]
    resume_skills: list[str]
    linkedin_skills: list[str]
    role: str

@router.post("/")
def advanced_recommend(data: AdvancedRequest):

    base_results = recommender.recommend(data.user_skills)

    gap_result = calculate_skill_gap(
        role=data.role,
        user_skills=data.user_skills
    )

    role_skills = gap_result["skills_you_have"] + gap_result["skills_to_learn"]

    enhanced = []

    for item in base_results:
        exp_score = calculate_experience_score(
            resume_skills=data.resume_skills,
            linkedin_skills=data.linkedin_skills,
            role_skills=role_skills
        )

        item["experience_score"] = exp_score
        item["final_score"] = min(item["match_score"] + exp_score, 100)
        item["reason"] = "Based on skills and your past experience"

        enhanced.append(item)

    return enhanced
