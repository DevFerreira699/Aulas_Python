import sqlite3

conexao = sqlite3.connect("TesteEmpresa.db")

cursor = conexao.cursor()

cursor.execute("SELECT * FROM veiculos")

resultado = cursor.fetchall()

print(resultado)

conexao.commit()

conexao.close()