#!/usr/bin/python3
'''This script starts a Flask web application'''

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/states/')
def states():
    '''Will display an HTML page'''
    return render_template('9-states.html')


@app.route('/states/<id>')
def states_id():
    '''Will display an HTML page'''
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown():
    '''Will remove the current SQLAlchemy Session after each request'''
    storage.close()