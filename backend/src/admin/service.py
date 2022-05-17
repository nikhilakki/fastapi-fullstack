# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from sqlalchemy.orm import Session
from .dto.users import UserCreate
from .entities.users import User
from src.base.hashing import Hasher


class UserService:
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

    @staticmethod
    def update_user(id: int, user: UserCreate, db: Session):
        try:
            user = db.query(User).filter(User.id == id).update(user)
            print(f"{user=}")
            db.execute(user)
            db.refresh(user)
            return user
        except Exception as e:
            print(f"Error {e}")
            return {}

    @staticmethod
    def delete_by_user_id(id: int, db: Session):
        try:
            user = db.query(User).filter(User.id == id).delete()
            return user
        except Exception as e:
            print(f"Error {e}")
            return {}
