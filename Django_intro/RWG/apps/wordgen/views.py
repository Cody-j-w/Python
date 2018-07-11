from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.utils.crypto import get_random_string


def index(request):
    request.session['random'] = get_random_string(length=14)
    request.session['attempts'] += 1
    

    return render( request, 'wordgen/index.html')

def reset(request):
    request.session['attempts'] = 0
    return HttpResponseRedirect('/wordgen')

def randomize(request):
    return HttpResponseRedirect('/wordgen')
