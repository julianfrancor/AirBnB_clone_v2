#!/usr/bin/python3
"""script that starts a Flask web application
→ the web application listens on 0.0.0.0 , port 5000
→ You must use storage for fetching data from the storage engine
  (FileStorage or DBStorage)

"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """display cities_by_states inside the tag BODY 'UL' """
    dictionary = storage.all(State)
    return render_template('8-cities_by_states.html', dictionary=dictionary)


@app.teardown_appcontext
def teardown(whatever):
    """After each request you must remove the current
    SQLAlchemy Session"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
