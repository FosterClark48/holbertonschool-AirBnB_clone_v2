#!/usr/bin/python3
"""
Script that starts a Flask web application listening on 0.0.0.0, port 5000
Routes: /: display "Hello HBNB!"
Use strict_slashes=False in route decorator
"""
from flask import Flask


# Create instance of Flask
app = Flask(__name__)

# Tell Flask what URL should trigger function, trailing slashes = ignored
@app.route('/', methods=['GET'], strict_slashes=False)
def hello():
    """Route func that returns gretting message"""
    return "Hello HBNB!"

# specify host as 0.0.0.0 and port as 5000 using app.run() method
if __name__ == '__main__':
    """Ensure web app is only started if script is run directly"""
    app.run(host='0.0.0.0', port=5000)
