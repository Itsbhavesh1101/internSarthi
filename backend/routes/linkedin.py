from fastapi import APIRouter
from pydantic import BaseModel
from backend.ml.linkedin_analyzer import analyze_linkedin

router = APIRouter(prefix="/linkedin", tags=["LinkedIn"])

class LinkedInRequest(BaseModel):
    profile_text: str
    target_role: str

@router.post("/analyze")
def analyze(data: LinkedInRequest):
    return analyze_linkedin(
        text=data.profile_text,
        target_role=data.target_role
    )
