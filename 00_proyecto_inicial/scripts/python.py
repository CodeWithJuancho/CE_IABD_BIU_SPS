# import necessary libraries
import pandas as pd
import datetime as dt

# Method to add reject rows to a document
def add_rows_to_document(file, rows):
    open(file, 'a').writelines([row + '\n' for row in rows])

# Method to add imported rows to a document
def add_rows_size_to_document(file, rows_size, rows_type):
    open(file, 'w').writelines(f'There were {rows_size} {rows_type} rows.' + '\n')

# Date variable to be used in the file name
date = dt.datetime.now().strftime("%m_%d_%y")
# Rejected rows log file
rejected_log_file = f"logs/{date}_rejected_rows.txt"
# Rejected rows list to store the rows that have been rejected
rejected_rows = []

# Imported rows log file
imported_log_file = f"logs/{date}_imported_rows.txt"
# Imported rows list to store the rows that have been successfully imported
imported_rows = []

# read the CSV file into a DataFrame
file='../users/extracted/users.csv'
df = pd.read_csv(file)

# Read through the DataFrame and check for missing data 
# and add the rows to the rejected or imported list accordingly
for index, row in df.iterrows():
    row_string=row.to_string()
    if row_string.__contains__("NaN"):
        rejected_rows.append(row.to_string())
    else:    
        imported_rows.append(row.to_string())

add_rows_size_to_document(rejected_log_file, len(rejected_rows), "rejected")            
add_rows_to_document(rejected_log_file, rejected_rows)
add_rows_size_to_document(imported_log_file, len(imported_rows), "imported")

