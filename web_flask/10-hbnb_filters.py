#!/usr/bin/python3
"""
Script that starts a Flask web application listening on 0.0.0.0:5000
Use storage for fetching data from the storage engine File or DB storage
from models import storage and storage.all(...)
To load all cities of a State:
    If storage engine is DBStorage, use cities relationsship
    Otherwise, use the public getter method cities
After each request, remove current SQLAlchemy Session:
    Declare method to handle @app.teardown_appcontext
    Call in this method: storage.close()
Route /hbnb_filters: display a HTML page like 6-index.html from web-static
Must use option strict_slashes=False
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/hbnb_filters")
def hbnb_filters():
    """
    Displays an HTML formatted of cities with a given State id
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html", state_list=states,
                           amenity_list=amenities)


@app.teardown_appcontext
def teardown(stuff):
    """
    Remove current SQLAlchemy session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
