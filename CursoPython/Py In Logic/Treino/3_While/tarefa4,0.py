'''
Nova tarefa Python — Sistema de empréstimos bancários

Desenvolva um programa que simule a análise de empréstimos de um banco. 
O sistema deverá cadastrar clientes, verificar se eles atendem aos critérios de aprovação
e apresentar um relatório com os resultados.
_________________________________________________________________________________________________
1. Cadastro de clientes — for

O programa deverá cadastrar 5 clientes, solicitando:

- Nome do cliente.
- Salário mensal.
- Valor do empréstimo solicitado.
_________________________________________________________________________________________________
2. Análise de crédito — condicionais

O banco possui os seguintes critérios:

Salário mensal	                Limite do empréstimo
A partir de R$ 3.000	        Até 10 vezes o salário
A partir de R$ 2.000	        Até 5 vezes o salário
Abaixo de R$ 2.000	            Não elegível

Classifique cada cliente:

- Aprovado: atende aos critérios de salário e valor solicitado.
- Em análise: atende ao salário mínimo, mas ultrapassa o limite permitido.
- Não elegível: recebe menos de R$ 2.000.
_________________________________________________________________________________________________
3. Menu de consulta — while

Após cadastrar os 5 clientes, o programa deverá apresentar um menu 
que continue funcionando até o usuário escolher encerrar.

1. Consultar todos os clientes e seus resultados.
2. Consultar a quantidade de empréstimos aprovados.
3. Consultar o valor total dos empréstimos aprovados.
4. Consultar um cliente pelo nome.
5. Encerrar o programa.

4. Relatório final

Ao encerrar, apresente:

- Quantidade total de clientes cadastrados.
- Quantidade de empréstimos aprovados, em análise e não elegíveis.
- Valor total dos empréstimos aprovados.
- Média salarial dos clientes cadastrados.
_________________________________________________________________________________________________
Regras do exercício

- Utilize variáveis, condicionais, for e while.
- Utilize listas para armazenar os dados dos clientes.
- Utilize if, elif e else, incluindo pelo menos uma condicional aninhada.
- Não utilize funções (def), classes ou bibliotecas externas.
- Não permita salários ou valores de empréstimo negativos ou iguais a zero.
_________________________________________________________________________________________________
Desafio extra: permita que o usuário informe um valor de empréstimo
e o programa calcule qual seria o salário mínimo necessário para aprová-lo.
'''


# ==================================================
# 1. INICIALIZAÇÃO DAS VARIÁVEIS
# ==================================================

# Lista que armazenará os dados dos clientes
clientes = []

# Contadores para acompanhar a situação dos empréstimos
aprovado = 0
analise = 0
reprovado = 0

# Acumuladores para somar os valores dos empréstimos
totalAprovados = 0
totalSolicitado = 0

# ==================================================
# 2. CADASTRO DOS CLIENTES
# ==================================================

# Executa o cadastro de 5 clientes
for i in range(2):
    print("=== Solicitação de Empréstimo: Ferreira Bank's ===")

    # Solicita os dados do cliente
    nome = input("Nome do Cliente: ")
    salarioMensal = float(input("Salário mensal: "))
    emprestimo = float(input("Empréstimo pretendido: "))

    # ==================================================
    # 3. ANÁLISE E CLASSIFICAÇÃO DO CRÉDITO
    # ==================================================

    # Clientes com salário igual ou superior a R$ 3.000
    if salarioMensal >= 3000:

        # Limite de empréstimo de até 10 vezes o salário
        if emprestimo <= salarioMensal * 10:
            print(f"Olá senhor(a) {nome}, seu empréstimo está aprovado")
            status = "Aprovado"
            aprovado += 1

        else:
            print(f"Olá senhor(a) {nome}, seu empréstimo está em análise!")
            status = "Em análise"
            analise += 1

    # Clientes com salário entre R$ 2.000 e R$ 2.999,99
    elif salarioMensal >= 2000:

        # Limite de empréstimo de até 5 vezes o salário
        if emprestimo <= salarioMensal * 5:
            print(f"Olá senhor(a) {nome}, seu empréstimo está aprovado")
            status = "Aprovado"
            aprovado += 1

        else:
            print(f"Olá senhor(a) {nome}, seu empréstimo está em análise!")
            status = "Em análise"
            analise += 1

    # Clientes com salário inferior a R$ 2.000
    else:
        print(f"Olá senhor(a) {nome}, não foi possível habilitar um empréstimo")
        status = "Reprovado"
        reprovado += 1

    # ==================================================
    # 4. ARMAZENAMENTO DOS DADOS
    # ==================================================

    # Adiciona os dados do cliente à lista como um dicionário
    clientes.append({
        "Cliente": nome,
        "Salario": salarioMensal,
        "Emprestimo": emprestimo,
        "Status": status,
    })

# ==================================================
# 5. CONSULTA DE CLIENTES
# ==================================================

# Variável de controle para permitir consultas repetidas
continuar = "S"

# Mantém o processo de consulta enquanto a resposta for S
while continuar == "S":

    # Solicita o nome do cliente que será pesquisado
    consulta = input("\nQual Cliente deseja consultar? ")

    # Controla se o cliente foi encontrado na lista
    encontrado = False

    # Percorre todos os clientes cadastrados
    for cliente in clientes:

        # Compara os nomes ignorando diferenças entre maiúsculas e minúsculas
        if consulta.lower() == cliente["Cliente"].lower():

            print("\n=== Dados do Cliente ===")
            print(f"Cliente: {cliente['Cliente']}")
            print(f"Salario: {cliente['Salario']:.2f}")
            print(f"Emprestimo: {cliente['Emprestimo']:.2f}")
            print(f"Status: {cliente['Status']}")

            # Indica que o cliente foi localizado
            encontrado = True

    # Executa caso nenhum cliente corresponda à pesquisa
    if encontrado == False:
        print("Cliente não cadastrado!")

    # Pergunta se o usuário deseja realizar outra consulta
    continuar = input("\nDeseja consultar outro cliente? S/N: ").upper()

print("Consultas encerradas!")

# ==================================================
# 6. CÁLCULO DOS EMPRÉSTIMOS
# ==================================================

# Percorre os clientes para calcular os valores financeiros
for cliente in clientes:

    # Soma todos os empréstimos solicitados, independentemente do status
    totalSolicitado += cliente["Emprestimo"]

    # Verifica quais empréstimos foram aprovados
    if cliente["Status"] == "Aprovado":

        # Soma somente os valores dos empréstimos aprovados
        totalAprovados += cliente["Emprestimo"]

# ==================================================
# 7. RELATÓRIO FINAL
# ==================================================

# Exibe o resumo geral dos clientes e empréstimos
print("\n================================")
print("       RELATÓRIO DO CLIENTES")
print("================================")

# Quantidade total de clientes cadastrados
print(f"Clientes cadastrados: {len(clientes)}")

# Quantidade de empréstimos por situação
print(f"Total Aprovados: {aprovado}")
print(f"Total Em Analise: {analise}")
print(f"Total Reprovados: {reprovado}")

# Valores financeiros acumulados
print(f"Total de Empréstimos Aprovados: R$ {totalAprovados:.2f}")
print(f"Total de Empréstimos Solicitados: R$ {totalSolicitado:.2f}")
