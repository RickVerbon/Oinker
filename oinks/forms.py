from django import forms
from .models import Oink, Comment


class OinkForm(forms.ModelForm):
    class Meta:
        model = Oink
        fields = ("oink_text",)

        widgets = {
            'oink_text': forms.TextInput(attrs={
        'class': 'form-control'
        })}

        labels = {
        'oink_text': 'Whats on your mind?'
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment_text",)

        widgets = {
            'comment_text': forms.TextInput(attrs={
        'class': 'form-control'
        })}

        labels = {
        'comment_text': "Comment:"
        }
