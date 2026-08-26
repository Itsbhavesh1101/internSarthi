import os
import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

# Ensure project root is in python path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# Import routers safely
try:
    from backend.routes.recommend import router as recommend_router
    from backend.routes.resume import router as resume_router
    from backend.routes.skill_gap import router as skill_gap_router
    from backend.routes.linkedin import router as linkedin_router
    from backend.routes.interview import router as interview_router
    from backend.routes.recommend_advanced import router as advanced_router
    from backend.routes.dashboard import router as dashboard_router
    from backend.routes.career import router as career_router
    from backend.routes.internship_detail import router as detail_router
except ModuleNotFoundError:
    from routes.recommend import router as recommend_router
    from routes.resume import router as resume_router
    from routes.skill_gap import router as skill_gap_router
    from routes.linkedin import router as linkedin_router
    from routes.interview import router as interview_router
    from routes.recommend_advanced import router as advanced_router
    from routes.dashboard import router as dashboard_router
    from routes.career import router as career_router
    from routes.internship_detail import router as detail_router

# 1️⃣ Create app FIRST
app = FastAPI(
    title="internSarthi API",
    description="AI-Powered Internship Recommendation, Skill Gap Analysis & Interview Preparation Platform",
    version="2.0.0"
)

# 2️⃣ Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3️⃣ Include routers AFTER app is created
app.include_router(recommend_router)
app.include_router(resume_router)
app.include_router(skill_gap_router)
app.include_router(linkedin_router)
app.include_router(interview_router)
app.include_router(advanced_router)
app.include_router(dashboard_router)
app.include_router(career_router)
app.include_router(detail_router)

# 4️⃣ Mount Frontend Static Files if available
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")
if os.path.exists(FRONTEND_DIR):
    app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

    @app.get("/")
    def read_root():
        index_file = os.path.join(FRONTEND_DIR, "index.html")
        if os.path.exists(index_file):
            return FileResponse(index_file)
        return {"status": "internSarthi backend running", "docs": "/docs"}
else:
    @app.get("/")
    def home():
        return {"status": "internSarthi backend running", "docs": "/docs"}

