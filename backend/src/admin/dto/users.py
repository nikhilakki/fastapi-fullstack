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


class UserUpdate(BaseModel):
    username: str = None
    email: EmailStr = None
    is_active: bool = None
    is_superuser: bool = None


class ShowUser(BaseModel):
    id: int = None
    username: str
    email: EmailStr
    is_active: bool = None
    is_superuser: bool = None
