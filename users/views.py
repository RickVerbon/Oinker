from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def register(req):
    return HttpResponse("Register page")

def login(req):
    return HttpResponse("Login page")