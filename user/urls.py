from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from user.views import sign_up


urlpatterns = [
    path('',  TemplateView.as_view(template_name="user/home.html"), name="home"),
    path('login',
         auth_views.LoginView.as_view(
             template_name="user/login.html"),
         name="login"),
    path('logout',
         auth_views.LogoutView.as_view(
             next_page='login'), name="logout"),
    path('sign-up', sign_up, name="sign_up"),
    path('reset-password',
         auth_views.PasswordResetView.as_view(
             template_name="user/reset-password.html",
             email_template_name="user/reset-password-email.html",
             success_url="reset-password-done"),
         name="reset_password"),
    path('reset-password-done',
         auth_views.PasswordResetDoneView.as_view(
             template_name="user/reset-password-sent.html"), name="reset_password_done"),
    path('password-reset-confirm/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(
             template_name="user/password-reset-confirm.html",
             success_url="reset-password-done"), name="password_reset_confirm"),
    path('reset-password-complete',
         auth_views.PasswordResetCompleteView.as_view(
             template_name="user/password-reset-complete.html"),
         name="reset_password_complete")
]

#CONTINUE: WHAT HAPPEN AFTER PasswordResetCompleteView?  jane pw Gat#105jane 
#ALSO REVIEW PROPER NAMING BASED ON FLOW EVENTS