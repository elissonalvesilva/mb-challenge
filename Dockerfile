# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
RUN mkdir /script
COPY . /script
RUN rm -rf api/
COPY pyproject.toml /script

WORKDIR /script

ENV PYTHONPATH=${PYTHONPATH}:${PWD}
ENV PROJECT_FOLDER=/script
ENV WORKDIRECTORY_TO_RESULTS=/mb_data
ENV WORKDIRECTORY_TO_RETRY=/mb_data


RUN pip3 install poetry
RUN python -m pip install "pymongo[srv]"
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
