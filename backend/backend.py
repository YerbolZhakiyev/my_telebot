import psycopg2
from flask import Flask, render_template, jsonify

conn = psycopg2.connect(dbname='tg_bot',
                        user='erbol', 
                        password='password',
                        host='db',
                        port='5432')

cursor = conn.cursor()

app = Flask(__name__)
@app.route('/')
def index():
	cursor.execute("SELECT * FROM orders")
	rows = cursor.fetchall()
	results = []
	for row in rows:
		results.append({'id': row[0], 'description': row[1], 'from_address': row[2], 'to_address': row[3], 'weight': row[4], 'phone': row[5]})

	return results

if __name__ == '__main__':
	app.run(debug=True)