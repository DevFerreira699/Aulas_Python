# Problema - Gastos totais com pagamentos de salario
# Dado uma lista de salários, calcule o total pago a todos os funcionarios

'''
Metodo 5Q's

1 - Quais são os dados de entrada?
-- Salarios 

2 - O que devo fazer com estes dado
-- Calcular todos os valores 
-- Somar todos os salarios

3 - Quais as restrições deste problema?
-- Pelo menos 2 salarios

4 - Qual é o resultado esperado?
-- Exibir a soma dos valores

5 - Qual a sequencia de passos a ser feita para chegar ao resultado esperado? (Pseudocodigo)

Receber a lista de salário
somar todos os itens da lista
exibir a soma total dos gastos com salãrio
 

''' 

salarios = [2000, 5000, 7000, 3780]
total = 0
for salario in salarios:
    # 2000 -> 2000 + 5000 -> 7000 + 7000 -> 14000 + 3780 -> 17780
    total = total + salario
    
print(total)
    