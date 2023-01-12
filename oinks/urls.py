from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create-oink', views.create_oink, name="create-oink"),
    path('delete-oink/<int:pk>', views.delete_oink, name="delete-oink")
]