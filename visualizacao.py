#visualizacao de um grafico simples
import matplotlib.pyplot as plt

x = [1,2,5]
y = [2,3,7]
#titulo
plt.title("Grafico simples em python")
#eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.plot(x, y)
plt.show()
