from django import forms
from .models import Remedio

class RemedioForm(forms.ModelForm):
    class Meta:
        model = Remedio
        fields = ['nome', 'descricao']
        widgets = {
            'descricao': forms.TimeInput(attrs={'type': 'time'}),  # Força o campo a ser renderizado como <input type="time">
        }
