#!/usr/bin/python3
"""
Task 6 - Odd or even?
Script that starts a Flask web application listening on 0.0.0.0, port 5000
Route: /: display "Hello HBNB!"
Route: /hbnb: display "HBNB"
Route: /c/<text>: display “C ” followed by the value of the text variable
Route: /python/<text>: display "Python " followed by val of text var
- default text value = "is cool"
Route: /number/<n>: display “n is a number” only if n is an integer
Route: /number_template/<n>: display a HTML page only if n is an integer:
- H1 tag: “Number: n” inside the tag BODY
Route: /number_odd_or_even/<n>: display a HTML page only if n is an integer:
- H1 tag: “Number: n is even|odd” inside the tag BODY
Use strict_slashes=False in route decorators
"""
from flask import Flask, render_template


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
    """ Route func that returns 'Python <text>' """
    return 'Python {}'.format(text.replace('_', ' '))


# Route decorator for /number/<n> URL, used only if n is int
# trailing slashses = ignored
@app.route('/number/<int:n>', methods=['GET'], strict_slashes=False)
def number(n):
    """ Route func that returns '<int:n> is a number' """
    return '{} is a number'.format(n)


# Route dec for /number_template/<n> URL
# display HTML page only if n is int
# trailing slashes = ignored
@app.route('/number_template/<int:n>', methods=['GET'], strict_slashes=False)
def number_template(n):
    """ Route fun that renders template if n is int """
    return render_template('5-number.html', n=n)


# Route dec for /number_odd_or_even/<int:> URl
# display HTML page only if n is int or even/odd
# trailing slashes = ignored
@app.route('/number_odd_or_even/<int:n>', methods=['GET'], strict_slashes=False)
def number_odd_or_even(n):
    """ Route func that renders template if n is int """
    if n % 2 == 0:
        odd_or_even = "even"
    else:
        odd_or_even = "odd"
    return render_template('6-number_odd_or_even.html', n=n, odd_or_even=odd_or_even)

# specify host as 0.0.0.0 and port as 5000 using app.run() method
if __name__ == '__main__':
    """ Ensure web app is only started if script is run directly """
    app.run(host='0.0.0.0', port=5000)
