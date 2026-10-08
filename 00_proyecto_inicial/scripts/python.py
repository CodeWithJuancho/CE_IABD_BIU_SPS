
import psycopg2
import pandas as pd
from datetime import datetime

FECHA = datetime.now().strftime("%m_%d_%y")


class User:
    def __init__(self, name, surname, email, genre, birth, phone, country, city, state):
        self.name = name
        self.surname = surname
        self.email = email
        self.genre = genre
        self.birth = birth
        self.phone = phone
        self.country = country
        self.city = city
        self.state = state


def database_init_connection():
    db_connection = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="1234",
        port="5432"
    )

    return db_connection


def database_insertion_query(db_connection, users):
    cursor = db_connection.cursor()

    for user in users:
        cursor.execute(
            """
            INSERT INTO users
            (name, surname, email, genre, birth, phone, country, city, state)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                user.name,
                user.surname,
                user.email,
                user.genre,
                user.birth,
                user.phone,
                user.country,
                user.city,
                user.state
            )
        )

    db_connection.commit()
    cursor.close()
    db_connection.close()
filas_rechazadas = []
filas_importadas = []
users = []

datos = pd.read_csv("../users/extracted/users.csv", keep_default_na=False)

for i, fila in datos.iterrows():
    fila_rechazada = False

    for dato in fila:
        if dato == "":
            fila_rechazada = True

    if fila_rechazada:
        filas_rechazadas.append(fila)
    else:
        filas_importadas.append(fila)

        user = User(
            fila["name"],
            fila["surname"],
            fila["email"],
            fila["genre"],
            fila["birth"],
            fila["phone"],
            fila["country"],
            fila["city"],
            fila["state"]
        )

        users.append(user)

with open(f"logs/{FECHA}_rejected_rows.txt", "w", encoding="utf-8") as archivo:
    archivo.write(f"There were {len(filas_rechazadas)} rejected rows.\n")

    for fila in filas_rechazadas:
        archivo.write(str(fila.to_dict()) + "\n")


with open(f"logs/{FECHA}_imported_rows.txt", "w", encoding="utf-8") as archivo:
    archivo.write(f"There were {len(filas_importadas)} imported rows.\n")

    for fila in filas_importadas:
        archivo.write(str(fila.to_dict()) + "\n")


db_connection = database_init_connection()
database_insertion_query(db_connection, users)

print("programa ejecutado con exito")


"""

docker run -d -p 5432:5432 --name proyecto0 -e POSTGRES_PASSWORD=1234 postgres

docker exec -i proyecto0 psql -U postgres <<'EOF'
CREATE TABLE IF NOT EXISTS users (
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
EOF


"""