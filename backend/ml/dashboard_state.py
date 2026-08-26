# Temporary in-memory dashboard storage
# Later this can be replaced with a database

USER_DASHBOARD = {
    "saved": [],
    "applied": [],
    "interview_scores": [],
    "completed_skills": []
}

def save_internship(internship):
    if internship not in USER_DASHBOARD["saved"]:
        USER_DASHBOARD["saved"].append(internship)

def apply_internship(internship):
    if internship not in USER_DASHBOARD["applied"]:
        USER_DASHBOARD["applied"].append(internship)

def add_interview_score(score):
    USER_DASHBOARD["interview_scores"].append(score)

def add_completed_skill(skill):
    if skill not in USER_DASHBOARD["completed_skills"]:
        USER_DASHBOARD["completed_skills"].append(skill)

def get_dashboard():
    return USER_DASHBOARD
