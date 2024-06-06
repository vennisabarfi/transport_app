from django import forms
from django.contrib.auth.forms import UserCreationForm
from userRegistration.models import UserProfile # import userprofile from models.py
from django.contrib.auth.hashers import make_password #save password in database

class UserRegistrationForm(UserCreationForm):

    password1 = forms.CharField(
        label='Enter password here',
        widget =forms.PasswordInput
    )

    password2 = forms.CharField(
        label='Confirm your password',
        widget =forms.PasswordInput
    )

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email',
                  'password1', 'password2']
    #validations
    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        if not password1:
            message = "Please enter your password"
            raise forms.ValidationError(message)
        
        min_length =8
        
        #check for length

        if len(password1) < min_length:
            message = "Your password must be at least 8 characters long"
            raise forms.ValidationError(message)
        
        #check for digit
        if not any(char.isdigit() for char in password1):
            message = "Password must contain at least 1 digit"
            raise forms.ValidationError(message)
        
        #check for letter
        if not any(char.isalpha() for char in password1):
            message = "Password must contain at least 1 letter"
            raise forms.ValidationError(message)
        
        #check for upper case letters
        if not any(char.isupper() for char in password1):
            message = "Password must contain at least 1 uppercase letter"
            raise forms.ValidationError(message)
        
        return password1
    

    def clean_password2(self):
        password1= self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        #check for confirmation password
        if not password2:
            message = "Please confirm your password to proceed"
            raise forms.ValidationError(message)
        
        #check for password match
        if password1 and password2 and password1 != password2:
            message = "Passwords do not match"
            raise forms.ValidationError(message)
        
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
        
        class Meta:
            model = UserProfile
            fields =["email", "password", "username","first name", "last name"] #included fields in form

        def save(self, commit=True):
            user = super(UserRegistrationForm, self).save(commit=False)
            user.username = self.cleaned_data['username'] 
            user.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data['first name']
            user.last_name = self.cleaned_data['last name']
            user.password = make_password(self.cleaned_data['password'])
            if commit:
                user.save()
            return user
        
        def __init__(self, *args, **kwargs):
            super(UserRegistrationForm, self).__init__(*args, **kwargs)
            for field in self.fields.values():
                field.required = False #change after consideration
        
class UserLoginForm(forms.Form):
    # Form to authenticate user using email and password

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


    #remove username field if password used?