#Strings

#Concatenação de strings
a = "mateus"
b = "lucas"

concatenar = a +" " + b + "\n"
print(concatenar)

#tamanho da string
tamanho = len(concatenar)
print(tamanho)

#navegar por indices
print(a[3])
#imprimir partes especificas da string
print(concatenar[0:6])

#métodos para deixar tudo minusculo e maiusculo, respectivamente
print(concatenar.lower())
print(concatenar.upper())
#remove espaços em string
print(concatenar.strip())
#remove caracteres especificos da string
minha_string = "O rato roeu a roupa do rei de roma"
minha_string = minha_string.split("r")
print(minha_string)


