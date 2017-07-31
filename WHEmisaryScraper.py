import requests
from bs4 import BeautifulSoup

page = requests.get("http://www.wowhead.com/")
soup = BeautifulSoup(page.content, 'html.parser')

print('Emissary Missions')
missionTable = soup.find("table", {"class": "tiw-group tiw-group-type-misc tiw-group-emissary"})
for trow in missionTable.find_all('tr', class_=lambda t: t != 'tiw-heading'):
    col = trow.find_all('td')
    tdVAl = col[0].string.strip()
    tdVAl2 = col[1].find_all('a')[0].contents[0]
    print("Time Remaining {0} Faction {1}".format(tdVAl, tdVAl2))

print('Blues Latest posts')
newsDiv = soup.find("div", {"class": "news-recent-blue-posts"})
tables = newsDiv.find_all('table')
tableBluesMain = tables[0]
for trRow in  tableBluesMain.find_all('tr'):
    cols = trRow.find_all('td')
    tdValue1 = cols[0].string
    tdValue2 = cols[1].text.strip()
    print("Last Updated {0} : Heading {1}".format(tdValue1, tdValue2))

profileGnomeifixPage = requests.get("http://www.wowhead.com/list=1036141/us-khazgoroth-gnomeifix")
profileGnomeifixPageSoup = BeautifulSoup(page.content, 'html.parser')

#page = requests.get("http://www.wowhead.com/")
#soup = BeautifulSoup(page.content, 'html.parser')
