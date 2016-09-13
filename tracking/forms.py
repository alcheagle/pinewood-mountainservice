from django import forms

class UploadForm(forms.Form):
    name = forms.CharField()
    file = forms.FileField()
	
    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass