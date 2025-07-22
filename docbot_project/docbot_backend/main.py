import nlp_parser as np
from symptoms import symptom_vocab
import disease_prediction as dp
import drug_recommender as dr

def run_bot():
    while True:
        print('\n******** Welcome To DocBOT *************\n')
        user_input = input('Hello, please describe how you are feeling: ')
        extracted = np.extract_symptoms(user_input, symptom_vocab)
        final_symptoms = np.fuzzy_match(extracted, symptom_vocab)

        if not final_symptoms:
            print("Sorry, I couldn't recognize any known symptoms.")
            continue

        label, conf, top = dp.predict_disease(final_symptoms)

        if top is None or conf is None:
            retry = input("Would you like to try again? (yes/no): ").strip().lower()
            if retry != 'yes':
                print("\nThanks for using DocBOT. Stay safe!")
                break
            continue

        print("\nBased on your symptoms, here are the most likely conditions:")
        for disease, prob in top:
            print(f"  {disease}: {prob:.2f}%")

        print(f"\nTop guess: {label} (confidence: {conf:.2f}%)")

        if conf < 30:
            print("\nThis is a low-confidence prediction.")
            print("But here's what we know so far based on your symptoms:")
            dr.get_disease_info(label)
            print('\nDue to the lower confidence level, these recommendations should be taken cautiously.')
            print('Please consult a doctor before taking any medicine or supplements.\n')
            retry = input("Would you like to describe your symptoms again for a better prediction? (yes/no): ").strip().lower()
            if retry != 'yes':
                print("\nThanks for using DocBOT. Wishing you a speedy recovery.")
                break
        else:
            print(f"\nBased on your symptoms {final_symptoms}, you most likely have: {label}")
            print('\nHere is more information about this condition...\n')
            dr.get_disease_info(label)
            print('\nNOTE: DocBOT is a guidance tool and may not be fully accurate.')
            print('Please consult a medical professional before taking any medicines or supplements.')
            break


run_bot()