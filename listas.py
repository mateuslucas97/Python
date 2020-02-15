#Listas (aka. vetores)
#lista de strings
minha_lista = ["kiwi","papaya","manga","abacate"]
print(minha_lista)
#lista de numeros
minha_lista2 = [1,2,3,4,5]
print(minha_lista2)
#lista mista
minha_lista3 = ["abacate",2,9,63,True]
print(minha_lista3)
#imprime a primeira posição da lista
print(minha_lista[1])
#usando for para imprimir a primeira lista
for item in minha_lista:
	print(item)

#verifica se um item está na lista
minha_lista.append("limão")
if 3 in minha_lista2:
	print("3 está na lista")

print(minha_lista)
#deleta itens da lista
del minha_lista[2:]
print(minha_lista)

#criando uma nova lista
minha_lista4 = []
minha_lista4.append(57)
print(minha_lista4)