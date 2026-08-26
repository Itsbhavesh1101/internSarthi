def suggest_next_action(
    ats_score: int,
    skill_gap_percent: int,
    interview_scores: list,
    saved_internships: list,
    applied_internships: list
):
    # 1. Resume improvement
    if ats_score < 60:
        return {
            "action": "Improve Resume",
            "reason": "Your resume score is low. Improving it will increase shortlisting chances."
        }

    # 2. Skill gap learning
    if skill_gap_percent > 40:
        return {
            "action": "Learn Missing Skills",
            "reason": "You are missing important skills required for your target role."
        }

    # 3. Interview practice
    if interview_scores and sum(interview_scores) / len(interview_scores) < 60:
        return {
            "action": "Practice Mock Interviews",
            "reason": "Your interview confidence score is low."
        }

    # 4. Apply internships
    if saved_internships and len(applied_internships) < len(saved_internships):
        return {
            "action": "Apply to Internships",
            "reason": "You have saved internships but have not applied yet."
        }

    # 5. Default
    return {
        "action": "Keep Progressing",
        "reason": "You are on the right track. Keep applying and learning."
    }
