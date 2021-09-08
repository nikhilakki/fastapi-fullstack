# Copyright (c) 2021 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base_class import Base
from admin.routes import users


def create_tables():
    Base.metadata.create_all(bind=engine)
    print("tables created")


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    app.include_router(users.router, prefix="/api/v1", tags=["Users"])
    create_tables()
    return app


app = start_application()


@app.get("/")
def health_check():
    return dict(response="Health check success 😃")
