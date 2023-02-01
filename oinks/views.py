from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import OinkForm, CommentForm
from .models import Oink, Comment
from django.contrib import messages
from profiles.models import UserProfile


# Create your views here.
def home(req):
    oink_form = OinkForm()
    comment_form = CommentForm()
    oinks = []
    if req.user.is_authenticated:
        #.order_by('-id') draait de order om.
        #oinks = Oink.get_user_oinks(user=req.user).order_by('-id')
        oinks = Oink.get_following_oinks(user=req.user)\
            .order_by('-id')\
            .prefetch_related('comment_set')
    return render(req, 'oinks/home.html', {'oink_form': oink_form, "comment_form": comment_form, "oinks": oinks, "user": req.user})


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


def create_comment(req, oink_pk):
    if req.method == "POST":
        form = CommentForm(req.POST)
        if form.is_valid():

            profile = UserProfile.objects.get(user=req.user)
            comment_text = form.cleaned_data.get("comment_text")
            oink = Oink.objects.get(pk=oink_pk)
            Comment.create_comment(profile, oink, comment_text)
    return redirect('home')


def search_all(req):
    if req.method == "POST":
        logged_in_profile = UserProfile.objects.get(user=req.user)
        search = req.POST.get('search')
        profiles = UserProfile.objects.filter(user__username__icontains=search)
        oinks = Oink.objects.filter(oink_text__icontains=search)
    return render(req, 'oinks/search_results.html', {'profiles': profiles, 'oinks': oinks, 'logged_in_profile': logged_in_profile})

