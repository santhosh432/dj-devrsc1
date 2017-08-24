from django import forms
from datetime import date
import warnings


class UserRegistrationForm(forms.Form):
	username = forms.CharField(max_length=200, label=("User Name:"), required=True)
	password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30)), label=("Password:"))
	fname = forms.CharField(max_length=10, label=("First Name:"), required=True)
	lname = forms.CharField(max_length=10, label=("Last Name:"), required=True)
	emailid = forms.EmailField(max_length=100, label=("Email Address:"), required=True)
	address=forms.CharField(max_length=200, widget=forms.Textarea,label=("Address:"))
	phone =forms.IntegerField(label=("Phone"),widget=forms.TextInput)
	tech = forms.CharField(max_length=20, label=("Select Technolgy:"), required=True)


class ExfinalForm(forms.Form):
    original_ans = forms.CharField(max_length=2)

