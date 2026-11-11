def calcu_vel_media(distancia, tempo):
    #codigo da função
    velocidadeMedia = distancia / tempo
    #Exibir o resultado
    print(f"A velocidade média é: {velocidadeMedia}")
    

#Solicitar distancia e tempo
dist_digitada = float(input("Digite a distancia percorrida: "))
tempo_digitado = float(input("Digite o tempo da viagem "))
calcu_vel_media(dist_digitada, tempo_digitado)

#O def pega o calculo e armazena o valor, e dentro dos (), voce coloca os valores que voce deseja!
