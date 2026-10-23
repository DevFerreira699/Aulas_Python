# 🐍 Tarefa: Sistema de aprovação de empréstimo
# Você deverá criar um programa que analisa se uma pessoa pode receber um empréstimo.
'''
Regras do programa:

1. Solicite o nome da pessoa.
2. Solicite o salário mensal.
3. Solicite o valor do empréstimo desejado.
4. Solicite a idade da pessoa.
5. Analise as condições abaixo.

Condição	
1 -Idade menor que 18 anos
2 -Salário menor que R$ 1.500
3 -Empréstimo maior que 10 vezes o salário
4 -Atende a todos os requisitos

Resultado
1 -Empréstimo negado
2 -Empréstimo negado
3 -Empréstimo negado
4 -Empréstimo pré-aprovado
'''
nome = (input("Qual é o seu nome: "))
idade = int(input("Qual sua idade: "))

if idade < 18:
    print("Idade não permitida")

else:
    salario = float(input("Qual é o seu salário: "))

    if salario < 1500:
        print("Sem emprestimos disponiveis")
    else:
        emprestimo = float(input("Quanto deseja de emprestimo: "))  
       
        if emprestimo > salario * 10:
            print("Emprestimo negado")
        else:
            print(f"Emprestimo pré-aprovado em nome de {nome}")
