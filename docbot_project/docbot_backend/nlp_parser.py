import os
import re
import difflib
from docbot_backend.symptoms import symptom_vocab


os.environ["GEMINI_API_KEY"] = "AIzaSyDBKa6VG-6euP_X2zMjxF3UgOnIIRs45ek"
print("API key environment variable set for this session.")

import google.generativeai as genai
model = genai.GenerativeModel("gemma-3-4b-it") # BETA VERSION OF AI

def fuzzy_match(symptoms, vocab, cutoff=0.8):
    matched = []
    for s in symptoms:
        match = difflib.get_close_matches(s, vocab, n=1, cutoff=cutoff)
        if match:
            matched.append(match[0])
    return matched

def extract_symptoms(user_input, symptom_vocab):
    prompt = f"""
You're a medical assistant. Based on the user's statement, extract symptoms ONLY from the provided list.

User Input: "{user_input}"

Symptom Vocabulary: {symptom_vocab}

Return a Python list containing only the matched symptoms (as exact strings), like ['fever', 'night sweats'].
If none match, return [].
    """
    
    response = model.generate_content(prompt)
    response_text = response.text.strip()

    # Remove triple backticks and optional language hint
    cleaned = re.sub(r"```(?:python)?", "", response_text).replace("```", "").strip()

    try:
        result = eval(cleaned)
        if isinstance(result, list):
            return result
    except Exception as e:
        print("Error parsing cleaned response:", e)
        print("Cleaned Response:", cleaned)
    
    return []
