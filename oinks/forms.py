from django import forms
from .models import Oink


class OinkForm(forms.ModelForm):
    class Meta:
        model = Oink
        fields = ["oink_text"]