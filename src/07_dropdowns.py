from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select 

# Chrome 
executable_path = 'D:/Pranjal Tutorial Videos/GitHub/AI-Poet/selenium_drivers/chromedriver.exe'
driver = webdriver.Chrome(executable_path)

driver.get("http://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

element = driver.find_element(By.XPATH, '//*[@id="RESULT_RadioButton-9"]')
dropdown = Select(element)
# print(dropdown.options)

for option in dropdown.options:
    print(option.text)

driver.quit()