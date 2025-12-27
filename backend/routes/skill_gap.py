from fastapi import APIRouter
from pydantic import BaseModel
from backend.ml.skill_gap import calculate_skill_gap

router = APIRouter(prefix="/skill-gap", tags=["Skill Gap"])

class SkillGapRequest(BaseModel):
    role: str
    user_skills: list[str]

@router.post("/")
def skill_gap(data: SkillGapRequest):
    return calculate_skill_gap(
        role=data.role,
        user_skills=data.user_skills
    )
