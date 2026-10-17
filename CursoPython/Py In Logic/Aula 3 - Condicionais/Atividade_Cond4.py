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