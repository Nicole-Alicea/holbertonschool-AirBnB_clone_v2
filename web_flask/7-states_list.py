#!/usr/bin/python3
'''This script starts a Flask web application'''

from flask import Flask, render_template
from models import storage


app = Flask(__name__, template_folder="templates")
app.url_map.strict_slashes = False


@app.route('/states_list/')
def states():
    states = storage.all("State")
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown():
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)