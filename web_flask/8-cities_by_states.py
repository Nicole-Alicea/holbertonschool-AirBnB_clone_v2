#!/usr/bin/python3
'''This script starts a Flask web application'''

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states/')
def cities():
    '''Will display an HTML page containing a list,
    sorted by name, of cities by states'''
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda state: state.name)

    for state in states:
        state.cities.sort(key=lambda state: state.name)

    city_dict = {
        'states': sorted_states
    }

    return render_template('8-cities_by_states.html', **city_dict)


@app.teardown_appcontext
def teardown():
    '''Will remove the current SQLAlchemy Session after each request'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
