from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def checkerboard8x8():
    return render_template("index.html", x = 8, y = 8)

@app.route('/<x>/<y>')
def checkerboard(x,y):
    length = int(x)
    size = int(y)
    return render_template("index.html", x = length, y = size)

if __name__=="__main__":
    app.run(debug=True)