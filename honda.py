from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome("/Users/Buster/chromedriver")
#urls=["https://www.alfaromeousa.com/car-shopping/current-offers",'https://www.alfaromeousa.com/car-shopping/current-offers#2019-giulia',"https://www.alfaromeousa.com/car-shopping/current-offers#2020-stelvio","https://www.alfaromeousa.com/car-shopping/current-offers#2019-stelvio"]
final = []


browser.get("https://automobiles.honda.com/tools/current-offers?zipcode=95407")
browser.fullscreen_window()
time.sleep(1)

offers_container = browser.find_element_by_xpath("//*[@offer-type='lease']")
offer_cards = offers_container.find_elements_by_class_name('offer-card-content')
models = []
terms = []
prices = []
disclaimers = []
expirations = []
for offer in offer_cards:
    model = offer.find_element_by_class_name('offer-card-title').get_attribute("textContent")
    term = offer.find_element_by_class_name('offer-card-term').get_attribute("textContent")
    raw_price = offer.find_element_by_class_name('offer-card-payment').get_attribute("textContent")
    price = " ".join(raw_price.split())
    disclaimer = offer.find_element_by_class_name('offer-card-legal').get_attribute("textContent")
    disclaimers.append(" ".join(disclaimer.split()))
    models.append(model)
    terms.append(term)
    prices.append(price)
raw_exps = offers_container.find_elements_by_tag_name('platform-offer-card')
for exp in raw_exps:
    expirations.append(exp.get_attribute('expiration'))
    
browser.close()
honda = pd.DataFrame()
honda["Models"] = models
honda["Price"] = prices
honda["Terms"] = terms
honda["Expiration"] = expirations
honda["Disclaimers"] = disclaimers
honda.to_csv('honda_scrape.csv', sep='\t')
print('Done')

