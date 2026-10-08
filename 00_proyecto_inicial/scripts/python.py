import datetime
from dataclasses import dataclass
import polars as pl
fecha = datetime.datetime.now()
Fecha_hoy=fecha.strftime("%m_%d_%Y")
print (Fecha_hoy)

df = pl.read_csv("../users/extracted/users.csv")

filas_rechazadas_df = df.filter(pl.any_horizontal(pl.all().is_null()))
df_importadas = df.drop_nulls()

filas_rechazadas = filas_rechazadas_df.to_dicts()
filas_importadas = df_importadas.to_dicts()

rechazadas = (f"Total filas rechazadas: {len(filas_rechazadas)}")
aceptadas = (f"Total de filas importadas (válidas): {len(filas_importadas)}")

mal=(f"logs/{Fecha_hoy}_rejected_rows.txt")
bien=(f"logs/{Fecha_hoy}_imported_rows.txt")

filas_rechazadas_df.write_csv(mal)
df_importadas.write_csv(bien)

@dataclass
class user:
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
    u = user(**a)
    users.append(u)
print(users)
