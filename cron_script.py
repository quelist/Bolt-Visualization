import MySQLdb
import MySQLdb.cursors

import json
import requests



database = MySQLdb.connect(host = "localhost",
    user = "root",
    passwd = "123456",
    db = "bolt_graph",
    cursorclass = MySQLdb.cursors.DictCursor)
cursor = database.cursor()



def init():
    serialBegin()
    data  = json.loads(serialRead())
    sensor_data = data['value'].split(",")
    store_value(sensor_data[0], sensor_data[1])

def store_value(temp, hum):
    query = "INSERT INTO sensor_data (temperature, humidity) VALUES (%s,%s)" %(temp,hum)
    print (query)
    cursor.execute(query)
    database.commit()
    return True

def serialBegin():
    url = "http://beta.boltiot.com/remote/d219c589-ec8b-4947-a622-d1e3095ef4f4/serialBegin"
    querystring = {"baud":"9600","deviceName":"BOLT366397"}
    headers = {
    'Cache-Control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text



def serialRead():
    url = "http://beta.boltiot.com/remote/d219c589-ec8b-4947-a622-d1e3095ef4f4/serialRead"
    querystring = {"till":"10","deviceName":"BOLT366397"}
    headers = {
    'Cache-Control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text

init()
