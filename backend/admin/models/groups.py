# Copyright (c) 2021 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from db.base_class import Base


class Groups(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    permissions = Column(String, nullable=False, unique=True, index=True)
    create_timestamp = Column(DateTime(timezone=True), default=func.now())
    update_timestamp = Column(DateTime(timezone=True), update=func.now())
