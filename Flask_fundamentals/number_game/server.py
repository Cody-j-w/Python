from flask import Flask, render_template, request, redirect, session
import random


app = Flask(__name__)
app.secret_key = 'YOUCANTEVENGUESSTHENUMBER'

@app.route('/')
def numgame():
    if 'randomNum' not in session:
        session['randomNum'] = random.randrange(0,100)
    return render_template('index.html')

@app.route('/results', methods=['post'])
def results():
    if request.form['guess'] == '':
        return redirect('/')
    session['guess'] = request.form['guess']
    if int(session['guess']) == int(session['randomNum']):
        return redirect('/success')
    elif int(session['guess']) > int(session['randomNum']):
        return redirect('/toohigh')
    elif int(session['guess']) < int(session['randomNum']):
        return redirect('/toolow')


@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/toohigh')
def toohigh():
    return render_template('toohigh.html')

@app.route('/toolow')
def toolow():
    return render_template('toolow.html')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
