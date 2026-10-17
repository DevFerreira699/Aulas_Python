faturamente = 1000.00
custo = 500.00
lucro = faturamente - custo
print("O lucro é:", lucro)


novasVendas = 1500.00
faturamente += novasVendas

imposto = 0.15 * faturamente
print("O imposto a ser pago é:", imposto)

print("O faturamento total é:", faturamente)
print("O custo total é:", custo)
print("O lucro líquido é:", lucro - imposto)

mensagem = "O lucro líquido após o pagamento do imposto é: {lucro - imposto}" #string

teveLucro = True #boolean

margemLucro = lucro / faturamente #float
print("A margem de lucro é:", margemLucro)



