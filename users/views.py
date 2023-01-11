from django.http import HttpResponse
from django.shortcuts import render
from . import forms

# Create your views here.
def register(req):
    form = forms.Register()
    return render(req, 'users/register.html', {'form': form})

def login(req):
    return HttpResponse("Login page")