from django.urls import path
from . import views
from django.contrib.auth import logout

urlpatterns = [
    path('register/', views.register, name="user-register"),
    path('login/', views.login_user, name="user-login"),
    path('logout/', views.logout_user, name="user-logout"),
    path('search/', views.search_user, name="search")
]