from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import re

# Wait for the page to load 
# https://stackoverflow.com/a/25651197/2042701
def wait_for(condition_function):
    timeout = 30 # seconds
    start_time = time.time()
    while time.time() < start_time + timeout:
        if condition_function():
            return True
        else:
            time.sleep(0.1)
    raise Exception('Timeout waiting for {}'.format(condition_function.__name__))

def page_has_loaded(driver):
    # old_page = driver.find_element_by_tag_name('html')
    new_page = driver.find_element_by_tag_name('html')
    return new_page.id != old_page.id

# Chrome 
executable_path = 'D:/Pranjal Tutorial Videos/GitHub/AI-Poet/selenium_drivers/chromedriver.exe'
driver = webdriver.Chrome(executable_path)

driver.get("https://www.poetryfoundation.org/poems/browse#page=22&sort_by=recently_added&preview=1")
# Wait for the page to load  
# https://stackoverflow.com/a/42975937/2042701
driver.implicitly_wait(60)

links = driver.find_elements(By.TAG_NAME, 'a') # By.LINK_TEXT for find by link text
# Get the link text 
# for link in links:
#     print(link.text)
# Get the link href 
# https://stackoverflow.com/a/12459228/2042701
# for link in links:
#     print(link.get_attribute("href"))

# Get the links of the poems 
regex = r'.*/poems/[0-9]+/.*'
for link in links:
    match = re.search(regex, link.get_attribute('href'))
    if match != None:
        print(link.text)  

# driver.quit()
