# Exercício de Python — Sistema de empréstimos bancários

# Vamos mudar de assunto, mas continuar praticando for, if/elif/else, contadores e acumuladores

'''
Enunciado

Você trabalha em um banco e precisa analisar o pedido de empréstimo de 4 clientes.

Para cada cliente, solicite:

- Nome;
- Salário mensal;
- Valor do empréstimo solicitado.
________________________________________________________________________________________________________
Regras de aprovação

Condição	                                                                    Resultado
Salário igual ou superior a R$ 3.000 e empréstimo até 10 vezes o salário	    Empréstimo aprovado
Salário igual ou superior a R$ 2.000 e empréstimo até 5 vezes o salário	        Empréstimo em análise
Qualquer outra situação	                                                        Empréstimo recusado

Se o cliente atender à primeira regra, classifique-o como aprovado. 
Caso contrário, verifique a segunda regra.
__________________________________________________________________________________________________________
O que seu programa precisa apresentar no final

1. Quantos empréstimos foram aprovados.
2. Quantos ficaram em análise.
3. Quantos foram recusados.
4. A soma dos valores de empréstimos aprovados.
5. A média dos valores solicitados pelos quatro clientes.
___________________________________________________________________________________________________________
'''


aprovados = 0
analise = 0
recusados = 0
totalAprovado = 0
totalSolicitado = 0 


for i in range(4):
    nome = input("Informe o seu nome: ")
    salarioMensal = float(input("Informe seu rendimento mensal: "))
    emprestimo = float(input("Informe sua pretensão de emprestimo: "))
    
    totalSolicitado += emprestimo

    if salarioMensal >= 3000 and emprestimo <= salarioMensal * 10:
        print(f"Olá {nome} seu emprestimo de {emprestimo} foi aprovado")
        aprovados +=1
        totalAprovado += emprestimo

    elif salarioMensal >= 2000 and emprestimo <= salarioMensal * 5:
        print(f"Olá {nome}, seu emprestimo de {emprestimo} está em análise")
        analise +=1

    else:
        print(f"Olá {nome}, infelizmente não foi seu emprestimo não foi aprovado.")
        recusados +=1
        
media = totalSolicitado / 4

print(f"O total de aprovados é: {aprovados}")
print(f"O total de recusas é: {recusados}")     
print(f"O total em analise é: {analise}")
print(f"A soma de valores: {totalAprovado:.2f} e a média é: {media:.2f}")