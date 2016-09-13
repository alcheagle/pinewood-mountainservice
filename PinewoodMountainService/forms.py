from django import forms

class MainForm(forms.Form):
    file = forms.FileField()