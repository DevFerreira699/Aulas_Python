import sqlite3

conexao = sqlite3.connect("empresa.db")

cursor = conexao.cursor()

# Primeira tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS departamentos (
    id INTEGER,
    setor TEXT,
    responsavel TEXT,
    quantidade_funcionarios INTEGER
)
""")

# Segunda Tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS funcionarios_teste (
    id INTEGER,
    nome TEXT,
    idade INTEGER,
    salario REAL,
    ativo INTEGER    
)         
""")

conexao.commit()

print("Tabelas criadas com sucesso!")

cursor.execute("""
INSERT INTO departamentos (id, setor, responsavel, quantidade_funcionarios) 
VALUES
(1, 'Recursos Humanos', 'Maria Silva', 10),
(2, 'Financeiro', 'João Souza', 8),
(3, 'Tecnologia da Informação', 'Carlos Oliveira', 15)
""")

cursor.execute("""
INSERT INTO funcionarios_teste (id, nome, idade, salario, ativo)
VALUES
(1, 'Ana Santos', 28, 3500.00, 1),
(2, 'Bruno Lima', 35, 4500.00, 1),
(3, 'Carla Pereira', 30, 4000.00, 0),
(4, 'Diego Costa', 25, 3000.00, 1),
(5, 'Fernanda Rocha', 32, 4200.00, 1)             
""")

conexao.commit()

print("inserção concluída!")
conexao.close()