import time

#!/usr/bin/env python
# coding: utf-8

# In[118]:


from selenium import webdriver
from selenium.webdriver.common.by import By


# In[119]:


driver = webdriver.Chrome()
driver.get("https://crmciec.hostingcrm.com.ar/index.php?module=Users&action=Login")


# In[120]:


usuario = driver.find_element(by=By.NAME, value="user_name")  
usuario.send_keys('nicolas.vivas')

password = driver.find_element(by=By.NAME, value="username_password") 
password.send_keys('12345')


# In[121]:


submit_btn = driver.find_element(by=By.NAME, value="Login")  
submit_btn.click()


# In[122]:


driver.find_element(By.LINK_TEXT, value="Crear").click()


# In[123]:


driver.find_element(By.LINK_TEXT, value="Create Expedientes").click()


# In[124]:


#Buscar matriculado
driver.find_element(By.ID, value="btn_account_name").click()


# In[125]:


driver.switch_to.window(driver.window_handles[1])


# In[126]:


driver.find_element(By.XPATH, value='//*[@id="name_advanced"]').send_keys('ANTUÑA')


# In[127]:


#Seleccionamos estado 'Activo'
driver.find_element(By.XPATH, value='//*[@id="estado_despl_c_advanced"]/option[1]').click()


# In[128]:


driver.find_element(By.XPATH, value='//*[@id="search_form_submit"]').click()


# In[129]:


driver.find_element(By.XPATH, value='/html/body/table[4]/tbody/tr/td[2]/a').click()


# In[130]:


driver.switch_to.window(driver.window_handles[0])


# In[101]:


#driver.current_url


# In[131]:


#Vamos a seleccionar comitente
driver.find_element(By.ID, value="btn_comitente_c").click()
driver.switch_to.window(driver.window_handles[1])
driver.current_url


# In[132]:


# Buscamos Poder Judicial
driver.find_element(By.XPATH, value='//*[@id="name_advanced"]').send_keys('PODER JUDICIAL')
driver.find_element(By.XPATH, value='//*[@id="search_form_submit"]').click()


# In[133]:


# Seleccionamos Poder Judicial
driver.find_element(By.XPATH, value='/html/body/table[4]/tbody/tr[2]/td[2]/a').click()


# In[134]:


driver.switch_to.window(driver.window_handles[0])
#driver.current_url


# In[135]:


#Seleccionamos Pericia Judicial
driver.find_element(By.XPATH, value='//*[@id="opportunity_type"]/option[6]').click()


# In[136]:


#Colocamos autos
driver.find_element(By.ID, value="description").send_keys('PER.JUD.')


# In[137]:


driver.find_element(By.XPATH, value='//*[@id="SAVE"]').click()


# In[138]:

time.sleep(7)
driver.quit()
