#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_holberton():
    """Return some stuff"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return some stuff"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Return some stuff"""
    txt = text.replace('_', ' ')
    return 'C {}'.format(txt)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """Return some stuff"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """Return some stuff"""
    if n.isnumeric():
        return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
