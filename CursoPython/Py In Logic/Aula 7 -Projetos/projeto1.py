# Projeto 1 - Fatorial de um número
# Crie um programa que recebe um número e imprime o seu fatorial
'''
Metodo 5Q's

1 - Quais são os dados de entrada?
- Um numero
- 

2 - O que devo fazer com estes dado
-- Deve multiplicar os numeros antecessores ao valor obtido 
-- 

3 - Quais as restrições deste problema?
-- Tem que ser um numero inteiro
-- Ser > que 1 
-- Ser positivo

4 - Qual é o resultado esperado?
-- O total da multiplicação do fatorial
-- Exibir o resultado na tela

5 - Qual a sequencia de passos a ser feita para chegar ao resultado esperado? (Pseudocodigo)

 Receber o valor
 verificar se é um numero inteiro e positivo
 Pegar o fatorial e somar o resultado com a multiplicação do seu antecessor(fatorial até1)
 exibir na tela o resultado
 exibir o valor na tela
'''

numero = int(input("Digite o fatorial que deseja calcular: "))
if numero > 0 and type(numero) == int:
    fatoiral = 1 
    for item in range(1, numero+1):
        print(f"{fatoiral} * {item}")
        fatoiral = fatoiral * item
        print(F"{fatoiral}")
    print(f"O fatorial de {numero} é {fatoiral}")
else:
    print("Favor informar apenas numeros interios positivos")
        
        
