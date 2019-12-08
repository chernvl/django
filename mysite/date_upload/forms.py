from django import forms
from .models import Raw_data

class Formname(forms.Form):
    name = forms.CharField()

class Data_form (forms.ModelForm):
    class Meta:
        model = Raw_data
        fields = ('name','author','csv')