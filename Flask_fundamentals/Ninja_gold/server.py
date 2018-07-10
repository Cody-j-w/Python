from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'N33NJAA'

@app.route('/')
def index():
    alert_message = []
    if 'gold' not in session:
        session['gold'] = 0
    if 'alert message' not in session:
        session['alert message'] = ['<li class="text-light">welcome, ninja!</li>']
    elif 'alert message' in session:
        alert_message = reversed(session['alert message'])
    return render_template("index.html", alert_message = alert_message, gold = session['gold'])

@app.route('/process_money', methods=['post'])
def money():
    casino_gold = random.randint(-50,50)
    farm_gold = random.randint(5,10)
    cave_gold = random.randint(10,20)
    house_gold = random.randint(0,5)
    session['building'] = request.form['building']
    if session['building'] == 'farm':
        session['gold'] += farm_gold
        session['alert message'].append('<li class="text-success lead">you find ' + str(farm_gold) + ' gold in old barn!</li>')
    elif session['building'] == 'cave':
        session['gold'] += cave_gold
        session['alert message'].append('<li class="text-success lead">you find ' + str(cave_gold) + ' gold hidden in the pirate caves!</li>')
    elif session['building'] == 'house':
        session['gold'] += house_gold
        session['alert message'].append('<li class="text-success lead">you find ' + str(house_gold) + ' gold tucked behind a dresser in the abandoned house!</li>')
    elif session['building'] == 'casino' and int(session['gold']) > 50:
        session['gold'] += casino_gold
        if casino_gold > 0:
            session['alert message'].append('<li class="text-success lead">Well done! You won ' + str(casino_gold) +' gold! Care for another round?</li>')
        elif casino_gold<0:
            session['alert message'].append('<li class="text-danger lead ">You lost ' + str(-casino_gold) + ' gold! Better luck next time! </li>')
    elif session['building'] == 'casino' and int(session['gold'])<50:
        session['alert message'].append('<li class="text-danger lead">come back when you have more money!</li>')
        print(session['alert message'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')
    


app.run(debug=True)