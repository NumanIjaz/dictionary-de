import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")

POSTGRES_SERVER = os.getenv("POSTGRES_SERVER")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
