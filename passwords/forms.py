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

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'password', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control w-50','required': 'false'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control w-50'}),
            'email': forms.TextInput(attrs={'class': 'form-control w-50'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control w-50'}),
        }

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
