import PyPDF2

KNOWN_SKILLS = [
    "python", "java", "sql", "machine learning",
    "data analysis", "html", "css", "javascript"
]

def analyze_resume(file):
    reader = PyPDF2.PdfReader(file)
    text = " ".join(
        page.extract_text() for page in reader.pages
    ).lower()

    found = [skill for skill in KNOWN_SKILLS if skill in text]
    ats_score = int((len(found) / len(KNOWN_SKILLS)) * 100)

    return {
        "skills_found": found,
        "ats_score": ats_score,
        "suggestions": "Add more technical skills and project details"
    }
