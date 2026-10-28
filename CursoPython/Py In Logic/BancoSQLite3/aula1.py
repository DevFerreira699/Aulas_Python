import sqlite3

banco = sqlite3.connect('primeiro_banco.db')

cursor = banco.cursor()

cursor.execute("CREATE TABLE Pessoas (Nome text,idade integer,email text)")

cursor.execute("INSERT INTO Pessoas VALUES ('Ferreira',23,'contatoferreira830@gmail.com')")

banco.commit()