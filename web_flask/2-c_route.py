#!/usr/bin/python3
'''This script starts a Flask web application'''
from flask import Flask


app = Flask(__name__)
'''Creates a Flask application instance'''

@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''Will display the following string when accessed'''
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Will display the following string when accessed'''
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    '''Will display the following string when accessed. Receives a value in
    the text variable and replaces '_' with spaces'''
    return 'C ' + str(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
