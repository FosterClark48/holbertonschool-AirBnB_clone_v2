#!/usr/bin/python3
"""
Task 8 - List of states
This is a Flask web application that displays a list of states sorted by name
from a database.
The web application listens on 0.0.0.0:5000 and uses either FileStorage
or DBStorage for fetching data from the storage engine.
After each request, the current SQLAlchemy Session is removed.

Routes:
    - /states_list: displays a HTML page with a list of all states present
    in the database sorted by name (A->Z)

Requirements:
    - Flask
    - SQLAlchemy

Usage: python3 <filename.py>

Notes:
    - Make sure database is populated with data before running this script.
    - A template file named "7-states_list.html" is required in a templates
    folder in the same directory as this script.
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display HTML page w/ list of all states present in DBStorage"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """ Removes the current SQLAlchemy Session """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
