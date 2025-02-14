from django import forms
from .models import RemuneraServ

class EdicaoRemuneraServ(forms.ModelForm):
    class Meta:
        model = RemuneraServ
        fields = ['competencia', 'valor']
        widgets = {
            'competencia': forms.DateInput(attrs={'type': 'date'}),
        }