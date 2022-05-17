# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from .dto.users import UserCreate, ShowUser, UserUpdate
from .service import UserService


router = APIRouter()


@router.get("/")
async def get_all_users():
    users = await UserService.list_users()
    response = [ShowUser.validate(user) for user in users]
    return response


@router.get("/{id}")
async def get_user(
    id: int = Path("id"),
):
    user = await UserService.retreive_user(
        id,
    )
    return dict(response=ShowUser.validate(user))


@router.post("/")
async def create_user(
    user: UserCreate,
):
    new_user = await UserService.create_new_user(
        user,
    )
    response = ShowUser.validate(user)
    return dict(response=response)


@router.patch("/{id}")
async def update_user(
    user: UserUpdate,
    id: int = Path("id"),
):
    response = await UserService.update_user(
        id,
        user,
    )
    return dict(response=response)


@router.delete("/{id}")
async def delete_by_user_id(
    id: int = Path("id"),
):
    response = await UserService.delete_by_user_id(
        id,
    )
    return response
