# 🐍 Tarefa — Avaliação de alunos

'''
Nível intermediário

Objetivo: criar um programa que avalie 5 alunos e informe a situação de cada um.
_______________________________________________________________________________
1. Variáveis

Solicite, para cada aluno:
- Nome
- Idade
- Nota da prova
________________________________________________________________________________
2. Condicionais

Utilize as seguintes regras:
- Menor de 18 anos: Não elegível.
- Nota igual ou superior a 7: Aprovado.
- Nota entre 5 e 6,9: Recuperação.
- Nota abaixo de 5: Reprovado.
_________________________________________________________________________________
3. Laço for

- Repita o cadastro para 5 alunos.
- Mostre o nome, a nota e a situação de cada aluno.
- Não utilize while.
'''

aprovado = 0
recuperacao = 0
reprovado = 0
somaNotas = 0

for a in range(5):
    nome = input("Qual o seu nome: ")
    idade = int(input("Qual sua idade: "))
    nota =  float(input("Qual sua nota: "))
    
    somaNotas += nota
    
    if idade < 18:
        print("Cadastro invalido")
        
    elif nota >= 7:
        print(f"O aluno {nome} foi aprovado com nota: {nota}")
        aprovado +=1
        
    elif nota >= 5 and nota < 7:
        print(f"O aluno {nome} esta de recuperação com nota: {nota}")
        recuperacao +=1
        
    else:
        print(f"O aluno {nome} foi reprovado com nota: {nota}")
        reprovado +=1
        
media = somaNotas / 5

print("\n--- RESUMO FINAL ---")

for nome, valor in [
    ("Aprovados", aprovado),
    ("Em recuperação", recuperacao),
    ("Reprovados", reprovado),
    ("Soma das notas", somaNotas),
    ("Média das notas", media)
]:
    print(f"{nome}: {valor}")


