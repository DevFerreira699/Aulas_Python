'''
Nova atividade — Controle de estoque e vendas

Nível intermediário inicial

1. Cadastro de produtos

Cadastre 3 produtos manualmente em uma lista utilizando .append().

Cada produto deverá ter:

- Nome;
- Preço;
- Quantidade em estoque.

2. Registro de vendas

Utilize for para percorrer os produtos cadastrados.

Para cada produto:

1. Solicite a quantidade vendida.
2. Verifique se existe estoque suficiente.
3. Se houver estoque, desconte a quantidade.
4. Se não houver, informe que a venda não pode ser realizada.
5. Calcule o valor da venda.

3. Relatório final

Ao terminar as vendas, apresente:

- Nome dos produtos;
- Quantidade restante;
- Preço unitário;
- Valor total em estoque;
- Faturamento total;
- Quantidade de produtos esgotados;
- Quantidade de produtos com estoque baixo.

4. Regras

Situação	        Condição
Esgotado	        Quantidade = 0
Estoque baixo	    Quantidade entre 1 e 5
Adequado	        Quantidade acima de 5
'''


produtos = []
faturamento = 0
valor_total_estoque = 0
esgotados = 0
estoque_baixo = 0
estoque_adequado = 0

for i in range(3):
    print("-----Tabela de produtos-----")
    nome = input("Nome do Produto: ")
    preco = float(input("Preço do Produto: "))
    quantidade = int(input("Unidades do produto: "))
    vendido = int(input("Quantidade vendida: "))

    produtos.append({
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade,
        "vendido": vendido
    })

for produto in produtos:
    if produto["vendido"] >= 0 and produto["vendido"] <= produto["quantidade"]:
        produto["quantidade"] -= produto["vendido"]

        valorVenda = produto["vendido"] * produto["preco"]
        faturamento += valorVenda
        print("Venda realizada!")
    else:
        print("Estoque insuficiente!")

print("\n===== DETALHAMENTO DOS PRODUTOS =====")

for produto in produtos:
    print(produto["nome"])
    print(produto["quantidade"])

    valor_produto = produto["preco"] * produto["quantidade"]
    valor_total_estoque += valor_produto

    if produto["quantidade"] == 0:
        esgotados += 1

    elif produto["quantidade"] <= 5:
        estoque_baixo += 1

    else:
        estoque_adequado += 1

print("\n===== RELATÓRIO DE ESTOQUE =====")
print(f"Produtos esgotados: {esgotados}")
print(f"Estoque baixo: {estoque_baixo}")
print(f"Estoque adequado: {estoque_adequado}")
print(f"Faturamento total: R$ {faturamento:.2f}")
print(f"Valor total em estoque: R$ {valor_total_estoque:.2f}")
