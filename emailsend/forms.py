from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(max_length=100)
    email=forms.EmailField()
    contect=forms.CharField(widget=forms.Textarea)