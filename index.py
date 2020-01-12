import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

import pandas as pd

import time

# pull chrome driver
driver = webdriver.Chrome()
driver.get("https://lootbits.io/login.php")

# Enter user name and password
username = driver.find_element_by_name('username')
password  = driver.find_element_by_name('password')

# Credentails
username.send_keys('Ocaka')
password.send_keys('.Cashmoney11.')
# SUbmit
submit_button=driver.find_element_by_name('action')
submit_button.click()

#  Get dashboard  link
driver.get("https://lootbits.io/dashboard.php")

# check id the button is diabled
try:
    bonus =  driver.find_element_by_id('claimbtn')
    bonus.click()
except NoSuchElementException:
    pass

#check if user still have more GEMS
# and loop through all the GEMS
count = 0

lootbits = driver.find_element_by_id('lootbits')

lootbits_number  = int(lootbits.text)

while  lootbits_number > 0:
    # Click the box
    box = driver.find_element_by_class_name('lootbox')
    box.click()
    driver.get("https://lootbits.io/dashboard.php")
    time.sleep(4)




