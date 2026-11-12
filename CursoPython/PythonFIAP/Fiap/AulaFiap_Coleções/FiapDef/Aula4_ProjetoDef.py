#FUNÇÃO PARA CALCULAR VELOCIDADE MÉDIA
def calcu_vel_media(distancia:float, tempo:float, unidadeMedida="km/h"):
    if tempo == 0:
        return 0
    velocidade_media = distancia / tempo
    return f"{velocidade_media} {unidadeMedida}"

#FUNÇÃO PARA CONVERTER A TEMPERATURA
def convert_tempe(temperatura:float, uni_medida="celsius"):
    if uni_medida == "celsius":
        return temperatura * 1.8 + 32
    elif uni_medida == "fahrenheit":
        return(temperatura - 32) / 1.8
    else:
        return 0
    
#FUNÇÃO PARA EXIBIR UM MENU
def exibirMenu():
    print("MENU")
    print("1 - Calcular a velocidade média ")
    print("2 - Converter a temperatura ")
    print("3 - Sair")
    
#FUNÇÃO PARA CHAMAR AS OUTRAS FUNCÕES
def alunoDfisica():
    op = 0
    while op != 3: # Função velocidade
        exibirMenu()
        op = int(input("Informe a opção desejada: "))
        if op == 1:
            dist_percorrida = float(input("Informe a distancia: "))
            tempo_viagem = float(input("Informe o tempo da viagem: "))
            medida = input("Informe a unidade de medida: ")
            print(f"A velocidade média é: {calcu_vel_media(dist_percorrida, tempo_viagem, medida)}")
            
        elif op == 2: # Função temperatura
            temp_informada = float(input("Informe a temperatura que deseja converter: "))
            medida = input("A temperatura informada está em celsius ou fahrenheit: ")
            print(f"O resultado da conversão é: {convert_tempe(temp_informada, medida)}")
            
        elif op == 3: 
            print("SAINDO DO SISTEMA")
            break
        else:
            print("Opção invalidad")
            
 # Faz a função ser chamada, tipo o print
