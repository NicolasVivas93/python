pesos = input("¿Cuantos pesos argentinos tienes?: ")
pesos = float(pesos)
valor_dolar = 275
dolares = pesos / valor_dolar
dolares = round(dolares, 2) #redondeamos los decimales a dos dígitos decimales
dolares = str(dolares) # convertimos a texto la variable dolares

print("Tienes $" + dolares + " dolares")

usd = input("Cuantos dolares tienes:")
usd = float(usd)
ars = valor_dolar * usd
ars = round(ars, 2)
ars = str(ars)

print("Tienes $" + ars + "pesos")
