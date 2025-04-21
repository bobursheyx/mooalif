# forms.py
from django import forms
from .models import Ariza

class ArizaForm(forms.ModelForm):
    class Meta:
        model = Ariza
        fields = ['ismi', 'email', 'xabar']
