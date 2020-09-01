#!/usr/bin/python3
"""script that starts a Flask web application
→ the web application listens on 0.0.0.0 , port 5000
→ Routes:
    → /: display “Hello HBNB!”
    → /hbnb: display “HBNB”
    → /c/<text>: display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space )
    → /python/(<text>): display “Python ”, followed by the value of the
    text variable (replace underscore _ symbols with a space )
    → /number/<n>: display “n is a number” only if n is an integer
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """display “Hello HBNB!”"""
    return ''


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_C_text(text):
    """display “C ” followed by the value of the text variable"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_Python_text(text='is cool'):
    """display “C ” followed by the value of the text variable
        The default value of text is “is cool” """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    """display “n is a number” only if n is an integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_show_number(n):
    """display “n is a number” only if n is an integer"""
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
