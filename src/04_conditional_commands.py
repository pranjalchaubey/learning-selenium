from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Chrome 
driver = webdriver.Chrome(executable_path='D:/Pranjal Tutorial Videos/GitHub/AI-Poet/selenium_drivers/chromedriver.exe')

driver.get("http://newtours.demoaut.com/")
element = driver.find_element_by_name('userName')
print(element.is_displayed()) # T/F based on element's state 
# print(element.is_enabled)
element.send_keys("mercury")

password = driver.find_element_by_name('password')
print(password.is_displayed()) # T/F based on element's state 
# print(password.is_enabled)
password.send_keys('mercury')

driver.find_element_by_name('login').click()

roundtrip_radio = driver.find_element_by_css_selector("input[value=roundtrip]")
print('roundtrip_radio.is_selected() ', roundtrip_radio.is_selected())