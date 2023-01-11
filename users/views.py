from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import RegisterForm

# Create your views here.
def register(req):
    form = RegisterForm()
    return render(req, 'users/register.html', {'form': form})

def login(req):
    return HttpResponse("Login page")