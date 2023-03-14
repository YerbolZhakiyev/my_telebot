import psycopg2
from flask import Flask, jsonify, Response, request
import json
from dotenv import load_dotenv, find_dotenv
import os

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
DB_NAME = os.getenv('DATABASENAME')
DB_USER = os.getenv('DATABASEUSER')
DB_PASSWORD = os.getenv('DATABASEPASSWORD')
#-------------------Connect to db
conn = psycopg2.connect(dbname=DB_NAME,
                        user=DB_USER, 
                        password=DB_PASSWORD,
                        host='db',
                        port='5432')
cursor = conn.cursor()

app = Flask(__name__)

@app.route('/orders', methods = ['GET'])
def index(): 
	if request.method == 'GET':
		cursor.execute("SELECT * FROM orders")
		rows = cursor.fetchall()
		results = []
		for row in rows:
			results.append({'id': row[0], 'description': row[1], 'from_address': row[2], 'to_address': row[3], 'weight': row[4], 'phone': row[5]})
		orders = json.dumps({
			'data': results
			}, ensure_ascii = False)
		return Response(orders,content_type="application/json; charset=utf-8" )

if __name__ == '__main__':
	app.run(debug=True)
