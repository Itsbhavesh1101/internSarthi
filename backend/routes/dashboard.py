from fastapi import APIRouter
from pydantic import BaseModel
from backend.ml.dashboard_state import (
    save_internship,
    apply_internship,
    add_interview_score,
    get_dashboard
)

router = APIRouter(prefix="/dashboard")

class InternshipAction(BaseModel):
    internship: str

class InterviewScore(BaseModel):
    score: int

@router.post("/save")
def save_item(data: InternshipAction):
    save_internship(data.internship)
    return {"message": "Internship saved"}

@router.post("/apply")
def apply_item(data: InternshipAction):
    apply_internship(data.internship)
    return {"message": "Internship marked as applied"}

@router.post("/interview-score")
def record_interview(score: InterviewScore):
    add_interview_score(score.score)
    return {"message": "Interview score recorded"}

@router.get("/")
def dashboard():
    return get_dashboard()
