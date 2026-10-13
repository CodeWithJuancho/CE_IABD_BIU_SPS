# CE_IABD_BIU_SPS
This repo will contain the course structure for managing and working with GIt during the whole duration of the scholar year.

### EN
# Python
To process the CSV data, validate rows, generate logs, and connect to PostgreSQL, you need the following Python libraries:
    **`pandas`**       -> To manipulate CSV files.
    **`psycopg2`**: The PostgreSQL adapter for Python, enabling database connections, query execution, and secure insertions.
    **`datetime` & `os`**: Built-in standard Python libraries used for managing file paths, creating log directories, and formatting timestamps (`MM_DD_YY`).

# Python Dependencies Installation
*pip install pandas psycopg2-binary*

# Docker
Ensure the Docker daemon is active on your system:
    *sudo systemctl start docker*

To run the PostgeSQL Container, we should execute the following command to download and run the PostgreSQL container in the Backgrond:
    *sudo docker run --name postgres-container -e POSTGRES_PASSWORD=1234 -p 5432:5432 -d postgres*
        **`--name postgres-container`** Assigns a readable name to your container.
        **`-e POSTGRES_PASSWORD=1234`** Sets 1234 as password for PostgreSQL.
        **`-p 5432:5432`**  Maps port 5432 of the container to your local machine.
        **`-d`** Runs the container in detached mode (in the background).

To vewrify if the container is running, whe should check it with the next command:
    *sudo docker ps*

# Database Schema Initialization
Once the container is running, create the users table where Python will insert the valid records:
    1. Access the PostgreSQL interactive terminal inside the container:
        *sudo docker exec -it postgres-container psql -U postgres*
        
    2. Execute the table creation query:
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            surname VARCHAR(100),
            email VARCHAR(150),
            genre VARCHAR(50),
            birth VARCHAR(50),
            phone VARCHAR(50),
            country VARCHAR(100),
            city VARCHAR(100),
            state VARCHAR(100)
        );

    3. Execute the query to show the data from the database
        Select * from users;


### ES
# Python
Para procesar los datos del CSV, validar filas, generar registros de log y conectar con PostgreSQL, necesitas las siguientes librerías de Python:
    **`pandas`** Para manipular archivos CSV.
    **`psycopg2`** El adaptador de PostgreSQL para Python, que permite realizar conexiones a la base de datos, ejecución de consultas e inserciones seguras.
    **`datetime` & `os`** Librerías estándar integradas de Python utilizadas para gestionar rutas de archivos, crear directorios de logs y formatear marcas de tiempo (`MM_DD_YY`).

# Instalación de Dependencias de Python
*pip install pandas psycopg2-binary*

# Docker
Asegúrate de que Docker esté activo en tu sistema:
    *sudo systemctl start docker*

Para ejecutar el contenedor de PostgreSQL, debemos ejecutar el siguiente comando para descargar y arrancar el contenedor de PostgreSQL en segundo plano:
    *sudo docker run --name postgres-container -e POSTGRES_PASSWORD=1234 -p 5432:5432 -d postgres*
        **`--name postgres-container`** Asigna un nombre legible a tu contenedor.
        **`-e POSTGRES_PASSWORD=1234`** Establece 1234 como contraseña para PostgreSQL.
        **`-p 5432:5432`** Mapea el puerto 5432 del contenedor a tu máquina local.
        **`-d`** Ejecuta el contenedor en modo independiente (en segundo plano).

Para verificar si el contenedor se está ejecutando, debemos comprobarlo con el siguiente comando:
    *sudo docker ps*

# Inicialización del Esquema de la Base de Datos
Una vez que el contenedor esté en marcha, crea la tabla de usuarios donde Python insertará los registros válidos:
1. Accede a la terminal interactiva de PostgreSQL dentro del contenedor:
        *sudo docker exec -it postgres-container psql -U postgres*
        
2. Ejecuta la consulta de creación de la tabla:
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            surname VARCHAR(100),
            email VARCHAR(150),
            genre VARCHAR(50),
            birth VARCHAR(50),
            phone VARCHAR(50),
            country VARCHAR(100),
            city VARCHAR(100),
            state VARCHAR(100)
        );

3. Ejecuta la consulta para mostrar los datos de la base de datos:
        Select * from users;