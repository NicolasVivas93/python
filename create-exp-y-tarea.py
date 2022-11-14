#!/usr/bin/env python
# coding: utf-8

# In[206]:

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# In[207]:

driver = webdriver.Chrome()
driver.get("https://crmciec.hostingcrm.com.ar/index.php?module=Users&action=Login")


# In[208]:


usuario = driver.find_element(by=By.NAME, value="user_name")  
usuario.send_keys('nicolas.vivas')

password = driver.find_element(by=By.NAME, value="username_password") 
password.send_keys('12345')


# In[209]:


submit_btn = driver.find_element(by=By.NAME, value="Login")  
submit_btn.click()


# In[210]:


driver.find_element(By.LINK_TEXT, value="Crear").click()


# In[211]:


driver.find_element(By.LINK_TEXT, value="Create Expedientes").click()


# In[212]:


#Buscar matriculado
driver.find_element(By.ID, value="btn_account_name").click()


# In[213]:


driver.switch_to.window(driver.window_handles[1])


# In[214]:


driver.find_element(By.XPATH, value='//*[@id="name_advanced"]').send_keys('ANTUÑA')


# In[215]:


#Seleccionamos estado 'Activo'
driver.find_element(By.XPATH, value='//*[@id="estado_despl_c_advanced"]/option[1]').click()


# In[216]:


driver.find_element(By.XPATH, value='//*[@id="search_form_submit"]').click()


# In[217]:


driver.find_element(By.XPATH, value='/html/body/table[4]/tbody/tr/td[2]/a').click()


# In[218]:


driver.switch_to.window(driver.window_handles[0])


# In[219]:


#driver.current_url


# In[220]:


#Vamos a seleccionar comitente
driver.find_element(By.ID, value="btn_comitente_c").click()
driver.switch_to.window(driver.window_handles[1])
driver.current_url


# In[221]:


# Buscamos Poder Judicial
driver.find_element(By.XPATH, value='//*[@id="name_advanced"]').send_keys('PODER JUDICIAL')
driver.find_element(By.XPATH, value='//*[@id="search_form_submit"]').click()


# In[222]:


# Seleccionamos Poder Judicial
driver.find_element(By.XPATH, value='/html/body/table[4]/tbody/tr[2]/td[2]/a').click()


# In[223]:


driver.switch_to.window(driver.window_handles[0])
#driver.current_url


# In[224]:


#Seleccionamos Pericia Judicial
driver.find_element(By.XPATH, value='//*[@id="opportunity_type"]/option[6]').click()


# In[225]:


#Colocamos autos
driver.find_element(By.ID, value="description").send_keys('PER.JUD.')


# In[226]:


driver.find_element(By.XPATH, value='//*[@id="SAVE"]').click()


# In[227]:


# Iniciamos creación de Tarea de Expediente
driver.find_element(By.XPATH, value='//*[@id="subpanel_title_opportunities_knn_tareasexpediente_1"]/div/div').click()
time.sleep(5)


# In[228]:


driver.find_element(By.LINK_TEXT, value="Nuevo").click()


# In[229]:


driver.find_element(By.XPATH, value='//*[@id="tipo_tarea_c"]/option[29]').click()


# In[230]:


driver.find_element(By.ID, value="btn_accounts_knn_tareasexpediente_1_name").click()


# In[231]:


driver.switch_to.window(driver.window_handles[1])


# In[232]:


driver.find_element(By.XPATH, value='//*[@id="name_advanced"]').send_keys('ANTUÑA')
driver.find_element(By.XPATH, value='//*[@id="estado_despl_c_advanced"]/option[1]').click()
driver.find_element(By.XPATH, value='//*[@id="search_form_submit"]').click()


# In[233]:


driver.find_element(By.XPATH, value='/html/body/table[4]/tbody/tr/td[2]/a').click()


# In[234]:


driver.switch_to.window(driver.window_handles[0])


# In[235]:


driver.find_element(By.XPATH, value='//*[@id="monto_obra"]').send_keys('0')
driver.find_element(By.XPATH, value='//*[@id="monto_honorario"]').send_keys('40000')


# In[236]:


driver.find_element(By.ID, value="btn_knn_comitente_knn_tareasexpediente_1_name").click()


# In[237]:


driver.switch_to.window(driver.window_handles[1])


# In[238]:


driver.find_element(By.XPATH, value='//*[@id="name_advanced"]').send_keys('PODER JUDICIAL')
driver.find_element(By.XPATH, value='//*[@id="search_form_submit"]').click()
driver.find_element(By.XPATH, value='/html/body/table[4]/tbody/tr[2]/td[2]/a').click()


# In[239]:


driver.switch_to.window(driver.window_handles[0])


# In[240]:


driver.find_element(By.XPATH, value='//*[@id="description"]').clear() # Así borramos cualquier otro valor predeterminado que pueda tener el campo
driver.find_element(By.XPATH, value='//*[@id="description"]').send_keys('PER.JUD.')


# In[241]:


estado = input('Ingrese estado:')
state = estado.lower()


# In[242]:


if state == 'observado':
    observacion = input('Ingrese observacion:')
    driver.find_element(By.XPATH, value='//*[@id="estado_tarea_c"]/option[10]').click()
    driver.find_element(By.ID, value="btn_visador_c").click()
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.XPATH, value='//*[@id="last_name_advanced"]').send_keys('ciec')
    driver.find_element(By.XPATH, value='//*[@id="search_form_submit"]').click()
    driver.find_element(By.XPATH, value='/html/body/table[4]/tbody/tr/td[1]/a').click()
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.XPATH, value='//*[@id="observacion_tarea_c"]').send_keys(observacion)
else:
    driver.find_element(By.XPATH, value='//*[@id="estado_tarea_c"]/option[1]').click()


# In[243]:


driver.find_element(By.XPATH, value='//*[@id="obra_c"]').send_keys('PER.JUD.')
driver.find_element(By.XPATH, value='//*[@id="obra_cp"]').send_keys('5000')
driver.find_element(By.XPATH, value='//*[@id="obra_direccion"]').send_keys('CORDOBA')
driver.find_element(By.XPATH, value='//*[@id="obra_localidad"]').send_keys('CAPITAL')


# In[244]:


driver.find_element(By.ID, value="btn_created_by_name").click()


# In[245]:


driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.XPATH, value='//*[@id="last_name_advanced"]').send_keys('vivas')
driver.find_element(By.XPATH, value='//*[@id="search_form_submit"]').click()
driver.find_element(By.XPATH, value='/html/body/table[4]/tbody/tr/td[1]/a').click()


# In[246]:

driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
driver.find_element(By.LINK_TEXT, value="GUARDAR").click()
#https://stackoverflow.com/questions/11908249/debugging-element-is-not-clickable-at-point-error
#https://www.lambdatest.com/blog/how-to-deal-with-element-is-not-clickable-at-point-exception-using-selenium/
# In[ ]:

driver.quit()

