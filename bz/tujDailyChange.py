import mysql.connector
from mysql.connector import Error
import pandas as pd
import matplotlib.pyplot as plt
 
 
def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='newswire.theunderminejournal.com',
                                       database='newsstand',
                                       user='',
                                       password='')
        if conn.is_connected():
            print('Connected to MySQL database')
            sql = """SELECT DBItm.name_enus ,IHD.* FROM tblItemHistoryDaily IHD JOIN tblDBCItem DBItm ON IHD.item = DBItm.id JOIN tblRealm RLM ON RLM.house = IHD.house WHERE RLM.region = 'US' AND RLM.slug = 'dathremar' AND DBItm.name_enus IN ('Deep Sea Satin') order by IHD.when DESC LIMIT 10"""
            df = pd.read_sql_query(sql, conn)
            df.plot(x='when', y='pricemax', kind='barh', figsize=(20,14), title='Price Max')
            plt.show()
            #print(df.shape)
 
    except Error as e:
        print(e)
 
    finally:
        conn.close()
def main():
        connect()

if __name__ == '__main__':
    main()