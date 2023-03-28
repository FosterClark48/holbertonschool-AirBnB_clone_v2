#!/usr/bin/python3
"""
Task 1
Script that starts a Flask web application listening on 0.0.0.0, port 5000
Routes: /: display "Hello HBNB!"
Routes: /hbnb: display "HBNB"
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

# specify host as 0.0.0.0 and port as 5000 using app.run() method
if __name__ == '__main__':
    """ Ensure web app is only started if script is run directly """
    app.run(host='0.0.0.0', port=5000)
