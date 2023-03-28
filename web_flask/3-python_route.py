#!/usr/bin/python3
"""
Task 3 - Python is cool!
Script that starts a Flask web application listening on 0.0.0.0, port 5000
Route: /: display "Hello HBNB!"
Route: /hbnb: display "HBNB"
Route: /c/<text>: display “C ” followed by the value of the text variable
Route: /python/<text>: display "Python " followed by val of text var
default text value = "is cool"
Use strict_slashes=False in route decorator
"""
from flask import Flask


# Create instance of Flask
app = Flask(__name__)


# Route decorator for '/' URL, trailing slashes = ignored
@app.route('/', methods=['GET'], strict_slashes=False)
def hello_hbnb():
    """ Route func that returns gretting message """
    return "Hello HBNB!"


# Route decorator for '/hbnb' URL, trailing slashes = ignored
@app.route('/hbnb', methods=['GET'], strict_slashes=False)
def hbnb():
    """ Route func that returns 'HBNB' """
    return "HBNB"


# Route decorator for /c/<text> URL, trailing slashes = ignored
@app.route('/c/<text>', methods=['GET'], strict_slashes=False)
def c(text):
    """ Route func that returns 'C <text>' """
    return 'C {}'.format(text.replace('_', ' '))


# Route decorator for /python/<text> URL, def text = is cool
# trailing slashes = ignored
@app.route('/python/', methods=['GET'], defaults={'text': 'is cool'},
           strict_slashes=False)
@app.route('/python/<text>', methods=['GET'], strict_slashes=False)
def python(text):
    """ Route fun that returns 'Python <text>' """
    return 'Python {}'.format(text.replace('_', ' '))

# specify host as 0.0.0.0 and port as 5000 using app.run() method
if __name__ == '__main__':
    """ Ensure web app is only started if script is run directly """
    app.run(host='0.0.0.0', port=5000)
