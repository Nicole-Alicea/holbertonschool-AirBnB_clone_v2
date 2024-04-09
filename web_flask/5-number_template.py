#!/usr/bin/python3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return 'C ' + str(text.replace('_', ' '))

@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python_text(text='is cool'):
    return 'Python ' + str(text.replace('_', ' '))

@app.route('/number/<n>', strict_slashes=False)
def number(n):
    if n.isdigit():
        return n + ' is a number'
    else:
        return 'Error: n must be an integer'
    
@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    if n.isdigit():
        return render_template('5-number.html', value=int(n))
    else:
        return 'Error: n must be an integer'
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)