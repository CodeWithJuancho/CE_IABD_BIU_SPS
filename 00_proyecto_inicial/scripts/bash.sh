#!/bin/bash

fecha=$(date +"%m_%d_%y")
echo "$fecha"

cp ../users/extracted/users.csv ../users/processed/"$fecha"_processed_users.txt

python3 python.py