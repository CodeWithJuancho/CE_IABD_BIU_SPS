
from datetime import date
from datetime import datetime
from pathlib import Path
import numpy as np
import pandas as pd
import os

fechaActual= date.today()

fechaPartes=(f"{fechaActual.month}_{fechaActual.day}_{fechaActual.year}")
print(fechaPartes)
rutaCsv=Path('/home/gabriel/proyecto/CE_IABD_BIU_SPS/00_proyecto_inicial/users/extracted/users.csv')

df=pd.read_csv(rutaCsv)

filasImportadas=df.dropna()


print(filasImportadas) #Esto devuelve las filas que estan de manera correcta

filasRechazadas=df.loc[df.isnull().any(axis=1)]
print(filasRechazadas) # Source - https://stackoverflow.com/a/62859043
#Filas de los atributos nulos

print(df.isnull().any(axis = 1).sum()) #cantidad de datos nulos

#eliminar archivos si existen





#https://stackoverflow.com/questions/16923281/writing-a-pandas-dataframe-to-csv-file
filasRechazadas.to_csv (f'/home/gabriel/proyecto/CE_IABD_BIU_SPS/00_proyecto_inicial/scripts/logs/{fechaActual}_rejected_rows.txt', index = None, header=True) 
filasImportadas.to_csv (f'/home/gabriel/proyecto/CE_IABD_BIU_SPS/00_proyecto_inicial/scripts/logs/{fechaActual}_imported_rows.txt', index = None, header=True) 
