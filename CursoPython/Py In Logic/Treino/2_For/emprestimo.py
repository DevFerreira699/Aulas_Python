
aprovados = 0
analise = 0
recusados = 0
totalAprovado = 0
totalSolicitado = 0

for i in range(4):
    print(f"\n--- Cliente {i + 1} de 4 ---")

    nome = input("Informe o seu nome: ")
    salarioMensal = float(input("Informe seu rendimento mensal: "))
    emprestimo = float(input("Informe o valor do empréstimo solicitado: "))

    totalSolicitado += emprestimo

    if salarioMensal >= 3000 and emprestimo <= salarioMensal * 10:
        print(f"Olá, {nome}! Seu empréstimo de R$ {emprestimo:.2f} foi aprovado.")
        aprovados += 1
        totalAprovado += emprestimo

    elif salarioMensal >= 2000 and emprestimo <= salarioMensal * 5:
        print(f"Olá, {nome}! Seu empréstimo de R$ {emprestimo:.2f} está em análise.")
        analise += 1

    else:
        print(f"Olá, {nome}! Seu empréstimo não foi aprovado.")
        recusados += 1

media = totalSolicitado / 4

print("\n===== RESUMO FINAL =====")
print(f"Total de aprovados: {aprovados}")
print(f"Total em análise: {analise}")
print(f"Total de recusados: {recusados}")
print(f"Valor total dos empréstimos aprovados: R$ {totalAprovado:.2f}")
print(f"Valor total solicitado: R$ {totalSolicitado:.2f}")
print(f"Média dos valores aprovados: R$ {media:.2f}")
