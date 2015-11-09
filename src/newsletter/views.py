from django.shortcuts import render
from .forms import NewsletterForm, ContactForm
from django.core.mail import send_mail
from django.conf import settings

def home(request):
	title = "Welcome"
	form = NewsletterForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	if request.user.is_authenticated():
		title = "My title %s" %(request.user)
	context = {
		"title": title,
		"form": form
	}
	return render(request, "home.html", context)

def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		email = form.cleaned_data.get("email")
		full_name = form.cleaned_data.get("full_name")
		message = form.cleaned_data.get("message")

		subject = 'Site Contact Form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [settings.EMAIL_HOST_USER, email]
		contact_message = "%s:%s" %(full_name, message)
		send_mail(subject, contact_message, from_email, [to_email], fail_silently=False)


	context = {
		"form": form,
	}
	return render(request, "forms.html", context)