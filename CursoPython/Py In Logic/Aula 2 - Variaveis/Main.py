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

salario_Mensal = float(input("Digite o salario mensal: "))
horas_Trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
valor_Hora = float(salario_Mensal / horas_Trabalhadas)

print(f"O valor do salario por hora é: {valor_Hora:.2f}")
