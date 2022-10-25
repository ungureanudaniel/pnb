from django import forms
from .models import Attraction

class AttractionForm(forms.ModelForm):
    body = forms.CharField(required=True)

    class Meta:
        model = Attraction
        exclude = ()
