#!/usr/bin/env python
# coding: utf-8

# In[268]:

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

COMITENTE = "PODER JUDICIAL"

perito = input("Perito:")
pericia = input("Nombre autos:")
print("")
honorarios = float(input("Ingrese honorarios:"))
monto_caja = float(input("Ingrese monto aportado a caja:"))
medio_pago_caja = input("Medio de pago (T/C/MP/PF/PL/RP):")
comprobante_caja = input("Cód. comprobante caja:")
fecha_pago_caja = input("Fecha de pago caja:")
print("")

def aportes5(honor):
    if honor <= 36000:
        arancel_5 = 1800
        return arancel_5
    else:
        arancel_5 = honor * 0.05
        return arancel_5

def calculoCiec():
    arancel_adm = 1200
    aporte_ciec = aportes5(honorarios) + arancel_adm
    return aporte_ciec


# In[269]:
#options = ChromeOptions()
#options.add_argument("--headless")
#assert options.headless
driver = webdriver.Chrome()#options=options)
driver.get("https://crmciec.hostingcrm.com.ar/index.php?module=Users&action=Login")

# In[270]:


usuario = driver.find_element(by=By.NAME, value="user_name")  
usuario.send_keys('nicolas.vivas')

password = driver.find_element(by=By.NAME, value="username_password") 
password.send_keys('12345')


# In[271]:
submit_btn = driver.find_element(by=By.NAME, value="Login")  
submit_btn.click()

# In[272]:

driver.find_element(By.LINK_TEXT, value="Crear").click()

# In[273]:

driver.find_element(By.LINK_TEXT, value="Create Expedientes").click()

# In[274]:

#Buscar matriculado
driver.find_element(By.ID, value="btn_account_name").click()


# In[275]:

driver.switch_to.window(driver.window_handles[1])

# In[276]:

driver.find_element(By.XPATH, value='//*[@id="name_advanced"]').send_keys(f'{perito}')


# In[277]:

#Seleccionamos estado 'Activo'
driver.find_element(By.XPATH, value='//*[@id="estado_despl_c_advanced"]/option[1]').click()

# In[278]:

driver.find_element(By.XPATH, value='//*[@id="search_form_submit"]').click()


# In[279]:

driver.find_element(By.XPATH, value='/html/body/table[4]/tbody/tr/td[2]/a').click()

# In[280]:

driver.switch_to.window(driver.window_handles[0])

# In[282]:

#Vamos a seleccionar comitente
driver.find_element(By.ID, value="btn_comitente_c").click()
driver.switch_to.window(driver.window_handles[1])
#driver.current_url

# In[283]:

# Buscamos Poder Judicial
driver.find_element(By.XPATH, value='//*[@id="name_advanced"]').send_keys(f'{COMITENTE}')
driver.find_element(By.XPATH, value='//*[@id="search_form_submit"]').click()

# In[284]:

# Seleccionamos Poder Judicial
driver.find_element(By.XPATH, value='/html/body/table[4]/tbody/tr[2]/td[2]/a').click()

# In[285]:

driver.switch_to.window(driver.window_handles[0])
#driver.current_url

# In[286]:

#Seleccionamos Pericia Judicial
driver.find_element(By.XPATH, value='//*[@id="opportunity_type"]/option[6]').click()

# In[287]:

#Colocamos autos
driver.find_element(By.ID, value="description").send_keys(f'PER.JUD.{pericia.upper()}')


# In[288]:

driver.find_element(By.XPATH, value='//*[@id="SAVE"]').click()

# In[289]:
time.sleep(5)
# Iniciamos creación de Tarea de Expediente
driver.find_element(By.XPATH, value='/html/body/div[3]/div/div/ul/li[1]/div/div[1]/a/div').click()
time.sleep(5)

# In[290]:

driver.find_element(By.LINK_TEXT, value="Nuevo").click()

# In[291]:

driver.find_element(By.XPATH, value='//*[@id="tipo_tarea_c"]/option[29]').click()

# In[292]:

driver.find_element(By.ID, value="btn_accounts_knn_tareasexpediente_1_name").click()

# In[293]:

driver.switch_to.window(driver.window_handles[1])

# In[294]:

driver.find_element(By.XPATH, value='//*[@id="name_advanced"]').send_keys(f'{perito}')
driver.find_element(By.XPATH, value='//*[@id="estado_despl_c_advanced"]/option[1]').click()
driver.find_element(By.XPATH, value='//*[@id="search_form_submit"]').click()

# In[295]:

driver.find_element(By.XPATH, value='/html/body/table[4]/tbody/tr/td[2]/a').click()

# In[296]:

driver.switch_to.window(driver.window_handles[0])

# In[297]:

driver.find_element(By.XPATH, value='//*[@id="monto_obra"]').send_keys('0')
driver.find_element(By.XPATH, value='//*[@id="monto_honorario"]').send_keys(f'{honorarios}')

# In[298]:

driver.find_element(By.ID, value="btn_knn_comitente_knn_tareasexpediente_1_name").click()

# In[299]:

driver.switch_to.window(driver.window_handles[1])

# In[300]:

