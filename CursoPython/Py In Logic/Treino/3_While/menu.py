# ==================================================
# 1. INICIALIZAÇÃO DAS VARIÁVEIS
# ==================================================

clientes = []
aprovado = 0
analise = 0
reprovado = 0
totalAprovados = 0
totalSolicitado = 0

# ==================================================
# 2. CADASTRO DOS CLIENTES
# ==================================================

for i in range(2):
    print("\n=== Solicitação de Empréstimo: Ferreira Bank's ===")
    nome = input("Nome do Cliente: ")
    salarioMensal = float(input("Salário mensal: "))
    emprestimo = float(input("Empréstimo pretendido: "))

    # ==================================================
    # 3. ANÁLISE DE CRÉDITO
    # ==================================================

    if salarioMensal >= 3000:

        if emprestimo <= salarioMensal * 10:
            print(f"Olá senhor(a) {nome}, seu empréstimo está aprovado")
            status = "Aprovado"
            aprovado += 1

        else:
            print(f"Olá senhor(a) {nome}, seu empréstimo está em análise!")
            status = "Em análise"
            analise += 1

    elif salarioMensal >= 2000:

        if emprestimo <= salarioMensal * 5:
            print(f"Olá senhor(a) {nome}, seu empréstimo está aprovado")
            status = "Aprovado"
            aprovado += 1

        else:
            print(f"Olá senhor(a) {nome}, seu empréstimo está em análise!")
            status = "Em análise"
            analise += 1

    else:
        print(f"Olá senhor(a) {nome}, não foi possível habilitar um empréstimo")
        status = "Reprovado"
        reprovado += 1

    # ==================================================
    # 4. ARMAZENAMENTO DOS CLIENTES
    # ==================================================

    clientes.append({
        "Cliente": nome,
        "Salario": salarioMensal,
        "Emprestimo": emprestimo,
        "Status": status,
    })

# ==================================================
# 5. CÁLCULO DOS VALORES FINANCEIROS
# ==================================================

for cliente in clientes:
    totalSolicitado += cliente["Emprestimo"]

    if cliente["Status"] == "Aprovado":
        totalAprovados += cliente["Emprestimo"]

# ==================================================
# 6. MENU PRINCIPAL
# ==================================================

opcao = 0

while opcao != 6:

    print("\n================================")
    print("         FERREIRA BANK'S")
    print("================================")
    print("1 - Consultar todos os clientes")
    print("2 - Consultar estatísticas")
    print("3 - Total de empréstimos aprovados")
    print("4 - Total de empréstimos solicitados")
    print("5 - Pesquisar cliente pelo nome")
    print("6 - Encerrar sistema")
    print("================================")

    opcao = int(input("Escolha uma opção: "))

    # ==================================================
    # 7. OPÇÃO 1 - CONSULTAR TODOS OS CLIENTES
    # ==================================================

    if opcao == 1:
        
        for cliente in clientes:

            print("\n=== Dados do Cliente ===")
            print(f"Cliente: {cliente['Cliente']}")
            print(f"Salário: R$ {cliente['Salario']:.2f}")
            print(f"Empréstimo: R$ {cliente['Emprestimo']:.2f}")
            print(f"Status: {cliente['Status']}")

    # ==================================================
    # 8. OPÇÃO 2 - ESTATÍSTICAS
    # ==================================================

    elif opcao == 2:

        print("\n=== Estatísticas de Crédito ===")
        print(f"Clientes cadastrados: {len(clientes)}")
        print(f"Aprovados: {aprovado}")
        print(f"Em análise: {analise}")
        print(f"Reprovados: {reprovado}")

    # ==================================================
    # 9. OPÇÃO 3 - TOTAL APROVADO
    # ==================================================

    elif opcao == 3:

        print("\n=== Empréstimos Aprovados ===")
        print(f"Total aprovado: R$ {totalAprovados:.2f}")

    # ==================================================
    # 10. OPÇÃO 4 - TOTAL SOLICITADO
    # ==================================================

    elif opcao == 4:

        print("\n=== Empréstimos Solicitados ===")
        print(f"Total solicitado: R$ {totalSolicitado:.2f}")

    # ==================================================
    # 11. OPÇÃO 5 - PESQUISAR CLIENTE
    # ==================================================

    elif opcao == 5:

        consulta = input("\nQual cliente deseja consultar? ")
        encontrado = False

        for cliente in clientes:

            if consulta.lower() == cliente["Cliente"].lower():

                print("\n=== Dados do Cliente ===")
                print(f"Cliente: {cliente['Cliente']}")
                print(f"Salário: R$ {cliente['Salario']:.2f}")
                print(f"Empréstimo: R$ {cliente['Emprestimo']:.2f}")
                print(f"Status: {cliente['Status']}")

                encontrado = True

        if encontrado == False:
            print("Cliente não cadastrado!")

    # ==================================================
    # 12. OPÇÃO 6 - ENCERRAR
    # ==================================================

    elif opcao == 6:
        print("\nSistema Ferreira Bank's encerrado!")

    # ==================================================
    # 13. OPÇÃO INVÁLIDA
    # ==================================================

    else:
        print("\nOpção inválida! Tente novamente.")