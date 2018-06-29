import pandas as PD
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from io import BytesIO
import time
from PIL import Image
import wmiotdata
import pandas as pd
import base64

def plot_dataframe(DataFrame):
    DataFrame['Inserted'] = pd.to_datetime(DataFrame['Inserted'], format='%Y-%m-%d %H:%M:%S.%f')
    DataFrame.set_index('Inserted', inplace=True)

    fig, ax = plt.subplots(figsize=(15, 7))
    DataFrame.plot(ax=ax)

    # set ticks every week
    ax.xaxis.set_major_locator(mdates.HourLocator())
    # set major ticks format
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
    plt.savefig("E:\dev\MyPyPlayGround\WMIOT\static\chart.png")

if __name__ == '__main__':
    data = wmiotdata.fetch_temperature_for_last_day()
    plot_dataframe(data)
    print(data.head)