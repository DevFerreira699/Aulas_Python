'''
Atividade 1 — Sistema de controle de estoque com while

Cenário

Você foi contratado para desenvolver um sistema de controle de estoque de uma empresa. 
O programa deverá cadastrar 5 produtos, analisar suas quantidades e calcular o valor total armazenado.

Requisitos da atividade

1. Solicitar o nome de cada produto.
2. Solicitar a quantidade disponível em estoque.
3. Solicitar o preço unitário de cada produto.
4. Calcular o valor total de cada produto: quantidade X preço.
5. Classificar a situação do estoque:
   - Quantidade igual a zero: Esgotado.
   - Quantidade entre 1 e 10: Estoque baixo.
   - Quantidade acima de 10: Estoque adequado.
   
6. Contabilizar quantos produtos estão em cada categoria.
7. Calcular o valor total de todos os produtos cadastrados.
8. Exibir um relatório final com todos os resultados.
'''
totalGeral = 0
esgotados = 0
estoqueBaixo = 0
estoqueAdequado = 0
produtos = []

for contador in range(3):
    print("------ Cadastro de produto ------")

    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    
    while quantidade < 0:
        print("Erro! A quantidade não pode ser negativa.")
        quantidade = int(input("Digite novamente a quantidade: "))

    preco = float(input("Preço unitário: R$ "))
    while preco < 0:
        print("Erro! O preço não pode ser negativo.")
        preco = float(input("Digite novamente o preço: R$ "))

    total = quantidade * preco
    totalGeral += total

    if quantidade == 0:
        situacao = "Esgotado"
        esgotados += 1
    elif quantidade <= 10:
        situacao = "Estoque baixo"
        estoqueBaixo += 1
    else:
        situacao = "Estoque adequado"
        estoqueAdequado += 1

    produtos.append({
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco,
        "total": total,
        "situacao": situacao
    })

print("\n====== RELATÓRIO DE ESTOQUE ======")

for produto in produtos:
    print(f"\nProduto: {produto['nome']}")
    print(f"Quantidade: {produto['quantidade']}")
    print(f"Preço unitário: R$ {produto['preco']:.2f}")
    print(f"Valor em estoque: R$ {produto['total']:.2f}")
    print(f"Situação: {produto['situacao']}")

print("\n====== RESUMO FINAL ======")
print(f"Produtos esgotados: {esgotados}")
print(f"Produtos com estoque baixo: {estoqueBaixo}")
print(f"Produtos com estoque adequado: {estoqueAdequado}")
print(f"Valor total do estoque: R$ {totalGeral:.2f}")