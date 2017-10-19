#!/usr/bin/python3
# -*- coding: utf8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup

__author__ = "Laird Streak"

def fetch_tuj_data():
    fetch_tuj_category("alchemy")
    fetch_tuj_category("inscription")


def fetch_tuj_category(category):
    url = "https://theunderminejournal.com/#us/khazgoroth/category/" + category
    driver = webdriver.PhantomJS(executable_path="./driver/phantomjs")
    driver.get(url)
    content_data = driver.page_source
    soup = BeautifulSoup(content_data, "html.parser")
    categorydivs = soup.find_all("div", class_="category category-itemlist")
    for divitem in categorydivs:
        tableItem = divitem.find_all("table", class_="category category-items")
        tableRows = divitem.find_all("tr")
        for row in tableRows:
            tdcells = row.find_all("td")
            lengthArray = len(tdcells)
            if lengthArray > 0:
                print(tdcells[1].text + " " + tdcells[2].text + " " + tdcells[3].text + " " + tdcells[4].text + " " + tdcells[5].text)
            else:
                thcells = row.find_all("th")
                lenheaders = len(thcells)
                if lenheaders == 1:
                   theader = row.find("th", class_="title")
                   if theader is not None:
                      print(theader.contents[0])
                else:
                    print(thcells[0].text + " " + thcells[1].text + " " + thcells[2].text + " " + thcells[3].text + " " + thcells[4].text)            


if __name__ == '__main__':
    fetch_tuj_data()