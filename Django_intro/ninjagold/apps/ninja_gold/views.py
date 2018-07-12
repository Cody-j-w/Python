from django.shortcuts import render, redirect, HttpResponse
from random import randint


def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'alert message' not in request.session:
        request.session['alert message'] = ['<li class="text-light">welcome, ninja!</li>']
    elif 'alert message' in request.session:
        alert_message = reversed(request.session['alert message'])
    context = {
        'alert_message': reversed(request.session['alert message'])
        }
    return render(request, 'ninja_gold/index.html', context)

def process(request):
    loot = 0
    temp_message = request.session['alert message']
    request.session['building'] = request.POST['building']
    if request.session['building'] == 'farm':
        loot = randint(5,10)
        request.session['gold'] += loot
        temp_message.append('<li class="text-success lead">you find ' + str(loot) + ' gold in old barn!</li>')
        request.session['alert message'] = temp_message
    elif request.session['building'] == 'cave':
        loot = randint(10,20)
        request.session['gold'] += loot
        temp_message.append('<li class="text-success lead">you find ' + str(loot) + ' gold hidden in the pirate caves!</li>')
        request.session['alert message'] = temp_message
    elif request.session['building'] == 'house':
        loot = randint(0,5)
        request.session['gold'] += loot
        temp_message.append('<li class="text-success lead">you find ' + str(loot) + ' gold tucked behind a dresser in the abandoned house!</li>')
        request.session['alert message'] = temp_message
    elif request.session['building'] == 'casino' and int(request.session['gold']) > 50:
        loot = randint(-50,50)
        request.session['gold'] += loot
        if loot > 0:
            temp_message.append('<li class="text-success lead">Well done! You won ' + str(loot) +' gold! Care for another round?</li>')
            request.session['alert message'] = temp_message
        elif loot<0:
            temp_message.append('<li class="text-danger lead ">You lost ' + str(-loot) + ' gold! Better luck next time! </li>')
            request.session['alert message'] = temp_message
    elif request.session['building'] == 'casino' and int(request.session['gold'])<50:
        temp_message.append('<li class="text-danger lead">come back when you have more money!</li>')
        request.session['alert message'] = temp_message
    print(temp_message)
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')