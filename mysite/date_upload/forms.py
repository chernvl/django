from django import forms
from .models import Raw_data
from django.contrib.auth.models import User
from date_upload.models import UserProfileInfo

class Formname(forms.Form):
    name = forms.CharField()

class Data_form (forms.ModelForm):
    class Meta:
        model = Raw_data
        fields = ('name','author','csv')

class UserForm (forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ['username','email','password']




