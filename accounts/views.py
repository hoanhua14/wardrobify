from django.shortcuts import render, redirect
from accounts.forms import LogInForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.
def user_log_in(request):
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = LogInForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


def user_log_out(request):
    logout(request)
    return redirect("login")


def signup_form(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            confirmation = form.cleaned_data["password_confirmation"]
            if password == confirmation:
                user = User.objects.create_user(username, password=password)
                login(request, user)
                return redirect("home")
            else:
                form.add_error("password", "Passwords do not match.")
    else:
        form = SignupForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)
