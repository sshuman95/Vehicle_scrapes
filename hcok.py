from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
browser = webdriver.Chrome("/Users/Buster/chromedriver")
urls=[]
models = []
colors = []
images = []
for i in range(1,34):
    browser.get("https://www.hondacarsofkaty.com/new?page="+str(i))
    time.sleep(1)
    soup = BeautifulSoup(browser.page_source,"html.parser")
    vehicle_overviews = soup.select('.new_inv_vehicle')
    for v in vehicle_overviews:
        model = v.select('.search_headline_row')[0].text
        hm = v.select('.c_main_class')[0].select('.new_inv_cell_width_2')
        image = v.select('.inventory_thumb')[0]['src']
        if(image == '//rndinteractive.com/images/no_image.jpg'):
            colors.append(hm[0].text)
            models.append(model[:-12])
            images.append(image)
        else:
            print('hm')

df = pd.DataFrame([])
df['Models'] = models
df['Colors'] = colors
df['Images'] = images
browser.close()
df.to_csv('hcok.csv', sep='\t')
print('Done')