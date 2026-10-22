'''
róximo passo: validar as notas
Tente resolver este novo desafio sem mudar a lógica de aprovação que você já criou:

Regra: se qualquer uma das duas notas for menor que 0 ou maior que 10,
o programa deverá exibir Nota inválida. 
Caso contrário, deverá calcular a média e informar se o aluno foi aprovado, 
ficou de recuperação ou foi reprovado.

Dica: você pode usar or para verificar se pelo menos uma das notas é inválida.
'''
nome = input("digite seu nome: ")

nota1 = float(input("Qual sua nota na P1: "))
nota2 = float(input("Qual sua nota na P2: "))

if (nota1 < 0 or nota1 > 10) or (nota2 < 0 or nota2 > 10):
    print("Nota inválida")
else:
    media = (nota1 + nota2) / 2
    
    if media >= 7:
        print(f"O aluano {nome} foi aprovado com a média {media}")
    elif media >= 5 and media < 7:
        print(f"O aluno {nome} está de Recuperação com a média {media}")
    else:
        print(f"O aluno {nome} está Reprovado com a média {media}")
