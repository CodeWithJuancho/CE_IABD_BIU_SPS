# import necessary libraries
import pandas as pd
import datetime as dt
import psycopg2 

# User class to represent a user in the system
class User:
    def __init__(self, name, surname, email, genre, birth, phone, country, city, state):
        self.name = name
        self.surname = surname
        self.email = email
        self.genre = genre
        self.birth = birth
        self.phone = phone
        self.country = country
        self.city = city
        self.state = state

    def __str__(self):
        return f"{self.name} {self.surname} is a {self.genre} born on {self.birth}."

# Method to add reject rows to a document
def add_rows_to_document(file, rows):
    open(file, 'a').writelines([row + '\n' for row in rows])

# Method to add imported rows to a document
def add_rows_size_to_document(file, rows_size, rows_type):
    open(file, 'w').writelines(f'There were {rows_size} {rows_type} rows.' + '\n')

# Method to establish a connection to the database
def database_init_connection():
    return psycopg2.connect(database = "proyecto0", 
                            user = "admin", 
                            host= 'localhost',
                            password = "admin123",
                            port = 5432)

# Method to insert the users into the database having a connection to the database and a list of users as parameters
def database_insertion_query(db_connection, users):
    # Create a cursor object for executing SQL queries
    cur = db_connection.cursor()
    # Execute a command: create datacamp_courses table
    for user in users:
        cur.execute("INSERT INTO users(name, surname, email, genre, birth, phone, country, city, state) " \
        "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);", (user.name, user.surname, user.email, user.genre, user.birth, user.phone, user.country, user.city, user.state))
    # Make the changes to the database persistent
    db_connection.commit()
    # Close cursor and communication with the database
    cur.close()
    db_connection.close()


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

# Users list to store the users that have been successfully imported
users = []

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
        users.append(User(row['name'], row['surname'], row['email'], row['genre'], row['birth'], row['phone'], row['country'], row['city'], row['state']))

# Write the rejected and imported rows to their respective log files
add_rows_size_to_document(rejected_log_file, len(rejected_rows), "rejected")            
add_rows_to_document(rejected_log_file, rejected_rows)
add_rows_size_to_document(imported_log_file, len(imported_rows), "imported")

# Call the database_insertion_query method to insert the processed users into the database
database_insertion_query(database_init_connection(), users)