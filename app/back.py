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

@app.route('/orders')
def get_orders():
   cursor.execute("SELECT * FROM orders")
   rows = cursor.fetchall()
   data = []
   for row in rows:
      data.append({'id': row[0], 'description': row[1], 'weight': row[2], 'from_address': row[3], 'to_address': row[4], 'phone': row[5]})
   return jsonify({'data': data})

if __name__ == '__main__':
    app.run()