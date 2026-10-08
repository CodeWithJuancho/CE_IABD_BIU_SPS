#!/bin/bash

#content=$(cat ../users/extracted/users.csv)
#Extraer las fechas del archivo users.csv y mostrarlas en pantalla
#dates=$(awk -F',' '{print $6}' ../users/extracted/users.csv)
#echo "Fechas extraídas del archivo users.csv:"
#echo "$dates"

fecha=$(awk 'BEGIN {FS=0FS=","} {
    split($2, a, "-");
    $2 = sprintf("%s/%s/%s", a[3], a[2], a[1])
} 1' ../users/extracted/users.csv > ../users/extracted/users_formatted.csv)

content=$(cat ../users/extracted/users_formatted.csv)
echo "Contenido del archivo users_formatted.csv:"
echo "$content"