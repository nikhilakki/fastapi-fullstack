# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from sqlalchemy import Column, Table, Integer, String, Boolean
from src.db.session import metadata


User = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("username", String, unique=True, nullable=False),
    Column("email", String, nullable=False, unique=True, index=True),
    Column("hashed_password", String, nullable=False),
    Column("is_active", Boolean(), default=True),
    Column("is_superuser", Boolean(), default=False),
)
