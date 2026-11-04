import sqlite3


# 1. Conexão com o banco
conexao = sqlite3.connect("ferreira_bank.db")

# 2. Criação do cursor
cursor = conexao.cursor()

# 3. Execução do comando SQL
cursor.execute("""
CREATE TABLE funcionarios (
    id INTEGER,
    nome TEXT,
    idade INTEGER
    
)
""")

cursor.execute("""
CREATE TABLE iF NOT EXISTS produtos(
    id INTEGER,
    nome TEXT,
    preco REAL,
    estoque INTEGER
)                
""")

# 4. Confirmação das alterações
conexao.commit()

print("Tabelas criada com sucesso!")

# 5. Encerramento da conexão
conexao.close()