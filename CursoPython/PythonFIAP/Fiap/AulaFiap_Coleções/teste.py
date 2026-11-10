opcao = 0
ficha = {}

while opcao !=4:
    print("\nFICHA DE CADASTRO")
    print("1 - Incluir informações na ficha")
    print("2 - Recuperar informações da ficha")
    print("3 - Exibir a ficha completa")
    print("4 - Sair")
    
    opcao = int(input("Qual opção deseja selecionar: "))
    
    if opcao == 1:
        chave = input("Insira o campo que deseja cadastrar: ")
        valor = input("Inform o dado que deseja cadastrar: ")
        ficha.update({chave:valor}) #.update adciona um campo novo ao dicionario
    
    elif opcao == 2:
           print(f"Os campos disponiveis são: {ficha.keys()}") # .key mostra as chaves no dicionario
           chave = input("informe o campo que deseja exibir: ")
           if chave in ficha.keys(): 
               print(f"O campo {chave} contem o dado {ficha.get(chave)}")  #.get mostra o valor que contem na chave
           else:
               print("Campo inexistente")
               
    elif opcao == 3:
        print(f"== INFORMAÇÕES CADASTRAIS ==")
        for campo, dado in ficha.items(): #.items transforma a lista em uma tupla, e separa a chave do valor (Chave-nome:Valor-Ferreira)
            print(f"{campo.upper()} -> {dado}")
            
    elif opcao == 4:
           print("Saindo da aba de cadastro")
           break #Interrompe o loop while
           
    else:
        print("Insira um valor valido! ")