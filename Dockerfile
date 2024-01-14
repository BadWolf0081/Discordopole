# Basic Docker image for discord Discordopole.
# docker build -t Discordopole.
# docker run --rm -v "$(pwd)"/config:/usr/src/app/config -t Discordopole python3 discordopole.py --init
# docker run --rm -v "$(pwd)"/config:/usr/src/app/config -t Discordopole

# pull official base image
FROM python:3.7-slim

# set work directory
RUN mkdir /usr/src/app
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt .
RUN  python3 -m pip install --upgrade -r requirements.txt

# copy project
COPY . /usr/src/app/