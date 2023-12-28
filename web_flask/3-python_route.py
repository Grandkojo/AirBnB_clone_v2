#!/usr/bin/python3

"""This script returns hello hbnb or HBNB depending on the route"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """The function from hello hbnb"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """The function for hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Returns c with additional text"""
    return f"C {text.replace('_', ' ')}"

@app.route("/python/<text>", strict_slashes=False)
def hpython(text):
    """Returns default text, if text is NULL"""
    if text is Null:
        return "Python is cool"
    else:
        return f"Python {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
