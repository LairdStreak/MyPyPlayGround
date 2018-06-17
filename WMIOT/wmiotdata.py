import mysql.connector

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
    cnx.close()
    return d


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