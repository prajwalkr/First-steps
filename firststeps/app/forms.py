from django import forms

class userform(forms.Form):
	name = forms.CharField(max_length = 25)
	