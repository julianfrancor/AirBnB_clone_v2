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
from models.place import Place
from models.user import User

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb_filters():
    """display cities_by_states inside the tag BODY 'UL' """
    list_states = storage.all(State).values()
    list_amenities = storage.all(Amenity).values()
    list_places = storage.all(Place).values()
    list_users = storage.all(User).values()
    return render_template('100-hbnb.html', states=list_states,
                           amenities=list_amenities, places=list_places,
                           users=list_users)


@app.teardown_appcontext
def teardown(self):
    """After each request you must remove the current
    SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
