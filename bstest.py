import requests
from bs4 import BeautifulSoup


page = requests.get("http://www.wowhead.com/")
soup = BeautifulSoup(page.content, 'html.parser')
missionTable = soup.find("table", {"class" : "tiw-group tiw-group-type-misc tiw-group-emissary"})  
for trow in missionTable.find_all('tr', class_=lambda t: t != 'tiw-heading'):
    col = trow.find_all('td')
    tdVAl = col[0].string.strip()
    tdVAl2 = col[1].find_all('a')[0].contents[0]
    print("Hours Remaining {0} Faction {1}".format(tdVAl, tdVAl2))
