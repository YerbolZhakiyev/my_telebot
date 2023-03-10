#--------backend--------------
import requests
import psycopg2
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
	conn = psycopg2.connect(dbname='tg_bot',
                        user='postgres', 
                        password='password',
                        host='64.227.127.179',
                        port='5432')
	cursor = conn.cursor()

	cursor.execute("SELECT * FROM orders")
	orders = cursor.fetchall()
	cursor.close()
   conn.close()
   return render_template('index.html', orders=orders)
 if __name__ == '__main__':
    app.run(port=80)
