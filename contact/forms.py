from .models import ContactForm
from django import forms


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ('name', 'email', 'message')