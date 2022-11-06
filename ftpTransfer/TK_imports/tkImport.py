# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 22:54:16 2022

@author: Mark Patmore FMDJP
"""

#automates report imports from TK tracking and carrier e solutions.



import pyautogui as gui
import time
import cv2
import os




# from selenium import webdriver
# from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service


# profile = FirefoxProfile(r'C:\Users\breakdown\AppData\Roaming\Mozilla\Firefox\Profiles\todaga6b.default')
# driver = webdriver.Firefox(profile)

profile_path = r'C:\Users\breakdown\AppData\Roaming\Mozilla\Firefox\Profiles\todaga6b.default'

options = Options()

options.set_preference('profile', profile_path)

service = Service('TK_imports/geckodriver.exe')

driver = Firefox(service=service, options=options)








def TK_login():

    

    original_window = driver.current_window_handle


    driver.maximize_window()
    time.sleep(2)
    driver.get('https://www.tracking.thermoking.com/Combo/v2/logon')

    time.sleep(5)


    cookie = driver.find_element(By.ID, 'acceptCookie')
    cookie.click()

    time.sleep(.5)

    username = driver.find_element(By.ID, 'username')
    username.send_keys('maintenance@questglobal.net')

    time.sleep(.1)

    password = driver.find_element(By.ID, 'password')
    password.send_keys('Questbreakdown123')  ###################change when password changes


    login = driver.find_element(By.ID, 'logonButton')
    login.click()


    time.sleep(10)
    reports = driver.find_element(By.ID, 'main-menu-data-analysis')
    reports.click()

    time.sleep(10)

    report_type = driver.find_element(By.CSS_SELECTOR, '#reportId_chosen')
    report_type.click()
    
    
    report_input = driver.find_element(By.CSS_SELECTOR, '#reportId_chosen > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)')
    
    report_input.send_keys('Engine Hours')
    report_input.send_keys(Keys.ENTER)


    generate_report = driver.find_element(By.ID, 'generate_report_button')
    generate_report.click()
    
    
    time.sleep(10)
    
    
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    
    
    
    
    
    download_report = driver.find_element(By.CSS_SELECTOR, 'a.export-button:nth-child(2)')
    download_report.click()

            

    


    





# TK_login()

# time.sleep(5)

# driver.quit()


 

