import sqlite3

conexao = sqlite3.connect("empresa.db")

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE iF NOT EXISTS produtos(
    id INTEGER,
    nome TEXT,
    preco REAL,
    estoque INTEGER
)                
""")

conexao.commit()

print("Tabela produtos criada com sucesso!")

conexao.close()