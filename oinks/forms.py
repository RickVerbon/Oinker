from django import forms
from .models import Oink


class OinkForm(forms.ModelForm):
    class Meta:
        model = Oink
        fields = ["oink_text"]

        widgets = {
            'oink_text': forms.TextInput(attrs={
        'class': 'form-control'
        })}

        labels = {
        'oink_text': 'Whats on your mind?'
        }
