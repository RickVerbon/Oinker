from django import forms
from profiles.models import UserProfile


class ProfileForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'email', 'description',)
