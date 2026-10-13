# Importar las librerias necesarias para procesar y parsear el archivo .csv
import pandas as pd
import csv

with open("00_proyecto_inicial/users/extracted/users.csv", newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter =',', quotechar='"')
    for fila in lector_csv:
        print(fila)