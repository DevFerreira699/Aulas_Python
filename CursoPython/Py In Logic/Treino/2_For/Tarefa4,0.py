# Exercício de Python — Controle de vendas

'''
Vamos fazer um exercício parecido com o dos alunos, usando for, if/elif/else, contadores e acumuladores. 
Sem while e sem tuplas por enquanto.
_______________________________________________________________________________
Enunciado 

Você deve criar um programa que registre as vendas de 5 vendedores.

Para cada vendedor, solicite:

- Nome;
- Valor total vendido no mês (R$).

O programa deve classificar cada vendedor conforme as regras:

Valor vendido	                          Classificação
R$ 5.000 ou mais	                      Meta atingida
R$ 3.000 até menos de R$ 5.000	          Quase atingiu a meta
Menos de R$ 3.000	                      Meta não atingida
_______________________________________________________________________________
O programa precisa apresentar no final

1. Quantos vendedores atingiram a meta.
2. Quantos quase atingiram a meta.
3. Quantos não atingiram a meta.
4. O total vendido pelos cinco vendedores.
5. A média de vendas por vendedor.
'''


metaSim = 0
metaQuase = 0
metaNao = 0
total = 0

for vendedor in range(3):
    nome = input("Qual seu nome: ")
    valor = float(input("Vendas mensal: "))
    
    total += valor
    
    if valor >= 5000:
        print(f"O vendedor {nome} atingiu a meta: {valor:.2f} este mes")
        metaSim +=1
        
    elif valor >= 3000:
        print(f"O vendedor {nome} quase atingiu a meta: {valor:.2f} este mes")
        metaQuase +=1
        
    else:
        print(f"O vendedor {nome} não conseguiu atingir a meta necessaria")
        metaNao +=1
        
media = total / 3

print("\n--- RESUMO FINAL ---")
print(f"Atingiram a meta: {metaSim}")
print(f"Quase atingiram a meta: {metaQuase}")
print(f"Não atingiram a meta: {metaNao}")
print(f"Total vendido: {total:.2f}")
print(f"Media de vendas: {media:.2f}")