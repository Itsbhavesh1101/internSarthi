from fastapi import APIRouter, Query
import pandas as pd
import os

router = APIRouter()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATASET_PATH = os.path.join(BASE_DIR, "data", "internships.csv")


@router.get("/internship-detail")
def get_internship_detail(
    title: str = Query(...),
    company: str = Query(...)
):
    df = pd.read_csv(DATASET_PATH)

    # ✅ KEEP ORIGINAL CASE (DO NOT TOUCH)
    df["internship_title"] = df["internship_title"].astype(str)
    df["company_name"] = df["company_name"].astype(str)

    # ✅ CREATE TEMP NORMALIZED COLUMNS FOR MATCHING ONLY
    df["internship_title_norm"] = df["internship_title"].str.lower()
    df["company_name_norm"] = df["company_name"].str.lower()

    row = df[
        (df["internship_title_norm"] == title.lower()) &
        (df["company_name_norm"] == company.lower())
    ]

    if row.empty:
        return {"error": "Internship not found"}

    # ✅ RETURN ORIGINAL DATASET VALUES
    return row.iloc[0][[
        "internship_title",
        "company_name",
        "location",
        "start_date",
        "duration",
        "stipend",
        "required_skills"
    ]].to_dict()
