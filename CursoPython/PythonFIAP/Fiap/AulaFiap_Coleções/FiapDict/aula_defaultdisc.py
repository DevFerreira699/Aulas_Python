# Importanto0
from collections import defaultdict

#Criação de um default dict com uma lista como valor padrão
print("==FUNÇÃO DEFAULT DICT==")
dicionario_lista = defaultdict(list)
dicionario_lista["PRODUTO"] = "Mouse"
dicionario_lista["MARCA"] = "Razer"
print(dicionario_lista)

print(dicionario_lista["PREÇO"])
print(dicionario_lista)

#Criação de função que retorna a frase: "INEXISTENTE"
print("==FUNÇÃO DEF==")
def funcaoX():
    return "INEXISTENTE"
dicionario_x = defaultdict(funcaoX)
dicionario_x["PRODUTO"] = "Mouse"
dicionario_x["MARCA"] = "Razer"

print(dicionario_x)
print(dicionario_x["PRECO"])
print(dicionario_x)

#Criação de um dicionario com uma função lambda
print("==FUNÇÃO LAMBDA==")
dicionario_lambda = defaultdict(lambda: "Não disponivel")
dicionario_lambda["PRODUTO"] = "Mouse"
dicionario_lambda["MARCA"] = "Razer"

print(dicionario_lambda)
print(dicionario_lambda["PRECO"])
print(dicionario_lambda)