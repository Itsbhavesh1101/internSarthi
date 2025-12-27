from fastapi import APIRouter, UploadFile, File
from backend.ml.resume_parser import analyze_resume

router = APIRouter(prefix="/resume")

@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    return analyze_resume(file.file)
