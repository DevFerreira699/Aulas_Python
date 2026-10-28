# Projeto 2 - Chute o número
'''
Escreva um programa que, ao iniciar, gere um valor aleatorio de 1 a 10 e permita que o usuario chute números até acertar o valor gerado.

o programa deve informar se o chute foi maior, menor ou igual ao valor aleatorio gerado no inicio.

Metodo 5Q's

1 - Quais são os dados de entrada?
-- Receber um numero
--

2 - O que devo fazer com estes dado
-- comparar se o valor informado é > ou < ou = ao valor aleatorio
-- 

3 - Quais as restrições deste problema?
-- Numero de 1 a 10
-- O usuario pode chutar quantas vezes for necessario até acertar

4 - Qual é o resultado esperado?
-- Exibir se o valor chutado é > ou < que o aleatorio
-- Se = mostrar que acertou

5 - Qual a sequencia de passos a ser feita para chegar ao resultado esperado? (Pseudocodigo)

gerar um valor de A a B
permitir que o usuario chute um numero
informar se esta acima, abaixo ou igual ao valor gerado
Se errar, permitir novas tentativas até acertar
'''

import random

Aleatorio = random.randint(1, 10)
acertou = False

while acertou == False:
    chute = int(input("Chute um número: "))
    if chute > Aleatorio:
        print("Valor acima")
    elif chute < Aleatorio:
        print("Valor abaixo")
    else:
        print("Voce acertou!")
        acertou = True