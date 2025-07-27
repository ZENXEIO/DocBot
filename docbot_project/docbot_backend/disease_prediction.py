import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from docbot_backend.labels import label_mapping

df = pd.read_csv("ready_dataset.csv")
df['label'] = df['label'].replace(label_mapping)

# Declaring targets
X = df.drop(columns=['label'])
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

svm_model = SVC(kernel='linear', probability=True, class_weight='balanced', random_state=42)
svm_model.fit(X_train, y_train)

rf_model = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
rf_model.fit(X_train, y_train)

knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_train, y_train)

logreg_model = LogisticRegression(max_iter=1000, class_weight='balanced')
logreg_model.fit(X_train, y_train)

# --- Model predictions ---
svm_probs = svm_model.predict_proba(X_test)
rf_probs = rf_model.predict_proba(X_test)
knn_probs = knn_model.predict_proba(X_test)
logreg_probs = logreg_model.predict_proba(X_test)

weights = {
    'svm': 1.0,
    'rf': 1.0,
    'knn': 1.0,
    'logreg': 0.8
}

total = sum(weights.values())

ensemble_probs = (
    svm_probs * weights['svm'] +
    rf_probs * weights['rf'] +
    knn_probs * weights['knn'] +
    logreg_probs * weights['logreg']
) / total

common_classes = svm_model.classes_

def predict_disease(symptom_list):
    user_symptoms = [s.strip().lower() for s in symptom_list]
    input_vector = [1 if col in user_symptoms else 0 for col in X.columns]
    input_df = pd.DataFrame([input_vector], columns=X.columns)

    # Get probabilities from all models
    svm_p = svm_model.predict_proba(input_df)
    rf_p = rf_model.predict_proba(input_df)
    knn_p = knn_model.predict_proba(input_df)
    logreg_p = logreg_model.predict_proba(input_df)

    # Weighted average of probabilities
    combined_p = (
        svm_p * weights['svm'] +
        rf_p * weights['rf'] +
        knn_p * weights['knn'] +
        logreg_p * weights['logreg']
    ) / total

    # Top prediction and confidence
    top_index = np.argmax(combined_p)
    pred_label = common_classes[top_index]
    confidence = combined_p[0][top_index] * 100

    # Top 10 predictions
    top_indices = combined_p[0].argsort()[-10:][::-1]
    top_filtered = [(common_classes[i], combined_p[0][i] * 100) for i in top_indices]

    # If top confidence is too low, ask user to re-enter
    if confidence < 30:
        print("Prediction confidence is low ({:.2f}%).".format(confidence))
        print("Please provide more specific or accurate symptoms.\n")
        return None, None, None

    return pred_label, confidence, top_filtered

