from django import forms
from .models import ContactName, PhoneNumber

class ContactNameForm(forms.ModelForm):
    class Meta:
        model = ContactName
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ['number']
        widgets = {
            'number': forms.TextInput(attrs={'class': 'form-control'}),
        }


