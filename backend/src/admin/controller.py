# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from .dto.users import UserCreate, ShowUser
from .service import UserService
from src.db.session import get_db


router = APIRouter()


@router.get("/")
def get_all_users(db: Session = Depends(get_db)):
    users = UserService.list_users(db)
    response = [ShowUser.validate(user) for user in users]
    return response


@router.get("/{id}")
def get_user(id: int = Path("id"), db: Session = Depends(get_db)):
    user = UserService.retreive_user(id, db)
    return dict(response=ShowUser.validate(user))


@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = UserService.create_new_user(user, db)
    response = ShowUser.validate(user)
    return dict(response=response)


@router.patch("/{id}")
def update_user(user: UserCreate, id: int = Path("id"), db: Session = Depends(get_db)):
    response = UserService.update_user(id, user, db)
    print(f"{response=}")
    return dict(response=response)


@router.delete("/{id}")
def delete_user(id: int = Path("id"), db: Session = Depends(get_db)):
    response = UserService.retreive_user(id, db)
    return dict(response=response)


@router.get("/{id}")
def delete_by_user_id(id: int = Path("id"), db: Session = Depends(get_db)):
    response = UserService.delete_by_user_id(id, db)
    return response
