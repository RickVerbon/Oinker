from django.db import models

from profiles.models import UserProfile


# Create your models here.
class DirectMessage(models.Model):
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="sent_direct_messages")
    receiver = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="received_direct_messages")
    dm_text = models.CharField(max_length=140)
    date_time = models.DateTimeField(auto_now_add=True)
    read_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sender} to { self.receiver}"
