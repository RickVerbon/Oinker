from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def register(req):
    name = "Rick"
    return render(req, 'users/register.html', {'name': name})

def login(req):
    return HttpResponse("Login page")