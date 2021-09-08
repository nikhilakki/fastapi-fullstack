# Copyright (c) 2021 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import date, datetime


class GroupCreate(BaseModel):
    name: str
    permissions: EmailStr


class ShowGroup(BaseModel):
    username: str
    email: EmailStr
    is_active: bool

    class Config:
        orm_mode = True
