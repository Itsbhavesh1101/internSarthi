from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from backend.ml.recommender import InternshipRecommender

router = APIRouter()

# -------- Request Schema --------
class RecommendRequest(BaseModel):
    role: str
    user_skills: List[str]


# -------- Initialize Recommender --------
recommender = InternshipRecommender()


# -------- API Endpoint --------
@router.post("/recommend")
def recommend_internships(request: RecommendRequest):
    """
    Recommend internships based on:
    1. Job role name trace
    2. Related roles via skill similarity
    3. Per-internship skill gap
    """

    results = recommender.recommend(
        role=request.role,
        user_skills=request.user_skills
    )

    return results
