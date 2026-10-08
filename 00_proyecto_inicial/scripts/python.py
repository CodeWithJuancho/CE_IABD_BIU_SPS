import pandas as pd
import datetime
import os
import psycopg2
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


# FECHA EN FORMATO MM_DD_YY
fecha_formateada = datetime.datetime.now().strftime("%m_%d_%y")

# Cambiar al directorio del script actual
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Cargar el CSV en un DataFrame de pandas
df = pd.read_csv("../users/extracted/users.csv", encoding="utf-8")

lista_rechazada = []
lista_importada = []
users = []

for _, fila in df.iterrows():
    if fila.isnull().any():
        # Creamos una instancia de tu clase User
        usuario_incompleto = User(
            fila["name"], fila["surname"], fila["email"], 
            fila["genre"], fila["birth"], fila["phone"], 
            fila["country"], fila["city"], fila["state"]
        )
        # Añadimos el objeto a la lista
        lista_rechazada.append(usuario_incompleto)
#
    else:
        # Creamos una instancia de tu clase User
        usuario_completo = User(
            fila["name"], fila["surname"], fila["email"], 
            fila["genre"], fila["birth"], fila["phone"], 
            fila["country"], fila["city"], fila["state"]
        )
        # Añadimos el objeto a la lista
        lista_importada.append(usuario_completo)
        users.append(usuario_completo)
        print(f"Usuario importado: {usuario_completo.name} {usuario_completo.surname}")

print(f"Total de objetos User rechazados: {len(lista_rechazada)}")
print(f"Total de objetos User importados: {len(lista_importada)}")



# 1. Definir la ruta de la carpeta de logs
carpeta_logs = "../logs"

# 2. Crear la carpeta si no existe (exist_ok=True evita errores si ya existía)
os.makedirs(carpeta_logs, exist_ok=True)

# 3. Ahora ya puedes escribir tus archivos de forma segura
with open(f"{carpeta_logs}/{fecha_formateada}_rejected_rows.txt", "w", encoding="utf-8") as f:
    f.write(f"There were {len(lista_rechazada)} rejected rows\n")
    f.write("Rejected Users:\n")
    for usuario in lista_rechazada:
        f.write(f"Name: {usuario.name}, Surname: {usuario.surname}, Email: {usuario.email}, "
                f"Genre: {usuario.genre}, Birth: {usuario.birth}, Phone: {usuario.phone}, "
                f"Country: {usuario.country}, City: {usuario.city}, State: {usuario.state}\n")

with open(f"{carpeta_logs}/{fecha_formateada}_imported_rows.txt", "w", encoding="utf-8") as f:
    f.write(f"There were {len(lista_importada)} imported rows\n")


def database_inertion_query(db_conection, users):
    if db_conection is None:
        print("No hay conexión activa.")
        return
        
    try:
        cursor = db_conection.cursor() #
        for user in users: #
            insert_query = """
                INSERT INTO users (name, surname, email, genre, birth, phone, country, city, state)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """ #
            cursor.execute(insert_query, (user.name, user.surname, user.email,
                                          user.genre, user.birth, user.phone,
                                          user.country, user.city, user.state)) #
        db_conection.commit() #
        print(f"{len(users)} usuarios insertados con éxito.")
    except Exception as e:
        print(f"Error al insertar usuarios en la base de datos: {e}")
    finally:
        cursor.close() #
        db_conection.close()  # <-- FALTA: Cerrar la conexión como pide el PDF
