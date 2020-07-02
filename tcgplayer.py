from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome("/Users/Buster/chromedriver")
big_data = pd.DataFrame()
#urls=["https://www.alfaromeousa.com/car-shopping/current-offers",'https://www.alfaromeousa.com/car-shopping/current-offers#2019-giulia',"https://www.alfaromeousa.com/car-shopping/current-offers#2020-stelvio","https://www.alfaromeousa.com/car-shopping/current-offers#2019-stelvio"]
pages = []
seller1 = []

browser.get("https://shop.tcgplayer.com/yugioh/2010-collectors-tins/the-wicked-dreadroot")

test = browser.find_elements_by_tag_name('option')
for t in test:
    if(t.text != '50'):
        continue
    else:
        t.click()
        break
time.sleep(3)
elm = browser.find_elements_by_class_name('seller__name')
for e in elm:
    seller1.append(e.text)


browser.close()



time.sleep(1)
browser = webdriver.Chrome("/Users/Buster/chromedriver")
#urls=["https://www.alfaromeousa.com/car-shopping/current-offers",'https://www.alfaromeousa.com/car-shopping/current-offers#2019-giulia',"https://www.alfaromeousa.com/car-shopping/current-offers#2020-stelvio","https://www.alfaromeousa.com/car-shopping/current-offers#2019-stelvio"]
pages = []
seller2 = []

browser.get("https://shop.tcgplayer.com/yugioh/2010-collectors-tins/the-wicked-avatar")

test = browser.find_elements_by_tag_name('option')
for t in test:
    if(t.text != '50'):
        continue
    else:
        t.click()
        break
time.sleep(3)
elm = browser.find_elements_by_class_name('seller__name')
for e in elm:
    seller2.append(e.text)


browser.close()

time.sleep(1)
browser = webdriver.Chrome("/Users/Buster/chromedriver")
#urls=["https://www.alfaromeousa.com/car-shopping/current-offers",'https://www.alfaromeousa.com/car-shopping/current-offers#2019-giulia',"https://www.alfaromeousa.com/car-shopping/current-offers#2020-stelvio","https://www.alfaromeousa.com/car-shopping/current-offers#2019-stelvio"]
pages = []
seller3 = []

browser.get("https://shop.tcgplayer.com/yugioh/2010-collectors-tins/the-wicked-eraser")

test = browser.find_elements_by_tag_name('option')
for t in test:
    if(t.text != '50'):
        continue
    else:
        t.click()
        break
time.sleep(3)
elm = browser.find_elements_by_class_name('seller__name')
for e in elm:
    seller3.append(e.text)


browser.close()

elems_in_both_lists = set(seller1) & set(seller2) & set(seller3)

print(elems_in_both_lists)
"""
time.sleep(4)
elm = browser.find_elements_by_class_name('seller__name')
for e in elm:
    final.append(e)
    """