import flask
from flask import Flask, request
import json

_flask = Flask(__name__)

@_flask.route('/', methods = ['GET'])
def flask_main():
    return "Hello"

def run(fn_main):
    global global_fn_main
    global_fn_main = fn_main
    _flask.run(debug = False, port = 8080, host = '0.0.0.0', threaded = True)
