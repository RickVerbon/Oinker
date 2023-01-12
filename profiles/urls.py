from django.urls import path

from . import views

urlpatterns = [
    path('profile/edit', views.edit_profile, name="edit-profile"),
    path('profile/<str:username>', views.view_profile, name="view-profile")
]
