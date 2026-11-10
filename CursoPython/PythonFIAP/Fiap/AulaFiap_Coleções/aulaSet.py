
# Criando um set vazio0
conjunto = set()
print(type(conjunto))

# Criando um set a partir de uma lista

lista = ["Thiago", "Lucas", "Juliana", "Kimberly", "Thiago"]
print(lista)

conjunto2 = set(lista)
print(conjunto2)

# Criando um set com valores

conjunto3 = {"CJ", "Trevor", "Franklin", "NIKO", "CJ"}
print(conjunto3)

conjunto3.add("Claude") # adiciona um elemento (.add)
print(conjunto3)

# comparando dois sets

itens1 = {"Thiago", "Lucas", "Juliana", "Kimberly", "Thiago", "CJ", "Trevor",}
itens2 = {"CJ", "Trevor", "Franklin", "NIKO", "CJ", "Thiago", "Lucas", "Juliana"}

print(itens1)
print(itens2)

itens1.difference_update(itens2)
print(itens1)


# remover um elemento (.remove ou .discard)

itens1 = {"Thiago", "Lucas", "Juliana", "Kimberly", "Thiago", "CJ", "Trevor",}
itens1.remove("CJ")
print(itens1)

itens1.discard("Thiago")
print(itens1)