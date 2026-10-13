#!/bin/bash

# Obtener la fecha actual con formato mes_dia_año
fecha_hoy=$(date +%m_%d_%Y)

# Mostrar esa fecha por pantalla
echo "Fecha de hoy: $fecha_hoy"

#copiar ../users/exracted/users.csv en la carpeta ../users/processed y la copia debe llamarse fecha_hoy_processed_users.txt
cp ../users/extracted/users.csv ../users/processed/"${fecha_hoy}_processed_users.txt"

# Ejecutar el script Python python.py
: 'python3 python.py'
