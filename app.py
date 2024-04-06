from flask import Flask
app = Flask(__name__)
import psycopg2

@app.route('/')
def hello_world():
    return 'Hello, World from Andrew Byrnes in 3308!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://hello_world_postgres_user:thSKOlH19WgLeN8VVIWTwFX9Ss0H6w4e@dpg-co89135jm4es738vll40-a/hello_world_postgres")
    conn.close()
    return "Database Connection Successful" 

@app.route('/db_create')
def creating():
    conn=psycopg2.connect("postgres://hello_world_postgres_user:thSKOlH19WgLeN8VVIWTwFX9Ss0H6w4e@dpg-co89135jm4es738vll40-a/hello_world_postgres")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
            );
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"

