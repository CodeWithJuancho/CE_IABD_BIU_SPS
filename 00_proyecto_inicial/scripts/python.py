#!/usr/bin/env python3

import csv
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import pandas as pd

try:
    import psycopg2
except ImportError:  # pragma: no cover
    psycopg2 = None


@dataclass
class User:
    name: str
    surname: str
    email: str
    genre: str
    birth: str
    phone: str
    country: str
    city: str
    state: str


def get_date_string() -> str:
    return datetime.now().strftime("%m_%d_%y")


def find_project_root() -> Path:
    if len(sys.argv) > 1:
        return Path(sys.argv[1]).resolve()
    return Path(__file__).resolve().parent.parent


def database_init_connection():
    if psycopg2 is None:
        print("psycopg2 no está instalado. No se puede conectar a PostgreSQL.")
        return None

    last_error = None
    for port in (5432, 5433):
        try:
            connection = psycopg2.connect(
                host="localhost",
                port=port,
                dbname="postgres",
                user="postgres",
                password="1234",
            )
            print(f"Conexión a PostgreSQL establecida en el puerto {port}.")
            return connection
        except Exception as exc:  # pragma: no cover
            last_error = exc

    print(f"No fue posible conectar con PostgreSQL: {last_error}")
    return None


def ensure_database_schema(db_connection):
    if db_connection is None:
        return

    with db_connection.cursor() as cursor:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
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
        )
    db_connection.commit()


def database_insertion_query(db_connection, users):
    if db_connection is None:
        print("No hay conexión activa a la base de datos; se omite la inserción.")
        return

    try:
        ensure_database_schema(db_connection)
        with db_connection.cursor() as cursor:
            for user in users:
                cursor.execute(
                    """
                    INSERT INTO users (name, surname, email, genre, birth, phone, country, city, state)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """,
                    (
                        user.name,
                        user.surname,
                        user.email,
                        user.genre,
                        user.birth,
                        user.phone,
                        user.country,
                        user.city,
                        user.state,
                    ),
                )
            db_connection.commit()
            print(f"Se insertaron {len(users)} usuarios válidos en PostgreSQL.")
    except Exception as exc:  # pragma: no cover
        db_connection.rollback()
        print(f"Error al insertar usuarios en PostgreSQL: {exc}")
    finally:
        try:
            db_connection.close()
        except Exception:  # pragma: no cover
            pass


def process_users(csv_path: Path, log_dir: Path, current_date: str):
    imported_rows = []
    rejected_rows = []
    valid_records = []

    with csv_path.open("r", encoding="utf-8", newline="") as csv_file:
        reader = csv.reader(csv_file)
        try:
            header = next(reader)
        except StopIteration:
            header = []

        for row in reader:
            normalized = [value.strip() for value in row]
            if len(normalized) != len(header) or any(value == "" for value in normalized):
                rejected_rows.append(row)
                continue

            if len(normalized) < 10:
                rejected_rows.append(row)
                continue

            imported_rows.append(row)
            valid_records.append({
                "id": normalized[0],
                "name": normalized[1],
                "surname": normalized[2],
                "email": normalized[3],
                "genre": normalized[4],
                "birth": normalized[5],
                "phone": normalized[6],
                "country": normalized[7],
                "city": normalized[8],
                "state": normalized[9],
            })

    valid_df = pd.DataFrame(valid_records, columns=[
        "id", "name", "surname", "email", "genre", "birth", "phone", "country", "city", "state"
    ])

    users = [
        User(
            name=row["name"],
            surname=row["surname"],
            email=row["email"],
            genre=row["genre"],
            birth=row["birth"],
            phone=row["phone"],
            country=row["country"],
            city=row["city"],
            state=row["state"],
        )
        for _, row in valid_df.iterrows()
    ]

    rejected_variants = [
        log_dir / f"{current_date}_rejected.txt",
        log_dir / f"{current_date}_rejected_rows.txt",
    ]
    imported_variants = [
        log_dir / f"{current_date}_imported.txt",
        log_dir / f"{current_date}_imported_rows.txt",
    ]

    rejected_content = (
        f"There were {len(rejected_rows)} rejected rows.\n"
        + ("\n".join([",".join(r) for r in rejected_rows]) + "\n" if rejected_rows else "")
    )
    imported_content = (
        f"There were {len(imported_rows)} imported rows.\n"
        + ("\n".join([",".join(r) for r in imported_rows]) + "\n" if imported_rows else "")
    )

    for file_path in rejected_variants:
        file_path.write_text(rejected_content, encoding="utf-8")

    for file_path in imported_variants:
        file_path.write_text(imported_content, encoding="utf-8")

    return imported_rows, rejected_rows, users


def main():
    project_root = find_project_root()
    current_date = get_date_string()
    csv_path = project_root / "users" / "extracted" / "users.csv"
    script_dir = Path(__file__).resolve().parent
    log_dir = script_dir / "logs" if (script_dir / "logs").exists() else project_root / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)

    imported_rows, rejected_rows, users = process_users(csv_path, log_dir, current_date)

    print(f"Imported rows: {len(imported_rows)}")
    print(f"Rejected rows: {len(rejected_rows)}")

    db_connection = database_init_connection()
    database_insertion_query(db_connection, users)


if __name__ == "__main__":
    main()
