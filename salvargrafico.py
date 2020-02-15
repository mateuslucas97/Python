#salvar grafico
#inserindo pontos no grafico de linha 
import matplotlib.pyplot as plt 

x = [1,3,5,7,9]
y = [2,3,7,1,0]
z = [200,25,400,330,100] #tamanho dos pontos no grafico
titulo = "Scatterplot: grafico de dispersao"
eixox = "Eixo X"
eixoy = "Eixo Y"

#legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

#usando valores em hexadecimal para as cores
plt.plot(x,y, color = "#000000", linestyle = "--") #verde
plt.scatter(x,y, label = "Meus pontos", color = "k", marker = ".", s = z)
plt.legend()
#plt.show()
plt.savefig("Figura1.png", dpi = 300) #salva o grafico num arquivo separado dependendo do formato no diretorio corrente
#dpi eh o tamanho da imagem