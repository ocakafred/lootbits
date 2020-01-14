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


#
# -------------------------------
# Please enter your   credentails here
# -----------------------------
# 
lootbits_username = ''
lootbits_password = ''

# Getting username and password fields
username = driver.find_element_by_name('username')
password  = driver.find_element_by_name('password')
# Sending username & password values
username.send_keys(lootbits_username)
password.send_keys(lootbits_password)

# Login
submit_button=driver.find_element_by_name('action')
submit_button.click()

#  Get dashboard  link
driver.get("https://lootbits.io/dashboard.php")

#check if user still have more GEMS
# and loop through all the GEMS
while True:

    # check id the button is diabled
    try:
        bonus =  driver.find_element_by_id('claimbtn')
        bonus.click()
        driver.get("https://lootbits.io/dashboard.php")
    except NoSuchElementException:
        driver.get("https://lootbits.io/dashboard.php")

    # obtain tne remaining GEMs number
    lootbits = driver.find_element_by_id('lootbits')
    lootbits_number  = int(lootbits.text)

    broken = False
    print(broken)
    while  lootbits_number >= 1:
        # Click the box
        box = driver.find_element_by_class_name('lootbox')
        box.click()
        driver.get("https://lootbits.io/dashboard.php")
        time.sleep(5)
        
        if lootbits_number == 0:
            # break
            # broken = True
        else:
            break

    print("Endings")
    time.sleep(10)
        





