from django.shortcuts import render
from docbot_app.forms import SymptomForm
from docbot_backend import nlp_parser as np
from docbot_backend.symptoms import symptom_vocab
from docbot_backend import disease_prediction as dp
from docbot_backend import drug_recommender as dr

def home(request):
    context = {}

    if request.method == 'POST':
        form = SymptomForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['symptoms']
            extracted = np.extract_symptoms(user_input, symptom_vocab)
            final_symptoms = np.fuzzy_match(extracted, symptom_vocab)

            if not final_symptoms:
                context['error'] = "Sorry, we couldn't recognize any symptoms."
                return render(request, 'index.html', {'form': form, **context})

            label, conf, top = dp.predict_disease(final_symptoms)
            
            if label and conf and top:
                context.update({
                    'final_symptoms': final_symptoms,
                    'label': label,
                    'confidence': round(conf, 2),
                    'top_predictions': top,  # <<< THIS IS ESSENTIAL
                    'disease_info': dr.get_disease_info(label)
                })

            if not label:
                context['error'] = "Low confidence. Please try describing your symptoms more clearly."
            else:
                # Gather disease info
                disease_info = dr.get_disease_info(label)
                context.update({
                    'final_symptoms': final_symptoms,
                    'label': label,
                    'confidence': round(conf, 2),
                    'top_predictions': top,
                    'disease_info': disease_info
                })
    else:
        form = SymptomForm()
    
    context['form'] = form
    return render(request, 'index.html', context)
