from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

# Chrome 
driver = webdriver.Chrome(executable_path='D:/Pranjal Tutorial Videos/GitHub/AI-Poet/selenium_drivers/chromedriver.exe')

driver.get("http://newtours.demoaut.com/")
print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.close()