#!/usr/bin/python3
# -*- coding: utf8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import pprint

__author__ = "Laird Streak"

questUrl = "http://www.wowhead.com/world-quests/na"

def main():
    data = fetch_wowhead_world_quests(questUrl)
    if data:
            if isValidForProcessing(data):
                read_daily_quests(data)
    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(data)

def isValidForProcessing(data):
    if "504 Gateway" in data:
        return False
    else:
        return True

def read_daily_quests(data):
    questList = []
    soup = BeautifulSoup(data, "html.parser")
    mainTable = soup.find_all("table",  class_="listview-mode-default")
    #print(maindiv.text)
    tableRows = mainTable[0].find_all("tr")
    for row in tableRows:
        tdcells = row.find_all("td")
        if len(tdcells) > 0:
            name = tdcells[0].find_all("div")[0].text
            reward = tdcells[1].find_all("div")[0].text
            faction = tdcells[2].find_all("div")[0].text
            remain = tdcells[3].find_all("div")[0].text
            print("{0} {1} {2} {3}".format(name, reward, faction, remain))


def fetch_wowhead_world_quests(uri):
    driver = webdriver.Chrome()
    driver.get(uri)
    content_data = driver.page_source
    return content_data


if __name__ == '__main__':
    main()