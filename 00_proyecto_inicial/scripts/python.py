import csv
from datetime import date
import os


hoy = date.today()
fechahoy=(f"{hoy.month}_{hoy.day}_{hoy.year}")



print(fechahoy)

os.makedirs("scripts/logs", exist_ok=True)

rechazadas = []
importadas = []

with open('users/extracted/users.csv') as csvfile:
    csvreader = csv.reader(csvfile)

    for row in csvreader:

        # Comprobar datos
        if "" in row:
            rechazadas.append(row)
        else:
            importadas.append(row)



# filas rechazadas
with open(f"scripts/logs/{fechahoy}_rejected_rows.txt", "w") as file:
    file.write(f"There were {len(rechazadas)} rejected rows.\n")

    for row in rechazadas:
        file.write(",".join(row) + "\n")


# filas importadas
with open(f"scripts/logs/{fechahoy}_imported_rows.txt", "w") as file:
    file.write(f"Filas importadas: {len(importadas)}\n")

    for row in importadas:
        file.write(",".join(row) + "\n")