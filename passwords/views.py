from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SecretForm, UserForm, LoginForm, HiddenMessage
from django.contrib.auth.hashers import make_password
from cryptography.fernet import Fernet
from django.utils.crypto import get_random_string
from passwords.models import Secret
from django.contrib.auth.models import User


def user_authorized(func):
   """View decorator that checks a user is logged in."""
   def wrapper(request, *args, **kwargs):
       if request.session['user_id'] is None:
           return redirect("/")
       return func(request, *args, **kwargs)
   return wrapper

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SecretForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            message = form.data['message']
            name = form.data['name']
            # TODO remove this key from the code...
            key = b'3p8kC5Df0xbj-tif1uskB1BnCo7SwMXMUYy0RnSH9L4='
            fernet = Fernet(key)
            encMessage = fernet.encrypt(message.encode())
            secret = Secret(id=get_random_string(length=32), name=name, message=encMessage.decode('UTF-8'))
            secret.save()
            return redirect(generated, id=secret.id)
    else:
        form = SecretForm()
    return render(request, "passwords/index.html", {'form': form})

def view_secret(request, id):
    record = Secret.objects.get(id=str(id))
    key = b'3p8kC5Df0xbj-tif1uskB1BnCo7SwMXMUYy0RnSH9L4='
    fernet = Fernet(key)
    decrypt = fernet.decrypt(str.encode(record.message)).decode()
    name = record.name
    id = record.id
    if record.destroy:
        record.delete()
    return render(request, "passwords/view_secret.html", {'message': decrypt, 'from': name, 'id': id})

def generated(request, id=3):
    return render(request, "passwords/generated.html", {"id": id})

def create_account(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        user = User.objects.create_user(
         first_name = form.data['first_name'],
         last_name = form.data['last_name'],
         username = form.data['email'],
         password = form.data['password'])
        return redirect(generated, id=user.id)
    else:
        form = UserForm()
        return render(request, "passwords/create_account.html", {'form': form})


# Session views
class Session:
    def new(request):
        form = LoginForm()
        return render(request, "passwords/login.html", {'form': form})

    def create(request):
        form = LoginForm(request.POST)
        user = authenticate(username=form.data['email'], password=form.data['password'])
        if user is not None:
            request.session['user_id'] = user.id
            return render(request, "passwords/index.html")

    def delete(request):
        request.session['user_id'] = None
        return redirect("/")


# My vault views
class MyVault:
    @user_authorized
    def my_vault(request):
        user_id = request.session["user_id"]
        user = User.objects.get(id=user_id)
        secrets = user.secret_set.all()
        return render(request, "passwords/my_vault.html", {"user": user, "secrets": secrets})

    @user_authorized
    def add(request):
        form = HiddenMessage(request.POST)
        user_id = request.session['user_id']
        key = b'3p8kC5Df0xbj-tif1uskB1BnCo7SwMXMUYy0RnSH9L4='
        fernet = Fernet(key)
        encMessage = fernet.encrypt(form.data['message'].encode())
        secret = Secret(id=get_random_string(length=32), name="My Vault", message=encMessage.decode('UTF-8'), user_id=user_id, destroy=False)
        secret.save()
        return redirect(my_vault)

