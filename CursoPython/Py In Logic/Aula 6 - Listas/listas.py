# Listas

precos = [20, 30, 50]
print(precos[2]) # Acessando por indice

nomes = ["Brasil", "EUA", "Canadá", "Espanha"]
print(nomes[3])

# Encontrar índice automaticamente 
print(nomes.index("Espanha"))

# Manipular - add novos itens 
salarios = [2000, 5000, 7000, 1000]
salario_usuario = float(input("Quanto voce recebe: "))
salarios.append(salario_usuario)
print(salarios)