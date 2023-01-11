from django.shortcuts import render, redirect
from .forms import OinkForm
from .models import Oink
from django.contrib import messages
from datetime import datetime


# Create your views here.
def home(req):
    if req.method == "POST":
        form = OinkForm(req.POST)
        if form.is_valid():
            user = req.user
            oink_text = form.cleaned_data.get("oink_text")
            Oink.create_oink(user=user, oink_text=oink_text)
            messages.success(req, f"Oink created successfully")
            return redirect("home")
    else:
        form = OinkForm()
        if req.user:
            oinks = Oink.objects.filter(user=req.user)
        else:
            return None
    return render(req, 'oinks/home.html', {'form': form, "oinks": oinks})
