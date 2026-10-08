#!/bin/bash
FECHA="$(date +%m-%d-%Y)"
echo "$FECHA"
cp ../users/extracted/users.csv ../users/processed/"$FECHA"_processed_users.txt