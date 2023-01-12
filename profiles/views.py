from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.messages import error
from django.core.checks import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ProfileForm

# Create your views here.



def user_profile(req):
    form = ProfileForm(instance=req.user)
    return render(req, "profiles/profiles.html", {'form': form})
