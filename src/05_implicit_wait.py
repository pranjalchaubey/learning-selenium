from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Chrome 
driver = webdriver.Chrome(executable_path='D:/Pranjal Tutorial Videos/GitHub/AI-Poet/selenium_drivers/chromedriver.exe')

driver.get("http://newtours.demoaut.com/")
driver.implicitly_wait(10) # Seconds
assert "Welcome: Mercury Tours" in driver.title

driver.find_element_by_name('userName').send_keys("mercury")
driver.find_element_by_name('password').send_keys("mercury")
driver.find_element_by_name('login').click()