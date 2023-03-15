import psycopg2
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
cursor.close()
conn.close()