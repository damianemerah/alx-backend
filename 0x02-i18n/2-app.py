#!/usr/bin/env python3
""" Basic Flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel



class Config(object):
    """ Config class for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"



app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)
app.url_map.strict_slashes = False


@babel.localeselector
def get_locale() -> str:
    """Determines the best match with our supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """ Returns a string"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
