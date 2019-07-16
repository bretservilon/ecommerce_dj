from django import forms
from django.contrib.auth.models import User

class GuestForm(forms.Form):
	email = forms.EmailField()

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
	username = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput)

	def clean_username(self):
		username = self.cleaned_data['username']
		qs = User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("Username is taken")
		return username

	def clean_email(self):
		email = self.cleaned_data['email']
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("Email is taken")

		email = self.cleaned_data['email']
		if "gmail.com" not in email:
			raise forms.ValidationError("Email has to be gmail.com")

		return email

	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data['password']
		password2 = self.cleaned_data['password2']
		if password != password2:
			raise forms.ValidationError("Passwords must match.")


		return data
