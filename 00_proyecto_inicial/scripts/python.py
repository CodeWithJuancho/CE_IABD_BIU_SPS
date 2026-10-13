import datetime
from dataclasses import dataclass, astuple, fields
import polars as pl
import psycopg2
from psycopg2.extras import execute_values
fecha = datetime.datetime.now()
Fecha_hoy=fecha.strftime("%m_%d_%Y")

df = pl.read_csv("../users/extracted/users.csv")

filas_rechazadas_df = df.filter(pl.any_horizontal(pl.all().is_null()))
df_importadas = df.drop_nulls()

filas_rechazadas = filas_rechazadas_df.to_dicts()
filas_importadas = df_importadas.to_dicts()

rechazadas = (f"There were {len(filas_rechazadas)} rejected rows. \n \n")
aceptadas = (f"There were {len(filas_importadas)} imported rows. \n \n")

mal = open(f"logs/{Fecha_hoy}_rejected_rows.txt", "w")
bien = open(f"logs/{Fecha_hoy}_imported_rows.txt", "w")

mal.write(rechazadas)
filas_rechazadas_df.write_csv(mal)

bien.write(aceptadas)
df_importadas.write_csv(bien)

@dataclass
class User:
    id: int
    name: str
    surname: str
    email: str
    genre: str
    birth: str
    phone: str
    country: str
    city: str
    state: str

users = []
for a in filas_importadas:
    u = User(**a)
    users.append(u)

def database_init_connection():
    return psycopg2.connect(
        host=("localhost"),
        port=("5432"),
        dbname=("proyecto0"),
        user=("postgres"),
        password=("1234"),
    )
def database_insertion_query(db_connection, users):
    if not users:
        return 0
    col = ", ".join(f.name for f in fields(User))
    query = f"INSERT INTO users ({col}) VALUES %s"
    val = [astuple(u) for u in users]
    try:
        with db_connection.cursor() as cur:
            execute_values(cur, query, val)
        db_connection.commit()
        return len(val)
    except Exception as e:
        db_connection.rollback()
        print(f"Error al insertar los usuarios: {e}")
        return 0

conn = database_init_connection()
insertados = database_insertion_query(conn, users)
print(f"Insertados: {insertados}")
conn.close()
