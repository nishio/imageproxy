import requests
from flask import Flask
from flask import Response
from flask import request
import urllib
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def create_app():
    return app

@app.route('/gyazo.com/<hash>')
def gyazo(hash):
    url = f"https://gyazo.com/{hash}/thumb/400"
    r = requests.get(url, allow_redirects=True)
    r = Response(r.content, mimetype="image/png")
    r.headers['Access-Control-Allow-Origin'] = '*'
    r.headers['Cache-Control'] = 'max-age = 31536000'
    return r


@app.route('/get/')
def get():
    url = request.args["q"]
    url = urllib.parse.unquote(url)
    r = requests.get(url, allow_redirects=True)
    r = Response(r.content, mimetype="image/png")
    r.headers['Access-Control-Allow-Origin'] = '*'
    r.headers['Cache-Control'] = 'max-age = 31536000'
    return r
