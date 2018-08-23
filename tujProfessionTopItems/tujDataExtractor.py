from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

def fetch_data(uri):
    option = webdriver.ChromeOptions()
    option.add_argument("--headless")
    driver = webdriver.Chrome(executable_path=r"chromedriver.exe", chrome_options=option)
    driver.get(uri)
    response = driver.page_source
    driver.close()
    return response



def tuj_front_page():
    uri = 'https://theunderminejournal.com/#us/khazgoroth'
    page_content = fetch_data(uri)
    parser = BeautifulSoup(page_content, "html.parser")
    front_page_most_available = parser.find(id = "front-page-most-available")
    for link_item in front_page_most_available.find_all('a'):
        print(link_item.text.strip())    


def main():
    #responseData = fetch_data("https://www.pythonforbeginners.com/python-on-the-web/web-scraping-with-beautifulsoup")
    #print(responseData)
    tuj_front_page()

if __name__ == '__main__':
    main()