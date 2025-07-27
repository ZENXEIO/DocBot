# DocBot - AI Medical Assistant

**DocBot** is a Django-based AI-powered medical assistant that accepts natural language symptoms and predicts likely diseases using multiple machine learning models. It also provides contextual health information and treatment suggestions.

## Features

- Accepts natural language symptom input  
- Intelligent symptom parsing and fuzzy matching  
- Ensemble disease prediction using SVM, Random Forest, KNN, and Logistic Regression  
- Confidence-based result display with top predictions  
- Context, drug, and supplement suggestions  
- Clean UI (Teal + White), animated prediction bars  
- Reset button to clear session

## Tech Stack

- **Backend**: Django, Python, Scikit-learn  
- **Frontend**: HTML, CSS, JavaScript (with scroll animations)  
- **ML Models**: SVM, Random Forest, KNN, Logistic Regression  
- **Deployment**: Render or any WSGI-compatible platform

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ZENXEIO/docbot.git
cd docbot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Start the Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## Sample Inputs

Try the following for testing:

- `fever, chills, body pain`
- `headache, nausea, blurred vision`
- `sore throat, cough, congestion`

## Deployment (Render)

1. Create `requirements.txt` and `Procfile`:
   ```
   web: gunicorn docbot_project.wsgi
   ```

2. In `settings.py`:
   - Set `DEBUG = False`
   - Add static config:
     ```python
     STATIC_URL = '/static/'
     STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
     ```
   - Add `'whitenoise.middleware.WhiteNoiseMiddleware'` to `MIDDLEWARE`

3. Push to GitHub

4. Go to [Render](https://render.com), create a Web Service

5. Set environment variable:
   ```
   DJANGO_SECRET_KEY = your-secret-key
   ```

## Project Structure

```
docbot_project/
├── docbot_app/
│   ├── views.py
│   ├── forms.py
│   └── templates/
├── docbot_backend/
│   ├── disease_prediction.py
│   ├── drug_recommender.py
│   ├── nlp_parser.py
│   └── symptoms.py
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── manage.py
└── requirements.txt
```

## License

MIT License

Copyright (c) 2025 ZENXEIO

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in  
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  
SOFTWARE.

