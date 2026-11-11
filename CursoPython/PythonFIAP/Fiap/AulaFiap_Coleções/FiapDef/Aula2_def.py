def calcu_vel_media(distancia:float, tempo:float, unidade_med="km/h"):
    #codigo da função
    velocidadeMedia = distancia / tempo
    #Exibir o resultado
    print(f"A velocidade média é: {velocidadeMedia} {unidade_med}")
    

calcu_vel_media(200, 50, "m/s")

#Os valores que estiverem dentro do (), sempre serão prioridade
