from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from oinks.models import Oink
from .forms import ProfileForm
from .models import UserProfile
from dm.models import DirectMessage


# Create your views here.

def edit_profile(req):
    form = ProfileForm(instance=req.user)
    return render(req, "profiles/edit_profile.html", {'form': form})


def view_profile(req, username):
    user = User.objects.get(username=username)
    logged_in_profile = UserProfile.objects.get(user=req.user)
    user_profile = UserProfile.objects.prefetch_related("sent_direct_messages", "received_direct_messages").get(user=user)
    sent_direct_messages = user_profile.sent_direct_messages.all()
    received_direct_messages = user_profile.received_direct_messages.all()
    oinks = Oink.get_last_oinks(user=user, amount=4)
    num_oinks = len(oinks)

    return render(req, "profiles/view_profile.html", {"profile": user_profile, "sent_direct_messages": sent_direct_messages, "received_direct_messages": received_direct_messages, "oinks": oinks, "num_oinks": num_oinks, "user": req.user, "logged_in_profile": logged_in_profile})


def follow_profile(req, username):
    logged_in_user = req.user
    logged_in_profile = UserProfile.objects.get(user=logged_in_user)
    user = User.objects.get(username=username)
    profile = UserProfile.objects.get(user=user)
    if not logged_in_profile.following.filter(pk=profile.pk).exists():
        logged_in_profile.following.add(profile)
    return redirect("home")


def unfollow_profile(req, username):
    logged_in_user = req.user
    logged_in_profile = UserProfile.objects.get(user=logged_in_user)
    user = User.objects.get(username=username)
    profile = UserProfile.objects.get(user=user)
    if logged_in_profile.following.filter(pk=profile.pk).exists():
        logged_in_profile.following.remove(profile)
    return redirect("home")

