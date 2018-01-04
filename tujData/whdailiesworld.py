#!/usr/bin/python3
# -*- coding: utf8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import pygal

__author__ = "Laird Streak"

def fetch_WH_dailies():
    url = "http://www.wowhead.com/world-quests/na"
    driver = webdriver.PhantomJS()#(executable_path="./driver/phantomjs")
    driver.get(url)
    content_data = driver.page_source
    soup = BeautifulSoup(content_data, "html.parser")
    print(soup.prettify())






if __name__ == '__main__':
    fetch_WH_dailies()