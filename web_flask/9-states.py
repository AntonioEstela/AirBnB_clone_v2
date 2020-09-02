#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """Display all states in the database"""
    if id:
        id = 'State.{}'.format(id)

    states = storage.all(State)
    return render_template('9-states.html', id=id, states=states)


@app.teardown_appcontext
def db_close(self):
    """Method to close the session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
