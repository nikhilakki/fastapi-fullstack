# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from sqlalchemy.orm import Session
from admin.models.users import User
from admin.schemas.users import UserCreate
from core.hashing import Hasher


class UserController:
    @staticmethod
    def retreive_user(id: int, db: Session):
        user = db.query(User).filter(User.id == id).first()
        return user

    @staticmethod
    def list_users(db: Session):
        users = db.query(User).filter(User.is_active == True).all()
        return users

    @staticmethod
    def create_new_user(user: UserCreate, db: Session):
        try:
            user = User(
                username=user.username,
                email=user.email,
                hashed_password=Hasher.get_password_hash(user.password),
                is_active=True,
                is_superuser=False,
            )
            db.add(user)
            db.commit()
            db.refresh(user)
            return user
        except Exception as e:
            print(f"Error {e}")
            return {}
