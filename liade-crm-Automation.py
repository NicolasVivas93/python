#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# In[3]:


driver = webdriver.Chrome()
driver.get("https://crmciec.hostingcrm.com.ar/index.php?module=Users&action=Login")


# In[4]:


usuario = driver.find_element(by=By.NAME, value="user_name")  
usuario.send_keys('nicolas.vivas')

password = driver.find_element(by=By.NAME, value="username_password") 
password.send_keys('12345')


# In[5]:


submit_btn = driver.find_element(by=By.NAME, value="Login")  
submit_btn.click()


# In[6]:


driver.find_element(By.LINK_TEXT, value="Crear").click()


# In[7]:


driver.find_element(By.LINK_TEXT, value="Create Expedientes").click()


# In[8]:


#Buscar matriculado
driver.find_element(By.ID, value="btn_account_name").click()


# In[9]:


driver.switch_to.window(driver.window_handles[1])


# In[13]:


driver.find_element(By.XPATH, value='//*[@id="name_advanced"]').send_keys('VANELLA OSCAR RODOLFO')


# In[14]:


driver.find_element(By.XPATH, value='//*[@id="search_form_submit"]').click()


# In[15]:


#Seleccionamos el matriculado del listado
driver.find_element(By.XPATH, value='/html/body/table[4]/tbody/tr/td[2]/a').click()


# In[16]:


driver.switch_to.window(driver.window_handles[0])


# In[281]:


#driver.current_url


# In[17]:


#Vamos a seleccionar comitente
driver.find_element(By.ID, value="btn_comitente_c").click()
driver.switch_to.window(driver.window_handles[1])
driver.current_url


# In[18]:


# Buscamos ERSEP
driver.find_element(By.XPATH, value='//*[@id="name_advanced"]').send_keys('ERSEP (ENTE REGULADOR DE S.P.)')
driver.find_element(By.XPATH, value='//*[@id="search_form_submit"]').click()


# In[19]:


# Seleccionamos ERSEP
driver.find_element(By.XPATH, value='/html/body/table[4]/tbody/tr/td[2]/a').click()


# In[20]:


driver.switch_to.window(driver.window_handles[0])
#driver.current_url


# In[21]:


#Seleccionamos Tipo de Expediente: Otros
driver.find_element(By.XPATH, value='//*[@id="opportunity_type"]/option[7]').click()


# In[24]:


#Colocamos Descripción
driver.find_element(By.ID, value="description").send_keys('20 INFORMES DE MEDICION RNI')


# In[25]:


driver.maximize_window()
driver.find_element(By.XPATH, value='//*[@id="SAVE"]').click()


# In[26]:


# Iniciamos creación de Tarea de Expediente
time.sleep(5)
driver.find_element(By.XPATH, value='//*[@id="subpanel_title_opportunities_knn_tareasexpediente_1"]/div/div').click()
time.sleep(5)


# In[27]:


driver.find_element(By.LINK_TEXT, value="Nuevo").click()


# In[28]:


driver.find_element(By.XPATH, value='//*[@id="tipo_tarea_c"]/option[31]').click()


# In[29]:


driver.find_element(By.ID, value="btn_accounts_knn_tareasexpediente_1_name").click()


# In[30]:


driver.switch_to.window(driver.window_handles[1])


# In[31]:


driver.find_element(By.XPATH, value='//*[@id="name_advanced"]').send_keys('VANELLA OSCAR RODOLFO')
driver.find_element(By.XPATH, value='//*[@id="search_form_submit"]').click()


# In[32]:


driver.find_element(By.XPATH, value='/html/body/table[4]/tbody/tr/td[2]/a').click()


# In[33]:


driver.switch_to.window(driver.window_handles[0])


# In[34]:


driver.find_element(By.XPATH, value='//*[@id="monto_obra"]').send_keys('0')
driver.find_element(By.XPATH, value='//*[@id="monto_honorario"]').send_keys('36000')


# In[35]:


#Buscamos comitente
driver.find_element(By.ID, value="btn_knn_comitente_knn_tareasexpediente_1_name").click()


# In[36]:


driver.switch_to.window(driver.window_handles[1])


# In[38]:


driver.find_element(By.XPATH, value='//*[@id="name_advanced"]').send_keys('ERSEP (ENTE REGULADOR DE S.P.)')
driver.find_element(By.XPATH, value='//*[@id="search_form_submit"]').click()
driver.find_element(By.XPATH, value='/html/body/table[4]/tbody/tr/td[2]/a').click()


# In[39]:


driver.switch_to.window(driver.window_handles[0])


# In[40]:


driver.find_element(By.XPATH, value='//*[@id="description"]').clear() # Así borramos cualquier otro valor predeterminado que pueda tener el campo
driver.find_element(By.XPATH, value='//*[@id="description"]').send_keys('20 INFORMES DE MEDICION RNI')


# In[41]:


driver.find_element(By.XPATH, value='//*[@id="obra_c"]').send_keys('20 INFORMES DE MEDICION RNI')
driver.find_element(By.XPATH, value='//*[@id="obra_cp"]').send_keys('5000')
driver.find_element(By.XPATH, value='//*[@id="obra_direccion"]').send_keys('CORDOBA')
driver.find_element(By.XPATH, value='//*[@id="obra_localidad"]').send_keys('CAPITAL')


# In[42]:


driver.find_element(By.ID, value="btn_created_by_name").click()


# In[43]:


driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.XPATH, value='//*[@id="last_name_advanced"]').send_keys('vivas')
driver.find_element(By.XPATH, value='//*[@id="search_form_submit"]').click()
driver.find_element(By.XPATH, value='/html/body/table[4]/tbody/tr/td[1]/a').click()


# In[44]:


driver.switch_to.window(driver.window_handles[0])
time.sleep(5)


# In[45]:


driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/form/div[3]/input[1]').click()


# In[54]:


#Descargamos carátula expediente
time.sleep(5)
driver.find_element(By.XPATH, value='//*[@id="list_subpanel_opportunities_knn_tareasexpediente_1"]/table/tbody/tr/td[2]/a').click()
driver.find_element(By.XPATH, value='/html/body/div[3]/div/div/div[4]/ul/li[2]/a').click()
driver.find_element(By.XPATH, value='//*[@id="tab-actions"]/ul/li[5]/input').click()
driver.find_element(By.XPATH, value='//*[@id="popupForm"]/table/tbody/tr[3]/td[2]/a/b').click()


# In[58]:


time.sleep(5)
driver.quit()

