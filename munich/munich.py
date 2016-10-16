from flask import Flask, jsonify


application = Flask(__name__)


@application.route('/')
def index():
    data = {
        'celsius': 20.78
    }

    return jsonify(data)
