import os

COMITENTE = "PODER JUDICIAL"
perito = input("Perito:")
pericia = input("Nombre autos:")
honorarios = float(input("Ingrese honorarios:"))

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

def calculoCaja(honor):
    aporte_caja = honor * 0.18
    return aporte_caja

def calculoSellos(honor):
    sellos = honor * 0.012
    bonificacion = sellos * 0.30
    total_sellos = sellos - bonificacion 
    return total_sellos

print("Perito:", perito)
print("PER.JUD." + pericia.upper())
print("Comitente:", COMITENTE)
print("Honorarios:", honorarios)
print("Aporte 5%:", aportes5(honorarios))
print("Total aportes:", calculoCiec())
print("Caja:", calculoCaja(honorarios))
print("Sellos:", calculoSellos(honorarios))


#my_file = r'C:\Users\nvivas\Desktop\PERICIAS\LIQUIDACIONESPERITOS.xlsx'
#os.startfile(my_file)

#Data de ingreso:




#Data salida