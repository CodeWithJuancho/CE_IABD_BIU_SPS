import csv
import psycopg2
from datetime import datetime

fecha = datetime.now().strftime("%m_%d_%y")
print(fecha)

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

aceptadas = []
rechazadas = []
users = []

#abre csv y lo mete en la variable archivo
with open("users/extracted/users.csv") as archivo:
    #lee el archivo y lo mete en datos
    datos = csv.reader(archivo)
    
    #salto la primera fila porque solo tiene los nombres de las columnas
    cabecera = next(datos)
    
    for fila in datos:
        if len(fila) != 10:
            rechazadas.append(fila)
        else:
            #creo el objeto a partir de los datos de la fila
            usuario = User(*fila[1:])
            
            #compruebo los atributos del objeto
            if (
                   not usuario.name.strip()
                or not usuario.surname.strip()
                or not usuario.email.strip()
                or not usuario.genre.strip()
                or not usuario.birth.strip()
                or not usuario.phone.strip()
                or not usuario.country.strip()
                or not usuario.city.strip()
                or not usuario.state.strip()
            ):
                rechazadas.append(fila)
                
            else:
                aceptadas.append(usuario)
                users.append(usuario)

#archivo rechazadas
with open (f"scripts/logs/{fecha}_rejected_rows.txt", "w") as archivo:
    archivo.write(f"There were {len(rechazadas)} rejected rows.\n")
    for fila in rechazadas:
        archivo.write(", ".join(fila) + "\n")

#archivo aceptadas        
with open (f"scripts/logs/{fecha}_imported_rows.txt", "w") as archivo:
    archivo.write(f"There were {len(aceptadas)} imported rows.\n")
    for usuario in aceptadas:
        archivo.write(f"{usuario.name}, {usuario.surname}, {usuario.email}, {usuario.genre}, {usuario.birth}, {usuario.phone}, {usuario.country}, {usuario.city}, {usuario.state}\n")
        
