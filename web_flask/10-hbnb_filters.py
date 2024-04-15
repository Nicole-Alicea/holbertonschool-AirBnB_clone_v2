#!/usr/bin/python3
'''This script will start a Flask web application'''

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown"""
    storage.close() 
    

@app.route('/hbnb_filters/')
def filters():
    """Will display an HTML page like 6-index.html from static"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
