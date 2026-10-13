# Docker y PostgreSQL

Este documento describe cómo iniciar PostgreSQL con Docker y ejecutar el proceso
de importación de usuarios del proyecto.

## Requisitos

- Docker instalado y en ejecución.
- Python 3 instalado.
- Las dependencias `pandas` y `psycopg2` instaladas en el entorno de Python que
  se vaya a utilizar (`psycopg2-binary` proporciona el módulo `psycopg2`).
- El archivo `00_proyecto_inicial/users/extracted/users.csv` disponible.

## Iniciar PostgreSQL

Desde una terminal, crea e inicia el contenedor:

```bash
docker run -d \
  --name proyecto0 \
  -p 5433:5432 \
  -e POSTGRES_PASSWORD=1234 \
  postgres:16-alpine
```

El puerto `5432` es el puerto de PostgreSQL dentro del contenedor; Docker lo
publica en el puerto `5433` del equipo. El contenedor usa el usuario `postgres`
y la base de datos inicial `postgres`. La contraseña configurada aquí debe
coincidir con la utilizada por `python.py`.

Comprueba que el contenedor está activo y revisa sus mensajes de inicio:

```bash
docker ps --filter name=proyecto0
docker logs proyecto0
```

Espera a que los logs indiquen que el servidor está listo para aceptar
conexiones antes de ejecutar la importación.

Si el contenedor ya existe y está detenido, puedes volver a iniciarlo:

```bash
docker start proyecto0
```

## Ejecutar la importación

Desde la raíz del repositorio:

```bash
bash 00_proyecto_inicial/scripts/bash.sh
```

El proceso:

1. Copia el CSV a `00_proyecto_inicial/users/processed/` con la fecha actual.
2. Valida las filas del CSV y genera logs de filas importadas y rechazadas en
   `00_proyecto_inicial/scripts/logs/`.
3. Intenta conectarse a PostgreSQL en `localhost`, primero por el puerto `5432`
   y después por el `5433`.
4. Crea la tabla `users` si todavía no existe e inserta los usuarios válidos.

La tabla contiene `id`, `name`, `surname`, `email`, `genre`, `birth`, `phone`,
`country`, `city` y `state`. Si no están instaladas las dependencias Python,
instálalas en el entorno que utilizará el script:

```bash
python3 -m pip install pandas psycopg2-binary
```

Si existe el entorno `.venv` en la raíz del repositorio, `bash.sh` lo utiliza.
En ese caso, instala las dependencias con:

```bash
.venv/bin/python -m pip install pandas psycopg2-binary
```

## Comprobar los datos

Abre la consola de PostgreSQL dentro del contenedor:

```bash
docker exec -it proyecto0 psql -U postgres -d postgres
```

En `psql`, comprueba la tabla y el número de registros:

```sql
\dt
SELECT COUNT(*) FROM users;
SELECT id, name, surname, email FROM users LIMIT 10;
```

Para salir:

```text
\q
```

También puedes ejecutar una consulta directamente desde la terminal:

```bash
docker exec proyecto0 psql -U postgres -d postgres \
  -c "SELECT COUNT(*) FROM users;"
```

## Detener y volver a iniciar

Detener el contenedor conserva los datos asociados a él:

```bash
docker stop proyecto0
docker start proyecto0
```

No elimines el contenedor si necesitas conservar la base de datos. La contraseña
del ejemplo es únicamente para desarrollo local; no la uses para un servicio
expuesto o en producción.

## Problemas frecuentes

- **El nombre `proyecto0` ya está en uso:** comprueba con
  `docker ps -a --filter name=proyecto0` si el contenedor está detenido y
  arráncalo con `docker start proyecto0`.
- **No se puede conectar a PostgreSQL:** confirma que Docker está activo, que
  `proyecto0` está ejecutándose, que los logs indican que PostgreSQL está listo
  y que el puerto publicado es `5433`. Comprueba también que las credenciales de
  `python.py` coinciden con las configuradas en el contenedor.
- **Se conecta al puerto equivocado:** el script prueba `5432` antes que
  `5433`. Si ya hay otro servidor PostgreSQL escuchando en `5432`, revisa el
  mensaje de conexión del script para confirmar a qué puerto se conectó.
- **Faltan módulos de Python:** instala `pandas` y `psycopg2-binary` en el
  entorno usado por `bash.sh`.
- **Hay filas rechazadas:** revisa los archivos `*_rejected.txt` y
  `*_rejected_rows.txt` del directorio `logs/`. Se rechazan filas con campos
  vacíos o con un número de columnas distinto al encabezado.
- **Se repite la importación:** cada ejecución inserta de nuevo los usuarios
  válidos; la tabla no evita duplicados.
