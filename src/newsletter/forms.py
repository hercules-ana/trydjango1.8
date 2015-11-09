from django import forms
from .models import Newsletter

class ContactForm(forms.Form):
	full_name = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField()

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extension = provider.split('.')
		if not extension == "edu":
			raise forms.ValidationError("Please use a valid .edu email address")
		return email


class NewsletterForm(forms.ModelForm):
	class Meta:
		model = Newsletter
		fields = ['email', 'full_name']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extension = provider.split('.')
		if not extension == "edu":
			raise forms.ValidationError("Please use a valid .edu email address")
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		return full_name