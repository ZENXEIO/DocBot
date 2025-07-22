from django import forms

class SymptomForm(forms.Form):
    symptoms = forms.CharField(
        label="Describe your symptoms",
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'e.g. I feel dizzy and have chest pain...'}),
        max_length=1000
    )
