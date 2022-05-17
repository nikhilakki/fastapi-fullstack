# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from fastapi.exceptions import HTTPException
from .dto.users import UserCreate, UserUpdate
from .entities.users import User
from src.base.hashing import Hasher
from src.db.session import database as db


class UserService:
    @staticmethod
    async def retreive_user(id: int):
        user = User.select().filter(User.c.id == id)
        result = await db.fetch_one(user)
        return result

    @staticmethod
    async def list_users():
        user = User.select()
        result = await db.fetch_all(user)
        return result

    @staticmethod
    async def create_new_user(user: UserCreate):
        try:
            new_user = User.insert().values(
                username=user.username,
                email=user.email,
                hashed_password=Hasher.get_password_hash(user.password),
                is_active=True,
                is_superuser=False,
            )
            last_record_id = await db.execute(new_user)
            return last_record_id
        except Exception as e:
            print(f"Error {e}")
            raise HTTPException(500, detail=str(e))
            return {}

    @staticmethod
    async def update_user(id: int, user: UserUpdate):
        try:
            print(f"{user=}")
            update_user = (
                User.update()
                .where(User.c.id == id)
                .values({k: v for k, v in user.dict().items() if v is not None})
            )
            result = await db.execute(update_user)
            return result
        except Exception as e:
            print(f"Error {e}")
            return {}

    @staticmethod
    async def delete_by_user_id(id: int):
        try:
            user = User.delete().where(User.c.id == id)
            return await db.execute(user)
        except Exception as e:
            print(f"Error {e}")
            return {}
