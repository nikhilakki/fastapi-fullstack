# Copyright (c) 2021 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import os
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings


MODE = settings.MODE

if MODE == "prod":
    print("using a SQL DB")
    SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
else:
    print("Using SQLite3")
    SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
