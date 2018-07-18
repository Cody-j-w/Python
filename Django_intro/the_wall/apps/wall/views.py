from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from apps.wall.models import *


def index(request):
    return render(request, 'wall/index.html')

def register(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        username = User.objects.get(email = request.POST['email']).first_name
        request.session['user'] = username
        return redirect('/wall')


def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        username = User.objects.get(email = request.POST['email']).first_name
        user_id = User.objects.get(email = request.POST['email']).id
        request.session['user_id'] = user_id
        request.session['user'] = username
        return redirect('/wall')


def the_wall(request):
    context = {
        'users': User.objects.all(),
        'posts': Message.objects.order_by('-created_at')
    }
    return render(request, 'wall/the_wall.html', context)

def create_message(request):
    errors = Message.objects.message_creator(request.POST)
    return redirect('/wall')

def create_comment(request):
    print(request.POST)
    errors = Comment.objects.comment_creator(request.POST)
    return redirect('/wall')

def logout(request):
    request.session.clear()
    return redirect('/')