#!/usr/bin/env python
# coding: utf-8

# In[119]:
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

# In[120]:
options = ChromeOptions()
options.add_argument("--headless")
assert options.headless
driver = webdriver.Chrome(options=options)
driver.get("https://a.paypertic.com/auth/realms/entidades/protocol/openid-connect/auth?client_id=16465308-1844-4abe-abe6-f184149ee740&redirect_uri=https%3A%2F%2Fentidad.paypertic.com%2F&state=2f7b7ac3-ff5d-41ad-b36a-07a138c13bfb&response_mode=fragment&response_type=code&scope=openid&nonce=713b8dc8-89e7-485b-8e0c-529ff3d110f6")

# In[121]:

usuario = driver.find_element(By.XPATH, value='//*[@id="username"]').send_keys('pablo.lardelli@ciec.com.ar')
password = driver.find_element(By.XPATH, value='//*[@id="password"]').send_keys('Contabilidad2020')
driver.find_element(By.ID, value="kc-login").click()


# In[122]:

time.sleep(10)
driver.maximize_window()
driver.find_element(By.XPATH, value='/html/body/app-root/app-secured/div/app-home/div/div[1]/div/app-buttons-options/div/div[3]/button').click()


# In[123]:

time.sleep(7)
saldo_str = driver.find_element(By.XPATH, value='/html/body/app-root/app-secured/div/app-withdrawal/div/div[4]/div[1]/div/div[2]').text
saldo = saldo_str[4:]
saldo = saldo.replace('.','')
saldo = saldo.replace(',','.')
saldo = float(saldo)


# In[124]:

print(f'El saldo disponible es de: ${saldo}')

# In[125]:

if saldo >= 25000:
    driver.find_element(By.XPATH, value='/html/body/app-root/app-secured/div/app-withdrawal/div/div[2]/div[2]/button/span').click()

# In[126]:

time.sleep(7)
driver.find_element(By.XPATH, value='/html/body/app-root/app-secured/div/app-retire/div/div[2]/form/div/div[2]/mat-radio-group/mat-radio-button[2]/label/span[1]/span[2]').click()
driver.find_element(By.XPATH, value='/html/body/app-root/app-secured/div/app-retire/div/div[2]/form/div/div[3]/div/input').send_keys('1910100455010002524914')
driver.find_element(By.XPATH, value='/html/body/app-root/app-secured/div/app-retire/div/div[2]/form/div/div[4]/mat-checkbox/label').click()
driver.find_element(By.XPATH, value='/html/body/app-root/app-secured/div/app-retire/div/div[2]/form/div/button').click()

# In[127]:

time.sleep(3)
driver.find_element(By.XPATH, value='/html/body/div[3]/div[2]/div/mat-dialog-container/app-confirm-dialog/div/div[3]/button[2]').click()

# In[128]:

time.sleep(5)
driver.quit()
print("Importe solicitado con éxito")

