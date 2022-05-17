# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import date, datetime


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class ShowUser(BaseModel):
    id: int = None
    username: str
    email: EmailStr
    is_active: bool
    is_superuser: bool

    class Config:
        orm_mode = True
