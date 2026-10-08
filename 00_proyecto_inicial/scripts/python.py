import csv
from datetime import datetime

fecha = datetime.now().strftime("%m_%d_%y")
print(fecha)

class Usuario:
    def __init__(self, id, name, surname, email, genre, birth, phone, country, city, state):
        self.id = id
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

#abre csv y lo mete en la variable archivo
with open("users/extracted/users.csv") as archivo:
    #lee el archivo y lo mete en datos
    datos = csv.reader(archivo)
    
    for fila in datos:
        if len(fila) != 10:
            rechazadas.append(fila)
        else:
            for campo in fila:
                if campo == "":
                    print("CAMPO VACIO")
            
print(rechazadas)