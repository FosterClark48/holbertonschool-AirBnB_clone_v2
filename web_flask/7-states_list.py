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
app.url_map.strict_slashes = False


# Route decorator for '/' URL, trailing slashes = ignored
@app.route('/')
def hello_hbnb():
    """ Route func that returns gretting message """
    return "Hello HBNB!"


# Route decorator for '/hbnb' URL, trailing slashes = ignored
@app.route('/hbnb')
def hbnb():
    """ Route func that returns 'HBNB' """
    return "HBNB"


# Route decorator for /c/<text> URL, trailing slashes = ignored
@app.route('/c/<text>')
def c(text):
    """ Route func that returns 'C <text>' """
    return 'C {}'.format(text.replace('_', ' '))


# Route decorator for /python/<text> URL, def text = is cool
# trailing slashes = ignored
@app.route('/python/')
@app.route('/python/<text>')
def python(text="is cool"):
    """ Route func that returns 'Python <text>' """
    return 'Python {}'.format(text.replace('_', ' '))


# Route decorator for /number/<n> URL, used only if n is int
# trailing slashses = ignored
@app.route('/number/<int:n>')
def number(n):
    """ Route func that returns '<int:n> is a number' """
    return '{} is a number'.format(n)


# Route dec for /number_template/<n> URL
# display HTML page only if n is int
# trailing slashes = ignored
@app.route('/number_template/<int:n>')
def number_template(n):
    """ Route fun that renders template if n is int """
    return render_template('5-number.html', n=n)


# Route dec for /number_odd_or_even/<int:> URl
# display HTML page only if n is int or even/odd
# trailing slashes = ignored
@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """ Route func that renders template if n is int """
    if n % 2 == 0:
        odd_or_even = "even"
    else:
        odd_or_even = "odd"
    return render_template('6-number_odd_or_even.html', n=n,
                           odd_or_even=odd_or_even)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display HTML page w/ list of all states present in DBStorage"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """ Removes the current SQLAlchemy Session """
    storage.close()

# specify host as 0.0.0.0 and port as 5000 using app.run() method
if __name__ == '__main__':
    """ Ensure web app is only started if script is run directly """
    app.run(host='0.0.0.0', port=5000)
