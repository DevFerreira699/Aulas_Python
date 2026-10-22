# 🐍 Nova tarefa: sistema de classificação de um candidato

# Imagine que uma empresa está selecionando candidatos para uma vaga. 
# Você vai criar um programa que avalia a elegibilidade com base em idade, experiência e resultado de uma prova.

'''
Regras do programa:
1. Solicite o nome do candidato.
2. Solicite a idade.
3. Pergunte quantos anos de experiência profissional ele possui.
4. Solicite a nota da prova, de 0 a 100.
5. Classifique o candidato pelas regras abaixo.
___________________________________________________________________________________
Condição	                                             Resultado
Menor de 18 anos	                                     Não elegível
Nota inferior a 60	                                     Reprovado na prova
Nota de 60 ou mais e experiência de 2 anos ou mais	     Aprovado
Nota de 60 ou mais e experiência inferior a 2 anos	     Cadastro reserva
___________________________________________________________________________________
'''

nome = input("Qual o seu nome: ")
idade = int(input("Qual a sua idade: "))


if idade < 18:
    print(f"O candidto {nome} está inelegivel")
else:
    experiencia = float(input("Quantos anos voce está na área: "))
    
    nota = float(input("Qual a sua nota: "))
    
    if nota < 60:
        print(f"O candidato {nome} não está legivel")
    elif (nota >= 60) and experiencia >= 2:
        print(f"Meus parabens {nome}, voce está APROVADO")
    else:
        print(f"O candidto {nome} está como reserva no cadastro")
        

