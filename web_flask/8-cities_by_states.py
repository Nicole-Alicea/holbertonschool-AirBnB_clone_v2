#!/usr/bin/python3
'''This script starts a Flask web application'''

from flask import Flask, render_template
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states/')
def cities():
    '''Will display an HTML page containing a list of cities by states'''


@app.teardown_appcontext
def teardown():
    '''Will remove the current SQLAlchemy Session after each request'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
