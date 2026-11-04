import sqlite3

conexao = sqlite3.connect("empresa.db")

cursor = conexao.cursor()

# Primeira tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS departamentos (
    id INTEGER,
    nome TEXT,
    responsavel TEXT,
    quantidade_funcionarios INTEGER
)
""")

# Segunda tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER,
    nome TEXT,
    preco REAL,
    estoque INTEGER
)
""")

# Terceira tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS fornecedores (
    id INTEGER,
    nome TEXT,
    telefone TEXT
)
""")

conexao.commit()

print("Tabelas criadas com sucesso!")

conexao.close()