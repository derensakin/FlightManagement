from flask import Flask


def create_app():
    _app = Flask(__name__)

    _app.config["SECRET_KEY"] = "SECRET KEY"

    return _app
