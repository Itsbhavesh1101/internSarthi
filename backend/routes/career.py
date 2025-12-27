from fastapi import APIRouter
from pydantic import BaseModel
from backend.ml.career_suggester import suggest_next_action
from backend.ml.dashboard_state import USER_DASHBOARD

router = APIRouter(prefix="/career")

class CareerInput(BaseModel):
    ats_score: int
    skill_gap_percent: int

@router.post("/suggest")
def get_career_suggestion(data: CareerInput):
    return suggest_next_action(
        ats_score=data.ats_score,
        skill_gap_percent=data.skill_gap_percent,
        interview_scores=USER_DASHBOARD["interview_scores"],
        saved_internships=USER_DASHBOARD["saved"],
        applied_internships=USER_DASHBOARD["applied"]
    )
