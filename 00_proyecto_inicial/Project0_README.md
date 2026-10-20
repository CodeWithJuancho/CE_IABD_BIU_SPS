# Project 0

Process Users File

## Python Script Dependencies
```
sudo apt-get install python3-pandas python3-psycopg2
```

## PostgreSQL Database with docker

### Install Docker

https://docs.docker.com/engine/install/ubuntu/

1. Set up Docker's apt repository.

```
# Add Docker's official GPG key:
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF

sudo apt update
```

2. Install the Docker packages (latest).

```
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

3. Verify that the installation is successful by running the `hello-world` image:

```
sudo docker run hello-world
```

### Create container
```
sudo docker run -d -p 5432:5432 --name proyecto0 -e POSTGRES_PASSWORD=1234 postgres
```

### Star container
Container needs to be started if it is stopped after creating it
```
sudo docker start proyecto0
```


4. Stop container
```
docker stop proyecto0
```

5. Access Database
```
sudo docker exec -it proyecto0 bash
psql -U postgres -d postgres
```

6. PostgreSQL

- List databases: `\l`
- Switch database: `\c postgres`
- List tables: `\dt`

### SQL query
```
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
```
