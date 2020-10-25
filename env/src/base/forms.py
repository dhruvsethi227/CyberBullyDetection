from django import forms
from django.contrib.auth import login, authenticate

class TranForm(forms.Form):
    text = forms.CharField(label = 'Transcript', max_length = 10000)
