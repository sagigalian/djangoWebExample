from django import forms

class CreateAcount(forms.Form):
	name = forms.CharField(max_length=200, label='Name')  
	phone = forms.CharField(max_length=200, label='Phone')
	email = forms.CharField(max_length=200, label='Email')

class Login(forms.Form):
	name = forms.CharField(max_length=200, label='Name')  
	phone = forms.CharField(max_length=200, label='Phone')

class Manager(forms.Form):
	name = forms.CharField(max_length=200, label='Name')
	password = forms.CharField(max_length=200, label='Password')

	