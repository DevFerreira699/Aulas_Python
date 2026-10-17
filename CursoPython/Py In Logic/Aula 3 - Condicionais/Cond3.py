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




