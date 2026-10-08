#!/bin/bash

date=$(date +"%m_%d_%y")
echo date
cp ../users/extracted/users.csv ../users/processed/$(date +"%m_%d_%y")_processed_users.txt
Python python.py
