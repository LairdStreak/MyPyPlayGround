#!/usr/bin/python3
# -*- coding: utf8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import pygal

__author__ = "Laird Streak"

def fetch_tuj_data():
    fetch_tuj_alchemy()


def fetch_tuj_alchemy():
    url = ("https://theunderminejournal.com/#us/khazgoroth/category"
          "/alchemy")
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
                print("td")
            else:
                thcells = row.find_all("th")
                lenheaders = len(thcells)
                if lenheaders == 1:
                   theader = row.find("th", class_="title")
                   if theader is not None:
                      print(theader.contents[0])
                else:
                    print(thcells[0].text + " " + thcells[1].text)            
        #print(divitem)

if __name__ == '__main__':
    fetch_tuj_data()