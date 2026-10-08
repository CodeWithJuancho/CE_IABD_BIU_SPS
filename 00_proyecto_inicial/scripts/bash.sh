#!/bin/bash

date=$(date +%m_%d_%y)
# echo $date
cp ../users/extracted/users.csv ../users/processed/${date}_procesed_users.txt
python3 python.py