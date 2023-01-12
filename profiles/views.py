from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.messages import error
from django.core.checks import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ProfileForm

# Create your views here.



def user_profile(req):
    if req.method == "POST":
        user = req.user
        form = ProfileForm(req.POST)
        if form.is_valid():
            user_form = form.save()
            messages.success(req, f'{user}, Your profile has been updated')
            return redirect('user-profile', user_form.User)

        for error in list(form.errors.values()):
            messages.error(req, error)

    user = User.objects.filter(username=User).first()
    if user:
        form = ProfileForm(instance=user)
        form.fields['description'].widget.attrs = {'rows':1}
        return render(req, "profiles/profiles.html", {'form': form})
    return render(req, "profiles/profiles.html")
