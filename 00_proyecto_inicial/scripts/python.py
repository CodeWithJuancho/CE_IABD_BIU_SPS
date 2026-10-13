# 1. Importamos las librerías necesarias
import os
import datetime
import pandas as pd
import psycopg2

# 2. Creamos la clase User para representar a cada usuario
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


# 3. Configuramos rutas y fecha
fecha_formateada = datetime.datetime.now().strftime("%m_%d_%y")
os.chdir(os.path.dirname(os.path.abspath(__file__)))

csv_path = "../users/extracted/users.csv"
carpeta_logs = "../logs"

# 4. Cargamos el CSV y procesamos los registros
df = pd.read_csv(csv_path, encoding="utf-8")

# 5. Creamos listas para almacenar los usuarios rechazados e importados
lista_rechazada = []
lista_importada = []
users = []

for _, fila in df.iterrows():
    usuario = User(
        fila["name"], fila["surname"], fila["email"], 
        fila["genre"], fila["birth"], fila["phone"], 
        fila["country"], fila["city"], fila["state"]
    )
    if fila.isnull().any():
        lista_rechazada.append(usuario)
    else:
        lista_importada.append(usuario)
        users.append(usuario)
        print(f"Usuario importado: {usuario.name} {usuario.surname}")

print(f"Total de objetos User rechazados: {len(lista_rechazada)}")
print(f"Total de objetos User importados: {len(lista_importada)}")

# 6. Generamos los archivos de Log
with open(f"{carpeta_logs}/{fecha_formateada}_rejected_rows.txt", "w", encoding="utf-8") as f:
    f.write(f"There were {len(lista_rechazada)} rejected rows\n")
    f.write("Rejected Users:\n")
    for usuario in lista_rechazada:
        f.write(f"Name: {usuario.name}, Surname: {usuario.surname}, Email: {usuario.email}, "
                f"Genre: {usuario.genre}, Birth: {usuario.birth}, Phone: {usuario.phone}, "
                f"Country: {usuario.country}, City: {usuario.city}, State: {usuario.state}\n")

with open(f"{carpeta_logs}/{fecha_formateada}_imported_rows.txt", "w", encoding="utf-8") as f:
    f.write(f"There were {len(lista_importada)} imported rows\n")


# 7. Creamos la función de conexión a la base de datos
def database_init_connection():
    """
    Establece y retorna una conexión con la base de datos PostgreSQL
    utilizando variables de entorno o valores por defecto.
    """
    try:
        # 8. Declaramos las variables que hemos utilizado para levantar el contenedor de PostgreSQL para conectarnos a la base de datos
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5432"),
            dbname=os.getenv("DB_NAME", "postgres"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD", "1234")
        )
        print("¡Conexión exitosa a la base de datos PostgreSQL!")
        return connection
    except Exception as error:
        print(f"Error al conectar con la base de datos: {error}")
        return None


# 9. Creamos la función de inserción en la base de datos
def database_insertion_query(db_connection, users):
    if db_connection is None:
        print("No hay conexión activa con la base de datos.")
        return
        
    try:
        # 10.Declaramos el cursor y la query de inserción
        cursor = db_connection.cursor()

        # 11. Creamos la query de inserción para la tabla users
        insert_query = """
            INSERT INTO users (name, surname, email, genre, birth, phone, country, city, state)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        #12. Iteramos sobre la lista de usuarios y ejecutamos la query de inserción para cada uno
        for user in users:
            cursor.execute(insert_query, (
                user.name, user.surname, user.email,
                user.genre, user.birth, user.phone,
                user.country, user.city, user.state
            ))
        db_connection.commit()
        print(f"{len(users)} usuarios insertados con éxito en PostgreSQL.")
    except Exception as e:
        print(f"Error al insertar usuarios en la base de datos: {e}")
        db_connection.rollback()
    finally:
        cursor.close()
        db_connection.close()
        print("Conexión a la base de datos cerrada.")


# 13. Ejecutamos la función de conexión y la función de inserción
if __name__ == "__main__":
    conn = database_init_connection()
    if conn:
        database_insertion_query(conn, users)