# laços de repetição
for item in range( 10):
    print(item)

#for é utilizado para percorrer uma sequência de elementos, como listas, tuplas, dicionários, conjuntos e strings. Com o for, podemos executar um bloco de código várias vezes, iterando sobre cada elemento da sequência.

#In é utilizado para verificar se um valor está presente em uma sequência. Ele retorna True se o valor estiver presente e False caso contrário.

for item in range(1, 11):  
    print(item)

#assim , o laço irá percorrer os números de 1 a 10, mas apenas os ímpares, pois o passo é de 2.

for item in range(1, 11, 2):  
    print(item)
    
    
    #LAÇOS DE REPETIÇÃO
#Listas de nomes

nomes = ['Ana', 'Bia', 'Carlos', 'Daniel', 'Eduardo']
for nome in nomes:
    print(nome)
    
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
        
        
cidades = ['São Paulo', 'Rio de Janeiro','Belo Horizonte', 'Curitiba', 'Porto Alegre']

siglas = ['SP', "RJ", 'BH', 'CU', 'PA']
for cidade, sigla in zip(cidades, siglas):
    print(cidade, sigla)

#zip é usado para mesclar duas listas já existentes (cidades e siglas)
