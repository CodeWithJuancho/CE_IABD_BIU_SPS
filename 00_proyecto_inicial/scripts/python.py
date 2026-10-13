from dataclasses import dataclass, astuple, fields
import polars as pl
import datetime
import psycopg2
from psycopg2.extras import execute_values
fechaact = datetime.datetime.now()
fechaform = fechaact.strftime("%m_%d_%y")
print(fechaform)
leecsv = pl.read_csv("../users/extracted/users.csv")
totalmal = leecsv.filter(pl.any_horizontal(pl.all().is_null())).height
mal = leecsv.filter(pl.any_horizontal(pl.all().is_null()))
totalbien = leecsv.filter(pl.all_horizontal(pl.all().is_not_null())).height
bien = leecsv.filter(pl.all_horizontal(pl.all().is_not_null()))

fm = open(f"logs/{fechaform}_rejected_rows.txt", "w")
fm.write(f"There were {totalmal} rejected rows \n")
fm.write(f"\n")
mal.write_csv(fm)
fm.close()

# id,name,surname,email,genre,birth,phone,country,city,state
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
for a in bien.iter_rows(named=True):
    u = User(**a)
    users.append(u)

fb = open(f"logs/{fechaform}_imported_rows.txt", "w")
fb.write(f"There were {totalbien} imported rows \n")
fb.write("\n")
bien.write_csv(fb)
fb.close()

def database_init_connection():
    return psycopg2.connect(
        host=("localhost"),
        port=("5432"),
        dbname=("proyecto0"),
        user=("postgres"),
        password=("1234")
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