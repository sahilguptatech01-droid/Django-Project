from django.contrib import admin
from django.urls import path ,include
from . import views
from django.contrib.auth import views as auth_views
app_name='users'

urlpatterns=[
    path('register/',views.register,name="register"),
    path('logout/',views.logout_view,name="logout"),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
]