from fastapi import APIRouter
from pydantic import BaseModel
from backend.ml.interview_questions import get_questions_for_role
from backend.ml.interview_evaluator import evaluate_answer

router = APIRouter(prefix="/interview", tags=["Interview"])

class QuestionRequest(BaseModel):
    role: str

class AnswerRequest(BaseModel):
    role: str
    answer: str

@router.post("/questions")
def get_questions(data: QuestionRequest):
    return {
        "questions": get_questions_for_role(data.role)
    }

@router.post("/evaluate")
def evaluate(data: AnswerRequest):
    return evaluate_answer(
        role=data.role,
        answer=data.answer
    )
