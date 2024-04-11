#!/usr/bin/python3
'''This script starts a Flask web application'''

from flask import Flask, render_template


app = Flask(__name__, template_folder="templates")
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    '''Will display the following string when accessed'''

    return 'Hello HBNB!'


@app.route('/hbnb/')
def hbnb():
    '''Will display the following string when accessed'''

    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    '''Will display the following string when accessed. Receives a value in
    the text variable and replaces '_' with spaces'''

    return 'C ' + str(text.replace('_', ' '))


@app.route('/python/<text>')
@app.route('/python/')
def python_text(text='is cool'):
    '''Will display the following string when accessed. Receives a value in
    the text variable and replaces '_' with spaces. If no value is written,
    it will use the default'''

    return 'Python ' + str(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    '''Will display the following string when accessed only if the value
    received is an integer'''

    if isinstance(n, int):
        return n + ' is a number'


@app.route('/number_template/<int:n>')
def number_template(n):
    '''Will display an HTML page when accessed only if the value received is
    an integer'''

    if isinstance(n, int):
        return render_template('5-number.html', value=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
