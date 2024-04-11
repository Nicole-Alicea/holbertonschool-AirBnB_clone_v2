#!/usr/bin/python3
'''This script starts a Flask web application'''

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    '''Will display the following string when accessed'''

    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''Will display the following string when accessed'''

    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    '''Will display the following string when accessed. Receives a value in
    the text variable and replaces '_' with spaces'''

    return 'C ' + str(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
