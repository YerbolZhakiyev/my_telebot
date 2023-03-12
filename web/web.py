import requests
import psycopg2
from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)
@app.route('/')
def index():
    data = json.load(open('app/data.json', 'r'))
    return render_template('index.html', data=data)

@app.route('/about')
def about():
   return "about page"

if __name__ == '__main__':
    app.run(debug=True)