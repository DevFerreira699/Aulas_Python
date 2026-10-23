'''
Nível iniciante

Prática

Objetivo: criar um programa que avalie as notas de 5 alunos.

1. Variáveis

Para cada aluno, solicite:

- O nome.
- A nota de 0 a 10.

2. Use o for
O programa deverá repetir a solicitação de dados 5 vezes, usando for e range().

3. Use condicionais
Depois de receber a nota, classifique o aluno:

Nota                       	Resultado
Menor que 5	                Reprovado
De 5 até menos de 7	        Recuperação
7 ou mais	                Aprovado

4. Resultado final
Para cada aluno, mostre uma mensagem com o nome e a situação.
'''

aprovados = 0

for aluno in range(5):
    nome = input("Qual seu nome: ")
    nota = float(input("Qual nota: "))
    
    if nota < 5:
        print(f"O aluno {nome} foi Reprovado")
        
    elif nota < 7:
        print(f"O aluno {nome} está de recuperação")
        
    else:
        print(f"O aluno {nome} foi aprovado")
        aprovados += 1
    
        print(f"total de aprovados {aprovados}")