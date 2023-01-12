from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from oinks.models import Oink
from .forms import ProfileForm
from .models import UserProfile


# Create your views here.

def edit_profile(req):
    form = ProfileForm(instance=req.user)
    return render(req, "profiles/edit_profile", {'form': form})


def view_profile(req, username):
    user = User.objects.get(username=username)
    user_profile = UserProfile.objects.get(user=user)
    oinks = Oink.get_user_oinks(user)
    return render(req, "profiles/view_profile.html", {"profile": user_profile, "oinks": oinks})