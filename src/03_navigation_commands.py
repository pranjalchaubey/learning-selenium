from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Chrome 
driver = webdriver.Chrome(executable_path='D:/Pranjal Tutorial Videos/GitHub/AI-Poet/selenium_drivers/chromedriver.exe')

driver.get("http://newtours.demoaut.com/")
print(driver.title)
driver.get("http://pavantestingtools.blogspot.in/")
print(driver.title)
time.sleep(5)

# Navigation 
driver.back()
print(driver.title)
time.sleep(5)
driver.forward()
print(driver.title)
time.sleep(5)

driver.quit()

