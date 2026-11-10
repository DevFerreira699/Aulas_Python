# Criando um dicionario0
#STAR WARS - EPISODIO IV - Uma nova esperança, George Lucas, 1977

dicionario = {
    "nome": "STAR WARS - EPISODIO IV - Uma nova esperança",
    "diretor": "George Lucas",
    "ano": 1977,
    "bilheteria": 7750000.00
}

#Exibição do dicionario completo
print(dicionario)


#Exibição do valor de uma chave
print(dicionario["nome"])


#Inserção de uma nova chave e valor (genero)
dicionario["genero"] = "Space Opera"
print(dicionario)


#Metodo Keys 
print(dicionario.keys()) #Mostra as chaves
for i in dicionario.keys():
    print(i)


#metodo values
print(dicionario.values()) #Mostra os valores das chaves
for i in dicionario.values():
    print(i)
    
    
#Metado Items
print(dicionario.items())
for chave, valor in dicionario.items():
    print(f"o nome é: {chave} --- {valor}")
    

#Metodo get
print(dicionario.get("pessoa")) # retorna none, pois o valor não existe
print(dicionario.get("diretor"))

#Metodo setdefault
dicionario.setdefault("publico", 1000)
print(dicionario)
dicionario.setdefault("publico", 2000) #Não muda uma inserção já feita
print(dicionario)