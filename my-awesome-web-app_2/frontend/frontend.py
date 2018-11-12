from flask import Flask, render_template
import requests
import json
import os
import unicodedata

app = Flask(__name__)

@app.route('/')
def getallstuff():
    port = os.environ['BACKEND_HOST']
    head = {"Accept": "text/plain", 'Accept-Charset': 'UTF-8'}
    joke = requests.get(('http://%s/getjoke' % port), headers=head)
    person = requests.get(('http://%s/getperson' % port), headers=head)
    dog = requests.get(('http://%s/getdog' % port), headers=head)
    dogtxt = dog.text
    json_data = json.loads(unicodedata.normalize('NFKD', dogtxt).encode('ascii','ignore'))
    dogurl = json_data['message']
    return render_template('index.html', jk=joke.text, us=person.text, dog=dogurl)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8111)

