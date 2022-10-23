

def anagram(s):
    
    contador = 0
    resultado = 0
    
    if len(s) % 2 == 0:
        mitad = len(s) // 2
        str1 = s[:mitad]
        str2 = s[mitad:len(s)]
        
        for i in range(len(str1)):
            for j in range(len(str2)):
                if str1[i] == str2[j]:
                    contador += 1
                    str2 = str2.replace(str2[j],"")
                    break
    
        resultado = len(str1) - contador
        return resultado
    else:
        return -1

print(anagram("aaabbb"))
print(anagram("ab"))
print(anagram("abc"))    
print(anagram("mnop"))
print(anagram("xyyx"))
print(anagram("xaxbbbxx"))
