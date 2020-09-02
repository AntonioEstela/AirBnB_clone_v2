#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template, g
from models.state import State
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display all states in the database"""
    data = storage.all(State).values()
    return render_template('7-states_list.html', states=data)


@app.teardown_appcontext
def db_close(self):
    """Method to close the session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
