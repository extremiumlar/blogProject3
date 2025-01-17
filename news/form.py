from django import forms
from .models import Contact,Comentary

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class ComentaryForm(forms.ModelForm):
    class Meta:
        model = Comentary
        fields = ['body']
