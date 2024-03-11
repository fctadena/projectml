from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView



urlpatterns = [
    path('',  TemplateView.as_view(template_name="user/home.html")),
    path('login',auth_views.LoginView.as_view(template_name="user/login.html"))    
]