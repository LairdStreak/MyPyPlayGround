#!/usr/bin/python3
# -*- coding: utf8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup

__author__ = "Laird Streak"

def fetch_WH_dailies():
    url = "http://www.wowhead.com/world-quests/na"
    driver = webdriver.PhantomJS(executable_path="./driver/phantomjs")
    driver.get(url)
    content_data = driver.page_source #.encode("ascii")
    soup = BeautifulSoup(content_data, "html.parser")
    mission_table = soup.find_all("table", class_="listview-mode-default")
    mission_rows = mission_table[0].find_all("tr")
    for trow in mission_rows:
        print(trow) 

if __name__ == '__main__':
    fetch_WH_dailies()