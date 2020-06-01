from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
 
# Chrome 
driver = webdriver.Chrome(executable_path='D:/Pranjal Tutorial Videos/GitHub/AI-Poet/selenium_drivers/chromedriver.exe')

driver.implicitly_wait(5)

driver.maximize_window()
driver.get("http://www.expedia.co.in/")
driver.find_element(By.ID, 'tab-flight-tab-hp').click() # Click the Flight Button

driver.find_element(By.ID, 'flight-origin-hp-flight').send_keys('SFO')
time.sleep(2)
driver.find_element(By.ID, 'flight-destination-hp-flight').send_keys('NYC')

driver.find_element(By.ID, 'flight-departing-hp-flight').clear() # Clear the field
driver.find_element(By.ID, 'flight-departing-hp-flight').send_keys('12/10/2020') 
driver.find_element(By.ID, 'flight-returning-hp-flight').clear() # Clear the field
driver.find_element(By.ID, 'flight-returning-hp-flight').send_keys('12/19/2020') 
driver.find_element(By.XPATH, '//*[@id="gcw-flights-form-hp-flight"]/div[9]/label/button').click()

wait = WebDriverWait(driver, 10)
# driver.find_element(By.XPATH, '//*[@id="changeOptionFilter-0"]')
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="changeOptionFilter-0"]')))
element.click()
time.sleep(5)

driver.quit() 