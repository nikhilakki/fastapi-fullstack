# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.base.config import settings


MODE = settings.MODE


if MODE == "prod":
    print("using a SQL DB")
    SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
else:
    print("Using SQLite3")
    SQLALCHEMY_DATABASE_URL = "sqlite:///./test.sqlite3"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
