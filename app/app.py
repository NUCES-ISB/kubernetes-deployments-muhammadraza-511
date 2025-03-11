from flask import Flask
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="postgres",
        database="mydb",
        user="postgres",
        password="password"
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    conn.close()
    return 'Database Connected!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
