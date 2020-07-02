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


browser.get("https://www.alfaromeousa.com/car-shopping/current-offers#2020-stelvio")
browser.fullscreen_window()
time.sleep(2)
zip_code = browser.find_elements_by_class_name('change-zipcode-text')
zip_code[0].click()
zip_input = browser.find_elements_by_class_name('zip-overlay-input')
zip_input[0].send_keys(77373)

button = browser.find_elements_by_class_name('gcss-button-variable')

button[13].click()
time.sleep(1)
elm = browser.find_elements_by_class_name('gcss-colors-element-disclosure-bubble')
names = []
disclaimers = []
all_spans = browser.find_elements_by_xpath("//h2[@class='vehicle-title']")
for span in all_spans:
    names.append(span.text)


for span in all_spans:
    elm[all_spans.index(span)].click()
    time.sleep(1)
    txt = browser.find_element_by_class_name("copy")
    true_disclaimer = txt.text.replace(',','')
    disclaimers.append(true_disclaimer)
    print(true_disclaimer)
    
    browser.find_element_by_id('current_offers').click()
    time.sleep(2)

browser.close()
new_stelvio = pd.DataFrame()
new_stelvio["Models"] = names
new_stelvio["Disclaimers"] = disclaimers
new_stelvio.to_csv('stelvio_incentives.csv', sep='\t')

print('Done')