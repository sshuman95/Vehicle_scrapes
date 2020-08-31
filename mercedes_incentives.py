import urllib.request, json 
import time
import pandas as pd
import requests


urls=[]
final = []
r = requests.get('https://www.mbusa.com/en/special-offers-regional/jcr:content.filter-offer-json.html')
text = r.json()
with open('data.json', 'w') as f:
    json.dump(text, f)