driver.find_element(By.XPATH, value='//*[@id="name_advanced"]').send_keys(f'{COMITENTE}')
driver.find_element(By.XPATH, value='//*[@id="search_form_submit"]').click()
driver.find_element(By.XPATH, value='/html/body/table[4]/tbody/tr[2]/td[2]/a').click()

# In[301]:

driver.switch_to.window(driver.window_handles[0])

# In[302]:

driver.find_element(By.XPATH, value='//*[@id="description"]').clear() # Así borramos cualquier otro valor predeterminado que pueda tener el campo
driver.find_element(By.XPATH, value='//*[@id="description"]').send_keys(f'PER.JUD.{pericia.upper()}')

# In[303]:

estado = input('Ingrese estado (Aprobado/Observado):')
state = estado.lower()

# In[304]:

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


# In[305]:


driver.find_element(By.XPATH, value='//*[@id="obra_c"]').send_keys(f'PER.JUD.{pericia.upper()}')
driver.find_element(By.XPATH, value='//*[@id="obra_cp"]').send_keys('5000')
driver.find_element(By.XPATH, value='//*[@id="obra_direccion"]').send_keys('CORDOBA')
driver.find_element(By.XPATH, value='//*[@id="obra_localidad"]').send_keys('CAPITAL')


# In[306]:

driver.find_element(By.ID, value="btn_created_by_name").click()

# In[307]:

driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.XPATH, value='//*[@id="last_name_advanced"]').send_keys('vivas')
driver.find_element(By.XPATH, value='//*[@id="search_form_submit"]').click()
driver.find_element(By.XPATH, value='/html/body/table[4]/tbody/tr/td[1]/a').click()

# In[308]:

driver.switch_to.window(driver.window_handles[0])
time.sleep(5)

# In[309]:

driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/form/div[3]/input[1]').click()

# In[310]:

time.sleep(5)
driver.find_element(By.XPATH, value='//*[@id="subpanel_title_opportunities_knn_tareasexpediente_1"]/div/div').click()
driver.find_element(By.XPATH, value='//*[@id="list_subpanel_opportunities_knn_tareasexpediente_1"]/table/tbody/tr/td[2]/a').click()

# In[311]:
# Cargamos aportes a la Caja
driver.find_element(By.XPATH, value='//*[@id="subpanel_title_knn_tareasexpediente_knn_aportes_terceros_1"]/div/div').click()
time.sleep(5)
driver.find_element(By.XPATH, value='//*[@id="KNN_Aportes_Terceros_nuevo_button"]').click()

# In[312]:

driver.find_element(By.XPATH, value='//*[@id="description"]').send_keys(f'PER.JUD.{pericia.upper()}')
driver.find_element(By.XPATH, value='//*[@id="monto_c"]').send_keys(f'{monto_caja}')

# In[313]:
caja_upper = medio_pago_caja.upper()

# In[314]:

match caja_upper:
    case 'T':
        driver.find_element(By.XPATH, value='//*[@id="lugar_pago_c"]/option[1]').click()
    case 'C':
        driver.find_element(By.XPATH, value='//*[@id="lugar_pago_c"]/option[4]').click()
    case 'MP':
        driver.find_element(By.XPATH, value='//*[@id="lugar_pago_c"]/option[10]').click()
    case 'PF':
        driver.find_element(By.XPATH, value='//*[@id="lugar_pago_c"]/option[12]').click()
    case 'PL':
        driver.find_element(By.XPATH, value='//*[@id="lugar_pago_c"]/option[13]').click()
    case 'RP':
        driver.find_element(By.XPATH, value='//*[@id="lugar_pago_c"]/option[15]').click()

# In[316]:

try:
    boleta_numerica = int(comprobante_caja)
    driver.find_element(By.XPATH, value='//*[@id="nroboleta_c"]').send_keys(boleta_numerica)
    driver.find_element(By.XPATH, value='//*[@id="n_boleta_c"]').send_keys(boleta_numerica)
except:
    driver.find_element(By.XPATH, value='//*[@id="description"]').send_keys('\n' + comprobante_caja)

# In[318]:

driver.find_element(By.XPATH, value='//*[@id="fecha_pago_c"]').clear()
driver.find_element(By.XPATH, value='//*[@id="fecha_pago_c"]').send_keys(fecha_pago_caja)

# In[319]:

driver.find_element(By.XPATH, value='/html/body/div[3]/div/div/form/div[3]/input[1]').click()

# In[320]:

#Descargamos carátula expediente
time.sleep(5)
driver.find_element(By.XPATH, value='//*[@id="tab-actions"]/a').click()
driver.find_element(By.XPATH, value='//*[@id="tab-actions"]/ul/li[5]/input').click()
driver.find_element(By.XPATH, value='//*[@id="popupForm"]/table/tbody/tr[3]/td[2]/a').click()

# In[321]:

time.sleep(5)
# Traemos nro de expediente - probar
#driver.find_element(By.XPATH, value='//*[@id="opportunities_knn_tareasexpediente_1opportunities_ida"]').text
driver.quit()

print("Aporte 5%:", aportes5(honorarios))
print("Total aportes:", calculoCiec())