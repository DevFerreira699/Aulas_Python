"""
Exercício 01 — Cadastro de funcionários
Iniciante

Você deverá criar uma função chamada cadastrar_funcionario.

Requisitos:
1. A função deve receber três parâmetros:
   - Nome do funcionário.
   - Idade.
   - Salário.

2. A função deverá criar um dicionário contendo essas três informações.

3. A função deverá utilizar return para devolver esse dicionário.

4. Fora da função, você deverá chamar a função e armazenar o resultado em uma variável.

5. Apresente o dicionário na tela.
   
   O que quero avaliar:
- Se você entendeu a declaração de funções.
- Se sabe diferenciar parâmetros e argumentos.
- Se consegue utilizar return.
- Se consegue armazenar o retorno em uma variável.
"""

def cadastrar_funcionarios(nome_Funcinario, idade_funcionario, salario_funcionario):
    funcionario = {
        "Nome":nome_Funcinario,
        "Idade": idade_funcionario,
        "Salario": salario_funcionario
    }

    return funcionario

cadastrofuncionario = cadastrar_funcionarios("Ferreira","23","3600")

print(cadastrofuncionario) 