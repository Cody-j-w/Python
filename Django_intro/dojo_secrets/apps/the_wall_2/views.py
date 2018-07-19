from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from apps.the_wall_2.models import *


def index(request):
    return render(request, 'the_wall_2/index.html')

def register(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        username = User.objects.get(email = request.POST['email']).first_name
        user_id = User.objects.get(email = request.POST['email']).id
        request.session['user'] = username
        request.session['user_id'] = user_id
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
        'you': User.objects.get(id = request.session['user_id']),
        'users': User.objects.all(),
        'posts': Message.objects.order_by('-created_at')
    }
    return render(request, 'the_wall_2/wall.html', context)

def poplist(request):
    context = {
        'popular_posts': Message.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')[:10],
        'you': User.objects.get(id = request.session['user_id'])
    }
    return render(request, 'the_wall_2/poplist.html', context)

def create_message(request):
    errors = Message.objects.message_creator(request.POST)
    return redirect('/wall')

def like(request):
    errors = Message.objects.likes(request.POST)
    if request.POST['page_validator'] == 'wall':
        return redirect('/wall')
    if request.POST['page_validator'] == 'poplist':
        return redirect('/poplist')

def delete_message(request):
    errors = Message.objects.message_deletor(request.POST)
    if request.POST['page_validator'] == 'wall':
        return redirect('/wall')
    if request.POST['page_validator'] == 'poplist':
        return redirect('/poplist')

def logout(request):
    request.session.clear()
    return redirect('/')