from datetime import date
from datetime import datetime
from pathlib import Path
import psycopg2
import numpy as np
import pandas as pd
import os

fechaActual = date.today()

fechaPartes = (f"{fechaActual.month}_{fechaActual.day}_{fechaActual.year}")
print("Fecha de ejecución:", fechaPartes)

# Ruta de tu archivo CSV
rutaCsv = Path('/home/gabriel/proyecto/CE_IABD_BIU_SPS/00_proyecto_inicial/users/extracted/users.csv')

df = pd.read_csv(rutaCsv)

filasImportadas = df.dropna()
filasRechazadas = df.loc[df.isnull().any(axis=1)]

#dirección de logs
dirLogs = Path('/home/gabriel/proyecto/CE_IABD_BIU_SPS/00_proyecto_inicial/scripts/logs')
dirLogs.mkdir(parents=True, exist_ok=True)

#a logs se crean archivos, con cierto nombre y se aañde la información
rutaImportadas = dirLogs / f"{fechaActual}_imported_rows.txt"
with open(rutaImportadas, 'w', encoding='utf-8') as f:
    f.write(f"logs/{fechaActual}_imported_rows.txt\nThere were {len(filasImportadas)} imported rows.\n")

rutaRechazadas = dirLogs / f"{fechaActual}_rejected_rows.txt"
texto_rechazadas = f"logs/{fechaActual}_rejected_rows.txt\nThere were {len(filasRechazadas)} imported rows.\n{filasRechazadas}"
with open(rutaRechazadas, 'w', encoding='utf-8') as f:
    f.write(texto_rechazadas)

#se crea la clase user 
class User:
    def __init__(self, id, name, surname, email, genre, birth, phone, country, city, state):
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
        self.genre = genre
        self.birth = birth
        self.phone = phone
        self.country = country
        self.city = city
        self.state = state

usuariosValidados = []
usuariosAusentes = []

#ya que tengo los usuarios separados, lo mento al lista
for fila in filasImportadas.to_dict(orient='records'):
    nuevo_usuario = User(**fila)
    usuariosValidados.append(nuevo_usuario)

for fila in filasRechazadas.to_dict(orient='records'):
    nuevo_usuario = User(**fila)
    usuariosAusentes.append(nuevo_usuario)

def database_init_conection():
    #conectar postgres a través de docker con py
    try:

        conexion = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="1234",
            port="5432"
        )
        print("se ha conectado docker y py")
        return conexion
    
    except Exception as e:
        print(f"error conexión: {e}")
        return None

def database_insertion_query(db_connection, users):
    #información necesaria para primero de todo crear la tabla, recorrerla e insertar los usuarios correctos
    try:
        cursor = db_connection.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            surname VARCHAR(50) NOT NULL,
            email VARCHAR(255) NOT NULL,
            genre VARCHAR(20),
            birth DATE,
            phone VARCHAR(20),
            country VARCHAR(50),
            city VARCHAR(50),
            state VARCHAR(50)
        );
        """)

        for user in users:
            cursor.execute("""
                INSERT INTO users (name, surname, email, genre, birth, phone, country, city, state)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                user.name, user.surname, user.email, 
                user.genre, user.birth, user.phone, 
                user.country, user.city, user.state
            ))

        db_connection.commit()
        print("usuarios insertados en bbdd")

    except Exception as e:
        print(f"error al insertar datos: {e}")
        db_connection.rollback()
#cerrar la conexcion
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        
        if db_connection:
            db_connection.close()
            print("conexión cerrada.")

mi_conexion = database_init_conection()

if mi_conexion:
    database_insertion_query(mi_conexion, usuariosValidados)