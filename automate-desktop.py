import pyautogui
import time

pos = pyautogui.position() #Obtener la position del cursor
print(pos)

#Posicionar el cursor en las coordenadas del ícono de Tango
pyautogui.moveTo(465,744)
pyautogui.click()

time.sleep(2)
pyautogui.moveTo(1122,213)
pyautogui.doubleClick()

time.sleep(3.5)
pyautogui.press("enter")


