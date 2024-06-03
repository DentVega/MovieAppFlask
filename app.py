from flask import Flask, request
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

    cur.execute('SELECT 1 + 1')
    result = cur.fetchone()
    print(result)
    return 'Hello World!'


@app.get('/api/movies')
def get_movies():
    return 'Getting Movies!'


@app.post('/api/movies')
def create_movie():
    new_movie = request.get_json()
    print(new_movie)
    return 'Creating Movies!'


@app.delete('/api/movies/1')
def delete_movie():
    return 'Deleting Movies!'


@app.put('/api/movies/1')
def update_movie():
    return 'Updating Movies!'


@app.get('/api/movies/1')
def get_movie():
    return 'Getting Movie 1!'


if __name__ == '__main__':
    app.run(debug=True)  # Debug active to reboot the code automatically
