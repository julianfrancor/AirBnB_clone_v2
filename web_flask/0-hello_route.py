#!/usr/bin/python3
"""script that starts a Flask web application
the web application must be listening on 0.0.0.0, port 5000
Routes: '/': display "Hello HBNB!"
You must use the option strict_slashes=False in your route definition
USAGE: python3 -m web_flask.0-hello_route
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """used to generate URLs for that particular function, and
    returns the message we want to display in the user’s browser."""
    return ('Hello HBNB!')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
