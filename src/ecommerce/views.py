from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from .forms import ContactForm
from django.contrib.auth.models import User

def home_page(request):
	# print(request.session.get("first_name", "Unknown"))
	context = {
		"title": "home",
		"content": "home to"
	}
	if request.user.is_authenticated:
		context['premium_content'] = "yowyowyow"
	return render(request, "home_page.html", context)

def about_page(request):
	context = {
		"title": "about",
		"content": "about to"
	}
	return render(request, "home_page.html", context)

def contact_page(request):
	contact_form = ContactForm(request.POST or None)

	if contact_form.is_valid():
		print(contact_form.cleaned_data)

	context = {
		"title": "contact",
		"content": "contact to",
		"form": contact_form
	}
	return render(request, "contact/view.html", context)


def login_page(request):
	form = LoginForm(request.POST or None)
	print(request.user)
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(request, username=username, password=password)

		if user is not None:
			print("lala")
			login(request, user)
			return redirect('home')

	context = {
		"form" : form
	}
	return render(request, "auth/login.html", context)

def register_page(request):
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data['username']
		email = form.cleaned_data['email']
		password = form.cleaned_data['password']
		new_user = User.objects.create_user(username, email, password)
		print(new_user)
	context = {
		"form": form
	}
	return render(request, "auth/register.html", context)
