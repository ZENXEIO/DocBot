symptom_vocab = [
    # Constitutional
    "fever", "chills", "night sweats", "fatigue", "malaise", "weakness",
    "weight loss", "weight gain", "cachexia", "anorexia",

    # Neurological
    "headache", "dizziness", "vertigo", "syncope", "fainting", "seizures",
    "memory loss", "confusion", "numbness", "tingling", "paresthesia",
    "muscle weakness", "tremor", "ataxia", "hallucination", "visual changes",
    "blurred vision", "double vision", "hearing loss", "tinnitus",
    "speech difficulty", "aphasia", "dysarthria", "brain fog",
    "sleep disturbance", "insomnia", "hypersomnia",

    # Cardiovascular / Chest
    "chest pain", "chest tightness", "palpitations", "tachycardia", 
    "bradycardia", "shortness of breath", "dyspnea", "orthopnea",
    "paroxysmal nocturnal dyspnea", "edema", "swollen ankles", 
    "claudication",

    # Respiratory / Infection
    "cough", "sputum", "hemoptysis", "wheezing", "pleuritic chest pain",
    "hoarseness", "stridor", "sore throat", "runny nose", "nasal congestion",
    "sinus pressure", "conjunctivitis", "red eye", "watery eye", 
    "eye pain",

    # Gastrointestinal
    "nausea", "vomiting", "abdominal pain", "bloating", "gas", "heartburn",
    "indigestion", "dyspepsia", "belching", "constipation", "diarrhea",
    "blood in stool", "melena", "hematochezia", "vomiting blood",
    "dysphagia", "odynophagia", "flatulence", "fecal incontinence",

    # Genitourinary / Reproductive
    "painful urination", "dysuria", "frequent urination", "polyuria",
    "nocturia", "hematuria", "urinary retention", "urinary incontinence",
    "pelvic pain", "vaginal bleeding", "abnormal vaginal bleeding",
    "vaginal discharge", "menstrual irregularity", "heavy periods",
    "genital lump", "breast lump", "breast pain", "nipple discharge",
    "erectile dysfunction", "sexual dysfunction",

    # Musculoskeletal
    "back pain", "joint pain", "joint swelling", "muscle pain",
    "bone pain", "arthralgia", "stiffness", "crepitus", "muscle cramps",

    # Skin & Dermatological
    "rash", "itching", "pruritus", "urticaria", "hives", "blisters",
    "ulcers", "non-healing ulcer", "skin discoloration", "jaundice",
    "easy bruising", "bleeding", "skin thickening", "hair loss",
    "alopecia", "scalp itching", "scaly patches", "folliculitis",
    "pustules", "cellulitis", "abscess", "skin lesions", "erythema",
    "perifollicular erythema", "painful sore", "new mole", "mole change",

    # Hair / Trichology
    "thinning hair", "bald spots", "hair shedding", "receding hairline",
    "scalp burning", "scalp tingling", "scalp pain", "traction alopecia",
    "telogen effluvium", "alopecia areata", "cicatricial alopecia",

    # Endocrine / Metabolic
    "excessive thirst", "polydipsia", "polyphagia", "cold intolerance",
    "heat intolerance", "hot flashes", "tremor", "sweating",

    # Immune / Infection / Systemic
    "persistent fever", "recurrent infection", "lymph node swelling",
    "lymphadenopathy", "rash with fever", "conjunctivitis", "joint erythema",
    "arthralgia", "chikungunya-like arthralgia",

    # Psychiatric / Cognitive
    "depression", "anxiety", "irritability", "mood swings", "mania",
    "phobia", "obsessive thoughts", "paranoia", "anhedonia",
    "delusions", "suicidal ideation", "panic attacks", "difficulty concentrating",
    "restlessness",

    # Sensory
    "loss of smell", "anosmia", "loss of taste", "ageusia", "altered taste",
    "photophobia", "photosensitivity",

    # Hematologic / Bleeding
    "unexplained bleeding", "easy bruising", "black stool", "petechiae",
    "purpura",

    # Danger warning signs
    "persistent sore throat", "non-healing sore", "new lump", "mass", "persistent cough",
    "hematemesis", "bright red blood per rectum"
]

list2 = 'itching', 'skin rash', 'nodal skin eruptions', 'continuous sneezing', 'shivering', 'chills', 'joint pain', 'stomach pain', 'acidity', 'ulcers on tongue', 'muscle wasting', 'vomiting', 'burning micturition', 'spotting  urination', 'fatigue', 'weight gain', 'anxiety', 'cold hands and feets', 'mood swings', 'weight loss', 'restlessness', 'lethargy', 'patches in throat', 'irregular sugar level', 'cough', 'high fever', 'sunken eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish skin', 'dark urine', 'nausea', 'loss of appetite', 'pain behind the eyes', 'back pain', 'constipation', 'abdominal pain', 'diarrhoea', 'mild fever', 'yellow urine', 'yellowing of eyes', 'acute liver failure', 'fluid overload', 'swelling of stomach', 'swelled lymph nodes', 'malaise', 'blurred and distorted vision', 'phlegm', 'throat irritation', 'redness of eyes', 'sinus pressure', 'runny nose', 'congestion', 'chest pain', 'weakness in limbs', 'fast heart rate', 'pain during bowel movements', 'pain in anal region', 'bloody stool', 'irritation in anus', 'neck pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen legs', 'swollen blood vessels', 'puffy face and eyes', 'enlarged thyroid', 'brittle nails', 'swollen extremeties', 'excessive hunger', 'extra marital contacts', 'drying and tingling lips', 'slurred speech', 'knee pain', 'hip joint pain', 'muscle weakness', 'stiff neck', 'swelling joints', 'movement stiffness', 'spinning movements', 'loss of balance', 'unsteadiness', 'weakness of one body side', 'loss of smell', 'bladder discomfort', 'foul smell of urine', 'continuous feel of urine', 'passage of gases', 'internal itching', 'toxic look (typhos)', 'depression', 'irritability', 'muscle pain', 'altered sensorium', 'red spots over body', 'belly pain', 'abnormal menstruation', 'dischromic  patches', 'watering from eyes', 'increased appetite', 'polyuria', 'family history', 'mucoid sputum', 'rusty sputum', 'lack of concentration', 'visual disturbances', 'receiving blood transfusion', 'receiving unsterile injections', 'coma', 'stomach bleeding', 'distention of abdomen', 'history of alcohol consumption', 'fluid overload.1', 'blood in sputum', 'prominent veins on calf', 'palpitations', 'painful walking', 'pus filled pimples', 'blackheads', 'scurring', 'skin peeling', 'silver like dusting', 'small dents in nails', 'inflammatory nails', 'blister', 'red sore around nose', 'yellow crust ooze'

for symptom in list2:
    if symptom not in symptom_vocab:
        symptom_vocab.append(symptom)

__all__ = ["symptom_vocab"]