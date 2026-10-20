#Problema

#Voce trabalha em um sistema que precisa verificar se todas as senhas digitadas por usuarios são válidas. Uma senha é considerada válida se atender aos seguintes critérios:

#1. Ter pelo menos 6 caracteres.
#2. Conter pelo menos uma letra maiúscula.
#3. Conter pelo menos um número.
#4. Conter um caracter especial

#Se a senha atender a todos os critérios, o sistema deve exibir uma mensagem informando que a senha é válida. Caso contrário, o sistema deve exibir uma mensagem informando que a senha é inválida.

# 1. Quais são os dados de entrada?
# --- Conter 6 ou mais caracterex
# --- Conter pelo menos uma letra maiúscula e numero
# --- Conter um caracter especial


# 2. O que devo fazer com esses dados?
# --- Verificar se tem os dados necessarios


# 3. Quais são as restrições do problema?
# --- Conter 6 ou mais caracterex
# --- Conter pelo menos uma letra maiúscula e numero
# --- Conter um caracter especial


# 4. Qual é o resultado esperado?
# --- Verificar se a senha tem os requisitos minimos e exibir na tela informando se está válido ou invalido


# 5. Quais são os passos para chegar ao resultado esperado? (pseudocodigo)

# receber a senha
# Verificar os requisitos minimos
# se possuir, permitir acesso
# se não, não permitir acesso

senhas = input("Diite sua senha: ")

tamanho = len(senhas) >= 6 # len para quantidade
maiuscula = any(c.isupper() for c in senhas) # isupper para letras maiusculas
numero = any(c.isdigit()for c in senhas) #isdigit para saber numeros
especial = any(not c.isalnum()for c in senhas) #isalnum para caracteres que não sejam letras ou numeros
    
if tamanho and maiuscula and numero and especial:
    print(f"A senha {senhas} é válida")
else:
    print(f"a senha {senhas} não contem os requisitos minimos.  ")