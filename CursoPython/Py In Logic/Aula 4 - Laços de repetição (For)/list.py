#LAÇOS DE REPETIÇÃO

#Listas de nomes

# O laço for percorre cada elemento da lista 'nomes' e imprime cada nome individualmente.

# ele percorre qualquer tipo de dado. como: number, boolean, listas, tuplas, dicionários, conjuntos e strings. Com o for, podemos executar um bloco de código várias vezes, iterando sobre cada elemento da sequência.

#idades = [12, 15, 18, 21, 24]
#for idade in idades:
    #print(idade)
    
#Exiba apenas os maiores de idade (18 anos ou mais) da lista de idades.
idades = [20, 12, 23, 15]
for idade in idades:
    if idade >= 18:
        print(f"{idade} é maior de idade")
    else:
        print(f"{idade} é menor de idade")