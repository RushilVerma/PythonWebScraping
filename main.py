#Code for WebScrapping 
#Author: Rushil Verma
#Description : For Nemish Technology Task
import pandas as pd
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
totalEntries = info.find('input')['value']


j=-3
location = []
prices = []
rates = []
area = []
colms = ['location','prices','rates','area','facing','status','floor no.','furnish type','freehold','no. of bathrooms','Posted by','Date']
raw_data = {'0': []}
for i in info.stripped_strings:
    
    if(j==0):
        raw_data[colms[0]]=i
    elif(j==2):
        raw_data[colms[1]]=i
    elif(j==3):
        raw_data[colms[2]]=i
    elif(j==5):
        raw_data[colms[3]]=i
    elif(j==8):
        raw_data[colms[4]]=i
    elif(j==10):
        raw_data[colms[5]]=i
    elif(j==11):
        raw_data[colms[6]]=i
    elif(j==12):
        raw_data[colms[7]]=i
    elif(j==13):
        raw_data[colms[8]]=i
    elif(j==14):
        raw_data[colms[9]]=i
    elif(j==15):
        raw_data[colms[10]]=i
    elif(j==16):
        raw_data[colms[11]]=i    
    elif(j==20):
        j=0

    '''
    print(i+str(j))
    j=j+1
    if(j==20):
        j=0
    '''
    df = pd.DataFrame(raw_data,columns=colms)
    file_name = 'Data2bhk.xlsx'
    df.to_excel(file_name)
    print('Process Successful!!')