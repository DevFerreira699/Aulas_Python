import sqlite3

conexao = sqlite3.connect("TesteEmpresa.db")

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS veiculos(
    id INTEGER,
    modelo TEXT,
    ano INTEGER,
    valor REAL,
    disponivel INTEGER
)               
""")

conexao.commit()
print("Teste executado com sucesso! ")

conexao.close()
