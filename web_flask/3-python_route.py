#!/usr/bin/python3
"""starts a flask web application"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_HBNB():
    return "Hello HBNB!"


@app.route("/hbnb")
def HBNB():
    return "HBNB"


@app.route("/c/<text>")
def C(text):
    text = text.replace("_", " ")
    return ("C {}".format(text))


@app.route("/python")
@app.route("/python/<text>")
def P_text(text="is cool"):
    text = text.replace("_", " ")
    return ("Python {}".format(text))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
