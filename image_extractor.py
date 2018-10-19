# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 17:57:18 2018

@author: udit.goswami
"""

#sys.path.append(os.path.abspath("../"))
#from google import google, images
#options = images.ImageOptions()
#options.license = 'fc'
##options.image_type = images.ImageType.CLIPART
##options.larger_than = images.LargerThan.MP_4
##options.color = "green"
##results = google.search_images("banana", options)
#results = google.search_images("engagement ring",options)

import os, os.path
import sys
sys.path.append(os.path.abspath("../"))
import requests
import selenium
from selenium import webdriver
from mimetypes import guess_extension
from urllib.request import urlretrieve
import time

filePath = r"C:\Users\udit.goswami\Documents\Received Files\Received Files\images(95).png"
save_path = r"D:\udit\workspace\NLP\Data\google_images\\"
searchUrl = 'http://www.google.com/searchbyimage/upload'
multipart = {'encoded_image': (filePath, open(filePath, 'rb')), 'image_content': ''}
response = requests.post(searchUrl, files=multipart, allow_redirects=False)
fetchUrl = response.headers['Location']
#uncommment the next line to use chrome
#options = webdriver.ChromeOptions()
options = webdriver.FirefoxOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--test-type")
#uncomment the next line to use chrome
#options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
options.binary_location = r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"
#uncomment the next line to use chrome browser
#driver = webdriver.Chrome(executable_path=r'../',chrome_options=options)
driver = webdriver.Firefox(executable_path=r'../geckodriver',firefox_options=options)
driver.get(fetchUrl)
elem = driver.find_element_by_css_selector("a.iu-card-header").click()

#for scrolling down and getting all the images
for i in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)
#This code is to click on the filter    
#elem1 = driver.find_element_by_class_name("mn-hd-txt").click()
#elem2 = driver.find_element_by_class_name("q qs").click()
imagesource = driver.current_url

images = driver.find_elements_by_css_selector('img.rg_ic.rg_i')

count = 1

for i in images:
    list1 = i.get_attribute('src')

    try:

        image_path = save_path+r"image"+str(count)+'.png'
        filename,m = urlretrieve(list1,filename=image_path)
        
#        print(filename,guess_extension(m.get_content_type()))

#        print(count)    
    except Exception as e: 
        print(e)
        continue
    count = count+1

driver.close()