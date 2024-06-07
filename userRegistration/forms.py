from django import forms
from django.contrib.auth.forms import UserCreationForm
from userRegistration.models import UserProfile # import userprofile from models.py
from django.contrib.auth.hashers import make_password #save password in database

class UserRegistrationForm(UserCreationForm):

    class Meta:
            model = UserProfile
            fields =["email", "username","first_name", "last_name"] #included fields in form
        #inherits password1 and password2 functionalities from UserCreationForm Django template
            
    def clean_username(self):
            #validate that username is not empty and is unique
        username = self.cleaned_data.get('username')

        if not username:
            message = "Please enter your username"
            raise forms.ValidationError(message)
        if UserProfile.objects.filter(username=username).exists():
            message = "A user with this username already exists"
            raise forms.ValidationError(message)

    def clean_email(self):
        # validate that email is not empty and is unique
        email = self.cleaned_data.get('email')

        if not email:
            message = "Please enter your email address"
            raise forms.ValidationError(message)
        if UserProfile.objects.filter(email=email).exists():
            message = "The email address given is already registered to another user"
            raise forms.ValidationError(message)
        return email
                
            
    def clean_first_name(self):
        first_name = self.cleaned.get('first name')
        if not first_name:
            message = "Please enter your first name"
            raise forms.ValidationError(message)
        return first_name
        
            
    def clean_last_name(self):
        last_name = self.cleaned.get('last name')
        if not last_name:
            message = "Please enter your last name"
            raise forms.ValidationError(message)
        return last_name
        
       

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data['username'] 
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
        
        
class UserLoginForm(forms.Form):
    # Form to authenticate user using email and password

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


    #remove username field if password used?