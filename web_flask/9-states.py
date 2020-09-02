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


@app.route('/states', strict_slashes=False, defaults={'id': None})
@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    """display cities_by_states inside the tag BODY 'UL' """
    dictionary = storage.all(State)
    if id is None:
        return render_template('9-states.html', dictionary=dictionary)
    for state in dictionary.values():
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown(whatever):
    """After each request you must remove the current
    SQLAlchemy Session"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
