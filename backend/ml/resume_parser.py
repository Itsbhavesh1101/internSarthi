import PyPDF2

KNOWN_SKILLS = [
    "python", "java", "c++", "c", "sql", "nosql", "mongodb", "postgresql",
    "html", "css", "javascript", "typescript", "react", "node", "express",
    "fastapi", "django", "flask", "tailwind", "bootstrap", "git", "github",
    "docker", "aws", "machine learning", "deep learning", "data analysis",
    "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch", "excel",
    "power bi", "tableau", "communication", "problem solving", "agile"
]

def analyze_resume(file):
    try:
        reader = PyPDF2.PdfReader(file)
        text_parts = []
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text_parts.append(extracted)
        text = " ".join(text_parts).lower()
    except Exception as e:
        return {
            "skills_found": [],
            "ats_score": 0,
            "error": "Could not extract text from PDF file. Please ensure it is a valid text-based PDF.",
            "suggestions": "Upload a readable text-based PDF resume (not a scanned image)."
        }

    found = [skill for skill in KNOWN_SKILLS if skill in text]
    
    # Calculate score based on found skills (benchmark: 5-8 key skills for strong entry level)
    target_skill_count = 6
    ats_score = min(int((len(found) / target_skill_count) * 100), 100) if found else 15

    missing_suggestions = []
    if "python" not in found and "javascript" not in found:
        missing_suggestions.append("Add core programming languages (e.g. Python, JavaScript)")
    if "git" not in found:
        missing_suggestions.append("Mention version control tools (Git / GitHub)")
    if "sql" not in found:
        missing_suggestions.append("Include database management skills (SQL, PostgreSQL)")

    suggestion_text = " • ".join(missing_suggestions) if missing_suggestions else "Great profile! Consider highlighting measurable project impacts."

    return {
        "skills_found": sorted(found),
        "ats_score": ats_score,
        "suggestions": suggestion_text
    }
