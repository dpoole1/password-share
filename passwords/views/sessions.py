from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NameForm, UserForm
from django.contrib.auth.hashers import make_password
from cryptography.fernet import Fernet
from django.utils.crypto import get_random_string
from passwords.models import Secret
from django.contrib.auth.models import User



