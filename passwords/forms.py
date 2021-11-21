from django import forms
from .models import User, Secret

class SecretForm(forms.ModelForm):
    class Meta:
        model = Secret
        fields = ('message', 'name')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control w-50','required': 'false'}),
            'message': forms.TextInput(attrs={'class': 'form-control w-50'})
        }

class UserForm(forms.Form):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    password = forms.CharField(label='Password')
    email = forms.CharField(label='Email')

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control w-50'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control w-50'})
        }

class HiddenMessage(forms.Form):
    message = forms.CharField(label='message')
