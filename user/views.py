from django.shortcuts import render
from user.forms import RegistrationForm



# def sign_up(request):
#     if request.method == "POST":
#         form = RegistrationForm(request.post)
#         if form.is_valid():
#             user = 