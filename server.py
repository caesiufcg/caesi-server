from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from flask_script import Manager
import requests

app = Flask(__name__)
CORS(app) 

@app.route("/")
def hello():
     return render_template('hello.html')
