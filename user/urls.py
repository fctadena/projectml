from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView



urlpatterns = [
    path('',  TemplateView.as_view(template_name="user/home.html"), name="home"),
    path('login',
         auth_views.LoginView.as_view(
             template_name="user/login.html",
             redirect_authenticated_user=True),
         name="login"),
    path('logout', auth_views.LogoutView.as_view(), name="logout"),
    path('accounts/', include('django.contrib.auth.urls')),    
]
