#função enumarate
lista = ["abacate","bola","cachorro"]

#metodo simples
for i in range(len(lista)):
	print(i, lista[i])


for i, nome in enumerate(lista):
	print(i, nome)