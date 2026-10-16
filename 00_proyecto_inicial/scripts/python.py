# Importar las librerias necesarias para procesar y parsear el archivo .csv
import pandas as pd
import csv
# Libreria para obtener la fecha
from datetime import date

""" with open("00_proyecto_inicial/users/extracted/users.csv", newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter =',', quotechar='"')
    for fila in lector_csv:
        print(fila) """
        
# Obtener la fecha actual
fecha_actual = date.today()

# Modificando la fecha para que tenga el formato "mm-dd-yyyy"
fecha_modificada = fecha_actual.strftime("%m_%d_%Y")

# Imprimiendo la fecha modificada
print("el dia de hoy es:",fecha_modificada)
