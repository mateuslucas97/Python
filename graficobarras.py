#visualizacao de um grafico de barras
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,3,7,1,0]


titulo = "grafico de barras"
eixox = "eixo x"
eixoy = "eixo y"
#titulo
plt.title(titulo)
#legendas
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x, y)
plt.show()
