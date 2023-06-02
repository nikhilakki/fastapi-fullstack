# Copyright (c) 2021 Nikhil Akki
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

# Stage 1
FROM python:3.9.6-slim as base
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
# Stage 2
FROM base AS python-deps
RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc
COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy
# Stage 3
FROM base AS python-runtime
COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser
COPY . .
EXPOSE 8000
ENTRYPOINT [ "uvicorn" ]
CMD ["main:app", "--host=0.0.0.0", "--port=8000"]
