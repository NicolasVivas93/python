import os

COMITENTE = "PODER JUDICIAL DE LA PROVINCIA DE CORDOBA"

perito = input("Perito:")
pericia = input("Nombre autos:")
print("")
pago_tribunales = float(input("Importe pagado por tribunales:"))
honorarios = float(input("Ingrese honorarios:"))
fecha_pago = input("Fecha de pago:")
print("")
monto_caja = float(input("Ingrese monto aportado a caja:"))
comprobante_caja = input("Cód. comprobante caja:")
medio_pago_caja = input("Medio de pago:")
fecha_pago_caja = input("Fecha de pago caja:")
print("")
pago_sellos = float(input("Ingrese monto pagado por sellos:"))
print("")
cbu = int(input("CBU perito:"))
print("")
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

def calculoCaja(honor):
    aporte_caja = honor * 0.18
    return aporte_caja

def calculoSellos(honor):
    sellos = honor * 0.012
    bonificacion = sellos * 0.30
    total_sellos = sellos - bonificacion 
    return total_sellos


def validarAportesCaja(aporte_corr, aporte_prof):
    if aporte_corr != aporte_prof:
        diferencia = aporte_corr - aporte_prof
    
    return "Existe una diferencia de aportes de:", diferencia

     
def validarAportesSellos(sellos_corr, sellos_prof):
    if sellos_corr != sellos_prof:
        diferencia = sellos_corr - sellos_prof
    
    return "Existe una diferencia de sellos de:", diferencia


def totalAPagar(tribunales,aporte_ciec):
    calculo = tribunales - aporte_ciec
    return calculo


print("Perito:", perito)
os.mkdir(f"C:/Users/nvivas/Desktop/PERICIAS/{perito}")
print("PER.JUD." + pericia.upper())
print("Comitente:", COMITENTE)
print("Honorarios:", honorarios)
print("")

print(f"Importe depositado: {pago_tribunales} - Fecha: {fecha_pago}")
print("Aporte 5%:", aportes5(honorarios))
print("Total aportes:", calculoCiec())
print("Total a pagar a perito:" , totalAPagar(pago_tribunales, calculoCiec()))
print("")

print("Caja:", calculoCaja(honorarios))
print("Sellos:", calculoSellos(honorarios))
print("")

print("VALIDACIONES:")
print(validarAportesCaja(calculoCaja(honorarios), monto_caja))
print(validarAportesSellos(calculoSellos(honorarios), pago_sellos))



#my_file = r'C:\Users\nvivas\Desktop\PERICIAS\LIQUIDACIONESPERITOS.xlsx'
#os.startfile(my_file)

#Data de ingreso:
# CBU




#Data salida
# Mostrar total a pagar

# Definir funciones de:
# - Validación de aportes
# - Calculo de total a pagar

# Base de datos rudimentaria:
# - Copiar data a un archivo json
# - Leer data de un archivo json
# - Cargar CBU's de peritos en archivo json para comparar. Crear función validadora de cbu's