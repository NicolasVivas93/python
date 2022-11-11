import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://crmciec.hostingcrm.com.ar/index.php?module=Users&action=Login")

usuario = driver.find_element(by=By.NAME, value="user_name")  
usuario.send_keys('nicolas.vivas')

password = driver.find_element(by=By.NAME, value="username_password") 
password.send_keys('12345')

submit_btn = driver.find_element(by=By.NAME, value="Login")  
submit_btn.click()

dropdown_crear = driver.find_element(By.XPATH, value='//*[@id="quickcreatetop"]/a')
action = ActionChains(driver)
action.move_to_element(dropdown_crear)
action.perform()

time.sleep(3)





