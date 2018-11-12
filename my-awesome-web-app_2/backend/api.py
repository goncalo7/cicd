from flask import Flask
import requests
import json
import os


app = Flask(__name__)

@app.route('/getjoke')
def getjoke():
    head = {"Accept": "text/plain", 'Accept-Charset': 'UTF-8'}
    r = requests.get('https://icanhazdadjoke.com/', headers=head)
    return r.text

@app.route('/getdog')
def getdog():
    head = {"Accept": "text/plain", 'Accept-Charset': 'UTF-8'}
    r = requests.get('https://dog.ceo/api/breeds/image/random', headers=head)
    return r.text

@app.route('/getperson')
def getperson():
    head = {"Accept": "text/plain", 'Accept-Charset': 'UTF-8'}
    r = requests.get('http://uinames.com/api/', headers=head)
    return r.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8110)

