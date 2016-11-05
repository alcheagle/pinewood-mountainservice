from django import forms

class Report (forms.Form):
	#id= forms.CharField(min_length=20, max_length=20)
	#key=forms.CharField(min_length=20, max_length=20)
	description = forms.CharField(label='description', max_length=3000)
	evaluation = forms.CharField (label='evalutation')
	pathName = forms.CharField(label='charField', max_length=200)
	
