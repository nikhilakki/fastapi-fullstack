# Copyright (c) 2021 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import responses
from schemas.users import UserCreate, ShowUser
from apis.controllers.users import UserController
from db.session import get_db


router = APIRouter()


@router.get("/user")
def get_user(id: int, db: Session = Depends(get_db)):
    response = UserController.retreive_user(id, db)
    return dict(response=response)


@router.post("/user")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = UserController.create_new_user(user, db)
    response = ShowUser.validate(user)
    return dict(response=response)


@router.put("/user")
def update_user(id: int, db: Session = Depends(get_db)):
    response = UserController.retreive_user(id, db)
    return dict(response=response)


@router.delete("/user")
def delete_user(id: int, db: Session = Depends(get_db)):
    response = UserController.retreive_user(id, db)
    return dict(response=response)


@router.get("/users")
def get_all_users(db: Session = Depends(get_db)):
    users = UserController.list_users(db)
    response = [ShowUser.validate(user) for user in users]
    return response


@router.get("/users")
def delete_all_users(db: Session = Depends(get_db)):
    response = UserController.list_users(db)
    return response
