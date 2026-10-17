# condicionais - if(Se), elif(Se não se), else (Se não) 

# Voce já terminou o trabalho? (True ou False)

Trabalho_terminado = True

if Trabalho_terminado == True:
    print("Parabéns, você terminou o trabalho!")
else:
    print("Você ainda não terminou o trabalho, continue se esforçando!")    
    
    
    
# Sintaxe

    # if condição:
        # código se for verdadeiro
    # else:
         # código se for falso
         
                 

# Ei, voce consegue me ajudar a mover essas caixas lá para fora hoje a tarde?

estou_disponivel = False
if estou_disponivel == True:
    print("Claro, posso te ajudar a mover as caixas!")
else:
    print("Desculpe, não posso te ajudar a mover as caixas hoje a tarde.")
   
   
   
   # Eu cheguei atrasado na aula. Ainda posso entrar?
   
   # Se for a primeira vez ou a segunda vez voce pode entrar, se for a terceira vez voce sera suspenso.
   
   
atrasos = int(input("Quantas vezes você chegou atrasado na aula? "))

if atrasos >= 3:
    print("Você foi suspenso por chegar atrasado na aula.")
elif atrasos == 2:
    print("Você ainda pode entrar na aula, mas tome cuidado com os atrasos.")
elif atrasos == 1:
    print("Mais duasn atrasos e você será suspenso, entre na aula agora.")
else:
    print("É a primeira vez que você chega atrasado, entre na aula agora.")
       
       
#  Sempre que você for usar o if, elif e else, você precisa ter uma condição para cada um deles.

#  Sempre começo com if, depois posso ter quantos elif eu quiser e por último o else. O else é opcional, mas se você quiser usar ele, ele precisa ser o último.



#Problema:

# Crie um programa que recebe dois valores e exibe o maior deles.
# Caso os valores sejam iguais, exiba uma mensagem informando que eles são iguais.

#---------------------------------------------------------------------

# metodo 5Q's para montar um algoritmo

# Analise criticamente o problema e descubra o que voce precisa fazer para resolve-lo. 

#(Tente explicar o problema com suas palavras, isso ajuda a entender melhor o que precisa ser feito. 
# Em voz alta, explique o problema para voce mesmo, ou para outra pessoa, ou escreva em um papel. 
# Isso ajuda a organizar as ideias e a entender melhor o que precisa ser feito.)

# Para isso, voce pode se basear em 5 perguntas:

#-------------------------------------------------------------------------

# 1. Quais são os dados de entrada?
# --- Valor 1 e valor 2 (dois números inteiros ou reais) que serão fornecidos pelo usuário.

# 2. O que devo fazer com esses dados?
# --- Comparar os dois valores e exibir o maior

# 3. Quais são as restrições do problema?
# --- Os valores devem ser números inteiros ou reais.

# 4. Qual é o resultado esperado?
# --- Exibir o maior valor entre os dois fornecidos ou informar que eles são iguais.

# 5. Quais são os passos para chegar ao resultado esperado? (pseudocodigo)

#input valor1 
#input valor2
#if valor1 > valor2 
    #print(valor1)
#elif valor2 > valor1
    #print(valor2)
#else valor1 == valor2
    #print("Os valores são iguais")

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
if valor1 > valor2:
    print(f"O maior valor é: {valor1}")
elif valor2 > valor1:
    print(f"O maior valor é: {valor2}")
else:
    print("Os valores são iguais.")