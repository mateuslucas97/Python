#crescimento  da populacao brasileira 1980-2016
#disponibilizado por DataSus
import matplotlib.pyplot as plt 
dados = open("populacao-brasileira.csv").readlines()

x = []
y = []

#recolhe o x e o y do grafico
for i in range(len(dados)): #percorre todo o vetor do tamanho corrente
	if i != 0: #ignora a primeira linha
		linha = dados[i].split(";") #divide as linhas por ;
		x.append(int(linha[0]))
		y.append(int(linha[1]))

plt.bar(x, y, color = "#e4e4e4") #cria as barras
plt.plot(x, y, color = "k", linestyle = "--") #cria as linhas
plt.title("Crescimento da populacao Brasileira 1980-2016")
plt.xlabel("Ano")
plt.ylabel("Populacao x 100.000.000")
#plt.show()
plt.savefig("Populacao.png", dpi = 300)