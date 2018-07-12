from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.utils.crypto import get_random_string


def index(request):
    request.session['random'] = get_random_string(length=14)
    if 'attempts' not in request.session:
        request.session['attempts'] = 0
    request.session['attempts'] += 1
    

    return render( request, 'wordgen/index.html')

def reset(request):
    request.session.clear()
    return HttpResponseRedirect('/')

def randomize(request):
    return HttpResponseRedirect('/')
