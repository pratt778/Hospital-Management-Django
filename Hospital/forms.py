from django import forms
from .models import ContactForm

class MyContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields=['Fullname',"Address","Email","Subject","Message"]
        widgets={
            'Fullname':forms.TextInput(attrs={'class':'form-control'}),
            'Address':forms.TextInput(attrs={'class':'form-control'}),
            'Email':forms.TextInput(attrs={'class':'form-control'}),
            'Subject':forms.TextInput(attrs={'class':'form-control'}),
            'Message':forms.Textarea(attrs={'class':'form-control'}),
        }