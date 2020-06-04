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
        if condition_function:
            return True
        else:
            time.sleep(0.1)
    raise Exception('Timeout waiting for {}'.format(condition_function.__name__))

def page_has_loaded(old_page, new_page):
    # old_page = driver.find_element_by_tag_name('html')
    # new_page = driver.find_element_by_tag_name('html')
    return new_page.id != old_page.id

# Chrome 
executable_path = 'D:/Pranjal Tutorial Videos/GitHub/AI-Poet/selenium_drivers/chromedriver.exe'
driver = webdriver.Chrome(executable_path)

# driver.get("http://demo.automationtesting.in/Windows.html")
# driver.find_element(By.XPATH, '//*[@id="Tabbed"]/a/button').click()
driver.implicitly_wait(15)
driver.get("https://www.poetryfoundation.org/poems/browse#page=22&sort_by=recently_added&preview=1")
print(driver.find_element_by_tag_name('html').id)
driver.refresh()
driver.implicitly_wait(15)
print(driver.find_element_by_tag_name('html').id)

driver.get("http://demo.automationtesting.in/Windows.html")
old_page = driver.find_element_by_tag_name('html')
driver.get("https://www.poetryfoundation.org/poems/browse#page=22&sort_by=recently_added&preview=1")
new_page = driver.find_element_by_tag_name('html')
wait_for(page_has_loaded(old_page, new_page))
print('The page has finally loaded!')