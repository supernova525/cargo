from django import forms

from core.models import Prealert

class PrealertForm(forms.ModelForm):
    
    class Meta:
        model = Prealert
        fields = '__all__'
