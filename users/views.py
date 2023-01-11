from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegisterForm

# Create your views here.
def register(req):
    if req.method == 'POST':
        form = RegisterForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            form = authenticate(username=username, password=raw_password)
            return redirect('home')
    else:
        form = RegisterForm()

    return render(req, 'users/register.html', {'form': form})

def login(req):
    return HttpResponse("Login page")