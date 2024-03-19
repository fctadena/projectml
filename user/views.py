from django.shortcuts import render
from user.forms import RegistrationForm, UserCreationForm



def sign_up(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
         
    else:
        form = RegistrationForm()
        context = {
                'form':form
            }
            
        return render(request, 'user/sign-up.html', context)