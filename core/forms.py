from django import forms

from core.models import Prealert, Contact

class PrealertForm(forms.ModelForm):
    
    class Meta:
        model = Prealert
        fields = '__all__'

class ContactForm(forms.ModelForm):

    message = forms.Textarea()
    class Meta:
        model = Contact
        fields = '__all__'


