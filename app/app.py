import psycopg2
import json
conn = psycopg2.connect(dbname='tg_bot',
                        user='postgres', 
                        password='password',
                        host='64.227.127.179',
                        port='5432')
cursor = conn.cursor()
cursor.execute("SELECT * FROM orders")
rows = cursor.fetchall()
results = []
for row in rows:
    results.append({'column1': row[0], 'column2': row[1], 'column3': row[2], 'column4': row[3], 'column5': row[4], 'column6': row[5]})
with open('app/data.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False)
cursor.close()
conn.close()