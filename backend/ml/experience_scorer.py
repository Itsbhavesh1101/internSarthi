def calculate_experience_score(
    resume_skills: list,
    linkedin_skills: list,
    role_skills: list
):
    resume_skills = set([s.lower() for s in resume_skills])
    linkedin_skills = set([s.lower() for s in linkedin_skills])
    role_skills = set([s.lower() for s in role_skills])

    # Overlap with role
    resume_overlap = resume_skills & role_skills
    linkedin_overlap = linkedin_skills & role_skills

    score = 0

    if resume_overlap:
        score += min(len(resume_overlap) * 10, 20)

    if linkedin_overlap:
        score += min(len(linkedin_overlap) * 5, 15)

    return min(score, 25)  # max 25%
