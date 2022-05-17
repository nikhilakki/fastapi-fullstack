# Copyright (c) 2022 Nikhil Akki
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

FROM python:3.10-slim as base
RUN apt update && apt upgrade -y
RUN pip install poetry
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser
COPY . .
RUN poetry install
EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]
