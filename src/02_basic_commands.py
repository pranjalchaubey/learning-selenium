from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Chrome 
driver = webdriver.Chrome(executable_path='D:/Pranjal Tutorial Videos/GitHub/AI-Poet/selenium_drivers/chromedriver.exe')
# Firefox
# driver = webdriver.Chrome(executable_path='D:/Pranjal Tutorial Videos/GitHub/AI-Poet/selenium_drivers/geckodriver.exe')

driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)
print(driver.current_url)
driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()
time.sleep(5)

# driver.close() # closes the parent tab
driver.quit() # Closes all the browsers