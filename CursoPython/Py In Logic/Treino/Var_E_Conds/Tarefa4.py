# Tarefa: sistema de cadastro de funcionário
# Você vai criar um programa que recebe os dados de um candidato a uma vaga 
# e verifica se as informações são válidas antes de avaliar a candidatura.

'''
Regras do exercício
_____________________________________________________________________________________
1. Solicite os dados:

- Nome do candidato.
- Idade.
- Salário pretendido.
- Anos de experiência profissional.
_____________________________________________________________________________________
2. Valide os dados:

Dado	                           Regra de validação
                                 
Idade	                           Deve estar entre 18 e 65 anos
Salário pretendido	               Deve ser maior que R$ 0
Experiência	                       Não pode ser negativa
______________________________________________________________________________________
3. Se os dados forem válidos, avalie a candidatura:

Condição	                       Resultado

Experiência de 3 anos ou mais	   Candidato experiente
Experiência inferior a 3 anos	   Candidato iniciante
_______________________________________________________________________________________

Se algum dado for inválido, informe o problema e não faça a classificação profissional.
'''

nome = input("Qual seu nome: ")
idade = int(input("Qual sua idade: "))
salario = float(input("Qual seu salário pretendido: "))
experiencia = float(input("Quanto tempo de experiencia voce tem: "))

if not (18 <= idade <= 65) or salario <= 0 or experiencia < 0:
    print("Inapto")   
    
elif experiencia >= 3:
    print(f"O candidato {nome} é experiente")
else:
    print(f"O candidato {nome} é iniciante")