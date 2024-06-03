from flask import Flask
from psycopg2 import connect

app = Flask(__name__)

host = 'localhost'
port = '5432'
dbname = 'postgres'
user = 'postgres'
password = '<PASSWORD>'


def get_connection():
    conn = connect(host=host, port=port, dbname=dbname, user=user, password=password)
    return conn


@app.get('/')
def home():  # put application's code here
    conn = get_connection()
    cur = conn.cursor()

    result = cur.execute('SELECT 1 + 1')
    print(result)
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)  # Debug active to reboot the code automatically
