import os
import json
import urllib.request
from bs4 import BeautifulSoup
from flask import Flask, request

app = Flask(__name__)
@app.route('/')
def hello():
    return 'Test OK'

@app.route('/findfbid', methods=['GET', 'POST'])
def findfbid():
    try :
        url = request.args.get('url')
        f = urllib.request.urlopen(url)
        content = f.read()
        soup = BeautifulSoup(content, 'html.parser')
        temp = soup.find('meta', attrs={'property': 'al:android:url'})
        temp = str(temp).split('\" ')[0]
        temp = temp.split('/')[-1]
        data = {}
        data['fbid'] = temp
        json_data = json.dumps(data)
        return json_data
    except :
        data = {}
        data['fbid'] = 'none'
        json_data = json.dumps(data)
        return json_data

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

