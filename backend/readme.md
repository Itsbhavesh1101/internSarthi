# internSarthi – AI-Powered Internship Recommendation System

internSarthi is an AI-driven internship recommendation platform designed to help students—especially those from rural or low-digital backgrounds—discover the most relevant internships based on their skills, interests, and career goals.  
The system provides personalized internship recommendations, identifies skill gaps, and helps users prepare for interviews.

---

## 🚀 Problem Statement

- Many students struggle to find suitable internships due to:
  - Lack of digital awareness and guidance
  - Overwhelming number of internship listings
  - Skill mismatch between student profiles and internship requirements
- There is no simple system that:
  - Matches internships intelligently
  - Highlights missing skills
  - Helps students prepare for interviews

---

## 💡 Proposed Solution

internSarthi provides a **lightweight AI-powered solution** that:

- Recommends internships based on:
  - Target roles
  - User skills
  - Skill similarity and relevance
- Identifies **skill gaps** for each internship
- Suggests **what to learn next**
- Tracks:
  - Saved internships
  - Applied internships
  - Interview practice history
- Offers **AI-based interview preparation and readiness scoring**

---

## 🧠 Is This an AI / ML Project?

✅ **Yes**

The project uses:
- Intelligent matching logic
- Skill similarity analysis
- Heuristic-based AI decision making
- Personalized recommendations
- Dynamic skill gap detection

Although it does not rely on deep learning models, it qualifies as an **Applied AI / ML system**, which is widely used in real-world industry products.

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- Tailwind CSS
- Vanilla JavaScript

### Backend
- Python
- FastAPI

### AI / Logic Layer
- Skill similarity analysis
- Rule-based recommendation engine
- Dynamic skill gap computation
- Interview readiness evaluation

### Data
- CSV-based dataset (`internships.csv`)

---

## 📂 Project Structure

```text
internSarthi/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   │
│   ├── ml/
│   │   ├── recommender.py
│   │   ├── skill_gap.py
│   │   ├── skill_gap_dynamic.py
│   │   ├── resume_parser.py
│   │   ├── linkedin_analyzer.py
│   │   ├── interview_evaluator.py
│   │   ├── interview_questions.py
│   │   ├── experience_scorer.py
│   │   ├── career_suggester.py
│   │   └── dashboard_state.py
│   │
│   ├── routes/
│   │   ├── recommend.py
│   │   ├── recommend_advanced.py
│   │   ├── internship_detail.py
│   │   ├── interview.py
│   │   ├── resume.py
│   │   ├── linkedin.py
│   │   └── skill_gap.py
│
├── data/
│   └── internships.csv
│
├── frontend/
│   ├── dashboard.html
│   ├── recommend.html
│   ├── internship_details.html
│   ├── skill_gap.html
│   ├── interview.html
│   └── profile.html
│
└── README.md

---


## ⚙️ How to Run Locally

Follow these steps to set up the project on your local machine.

### 1️⃣ Backend Setup

Open your terminal and navigate to the backend folder:
cd backend
--

###Create and activate a virtual environment:

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux / Mac)
source venv/bin/activate
--

###Install dependencies and run the server:

pip install -r requirements.txt

# Run the server on Port 8001
uvicorn main:app --reload --port 8001
--

### 2️⃣ Frontend Setup
1. Navigate to the frontend folder.

2. Open dashboard.html (or index.html) directly in your web browser.

3. Note: Ensure the backend is running at http://127.0.0.1:8001 for data to load correctly.
---

## 🔮 Future Enhancements

The project can be further improved by adding:

- Database integration (PostgreSQL / MongoDB)
- User authentication and profiles
- Resume upload and automatic parsing
- Real-time internship listings via APIs
- Advanced ML models for ranking and personalization
- Analytics dashboard for skill and career progress
- Cloud deployment with CI/CD

---

## 👨‍🎓 Ideal Use Cases

- College final-year or minor project
- AI / ML portfolio project
- Hackathons and innovation challenges
- Career guidance platforms
- Internship recommendation systems for institutions

---

## 🏁 Conclusion

internSarthi demonstrates how **AI-driven logic and data-based reasoning** can solve real-world career challenges.  
The project combines:

- Intelligent recommendation logic  
- Skill gap analysis  
- Clean and user-friendly UI  
- Practical career support features  

It is a strong example of an **applied AI/ML system** with real-world relevance.

---

## 📬 Author

**Bhavesh Barmashe**  
Bachelor of Computer Science Engineering  
AI / ML Enthusiast  

---

