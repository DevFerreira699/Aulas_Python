faturamento = float(1000) # o float é usado para converter o valor em ponto flutuante, ou seja, um número decimal.
custo = float(400)

lucro = faturamento - custo
# texto = "O lucro mensal é R$" + str(lucro) + " e o faturamento é R$" + str(faturamento)

texto = f"O lucro mensal é de R${lucro} e o faturamento é de R${faturamento}."
print(texto)
 
 
email = " CLIENTE@empresa.com"
 
email = email.lower() # o strip remove os espaços em branco no início e no final da string
email = email.strip() # o lower converte todos os caracteres da string para minúsculo
print(email)

# Tamanho de strings
print(len(email)) # length, ou seja, o tamanho da string. O resultado será 20!

# posição
posicao = email.find("@") 
print(email[12]) # o resultado será "m"

# pedaços do texto
print(email[0:7]) # o resultado será "cliente"
print(email[8:15]) # o resultado será "empresa"

print(email[posicao:]) # o resultado será "@empresa.com"

# Trocar um pedaço do texto por outro