# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from doctest import Example
from typing import Generator
from src.base.config import settings
import databases
import sqlalchemy

MODE = settings.MODE


if MODE == "prod":
    print("using a SQL DB")
    DATABASE_URL = settings.DATABASE_URL
else:
    print("Using SQLite3")
    DATABASE_URL = "sqlite:///./db.sqlite3"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()


engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)
