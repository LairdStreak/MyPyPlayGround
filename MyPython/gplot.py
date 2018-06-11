import gmplot
import os

gmap = gmplot.GoogleMapPlotter(-43.5429669, 172.6159263, 16)
gmap.marker(-43.541365, 172.610540, "#FFFF00" ,title="Here")
gmap.draw("mymap.html")