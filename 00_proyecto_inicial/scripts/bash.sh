#!/bin/bash

# Copies the file from the extracted directory to the processed directory
current_date=$(date +%m_%d_%y)
echo $current_date
cp ../users/extracted/users.csv ../users/processed/${current_date}_processed_users.txt

# Executes the python script that process the .csv file
python python.py
