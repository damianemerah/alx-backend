#!/usr/bin/env python3
""" Basic Flask app with Mock logging in"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict


class Config(object):
    """ Config class for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)
app.url_map.strict_slashes = False


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """ Returns a user dictionary or
        None if the ID cannot be found
    """
    try:
        return users.get(int(request.args.get('login_as')))
    except Exception:
        return None


@app.before_request
def before_request():
    """ Finds a user if any, and set it as a
        global on flask.g.user
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Determines the best match with our supported languages"""
    if request.args.get('locale') in app.config['LANGUAGES']:
        return request.args.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ Returns a string"""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
