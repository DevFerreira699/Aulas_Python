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

# 4. Confirmação das alterações
conexao.commit()

print("Tabela criada com sucesso!")

# 5. Encerramento da conexão
conexao.close()