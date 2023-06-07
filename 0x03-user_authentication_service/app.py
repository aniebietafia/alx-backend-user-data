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


def users():
    """Register users"""
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except Exception:
        return jsonify({"message": "email already registered"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
