'''
# Cenario real: Gerenciador de login simples

Crie um gerenciador de login simples, com maximo de 3 tentativas.

usuario = Ferreira
Senha = Senha123

após 3 tentativas, se o usuario estiver errado exibir:
"Aguarde 30 mins antes de tentar novamente"

Se acertar: "login feito com sucesso"

Metodo 5Q's

1 - Quais são os dados de entrada?
--- Login
--- Senha

2 - O que devo fazer com estes dados
--- Verificar se o login confere
--- Verificar se a senha confere 

3 - Quais as restrições deste problema?
--- Apenas 3 tentivas de acesso

4 - Qual é o resultado esperado?
--- Se acertar antes de 3 tentativas: login feito com sucesso
--- Se não acertar: Aguarde 30 minutos e tente novamente

5 - Qual a sequencia de passos a ser feita para chegar ao resultado esperado? (Pseudocodigo)

- Receber o login e senha
- Verificar se está correto
- permitir 3 tentativas
- Após 3 tentativas: Exibir "Tente novamente em 30 minutos"
- Se acertar antes: Exibir "Login feito com sucesso"

'''

usuario = ""
senha = ""
tentativas = 0

while (usuario != "Ferreira" or senha != "Senha123") and tentativas < 3:
    usuario = input("Digite seu usuario: ")
    senha = input("Digite sua senha: ")
    tentativas = tentativas + 1
    
if usuario == "Ferreira" and senha == "Senha123":
    print("Login feito com sucesso!")
else:
    print("Aguarde 30 minutos e tente novamente!")

# or (OU): basta uma das condições ser verdadeira para o resultado ser verdadeiro.

# and (E): todas as condições precisam ser verdadeiras para o resultado ser verdadeiro.

# Dica para memorizar: or aceita pelo menos uma condição verdadeira; and exige que todas sejam verdadeiras.