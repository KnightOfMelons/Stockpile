from django import forms
from .models import Roll

class RollForm(forms.ModelForm):
    class Meta:
        model = Roll
        fields = ['id', 'length', 'weight']