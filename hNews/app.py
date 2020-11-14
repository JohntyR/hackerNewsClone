import os
from flask import Flask
from flask import make_response
from flask import render_template

app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('front_page.html')

@app.errorhandler(404)
def other_page(e):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))