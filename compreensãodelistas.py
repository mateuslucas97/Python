#compreensao de listas
x = [1,2,3,4,5]
y = []
#metodo basico
for i in x:
	y.append(i**2)

print(x)
print(y)
print("Ideal")
z = [i**2 for i in x]
print(z)

a = [i for i in x if i%2==1]
print(a)