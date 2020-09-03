#!/usr/bin/python3
"""script that starts a Flask web application
→ the web application listens on 0.0.0.0 , port 5000
→ You must use storage for fetching data from the storage engine
  (FileStorage or DBStorage)

"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """display cities_by_states inside the tag BODY 'UL' """
    list_states = storage.all(State).values()
    list_amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=list_states,
                           amenities=list_amenities)


@app.teardown_appcontext
def teardown(self):
    """After each request you must remove the current
    SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
