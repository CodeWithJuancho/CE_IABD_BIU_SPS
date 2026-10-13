# Proceso: PostgreSQL en un contenedor Docker

Documentación del proceso seguido para levantar la base de datos PostgreSQL en un contenedor Docker y conectarla con el script `python.py`.

## 1. Iniciar el contenedor de PostgreSQL

```bash
docker run -d -p 5432:5432 --name proyecto0 -e POSTGRES_PASSWORD=1234 postgres
```

| Opción | Significado |
|---|---|
| `-d` | Ejecuta el contenedor en segundo plano |
| `-p 5432:5432` | Expone el puerto 5432 del contenedor en el 5432 del equipo |
| `--name proyecto0` | Nombre del contenedor |
| `-e POSTGRES_PASSWORD=1234` | Contraseña del usuario `postgres` |
| `postgres` | Imagen oficial de PostgreSQL |

Comprobar que el contenedor está en ejecución:

```bash
docker ps
```

## 2. Comprobar la conexión con PostgreSQL

Comprobación manual:

```bash
docker exec proyecto0 pg_isready -h localhost -U postgres
```

Salida esperada: `localhost:5432 - accepting connections`.

## 3. Crear la tabla `users`

```bash
docker exec -i proyecto0 psql -U postgres <<'EOF'
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
EOF
```

Comprobar que existe:

```bash
docker exec -it proyecto0 psql -U postgres -c "\d users"
```

## 4. Conexión desde Python

`python.py` usa `psycopg2` y los mismos datos del contenedor:

```python
def database_init_connection():
    db_connection = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="1234",
        port="5432"
    )
    return db_connection
```

La función `database_insertion_query(db_connection, users)`:

1. Recibe la conexión y la lista de usuarios válidos.
2. Crea un cursor (`db_connection.cursor()`), el objeto que ejecuta las sentencias SQL.
3. Recorre la lista `users`.
4. Inserta cada usuario en la tabla `users` con `cursor.execute(...)`.
5. Guarda los cambios con `commit`.
6. Cierra el cursor.
7. Cierra la conexión.

En este ejercicio solo se insertan los datos de los usuarios sin datos ausentes. Las filas rechazadas se guardan únicamente en el log.

## 5. Comprobación de los datos insertados

```bash
docker exec -it proyecto0 psql -U postgres -c "SELECT * FROM users;"
```

## 6. Limpieza

Vaciar la tabla y reiniciar el `id`:

```bash
docker exec -it proyecto0 psql -U postgres -c "TRUNCATE TABLE users RESTART IDENTITY;"
```

Parar y borrar el contenedor para empezar de cero:

```bash
docker rm -f proyecto0
```

## 7. Resumen de los comandos ejecutados

Orden completo del proceso, de principio a fin:

```bash
# 1. Iniciar el contenedor de PostgreSQL
docker run -d -p 5432:5432 --name proyecto0 -e POSTGRES_PASSWORD=1234 postgres

# 2. Crear la tabla users
docker exec -i proyecto0 psql -U postgres <<'EOF'
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
EOF

# 3. Ejecutar el flujo completo (copia del CSV, python.py, logs e inserción)
cd scripts
./bash.sh

# 4. Comprobar que solo se han insertado los usuarios válidos
docker exec -it proyecto0 psql -U postgres -c "SELECT * FROM users;"
```

Salida de `bash -x bash.sh` (el modo `-x` muestra cada comando que se ejecuta):
 
```
++ date +%m_%d_%y
+ FECHA=10_13_26
+ echo 'Fecha: 10_13_26'
Fecha: 10_13_26
+ cp ../users/extracted/users.csv ../users/processed 10_13_26_processed_users.txt
+ python3 python.py
programa ejecutado con exito
```
