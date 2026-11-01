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
_________________________________________________________________________________________________
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

# LISTA
clientes =[]
# Acumuladores
aprovados = 0
analise = 0
reprovados = 0
#contadores
totalAprovado = 0
totalSolicitado = 0


for i in range(3):
    print("\n=== Solicitação de Empréstimo: Ferreira Bank's ===")
    nome = input("Cliente: ")
    salarioMes = float(input("Informe seu salario: "))
    emprestimo = float(input("Pretensão de emprestimo: "))
    
    if salarioMes >= 3000:
        
        if emprestimo <= salarioMes * 10:
            print(f"Olá {nome}, seu emprestimo foi aprovado!")
            status = "Aprovado"
            aprovados += 1
            
        
        else:
            print(f"Olá {nome}, seu emprestimo está em analise!")
            status = "Em análise"
            analise += 1
           
    elif salarioMes >= 2000: 
        
        if emprestimo <= salarioMes * 5:
            print(f"Olá {nome}, seu emprestimo foi aprovado!")
            status = "Aprovado"
            aprovados += 1
            
        else:
            print(f"Olá {nome}, seu emprestimo está em analise!")
            status = "Em análise"
            analise += 1
    
    else:
        print(f"Olá {nome}, seu emprestimo foi reprovado")
        status = "Reprovado"
        reprovados += 1
        
    clientes.append({
        "Cliente": nome,
        "Salario": salarioMes,
        "Emprestimo": emprestimo,
        "Status": status,
    })
          
for cliente in clientes:
    totalSolicitado += cliente['Emprestimo']
    
    if cliente['Status'] == "Aprovado":
        totalAprovado += cliente['Emprestimo']
           
opcao = 0

while opcao != 6:
    
    print("\n================================")
    print("         FERREIRA BANK'S")
    print("================================")
    print("1 - Consultar todos os clientes")
    print("2 - Consultar estatísticas")
    print("3 - Total de empréstimos aprovados e solicitados")
    print("4 - Pesquisar cliente pelo nome")
    print("5 - Encerrar sistema")
    print("================================")
    
    opcao = int(input("Digite uma das opções: "))
    
    if opcao == 1:
        for cliente in clientes:
            print("\n=== Dados do Cliente ===")
            print(f"Cliente: {cliente['Cliente']}")
            print(f"Salário: {cliente['Salario']}")
            print(f"Emprestimo: {cliente['Emprestimo']}")
            print(f"Status: {cliente['Status']}")
            
    elif opcao == 2:
        print("\n=== Estatísticas de Crédito ===")
        print(f"Clientes cadastrados: {len(clientes)}")
        print(f"Foram aprovados: {aprovados}")
        print(f"Estão em analise: {analise}")
        print(f"Foram reprovados: {reprovados}")
        
    elif opcao == 3:
        print("\n=== Estatísticas de Crédito ===")
        print(f"Valor total solicitado: {totalSolicitado}")
        print(f"Valor total aprovado: {totalAprovado}")
        
    elif opcao == 4:
        
        consulta = input("\nQual cliente deseja consultar? ")
        encontrado = False
        
        for cliente in clientes:
            
            if consulta.lower() == cliente['Cliente'].lower():
                
                print("==CLIENTE==")
                print(f"Cliente: {cliente['Cliente']}")
                print(f"Salario: {cliente['Salario']}")
                print(f"Emprestimo: {cliente['Emprestimo']}")
                print(f"Status: {cliente['Status']}")
                
                encontrado = True
                
        if encontrado == False:
            print("Cliente não cadastrado!") 
    
    elif opcao == 5:
        print("\nSistema Ferreira Bank's encerrado!")       
        
    else:
        print("\nOpção inválida! Tente novamente.") 

