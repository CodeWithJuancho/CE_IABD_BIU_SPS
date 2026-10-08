#!/bin/bash

$date = date +%m_%d_%y
copy ../user/extracted/users.csv ../users/processed/$date_procesed_users.txt
python3 python.py