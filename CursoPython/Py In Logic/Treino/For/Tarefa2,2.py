#Exercício: contar alunos em recuperação

'''
Crie um programa que leia o nome e a nota de 5 alunos.

- Nota menor que 5: reprovado.
- Nota de 5 até menos de 7: recuperação.
- Nota igual ou maior que 7: aprovado.

Desafio: além de mostrar a situação de cada aluno, o programa deve contar quantos ficaram de recuperação e mostrar o total no final.

'''
aprovados = 0
recuperacao = 0
reprovado = 0
somaNotas = 0

for a in range(5):
    nome = input("Qual seu nome: ")
    nota = float(input("Qual sua nota: "))
    
    somaNotas += nota
    
    if nota < 5:
        print(f"O aluno {nome} foi reprovado: nota {nota}")
        reprovado +=1
        
    elif nota < 7:
        print(f"O aluno {nome} está de recuperação: nota {nota}")
        recuperacao +=1
        
    else:
        print(f"O aluno {nome} foi aprovado: nota {nota}")
        aprovados +=1
        
media = somaNotas / 5
        
print(f"Foram aprovados: {aprovados}, recuperação: {recuperacao} e reprovado: {reprovado}")
print(f"A média da turma foi: {media:.2f}")



 
 
 
 


