from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key="yourthoughtsmatter"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/results', methods=['POST'])
def surveyForm():
    error = 0
    if len(request.form['name'])<1:
        flash('name is a required field!')
        error += 1
    elif len(request.form['name'])>64:
        flash('Name must be under 64 characters!')
        error +=1
    else:
        session['name'] = request.form['name']

    if len(request.form['email'])<1:
        flash('E-mail is a required field!')
        error +=1
    elif len(request.form['email'])>120:
        flash('E-mail must be under 120 characters!')
        error +=1
    else:
        session['email'] = request.form['email']

    session['language'] = request.form['language']

    if len(request.form['comments'])<1:
        flash('Comments is a required field!')
        error +=1
    elif len(request.form['comments'])>120:
        flash('Comments must be under 120 characters!')
        error +=1
    else:
        session['comments'] = request.form['comments']

    session['location'] = request.form['location']
    if error > 1:
        return redirect('/')
    else:
        return redirect('/user_info')

@app.route('/user_info')
def user_info():
    return render_template('results.html', name = session['name'], email = session['email'], language = session['language'], location = session['location'], comments = session['comments'])

@app.route('/danger')
def reroute():
    print("User has tried to access /danger. They have been redirected to root")
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)