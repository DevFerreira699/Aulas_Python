# Variaveis

velocidadeInternet = 100  # velocidade em Mbps
print(f"Velocidade da internet: {velocidadeInternet} Mbps")

# Numeros inteiros (int)
numeroInteiro = 10
print(f"Numero inteiro: {numeroInteiro}")

# Numeros decimais (float)
numeroDecimal = 3.14
print(f"Numero decimal: {numeroDecimal}")

# Textos (str) (string)
texto = "Olá, mundo!"
print(f"Texto: {texto}")

#booleanos (True ou False)
verdadeiro = True 
false = False
print(f"Verdadeiro: {verdadeiro}")
print(f"False: {false}")

# Len - Quantidade de caracteres

senhas = len(["abs", "segura123", "123456", "python123", "09"])

# Caso voce precisa descobrir qual o tipo de uma variavel,
# voce pode usar a funcao type()
print(f"Tipo da variavel velocidadeInternet: {type(velocidadeInternet)}")



# metodo 5Q's para montar um algoritmo

# Analise criticamente o problema e descubra o que voce precisa fazer para resolve-lo. 

# Para isso, voce pode se basear em 5 perguntas:

# 1. Quais são os dados de entrada?
# ---Horas Trabalhadas e Salario mensal

# 2. O que devo fazer com esses dados?
# --- Calculator o salario por hora

# 3. Quais são as restrições do problema?
# --- Precisa ter a valor do salario mensal e das horas trabalhadas

# 4. Qual é o resultado esperado?
# --- Exibir o valor do salario por hora

# 5. Quais são os passos para chegar ao resultado esperado? (pseudocodigo)

# Receber o valor do salario mensal
# Receber o valor das horas trabalhadas
# valor horas trabalhadas = valor do salario mensal / valor das horas trabalhadas
# exibir o valor do salario por hora

salarioMensal = float(input("Digite o salario mensal: "))
horasTrabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
valorHora = float(salarioMensal / horasTrabalhadas)
print(f"O valor do salario por hora é: {valorHora:.2f}")
