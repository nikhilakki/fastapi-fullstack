# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from fastapi import FastAPI
from src.base.config import settings
from src.db.session import engine
from src.db.base_class import Base
from src.admin.controller import router as admin_router


def create_tables():
    Base.metadata.create_all(bind=engine)
    print("tables created")


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    app.include_router(admin_router, prefix="/users", tags=["Users"])
    create_tables()
    return app


app = start_application()


@app.get("/")
def health_check():
    return dict(response="Health check success 😃")
