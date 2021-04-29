from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(max_length=250, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(max_length=250, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=250, widget=forms.PasswordInput(attrs={'placeholder': 'Password again'}))

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            )

class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'validate','placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))