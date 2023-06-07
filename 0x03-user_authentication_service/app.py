#!/usr/bin/env python3
"""Flask app that has a single GET route ("/") and use
flask.jsonify to return a JSON payload of the form"""
from flask import Flask, jsonify, request, abort, redirect
form auth import Auth
app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=Flash)
def welcome():
    """Basic Flask app, return a JSON"""
    return jsonify({"message": "Bienvenue"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
