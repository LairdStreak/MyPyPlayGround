import csv
import requests

CSV_URL = 'http://www.wowuction.com/us/khazgoroth/alliance/Tools/RealmDataExportGetFileStatic?type=csv&token=wVQ31OiPJkUSpa1tbirwyA2'


with requests.Session() as s:
    download = s.get(CSV_URL)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    for row in my_list:
        print(row)    