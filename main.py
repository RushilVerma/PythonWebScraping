#Code for WebScrapping 
#Author: Rushil Verma
#Description : For Nemish Technology Task

import pandas as pd

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

colms = ['Location','Prices (in Rupees)','Rates(per Square feet)','Area(in Square Feet)','Facing','Status','Floor no.','Furnish type','Freehold','No. of bathrooms','Posted by','Posted Time']
raw_data = [[] for x in range (len(colms))]
# n=0
for i in info.stripped_strings:
#    print(i+str(j)) #for each line corelation with j
    if(j==0):
        raw_data[0].append(i)
    elif(j==2):
        raw_data[1].append(i)
    elif(j==3):
        raw_data[2].append(i.replace("@","").replace("/Sq Ft.",""))
    elif(j==5):
        raw_data[3].append(i)
    elif(j==8):
        raw_data[4].append(i)
    elif(j==10):
        raw_data[5].append(i)
    elif(j==11):
        raw_data[6].append(i)
    elif(j==12):
        raw_data[7].append(i)
    elif(j==13):
        raw_data[8].append(i)
    elif(j==14):
        raw_data[9].append(i)
    elif(j==15):
        raw_data[10].append(i)
    elif(j==16):
        raw_data[11].append(i.replace('Posted:',' '))    
    elif(j==20):
        j=0
        raw_data[0].append(i)  
#        n=n+1         #for step by step debugging
#        if(n==2):break

    j=j+1 #updating of arrayindex iterator
    

df = pd.DataFrame({colms[i]:raw_data[i] for i in range(len(colms))})
print(df)

#excel file name
file_name = 'Data2bhk.xlsx'

df.to_excel(file_name,sheet_name='Sheet1',index=False)

print('Process Successful!!')