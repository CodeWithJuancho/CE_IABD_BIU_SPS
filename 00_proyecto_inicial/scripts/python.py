import csv
from datetime import date
import os
import psycopg2


class User:

  def __init__(
      self, name, surname, email, genre, birth, phone, country, city, state
  ):
    self.name = name
    self.surname = surname
    self.email = email
    self.genre = genre
    self.birth = birth
    self.phone = phone
    self.country = country
    self.city = city
    self.state = state

  def __str__(self):
    return f"{self.name} {self.surname} ({self.email})"



hoy = date.today()
fechahoy = f"{hoy.month}_{hoy.day}_{hoy.year}"


os.makedirs("scripts/logs", exist_ok=True)

rechazadas = []
importadas = []
users = []  

with open("users/extracted/users.csv", encoding="utf-8", newline="") as csvfile:
  csvreader = csv.reader(csvfile)
  header = next(csvreader, None)

  if header is None:
    raise ValueError("El archivo CSV está vacío.")

  columnas_esperadas = len(header)

  for row in csvreader:
    
    if not row or all(field.strip() == "" for field in row):
      continue

   
    tiene_dato_ausente = any(field.strip() == "" for field in row)
    columnas_incorrectas = len(row) != columnas_esperadas

    if columnas_incorrectas or tiene_dato_ausente:
      
      rechazadas.append(row)
    else:

      importadas.append(row)

      
      user_obj = User(
          name=row[1].strip(),
          surname=row[2].strip(),
          email=row[3].strip(),
          genre=row[4].strip(),
          birth=row[5].strip(),
          phone=row[6].strip(),
          country=row[7].strip(),
          city=row[8].strip(),
          state=row[9].strip(),
      )

      
      users.append(user_obj)

with open(
    f"scripts/logs/{fechahoy}_rejected_rows.txt", "w", encoding="utf-8", newline=""
) as file:
  file.write(f"There were {len(rechazadas)} rejected rows.\n")
  for row in rechazadas:
    file.write(",".join(row) + "\n")


with open(
    f"scripts/logs/{fechahoy}_imported_rows.txt", "w", encoding="utf-8", newline=""
) as file:
  file.write(f"There were {len(importadas)} imported rows.\n")
  for row in importadas:
    file.write(",".join(row) + "\n")

def database_init_connection():
  
  connection = psycopg2.connect(
      host="localhost",
      database="postgres",  
      user="postgres",  
      password="1234",  
      port="5432",
  )
  return connection



def database_insertion_query(db_connection, users_list):
 
  cursor = db_connection.cursor()

  
  cursor.execute("""
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
    """)

  for user in users_list:
    cursor.execute(
        """
            INSERT INTO users (name, surname, email, genre, birth, phone, country, city, state)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            user.name,
            user.surname,
            user.email,
            user.genre,
            user.birth if user.birth else None,
            user.phone,
            user.country,
            user.city,
            user.state,
        ),
    )

  
  db_connection.commit()

  
  cursor.close()
  print(f"Se han insertado {len(users_list)} usuarios correctamente.")



if __name__ == "__main__":
  try:
    print("Conectando a la base de datos...")
    db_conn = database_init_connection()
    print("¡Conexión exitosa.")

    database_insertion_query(db_conn, users)

   
    db_conn.close()
    print("Conexión cerrada.")

  except Exception as e:
    print(f"Ocurrió un error con la base de datos: {e}")