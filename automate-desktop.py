import pyautogui
import time

# Posicionar el cursor en las coordenadas del ícono de Tango
pyautogui.moveTo(465, 744)
pyautogui.click()

# Entrar a Facturas (agregada a Favoritos para acceso rápido)
time.sleep(2)
pyautogui.moveTo(1122, 213)
pyautogui.doubleClick()

#Seleccionar modelo de facturación UNICO
time.sleep(3.5)
pyautogui.press("enter")

# Borrar talonario predeterminado y entrar a seleccion de talonario
time.sleep(5)
pyautogui.press("delete")
pyautogui.press("enter")


#9 veces flecha abajo para seleccionar talonario nro 11
for i in range(9):
    pyautogui.press("down")

time.sleep(5)
pyautogui.press("enter") # Seleccion de talonario 11
time.sleep(0.5)
pyautogui.press("enter")
time.sleep(0.5)
pyautogui.press("enter")
pyautogui.typewrite("unc-FCEF") # Seleccionar universidad
pyautogui.press("enter") 
pyautogui.press("enter")
    
for i in range(5):
    time.sleep(0.5)
    pyautogui.press("enter")
    
time.sleep(0.5)
pyautogui.typewrite("OBRA A") # Arancel 5%
pyautogui.press("enter")
pyautogui.press("enter")
time.sleep(0.3)
pyautogui.typewrite("1") # Cantidad
pyautogui.press("enter")
time.sleep(0.3)
pyautogui.typewrite("1800") # Importe
pyautogui.press("enter")
pyautogui.press("enter")

time.sleep(0.5)
pyautogui.press("enter")
pyautogui.typewrite("OBRA A") # Arancel administrativo
pyautogui.press("down")
pyautogui.press("enter")
time.sleep(0.3)
pyautogui.press("enter")
pyautogui.typewrite("1") # Cantidad
pyautogui.press("enter")
time.sleep(0.3)
pyautogui.typewrite("1200") # Importe
pyautogui.press("enter")
pyautogui.press("enter")
    
    
time.sleep(0.5)
pyautogui.press("enter")
pyautogui.typewrite("TASA") # Tasa por agrupacion de informe RNI
pyautogui.press("enter")
pyautogui.press("enter")
time.sleep(0.3)
pyautogui.typewrite("20") # Cantidad
pyautogui.press("enter")
time.sleep(0.3)
pyautogui.typewrite("1085") # Importe
pyautogui.press("enter")
pyautogui.press("enter")
    
    


    
    

