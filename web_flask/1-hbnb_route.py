#!/usr/bin/python3
"""script that starts a Flask web application
listening on 0.0.0.0, port 5000
Routes:
    /: display "Hello HBNB!"
    /hbnb: display “HBNB”
use the option strict_slashes=False in your route definition
USAGE: python3 -m web_flask.1-hbnb_route
curl 0.0.0.0:5000/hbnb ; echo "" | cat -e
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """used to generate URLs for that particular function, and
    returns the message we want to display in the user’s browser."""
    return ('Hello HBNB!')

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """used to generate URLs for that particular function, and
    returns the message we want to display in the user’s browser."""
    return ('HBNB')


if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000)
