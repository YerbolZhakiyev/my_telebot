#--------backend--------------
import requests
import psycopg2
from flask import Flask, render_template, jsonify

conn = psycopg2.connect(
      dbname='tg_bot',
      user='postgres', 
      password='password',
      host='64.227.127.179',
      port='5432'
   )
cursor = conn.cursor()

app = Flask(__name__)
@app.route('/')
   return "Hello"


if __name__ == '__main__':
    app.run(debug=True)