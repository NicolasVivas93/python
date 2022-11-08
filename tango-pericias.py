COMITENTE = "PODER JUDICIAL DE LA PROVINCIA DE CORDOBA"

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

print("Aporte 5%:", aportes5(honorarios))
print("Total aportes:", calculoCiec())
print("Comitente:", COMITENTE)
print("PER.JUD." + pericia.upper())
print("Perito:", perito)