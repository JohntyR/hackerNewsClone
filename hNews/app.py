import os
import requests
import json
from flask import Flask
from flask import make_response
from flask import render_template
from urllib.parse import urlparse

app = Flask(__name__)

@app.route('/')
def landing_page(storyArray=None, urlArray=None):
    response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
    topStories = response.json()

    storyArray = []
    urlArray = []

    for i in range(5):
        itemNum = topStories[i]
        response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{itemNum}.json?print=pretty')
        responsejson = response.json()
        storyArray.append(responsejson)
        urlArray.append(urlparse(responsejson['url']).netloc)

    return render_template('front_page.html', storyArray=storyArray, urlArray=urlArray)

@app.errorhandler(404)
def other_page(e):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))