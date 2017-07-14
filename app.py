#/home/trial420/mysite/flask_app.py

import requests
from flask import Flask
app = Flask(__name__)

data = 'hi there'
r = requests.get('http://cbseresults.nic.in')
data = r.content

@app.route('/')
def hello_world():
    return data	