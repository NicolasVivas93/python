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

time.sleep(3.5)
pyautogui.press("delete")
pyautogui.press("enter")


#9 veces flecha abajo
for i in range(9):
    pyautogui.press("down")

verificar = input("Es correcto el numero de factura? (Y/N):")
verif_lower = verificar.lower()

if verif_lower == 'n':
    print("Factura incorrecta")
elif verif_lower == 'y':
    print("Factura correcta, volver a Tango")
    time.sleep(5)
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.press("enter")
    pyautogui.typewrite("unc-FCEF")
    pyautogui.press("enter")
    pyautogui.press("enter")
    
    for i in range(5):
        time.sleep(0.5)
        pyautogui.press("enter")
    
    
    


    
    

