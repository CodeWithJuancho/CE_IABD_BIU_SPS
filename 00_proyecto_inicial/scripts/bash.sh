#!/bin/bash

fecha=$(date '+%d_%m_%Y')
echo $fecha

cp -i  ../users/extracted/users.csv ../users/processed/$fecha''_processed_users.txt
