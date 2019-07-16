from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from .forms import LoginForm, RegisterForm, GuestForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django.utils.http import is_safe_url

from .models import GuestEmail

def guest_register_view(request):
    form = GuestForm(request.POST or None)
    next_get = request.GET.get("next")
    next_post = request.POST.get("next")
    redirect_path = next_get or next_post or None

    if form.is_valid():
        email = form.cleaned_data.get("email")
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id
        print(f"yow {redirect_path}")
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("register")
    return redirect("register")

def login_page(request):
    form = LoginForm(request.POST or None)
    print(request.user)
    next_get = request.GET.get("next")
    next_post = request.POST.get("next")
    redirect_path = next_get or next_post or None

    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            print("lala")
            login(request, user)
            try:
                del request.session['guest_email_id']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")

    context = {
        "form" : form
    }
    return render(request, "accounts/login.html", context)

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
	return render(request, "accounts/register.html", context)
