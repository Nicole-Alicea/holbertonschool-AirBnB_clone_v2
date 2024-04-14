#!/usr/bin/python3
'''This script starts a Flask web application'''

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list/')
def states():
    '''Will display an HTML page containing a list of States
    sorted by name'''
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown():
    '''Will remove the current SQLAlchemy Session after each request'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)