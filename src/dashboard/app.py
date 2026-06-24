"""Minimal Flask dashboard placeholder."""

from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "Graph-Based Network Attack Detection Dashboard"

    return app
