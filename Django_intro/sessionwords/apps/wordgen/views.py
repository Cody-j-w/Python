from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    if 'wordlist' not in request.session:
        request.session['wordlist'] = []
    context = {
        'time': strftime('%I:%M %p, %B %d %Y', gmtime())
        }
    return render(request, 'wordgen/index.html', context)

def process(request):
    if request.method=='POST':
        if 'make_big' in request.POST:
            showbig = 'font-size:4rem;'
        else:
            showbig = ''
        temp_list = request.session['wordlist']
        temp_list.append({'newword': request.POST['word'], 'newcolor': request.POST['color'], 'show_big': showbig, 'newtime': strftime('%I:%M %p, %B %d %Y', gmtime())})
        request.session['wordlist'] = temp_list

        request.session['time'] = strftime('%I:%M %p, %B %d %Y', gmtime())

        print(request.session['wordlist'])
        

    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')