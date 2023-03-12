import psycopg2
import json
import time
conn = psycopg2.connect(dbname='tg_bot',
                        user='postgres', 
                        password='password',
                        host='64.227.127.179',
                        port='5432')
cursor = conn.cursor()
while True:
	 cursor.execute("SELECT * FROM orders")
	 rows = cursor.fetchall()
	 results = []
	 for row in rows:
         results.append({'id': row[0], 'description': row[1], 'from_address': row[2], 'to_address': row[3], 'weight': row[4], 'phone': row[5]})
     time.sleep(60)
with open('data.json', 'w', encoding='utf-8') as f:
	json.dump(results, f, ensure_ascii=False)