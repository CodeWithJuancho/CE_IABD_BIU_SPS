from pathlib import Path
from datetime import datetime
import pandas
import psycopg2

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

    @staticmethod
    def check_row(row): # return True is the row is ok, or False otherwise
        return  not pandas.isna(row.name) and row.surname and not pandas.isna(row.email) and not pandas.isna(row.genre) and not pandas.isna(row.birth) and not pandas.isna(row.phone) and not pandas.isna(row.country) and not pandas.isna(row.city) and not pandas.isna(row.state)

    @staticmethod
    def from_row(row):
        return User(row.name, row.surname, row.email, row.genre, row.birth, row.phone, row.country, row.city, row.state) if User.check_row(row) else None
        
def database_init_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="1234",
            port=5432  # Puerto predeterminado de PostgreSQL
        )

        # Create users table if it doesn't exist
        cursor = connection.cursor()

        table_users_exists = """
        SELECT EXISTS (
            SELECT 1 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            AND table_name = 'users'
        );
        """

        cursor.execute(table_users_exists)
        exists = cursor.fetchone()[0] # Boolean field

        if not exists:
            create_table_users = """
            CREATE TABLE users(
                id SERIAL PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                surname VARCHAR(50) NOT NULL,
                email VARCHAR(255) NOT NULL,
                genre VARCHAR(20),
                birth DATE,
                phone VARCHAR(20),
                country VARCHAR(50),
                city VARCHAR(50),
                state VARCHAR(50)
            );
            """
            cursor.execute(create_table_users)
            connection.commit()
            cursor.close()

        return connection

    except Exception as error:
        print("Can't connect database: ", error)

def database_insertion_query(db_connection, users):
    insert_users =f"""
    INSERT INTO users (name, surname, email, genre, birth, phone, country, city, state)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    #insert_users += ",\n ".join(f"    ('{user.name}', '{user.surname}', '{user.email}', '{user.genre}', {user.birth}, '{user.phone}', '{user.country}', '{user.city}', '{user.state}')" for user in users)
    cursor = db_connection.cursor()
    users_tuples = [(user.name, user.surname, user.email, user.genre, user.birth, user.phone, user.country, user.city, user.state) for user in users]
    cursor.executemany(insert_users, users_tuples)
    cursor.close()
    db_connection.commit()

date = datetime.now().strftime("%m_%d_%y")

users_file_path = "../users/extracted/users.csv"
logs_folder_path = "./logs"

rejected_rows = list()
users = list()

if Path(users_file_path).exists():
    users_file = pandas.read_csv(users_file_path)
    for row in users_file.itertuples(index=False):
        user = User.from_row(row)
        if user:
            users.append(user)
        else:
            rejected_rows.append(tuple(row))
    
    rejected_logs_file_path = logs_folder_path + "/" + date + "_rejected_rows.txt"
    
    with open(rejected_logs_file_path, "w") as rejected_logs:
        rejected_logs.write(f"There were {len(rejected_rows)} rejeted rows.\n")
        rejected_logs.writelines(f"{row}\n" for row in rejected_rows)

    imported_users = 0
    db_connection = database_init_connection();
    if (db_connection):
        database_insertion_query(db_connection, users)
        imported_users = len(users)
        db_connection.close()
        
    imported_logs_file_path = logs_folder_path + "/" + date + "_imported_rows.txt"
    with open(imported_logs_file_path, "w") as imported_logs:
        imported_logs.write(f"There were {imported_users} imported rows.\n")

        
