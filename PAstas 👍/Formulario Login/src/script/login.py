import os
import sqlite3

conn =sqlite3.connect('login.db')
cursor = conn.cursor()

cursor.execute(
    '''          
        CREATE TABLE IF NOT EXISTS usuarios ( 
        id INTEGER PRIMARY KEY,
        email TEXT NOT NULL,
        senha INTEGER NOT NULL
    )
'''
)


os.system('cls')
email = "gabrielgones5@gmail.com"
senha = "123123"

cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", (email, senha))
conn.commit


conn.commit()
conn.close