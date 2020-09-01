#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_holberton():
    """Return some stuff"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
