from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import OinkForm
from .models import Oink
from django.contrib import messages
from profiles.models import UserProfile


# Create your views here.
def home(req):
    form = OinkForm()
    oinks=[]
    if req.user.is_authenticated:
        #.order_by('-id') draait de order om.
        #oinks = Oink.get_user_oinks(user=req.user).order_by('-id')
        oinks = Oink.get_following_oinks(user=req.user).order_by('-id')

    return render(req, 'oinks/home.html', {'form': form, "oinks": oinks, "user": req.user})


def create_oink(req):
    if req.method == "POST":
        form = OinkForm(req.POST)
        if form.is_valid():
            user = req.user
            oink_text = form.cleaned_data.get("oink_text")
            Oink.create_oink(user=user, oink_text=oink_text)
            messages.success(req, f"Oink created successfully")
            return redirect("home")
        else:
            messages.error(req, f"Something went wrong")

    return redirect('home')


def delete_oink(req, pk):
    Oink.delete_oink(pk, req.user)
    return redirect('home')


def search_all(req):
    users = None
    if req.method == "POST":
        logged_in_profile = UserProfile.objects.get(user=req.user)
        search = req.POST.get('search')
        profiles = UserProfile.objects.filter(user__username__icontains=search)
        oinks = Oink.objects.filter(oink_text__icontains=search)
    return render(req, 'oinks/search_results.html', {'profiles': profiles, 'oinks': oinks, 'logged_in_profile': logged_in_profile})

