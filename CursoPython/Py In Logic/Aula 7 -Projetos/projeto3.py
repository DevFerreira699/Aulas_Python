# Projeto 3 - Medidor de velocidade

'''
Crie um programa que receba do usuaria um valor que represente a velocidade em uma via cuja velocidade maxima permitida é de 80km/h.

Com base nessa valor, o programa deve informar se o motorista levou uma multa leve, grave ou gravissima.

Se a velocidade estiver abaixo ou igual a 80km/h, exiba:"Não houve multa"
Se estiver até 10km/h acima, exiba: "Levou multa leve"
Se estiver 11km/h e 20km/h acima exiba: "Levou multa grave"
Se estiver acima de 20km/h exiba: "Levou multa gravissima"

Metodo 5Q's

1 - Quais são os dados de entrada?
-- Receber a velocidade do veiculo

2 - O que devo fazer com estes dado
-- Calcular qual a multa o veiculo irá receber

3 - Quais as restrições deste problema?
-- Se a velocidade estiver abaixo ou igual a 80km/h, exiba:"Não houve multa"
-- Se estiver até 10km/h acima, exiba: "Levou multa leve"
-- Se estiver 11km/h e 20km/h acima exiba: "Levou multa grave"
-- Se estiver acima de 20km/h exiba: "Levou multa gravissima"

4 - Qual é o resultado esperado?
-- Exibir qual foi a multa recebida
-- 

5 - Qual a sequencia de passos a ser feita para chegar ao resultado esperado? (Pseudocodigo)

-- receber a velocidade
-- Se a velocidade estiver abaixo ou igual a 80km/h, exiba:"Não houve multa"
-- Se estiver até 10km/h acima, exiba: "Levou multa leve"
-- Se estiver 11km/h e 20km/h acima exiba: "Levou multa grave"
-- Se estiver acima de 20km/h exiba: "Levou multa gravissima"
'''

velocidade = float(input("voce estava a quantos por hora: "))
maxima = 80

if velocidade <=  80:
    print("Voce está dentro do limite permitido!")
elif velocidade <= maxima + 10:
    print("Multa: Leve")
elif velocidade <= maxima + 20:
    print("Multa: Grave")
else:
    print("Multa: Gravissima")