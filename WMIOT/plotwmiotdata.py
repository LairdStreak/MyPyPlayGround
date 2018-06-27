import pandas as PD
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from io import BytesIO
import time
from PIL import Image

def plot_dataframe(DataFrame):
    DataFrame.set_index('Inserted', inplace=True)

    fig, ax = plt.subplots(figsize=(15, 7))
    DataFrame.plot(ax=ax)

    # set ticks every week
    ax.xaxis.set_major_locator(mdates.WeekdayLocator())
    # set major ticks format
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

    buf = BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    im = Image.open(buf)
    #im.show()
    #plt.show()
    #time.sleep(10)
    return im

