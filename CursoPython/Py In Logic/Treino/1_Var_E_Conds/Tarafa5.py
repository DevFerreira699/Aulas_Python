'''
Exercício 3 — Sistema de seleção de candidatos

Você deverá criar um programa em Python que avalie candidatos a uma vaga de emprego.
___________________________________________________________________________________________
1. Solicite os dados

- Nome do candidato.
- Idade.
- Salário pretendido.
- Anos de experiência.
- Nota na entrevista, de 0 a 10.
- Escolaridade: "medio", "tecnico" ou "superior".
___________________________________________________________________________________________
2. Valide os dados

Dado	                                      Regra
Idade	                                      Entre 18 e 65 anos
Salário	                                      Maior que R$ 0
Experiência	                                  Não pode ser negativa
Nota	                                      Entre 0 e 10
Escolaridade	                              Deve ser uma das três opções válidas
___________________________________________________________________________________________
Se qualquer dado for inválido, exiba Dados inválidos e não avalie a candidatura.
___________________________________________________________________________________________
3. Avalie a candidatura

Se os dados forem válidos, aplique as seguintes regras, nesta ordem:

1. Reprovado: nota inferior a 5.
2. Aprovado: nota igual ou superior a 5, mas inferior a 7.
3. Aprovado com destaque: nota igual ou superior a 7.
4. Classifique o perfil profissional
___________________________________________________________________________________________
Além do resultado acima, informe o perfil do candidato:

- Experiente: 5 anos ou mais de experiência.
- Intermediário: de 2 anos até menos de 5 anos.
- Iniciante: menos de 2 anos.
___________________________________________________________________________________________
5. Bônus: verifique a compatibilidade salarial

Se o candidato for aprovado ou aprovado com destaque, informe também:

- Salário pretendido de até R$ 3.000: Dentro do orçamento.
- Salário acima de R$ 3.000: Fora do orçamento.
___________________________________________________________________________________________
'''

nome = input("Qual o seu nome: ")
idade = int(input("Qual a sua idade: "))
salario = float(input("Qual seu pretenção salarial: "))
experiencia = float(input("Quanto tempo de experiencia possui: "))
nota = float(input("Qual a sua nota alcançada: "))
escolaridade = input("Qual sua escolaridade").lower()

if (
    idade < 18 or idade > 65
    or salario <= 0
    or experiencia < 0
    or nota < 0 or nota > 10
    or escolaridade not in ("medio", "tecnico", "superior")):
    print("Dados inválidos")
    
else:
    if nota < 5:
        print(f"O candidato {nome} foi reprovado")
    elif nota < 7:
        print(f"O candidato {nome} foi aprovado")
    else:
        print(f"O candidato {nome} foi aprovado com destaque")

    if experiencia >= 5:
        print("Experiente")
    elif experiencia >= 2:
        print("Intermediário")
    else:
        print("Iniciante")

    if nota >= 5:
    
        if salario <= 3000:
            print(f"O candidato {nome} está dentro do orçamento: {salario:.2f}")
        else:
            print("Fora do orçamento")
