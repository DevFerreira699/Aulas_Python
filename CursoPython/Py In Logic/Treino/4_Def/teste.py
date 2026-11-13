from datetime import datetime

funcionarios = [] 

op = 0

while op != 6:
    print("== Menu Principal ==")
    print("----------------------")
    print("1. Cadastrar funcionário.")
    print("2. Listar funcionários.")
    print("3. Consultar funcionário.")
    print("4. Calcular folha salarial.")
    print("5. Mostrar estatísticas.")
    print("6. Sair.")

    op = int(input("Escolha uma opção: "))

    if op == 1:
        print("----------------------")
        print("== Menu de Cadastro ==")
        print("Informe os dados do funcionário:")

        nome = input("Informe seu nome: ")
        nascimento = int(input("Informe o ano do seu nascimento: "))

        ano_atual = datetime.now().year
        idade = ano_atual - nascimento

        if idade <= 18 or nascimento > ano_atual:
            print("Idade inválida. O funcionário deve ter mais de 18 anos.")
            continue

        else:
            print(f"Idade válida: {idade} anos.")

            cargo = input("Informe seu cargo de ocupação: ")
            salario = float(input("Informe seu salário: "))
            horasTrabalhadas = float(input("Informe a quantidade de horas trabalhadas no mês: "))

            lista_cadastro = {
                "nome": nome,
                "idade": idade,
                "cargo": cargo,
                "salario": salario,
                "horas": horasTrabalhadas
            }

            funcionarios.append(lista_cadastro)

            print("Funcionário cadastrado com sucesso!")

    elif op == 2:
        print("\n----------------------")
        print("\n== Menu de Listagem ==")
        print("\nListando funcionários cadastrados...")

        if not funcionarios:
            print("Nenhum funcionário cadastrado.")

        else:
            for funcionario in funcionarios:
                print(f"\n- Nome: {funcionario['nome']}")
                print(f"\n- Idade: {funcionario['idade']}")
                print(f"\n- Cargo: {funcionario['cargo']}")
                print(f"\n- Salário: {funcionario['salario']:.2f}")
                print(f"\n- Horas Trabalhadas: {funcionario['horas']}")

    elif op == 3:
        print("----------------------")
        print("== Menu de Consulta ==")
        print("Informe o nome do funcionário que deseja consultar:")
        nomeConsulta = input("Nome do funcionário: ")

        encontrado = False
        for funcionario in funcionarios:
            if funcionario['nome'] == nomeConsulta:
                print(f"\n- Nome: {funcionario['nome']}")
                print(f"\n- Idade: {funcionario['idade']}")
                print(f"\n- Cargo: {funcionario['cargo']}")
                print(f"\n- Salário: {funcionario['salario']:.2f}")
                print(f"\n- Horas Trabalhadas: {funcionario['horas']}")
                encontrado = True
                break

            else:
                print("Funcionário não encontrado.")    

    elif op == 4:
        print("----------------------")
        print("== Menu de Folha Salarial ==")
        print("Calculando folha salarial...")

        if not funcionarios:   
            print("Nenhum funcionário cadastrado.")

        else:
            total_salarios = sum(funcionario['salario'] for funcionario in funcionarios)
            media_salarial = total_salarios / len(funcionarios)
            maior_salario = max(funcionario['salario'] for funcionario in funcionarios)
            menor_salario = min(funcionario['salario'] for funcionario in funcionarios)

            print(f"\n- Total gasto com salários: R$ {total_salarios:.2f}")
            print(f"- Média salarial: R$ {media_salarial:.2f}")
            print(f"- Maior salário: R$ {maior_salario:.2f}")
            print(f"- Menor salário: R$ {menor_salario:.2f}")

    elif op == 5:
        print("----------------------")
        print("== Menu de Estatísticas ==")
        print("Mostrando estatísticas...")

        if not funcionarios:
            print("Nenhum funcionário cadastrado.")

        else:
            total_funcionarios = len(funcionarios)
            acima_3000 = sum(1 for funcionario in funcionarios if funcionario['salario'] > 3000)
            abaixo_2000 = sum(1 for funcionario in funcionarios if funcionario['salario'] < 2000)
            idade_30_ou_mais = sum(1 for funcionario in funcionarios if funcionario['idade'] >= 30)

            print(f"\n- Quantidade total de funcionários: {total_funcionarios}")
            print(f"- Quantos recebem acima de R$ 3.000: {acima_3000}")
            print(f"- Quantos recebem abaixo de R$ 2.000: {abaixo_2000}")
            print(f"- Quantos têm idade igual ou superior a 30 anos: {idade_30_ou_mais}")

    elif op == 6:
        print("----------------------")
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")

