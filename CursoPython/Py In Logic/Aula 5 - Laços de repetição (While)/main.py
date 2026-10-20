# while

# Syntaxe
# while condição:
    #codigo a ser executado
# Criar um programa que permie 3 tentativas, antes de fechar

tentativas = 0
while tentativas < 3:
    print("Tente novamente")
    tentativas = tentativas + 1 
    
# Quando queremos que uma ação continue acontecendo, até que um criterio seja satisfeito

# só pode logar, se digitar a senha correta

senha = ""
while senha != "1995":
    senha = input("Digite a senha correta: ")
print("Bem-vindo ao sistema")

# Garantir que algo esteja preencido ou funcionando

nome = ""
while nome == "":
    nome = input("Digite seu nome: ")
print(f"Bem-vindo {nome}")


"""
Contadores dentro do while
ser avisado ás 17h do por do sol
contar de hora em hora até chegas ás 17h
ao chegar as 17h, exibir uma mensagem
"""

horario = 0
while horario <= 17:
    print(horario)
    horario = horario + 1
print("Hora de ver o por do sol")