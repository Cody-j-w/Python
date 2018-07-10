from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = '1337clicks'

@app.route('/')
def index():
    if 'count' in session:
        session['count'] = session.get('count') +1
    else:
        session['count'] =  1
    return render_template('index.html', count = session['count'])

@app.route('/destroy_session')
def end_session():
    for key in session.keys():
        session.pop(key)
        return redirect('/')

@app.route('/double_visit')
def x2():
    if 'count' in session:
        session['count'] = session.get('count') +1
    else:
        session['count'] = 2
    return redirect('/')

@app.route('/reset')
def reset():
    session['count'] = 1
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)