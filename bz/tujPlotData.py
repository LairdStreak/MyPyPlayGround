"""
Demonstration of how to return an image generated with numpy and a plot
generated with matplotlib using the Flask web server.
Requirements: numpy, flask, scikit-image, matplotlib.
"""

import io
import random
from flask import Flask, Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import mysql.connector
from mysql.connector import Error
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def generate_image():
    """
    Return a generated image as a png by
    saving it into a StringIO and using send_file.
    """
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def create_figure():
    fig = Figure()
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
            plot = df.plot(x='when', y='pricemax', kind='barh', figsize=(20,14), title='Price Max').get_figure()
            return plot
    except Error as e:
        print(e)
 
    finally:
        conn.close()

if __name__ == '__main__':
    app.run()    