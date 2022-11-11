COMITENTE = "PODER JUDICIAL DE LA PROVINCIA DE CORDOBA"

perito = input("Perito:")
pericia = input("Nombre autos:")
print("")
honorarios = float(input("Ingrese honorarios:"))
monto_caja = float(input("Ingrese monto aportado a caja:"))
comprobante_caja = input("Cód. comprobante caja:")
medio_pago_caja = input("Medio de pago:")
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


print(f"Perito: {perito}" )
print(f"PER.JUD.{pericia.upper()}")
print(f"Comitente: {COMITENTE}")
print("")
print(f"Honorarios: {honorarios}")
print("Aporte 5%:", aportes5(honorarios))
print("Total aportes:", calculoCiec())