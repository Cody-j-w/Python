from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from apps.login.models import *
import bcrypt
import datetime


def index(request):
    return render(request, 'login/index.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = password_hash, birthday = request.POST['birthday'])
        return redirect('/success/'+ str(user.id))


def login(request):
    user = User.objects.get(email=request.POST['email'])
    if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        return redirect('/success/'+ str(user.id))
    else:
        errors['passauth'] = 'E-mail and/or password incorrect.'
        return redirect('/')

def success(request, id):
    return render(request, 'login/success.html', {'user': User.objects.get(id=id)})