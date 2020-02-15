#estudo de caso DNA e RNA
#Neste estudo de caso, queremos avaliar se estruturas com 
#funcoes parecidas (estamos usando sequencias de RNA 
#ribossomal) de organismos diferentes tem diferencas. Para 
#isso vamos avaliar a quantidade de pares de nucleotideos.

entrada = open("bacteria.fasta").read()
saida = open("16s_bacteria.html","w")

cont = {}

#faz a combinacao de todos os nucleotideos
for i in ['A','T','C','G']:
	for j in ['A','T','C','G']:
		cont[i+j] = 0

entrada = entrada.replace("\n","")


for k in range(len(entrada)-1):
	cont[entrada[k] + entrada[k+1]] += 1
		

#HTML

i = 1
for k in cont:
	transparencia = float(cont[k])/max(cont.values())
	saida.write("<div style='width:100px; border:1px solid #111; color:#fff; height:100px;float:left; background-color:rgba(0,0,0, "+str(transparencia)+"')>"+k+"</div> ")
	
	if i%4 ==0:
		saida.write("<div style='clear:both'></div>")
	i+=1	
saida.close()