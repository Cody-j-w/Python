from flask import Flask
app = Flask(__name__)

@app.route('/')

def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/hello/<name>')

def say(name):
    print(name)
    return "hello "name

@app.route('/repeat/<num>/<object>')
    def count(num,object):
        length = int(num)
        value = object
        return value*length
