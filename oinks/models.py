from django.contrib.auth.models import User
from django.db import models
from django import forms
from datetime import datetime

from profiles.models import UserProfile


# Create your models here.
class Oink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    oink_text = models.TextField()
    date_time = models.DateTimeField(auto_now=True)

    @classmethod
    def create_oink(cls, user, oink_text):
        oink = cls(user=user, oink_text=oink_text)
        oink.save()
        return oink

    @classmethod
    def delete_oink(cls, pk):
        oink = cls.objects.get(id=pk)
        oink.delete()

    @classmethod
    def get_user_oinks(cls, user):
        oinks = cls.objects.filter(user=user.id)
        return oinks

    @classmethod
    def get_following_oinks(cls, user):
        NotImplemented()



    def __str__(self):
        _str = self.user.username + ": " + str(self.id)
        return _str
