#Tarefa 1 — Sistema de aprovação de aluno

'''
Objetivo: criar um programa que receba duas notas de um aluno, calcule a média e informe se ele foi aprovado, ficou de recuperação ou foi reprovado.

Regras do programa:

- Média igual ou superior a 7: Aprovado.
- Média igual ou superior a 5, mas inferior a 7: Recuperação.
- Média inferior a 5: Reprovado.
'''


nome = input("digite seu nome: ")

nota1 = float(input("Qual sua nota na P1: "))
nota2 = float(input("Qual sua nota na P2: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f"O aluano {nome} foi aprovado com a média {media}")
elif media >= 5 and media < 7:
    print(f"O aluno {nome} está de Recuperação com a média {media}")
else:
    print(f"O aluno {nome} está Reprovado com a média {media}") 
