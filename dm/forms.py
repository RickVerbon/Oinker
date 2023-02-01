from django.forms import ModelForm

from dm.models import DirectMessage


class DirectMessageForm(ModelForm):
    class Meta:
        model = DirectMessage
        fields = ("receiver", "dm_text",)
