#função reduce
from functools import reduce
def soma(x, y):
	return x + y

lista = [1,5,3,10,20]

resultado = reduce(soma, lista)

print (resultado)