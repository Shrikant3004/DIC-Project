import os
from dotenv import load_dotenv

load_dotenv()


# Postgres SQL
PSQL_HOST = os.environ.get("PSQL_HOST")
PSQL_USER = os.environ.get("PSQL_USER")
PSQL_PASSWORD = os.environ.get("PSQL_PASSWORD")
PSQL_DATABASE = os.environ.get("PSQL_DATABASE")