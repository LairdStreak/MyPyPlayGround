"""
Assuming this is file mymodule.py, then this string, being the
first statement in the file, will become the "mymodule" module's
docstring when the file is imported.
"""
import requests
from bs4 import BeautifulSoup

def main():
    """function"""
    page = requests.get("http://www.wowhead.com/")
    soup = BeautifulSoup(page.content, 'html.parser')

    print('Emissary Missions')
    missiontable = soup.find("table", {"class": "tiw-group tiw-group-type-misc tiw-group-emissary"})
    for trow in missiontable.find_all('tr', class_=lambda t: t != 'tiw-heading'):
        col = trow.find_all('td')
        tdval = col[0].string.strip()
        tdval2 = col[1].find_all('a')[0].contents[0]
        print("Time Remaining {0} Faction {1}".format(tdval, tdval2))

    print('Blues Latest posts')
    newsdiv = soup.find("div", {"class": "news-recent-blue-posts"})
    tables = newsdiv.find_all('table')
    tablebluesmain = tables[0]
    for trrow in  tablebluesmain.find_all('tr'):
        cols = trrow.find_all('td')
        tdvalue1 = cols[0].string
        tdvalue2 = cols[1].text.strip()
        print("Last Updated {0} : Heading {1}".format(tdvalue1, tdvalue2))


if __name__ == '__main__':
    main()
