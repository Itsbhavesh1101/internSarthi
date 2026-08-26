import sys
import os
import pytest
from fastapi.testclient import TestClient

# Ensure root directory is in sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from backend.main import app

client = TestClient(app)

def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200

def test_recommend_endpoint():
    payload = {
        "role": "Data Analyst",
        "user_skills": ["python", "sql", "excel"]
    }
    response = client.post("/recommend", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if len(data) > 0:
        assert "internship_title" in data[0]
        assert "match_score" in data[0]
        assert "skills_you_have" in data[0]

def test_skill_gap_endpoint():
    payload = {
        "role": "Data Analyst",
        "user_skills": ["python", "sql"]
    }
    response = client.post("/skill-gap/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "skills_you_have" in data
    assert "skills_to_learn" in data
    assert "gap_percentage" in data

def test_interview_questions_endpoint():
    payload = {"role": "Data Analyst"}
    response = client.post("/interview/questions", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "questions" in data
    assert isinstance(data["questions"], list)

def test_interview_evaluator_endpoint():
    payload = {
        "role": "Data Analyst",
        "answer": "I use python for data cleaning and sql for database queries and statistics."
    }
    response = client.post("/interview/evaluate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "confidence_score" in data
    assert "matched_keywords" in data

def test_linkedin_analyzer_endpoint():
    payload = {
        "profile_text": "Experienced data analyst skilled in python, sql, and machine learning.",
        "target_role": "Data Analyst"
    }
    response = client.post("/linkedin/analyze", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "detected_skills" in data
    assert "missing_keywords" in data

def test_dashboard_endpoint():
    response = client.get("/dashboard/")
    assert response.status_code == 200
    data = response.json()
    assert "saved" in data
    assert "applied" in data
