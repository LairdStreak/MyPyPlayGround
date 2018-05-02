#!/usr/bin/python3
# -*- coding: utf8 -*-
from selenium import webdriver
import __future__
import os
from bs4 import BeautifulSoup

__author__ = "Laird Streak"

def fetch_tuj_data():
    fetch_tuj_category("inscription")

def fetch_tuj_category(category):
    url = "https://theunderminejournal.com/#us/khazgoroth/category/" + category
    driver = webdriver.PhantomJS(executable_path="./driver/phantomjs")
    driver.get(url)
    content_data = driver.page_source
    soup = BeautifulSoup(content_data, "html.parser")
    categorydivs = soup.find_all("div", class_="category category-itemlist")
    allItems = []
    for divitem in categorydivs:
        tableRows = divitem.find_all("tr")
        for row in tableRows:
            tdcells = row.find_all("td")
            lengthArray = len(tdcells)
            if lengthArray > 0:
                strName = tdcells[1].text
                strName = strName.replace("[","")
                strName = strName.replace("]","")
                current = tdcells[3].text
                mean = current if tdcells[4].text == "" else tdcells[4].text
                diff = 1
                if current is not None:
                    if mean is not None:
                        diff = float(current) - float(mean)
                if diff > 0:
                    info = {"name" : strName, "available" : tdcells[2].text, "current" : tdcells[3].text, "mean" : tdcells[4].text,"lastseen" : tdcells[5].text,"move" : "UP","diff" : diff}
                    allItems.append(info)
                elif diff == 0:
                    info = {"name" : strName, "available" : tdcells[2].text, "current" : tdcells[3].text, "mean" : tdcells[4].text,"lastseen" : tdcells[5].text,"move" : "Unknown","diff" : diff}
                    allItems.append(info)
                else:
                    info = {"name" : strName, "available" : tdcells[2].text, "current" : tdcells[3].text, "mean" : tdcells[4].text,"lastseen" : tdcells[5].text,"move" : "DOWN","diff" : diff}
                    allItems.append(info)
    try:
      os.remove("Output.csv")
    except OSError:
      pass

    for infoItem in allItems:
        if "Glyph" in infoItem["name"]:
          line = "{},{},{}".format(infoItem["name"], str(infoItem["diff"]), str(infoItem["mean"]))
          with open("Output.csv", "a") as text_file:
            text_file.write("{}\n".format(line))

    print('Done')

if __name__ == '__main__':
    fetch_tuj_data()