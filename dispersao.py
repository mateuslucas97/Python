#grafico de dispersao

import matplotlib.pyplot as plt
x = [1,3,5,7,9]
y = [2,3,7,1,0]

titulo = "scatterplot: grafico de dispersao"
eixox = "Eixo X"
eixoy = "Eixo Y"

plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.scatter(x, y, label="Meus pontos", color="r",marker = ".", s = 200)
plt.plot(x, y, color ="k", linestyle=":")
plt.legend()
plt.show()