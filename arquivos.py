#arquivos
#abre um arquivo existente
arquivo = open("arquivo.txt")
#lê o arquivo em questao
linhas = arquivo.readlines()
#mostra  o arquivo em questao
print(linhas)

texto_completo = arquivo.read()
print(texto_completo)
#=======================#
w = open("Arquivo.txt","a")
w.write("Esse é o arquivo 2 que eu criei")
w.close()