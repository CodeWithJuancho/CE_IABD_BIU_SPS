#!/bin/bash
FECHA=$(date +"%m_%d_%y")

echo "Fecha: $FECHA"

cp ../users/extracted/users.csv ../users/processed/${FECHA}_processed_users.txt

python3 python.py
