#!/usr/bin/python3
# -*- coding: utf8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import pygal

__author__ = "Laird Streak"

def fetch_tuj_data():
    #fetch_tuj_category("alchemy")
    fetch_tuj_category("inscription")
    #fetch_tuj_category("herbalism") battlepets
    #print('here')
    #fetch_tuj_category("battlepets")


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
                current = tdcells[3].text
                mean = current if tdcells[4].text == "" else tdcells[4].text
                diff = 1
                if current is not None:
                    if mean is not None:
                        diff = float(current) - float(mean)
                if diff > 0:
                    info = {"name" : tdcells[1].text, "available" : tdcells[2].text, "current" : tdcells[3].text, "mean" : tdcells[4].text,"lastseen" : tdcells[5].text,"move" : "UP","diff" : diff}
                    #print(tdcells[1].text + " " + tdcells[2].text + " " + tdcells[3].text + " " + tdcells[4].text + " " + tdcells[5].text + "          UP")
                    allItems.append(info)
                elif diff == 0:
                    info = {"name" : tdcells[1].text, "available" : tdcells[2].text, "current" : tdcells[3].text, "mean" : tdcells[4].text,"lastseen" : tdcells[5].text,"move" : "Unknown","diff" : diff}
                    #print(tdcells[1].text + " " + tdcells[2].text + " " + tdcells[3].text + " " + tdcells[4].text + " " + tdcells[5].text + "          Unknown")      
                    allItems.append(info)
                else:
                    info = {"name" : tdcells[1].text, "available" : tdcells[2].text, "current" : tdcells[3].text, "mean" : tdcells[4].text,"lastseen" : tdcells[5].text,"move" : "DOWN","diff" : diff}
                    #print(tdcells[1].text + " " + tdcells[2].text + " " + tdcells[3].text + " " + tdcells[4].text + " " + tdcells[5].text + "          DOWN")    
                    allItems.append(info)
            #else:
            #    thcells = row.find_all("th")
            #    lenheaders = len(thcells)
            #    if lenheaders == 1:
            #       theader = row.find("th", class_="title")
            #       if theader is not None:
                      #print(theader.contents[0])
            #    else:
                    #print(thcells[0].text + " " + thcells[1].text + " " + thcells[2].text + " " + thcells[3].text + " " + thcells[4].text)            


    bar_chart = pygal.HorizontalBar()
    bar_chart.title = 'Profitability'
    for infoItem in allItems:
        #print(infoItem["name"] + " " + str(infoItem["diff"]))
        bar_chart.add(infoItem["name"],  infoItem["diff"])

    # bar_chart.render_in_browser()
    bar_chart.render_to_file('bar_chart.svg')  
    #print(allItems)
    #df = pd.DataFrame.from_records(allItems)
    #df.plot()

if __name__ == '__main__':
    fetch_tuj_data()