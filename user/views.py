from django.shortcuts import render, redirect
from user.forms import RegistrationForm, UserCreationForm
from django.contrib import messages




            
def sign_up(request):
    if request.method == "POST":
        try:
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Registration successful. You can now log in.')
                print('Registration successful. You can now log in')
                return redirect('login')
            else:
                # If the form is not valid, render the sign-up page with the form and errors
                messages.error(request, 'Form is not valid. Please correct the errors.')
                return render(request, 'user/sign-up.html', {'form': form})
        except Exception as e:
            # Handle the exception here, you might want to log it or display an error message
            print(f"An error occurred during form processing: {str(e)}")
            messages.error(request, 'An error occurred during registration. Please try again later.')
            return redirect('sign-up')
    else:
        form = RegistrationForm()
    
    # If it's a GET request, render the sign-up page with the empty form
    return render(request, 'user/sign-up.html', {'form': form})