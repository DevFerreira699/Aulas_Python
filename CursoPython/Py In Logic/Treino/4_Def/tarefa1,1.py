"""
Atividade — Cadastro de funcionários e reajuste salarial

Objetivo: criar duas funções que trabalhem em conjunto, utilizando um dicionário para armazenar os dados.

1. Função cadastrar_funcionarios()

A função deve:
- Solicitar o nome do funcionário.
- Solicitar a idade.
- Solicitar o salário.
- Armazenar os três dados em um dicionário.
- Retornar o dicionário utilizando return.

2. Função calcular_aumento(dados)

A função deve:
- Receber o dicionário retornado pela primeira função.
- Acessar o salário pela chave "Salario".
- Calcular um aumento de 10%.
- Somar o aumento ao salário atual.
- Atualizar o salário dentro do próprio dicionário.
- Retornar o dicionário atualizado.

3. Execução do programa

Fora das funções, você deverá:
- Chamar cadastrar_funcionarios() e armazenar o retorno em uma variável.
- Passar essa variável como argumento para calcular_aumento().
- Exibir os dados do funcionário após o reajuste.
"""

def cadastrar_funcionarios():
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    salario = float(input("Salario: "))

    dados = {
        "Nome": nome,
        "Idade": idade,
        "Salario": salario
    }

    return dados

def calcular_aumento(dados):

    salarioAtual = dados["Salario"]
    aumento = salarioAtual * 0.10
    salarioNovo = salarioAtual + aumento

    dados["Salario"] = salarioNovo

    return dados

funcionario = cadastrar_funcionarios()

calcular_aumento(funcionario)

print(funcionario)
