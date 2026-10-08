#!/bin/bash
FECHA=$(date +'%m_%d_%Y')
echo $FECHA
cp ../users/extracted/users.csv ../users/processed/${FECHA}_processed_users.txt
python python.py