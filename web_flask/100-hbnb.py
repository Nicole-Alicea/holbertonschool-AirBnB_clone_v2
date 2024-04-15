#!/usr/bin/pyhton3
'''This script starts a Flask web application'''
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(exception):
    '''Will remove the current SQLAlchemy Session after each request'''
    storage.close()


@app.route('/hbnb/')
def hbnb():
    '''Will display an HTML page like 8-index.html'''
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('100-hbnb.html', states=states,
                           amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
