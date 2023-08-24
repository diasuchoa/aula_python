# import mysql.connector

conexao = sgbd.connector.connct(
    host='localhost',
    user='root',
    password='123456',
    database='nomedobanco',
)

cursor = conexao.cursor()

cursor.close()
conexao.close()

# CREATE
nome_aluno = "junior"
idade = 39
comando = f'INSERT INTO aluno (nome, idade) values ("{nome_aluno}", {idade})'
cursor.execute(comando)
conexao.commit()  # Edita o banco de dados

# READ
comando = f'SELECT * FROM aluno'
cursor.execute(comando)
resultado = cursor.fetchall()  # Lê o banco de dados
print(resultado)

# UPDATE
nome_aluno = "junior"
idade = 38
comando = f'UPDATE aluno SET idade = {idade} WHERE nome_aluno = "{nome_aluno}"'
cursor.execute(comando)
conexao.commit()  # Edita o banco de dados

# DELETE
nome_aluno = "junior"
comando = f'DELET FROM aluno WHERE nome_aluno = "{nome_aluno}"'
cursor.execute(comando)
conexao.commit()  # Edita o banco de dados
