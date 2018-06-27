import mysql.connector
import pandas

def fetch_latestdata():
    cnx = mysql.connector.connect(user='wimosdata', password='wimosdata', host='127.0.0.1',
                                  database='wimosdata')
    cursor = cnx.cursor()

    query = ("SELECT Temperature, Humidity FROM dht11data ORDER BY Inserted DESC Limit 1;")

    cursor.execute(query)

    for (Temperature, Humidity) in cursor:
        d = {"Temperature":Temperature, "Humidity":Humidity}

    cursor.close()
    cnx.close()
    return d


def fetch_temperature_for_last_day():
    cnx = mysql.connector.connect(user='wimosdata', password='wimosdata', host='127.0.0.1',
                                  database='wimosdata')
    cursor = cnx.cursor()

    query = ("SELECT Temperature, Inserted FROM dht11data;") # WHERE Inserted = curdate();")
    cursor.execute(query)
    names = [x[0] for x in cursor.description]
    rows = cursor.fetchall()
    cursor.close()
    cnx.close()
    return pandas.DataFrame(rows, columns=names)


def fetch_humidity_for_last_day():
    cnx = mysql.connector.connect(user='wimosdata', password='wimosdata', host='127.0.0.1',
                                  database='wimosdata')
    cursor = cnx.cursor()

    query = ("SELECT Humidity, Inserted FROM dht11data WHERE Inserted = curdate();")
    cursor.execute(query)
    names = [x[0] for x in cursor.description]
    rows = cursor.fetchall()
    cursor.close()
    cnx.close()
    return pandas.DataFrame(rows, columns=names)

def put_latestdata(temerature,humidity):
    cnx = mysql.connector.connect(user='wimosdata', password='wimosdata', host='127.0.0.1',
                                  database='wimosdata')
    cursor = cnx.cursor()

    try:
        cmd = "Insert into dht11data(Temperature,Humidity,Inserted) Values ({},{},NOW());".format(temerature, humidity)
        cursor.execute(cmd)
        cnx.commit()
    except:
        cnx.rollback()