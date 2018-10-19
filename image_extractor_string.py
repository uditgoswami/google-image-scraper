# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 12:07:03 2018

@author: udit.goswami
"""

import os, os.path
import sys
sys.path.append(os.path.abspath("../"))
import selenium
from selenium import webdriver
#from mimetypes import guess_extension
from urllib.request import urlretrieve
import time
import pandas as pd

df = pd.read_excel(r"C:\Users\udit.goswami\Documents\Received Files\Received Files\demo_images_u\ringsclassification.xlsx")
search_list = df['search criteria'].tolist()

save_path = r"D:\udit\workspace\NLP\Data\google_images_2\\"
#options = webdriver.FirefoxOptions()
options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--test-type")
options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
#options.binary_location = r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"
fetchUrl = "https://images.google.com/"
#driver = webdriver.Firefox(executable_path=r'../geckodriver',firefox_options=options)
driver = webdriver.Chrome(executable_path=r'../chromedriver',chrome_options=options)
driver.get(fetchUrl)
inputElement = driver.find_element_by_css_selector('input#lst-ib.gsfi')
#here we need to specify our input string
for s in search_list:
    inputElement.send_keys(s)
    inputElement2 = driver.find_element_by_css_selector('button.sbico-c').click()
    search_tags_path = save_path+'\\'+s+'\\'
#     imagesource = driver.current_url
     
    for i in range(3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)
    images = driver.find_elements_by_css_selector('img.rg_ic.rg_i')       
    count = 1
    for i in images:
        list1 = i.get_attribute('src')
        
        try:
            image_path = search_tags_path+r"image"+str(count)+'.png'
            if not os.path.exists(search_tags_path):
                os.makedirs(search_tags_path)
            filename,m = urlretrieve(list1,filename=image_path)
            count = count+1
#        print(filename,guess_extension(m.get_content_type()))

#        print(count)    
        except Exception as e: 
            print(e)
            continue
            

driver.close()    
