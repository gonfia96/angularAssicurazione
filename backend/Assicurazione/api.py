import flask as flask
from flask import request
import json

import Cliente

app = flask.Flask(__name__)


@app.route('/prova', methods=['POST'])
def apiClient():
    stringa = ''
    first_name = 'matte'
    last_name = 'gigi'
    stringa = "{ " + first_name + " : " + ", " + last_name + " }"
    json_object = json.loads(stringa)
    return json_object


app.run()
