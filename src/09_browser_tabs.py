from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import re 

# FireFox
executable_path = r'D:\Pranjal Tutorial Videos\GitHub\AI-Poet\selenium_drivers\geckodriver.exe'
driver = webdriver.Firefox(executable_path=executable_path)

driver.get("http://demo.automationtesting.in/Windows.html")
driver.find_element(By.XPATH, '//*[@id="Tabbed"]/a/button').click()

print(driver.current_window_handle)
print(driver.window_handles)
handles = driver.window_handles # returns all the handle values of browser tabs

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)

driver.get("https://www.poetryfoundation.org/poems/browse#page=22&sort_by=recently_added&preview=1")
# Wait for the page to load  
# https://stackoverflow.com/a/42975937/2042701
driver.implicitly_wait(60)

links = driver.find_elements(By.TAG_NAME, 'a') # By.LINK_TEXT for find by link text
# Get the links of the poems 
regex = r'.*/poems/[0-9]+/.*'
for link in links:
    match = re.search(regex, link.get_attribute('href'))
    if match != None:
        print(link.text)  
