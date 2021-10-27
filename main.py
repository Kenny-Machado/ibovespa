# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 14:22:42 2021

@author: kenny
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

while True:
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    
    # Starting Google Chrome Session
    driver = webdriver.Chrome(chrome_options=chrome_options)#'/home/ubuntu/ibovespa/chromedriver.exe')
    
    # Go to Google Search
    driver.get('https://www.google.com')
    
    # Type in search bar
    text = 'IBOVESPA'
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(text + Keys.ENTER)
    
    # Get updated price
    price = driver. find_element_by_css_selector("span[class='IsqQVc NprOob XcVN5d wT3VGc']").text
    print('The price updated is R$ ',price)
    time.sleep(5)
    
    # Close the Browser
    driver.close()
