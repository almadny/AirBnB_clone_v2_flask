#!/usr/bin/python3
from flask import Flask
""" A Flask Application to Print Hello Word """
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def helloWorld():
    """ A function to return the string Hello world """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
