# Misc

## Virtual Environment

### Create a virtual environment

```bash
# create
python3 -m venv dzhw-3.9

# activate
 dzhw-3.9\Scripts\activate

# check python version == 3.9.12
```

### Create a Jupyter Kernel for the virtual environment

```bash

ipython kernel install --user --name=dzhw-master-thesis

```

## Docker Walkthrough

### Deploying with docker compose

- Check docker compose version

```bash
docker compose version
```

When deploying this setup, the pgAdmin web interface will be available at port 5050 (e.g. <http://localhost:5050>)

```bash
docker compose up -d
```

- List running containers

```bash

docker compose ps

```

- For a elegant shutdown, switch to a different shell run:

```bash
# To stop the containers, run:
docker compose down


# To Delete all data, run:
docker compose down -v
```

or use Ctrl+C in the same shell

## Connect to the database

Connect to Postgres with the following credentials:

- Host: localhost
- Port: 5432
- User: airflow
- Password: airflow

Connect to pgAdmin with the following credentials:

- email: admin@admin.com
- password: airflow

Create a connection in pgadmin and configuration (After logging in):

- Create Server in General Tab
- Connection Tab -> Host: localhost, Port: 5432, Username: airflow, Password: airflow
