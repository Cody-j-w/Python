from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from apps.users.models import *

def index(request):

    return render(request, 'users/index.html', {'users': User.objects.all()})

def new(request):
    return render(request, 'users/new.html')

def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/users/new')
    else:
        
        user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])
        return redirect (str(user.id))

def show(request, id):
    return render(request, 'users/user.html', {'users': User.objects.get(id = id)})

def update(request, id):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/users/'+ str(id) + '/edit')
    else:
        user = User.objects.get(id = id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        return redirect('/users/' + str(id))

def edit(request, id):
    return render(request, 'users/edit.html', {'users': User.objects.get(id = id)})

def destroy(request, id):
    User.objects.get(id = id).delete()
    return redirect('/users')



