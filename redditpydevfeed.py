"""
Assuming this is file mymodule.py, then this string, being the
first statement in the file, will become the "mymodule" module's
docstring when the file is imported.
"""
import requests
from bs4 import BeautifulSoup

# https://www.reddit.com/r/Python/
def main():
    """function"""
    page = requests.get("https://www.reddit.com/r/Python/")
    soup = BeautifulSoup(page.content, 'html.parser')

    recordsDiv = soup.find_all("div", {"id": "siteTable"})
    itemsDivs = recordsDiv.find_all("div", {"class" : "thing"})
    print(itemsDivs.count())

if __name__ == '__main__':
    main()    