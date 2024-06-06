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
    """Render register page and handle user registration. Sends email to user to confirm registration."""
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
            return redirect(reverse('profile')) #redirect to profile page
        else: #login error message
            messages.error(request, "Unable to log in. Please contact us or your admin",
                           extra_tags='alert alert-danger')
            
    else:
        form = UserRegistrationForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'register.html', args)

# user login capabilities
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POSTT)
        if form.is_valid():
            form.save()
            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password1'))
    
        if user is not None:
            auth.login(request,user)
            messages.success(request, "You have successfully logged in",
                             extra_tags = 'alert alert-success')
            return redirect(reverse('profile'))
        else:
            form.add_error(None,
                           "Please try again. Your email or password is incorrect")
    
    else:
        form = UserLoginForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'login.html', args)

