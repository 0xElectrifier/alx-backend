#!/usr/bin/env python3
"""Module to Get Locale from request"""
from flask import (render_template, request, Flask)
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

def get_locale():
    """Returns the locale from request"""
    accepted_languages = request.accept_languages

    return (accepted_languages.best_match(app.config["LANGUAGES"]) or
            app.config["BABEL_DEFAULT_LOCALE"])

babel.init_app(app, locale_selector=get_locale)

@app.route("/")
def display_basic_page():
    """Displays a simple page to test Babel connection"""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run()
