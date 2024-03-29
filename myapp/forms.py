
from django import forms
from .models import Snippet

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label='E-mail')
    category = forms.ChoiceField(choices=[('question', 'Question'), ('other', 'Other')])
    subjects = forms.CharField(required=False)
    descrp = forms.CharField(widget=forms.Textarea)



class SnippetForm(forms.ModelForm):
    class Meta:
        model=Snippet
        fields=('name','email','phno','body')
