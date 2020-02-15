#dicionario
meu_dicionario = {"A":"Ameixa","B":"Bola","C":"Cachorro"}
print(meu_dicionario)
#imprimeindo uma chave com um valor
for chave in meu_dicionario:
	print(chave+"-"+meu_dicionario[chave])

#imprimido só os valores
for i in meu_dicionario.values():
	print(i)
#imprimindo só as chaves
for i in meu_dicionario.keys():
	print(i)