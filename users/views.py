from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from .forms import RegisterForm, LoginForm

# Create your views here.


def register(req):
    if req.method == 'POST':
        form = RegisterForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = User.objects.create_user(username=username, password=raw_password)
            if user is not None:
                login(req, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(req, 'users/register.html', {'form': form})


def login_user(req):
    if req.method == "POST":
        form = LoginForm(req.POST)
        if form.is_valid:
            username = req.POST.get("username")
            password = req.POST.get("password")
            user = authenticate(username=username, password=password)
            if user:
                login(req, user)
                return redirect("home")
            else:
                return None
        return redirect("home")
    else:
        form = LoginForm()
    return render(req, "users/login.html", {'form': form})


def logout_user(req):
    logout(req)
    return redirect('home')