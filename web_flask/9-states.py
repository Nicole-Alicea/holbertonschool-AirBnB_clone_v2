#!/usr/bin/python3
'''This script starts a Flask web application'''

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(exception):
    '''Will remove the current SQLAlchemy Session after each request'''
    storage.close()


@app.route('/states/')
def states():
    '''Will display an HTML page with a list of all States'''
    states = storage.all(State)
    return render_template('9-states.html', state=states)


@app.route('/states/<id>')
def states_id(id):
    '''Will display an HTML page'''
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
