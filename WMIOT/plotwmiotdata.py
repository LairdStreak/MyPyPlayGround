import pandas as PD
import matplotlib.pyplot as plt
from io import StringIO


def plot_dataframe(DataFrame):
    plot = DataFrame.plt()
    img = StringIO()
    plot.savefig(img)
    img.seek(0)
    return img