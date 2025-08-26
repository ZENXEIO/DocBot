# docbot_backend/disease_prediction.py

import os
import re
import json
from typing import List, Tuple, Optional

import pandas as pd
import google.generativeai as genai

# --- Config ---
os.environ.setdefault("GEMINI_API_KEY", "AIzaSyDBKa6VG-6euP_X2zMjxF3UgOnIIRs45ek")
MODEL_NAME = "gemini-2.5-flash"
CONFIDENCE_THRESHOLD = 60.0

# --- Dataset ---
DF_PATH = "E:/My Things/Working Projects/docbot_project/data/ready_dataset.csv"
df = pd.read_csv(DF_PATH)
allowed_diseases = sorted(df["label"].unique())

# --- Gemini setup ---
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel(
    MODEL_NAME,
    generation_config={"response_mime_type": "application/json"}
)

# ---------------- Helpers ----------------

def _strip_code_fences(text: str) -> str:
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?", "", text).strip()
    if text.endswith("```"):
        text = text[:-3].strip()
    return text

def _parse_gemini_output(text: str):
    """Extract list of {disease, confidence} objects."""
    if not text:
        return []
    text = _strip_code_fences(text)
    try:
        j = json.loads(text)
        if isinstance(j, dict) and "disease" in j and "confidence" in j:
            return [j]
        if isinstance(j, list):
            return [x for x in j if "disease" in x and "confidence" in x]
    except Exception:
        pass
    matches = re.findall(r"\{.*?\}", text, flags=re.DOTALL)
    out = []
    for m in matches:
        try:
            obj = json.loads(m)
            if "disease" in obj and "confidence" in obj:
                out.append(obj)
        except Exception:
            continue
    return out

def _symptom_match_percent(disease: str, symptom_list: List[str]) -> float:
    rows = df[df["label"] == disease]
    if rows.empty:
        return 0.0
    symp_df = rows.drop(columns=["label"])
    disease_symptoms = set(symp_df.columns[symp_df.any(axis=0)])
    matched = len(set(symptom_list) & disease_symptoms)
    return (matched / len(symptom_list)) * 100 if symptom_list else 0.0

def _prevalence(disease: str) -> int:
    return int((df["label"] == disease).sum())

# ---------------- Main ----------------

def predict_disease(symptom_list: List[str]) -> Tuple[Optional[str], Optional[float], Optional[List[Tuple[str, float]]]]:
    if not symptom_list:
        return None, None, None

    user_syms = [s.strip().lower() for s in symptom_list if s.strip()]
    symptoms_str = ", ".join(user_syms)

    prompt = f"""
    You are a medical assistant. Based on the symptoms below, return ONLY a JSON array.
    Each element must be: {{"disease": "<name>", "confidence": <0-100>}}
    Allowed diseases: {", ".join(allowed_diseases)}

    Symptoms: {symptoms_str}
    """

    try:
        resp = model.generate_content(prompt)
        raw_text = resp.text or ""
    except Exception as e:
        print(f"[ERROR] Gemini API call failed: {e}")
        return None, None, None

    parsed = _parse_gemini_output(raw_text)
    if not parsed:
        return None, None, None

    scored = []
    for p in parsed:
        disease = str(p["disease"]).strip()
        if disease not in allowed_diseases:
            continue
        gem_conf = float(p["confidence"])
        match_pct = _symptom_match_percent(disease, user_syms)
        final_score = (gem_conf * 0.7) + (match_pct * 0.3)
        scored.append((disease, final_score, match_pct, _prevalence(disease)))

    # filter threshold
    scored = [s for s in scored if s[1] >= CONFIDENCE_THRESHOLD]
    if not scored:
        return None, None, None

    # sort by: final_score → match% → prevalence → alphabetical
    
    scored.sort(key=lambda x: (x[2], x[1], x[3]), reverse=True)


    top_label, top_score, _, _ = scored[0]
    top_list = [(d, round(s, 2)) for d, s, _, _ in scored]

    return top_label, round(top_score, 2), top_list
