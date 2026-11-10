def calcu_vel_media():
    velocidadeMedia = distancia / tempo
    print(f"A velocidade média é: {velocidadeMedia}")
    

#Solicitar distancia e tempo
distancia = float(input("Digite a distancia percorrida: "))
tempo = float(input("Digite o tempo da viagem: "))

velocidadeMedia = distancia / tempo
#exibir o resultado

print(f"A velocidade média é: {velocidadeMedia}")