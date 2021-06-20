#Code for WebScrapping 
#Author: Rushil Verma
#Description : For Nemish Technology Task

import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import webbrowser
import time


url = "https://www.propertiesguru.com/residential-search/2bhk-residential_apartment_flat-for-sale-in-new_delhi"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"}

#to click on 2bhk and 3bhk buttons
driver = webdriver.Chrome('D:\Project\PythonWebScraping\chromedriver_win32\chromedriver.exe')
driver.get(url)
time.sleep(1)
bhk_button = driver.find_element_by_xpath('/html/body/nav[1]/div/ul[1]/li[3]').click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/nav[1]/div/ul[1]/li[3]/ul/li/div/ul/li[3]/label/span").click();
time.sleep(1)
driver.find_element_by_xpath("/html/body/nav[1]/div/ul[1]/li[3]/ul/li/div/ul/li[4]/label/span").click();
time.sleep(1)

html_src = driver.page_source

driver.quit()

#soup = BeautifulSoup(req.content, "lxml")
soup = BeautifulSoup(html_src, "lxml")

#print(soup.get_text()) #to get only text
#print(soup.prettify()) #to get html src in nicely formated form

info = soup.find('div',{'class': 'searchlistitems'})
totalEntries = info.find('input')['value']


j=-1

colms = ['BHK','Location','Prices (in Rupees)','Rates(per Square feet)','Area','Facing','Status','Floor no.','Furnish type','Freehold','No. of bathrooms','Posted by','Posted Time']
raw_data = [[] for x in range (len(colms))]
n=0
for i in info.stripped_strings:
    print(i+str(j)) #for each line corelation with j
    if(i=='Featured'):
        continue
    if(j==0):
        raw_data[0].append(i[0:1])#bhk
    elif(j==1):
        raw_data[1].append(i)#location
    elif(j==4):
        raw_data[2].append(i)#prices
    elif(j==5):
        raw_data[3].append(i.replace("@",""))#rates
    elif(j==7):
        raw_data[4].append(i)#area
    elif(j==10):
        raw_data[5].append(i)#facing
    elif(j==12):
        raw_data[6].append(i)#status
    elif(j==13):
        raw_data[7].append(i)#floor
    elif(j==14):
        raw_data[8].append(i)#furnish type
    elif(j==15):
        raw_data[9].append(i)#freehold
    elif(j==16):
        raw_data[10].append(i[0:1])#bathroom
    elif(j==17):
        raw_data[11].append(i)#posted by
    elif(j==18):
        raw_data[12].append(i.replace('Posted:',' '))    #post date
    elif(j==20):
        j=0
        raw_data[0].append(i[0:1])#bhk

        '''
        n=n+1         #for step by step debugging
        if(n==5):break
        '''

    j=j+1 #updating of arrayindex iterator
print(raw_data[0])

df = pd.DataFrame({colms[i]:raw_data[i] for i in range(len(colms))})
print(df)

#excel file name
file_name = 'Data_all_bhk.xlsx'

df.to_excel(file_name,sheet_name='Sheet1',index=False)

print('Process Successful!!')
