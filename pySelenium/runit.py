#!/usr/bin/python3
# -*- coding: utf8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import pygal

__author__ = "Laird Streak"

def chartDrenorFlying():
    url = "http://www.wowhead.com/flying#us-khazgoroth-gnomeifix"

    driver = webdriver.PhantomJS(executable_path="./driver/phantomjs")
    driver.get(url)
    content_element = driver.find_element_by_id("flying-draenor")
    content_html = content_element.get_attribute("innerHTML")

    soup = BeautifulSoup(content_html, "html.parser")
    trColl = soup.find_all("tr")
    bar_chart = pygal.Pie()
    for trow in trColl:
        tdcells = trow.find_all("td")
        lengthArray = len(tdcells)
        if lengthArray > 0:
            header = tdcells[0].find_all(text=True)
            percentage = tdcells[1].find_all(text=True)
            percentageDisplay = percentage[0]

            if(percentageDisplay == 'Complete'):
                percentageDisplay = 100

            if(percentageDisplay == 'Incomplete'):
                percentageDisplay = 0

            percentageDisplay = str(percentageDisplay).replace("%","")
            bar_chart.add(header[0], [float(percentageDisplay)])

    bar_chart.render_in_browser()
    driver.close()


if __name__ == '__main__':
    chartDrenorFlying()