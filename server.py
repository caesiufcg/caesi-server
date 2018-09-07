from flask import Flask, request, abort
from flask_cors import CORS, cross_origin
from flask_script import Manager
import requests

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "EM BREVE!"
