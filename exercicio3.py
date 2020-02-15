import math
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = ((b ** 2) - 4 * a * c)

r1 = (math.sqrt(delta) - b)/2
print(r1)

r2 = (math.sqrt(delta) + b)/2
print(r2)