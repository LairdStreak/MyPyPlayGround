import csv
import requests
import pygal
from pygal.style import DarkSolarizedStyle
from aucitem import AucItem


__author__ = "Laird Streak"

CSV_URL = 'http://www.wowuction.com/us/khazgoroth/alliance/Tools/RealmDataExportGetFileStatic?type=csv&token=wVQ31OiPJkUSpa1tbirwyA2'
itemIDS = [765,8846,124106,129289,124105,129288]

#ite = AucItem(22,'yo')
#print(ite.itemID)
aucitems = []

with requests.Session() as s:
    download = s.get(CSV_URL)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    for row in my_list:
        if row[0] != 'Realm Name':
            ite = AucItem(int(row[4]),row[5],float(row[14]),float(row[8]))
            aucitems.append(ite)
#             print(row)
    #my_filter = lambda x: x.itemId in itemIDS
    #myItems = my_filter(aucitems)#filter(lambda x: x.itemID in itemIDS, aucitems)
   
    myItems = [
        item for item in aucitems
        if item.itemID in itemIDS
    ]
    
    line_chart = pygal.HorizontalBar(style=DarkSolarizedStyle,height=200)
    line_chart.title = 'Herb Movement'
    for item in myItems:
        lable = item.itemName + '' + str(item.Price)
        line_chart.add(item.itemName,[{'value' : item.changeNum, 'label' : lable}])
        #print(item.itemName)   

    line_chart.render_in_browser()    