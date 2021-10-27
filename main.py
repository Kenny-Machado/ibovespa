# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 14:22:42 2021

@author: kenny
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

while True:
    
    # Starting Google Chrome Session
    driver = webdriver.Chrome('C:\\Users\\kenny\\Desktop\\ChromeDriver New\\chromedriver.exe')
    
    # Go to Google Search
    driver.get('https://www.google.com')
    
    # Type in search bar
    text = 'IBOVESPA'
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(text + Keys.ENTER)
    
    # Get updated price
    price = driver. find_element_by_css_selector("span[class='IsqQVc NprOob XcVN5d wT3VGc']").text
    print('The price updated is R$ ',price)
    time.sleep(15)
    
    # Close the Browser
    driver.close()
