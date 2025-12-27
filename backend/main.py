from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers
from backend.routes.recommend import router as recommend_router
from backend.routes.resume import router as resume_router
from backend.routes.skill_gap import router as skill_gap_router
from backend.routes.linkedin import router as linkedin_router
from backend.routes.interview import router as interview_router
from backend.routes.recommend_advanced import router as advanced_router
from backend.routes.dashboard import router as dashboard_router
from backend.routes.career import router as career_router
from backend.routes.linkedin import router as linkedin_router
from backend.routes.internship_detail import router as detail_router

# 1️⃣ Create app FIRST
app = FastAPI(title="internSarthi API")

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
app.include_router(linkedin_router)
app.include_router(detail_router)

# 4️⃣ Root test endpoint
@app.get("/")
def home():
    return {"status": "internSarthi backend running"}
