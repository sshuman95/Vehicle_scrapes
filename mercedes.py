from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome("/Users/Buster/chromedriver")
urls=[]
final = []
for i in range(1,7):
    browser.get("https://www.mercedesalexandria.com/new-vehicles/#action=im_ajax_call&perform=get_results&page="+str(i))
    time.sleep(10)
    soup = BeautifulSoup(browser.page_source,"html.parser")
    vehicle_overviews = soup.select('.vehicle-overview')
    models = []
    vins = []
    stock_nums = []
    engine = []
    trans = []
    drive_train = []
    exterior = []
    interior = []
    hwy = []
    city = []
    raw_details = []
    price = []
    misc_details = []
    for v in vehicle_overviews:
        options = v.ul
        if(len(options) < 12):
            continue
        detail_labels = []
        detail_content = []
        models.append(v.h2.a.get_text())
        vehicle = v.select('.vinstock')
        stock_nums.append(vehicle[0].select('.stock-label')[0].get_text())
        vins.append(vehicle[0].span.get_text())
        raw_details.append(options)
        price.append(v.select('.price')[0].get_text().strip())
        misc_details.append(v.select('.vehicle-description-text')[0].get_text().strip())

    df = pd.DataFrame([])
    df['Models'] = models
    df['Vin Number'] = vins
    df['Stock Number'] = stock_nums

    # Add columns here
    clean_details = []
    for r in raw_details:
        clean_details.append(r.select('.detail-content'))

    for d in clean_details:
        engine.append(d[0].get_text())
        trans.append(d[1].get_text())
        drive_train.append(d[2].get_text())
        exterior.append(d[3].get_text())
        interior.append(d[4].get_text())
        hwy.append(d[5].get_text())
        city.append(d[6].get_text())


    df['Engine'] = engine
    df['Transmisison'] = trans
    df['Drive Train'] = drive_train
    df['Exterior'] = exterior
    df['Interior'] = interior
    df['Highway Miles'] = hwy
    df['City Miles'] = city
    df['Price'] = price
    df['Other Details'] = misc_details
  
    final.append(df)

browser.close()
bigdata = pd.concat(final)
bigdata.to_csv('full_inventory_test.csv', sep='\t')
print('Done')