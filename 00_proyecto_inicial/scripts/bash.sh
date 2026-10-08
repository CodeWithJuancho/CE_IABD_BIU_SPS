#!/bin/bash
FECHA=$(date +"%d_%m_%y") 

echo $FECHA


cp -i ../users/extracted/users.csv ../users/processed/$FECHA''_processed_users.txt
