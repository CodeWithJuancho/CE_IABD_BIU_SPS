from pathlib import Path
from datetime import datetime
import pandas

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
        
def database_init_connection():
    pass # TODO

def database_insertion_query(db_connection, users):
    pass # TODO

date = datetime.now().strftime("%m_%d_%y")

users_file_path = "../users/extracted/users.csv"
logs_folder_path = "./logs"

imported_rows = list()
rejected_rows = list()

if Path(users_file_path).exists():
    users_file = pandas.read_csv(users_file_path)
    for row in users_file.itertuples(index=False):
        if User.check_row(row):
            imported_rows.append(tuple(row))
        else:
            rejected_rows.append(tuple(row))
        # print(f"{row.id} {User.check_row(row)}")
    
    rejected_logs_file_path = logs_folder_path + "/" + date + "_rejected_rows.txt"
    
    with open(rejected_logs_file_path, "w") as rejected_logs:
        rejected_logs.write(f"There were {len(rejected_rows)} rejeted rows.\n")
        rejected_logs.writelines(f"{row}\n" for row in rejected_rows)

    imported_logs_file_path = logs_folder_path + "/" + date + "_imported_rows.txt"
        
    with open(imported_logs_file_path, "w") as imported_logs:
        imported_logs.write(f"There were {len(imported_rows)} imported rows.\n")
        
