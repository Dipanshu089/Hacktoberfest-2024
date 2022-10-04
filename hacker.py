import flask
from pytz import timezone
from flask import request, jsonify
from flask_cors import CORS
import psycopg2
import datetime
import os

app = flask.Flask(__name__)

dbURL = os.environ.get('DATABASE_URL')

@app.route('/updateLocation', methods=['GET'])
def updateLocation():
    print("Updating location...")
    args = request.args
    number = args['number']
    latitude = args['latitude']
    longitude = args['longitude']
    dateTime = datetime.datetime.now(timezone('Asia/Kolkata'))
    dateTime = dateTime.strftime('%Y-%m-%d %H:%M')
    conn = psycopg2.connect(dbURL)
    cur = conn.cursor()
    cur.execute("INSERT INTO locationData (number, latitude, longitude, date) VALUES (%s, %s, %s, %s)", (number, latitude, longitude, dateTime))
    conn.commit()
    conn.close()
    return "Updated", 200

@app.route('/getLastLocation', methods=['GET'])
def getLastLocation():
    try:
        print("Getting last location...")
        args = request.args
        number = args['number']
        conn = psycopg2.connect(dbURL)
        cur = conn.cursor()
        cur.execute("SELECT latitude, longitude, date FROM locationData WHERE number = %s ORDER BY date DESC LIMIT 1", (number,))
        row = cur.fetchone()
        conn.close()
        return jsonify(row), 200
    except Exception as e:
        print(e)
        return "Error", 500

@app.route('/getLocations', methods=['GET'])
def getLocations():
    try:
        print("Getting locations...")
        args = request.args
        number = args['number']
        conn = psycopg2.connect(dbURL)
        cur = conn.cursor()
        cur.execute("SELECT latitude, longitude, date FROM locationData WHERE number = %s ORDER BY date DESC LIMIT 5", (number,))
        rows = cur.fetchall()
        conn.close()
        return jsonify(rows), 200
    except Exception as e:
        print(e)
        return "Error", 500

def init():
    print("Initializing...")
    conn = psycopg2.connect(dbURL)
    cur = conn.cursor()
    createTable = """CREATE TABLE IF NOT EXISTS locationData (
                            id SERIAL PRIMARY KEY,
                            number BIGINT NOT NULL, 
                            latitude VARCHAR(500) NOT NULL,
                            longitude VARCHAR(500) NOT NULL,
                            date TIMESTAMPTZ NOT NULL
                            );"""
    cur.execute(createTable)
    conn.commit()
    conn.close()

#app.run()
if __name__ == "__main__":
    init()
    CORS(app)
    app.debug = False
    app.run("0.0.0.0",port=5000,threaded=True)
