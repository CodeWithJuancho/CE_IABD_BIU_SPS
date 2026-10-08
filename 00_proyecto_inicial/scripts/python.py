from dataclasses import dataclass
import polars as pl


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
fm.close

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
print(users)

fb = open(f"logs/{fechaform}_imported_rows.txt", "w")
fb.write(f"There were {totalbien} imported rows \n")
fb.write("\n")
bien.write_csv(fb)
fb.close

