import MySQLdb
import MySQLdb.cursors
from flask import Flask, render_template, json,jsonify

app = Flask(__name__)

database = MySQLdb.connect(host = "localhost",
    user = "root",
    passwd = "123456",
    db = "bolt_graph",
    cursorclass = MySQLdb.cursors.DictCursor)
cursor = database.cursor()

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/fetch_sensor_data",  methods=['GET'])
def fetch_sensor_data():
    lastest_data = get_sensor_data();
    return jsonify(data = lastest_data)

def get_sensor_data():
    cursor.execute("SELECT temperature, humidity, time_stamp FROM sensor_data \
                    ORDER BY time_stamp ASC")
    data = cursor.fetchall()
    return data


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
