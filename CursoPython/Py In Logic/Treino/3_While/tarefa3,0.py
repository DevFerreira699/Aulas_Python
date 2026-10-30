'''
Atividade — Sistema de cadastro e análise de alunos

Nível intermediário

Você deverá desenvolver um programa que cadastre 5 alunos, calcule suas médias e apresente um relatório de desempenho.

1. Cadastro dos alunos — for

Para cada aluno, solicite:

- Nome;
- Nota da primeira prova;
- Nota da segunda prova;
- Nota da terceira prova.

Armazene os dados em uma lista de dicionários.

2. Cálculo e classificação — if / elif / else

Calcule a média de cada aluno:

Classifique os alunos:

Média	                Situação
7,0 ou superior	        Aprovado
5,0 até 6,9	            Recuperação
Abaixo de 5,0	        Reprovado

3. Consulta de alunos — while

Após cadastrar os cinco alunos, permita consultar as notas e a média de um aluno pelo nome.

- Se encontrar, mostre os dados.
- Se não encontrar, informe que o aluno não está cadastrado.
- Pergunte se deseja realizar outra consulta.
- O programa deve continuar até o usuário escolher sair.

4. Relatório final

Ao encerrar as consultas, apresente:

- Quantidade de alunos cadastrados;
- Média geral da turma;
- Quantidade de aprovados;
- Quantidade em recuperação;
- Quantidade de reprovados;
- Maior média;
- Menor média.
'''

alunos = []
aprovados = 0
recuperacao = 0
reprovados = 0
soma_medias = 0

# 1. Cadastro dos alunos
for aluno in range(2):
    print("\n=== Cadastro de alunos ===")
    nome = input("Aluno: ")
    n1 = float(input("Nota P1: "))
    n2 = float(input("Nota P2: "))
    n3 = float(input("Nota P3: "))

    media = (n1 + n2 + n3) / 3

    if media >= 7:
        situacao = "Aprovado"
        aprovados += 1
    elif media >= 5:
        situacao = "Recuperação"
        recuperacao += 1
    else:
        situacao = "Reprovado"
        reprovados += 1

    alunos.append({
        "Aluno": nome,
        "Nota1": n1,
        "Nota2": n2,
        "Nota3": n3,
        "Média": media,
        "Situaçao": situacao,
    })

# 2. Inicialização da maior e menor média
maior_media = alunos[0]["Média"]
menor_media = alunos[0]["Média"]

# 3. Consulta de alunos
continuar = "S"

while continuar == "S":
    nomeBusca = input("\nQual aluno deseja consultar? ")
    encontrado = False

    for aluno in alunos:
        if nomeBusca.lower() == aluno["Aluno"].lower():
            print("\n=== Dados do aluno ===")
            print(f"Aluno: {aluno['Aluno']}")
            print(f"Nota P1: {aluno['Nota1']:.2f}")
            print(f"Nota P2: {aluno['Nota2']:.2f}")
            print(f"Nota P3: {aluno['Nota3']:.2f}")
            print(f"Média: {aluno['Média']:.2f}")
            print(f"Situação: {aluno['Situaçao']}")

            encontrado = True

    if encontrado == False:
        print("Aluno não cadastrado!")

    continuar = input("\nDeseja consultar outro aluno? S/N: ").upper()

print("\nConsultas encerradas!")

# 4. Cálculo do relatório
for aluno in alunos:
    soma_medias += aluno["Média"]

    if aluno["Média"] > maior_media:
        maior_media = aluno["Média"]

    if aluno["Média"] < menor_media:
        menor_media = aluno["Média"]

media_geral = soma_medias / len(alunos)

# 5. Relatório final
print("\n================================")
print("       RELATÓRIO DA TURMA")
print("================================")
print(f"Alunos cadastrados: {len(alunos)}")
print(f"Média geral: {media_geral:.2f}")
print("--------------------------------")
print(f"Aprovados: {aprovados}")
print(f"Recuperação: {recuperacao}")
print(f"Reprovados: {reprovados}")
print("--------------------------------")
print(f"Maior média: {maior_media:.2f}")
print(f"Menor média: {menor_media:.2f}")
print("================================")
