import string

s = "We promptly judged antique ivory buckles for the next prize"
s_lower = s.lower() # Convertimos todo en minusculas


s_no_spaces = s_lower.replace(" ", "") # Eliminamos espacios de la string


char_list = list(s_no_spaces) # Convertimos la string en lista de caracteres


# Generamos alfabeto
alfabeto = string.ascii_lowercase
abc_list = list(alfabeto)


bandera = True

for letter in abc_list:
    if not letter in char_list:
        bandera = False

if bandera == True:
    print("pangram")
else:
    print("not pangram")        