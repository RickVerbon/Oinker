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
    def delete_oink(cls, pk, user):
        oink = cls.objects.get(id=pk)
        if oink.user == user:
            oink.delete()
        else:
            return None

    @classmethod
    def get_user_oinks(cls, user):
        oinks = cls.objects.filter(user=user.id)
        return oinks

    @classmethod
    def get_following_oinks(cls, user):
        user_profile = UserProfile.objects.get(user=user)
        #About ".values_list('user', flat=True" it uses the values_list() method to retrieve the user field from the UserProfile queryset, and passing flat=True will return a simple list of User objects, instead of a list of tuples.
        following_users = user_profile.following.all().values_list('user', flat=True)

        #next, it's filtering all Oink objects for all the users in the following_users list.
        oinks = cls.objects.filter(user__in=following_users)
        return oinks

    def __str__(self):
        _str = self.user.username + ": " + str(self.id)
        return _str
