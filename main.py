#Code for WebScrapping 
#Author: Rushil Verma
#Description : For Nemish Technology Task

from typing import Text
import requests
from bs4 import BeautifulSoup

url = "https://www.propertiesguru.com/residential-search/2bhk-residential_apartment_flat-for-sale-in-new_delhi"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"}

req = requests.get(url, headers= headers)

#req.status_code #200 is good

soup = BeautifulSoup(req.content, "lxml")

#print(soup.get_text()) #to get only text
#print(soup.prettify()) #to get html src in nicely formated form

info = soup.find('div',{'class': 'searchlistitems'})

total_entries = info.input['value']

#print(info.get_text())

#detail = info.find_all('a',{'class': 'fullscreen'})

prices = info.('span',{'class': 'price'})
print(prices)

'''
location = []
i=0
for elem in detail:
    location[i] = 
    i=i+1
'''
#print(detail)