from django.shortcuts import render, redirect
from django.http import HttpResponse # allow us to send a response to the user
from userRegistration.forms import UserRegistrationForm, UserLoginForm
from django.contrib import messages, auth
from django.urls import reverse
from django.core.mail import send_mail #send confirmation emails to users 
from django.template.context_processors import csrf
# Create your views here.


# link here: https://github.com/IreneG5/spss_online/blob/master/accounts/views.py 

def home(request):
    """Render home page"""
    return render(request, 'home.html')

#register a new user
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password1'))
        if user:
            send_mail(request,user) 
            messages.info(request, "Thank you for signing up!"
                           "You have logged in successfully.", extra_tags ='alert alert-success')
            auth.login(request, user)
            return redirect(reverse('profile'))
        else:
            messages.error(request, "Unable to log in. Please contact us or your admin",
                           extra_tags='alert alert-danger')
            
    else:
        form = UserRegistrationForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'register.html', args)
