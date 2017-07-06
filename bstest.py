import requests
from bs4 import BeautifulSoup


page = requests.get("http://www.wowhead.com/")
soup = BeautifulSoup(page.content, 'html.parser')
for a in soup.find_all('a', href=True):
   print("Found the URL:", a['href'])

missionTable = soup.find("table", {"class" : "tiw-group tiw-group-type-misc tiw-group-emissary"})   
for trow in missionTable.find_all('tr', class_=lambda t: t != 'tiw-heading'):
    col = trow.find_all('td')
    tdVAl = col[0].string.strip()
    tdVAl2 = col[1].find_all('a')[0].contents[0]
    print(tdVAl + tdVAl2)


#print(soup.prettify())