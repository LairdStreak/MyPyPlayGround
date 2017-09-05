"""
Assuming this is file mymodule.py, then this string, being the
first statement in the file, will become the "mymodule" module's
docstring when the file is imported.
"""
import csv
import requests
import pygal
from pygal.style import DarkSolarizedStyle
from aucitem import AucItem

__author__ = "Laird Streak"

CSV_URL = ('http://www.wowuction.com/us/khazgoroth/alliance/Tools/'
           'RealmDataExportGetFileStatic?type=csv&token=wVQ31OiPJkUSpa1tbirwyA2')
ITEM_IDENTIFIERS = [765, 8846, 124106, 129289, 124105, 129288]

AUC_ITEMS = []

with requests.Session() as s:
    download = s.get(CSV_URL)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    for row in my_list:
        if row[0] != 'Realm Name':
            ite = AucItem(int(row[4]), row[5], float(row[14]), float(row[8]))
            AUC_ITEMS.append(ite)

    myItems = [
        item for item in AUC_ITEMS
        if item.itemID in ITEM_IDENTIFIERS
    ]

    LINE_CHART = pygal.HorizontalBar(style=DarkSolarizedStyle, height=200)
    LINE_CHART.title = 'Herb Movement'
    for item in myItems:
        lable = item.itemname + '' + str(item.price)
        LINE_CHART.add(item.itemName, [
            {'value': item.changenum, 'label': lable}])
        # print(item.itemName)

    LINE_CHART.render_in_browser()
