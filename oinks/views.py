from django.shortcuts import render, redirect
from .forms import OinkForm
from .models import Oink
from django.contrib import messages


# Create your views here.
def home(req):
    form = OinkForm()
    if req.user:
        #.order_by('-id') draait de order om.
        oinks = Oink.objects.filter(user=req.user.id).order_by('-id')
    else:
        return None
    return render(req, 'oinks/home.html', {'form': form, "oinks": oinks})


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
            messages.error(req, f"Somehting went wrong")

    return redirect('home')

def delete_oink(req, pk):
    oink = Oink.objects.get(id=pk)
    oink.delete()
    return redirect('home')


